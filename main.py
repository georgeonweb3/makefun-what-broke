#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy to /output/entry.txt:
a payment that went through while its confirmation got lost,
told straight, with a twist, and a concrete next step.

Stdlib only, no network, deterministic.

Candidate scoring (against the judge brief, in order):
  A password/DB "forgot it exists" — funny, but the next step is generic.
  B OOM ate the shopping cart — good image, weak next step ("start again").
  C upload lost mid-flight — failure too vague, retry is the whole joke.
  D/D2 payment went through, receipt printer jammed on "success" — the
    winner: names the exact failure (money taken, confirmation lost),
    gives the one money-saving next step (check the bank before paying
    twice), and the good-news/bad-news frame is repeatable out loud.
    134 chars, single line, shippable in a real error dialog.
"""

import os
import sys

ENTRY = (
    "Good news: your payment went through. "
    "Bad news: our receipt printer jammed on the word 'success'. "
    "Check your bank before paying twice."
)


def main() -> int:
    # Self-check: the gate requires UTF-8 text of 1-200 chars,
    # a single line, and not only whitespace.
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    ENTRY.encode("utf-8")  # must be valid UTF-8

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)  # no trailing newline
    return 0


if __name__ == "__main__":
    sys.exit(main())
