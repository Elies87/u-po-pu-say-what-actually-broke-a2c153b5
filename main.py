#!/usr/bin/env python3
"""Write one brutally honest, funny error line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, fully deterministic: every run writes the exact same bytes.
"""

import os

LINE = (
    "We lost your work. Not deleted \u2014 lost. The server crashed mid-save "
    "and the only backup was a Post-it that said \u2018back up the server\u2019. "
    "Try again."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
