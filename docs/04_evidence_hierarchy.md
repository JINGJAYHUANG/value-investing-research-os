# 04 — Evidence Hierarchy

**Status:** FINAL for framework governance

## Evidence levels

| Level | Evidence | Typical examples |
|---|---|---|
| E1 | Primary, legally or operationally authoritative | audited filings, exchange/regulator filings, court documents, official contracts when public |
| E2 | Primary company communication | earnings calls, official investor presentations, shareholder letters, official product disclosures |
| E3 | High-quality independent secondary | reputable financial press, established industry research, peer-reviewed work |
| E4 | General secondary | analyst commentary, trade publications, databases with unclear primary sourcing |
| E5 | Tertiary / discovery only | blogs, social posts, forums, unsourced summaries, AI-generated summaries |

## Usage rules

- E1/E2 should support material factual claims whenever available.
- E3 may contextualize or challenge primary materials.
- E4 is useful for discovery but should be verified before driving a conclusion.
- E5 should rarely support a final factual statement.
- AI output is **not evidence**. It is a synthesis layer that must point back to sources.

## Required source-ledger fields

- source ID;
- title;
- issuer / publisher;
- publication date;
- accessed date;
- URL or file reference;
- evidence level;
- period covered;
- claim supported;
- notes / conflicts.

## Evidence language

Use explicit labels in working notes:

- `FACT:` direct source support;
- `INFERENCE:` interpretation from one or more facts;
- `HYPOTHESIS:` unverified mechanism or explanation;
- `UNKNOWN:` decision-relevant gap.

## Time consistency

Avoid mixing information that would not have been known at the analysis date. For historical or backtested research, record the **availability date**, not only the period end date.
