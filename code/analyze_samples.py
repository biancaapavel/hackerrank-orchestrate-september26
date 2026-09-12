#!/usr/bin/env python3
"""Explain public-example errors; never imported by prediction code.

python3 code/analyze_samples.py --output evaluation/sample_errors.md
python3 code/analyze_samples.py --request-id request_10
"""
from __future__ import annotations

import argparse
import json
import statistics
from collections import Counter, defaultdict
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

from buy_or_wait.data import COLUMNS, Dataset, ZERO, day, fmt, money, read_csv
from buy_or_wait.forecast import build_forecast
from buy_or_wait.planner import solve
from buy_or_wait.validate import parse_plan, validate_all
from evaluation.score import score

FIELDS = COLUMNS[1:-1]


def running_balances(request: dict, prediction: dict, trace: dict) -> list[dict]:
    """Replay trace flows, including an expected-safe-amount counterfactual."""
    start, end = day(request["request_date"]), day(trace["forecast_end"])
    floor = money(trace["minimum_balance"])
    changes = {}
    if prediction["spending_changes_needed"] != "none":
        for action in prediction["spending_changes_needed"].split("|"):
            parts = action.split(":")
            changes[parts[1]] = ZERO if parts[0] == "stop" else money(parts[2])
    daily = defaultdict(lambda: ZERO)
    adjusted = defaultdict(lambda: ZERO)
    ids = defaultdict(list)
    payments = defaultdict(lambda: ZERO)
    for flow in trace["flows"]:
        when, value = day(flow["date"]), money(flow["amount"])
        daily[when] += value
        adjusted[when] += (-changes[flow["event_id"]]
                           if flow["origin"] == "recurring_expense" and flow["event_id"] in changes
                           else value)
        ids[when].append(flow["event_id"])
    for when, amount in parse_plan(prediction["payment_plan"]):
        payments[when] += amount
    baseline = planned = money(trace["opening_balance"])
    expected_safe = money(request["amount_safe_to_pay"])
    rows = []
    for offset in range((end - start).days + 1):
        when = start + timedelta(days=offset)
        baseline += daily[when]
        planned += adjusted[when] - payments[when]
        rows.append({"day": offset, "date": when.isoformat(), "net_flow": fmt(daily[when]),
                     "baseline": fmt(baseline), "headroom": fmt(baseline - floor),
                     "after_expected_safe_today": fmt(baseline - expected_safe),
                     "recommended_plan_balance": fmt(planned), "payment": fmt(payments[when]),
                     "event_ids": ids[when]})
    # Catch stale or incomplete traces rather than showing misleading tables.
    if [{"date": r["date"], "balance": r["baseline"]} for r in rows] != trace["baseline_balances"]:
        raise ValueError(f"{request['request_id']}: trace baseline does not replay")
    if trace["planned_balances"] and [
        {"date": r["date"], "balance": r["recommended_plan_balance"]} for r in rows
    ] != trace["planned_balances"]:
        raise ValueError(f"{request['request_id']}: trace plan does not replay")
    return rows


def diagnose(data: Dataset, request: dict, prediction: dict, trace: dict) -> dict:
    inputs = {k: v for k, v in request.items() if k not in COLUMNS[1:]}
    forecast = build_forecast(data, inputs)
    events = {e["event_id"]: e for e in data.events[request["user_id"]]}
    recurring = []
    for recurrence in forecast.recurring:
        history = [events[event_id] for event_id in recurrence.evidence_ids]
        values = [e["value"] for e in history]
        dates = [day(e["settlement_date"]) for e in history]
        recurring.append({"event_id": recurrence.event["event_id"],
                          "category": recurrence.event["category"],
                          "description": recurrence.event["description"],
                          "flexibility": recurrence.event["flexibility"],
                          "currency": recurrence.event["currency"],
                          "amount": fmt(recurrence.amount), "history_count": len(history),
                          "months": len({(d.year, d.month) for d in dates}),
                          "mean": str(statistics.mean(values)), "median": str(statistics.median(values)),
                          "min": fmt(min(values)), "max": fmt(max(values)),
                          "gaps": dict(Counter(str((b - a).days) for a, b in zip(dates, dates[1:]))),
                          "dates": [d.isoformat() for d in recurrence.dates],
                          "history": [{"event_id": e["event_id"], "date": e["settlement_date"],
                                       "amount": fmt(e["value"]), "description": e["description"]} for e in history]})
    balances = running_balances(request, prediction, trace)
    trough = min(balances, key=lambda r: money(r["baseline"]))
    expected = money(request["amount_safe_to_pay"])
    actual = money(prediction["amount_safe_to_pay"])
    return {"request": inputs, "profile": data.profiles[request["user_id"]],
            "comparisons": {field: {"expected": request[field], "actual": prediction[field],
                                    "match": (money(request[field]) == money(prediction[field])
                                              if field == "amount_safe_to_pay" else request[field] == prediction[field])}
                            for field in FIELDS},
            "signed_safe_amount_error": fmt(actual - expected),
            "normalized_absolute_error": str(abs(actual - expected) / money(request["requested_amount"])),
            "trough": trough, "salary_mode": trace["salary_mode"],
            "evidence_ids": trace["evidence_ids"], "unparsed_message_ids": trace["unparsed_message_ids"],
            "messages": [m for m in data.messages[request["user_id"]]
                         if m["sent_at"][:10] <= request["request_date"]
                         and (not m["request_id"] or m["request_id"] == request["request_id"])],
            "recurrences": recurring,
            "events": [{k: fmt(v) if isinstance(v, Decimal) else v for k, v in e.items()}
                       for e in events.values()],
            "flows": [{**f, "description": events.get(f["event_id"], {}).get("description", "Evidence-backed income")}
                      for f in trace["flows"]],
            "balances": balances}


