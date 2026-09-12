from __future__ import annotations

import calendar
import statistics
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, timedelta
from decimal import Decimal, ROUND_CEILING

from .data import Dataset, ZERO, day, money
from .evidence import Evidence, extract


def month_date(value: date, shift: int, anchor: int | None = None) -> date:
    total = value.year * 12 + value.month - 1 + shift
    year, month0 = divmod(total, 12)
    month = month0 + 1
    return date(year, month, min(anchor or value.day, calendar.monthrange(year, month)[1]))


def percentile(values: list[Decimal], fraction: float = .75) -> Decimal:
    ordered = sorted(values)
    position = Decimal(str(fraction)) * (len(ordered) - 1)
    lo = int(position)
    hi = min(lo + 1, len(ordered) - 1)
    return money(ordered[lo] + (ordered[hi] - ordered[lo]) * (position - lo))


@dataclass(frozen=True)
class Flow:
    date: date
    amount: Decimal  # credits positive; debits negative
    event_id: str
    category: str
    description: str
    origin: str


@dataclass
class Recurrence:
    event: dict
    amount: Decimal
    dates: list[date]
    evidence_ids: list[str]


@dataclass
class Forecast:
    start: date
    end: date
    opening: Decimal
    minimum: Decimal
    flows: list[Flow]
    recurring: list[Recurrence]
    evidence: Evidence
    notes: list[str] = field(default_factory=list)

    def balances(self, changes: dict[str, Decimal] | None = None, payments=()) -> list[tuple[date, Decimal]]:
        """Known same-day credits settle before bills and proposed payments.

        All amounts are posted to that day's closing checkpoint. With credits
        first and all debits nonnegative, the daily close is the day's low after
        settlement. The opening snapshot and every earlier day are protected.
        """
        changes = changes or {}
        totals = defaultdict(lambda: ZERO)
        for flow in self.flows:
            value = flow.amount
            if flow.origin == "recurring_expense" and flow.event_id in changes:
                value = -changes[flow.event_id]
            totals[flow.date] += value
        for when, amount in payments:
            totals[when] -= amount
        balance = self.opening
        result = []
        for n in range((self.end - self.start).days + 1):
            when = self.start + timedelta(days=n)
            balance += totals[when]
            result.append((when, balance))
        return result

    def safe(self, payments=(), changes=None) -> bool:
        if any(d < self.start or d > self.end or amount <= ZERO for d, amount in payments):
            return False
        # Opening balance is already the snapshot available for this request.
        return self.opening >= self.minimum and min(b for _, b in self.balances(changes, payments)) >= self.minimum

    def capacities(self, changes=None) -> list[tuple[date, Decimal]]:
        path = self.balances(changes)
        suffix = Decimal("Infinity")
        result = []
        prefix_safe = []
        running = self.opening >= self.minimum
        for _, balance in path:
            prefix_safe.append(running)
            running = running and balance >= self.minimum
        for i in range(len(path) - 1, -1, -1):
            when, balance = path[i]
            suffix = min(suffix, balance)
            capacity = max(ZERO, suffix - self.minimum) if prefix_safe[i] else ZERO
            result.append((when, capacity))
        return list(reversed(result))


def deduplicate(events: list[dict]) -> list[dict]:
    """Linked sales/refunds remain distinct; superseded authorizations do not."""
    by_id = {e["event_id"]: e for e in events}
    removed = set()
    for event in events:
        earlier = by_id.get(event["linked_event_id"])
        if not earlier:
            continue
        same_direction = event["direction"] == earlier["direction"]
        is_authorization = "authorization" in earlier["description"].lower()
        if same_direction and is_authorization and event["status"] == "settled":
            removed.add(earlier["event_id"])
    seen = set()
    result = []
    for event in events:
        if event["event_id"] in removed or event["event_id"] in seen:
            continue
        seen.add(event["event_id"])
        result.append(event)
    return result


def infer_expenses(events: list[dict], start: date, end: date, evidence: Evidence) -> list[Recurrence]:
    history = [e for e in events if e["direction"] == "debit" and e["status"] == "settled"
               and day(e["settlement_date"]) < start and not e["image_id"] and not e["linked_event_id"]]
    groups = defaultdict(list)
    for e in history:
        # Frequent essential purchases form a category budget across merchants.
        key = (e["category"], e["flexibility"], "") if e["category"] in {"groceries", "transport", "dining"} else (e["category"], e["flexibility"], e["description"])
        groups[key].append(e)
    result = []
    for _, rows in sorted(groups.items()):
        rows.sort(key=lambda e: (e["settlement_date"], e["event_id"]))
        unique = {e["settlement_date"]: e for e in rows}
        rows = list(unique.values())
        # Irregular discretionary meals across unrelated merchants do not prove
        # a fixed commitment. An explicitly reducible category is a budget.
        if (rows[-1]["category"] == "dining" and rows[-1]["flexibility"] == "fixed") or len(rows) < 3:
            continue
        dates = [day(e["settlement_date"]) for e in rows]
        last = rows[-1]
        anchor = statistics.mode([d.day for d in dates])
        monthly = len({(d.year, d.month) for d in dates}) >= 3 and sum(d.day == anchor for d in dates) / len(dates) >= .8
        gaps = [(b - a).days for a, b in zip(dates, dates[1:])]
        interval, count = Counter(gaps).most_common(1)[0]
        if not monthly and (len(rows) < 5 or count / len(gaps) < .65 or interval < 3 or interval > 31):
            continue
        if (start - dates[-1]).days > (45 if monthly else interval * 2 + 5):
            continue
        values = [e["value"] for e in rows]
        # Pool the history instead of repeating a high individual bill for every
        # future period. Preserve actual cadence and round reserves upward.
        amount = statistics.mean(values).quantize(Decimal("0.01"), rounding=ROUND_CEILING)
        if last["category"] == "rent":
            amount = money(amount * evidence.rent_multiplier)
        next_dates = []
        if monthly:
            for shift in range(0, 5):
                when = month_date(start, shift, anchor)
                if start <= when <= end:
                    next_dates.append(when)
        else:
            when = dates[-1] + timedelta(days=interval)
            while when <= end:
                if when >= start:
                    next_dates.append(when)
                when += timedelta(days=interval)
        result.append(Recurrence(last, amount, next_dates, [e["event_id"] for e in rows]))
    return result


