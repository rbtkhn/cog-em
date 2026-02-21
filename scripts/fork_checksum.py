#!/usr/bin/env python3
"""
Compute a checksum of the fork state (SELF + EVIDENCE + prompt sections).

Provides a verifiable "proof of development" — a hash that uniquely identifies
the fork's documented state at a given moment.

Usage:
    python scripts/fork_checksum.py
    python scripts/fork_checksum.py --append   # Append (ts, checksum) to FORK-CHECKSUM-LOG.txt
"""

import argparse
import hashlib
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROFILE_DIR = REPO_ROOT / "users" / "pilot-001"
BOT_DIR = REPO_ROOT / "bot"
LOG_PATH = PROFILE_DIR / "FORK-CHECKSUM-LOG.txt"


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text().strip()


def _canonicalize(text: str) -> bytes:
    """Normalize for hashing: strip, Unix line endings."""
    normalized = text.strip().replace("\r\n", "\n").replace("\r", "\n")
    return normalized.encode("utf-8")


def compute_checksum() -> str:
    """Compute SHA-256 of fork state."""
    parts = []
    parts.append(_read(PROFILE_DIR / "SELF.md"))
    parts.append(_read(PROFILE_DIR / "EVIDENCE.md"))
    # Key prompt sections that embed fork state
    prompt_path = BOT_DIR / "prompt.py"
    if prompt_path.exists():
        content = prompt_path.read_text()
        # Extract SYSTEM_PROMPT content (between triple quotes)
        import re
        m = re.search(r'SYSTEM_PROMPT\s*=\s*"""(.*?)"""', content, re.DOTALL)
        if m:
            parts.append(m.group(1).strip())
    h = hashlib.sha256()
    for p in parts:
        h.update(_canonicalize(p))
        h.update(b"\n---\n")
    return h.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute fork state checksum")
    parser.add_argument("--append", "-a", action="store_true", help="Append to FORK-CHECKSUM-LOG.txt")
    args = parser.parse_args()
    checksum = compute_checksum()
    print(checksum)
    if args.append:
        ts = datetime.now().isoformat()
        PROFILE_DIR.mkdir(parents=True, exist_ok=True)
        with open(LOG_PATH, "a") as f:
            f.write(f"{ts} {checksum}\n")
        print(f"Appended to {LOG_PATH}", file=sys.stderr)


if __name__ == "__main__":
    main()