def table(headers, rows) -> str:
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", " ") or "(empty)"
    return "\n".join(["| " + " | ".join(map(cell, headers)) + " |",
                      "| " + " | ".join("---" for _ in headers) + " |",
                      *("| " + " | ".join(map(cell, row)) + " |" for row in rows)])


def render(records: list[dict], metrics: dict, summary_only: bool = False) -> str:
    lines = ["# Public-sample error report", "",
             "Diagnostic use only: labels are never loaded by full-dataset inference.", "",
             f"Samples: {metrics['requests']}. Mean absolute safe-amount error / requested amount: "
             f"{metrics['mean_safe_amount_error_as_fraction_of_request']:.8%}.", "",
             table(["Field", "Exact matches"], metrics["exact_field_matches"].items()), "",
             "Signed errors below are actual minus expected, in each user's home currency.", "",
             table(["Request", "Expected safe", "Actual safe", "Error", "Absolute / request", "Trough day", "Trough headroom", "Salary mode"],
                   [(r["request"]["request_id"], r["comparisons"]["amount_safe_to_pay"]["expected"],
                     r["comparisons"]["amount_safe_to_pay"]["actual"], r["signed_safe_amount_error"],
                     f"{Decimal(r['normalized_absolute_error']):.4%}", r["trough"]["day"],
                     r["trough"]["headroom"], r["salary_mode"] or "historical") for r in records])]
    if summary_only:
        return "\n".join(lines) + "\n"
    for r in records:
        req, p = r["request"], r["profile"]
        lines += ["", f"## {req['request_id']} â€” {req['user_id']} ({p['home_currency']})", "",
                  f"Request: {req['requested_amount']} on {req['request_date']}; deadline {req['desired_completion_date']}. "
                  f"Opening {p['current_available_balance']}; minimum {p['minimum_balance_to_keep']}.", "",
                  table(["Field", "Expected", "Actual", "Match"],
                        [(f, v["expected"], v["actual"], "yes" if v["match"] else "NO") for f, v in r["comparisons"].items()]), "",
                  f"Baseline trough: day {r['trough']['day']} ({r['trough']['date']}), "
                  f"balance {r['trough']['baseline']}, headroom {r['trough']['headroom']}.", "",
                  f"Protected: {p['expense_categories_to_protect']}. Reduce: {p['expense_categories_user_is_willing_to_reduce']}. "
                  f"Stop: {p['expense_categories_user_is_willing_to_stop']}.", "",
                  f"Salary mode: {r['salary_mode'] or 'historical'}. Evidence: {', '.join(r['evidence_ids']) or 'none'}. "
                  f"Unparsed messages: {', '.join(r['unparsed_message_ids']) or 'none'}.", ""]
        for m in r["messages"]:
            lines += [f"- {m['message_id']} ({m['source_type']}, {m['sent_at']}): {m['message_text']}"]
        lines += ["", "### Recurrence assumptions", "",
                  table(["Event", "Category / description", "N / months", "Mean", "Median", "Range", "Reserve", "Future dates"],
                        [(c["event_id"], c["category"] + " / " + c["description"], f"{c['history_count']} / {c['months']}",
                          c["mean"], c["median"], f"{c['min']}â€“{c['max']}", c["amount"], ", ".join(c["dates"]))
                         for c in r["recurrences"]]), "", "### Full flow list from trace", "",
                  table(["Date", "Amount", "Event", "Category", "Origin", "Description"],
                        [(f["date"], f["amount"], f["event_id"], f["category"], f["origin"], f["description"]) for f in r["flows"]]),
                  "", "### Daily running balances", "",
                  "Expected-safe column subtracts the sample's safe amount today with no spending changes. "
                  "Plan column replays the actual recommendation; for `none` it equals the baseline.", "",
                  table(["Day", "Date", "Net flow", "Baseline", "Headroom", "After expected safe", "After plan", "Plan payment", "Events"],
                        [(b["day"], b["date"], b["net_flow"], b["baseline"], b["headroom"],
                          b["after_expected_safe_today"], b["recommended_plan_balance"], b["payment"], ", ".join(b["event_ids"]))
                         for b in r["balances"]])]
    return "\n".join(lines) + "\n"


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=root / "dataset")
    parser.add_argument("--request-id", action="append", help="Repeat to inspect several public examples")
    parser.add_argument("--output", type=Path, help="Write Markdown here instead of stdout")
    parser.add_argument("--json", type=Path, help="Also save machine-readable diagnostics and source history")
    parser.add_argument("--summary-only", action="store_true")
    args = parser.parse_args()
    data = Dataset(args.dataset)
    requests = read_csv(args.dataset / "sample_requests.csv")
    if args.request_id:
        unknown = set(args.request_id) - {r["request_id"] for r in requests}
        if unknown:
            parser.error(f"Unknown public sample IDs: {', '.join(sorted(unknown))}")
        requests = [r for r in requests if r["request_id"] in args.request_id]
    rows, traces = [], []
    for request in requests:
        inputs = {k: v for k, v in request.items() if k not in COLUMNS[1:]}
        row, trace = solve(data, inputs)
        rows.append(row)
        traces.append(trace)
    validate_all(data, requests, rows, traces)
    metrics = score(requests, rows)
    records = [diagnose(data, req, row, trace) for req, row, trace in zip(requests, rows, traces)]
    report = render(records, metrics, args.summary_only)
    for path, content in [(args.output, report),
                          (args.json, json.dumps({"metrics": metrics, "samples": records}, indent=2) + "\n")]:
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if args.output:
        print(f"Wrote diagnostics for {len(records)} public samples to {args.output}")
    else:
        print(report, end="")


if __name__ == "__main__":
    main()
