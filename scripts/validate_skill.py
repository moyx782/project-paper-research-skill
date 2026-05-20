#!/usr/bin/env python3
"""Validate the project-paper-research Codex skill repository.

This script is intentionally dependency-free so it can run on Windows,
macOS, Linux, and WSL with a standard Python installation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"[FAIL] {message}")
    sys.exit(1)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"Missing required file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def validate_skill_md() -> None:
    text = read_text(ROOT / "SKILL.md")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter: ---")

    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        fail("SKILL.md front matter must be closed with --- on its own line")

    front_matter = match.group(1)
    if not re.search(r"^name:\s*project-paper-research\s*$", front_matter, flags=re.MULTILINE):
        fail("SKILL.md front matter must contain: name: project-paper-research")
    if not re.search(r"^description:\s*.+", front_matter, flags=re.MULTILINE):
        fail("SKILL.md front matter must contain a non-empty description")
    ok("SKILL.md front matter is valid")


def validate_env_example() -> None:
    text = read_text(ROOT / ".env.example")
    required_keys = [
        "PAPER_RESEARCH_SOURCES",
        "ANONYMOUS_MODE",
        "PAPER_RESEARCH_LANGUAGE",
        "PAPER_RESEARCH_MAX_RESULTS_PER_QUERY",
        "PAPER_RESEARCH_MAX_PAPERS_TOTAL",
        "ARXIV_API_BASE",
        "CROSSREF_API_BASE",
        "DBLP_API_BASE",
        "SEMANTIC_SCHOLAR_API_KEY",
        "OPENALEX_API_KEY",
        "CROSSREF_MAILTO",
    ]

    for key in required_keys:
        if not re.search(rf"^{re.escape(key)}=", text, flags=re.MULTILINE):
            fail(f".env.example is missing {key}")

    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if "=" not in stripped:
            fail(f".env.example line {line_no} is not KEY=value: {line!r}")
        if re.search(r"\s+[A-Z0-9_]+=", stripped):
            fail(f".env.example line {line_no} may contain multiple variables on one line: {line!r}")

    ok(".env.example looks valid")


def validate_gitignore() -> None:
    text = read_text(ROOT / ".gitignore")
    required_patterns = [".env", ".env.local", ".env.*.local", "research-output/", "*.log"]
    patterns = {line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")}
    for pattern in required_patterns:
        if pattern not in patterns:
            fail(f".gitignore is missing pattern: {pattern}")
    ok(".gitignore protects local secrets and generated output")


def validate_no_private_env() -> None:
    if (ROOT / ".env").exists():
        fail("A local .env file exists in the repository root. Do not commit or publish it.")
    ok("No local .env file found in repository root")


def validate_required_paths() -> None:
    required_paths = [
        "README.md",
        "docs/source_config.md",
        "templates/paper_matrix_template.md",
        "templates/literature_review_report_template.md",
        "examples/ai_note_app_project.md",
        "examples/uav_swarm_project.md",
        "prompts/one_shot_prompt.md",
    ]
    for rel_path in required_paths:
        if not (ROOT / rel_path).exists():
            fail(f"Missing required path: {rel_path}")
    ok("Required support files exist")


def main() -> None:
    validate_required_paths()
    validate_skill_md()
    validate_env_example()
    validate_gitignore()
    validate_no_private_env()
    print("\nSkill validation passed.")


if __name__ == "__main__":
    main()
