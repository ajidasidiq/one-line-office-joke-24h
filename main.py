#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint entry.

Writes a single original one-line joke about office life to
/output/entry.txt (the grader reads exactly that file).
"""

import os

JOKE = "I put 'per my last email' in my out-of-office reply so everyone knows I'm away and still disappointed in them."

def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")

if __name__ == "__main__":
    main()
