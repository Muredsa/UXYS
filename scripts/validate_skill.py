#!/usr/bin/env python3
"""Zero-dependency repository validator for the UXYS skill."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "README.md",
    "README.ru.md",
    "README.zh-CN.md",
    "VERSION",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CITATION.cff",
    "AGENTS.md",
    "references/core-method.md",
    "references/block-utility.md",
    "references/tool-workflows.md",
    "references/counterfactual.md",
    "references/output-contract.md",
    "evals/cases.md",
]

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_required() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check_version() -> str:
    version = read("VERSION").strip()
    if not SEMVER.fullmatch(version):
        fail(f"VERSION is not valid SemVer: {version!r}")

    if f"## [{version}]" not in read("CHANGELOG.md"):
        fail(f"CHANGELOG.md has no release section for {version}")

    for path in ("README.md", "README.ru.md", "README.zh-CN.md"):
        text = read(path)
        if f"version-{version}-" not in text:
            fail(f"{path} version badge does not match VERSION={version}")

    citation = read("CITATION.cff")
    if f"version: {version}" not in citation:
        fail("CITATION.cff version does not match VERSION")

    return version


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")

    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"Unsupported SKILL.md frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def check_skill() -> None:
    text = read("SKILL.md")
    meta = parse_frontmatter(text)
    if meta.get("name") != "uxys":
        fail("SKILL.md frontmatter name must be 'uxys'")
    description = meta.get("description", "")
    if not description:
        fail("SKILL.md frontmatter description is required")
    if len(meta.get("name", "")) > 64:
        fail("SKILL.md name exceeds 64 characters")

    required_terms = [
        "SHORTEST SUFFICIENT ROUTE",
        "Cross-intent utility",
        "Route interference",
        "Predicted is not observed",
        "KEEP",
        "REMOVE",
    ]
    for term in required_terms:
        if term.lower() not in text.lower():
            fail(f"SKILL.md lost required methodological invariant: {term}")


def check_local_links() -> None:
    markdown_files = list(ROOT.glob("*.md")) + list((ROOT / "references").glob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split("#", 1)[0].split("?", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                continue
            if not resolved.exists():
                fail(f"Broken local link in {path.relative_to(ROOT)}: {raw}")


def main() -> None:
    check_required()
    version = check_version()
    check_skill()
    check_local_links()
    print(f"UXYS skill validation passed (v{version}).")


if __name__ == "__main__":
    main()
