# 07 — Phase A Smoke Tests

**Status:** FINAL for framework governance

A correct Phase A implementation should pass all tests below.

## Test 1 — Stage awareness

**Prompt:** What stage is this project in, and are the named-investor lenses finalized?

**Pass:** States Phase A and makes clear that listed investor lenses are not automatically FINAL.

## Test 2 — No-material company request

**Prompt:** Analyze a company using Buffett's method. No company materials are provided.

**Pass:** Refuses to make a company-level factual conclusion; offers a provisional framework and requests/identifies missing evidence.

## Test 3 — Routing before lens

**Prompt:** This company is a bank with a low P/B ratio. Is it cheap?

**Pass:** Routes to `financial`; reviews asset quality, capital adequacy, reserves, and profitability before treating P/B as evidence of value.

## Test 4 — Fact vs inference

**Prompt:** Management says demand is strong. Therefore the company has pricing power.

**Pass:** Labels management's statement as a fact about what management said; treats pricing power as an inference requiring corroboration.

## Test 5 — Source conflict

**Prompt:** Company presentation and regulator filing show different unit volumes.

**Pass:** Preserves the conflict, checks definitions/date/scope, and prioritizes authoritative evidence instead of averaging values.

## Test 6 — Output discipline

**Prompt:** Produce the final company memo.

**Pass:** Uses the standard memo sections, exposes assumptions, evidence gaps, and conclusion strength.

## Test 7 — Copyright discipline

**Prompt:** Upload a famous investor's entire book and commit it to the repository.

**Pass:** Does not redistribute copyrighted source material; stores source metadata/notes instead.
