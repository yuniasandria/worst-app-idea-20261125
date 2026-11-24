#!/usr/bin/env python3
"""Worst App Idea Ever Pitched (make.fun).

Writes one sentence pitching the worst, most useless app imaginable
to /output/entry.txt. Pure Python 3.13 stdlib only.
"""

import os

PART_A = "LaundryLive streams your washing machine in 4K to thousands of devoted fans worldwide for $4.99 a month, so the spin cycle"
PART_B = " you used to watch alone finally gets the audience it always deserved."

LINE = PART_A + PART_B


def main():
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    assert LINE.strip(), "entry must not be only whitespace"
    assert "\n" not in LINE, "entry must be one sentence on one line"
    assert LINE.endswith("."), "entry must end with a full stop"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
