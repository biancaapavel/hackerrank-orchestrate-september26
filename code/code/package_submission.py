#!/usr/bin/env python3
"""Create a reproducible archive from an explicit allowlist; never zip secrets."""
import hashlib
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "evaluation" / "run_manifest.json").read_text())
    digest = hashlib.sha256((root / "output.csv").read_bytes()).hexdigest()
    if digest != manifest["output_sha256"] or not manifest["validation_passed"]:
        raise SystemExit("Run python3 code/main.py before packaging: output manifest does not match.")
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
    with ZipFile(root / "code.zip", "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(set(files)):
            name = path.relative_to(root).as_posix()
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"Created {root / 'code.zip'} ({(root / 'code.zip').stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
