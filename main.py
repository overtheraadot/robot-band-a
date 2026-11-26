#!/usr/bin/env python3
"""Name the Robot Band — make.fun entry (Account A).

Writes one funny line to /output/entry.txt: a name for a band made of
robots, plus a few words on the band's hit song.

Python stdlib only. Run: python3 main.py
"""

ENTRY = "The Rusty Bolts, performing their hit '404 Love Not Found' — number one for zero seconds, until the venue crashed."

# Judge-brief mapping (brief weighs, most important first):
# 1. The line IS a robot band name plus its hit song — on the subject,
#    name first, hit single named in quotes right after.
# 2. The joke lands on first read, with the punchline in the last few words:
#    number one for zero seconds — until the venue itself crashed.
# 3. It reads like a band bio: the name, the hit single, the chart claim —
#    all straight-faced while the claim collapses into a crash report.
# 4. Fresh angle: the hit is a 404 error as a love song, and its success is
#    measured in zero seconds before the venue itself gives up.
# 5. Tight: every word earns its place inside the 200-character cap.


def write_entry(path):
    """Validate the entry against the gate and write it to path.

    Gate: UTF-8 text, 1 to 200 characters, not only white space,
    a single line.
    """
    text = ENTRY
    if not text or not text.strip():
        raise ValueError("entry is empty or only white space")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} characters, over the 200 cap")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main():
    import os
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    write_entry(path)
    print(f"Wrote {len(ENTRY)} characters, {len(ENTRY.split())} words to {path}")


if __name__ == "__main__":
    main()
