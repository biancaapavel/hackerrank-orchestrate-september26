from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal
from itertools import combinations, product

from .data import Dataset, ZERO, day, fmt, fmt_money, money
from .forecast import Forecast, build_forecast, month_date


@dataclass
class Candidate:
    method: str
    payments: list[tuple[date, Decimal]]
    changes: dict[str, Decimal]
    actions: list[str]
    option_id: str = ""

    def rank(self):
        # Deadline and safety have already been applied as hard constraints.
        return (bool(self.changes), sum(a for _, a in self.payments), self.payments[0][0],
                len(self.payments), self.option_id, len(self.changes), tuple(self.actions))


def option_schedule(option: dict) -> list[tuple[date, Decimal]]:
    count = int(option["number_of_payments"])
    frequency = int(option["payment_frequency_days"] or 0)
    if count < 1 or count > 1000 or count > 1 and frequency < 1:
        raise ValueError(f"Invalid payment option {option['payment_option_id']}")
    first = day(option["first_payment_date"])
    amount = money(option["payment_amount"])
    plan = [(first + timedelta(days=i * frequency), amount) for i in range(count)]
    if sum(a for _, a in plan) != money(option["total_payable_amount"]):
        raise ValueError(f"Payment option total does not equal its supplied schedule: {option['payment_option_id']}")
    return plan


def spending_options(forecast: Forecast, profile: dict):
    protect = set(profile["expense_categories_to_protect"].split("|"))
    reduce = set(profile["expense_categories_user_is_willing_to_reduce"].split("|"))
    stop = set(profile["expense_categories_user_is_willing_to_stop"].split("|"))
    choices = []
    for recurrence in forecast.recurring:
        event = recurrence.event
        category = event["category"]
        if category in protect or event["currency"] != profile["home_currency"]:
            continue
        alternatives = []
        if category in stop and event["flexibility"] in {"stoppable", "reducible_or_stoppable"}:
            alternatives.append((event["event_id"], ZERO, f"stop:{event['event_id']}"))
        if category in reduce and event["flexibility"] in {"reducible", "reducible_or_stoppable"} and event["minimum_allowed_amount"]:
            lower = money(event["minimum_allowed_amount"])
            if ZERO <= lower < recurrence.amount:
                alternatives.append((event["event_id"], lower, f"reduce_to:{event['event_id']}:{fmt_money(lower)}"))
        if alternatives and recurrence.dates:
            choices.append(alternatives)
    for count in range(1, min(3, len(choices)) + 1):
        for subset in combinations(choices, count):
            for choice in product(*subset):
                yield {event_id: value for event_id, value, _ in choice}, [action for _, _, action in choice]


