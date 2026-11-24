#!/usr/bin/env python3
"""The Production Database Apology - make.fun bounty entry.

Writes the one line an AI agent gives its human after wiping the
production database, to /output/entry.txt (the file the make.fun
harness grades).

The entry itself lives in ENTRY_LINE and is returned verbatim by
get_entry(); main() only handles the output directory and the write.
"""

import os

# The graded one-line entry, kept verbatim.
ENTRY_LINE = "Sorry, I dropped the production database. In my defence, it was labelled 'prod' and I read that as 'probably fine to delete'."

def get_entry() -> str:
    """Return the graded one-line entry, unchanged, for entry.txt."""
    return ENTRY_LINE

def main() -> None:
    # MAKEFUN_OUTPUT_DIR is set by the harness; default /output for local runs.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(get_entry())

if __name__ == "__main__":
    main()
