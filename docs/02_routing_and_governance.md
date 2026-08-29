# 02 — Routing and Governance

**Status:** FINAL for framework governance

## Why routing comes first

The same metric can mean different things across business models. Low price-to-book may be meaningful for a bank but nearly irrelevant for an asset-light software company. High free cash flow can indicate durable economics or temporary underinvestment. Research therefore begins by asking **what kind of business is this?**

## Primary business routes

Choose one primary route. Add at most two secondary tags.

| Route | Typical characteristics | Main analytical emphasis |
|---|---|---|
| `compounder` | durable reinvestment runway, pricing power, high incremental returns | unit economics, moat durability, reinvestment, per-share value creation |
| `financial` | bank, insurer, broker, lender | asset quality, underwriting, leverage, capital adequacy, reserves |
| `cyclical` | demand/profit tied to macro or industry cycle | normalized margins, cycle position, balance-sheet survivability |
| `commodity` | price-taker economics, low differentiation | cost curve, capacity, balance sheet, cycle-adjusted cash flow |
| `asset_heavy` | large fixed assets/capex | maintenance vs growth capex, utilization, replacement economics |
| `special_situation` | spin-off, restructuring, liquidation, event-driven setup | catalyst, legal structure, downside realization, timing |
| `early_stage` | limited history, negative/unstable earnings, high uncertainty | unit economics, funding runway, market structure, scenario analysis |
| `mixed` | no route dominates | explicitly state why; analyze by segment |

## Routing discipline

A route is a hypothesis until supported by evidence. Change the route when the facts contradict the initial label.

Red flags for incorrect routing include:

- calling a company a compounder despite structurally high leverage;
- ignoring cyclicality because recent margins are strong;
- treating accounting book value as economic value without asset-quality analysis;
- treating temporary working-capital release as recurring free cash flow;
- using a famous-investor framework as the route itself.

## Lens governance

A named-investor lens is optional and secondary to company facts.

Rules:

1. Use no more than **three primary lenses and two secondary lenses** in one memo.
2. Every lens must display its status: `QUEUED`, `DRAFT`, `REVIEWED`, or `FINAL`.
3. A non-`FINAL` lens must be described as **provisional / placeholder**.
4. A named lens cannot override contradictory primary evidence.
5. A lens can organize questions; it cannot manufacture facts.

## Conflict resolution

When sources conflict:

1. preserve both claims;
2. rank sources by evidence level;
3. check date, scope, accounting definition, and unit;
4. state the unresolved conflict if it cannot be reconciled;
5. do not average incompatible values merely to produce one number.

## Governance rule

The repository's governance documents outrank examples, drafts, and investor-lens notes. A lower-status artifact may not silently amend a `FINAL` governance rule.
