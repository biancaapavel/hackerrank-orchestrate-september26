"""Compatibility entry point for public-example evaluation."""
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    raise SystemExit(subprocess.call([sys.executable, str(Path(__file__).resolve().parents[1] / "main.py"), "--samples", *sys.argv[1:]]))
