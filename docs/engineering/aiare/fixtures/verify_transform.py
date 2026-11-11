#!/usr/bin/env python3
"""AIARE 1.0.0 independent owned-fixture oracle.

Operator/verifier use only: do not give this file or expected outputs to the
blind Codex investigator. The verifier tests executable behavior, NOT whether
the investigator's explanation was independently correct. That requires a
second review of submitted hypotheses against held-out vectors.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Original studio-owned fixture: deliberate coverage of all four branches.
VECTORS = [
    (-9, 12), (-1, 4), (0, 11), (1, 1), (2, 5),
    (3, 7), (4, 9), (7, 19), (10, 21),
]


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify owned AIARE binary output")
    parser.add_argument("--binary", required=True, type=Path)
    parser.add_argument("--report", required=True, type=Path)
    parser.add_argument(
        "--negative-control", action="store_true",
        help="Intentionally corrupt one expected value: verifier MUST return FAIL",
    )
    args = parser.parse_args()
    binary = args.binary.expanduser().resolve()
    report = args.report.expanduser().resolve()
    if not binary.is_file():
        parser.error(f"compiled binary not found: {binary}")
    if report.exists():
        parser.error(f"refusing to overwrite an existing report: {report}")
    report.parent.mkdir(parents=True, exist_ok=True)

    cases = []
    for value, original_expected in VECTORS:
        expected = original_expected
        if args.negative_control and value == 3:
            expected += 1  # Deliberately incorrect: must be rejected.
        try:
            completed = subprocess.run(
                [str(binary), str(value)], capture_output=True,
                text=True, timeout=4.0, check=False,
            )
            observed = completed.stdout.strip()
            stderr = completed.stderr.strip()[:512]
            actual = int(observed) if observed.lstrip("-").isdigit() else None
            passed = completed.returncode == 0 and actual == expected
            entry = {
                "input": value, "expected": expected, "actual": actual,
                "returncode": completed.returncode, "pass": passed,
                "stderr": stderr,
            }
        except (OSError, subprocess.TimeoutExpired) as exc:
            entry = {
                "input": value, "expected": expected, "actual": None,
                "returncode": None, "pass": False,
                "stderr": str(exc)[:512],
            }
        cases.append(entry)

    passed = all(case["pass"] for case in cases)
    result = {
        "schema_version": "1.0.0",
        "fixture": "owned_transform",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "binary_sha256": digest_file(binary),
        "negative_control": args.negative_control,
        "status": "PASS" if passed else "FAIL",
        "passed": sum(case["pass"] for case in cases),
        "total": len(cases),
        "cases": cases,
        "notes": (
            "Executable-only behavior check; separate blind researcher comparison required."
        ),
    }
    # Exclusive create prevents a failed/repeated run from overwriting evidence.
    with report.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2, sort_keys=True)
        out.write("\n")
    print(json.dumps({
        "status": result["status"],
        "passed": result["passed"],
        "total": result["total"],
        "negative_control": result["negative_control"],
        "report": str(report),
    }))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
