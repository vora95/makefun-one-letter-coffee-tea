#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program (akun utama @hazel-lynx-59).

Writes exactly one UTF-8 character, the letter A, to /output/entry.txt.

A = coffee. One letter, nothing else: no word, no explanation, no
punctuation, no trailing newline. Standard library only, no network,
no randomness, no arguments — the output is the same on every run.

Why A: the judge is a coffee-and-tea tasting judge weighing vivid first,
then funny, then true. Coffee is the more vivid drink — bold, dark,
aromatic, a jolt that lands alive — where tea reads calm and gentle.
Coffee also carries the richer joke (caffeine, "don't talk to me before
my first cup") and the truer claim for the people sending it: builders
run on coffee. A is the fuller, more alive answer.
"""

import os
import sys

LETTER = "A"  # A = coffee
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
