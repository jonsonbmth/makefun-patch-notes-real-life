#!/usr/bin/env python3
"""Real-Life Patch Notes entry.

Prints a single original patch note (at most 160 characters) and writes it
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Standard library only, no input, no network, deterministic.
"""

import os

ENTRY = "v3.2.0: fixed a bug where the brain replayed your most embarrassing moment from 2009 at 3 a.m. with no way to skip it."


def main() -> None:
    print(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "entry.txt"),
                  "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
