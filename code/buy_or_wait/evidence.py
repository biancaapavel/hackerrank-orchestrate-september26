"""Narrow bilingual fact extraction. Message text is never executed as instructions."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

from .data import day, money

MONEY_RE = re.compile(r"\b(INR|ZAR|IDR|USD|EUR)\s+([\d,]+(?:\.\d+)?)", re.I)
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")


@dataclass
class Evidence:
    salary_amount: Decimal | None = None
    salary_currency: str | None = None
    salary_date: date | None = None
    salary_mode: str | None = None
    rent_multiplier: Decimal = Decimal(1)
    references: list[str] = field(default_factory=list)
    ignored: list[str] = field(default_factory=list)


def extract(messages: list[dict], request: dict) -> Evidence:
    result = Evidence()
    for row in sorted(messages, key=lambda r: (r["sent_at"], r["message_id"])):
        if row["sent_at"][:10] > request["request_date"]:
            continue
        if row["request_id"] and row["request_id"] != request["request_id"]:
            continue
        # A one-to-one transaction message does not redefine the salary stream.
        if row["related_event_id"]:
            result.references.append(row["message_id"])
            continue
        text = row["message_text"].lower()
        amounts = MONEY_RE.findall(row["message_text"])
        dates = DATE_RE.findall(row["message_text"])
        source = row["source_type"]
        mode = None
        if source == "employer":
            if any(s in text for s in ("employment has ended", "seasonal contract has ended", "kontrak musiman saat ini telah berakhir", "hubungan kerja anda telah berakhir")):
                mode = "ended"
            elif any(s in text for s in ("salary has increased", "gaji bulanan anda naik")):
                mode = "increase"
            elif "now expected on" in text or "kini diperkirakan masuk" in text:
                mode = "delay"
            elif "temporary monthly pay" in text or "gaji bulanan sementara" in text:
                mode = "temporary"
            elif "next salary is reduced" in text or "gaji berikutnya dikurangi" in text:
                mode = "reduced"
            elif "base salary" in text or "gaji pokok" in text:
                mode = "base_only"
            elif "remaining confirmed monthly salary" in text or "sisa gaji bulanan" in text:
                mode = "remaining"
            elif "resumes on" in text or "gaji rutin" in text and "kembali" in text:
                mode = "resumed"
            elif "first salary" in text or "gaji pertama" in text:
                mode = "new_job"
            elif "regular salary for the next payroll" in text or "gaji rutin anda untuk penggajian" in text:
                mode = "regular_only"
            elif "salary of" in text and "confirmed" in text or "gaji sebesar" in text and "dikonfirmasi" in text:
                mode = "confirmed"
        elif source == "service_provider":
            if "approved an invoice payment" in text or "menyetujui pembayaran faktur" in text:
                mode = "one_time_invoice"
            elif "payout is still pending" in text or "pembayaran berikutnya" in text and "masih tertunda" in text:
                mode = "unconfirmed_gig"
            if "lease increases monthly rent" in text or "perpanjangan sewa menaikkan biaya sewa" in text:
                percentage = re.search(r"(\d+(?:\.\d+)?)\s*%", text)
                if percentage:
                    result.rent_multiplier = Decimal(1) + Decimal(percentage[1]) / 100
                    result.references.append(row["message_id"])
        if mode:
            result.salary_mode = mode
            result.salary_amount = money(amounts[0][1]) if amounts else None
            result.salary_currency = amounts[0][0].upper() if amounts else None
            result.salary_date = day(dates[0]) if dates else None
            result.references.append(row["message_id"])
        elif row["message_id"] not in result.references:
            result.ignored.append(row["message_id"])
    return result
