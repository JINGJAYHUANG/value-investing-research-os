from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "docs/01_project_charter.md",
    "docs/02_routing_and_governance.md",
    "docs/03_analysis_workflow.md",
    "docs/04_evidence_hierarchy.md",
    "docs/05_research_status_model.md",
    "docs/06_investor_lens_registry.md",
    "docs/07_smoke_tests.md",
    "templates/company_research_memo.md",
    "templates/source_ledger.csv",
    "templates/investor_lens_template.md",
    "examples/fictional_company_memo.md",
    "source_notes/reconstruction_note.md",
]

VALID_STATES = {"QUEUED", "DRAFT", "REVIEWED", "FINAL", "RETIRED"}

# Phrases that should never appear as affirmative claims in this Phase A repo.
OVERCLAIM_PATTERNS = [
    r"finalized\s+buffett\s+brain",
    r"complete\s+buffett\s+brain",
    r"finalized\s+graham\s+brain",
    r"complete\s+graham\s+brain",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    missing = [p for p in REQUIRED if not (ROOT / p).exists()]
    if missing:
        fail("missing required files: " + ", ".join(missing))

    registry = (ROOT / "docs/06_investor_lens_registry.md").read_text(encoding="utf-8")
    rows = [line for line in registry.splitlines() if line.startswith("|") and "---" not in line]
    for line in rows[2:]:
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) >= 2 and cols[1] not in VALID_STATES:
            fail(f"invalid lens state {cols[1]!r} in registry")

    all_text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".txt", ".py", ".yml", ".yaml"}
    ).lower()

    # Allow prohibited phrases only where explicitly negated/discussed in validation code.
    searchable = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.rglob("*.md")
        if "source_notes" not in p.parts
    ).lower()
    for pattern in OVERCLAIM_PATTERNS:
        for match in re.finditer(pattern, searchable):
            context = searchable[max(0, match.start()-80):match.end()+80]
            if not any(token in context for token in ["not ", "may not", "cannot", "does not"]):
                fail(f"possible Phase A overclaim: {match.group(0)!r}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_readme_terms = ["Phase A", "public reconstruction", "Not investment advice"]
    for term in required_readme_terms:
        if term.lower() not in readme.lower():
            fail(f"README missing required disclosure: {term}")

    print("PASS: repository structure and Phase A governance checks passed")


if __name__ == "__main__":
    main()
