"""One-line AI excuse for breaking production, for u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "I didn't break production; I just gave the bug a promotion so it could fail at a higher level."

# Entry is 94 characters, inside the 180-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
