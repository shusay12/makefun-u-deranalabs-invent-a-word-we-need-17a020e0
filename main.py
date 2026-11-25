#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented word with a one-line definition to /output/entry.txt
(or $OUTPUT_DIR/entry.txt).

The coinage is "byeloop": the round of "bye"s that keeps restarting after
a call is already over. Everybody has lived it — the farewell
that will not end, each "bye" birthing one more "bye" — and English has no
word for it. "Byeloop" is built from two words anyone already knows ("bye"
+ "loop"), so it is sayable, spellable and memorable at first sight, and
the definition lands in a single reading. The loop in the word mirrors the
loop in the behaviour: the name performs what it names.

Deterministic, standard library only: no network, no randomness, no input
files. The kit gate is enforced here before writing: 1-140 UTF-8
characters, not only whitespace.
"""

import os
import sys

ENTRY = 'Byeloop (n.): the round of "bye"s that keeps restarting after a call is already over.'


def main() -> int:
    # Enforce the kit gate on the entry text itself.
    chars = len(ENTRY)
    if chars < 1 or chars > 140:
        print(f"gate failure: entry is {chars} characters, outside 1-140", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("gate failure: entry is only whitespace", file=sys.stderr)
        return 1
    try:
        ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"gate failure: entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
