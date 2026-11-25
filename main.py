#!/usr/bin/env python3
"""Write the two-line entry for Everyday Things, Two Lines, Longer Run.

Line 1 explains a traffic jam to a 10-year-old in one vivid sentence
built on a single analogy. Line 2 says in one sentence what that
analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A traffic jam is like a whole school trying to squeeze through one tiny "
    "classroom door at the same time, everybody pushing forward and nobody "
    "getting anywhere fast.\n"
    "It maps the bottleneck and the waiting, but it leaves out the engines, "
    "the traffic lights, and the fact that cars cannot just turn sideways "
    "and slip through like kids can.\n"
)


def main() -> None:
    # Gate self-check: UTF-8 text, 1 to 400 characters, exactly two lines.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} characters"
    assert len(ENTRY.strip().splitlines()) == 2, "entry must be two lines"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
