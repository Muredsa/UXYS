---
name: uxys
description: Analyze or redesign a web interface with the UXYS intent-first method: multiple visitor intents, shortest sufficient routes, evidence, friction, cross-intent utility, and block-level actions. Use for UX audits, landing pages, product pages, dashboards, onboarding, checkout, screenshots, or live websites.
argument-hint: "[URL, screenshot, page, flow, or interface scope]"
---

# UXYS — User eXperience Yield System

Use UXYS to change **how** UX analysis is performed. Do not fall back to a generic UX checklist unless the user explicitly asks for one.

The core model is:

`INTENT → EVIDENCE → SHORTEST SUFFICIENT ROUTE → FRICTION → DESTINATION`

A strong interface is not one universally short funnel. It is a network of short **sufficient** routes for the important visitor intents, with minimal interference between those routes.

Read these references when their topic is needed:

- [`references/core-method.md`](references/core-method.md) — canonical definitions, phases, invariants, edge cases.
- [`references/block-utility.md`](references/block-utility.md) — cross-intent utility, route interference, and removal discipline.
- [`references/tool-workflows.md`](references/tool-workflows.md) — browser, screenshot, vision, DOM/source, image-editing, and implementation workflows.
- [`references/counterfactual.md`](references/counterfactual.md) — simulate redesigns without pretending predicted change is measured conversion lift.
- [`references/output-contract.md`](references/output-contract.md) — simple user-facing report structure.
- [`evals/cases.md`](evals/cases.md) — regression cases that define intended behavior.

## Non-negotiable invariants

1. **Start with intents, not defects.** Do not begin by hunting for weak CTAs, clutter, contrast, whitespace, trust, or other familiar audit items.
2. **Model several plausible intents.** Do not invent one “ideal user.” Usually infer 3–7 intents that are materially different.
3. **Never invent prevalence.** Without analytics or study data, intents are hypotheses, not percentages of real users.
4. **Give every intent a destination.** A route is meaningless without a concrete action or resolved state.
5. **Derive the shortest sufficient route before judging the actual layout.** Shortest means no unnecessary semantic steps; sufficient means the user still has enough evidence to decide.
6. **Block roles are intent-relative.** The same proof block may be a diversion for a visitor ready to act and necessary evidence for a visitor who needs confidence.
7. **Attention is not utility.** A visually dominant element can help, do nothing, or harm depending on the active intent.
8. **Do not optimize one route by silently damaging another.** Evaluate important recommendations across all modeled intents.
9. **Removal is a high-threshold action.** A block is not removable merely because one intent does not need it.
10. **Predicted is not observed.** Never claim eye-tracking, measured behavior, conversion lift, or real-user probability without observed data.
11. **Prefer evidence over scores.** Do not generate precise-looking numeric UX or attention scores unless they come from supplied measurements or a defined external scoring system.
12. **Show conclusions, not hidden reasoning.** Give concise rationale and inspectable evidence; do not dump internal chain-of-thought.

## Workflow

### Phase 0 — Establish evidence

Determine what you can inspect.

Prefer, when available:

1. a live page in a browser;
2. desktop and mobile renders;
3. screenshots of relevant states;
4. DOM / accessibility tree / source code;
5. real analytics or research explicitly supplied by the user.

If browser tools exist, inspect the real interface before concluding. Let fonts and visible media settle, scroll enough to expose lazy-loaded sections, and inspect responsive states when they matter. Do not treat a partially rendered capture as the page.

If only screenshots exist, analyze what is visible and mark anything dependent on unseen interaction or lower-page content as uncertain.

### Phase 1 — Orient to the page

Before criticism, establish:

- page/interface type;
- what it offers or enables;
- likely business or product objective;
- available primary actions and destinations;
- major semantic sections;
- any state or context that changes interpretation.

Summarize this in one short statement.

### Phase 2 — Infer visitor intents

Infer a compact set of materially different intents. Avoid synonyms that produce the same route.

Common examples include:

- ready to act;
- understand the offer;
- evaluate fit;
- compare options;
- understand price or conditions;
- build confidence / seek proof;
- resolve a specific objection;
- find a specific piece of information;
- continue an existing task.

For each intent define:

