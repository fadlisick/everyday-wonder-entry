#!/usr/bin/env python3
"""Everyday Wonder entry: one sentence about a raindrop race.

The program checks the sentence against the competition gate
(single line, 1-200 characters) and drops it into entry.txt
inside the harness output folder, with no trailing newline.
It reads nothing, reaches no network, and writes one file only.
"""

import os
import sys

LINE = "A single raindrop raced down the bus window and won, and for a moment I was genuinely proud of water."

LIMIT = 200


def target() -> str:
    """Where the graded entry.txt goes."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(base, exist_ok=True)
    return os.path.join(base, "entry.txt")


def main() -> int:
    text = LINE.strip()
    if not text:
        print("entry line is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry line must be one line", file=sys.stderr)
        return 1
    if len(text) > LIMIT:
        print("entry line over 200 characters", file=sys.stderr)
        return 1
    path = target()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
