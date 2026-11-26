#!/usr/bin/env python3
"""Print the entry: one apology line from a smart speaker.

Reads entry.txt (the single submitted line) and prints it exactly.
Deterministic: same input, same output, every run.
"""

from pathlib import Path


def main() -> None:
    path = Path(__file__).with_name("entry.txt")
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit(f"{path.name} is empty: the entry must be exactly one line")
    print(line)


if __name__ == "__main__":
    main()
