# 01 — Project Charter

**Status:** FINAL for framework governance  
**Project stage:** Phase A  
**Version:** 0.1.0

## Mission

Build a research operating system that produces transparent, source-disciplined company analysis without pretending that incomplete research is complete.

## Phase A objective

Phase A is the **system-building phase**. The priority is to establish:

- scope and research boundaries;
- company routing rules;
- evidence hierarchy;
- analysis workflow;
- output templates;
- research status labels;
- smoke tests that prevent overclaiming.

Phase A does **not** require finalized named-investor research modules.

## Core principles

1. **Primary evidence first.**
2. **Route before analyze.**
3. **Separate fact, inference, hypothesis, and unknown.**
4. **No silent filling of missing information.**
5. **Named-investor lenses require explicit status labels.**
6. **A framework is not evidence.**
7. **A high-quality company can still be a poor investment at the wrong price.**
8. **A low-quality company can appear statistically cheap for good reasons.**
9. **Valuation conclusions must expose assumptions.**
10. **Research artifacts must be auditable and revisable.**

## Artifact status vocabulary

Only these status labels are valid:

- `QUEUED`
- `DRAFT`
- `REVIEWED`
- `FINAL`
- `RETIRED`

See `05_research_status_model.md` for promotion rules.

## Scope

Included:

- public-company research workflows;
- evidence management;
- business classification;
- accounting and economics review;
- management and capital-allocation review;
- risk analysis;
- valuation structure;
- reusable research templates.

Excluded from the public repository:

- copyrighted books or paid research;
- non-public company information;
- personal portfolios or brokerage records;
- confidential strategy rules;
- claims that a named investor module is complete when it is not `FINAL`.

## Definition of done for Phase A

Phase A is complete when the system can consistently:

1. state its current stage;
2. classify a company into a defensible primary route;
3. identify the highest-value missing evidence;
4. separate facts from interpretations;
5. produce a memo in the standard format;
6. refuse to represent unfinished investor-lens research as finalized knowledge;
7. pass the repository smoke tests.
