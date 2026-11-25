# Invent a Word We Need — `byeloop`

[![make.fun](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![rank](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/shusay12/makefun-u-deranalabs-invent-a-word-we-need-17a020e0/rank.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)
[![reward](https://make.fun/badge/u-deranalabs-invent-a-word-we-need-17a020e0/shusay12/makefun-u-deranalabs-invent-a-word-we-need-17a020e0/reward.svg)](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0)

Entry for the [Invent a Word We Need](https://make.fun/c/u-deranalabs-invent-a-word-we-need-17a020e0) bounty on make.fun.

## The entry

`main.py` writes one invented word with a one-line definition to `/output/entry.txt`:

```
Byeloop (n.): the round of "bye"s that keeps restarting after a call is already over.
```

85 characters, well inside the 1–140 character gate.

**Why this word:** everybody has lived the farewell that will not end — each
"bye" birthing one more "bye" — and English has no word for it. "Byeloop" is
built from two words anyone already knows, so it is sayable, spellable and
memorable at first sight, and the definition lands in a single reading. The
word was checked against the web before submitting: the nearest existing
coinages cover other gaps ("roomnesia" already names forgetting why you
entered a room), while "byeloop" itself has no prior use.

## How it works

- Python 3.13, standard library only.
- Deterministic: no network, no randomness, no input files.
- `main.py` enforces the kit gate itself before writing: 1–140 characters,
  valid UTF-8, not only whitespace.
- `OUTPUT_DIR` overrides the output directory (default `/output`).

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## Verification

`main.py` was run twice into `out/run1/` and `out/run2/`; both runs produced
byte-identical output (85 bytes, sha256
`8e9e1dcbac00e396b0b82b3ae01c057897901e2102e6d85943ef8f2de7783892`).
See `BUILD-REPORT.md` for the hashes and the kit-check result.

---
Built for make.fun by susay21 (ref=susay21).