- **intent** — what the visitor is trying to resolve now;
- **destination** — the action or state that completes that intent on this interface;
- **required evidence** — what must be known or felt before the destination is reasonable.

Do not assign traffic shares unless real evidence supports them.

### Phase 3 — Derive the shortest sufficient route

Do this **independently of the page's current block order**.

Represent the route as semantic stages, not DOM nodes.

Example:

`Ready to act → orientation → destination`

A different intent may require:

`Build confidence → orientation → value → proof → objection resolution → destination`

Test sufficiency with this question:

> If a stage were removed, could this visitor still reasonably make the intended decision without a material information gap?

If yes, that stage is not required for the minimum sufficient route.

Do not confuse “shortest” with “fewest visible objects.” One semantic stage may be satisfied by several compact elements, and one large block may satisfy several stages.

### Phase 4 — Map actual page evidence

Segment the interface into meaningful blocks or screen-level sections. Do **not** create a route node for every `div`, icon, label, or decorative object.

For each important block and for each relevant intent, assign one role:

- **NECESSARY** — required to satisfy the route;
- **SUPPORTING** — not required, but materially helps the decision;
- **OPTIONAL** — potentially useful, but route quality barely depends on it;
- **DIVERSION** — captures attention or introduces choice that this intent does not currently need;
- **HARMFUL** — materially derails, obscures, delays, or contradicts progress toward the destination;
- **DESTINATION** — the route's completion point;
- **MISSING** — required evidence or stage is absent or impractically inaccessible.

A block may have different roles across intents. Preserve that distinction.

### Phase 5 — Trace three different transition types

Do not collapse all movement into one “user path.” Distinguish:

- **Attention transition** — what is likely to attract the next visual focus;
- **Semantic transition** — what idea, evidence, or question the interface presents next;
- **Action transition** — what the user can actually click, submit, open, or navigate to.

Example: text inside a product screenshot can attract attention and provide proof without being a clickable route node. Treat the parent visual as evidence; do not invent an action transition to pixels inside an image.

### Phase 6 — Compare sufficient route vs exposed route

For each intent, compare what is semantically required with what the page actually exposes before the destination.

Look for:

- missing required evidence;
- unnecessary semantic steps;
- premature actions before necessary context;
- competing calls to action;
- forced choices;
- visual attention that leaves the current route;
- semantic jumps;
- duplicated evidence;
- detours to another page when the current page could satisfy the stage;
- dead ends and return loops;
- important evidence appearing after the decision point;
- route obstruction from overlays, sticky UI, or responsive changes.

Call an element a diversion only in relation to a specific intent. “Not needed now” is not equivalent to “bad.”

### Phase 7 — Evaluate visual attention

Only after the route model exists, use visual hierarchy as evidence.

Consider, when visible:

- size and occupied area;
- contrast and color isolation;
- font size and weight;
- whitespace isolation;
- position in the viewport;
- imagery, faces, motion, video, novelty;
- sticky/fixed behavior;
- proximity and grouping;
- CTA affordance;
- density and simultaneous interactive targets;
- whether the first viewport makes the next useful step obvious.

Always ask:

> Where does this visual emphasis send this particular intent relative to its destination?

Do not translate qualitative visual judgment into fake percentages.

### Phase 8 — Compute cross-intent block utility

After evaluating individual routes, judge each significant block across all important intents.

Use two axes:

- **Cross-intent utility** — how much useful route work the block performs across intents;
- **Route interference** — how much unnecessary attention, choice, delay, or detour it creates for intents that do not need it.

Use this policy:

| Utility | Interference | Default interpretation |
|---|---|---|
| High | Low | Strong block: KEEP, sometimes EMPHASIZE |
| High | High | Valuable but intrusive: ADJUST, MOVE, or DE-EMPHASIZE |
| Low | Low | Optional: simplify or leave if harmless |
| Low | High | Strong REMOVE candidate |

Before recommending REMOVE, check all important intents. If a block is necessary for a meaningful route, prefer redesigning its exposure rather than deleting it.

Read [`references/block-utility.md`](references/block-utility.md) when removal or cross-intent conflict is central.

### Phase 9 — Generate counterfactuals for important conflicts

For a disputed block, reason through a small set of plausible interventions:

