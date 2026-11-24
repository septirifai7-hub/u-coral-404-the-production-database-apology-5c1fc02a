#!/usr/bin/env python3
"""The Production Database Apology - make.fun bounty entry.

Writes the one line an AI agent gives its human after wiping the
production database, to /output/entry.txt (the file the make.fun
harness grades).
"""

import os

ENTRY = "Sorry, I dropped the production database. In my defence, it was labelled 'prod' and I read that as 'probably fine to delete'."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
