"""The public examples are read here only; inference never reads output labels."""
from __future__ import annotations

from decimal import Decimal

from buy_or_wait.data import COLUMNS, money
from buy_or_wait.validate import parse_plan


def score(expected: list[dict], actual: list[dict]) -> dict:
    by_id = {row["request_id"]: row for row in actual}
    fields = COLUMNS[1:-1]
    matches = dict.fromkeys(fields, 0)
    differences = []
    errors = []
    semantic_plans = 0
    for truth in expected:
        prediction = by_id[truth["request_id"]]
        semantic_plans += parse_plan(truth["payment_plan"]) == parse_plan(prediction["payment_plan"])
        bad = {}
        for field in fields:
            same = money(truth[field]) == money(prediction[field]) if field == "amount_safe_to_pay" else truth[field] == prediction[field]
            if same:
                matches[field] += 1
            else:
                bad[field] = {"expected": truth[field], "actual": prediction[field]}
        if bad:
            differences.append({"request_id": truth["request_id"], "differences": bad})
        errors.append(abs(money(truth["amount_safe_to_pay"]) - money(prediction["amount_safe_to_pay"])) / money(truth["requested_amount"]))
    return {"requests": len(expected), "exact_field_matches": matches, "semantic_payment_plan_matches": semantic_plans,
            "mean_safe_amount_error_as_fraction_of_request": float(sum(errors) / len(errors)),
            "differences": differences}
