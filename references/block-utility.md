# Block Utility & Route Interference

Use this reference when deciding whether a block should stay, move, weaken, strengthen, merge, or be removed.

## Why block-level judgment must be cross-intent

A block has no single absolute UX role.

The same block can be:

- **NECESSARY** for one intent;
- **SUPPORTING** for another;
- **DIVERSION** for a visitor who is already ready to act.

Therefore “this block distracts” is not enough to recommend deletion.

## Two global axes

### Cross-intent utility

How much useful route work the block performs across the important intents.

Signals of high utility:

- satisfies required evidence for one or more intents;
- supports several intents simultaneously;
- reduces uncertainty before a decision;
- provides a legitimate destination or direct route;
- replaces several weaker/redundant blocks;
- makes the page easier to understand without imposing large route cost.

### Route interference

How much unnecessary route cost the block creates for intents that do not need it.

Signals of high interference:

- visually stronger than the current route's necessary destination;
- introduces a competing action at a sensitive decision point;
- forces a detour before required evidence/action;
- occupies an entire early viewport for only a narrow intent;
- repeats already-satisfied evidence;
- sends visitors to another page unnecessarily;
- creates avoidable choice or semantic switching;
- obstructs the route on mobile or through sticky/overlay behavior.

## Decision matrix

| Cross-intent utility | Route interference | Default action |
|---|---|---|
| High | Low | **KEEP**; consider **EMPHASIZE** if important evidence is undersold |
| High | High | **ADJUST**, **MOVE**, or **DE-EMPHASIZE**; preserve the value while reducing interruption |
| Low | Low | Usually **KEEP** if harmless, or simplify/merge when density matters |
| Low | High | Strong **REMOVE** candidate |

## Removal gate

Before recommending **REMOVE**, verify all of the following:

1. The block has low utility across the modeled important intents.
2. It is not necessary evidence for a meaningful route.
3. Its function is not the only path to a legitimate destination.
4. Its removal would not create a missing semantic stage.
5. It creates meaningful interference, duplication, or maintenance cost.
6. A less destructive intervention (move, de-emphasize, merge, progressive disclosure) would not preserve useful value better.

If any of 1–4 is false, prefer a non-removal action.

## The “ready to act” trap

The fastest intent often makes most content look unnecessary.

Do not optimize the whole page for this route merely because it is shortest.

Example:

- Intent A: **ready to register** — `orientation → CTA`.
- Intent B: **build confidence** — `orientation → proof → objection resolution → CTA`.

A proof block may distract Intent A yet be necessary for Intent B. The likely design action is to preserve a direct CTA path while keeping proof accessible and appropriately weighted.

## Shared evidence leverage

A block is especially valuable when it satisfies multiple route stages or several intents with little additional exposure cost.

Examples:

- a concise demo that explains the product and provides proof;
- pricing that simultaneously clarifies fit and enables comparison;
- an FAQ answer that resolves the dominant objection without forcing a detour;
- a trust/result block that supports evaluation and confidence.

Prefer compact shared evidence over duplicating intent-specific content when the meaning remains clear.

## Route interference is not “badness”

Interference describes a relationship, not moral quality.

A navigation menu may interfere with a conversion-ready route while remaining essential utility for the site. A proof visual may compete for attention while making hesitant visitors more likely to understand the offer.

The recommendation should explain the conflict:

> This block is useful for **Build confidence**, but it dominates the visual field for **Ready to act**. Keep the evidence, but preserve a visually direct path to the primary action.

## Block verdict rules

### KEEP

Use when the block's current form and position serve its intended routes without disproportionate interference.

### EMPHASIZE

Use when high-value evidence or a destination is too weak relative to nearby content.

### ADJUST

Use when the block is valuable but its content, density, hierarchy, affordance, or internal composition is suboptimal.

### DE-EMPHASIZE

Use when the block should remain available but should not dominate intents that do not need it.

### MOVE

Use when timing is the problem: the block appears before the visitor needs it, after the decision it should support, or between two stages that should remain continuous.

### REMOVE

Use only after the removal gate passes.

### ADD

Use when one or more important intents lack evidence, an action, feedback, or a destination required for a sufficient route.

## Priority rule

When ranking changes, prefer interventions with the best **network effect**:

- improve multiple intents;
- repair a missing route;
- reduce strong interference;
- shorten exposed route cost while preserving sufficiency;
- improve access to a destination;
- avoid damaging high-value shared evidence.

Do not rank purely by visual severity.
