#!/usr/bin/env python3
"""One line of error copy for the make.fun "Say What Actually Broke" round.

The scene: the money moved, the proof of it did not. The program hands
back a single honest sentence a real product could show in a dialog:
what happened, why the user should not pay again, and the one check
that keeps their money safe.

Running it drops the line into /output/entry.txt with no trailing
newline, exactly as the judge reads it.
"""

from __future__ import annotations

import os
import sys

ENTRY = (
    "Good news: your payment went through. "
    "Bad news: our receipt printer jammed on the word 'success'. "
    "Check your bank before paying twice."
)

MAX_CHARS = 200
DEFAULT_OUTPUT = "/output/entry.txt"


def entry_line() -> str:
    """Return the entry line, checked against the competition's gate."""
    line = ENTRY
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    if not line.strip():
        raise ValueError("entry must not be blank")
    if line != line.strip():
        raise ValueError("entry must not carry padding spaces")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must stay on one line")
    line.encode("utf-8")
    return line


def write_entry(path: str) -> None:
    """Write the checked line to path, creating folders as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry_line())


def main() -> int:
    write_entry(os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
