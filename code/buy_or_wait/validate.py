"""Independent contract checks and cash-flow replay before any output is saved."""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from datetime import timedelta
from decimal import Decimal

from .data import COLUMNS, Dataset, ZERO, day, money
from .forecast import month_date

PAYMENT = re.compile(r"^(\d{4}-\d{2}-\d{2}):(\d+(?:\.\d{1,2})?)$")
STATUSES = {"affordable_now", "affordable_with_plan", "affordable_later", "not_affordable"}
METHODS = {"full_payment", "partial_payment", "installments", "wait", "not_recommended"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_plan(value: str):
    if value == "none":
        return []
    result = []
    for entry in value.split("|"):
        match = PAYMENT.fullmatch(entry)
        require(match is not None, f"Malformed payment: {entry!r}")
        result.append((day(match[1]), money(match[2])))
    require(result == sorted(result, key=lambda x: x[0]), "Payments are not chronological")
    require(all(amount > ZERO for _, amount in result), "Payments must be positive")
    return result


def validate_row(data: Dataset, request: dict, row: dict, trace: dict) -> None:
    require(list(row) == COLUMNS, "Wrong output columns or column order")
    require(row["request_id"] == request["request_id"] == trace["request_id"], "Mismatched request IDs")
    amount = money(request["requested_amount"])
    safe = money(row["amount_safe_to_pay"])
    require(ZERO <= safe <= amount, "Safe amount outside requested bounds")
    status, method = row["affordability_status"], row["recommended_payment_method"]
    require(status in STATUSES and method in METHODS, "Unknown status or payment method")
    start = day(request["request_date"])
    end = start + timedelta(days=90)
    deadline = day(request["desired_completion_date"])
    earliest = day(row["earliest_date_for_full_payment"]) if row["earliest_date_for_full_payment"] else None
    profile = data.profiles[request["user_id"]]
    floor = money(profile["minimum_balance_to_keep"])
    opening = money(profile["current_available_balance"])
    allowed = profile["payment_methods_user_will_consider"].split("|")
    payments = parse_plan(row["payment_plan"])
    changes = {}
    events = {e["event_id"]: e for e in data.events[request["user_id"]]}
    recurring = {f["event_id"] for f in trace["flows"] if f["origin"] == "recurring_expense"}
    if row["spending_changes_needed"] != "none":
        actions = row["spending_changes_needed"].split("|")
        require(len(actions) <= 3, "More than three spending changes")
        for action in actions:
            parts = action.split(":")
            require(len(parts) in {2, 3}, "Malformed spending change")
            verb, event_id = parts[:2]
            require(event_id in events and event_id in recurring, "Change does not target a recurring user expense")
            require(event_id not in changes, "Cannot stop and reduce the same expense")
            event = events[event_id]
            category = event["category"]
            require(category not in profile["expense_categories_to_protect"].split("|"), "Protected expense changed")
            require(event["currency"] == profile["home_currency"], "Spending-change currency mismatch")
            if verb == "stop":
                require(len(parts) == 2, "Malformed stop action")
                require(category in profile["expense_categories_user_is_willing_to_stop"].split("|"), "User rejects stopping this category")
                require(event["flexibility"] in {"stoppable", "reducible_or_stoppable"}, "Expense is not stoppable")
                changes[event_id] = ZERO
            else:
                require(verb == "reduce_to" and len(parts) == 3, "Unknown spending action")
                require(category in profile["expense_categories_user_is_willing_to_reduce"].split("|"), "User rejects reducing this category")
                require(event["flexibility"] in {"reducible", "reducible_or_stoppable"}, "Expense is not reducible")
                target = money(parts[2])
                require(target >= money(event["minimum_allowed_amount"]), "Reduction breaches expense floor")
                require(target <= event["value"], "Reduction would increase the historical expense")
                changes[event_id] = target
    if method == "not_recommended":
        require(not payments and not changes and status == "not_affordable", "Invalid fallback decision")
    else:
        require(payments, "Recommended payment plan is empty")
        require(all(start <= d <= min(deadline, end) for d, _ in payments), "Payment outside deadline or forecast")
        require(method in allowed or method == "wait" and "full_payment" in allowed, "User does not accept payment method")
        require(status != "not_affordable", "Recommended plan has a contradictory status")
        total = sum(a for _, a in payments)
        if method == "installments":
            require(status == "affordable_with_plan", "Installments require plan status")
            matches = []
            for option in data.options[request["request_id"]]:
                if option["payment_method"] != "installments":
                    continue
                count = int(option["number_of_payments"])
                first = day(option["first_payment_date"])
                frequency = int(option["payment_frequency_days"] or 0)
                supplied = [(first + timedelta(days=i * frequency), money(option["payment_amount"])) for i in range(count)]
                if payments == supplied and total == money(option["total_payable_amount"]):
                    matches.append(option)
            require(matches, "Installments do not exactly match a supplied offer")
            require(bool(profile["max_installment_months"]), "Installments are disabled")
            require(payments[-1][0] < month_date(payments[0][0], int(profile["max_installment_months"])), "Installment term exceeds user preference")
        else:
            require(total == amount, "Payment total does not equal requested amount")
        if method == "partial_payment":
            require(status == "affordable_with_plan" and request["allows_partial_payment"].lower() == "true", "Partial payment is not allowed")
            require(ZERO < safe < amount and earliest is not None, "Partial payment capacity is invalid")
            require(payments == [(start, safe), (earliest, amount - safe)], "Partial payment must use exactly the prescribed two payments")
        if method == "full_payment":
            require(payments == [(start, amount)], "Immediate full-payment schedule is invalid")
            require(status == ("affordable_with_plan" if changes else "affordable_now"), "Full-payment status is inconsistent")
        if method == "wait":
            require(len(payments) == 1 and payments[0][0] > start and payments[0][1] == amount, "Wait payment is inconsistent")
            if not changes:
                require(earliest is not None and payments == [(earliest, amount)], "Wait date is inconsistent")
            require(status == ("affordable_with_plan" if changes else "affordable_later"), "Wait status is inconsistent")
    if status == "affordable_now":
        require(earliest == start and safe == amount and not changes, "Affordable-now capacity is inconsistent")
    require(bool(row["decision_explanation"].strip()), "Explanation is empty")
    # Independently replay trace facts; never trust a cached planned balance.
    baseline = defaultdict(lambda: ZERO)
    adjusted = defaultdict(lambda: ZERO)
    for flow in trace["flows"]:
        when, value = day(flow["date"]), money(flow["amount"])
        require(start <= when <= end, "Cash flow outside forecast")
        baseline[when] += value
        adjusted[when] += (-changes[flow["event_id"]]
                           if flow["origin"] == "recurring_expense" and flow["event_id"] in changes else value)
    for when, value in payments:
        adjusted[when] -= value
    balance = planned = opening
    values = []
    for offset in range(91):
        when = start + timedelta(days=offset)
        balance += baseline[when]
        planned += adjusted[when]
        values.append((when, balance))
        if payments:
            require(opening >= floor and planned >= floor, f"Minimum balance breached on {when}")
    expected_safe = min(amount, max(ZERO, min(b for _, b in values) - floor)) if opening >= floor else ZERO
    require(safe == expected_safe, "Safe amount differs from independently replayed baseline")
    expected_earliest = None
    prefix_ok = opening >= floor
    for index, (when, balance) in enumerate(values):
        if prefix_ok and min(b for _, b in values[index:]) - amount >= floor:
            expected_earliest = when
            break
        prefix_ok = prefix_ok and balance >= floor
    require(earliest == expected_earliest, "Earliest date differs from baseline forecast")


def validate_all(data, requests, rows, traces):
    identifiers = [r["request_id"] for r in requests]
    require(len(identifiers) == len(set(identifiers)), "Duplicate input request ID")
    require(Counter(identifiers) == Counter(r["request_id"] for r in rows), "Missing or duplicate predictions")
    require(len(traces) == len(rows), "Missing audit traces")
    for request, row, trace in zip(requests, rows, traces):
        try:
            validate_row(data, request, row, trace)
        except (ValueError, KeyError) as error:
            raise ValueError(f"{request['request_id']}: {error}") from error
