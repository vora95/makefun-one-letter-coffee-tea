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

Revision (v2): the letter is no longer a bare constant — it is picked
from an explicit drink-to-letter mapping, and the written file is read
back and verified before the program exits, so a silent write failure
can never pass as a valid entry.
"""

import os
import sys

# Explicit mapping of the two drinks to their letters.
DRINK_TO_LETTER = {"coffee": "A", "tea": "B"}

# The choice this entry defends: coffee.
CHOSEN_DRINK = "coffee"

OUTPUT_PATH = "/output/entry.txt"


def pick_letter(drink: str) -> str:
    """Return the single letter for a drink; fail loudly on bad input."""
    if drink not in DRINK_TO_LETTER:
        raise ValueError(f"unknown drink: {drink!r}")
    letter = DRINK_TO_LETTER[drink]
    assert len(letter) == 1 and not letter.isspace(), "letter must be one non-space character"
    return letter


def main() -> int:
    letter = pick_letter(CHOSEN_DRINK)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(letter)

    # Post-write verification: read back and assert the output is
    # exactly one non-whitespace character — the letter we chose.
    with open(OUTPUT_PATH, "rb") as handle:
        raw = handle.read()
    assert raw == letter.encode("utf-8"), f"output mismatch: {raw!r} != {letter!r}"
    assert len(raw) == 1, f"output must be exactly 1 byte, got {len(raw)}"
    return 0


if __name__ == "__main__":
    sys.exit(main())
