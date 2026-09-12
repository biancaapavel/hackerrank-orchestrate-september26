"""Submission guards use a real one-request dataset, output and cash-flow trace."""
import csv
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from buy_or_wait.data import COLUMNS, Dataset
from buy_or_wait.planner import solve
from package_submission import verify_run
from test_engine import fixture, request


class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(dir=Path.cwd())
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        for folder in ("code", "dataset", "evaluation"):
            (self.root / folder).mkdir()
        (self.root / "code" / "solver.py").write_text("# Test source version\n")
        profile = fixture().profiles["u1"]
        req = request()
        self.write_csv("dataset/financial_profiles.csv", list(profile), [profile])
        self.write_csv("dataset/requests.csv", list(req), [req])
        for filename in ("financial_events", "exchange_rates", "images", "messages", "request_payment_options"):
            self.write_csv(f"dataset/{filename}.csv", ["unused"], [])
        data = Dataset(self.root / "dataset")
        row, trace = solve(data, req)
        self.write_csv("output.csv", COLUMNS, [row])
        (self.root / "evaluation" / "full_traces.json").write_text(json.dumps([trace]))
        self.manifest = {
            "requests": 1, "validation_passed": True,
            "dataset_sha256": {p.name: self.digest(p) for p in (self.root / "dataset").glob("*.csv")},
            "source_sha256": {"code/solver.py": self.digest(self.root / "code" / "solver.py")},
        }
        self.update_output_hash()

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def write_csv(self, path, fields, rows):
        with (self.root / path).open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def update_output_hash(self):
        digest = self.digest(self.root / "output.csv")
        self.manifest["output_sha256"] = digest
        (self.root / "evaluation" / "run_manifest.json").write_text(json.dumps(self.manifest))
        (self.root / "evaluation" / "usage_report.md").write_text(f"Output SHA-256: {digest}\n")

    def test_matching_run_replays_successfully(self):
        self.assertEqual(verify_run(self.root)["requests"], 1)

    def test_changed_source_rejects_stale_predictions(self):
        (self.root / "code" / "solver.py").write_text("# Changed after inference\n")
        with self.assertRaisesRegex(ValueError, "Code or dataset changed"):
            verify_run(self.root)

    def test_changed_dataset_rejects_stale_predictions(self):
        with (self.root / "dataset" / "financial_profiles.csv").open("a") as handle:
            handle.write("\n")
        with self.assertRaisesRegex(ValueError, "Code or dataset changed"):
            verify_run(self.root)

    def test_changed_output_rejects_stale_manifest(self):
        with (self.root / "output.csv").open("a") as handle:
            handle.write("\n")
        with self.assertRaisesRegex(ValueError, "Output manifest does not match"):
            verify_run(self.root)

    def test_missing_row_rejected_even_with_matching_output_hash(self):
        self.write_csv("output.csv", COLUMNS, [])
        self.update_output_hash()
        with self.assertRaisesRegex(ValueError, "row count"):
            verify_run(self.root)


if __name__ == "__main__":
    unittest.main()