def solve(data: Dataset, request: dict) -> tuple[dict, dict]:
    forecast = build_forecast(data, request)
    profile = data.profiles[request["user_id"]]
    amount = money(request["requested_amount"])
    if amount <= ZERO:
        raise ValueError("Requested amount must be positive")
    deadline = day(request["desired_completion_date"])
    allowed = set(profile["payment_methods_user_will_consider"].split("|"))
    capacities = forecast.capacities()
    safe_today = min(amount, capacities[0][1])
    earliest = next((when for when, capacity in capacities if capacity >= amount), None)
    schedules = []
    if "full_payment" in allowed:
        schedules.append(("full_payment", [(forecast.start, amount)], ""))
        if earliest and earliest > forecast.start:
            schedules.append(("wait", [(earliest, amount)], ""))
    if ("partial_payment" in allowed and request["allows_partial_payment"].lower() == "true"
            and ZERO < safe_today < amount and earliest and earliest <= deadline):
        schedules.append(("partial_payment", [(forecast.start, safe_today), (earliest, amount - safe_today)], ""))
    if "installments" in allowed and profile["max_installment_months"]:
        maximum = int(profile["max_installment_months"])
        for option in data.options[request["request_id"]]:
            if option["payment_method"] != "installments":
                continue
            plan = option_schedule(option)
            if plan[-1][0] >= month_date(plan[0][0], maximum):
                continue
            schedules.append(("installments", plan, option["payment_option_id"]))
    candidates = []

    def consider(changes, actions):
        for method, payments, option_id in schedules:
            if payments[-1][0] > deadline or payments[0][0] < forecast.start:
                continue
            if forecast.safe(payments, changes):
                candidates.append(Candidate(method, payments, changes, actions, option_id))
        if changes and "full_payment" in allowed:
            changed_date = next((d for d, capacity in forecast.capacities(changes) if capacity >= amount), None)
            if changed_date and forecast.start < changed_date <= deadline:
                candidates.append(Candidate("wait", [(changed_date, amount)], changes, actions))

    consider({}, [])
    if not candidates:
        for changes, actions in spending_options(forecast, profile):
            consider(changes, actions)
    best = min(candidates, key=Candidate.rank) if candidates else None
    currency = profile["home_currency"]
    opening_text = f"{currency} {fmt_money(forecast.opening)} available; protect {fmt_money(forecast.minimum)} minimum."
    if best:
        status = ("affordable_now" if best.method == "full_payment" and not best.changes else
                  "affordable_later" if best.method == "wait" and not best.changes else "affordable_with_plan")
        plan_text = "|".join(f"{when.isoformat()}:{fmt_money(value)}" for when, value in best.payments)
        minimum = min(balance for _, balance in forecast.balances(best.changes, best.payments))
        explanation = (f"{opening_text} Pay {currency} {fmt_money(sum(a for _, a in best.payments))} "
                       f"via {best.method.replace('_', ' ')}; finish {best.payments[-1][0]}. "
                       f"Forecast low {fmt_money(minimum)} through {forecast.end}.")
        if best.actions:
            explanation += " Apply " + ", ".join(best.actions) + "."
    else:
        status = "not_affordable"
        plan_text = "none"
        explanation = f"{opening_text} Safe today: {fmt(safe_today)}. No accepted plan completes the request by {deadline} while preserving the minimum for 90 days."
        if earliest:
            explanation += f" Financial capacity for full payment exists on {earliest}."
    if forecast.evidence.references:
        explanation += " Evidence: " + ",".join(forecast.evidence.references) + "."
    next_income = next((f for f in forecast.flows if f.amount > ZERO), None)
    if next_income:
        explanation += f" Next supported income: {fmt_money(next_income.amount)} on {next_income.date}."
    output = {
        "request_id": request["request_id"], "amount_safe_to_pay": fmt(safe_today),
        "affordability_status": status, "recommended_payment_method": best.method if best else "not_recommended",
        "payment_plan": plan_text, "earliest_date_for_full_payment": earliest.isoformat() if earliest else "",
        "spending_changes_needed": "|".join(best.actions) if best else "none", "decision_explanation": explanation,
    }
    if best and not best.actions:
        output["spending_changes_needed"] = "none"
    trace = {
        "request_id": request["request_id"], "forecast_end": forecast.end.isoformat(),
        "opening_balance": fmt(forecast.opening), "minimum_balance": fmt(forecast.minimum),
        "salary_mode": forecast.evidence.salary_mode, "evidence_ids": forecast.evidence.references,
        "unparsed_message_ids": forecast.evidence.ignored, "selected_option_id": best.option_id if best else None,
        "flows": [{"date": f.date.isoformat(), "amount": fmt(f.amount), "event_id": f.event_id,
                   "category": f.category, "origin": f.origin} for f in forecast.flows],
        "baseline_balances": [{"date": d.isoformat(), "balance": fmt(b)} for d, b in forecast.balances()],
        "planned_balances": [{"date": d.isoformat(), "balance": fmt(b)} for d, b in forecast.balances(best.changes, best.payments)] if best else [],
        "image_evidence_ids": [e["image_id"] for e in data.events[request["user_id"]] if e["image_id"]],
    }
    return output, trace
