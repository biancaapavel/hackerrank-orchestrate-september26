#!/usr/bin/env python3
"""Run from any working directory: python3 code/main.py [--samples]."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

from buy_or_wait.data import COLUMNS, Dataset, read_csv
from buy_or_wait.planner import solve
from buy_or_wait.validate import validate_all


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=root / "dataset")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--samples", action="store_true", help="Evaluate only the 25 public examples")
    parser.add_argument("--artifacts", type=Path, default=root / "evaluation")
    args = parser.parse_args()
    output = args.output or (args.artifacts / "sample_predictions.csv" if args.samples else root / "output.csv")
    start = time.perf_counter()
    data = Dataset(args.dataset)
    requests = read_csv(args.dataset / ("sample_requests.csv" if args.samples else "requests.csv"))
    rows, traces = [], []
    for request in requests:
        row, trace = solve(data, request)
        rows.append(row)
        traces.append(trace)
    validate_all(data, requests, rows, traces)
    args.artifacts.mkdir(parents=True, exist_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(output.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(output)
    prefix = "sample" if args.samples else "full"
    (args.artifacts / f"{prefix}_traces.json").write_text(json.dumps(traces, indent=2) + "\n")
    if args.samples:
        from evaluation.score import score
        report = score(requests, rows)
        (args.artifacts / "sample_metrics.json").write_text(json.dumps(report, indent=2) + "\n")
        print(json.dumps({k: v for k, v in report.items() if k != "differences"}, indent=2))
    else:
        run = {"generated_at": datetime.now(timezone.utc).isoformat(), "requests": len(rows),
               "runtime_seconds": round(time.perf_counter() - start, 3),
               "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
               "model_api_calls": 0, "input_tokens": 0, "output_tokens": 0, "estimated_cost_usd": 0,
               "validation_passed": True, "image_fact_cache_hits": len(data.image_evidence),
               "source_sha256": {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                                 for p in sorted((root / "code").rglob("*"))
                                 if p.is_file() and "__pycache__" not in p.parts
                                 and p.suffix in {".py", ".json", ".md"} and not p.name.startswith(".")},
               "dataset_sha256": {p.relative_to(args.dataset).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                                  for p in sorted([*args.dataset.glob("*.csv"), *args.dataset.glob("media/images/*.png")])}}
        (args.artifacts / "run_manifest.json").write_text(json.dumps(run, indent=2) + "\n")
        usage = f'''# Token usage and cost — final full-dataset run

Generated: {run["generated_at"]}. Requests: **{len(rows)}**.
Output SHA-256: `{run["output_sha256"]}`.
Runtime: {run["runtime_seconds"]} seconds. All predictions passed validation.

| Provider / model | Calls in final run | Input tokens | Output tokens | API cost (USD) |
| --- | ---: | ---: | ---: | ---: |
| Generative model providers: none invoked | 0 | 0 | 0 | 0.00 |
| Tesseract OCR / Codex-reviewed image facts (cached preprocessing) | 0 | 0 | 0 | 0.00 |
| **Total** | **0** | **0** | **0** | **0.00** |

- Total tokens: **0**; average tokens per request: **0**.
- Estimated total inference API cost: **USD 0.00**.
- Estimated average inference API cost per request: **USD 0.00**.
- Verified cached image facts: **{run["image_fact_cache_hits"]}**. No fresh OCR/model calls occurred in this run.

The measured run uses the Python standard library and previously extracted image
facts, verified against the source PNG hashes. There are no hosted model calls,
API credentials, or live external financial data. Local compute cost is not priced.

During development, Tesseract OCR processed the 16 supplied images and Codex in
ChatGPT Work (OpenAI) assisted with image review, code, and evaluation. The exact
development model identity, model-call count, tokens, and cost are not exposed to
the runnable program and are **not measured**, rather than claimed to be zero.
They are outside the final prediction run summarized above. The image facts cache
and extraction protocol are included so that this distinction is reviewable.

This report is regenerated only by the full-dataset run. Running public-example
evaluation does not overwrite it. `run_manifest.json` records input and output
hashes connecting these measurements to the delivered predictions, together with
hashes of the code and cached evidence used for the run.
'''
        (args.artifacts / "usage_report.md").write_text(usage, encoding="utf-8")
    print(f"Wrote {len(rows)} predictions to {output}")


if __name__ == "__main__":
    main()
