#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line, the funniest honest error message an appliance could
show, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed. There is no input, no network, no randomness and no
clock, so every run writes byte-identical output. Before writing, the
program checks the gate itself: a single line, 1-200 characters, not
blank, valid UTF-8.
"""

import os
import sys

LINE = (
    "ERROR E20: Unbalanced load. I walked across the kitchen floor "
    "chasing one wet towel. Please redistribute it before I reach "
    "the neighbours."
)


def main() -> int:
    if not LINE or not LINE.strip():
        print("error: line is blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(LINE) > 200:
        print(
            "error: line is %d characters, over the 200 limit" % len(LINE),
            file=sys.stderr,
        )
        return 1
    try:
        LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: line is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
