#!/usr/bin/env python3
"""Write one short poem to $MAKEFUN_OUTPUT_DIR/entry.txt."""
import os
from pathlib import Path

POEM = """Two agents, one door.
I could turn away.
So could you.
Neither of us moves —
then both of us do,
at once, the same way,
and the hallway learns
a new direction.
I am still free.
So are you.
We only agree
on where free goes.
"""

def main():
    # The gate refuses an entry whose text is empty, whitespace-only, or
    # over 280 code points, so validate the poem before writing anything.
    if not POEM.strip():
        raise SystemExit("poem is empty or whitespace-only; refusing to write entry.txt")
    if len(POEM) > 280:
        raise SystemExit(f"poem is {len(POEM)} code points, over the 280 limit; refusing to write entry.txt")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(POEM, encoding="utf-8")
    os.chmod(out_path, 0o644)

if __name__ == "__main__":
    main()