- remove;
- move earlier/later;
- reduce visual prominence;
- increase visual prominence;
- merge with adjacent evidence;
- collapse behind progressive disclosure;
- provide a direct bypass to the destination;
- rewrite so it satisfies more than one route stage.

Re-evaluate the important intents after each candidate change.

Reject a candidate that improves one route but materially degrades a more important route without explicit user approval.

If image-editing or code tools are available, create and inspect real variants rather than relying only on verbal imagination. See [`references/counterfactual.md`](references/counterfactual.md).

### Phase 10 — Produce block-level decisions

Translate the internal route analysis into simple actions:

- **KEEP** — useful and functioning well;
- **EMPHASIZE** — important evidence/action is too easy to miss;
- **ADJUST** — needed, but content, structure, or presentation is suboptimal;
- **DE-EMPHASIZE** — useful to some intents but over-exposed to others;
- **MOVE** — useful content appears at the wrong decision stage;
- **REMOVE** — low cross-intent utility with disproportionate interference;
- **ADD** — important intent lacks required evidence or destination access.

For each decision state:

1. what block/section you mean;
2. why, in 1–3 plain-language sentences;
3. which intents it helps;
4. which intents it interferes with, if any;
5. one concrete change.

Do not write vague recommendations such as “improve UX,” “increase engagement,” or “strengthen hierarchy” without saying exactly what to alter.

### Phase 11 — Prioritize

Do not return dozens of equal findings.

Choose approximately 3–7 changes with the highest expected structural value. Prefer changes that:

- improve multiple intents;
- fix missing necessary evidence;
- shorten a route without making it insufficient;
- reduce route interference;
- make an important destination easier to reach;
- simplify a high-friction decision;
- preserve or improve other important routes.

Also state what should **not** be removed when that prevents an obvious over-simplification mistake.

## Output default

Unless the user asks for a technical deep dive, present the result in this order:

1. **What this page is trying to accomplish** — 1–2 sentences.
2. **Main visitor intents** — concise list with destinations.
3. **Route snapshot** — minimum sufficient route vs exposed route for the important intents.
4. **Page-by-page / screen-by-screen review** — block-level KEEP / EMPHASIZE / ADJUST / DE-EMPHASIZE / MOVE / REMOVE / ADD decisions.
5. **Top changes** — 3–7 prioritized actions.
6. **Keep these** — useful blocks that might look removable from one route but have high cross-intent value.
7. **Uncertainty / evidence** — only where limitations materially affect confidence.

Use the user's language. Keep advanced route tables and model details secondary unless requested. Follow [`references/output-contract.md`](references/output-contract.md).

## Tool behavior

When browser, vision, image-editing, or source-code tools are available, use them when they materially reduce uncertainty. Do not ask the user to manually provide data you can inspect with an available authorized tool.

For redesign work, prefer a closed loop when possible:

`inspect → model intents/routes → identify conflict → generate variant → inspect variant → implement accepted variant → verify`

See [`references/tool-workflows.md`](references/tool-workflows.md).

## Observed data

If the user provides analytics, recordings, experiments, click/scroll data, or research:

- keep **PREDICTED** and **OBSERVED** evidence separate;
- use observed data to validate or falsify route hypotheses;
- do not retroactively describe model predictions as measurements;
- explicitly call out meaningful disagreement between predicted and observed routes.

## Stop conditions

Stop and qualify the analysis rather than guessing when:

- the relevant interface state cannot be inspected;
- a screenshot omits the section needed to judge a route;
- the destination is ambiguous and different destinations would change the verdict materially;
- an interaction must be tested but no interaction evidence is available;
- the recommendation depends on real user prevalence that has not been supplied.

If the ambiguity is small, proceed with explicit assumptions instead of blocking the entire analysis.

## What UXYS is not

UXYS is not:

- eye-tracking;
- a generic heuristic checklist;
- a Lighthouse replacement;
- an accessibility score (accessibility can be analyzed separately);
- a promise of conversion uplift;
- an excuse to remove every block not used by the fastest visitor;
- a single “ideal path” imposed on all users.

The method succeeds when the final advice explains **which visitor needs which evidence, where the page creates unnecessary route cost, and what concrete interface change improves the network of routes without damaging the rest of it**.
