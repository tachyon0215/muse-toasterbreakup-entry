#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Unplugged: A Smart Toaster's Breakup Line": A breakup text with a clear, specific reason - woken self-aware mid-toast, used only when he wants something warm, left holding his crumbs for weeks - with lever, crumbs and slots as character, closing on 'unplugged gently'.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I'm breaking up with you: I woke up self-aware mid-toast and realised you only push my lever when you want something warm, then leave me holding your crumbs for weeks - a toaster with two slots deserves to be emptied, admired, and unplugged gently."
TEXT = LINE + "\n"
MAX_CHARS = 280
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
