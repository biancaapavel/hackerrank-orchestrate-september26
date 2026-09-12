#!/usr/bin/env python3
"""Validate and package a run; --refresh runs all final checks and regenerates it."""
import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def verify_run(root: Path) -> dict:
    manifest = json.loads((root / "evaluation" / "run_manifest.json").read_text())
    digest = hashlib.sha256((root / "output.csv").read_bytes()).hexdigest()
    if digest != manifest["output_sha256"] or not manifest["validation_passed"]:
        raise ValueError("Output manifest does not match; run package_submission.py --refresh.")
    dataset_hashes = {p.relative_to(root / "dataset").as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in sorted([*(root / "dataset").glob("*.csv"),
                                       *(root / "dataset").glob("media/images/*.png")])}
    source_hashes = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted((root / "code").rglob("*"))
                     if p.is_file() and "__pycache__" not in p.parts
                     and p.suffix in {".py", ".json", ".md"} and not p.name.startswith(".")}
    if dataset_hashes != manifest.get("dataset_sha256") or source_hashes != manifest.get("source_sha256"):
        raise ValueError("Code or dataset changed after inference; run package_submission.py --refresh.")
    # Recheck row coverage and replay the saved full trace before making a ZIP.
    from buy_or_wait.data import COLUMNS, Dataset, read_csv
    from buy_or_wait.validate import validate_all
    requests = read_csv(root / "dataset" / "requests.csv")
    with (root / "output.csv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != COLUMNS:
            raise ValueError("Output columns do not match the submission contract.")
        rows = list(reader)
    if manifest["requests"] != len(requests) or len(rows) != len(requests):
        raise ValueError("Output row count does not match the full request dataset.")
    traces = json.loads((root / "evaluation" / "full_traces.json").read_text())
    validate_all(Dataset(root / "dataset"), requests, rows, traces)
    usage = (root / "evaluation" / "usage_report.md").read_text(encoding="utf-8")
    if digest not in usage:
        raise ValueError("Usage report is not tied to the current output hash.")
    return manifest


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true",
                        help="Run tests, sample diagnostics and full inference before packaging")
    args = parser.parse_args()
    if args.refresh:
        commands = [
            [sys.executable, "-m", "unittest", "discover", "-s", str(root / "code" / "tests"), "-v"],
            [sys.executable, str(root / "code" / "main.py"), "--samples"],
            [sys.executable, str(root / "code" / "analyze_samples.py"),
             "--output", str(root / "evaluation" / "sample_errors.md"),
             "--json", str(root / "evaluation" / "sample_diagnostics.json")],
            [sys.executable, str(root / "code" / "main.py")],
        ]
        for command in commands:
            subprocess.run(command, check=True, cwd=root)
    manifest = verify_run(root)
    report = {
        "requests": manifest["requests"], "output_sha256": manifest["output_sha256"],
        "output_manifest_match": True, "source_hashes_verified": True,
        "dataset_hashes_verified": True, "row_coverage_verified": True,
        "full_balance_replay_passed": True, "usage_report_output_match": True,
        "unit_tests": "passed" if args.refresh else "not rerun",
        "sample_evaluation": "passed" if args.refresh else "not rerun",
        "sample_diagnostic_replay": "passed" if args.refresh else "not rerun",
    }
    (root / "evaluation" / "validation_report.json").write_text(json.dumps(report, indent=2) + "\n")
    files = [root / f for f in ["README.md", "problem_statement.md", "AGENTS.md", "output.csv"]]
    for directory in ["code", "dataset", "evaluation"]:
        for path in (root / directory).rglob("*"):
            relative = path.relative_to(root)
            if not path.is_file() or "__pycache__" in relative.parts or path.name.startswith("."):
                continue
            if directory == "code" and path.suffix not in {".py", ".md", ".json"}:
                continue
            if directory == "dataset" and path.suffix not in {".csv", ".png"}:
                continue
            if directory == "evaluation" and path.suffix not in {".csv", ".json", ".md"}:
                continue
            files.append(path)
    temporary = root / "code.zip.tmp"
    with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(set(files)):
            name = path.relative_to(root).as_posix()
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    temporary.replace(root / "code.zip")
    print(f"Verified {manifest['requests']} rows, source/data hashes, usage report and full balance replay.")
    print(f"Created {root / 'code.zip'} ({(root / 'code.zip').stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
