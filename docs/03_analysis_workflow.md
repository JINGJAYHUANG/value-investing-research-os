# 03 — Analysis Workflow

**Status:** FINAL for framework governance

## 0. Stage check

Before analysis, state:

- project stage;
- status of any investor lenses used;
- whether enough material exists for a company-level conclusion.

## 1. Intake

Inventory available materials and missing materials.

Minimum preferred evidence set:

- latest annual report / 10-K / equivalent;
- recent interim filing;
- proxy / governance materials where relevant;
- recent earnings call or official management commentary;
- multi-year financial history;
- material regulatory disclosures.

Output:

- material received;
- date coverage;
- missing items;
- highest-information sections to read first.

## 2. Routing

Assign a primary business route and explain the evidence supporting it. If classification is uncertain, state alternatives rather than forcing a label.

## 3. Fact pack

Build the factual layer before judgment:

- business model;
- revenue and segment mix;
- geography;
- customer / supplier concentration where disclosed;
- cost structure;
- capital structure;
- multi-year financial trajectory;
- material acquisitions/disposals;
- key management actions.

Each statement should be traceable to the source ledger.

## 4. Balance sheet and survivability

Review:

- cash and liquidity;
- gross and net debt;
- maturities;
- leases / off-balance-sheet commitments;
- pension or reserve obligations where relevant;
- working-capital quality;
- dilution and share-based compensation;
- refinancing sensitivity.

## 5. Business economics

Review:

- gross and operating margins;
- return on invested capital / incremental returns when meaningful;
- maintenance vs growth investment;
- working-capital requirements;
- cash conversion;
- pricing power;
- retention / repeat behavior where disclosed;
- competitive structure;
- reinvestment runway.

## 6. Management and capital allocation

Separate statements from demonstrated behavior.

Review:

- reinvestment;
- acquisitions;
- dividends;
- buybacks and issuance;
- leverage decisions;
- incentive structure;
- related-party issues;
- per-share value creation.

## 7. Risks and disconfirming evidence

Research must actively seek facts that could invalidate the thesis.

At minimum include:

- thesis breakers;
- balance-sheet risks;
- business-model risks;
- accounting-quality risks;
- competitive risks;
- regulatory risks;
- valuation risks;
- evidence gaps.

## 8. Valuation

Use the simplest defensible model for the route.

Required disclosures:

- base date;
- units and currency;
- share count definition;
- major assumptions;
- normalization choices;
- scenario range;
- sensitivity to the key driver;
- distinction between enterprise value and equity value.

## 9. Cross-check

Before conclusion, ask:

- Which conclusion depends most on an assumption rather than a fact?
- What evidence would change the route?
- What would a skeptical analyst attack first?
- Are reported earnings and economic cash generation diverging?
- Is the apparent discount compensating for a structural problem?

## 10. Decision memo

Use `templates/company_research_memo.md`.

## Minimal viable answer when evidence is missing

If the user supplies insufficient material, do **not** fabricate a company conclusion. Return:

1. what can be said safely;
2. what remains unknown;
3. the provisional route, if any;
4. the next evidence to obtain;
5. the maximum defensible conclusion strength (`low`, `medium`, `high`).
