#!/usr/bin/env python3
"""Validate the Chinese Humanizer package without external dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
LOCALIZATION = (ROOT / "LOCALIZATION.md").read_text(encoding="utf-8")
LICENSE = (ROOT / "LICENSE").read_text(encoding="utf-8")
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
OPENAI = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")


def require(match: re.Match[str] | None, message: str) -> re.Match[str]:
    if match is None:
        raise SystemExit(message)
    return match


frontmatter = require(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md must start with YAML frontmatter",
).group(1)

if not re.search(r"(?m)^name:\s+humanizer-zh\s*$", frontmatter):
    raise SystemExit("SKILL.md name must be humanizer-zh")

for nonportable_key in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(nonportable_key)}", frontmatter):
        raise SystemExit(f"Remove nonportable frontmatter key: {nonportable_key[:-1]}")

version_pattern = r"[0-9]+\.[0-9]+\.[0-9]+-zh\.[0-9]+"
skill_version = require(
    re.search(rf'(?m)^\s+version:\s*["\']({version_pattern})["\']\s*$', frontmatter),
    "SKILL.md metadata.version is missing or not a zh version",
).group(1)
readme_version = require(
    re.search(rf"(?m)^- \*\*({version_pattern})\*\*", README),
    "README version history is missing",
).group(1)

versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(versions) != 1:
    raise SystemExit(f"Version mismatch: {sorted(versions)}")

pattern_numbers = [int(number) for number in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)]
if pattern_numbers != list(range(1, 34)):
    raise SystemExit(f"Expected patterns 1-33, found {pattern_numbers}")

readme_numbers = {int(number) for number in re.findall(r"(?m)^\| ([0-9]+) \|", README)}
if readme_numbers != set(range(1, 34)):
    raise SystemExit("README pattern table must contain patterns 1-33")

if len(SKILL.splitlines()) > 500:
    raise SystemExit("SKILL.md exceeds the 500-line portability budget")

required_attribution = (
    "https://github.com/blader/humanizer",
    "Siqi Chen",
    "Copyright (c) 2025 Siqi Chen",
)
combined = README + LOCALIZATION + LICENSE
for value in required_attribution:
    if value not in combined:
        raise SystemExit(f"Required upstream attribution is missing: {value}")

if "humanizer-zh" not in OPENAI or "$humanizer-zh" not in OPENAI:
    raise SystemExit("agents/openai.yaml does not reference humanizer-zh")

if PLUGIN.get("name") != "humanizer-zh" or PLUGIN.get("license") != "MIT":
    raise SystemExit("Claude plugin name or license is incorrect")

print(f"Chinese Humanizer package v{skill_version} is valid")
