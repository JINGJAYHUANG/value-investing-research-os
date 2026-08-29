# Value Investing Research OS

A public, evidence-driven operating system for structured company research.

> **Project status: Phase A / public reconstruction v0.1.0**  
> This repository defines research governance, routing, evidence discipline, output templates, and validation checks. It does **not** claim to contain finalized “brains” for Buffett, Graham, Fisher, Munger, Marks, or any other investor.

## Why this exists

Investment research often fails before valuation: evidence is mixed with inference, company types are routed into the wrong analytical framework, missing data is silently filled with assumptions, and famous-investor ideas are invoked without source discipline.

This project turns those failure modes into explicit rules:

1. **Stage awareness** — research artifacts move through `QUEUED → DRAFT → REVIEWED → FINAL`.
2. **Evidence hierarchy** — primary materials outrank commentary and summaries.
3. **Routing before interpretation** — classify the business before choosing lenses and metrics.
4. **Facts / inference / hypothesis separation** — every memo distinguishes what is known from what is inferred.
5. **Minimal viable answer under missing data** — uncertainty is surfaced, not hidden.
6. **Reproducible outputs** — every company memo follows a stable structure.
7. **Smoke tests** — the repository checks that unfinished research is not presented as finalized knowledge.

## Repository map

```text
.
├── docs/
│   ├── 01_project_charter.md
│   ├── 02_routing_and_governance.md
│   ├── 03_analysis_workflow.md
│   ├── 04_evidence_hierarchy.md
│   ├── 05_research_status_model.md
│   ├── 06_investor_lens_registry.md
│   └── 07_smoke_tests.md
├── templates/
│   ├── company_research_memo.md
│   ├── source_ledger.csv
│   └── investor_lens_template.md
├── examples/
│   └── fictional_company_memo.md
├── scripts/
│   └── validate_repo.py
├── .github/workflows/
│   └── validate.yml
├── source_notes/
│   └── reconstruction_note.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## Default research sequence

`Stage check → Intake → Business routing → Fact pack → Balance sheet → Economics → Management/capital allocation → Risks → Valuation → Cross-check → Decision memo`

The system intentionally requires routing before applying any named-investor lens.

## Evidence labels

Every substantive statement should be tagged as one of:

- **FACT** — directly supported by cited material.
- **INFERENCE** — reasoned interpretation from facts.
- **HYPOTHESIS** — plausible but unverified explanation that needs testing.
- **UNKNOWN** — required information is missing.

## Investor lenses

Named-investor lenses are research modules, not authority shortcuts. In Phase A, the registry is explicitly `QUEUED` unless a module has been independently researched, sourced, reviewed, and promoted to `FINAL`.

## Quick start

1. Copy `templates/company_research_memo.md`.
2. Create a source ledger from `templates/source_ledger.csv`.
3. Classify the company using `docs/02_routing_and_governance.md`.
4. Fill the fact layer before writing conclusions.
5. Run:

```bash
python scripts/validate_repo.py
```

## What this repository is not

- Not investment advice.
- Not a stock-picking service.
- Not a repository of copyrighted books or paid research.
- Not proof that any named investor's philosophy has been exhaustively reconstructed.
- Not a substitute for original filings, audited statements, regulatory documents, or professional judgment.

## Public reconstruction note

This public version was reconstructed from an earlier private Phase A system whose raw project files were not fully exportable at reconstruction time. The public version preserves the verified governance concepts while deliberately omitting inaccessible or copyright-sensitive source material. See `source_notes/reconstruction_note.md`.

## License

MIT License. See `LICENSE`.