def salary_flows(events: list[dict], evidence: Evidence, start: date, end: date, data: Dataset, home: str) -> list[Flow]:
    salaries = sorted([e for e in events if e["category"] == "salary" and e["direction"] == "credit" and not e["image_id"]
                       and e["status"] in {"settled", "scheduled"}], key=lambda e: (e["settlement_date"], e["event_id"]))
    stable_words = ("payroll", "base salary", "household salary", "salary")
    eligible = [e for e in salaries if any(w in e["description"].lower() for w in stable_words)
                and not any(w in e["description"].lower() for w in ("arrears", "bonus", "commission", "before leave", "previous employer", "final employer"))]
    mode = evidence.salary_mode
    if mode in {"ended", "unconfirmed_gig"} or any("Final employer payroll" == e["description"] for e in salaries):
        return []
    if mode == "one_time_invoice":
        if evidence.salary_amount is None or evidence.salary_date is None:
            raise ValueError("Confirmed invoice lacks amount or settlement date")
        when = evidence.salary_date
        if start <= when <= end:
            value = data.convert(evidence.salary_amount, evidence.salary_currency, home, when)
            return [Flow(when, value, "|".join(evidence.references), "salary", "Confirmed invoice only", "confirmed_income")]
        return []
    if not eligible and evidence.salary_amount is None:
        return []
    last = eligible[-1] if eligible else None
    past = [e for e in eligible if day(e["settlement_date"]) < start]
    if last and len(past) < 2 and last["status"] != "scheduled" and mode is None:
        return []
    amount = last["value"] if last else evidence.salary_amount
    currency = last["currency"] if last else evidence.salary_currency
    if evidence.salary_amount is not None:
        # A generic confirmation is not an explicit raise. When confirmed base
        # pay conflicts with net settled base pay, retain the safer amount.
        amount = (min(amount, evidence.salary_amount)
                  if last and currency == evidence.salary_currency and mode in {"base_only", "remaining"}
                  else evidence.salary_amount)
        currency = evidence.salary_currency
    anchor = evidence.salary_date.day if evidence.salary_date else (day(last["settlement_date"]).day if last else 15)
    # One documented salary stream replaces its historical and scheduled copies.
    result = []
    for shift in range(0, 5):
        when = month_date(start, shift, anchor)
        if not start <= when <= end:
            continue
        if evidence.salary_date and when < evidence.salary_date:
            continue
        value = data.convert(amount, currency, home, when)
        result.append(Flow(when, value, last["event_id"] if last else "|".join(evidence.references),
                           "salary", "Recurring confirmed salary", "recurring_income"))
    return result


def build_forecast(data: Dataset, request: dict) -> Forecast:
    profile = data.profiles[request["user_id"]]
    start = day(request["request_date"])
    end = start + timedelta(days=90)
    evidence = extract(data.messages[request["user_id"]], request)
    events = deduplicate(data.events[request["user_id"]])
    recurring = infer_expenses(events, start, end, evidence)
    home = profile["home_currency"]
    flows = salary_flows(events, evidence, start, end, data, home)
    for recurrence in recurring:
        for when in recurrence.dates:
            value = data.convert(recurrence.amount, recurrence.event["currency"], home, when)
            flows.append(Flow(when, -value, recurrence.event["event_id"], recurrence.event["category"], recurrence.event["description"], "recurring_expense"))
    for event in events:
        if event["status"] in {"failed", "cancelled", "unrealized"} or event["direction"] == "non_cash":
            continue
        if event["direction"] == "credit" and event["status"] == "pending":
            continue
        if event["category"] == "salary":
            continue
        settled = day(event["settlement_date"] or event["event_date"])
        if settled < start and event["status"] == "settled":
            continue  # Historical cash is already included in the opening balance.
        when = max(start, settled)
        if when > end:
            continue
        value = data.convert(event["value"], event["currency"], home, settled)
        sign = -1 if event["direction"] == "debit" else 1
        # An explicit same bill/date replaces a forecast copy, not a different bill.
        flows = [f for f in flows if not (f.origin == "recurring_expense" and f.date == when and f.description == event["description"])]
        flows.append(Flow(when, sign * value, event["event_id"], event["category"], event["description"], "explicit_event"))
    flows.sort(key=lambda f: (f.date, -f.amount, f.event_id))
    return Forecast(start, end, money(profile["current_available_balance"]), money(profile["minimum_balance_to_keep"]), flows, recurring, evidence)
