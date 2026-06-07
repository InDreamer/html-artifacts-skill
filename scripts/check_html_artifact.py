#!/usr/bin/env python3
"""Static checks for self-contained HTML artifacts."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REMOTE_RE = re.compile(
    r"""(?ix)
    <script\b[^>]*\bsrc\s*=\s*["']https?://
    |<link\b[^>]*\brel\s*=\s*["']stylesheet["'][^>]*\bhref\s*=\s*["']https?://
    |<link\b[^>]*\bhref\s*=\s*["']https?://[^>]*\brel\s*=\s*["']stylesheet["']
    |<(?:img|iframe|audio|video|source)\b[^>]*\bsrc\s*=\s*["']https?://
    |url\s*\(\s*["']?https?://
    |@import\s+
    |fetch\s*\(\s*["']https?://
    |new\s+WebSocket\s*\(
    """
)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_html_artifact.py <artifact.html>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"error: not found: {path}", file=sys.stderr)
        return 2

    text = path.read_text(encoding="utf-8", errors="replace")
    lower = text.lower()
    failures: list[str] = []
    warnings: list[str] = []

    if "<!doctype html" not in lower[:300]:
        failures.append("missing <!doctype html> near top")
    if "<html" not in lower:
        failures.append("missing <html>")
    if 'name="viewport"' not in lower and "name='viewport'" not in lower:
        failures.append("missing viewport meta")
    if REMOTE_RE.search(text):
        failures.append("contains external network dependency")
    if "<script" in lower and "</script>" not in lower:
        failures.append("script tag appears unclosed")
    if "<style" not in lower:
        warnings.append("no inline <style>; artifact may be under-designed")
    if "<svg" not in lower and "<table" not in lower and "<button" not in lower:
        warnings.append("no svg/table/button; verify HTML adds value over Markdown")
    if "navigator.clipboard" in text and "<textarea" not in lower:
        warnings.append("clipboard used without visible textarea fallback")
    if re.search(r"/Users/|/home/|~/", text):
        warnings.append("contains local filesystem path; check before sharing")

    for item in failures:
        print(f"FAIL: {item}")
    for item in warnings:
        print(f"WARN: {item}")

    if failures:
        return 1

    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
