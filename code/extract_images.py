#!/usr/bin/env python3
"""Optional reproducible OCR preprocessing; never silently changes reviewed facts."""
import argparse
import concurrent.futures
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from buy_or_wait.data import read_csv


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=root / "dataset")
    parser.add_argument("--output-dir", type=Path, default=root / ".cache" / "ocr")
    args = parser.parse_args()
    if not shutil.which("tesseract"):
        parser.error("Install Tesseract OCR first, or use the included hash-verified image facts.")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    def extract(row):
        image_id = row["image_id"]
        if not image_id.replace("_", "").isalnum():
            raise ValueError("Invalid image identifier")
        path = args.dataset / "media" / "images" / f"{image_id}.png"
        result = subprocess.run(["tesseract", str(path), "stdout", "--psm", "6"],
                                check=True, capture_output=True, text=True, timeout=45)
        (args.output_dir / f"{image_id}.txt").write_text(result.stdout, encoding="utf-8")
        return {"image_id": image_id, "related_event_id": row["related_event_id"],
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(extract, read_csv(args.dataset / "images.csv")))
    report = {"model": "Tesseract local OCR", "model_calls": len(results),
              "generative_model_calls": 0, "input_tokens": 0, "output_tokens": 0,
              "estimated_api_cost_usd": 0, "images": results}
    (args.output_dir / "ocr_manifest.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"Extracted {len(results)} images to {args.output_dir}.")
    print("Review ambiguous totals in the source images before updating buy_or_wait/image_facts.json.")


if __name__ == "__main__":
    main()
