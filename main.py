#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum-placard line for an everyday office object
to /output/entry.txt. The line is fixed and deterministic: the same
bytes on every run, so the grader sees an identical entry each time.
"""

import os

def validate(line):
    """Check the placard obeys the contest rules before it is written."""
    if "\n" in line or "\r" in line:
        raise ValueError("placard must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "placard is %d characters, over the %d limit" % (len(line), MAX_CHARS)
        )
    if not line.strip():
        raise ValueError("placard must not be empty")
    return line


def main():
    line = validate(PLACARD)
    # Never remove or recreate the output directory: the grader may
    # hand us a read-only parent with /output already in place.
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))


# Where the grader reads the entry from.
OUTPUT_PATH = "/output/entry.txt"

# Why the stapler: every desk on earth has one, everyone has felt
# the crunch, and "binding pages forever" is the most marriage-like
# thing an office object ever does. The shredder is the only divorce
# court it recognises.
PLACARD = (
    "Stapler, c. 1987, Office of Eternal Binding. "
    "With one sacred crunch it weds loose pages in holy matrimony \u2014 "
    "two sheets, one staple, till the shredder do them part."
)

# The contest limit: one line, at most 180 characters.
MAX_CHARS = 180


if __name__ == "__main__":
    main()
