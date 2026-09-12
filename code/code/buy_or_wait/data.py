from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

CENT = Decimal("0.01")
ZERO = Decimal(0)
COLUMNS = [
    "request_id", "amount_safe_to_pay", "affordability_status",
    "recommended_payment_method", "payment_plan", "earliest_date_for_full_payment",
    "spending_changes_needed", "decision_explanation",
]


def money(value) -> Decimal:
    if value is None or str(value).strip() == "":
        raise ValueError("Missing monetary amount; evidence is required")
    return Decimal(str(value).replace(",", "")).quantize(CENT, rounding=ROUND_HALF_UP)


def fmt(value: Decimal) -> str:
    return format(value.quantize(CENT), "f").rstrip("0").rstrip(".") if value else "0"


def day(value: str) -> date:
    return date.fromisoformat(value)


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


class Dataset:
    """Only opens the explicitly permitted participant-facing data files."""

    def __init__(self, root: Path, image_facts: Path | None = None):
        self.root = root.resolve()
        self.profiles = {r["user_id"]: r for r in read_csv(root / "financial_profiles.csv")}
        self.events = defaultdict(list)
        self.messages = defaultdict(list)
        self.options = defaultdict(list)
        self.rates = {
            (r["rate_date"], r["from_currency"], r["to_currency"]): Decimal(r["rate"])
            for r in read_csv(root / "exchange_rates.csv")
        }
        facts_path = image_facts or Path(__file__).with_name("image_facts.json")
        self.image_facts = json.loads(facts_path.read_text(encoding="utf-8"))
        self.image_evidence = {}
        for row in read_csv(root / "images.csv"):
            image_id = row["image_id"]
            if not image_id.replace("_", "").isalnum():
                raise ValueError(f"Invalid image identifier {image_id!r}")
            path = root / "media" / "images" / f"{image_id}.png"
            fact = self.image_facts.get(image_id)
            if not path.is_file() or fact is None:
                raise ValueError(f"Missing image or verified extraction for {image_id}")
            if hashlib.sha256(path.read_bytes()).hexdigest() != fact["sha256"]:
                raise ValueError(f"Image {image_id} changed; re-extract and review its amount")
            self.image_evidence[row["related_event_id"]] = {**fact, **row}
        for row in read_csv(root / "financial_events.csv"):
            row = dict(row)
            row["image_id"] = ""
            if not row["amount"]:
                fact = self.image_evidence.get(row["event_id"])
                if fact is None:
                    raise ValueError(f"Unresolved amount: {row['event_id']}")
                if row["currency"] != fact["currency"]:
                    raise ValueError(f"Currency conflict: {row['event_id']}")
                row["amount"] = fact["amount"]
                row["image_id"] = fact["image_id"]
            row["value"] = money(row["amount"])
            if row["value"] < ZERO:
                raise ValueError(f"Negative event amount: {row['event_id']}")
            self.events[row["user_id"]].append(row)
        for row in read_csv(root / "messages.csv"):
            self.messages[row["user_id"]].append(row)
        for row in read_csv(root / "request_payment_options.csv"):
            self.options[row["request_id"]].append(row)

    def convert(self, amount: Decimal, currency: str, home: str, settled: date) -> Decimal:
        if currency == home:
            return amount
        key = (settled.isoformat(), currency, home)
        if key not in self.rates:
            raise ValueError(f"No supplied settlement-date exchange rate for {key}")
        return money(amount * self.rates[key])
