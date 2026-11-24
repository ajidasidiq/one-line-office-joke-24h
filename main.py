#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes a single original one-line joke about office life to
/output/entry.txt (the grader reads exactly that file).
"""

import os

JOKE = "I muted myself on a call, and for the first time all week, everyone in the meeting agreed with me."

def main():
    # Gate (per the bounty rules): one line, 1-200 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 200, f"joke must be 1-200 chars, got {len(JOKE)}"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Byte-level round-trip check: what was written must match main.py exactly.
    with open(path, "rb") as f:
        written = f.read()
    assert written == JOKE.encode("utf-8"), "round-trip mismatch"
    print(f"Wrote {len(JOKE)} characters to {path} (round-trip verified)")

if __name__ == "__main__":
    main()
