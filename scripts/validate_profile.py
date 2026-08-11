from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
REQUIRED = ["README.md", "RESEARCH.md", "OUTPUTS.md", "OPEN-SCIENCE.md", "PROFILE.en.md", "assets/profile-header.svg", "assets/research-ecosystem.svg", "assets/trajectory.svg"]

for rel in REQUIRED:
    if not (ROOT / rel).is_file():
        ERRORS.append(f"Missing required profile asset: {rel}")

link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
html_pattern = re.compile(r'(?:href|src)=["\']([^"\']+)["\']')
checked = 0
for md in ROOT.glob("*.md"):
    text = md.read_text(encoding="utf-8")
    for raw in link_pattern.findall(text) + html_pattern.findall(text):
        raw = raw.strip().split()[0]
        if raw.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        if not target or target.startswith("/"):
            continue
        checked += 1
        if not (md.parent / target).resolve().exists():
            ERRORS.append(f"Broken local link in {md.name}: {raw}")

print(f"Validated profile structure and {checked} local links.")
if ERRORS:
    for error in ERRORS:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print("Profile validation passed.")
