#!/usr/bin/env python3
"""One Star, Five Stars for the Food.

Writes the entry line (one sentence, max 200 characters) to /output/entry.txt.
The line lives in entry.txt next to this script; this runner only copies it
verbatim (stripped) so the output is deterministic.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        text = f.read().strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry length {len(text)} out of range 1-200")
    # One sentence only: exactly one terminal punctuation mark.
    if sum(text.count(c) for c in ".!?") != 1:
        raise SystemExit("entry must be exactly one sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
