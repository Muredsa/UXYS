# Core Method Reference

This file is the canonical conceptual reference for UXYS. `SKILL.md` defines the executable workflow; this document clarifies terms, edge cases, and invariants.

## 1. Unit of analysis

UXYS analyzes an interface as a **network of intent-dependent routes**, not as a flat collection of components.

A route is semantic. It answers: what must this visitor understand, verify, decide, or do before reaching a destination?

Do not equate route stages with DOM elements. A route stage may be satisfied by one block, several compact elements, or an interaction state.

## 2. Intent

An intent is the visitor's immediate unresolved job on the current interface.

Good intents are behaviorally distinct enough to require different evidence or routes. Examples:

- ready to act;
- understand the offer;
- evaluate fit;
- compare options;
- understand price/conditions;
- build confidence;
- resolve an objection;
- find specific information.

Bad intent sets are duplicates with different wording, such as “learn more,” “understand product,” and “discover product” when they all require the same route.

Without observed data, do not estimate traffic share.

## 3. Destination

Every intent has a destination: the action or resolved state that completes the current job.

Destinations may be:

- submit/register/buy/contact;
- reach a specific answer;
- choose a plan;
- confirm compatibility;
- understand how a feature works;
- navigate to a legitimate next step.

The business conversion is not always the destination for every intent. For a research intent, the correct destination may be “understand pricing well enough to decide whether to continue.”

## 4. Evidence

Evidence is anything the interface uses to move an intent toward its destination.

Examples:

- value proposition;
- product capability;
- price or condition;
- demonstration;
- proof/result/case;
- trust signal;
- objection answer;
- comparison;
- instruction;
- status/feedback;
- CTA or direct action.

Evidence can be visual, textual, interactive, or structural.

## 5. Shortest sufficient route

The shortest sufficient route is the minimum sequence of semantic stages that lets a specific intent reach its destination without a material decision gap.

Two errors must be avoided:

### Under-shortening

Removing evidence merely to reduce steps.

Example: `H1 → Buy` is short but insufficient for a visitor who needs proof before committing.

### Over-lengthening

Forcing evidence on a visitor who no longer needs it.

Example: a visitor ready to register is made to traverse feature details, cases, blog links, and comparisons before the primary action is visually accessible.

Use the removal test:

> If this stage disappears, can this intent still reasonably reach the destination with enough context to decide?

If yes, the stage is not required in the minimum route.

## 6. Exposed route

The exposed route is what the current page places in the visitor's perceptual and semantic path before the destination.

It is not necessarily a single deterministic sequence. Treat it as the most relevant ordered evidence plus meaningful branches and competing signals.

Do not invent a precise transition probability unless a real model or observed dataset provides one.

## 7. Friction

Friction is route cost that does not proportionally help the current intent.

Common classes:

- **choice friction** — unnecessary decision among competing actions;
- **attention friction** — strong focal point unrelated to the current route;
- **semantic friction** — abrupt topic/context shift;
- **navigation friction** — required evidence lives behind avoidable navigation;
- **interaction friction** — form/state mechanics make progress harder;
- **evidence friction** — proof exists but is hard to find, decode, or trust;
- **responsive friction** — mobile/desktop layout changes route accessibility;
- **obstruction** — overlays/sticky elements physically hide useful evidence/action.

Friction is intent-relative. A comparison table may be necessary evidence for one intent and choice friction for another.

## 8. Block roles

Roles are assigned per intent, never globally first.

### NECESSARY

The route becomes materially insufficient without this block or equivalent evidence.

### SUPPORTING

Improves confidence, comprehension, or decision quality, but the minimum route can survive without it.

### OPTIONAL

Potentially useful, but low route impact for this intent.

### DIVERSION

Consumes attention or introduces a branch the intent does not currently need. A diversion may still be valuable elsewhere.

### HARMFUL

Creates substantial derailment, contradiction, obstruction, or avoidable route cost.

### DESTINATION

Completes the route.

### MISSING

Required evidence or an actionable destination is absent or practically inaccessible.

## 9. Three transition layers

UXYS must keep these separate:

### Attention transition

What is likely to attract the next visual focus.

### Semantic transition

What idea/evidence the interface makes salient next.

### Action transition

What the visitor can actually do next.

A screenshot inside a hero can contain visually prominent words and metrics. Those pixels can influence attention and semantics without being interactive destinations.

## 10. Shared evidence

The best blocks often serve multiple intents at once.

Example: a compact product demonstration may help:

- understand the offer;
- evaluate fit;
- build confidence.

Shared evidence has high cross-intent utility. Prefer strengthening or restructuring such blocks instead of duplicating route-specific content.

## 11. Route interference

Route interference occurs when evidence or actions useful to one intent disproportionately interrupt another intent.

This is not automatically a defect. The design problem is often exposure, order, prominence, or bypassability rather than existence.

Example: a detailed proof visual may be necessary for “build confidence” but can visually delay the direct CTA for “ready to act.” A better solution may keep the proof while preserving a direct action route.

## 12. Cross-intent optimization

A change is globally strong when it improves several important routes or fixes a serious route gap without materially degrading the others.

Never optimize one route in isolation unless the user explicitly prioritizes that intent.

If the user supplies business priorities, treat them as route weights. Do not invent weights yourself.

## 13. Page segmentation

Segment by meaningful visual/semantic sections, not arbitrary DOM boundaries.

Typical sections:

- header/navigation;
- hero;
- benefits/features;
- demonstration/how it works;
- proof/cases/reviews;
- comparison/pricing;
- objection handling/FAQ;
- final CTA;
- footer/utility.

On long pages, reason screen-by-screen or section-by-section so the report remains actionable.

## 14. Interaction states

A page URL may have multiple UX states:

- menu closed/open;
- modal hidden/open;
- tab selected;
- form empty/error/success;
- checkout step;
- carousel state;
- authenticated/anonymous state.

If an intent depends on a state, inspect or explicitly scope it. Do not assume the static first render fully describes the experience.

## 15. Mobile vs desktop

Do not treat mobile as a smaller screenshot of desktop.

Responsive changes may alter:

- evidence order;
- CTA visibility;
- navigation exposure;
- sticky elements;
- information density;
- interaction cost;
- whether a supporting block becomes a diversion because it consumes an entire viewport.

Model routes separately when the structure materially changes.

## 16. Predicted vs observed

### Predicted

Derived from interface evidence, visual hierarchy, semantics, and model reasoning.

### Observed

Derived from real analytics, experiments, user studies, event logs, or recordings.

Keep labels explicit. When they disagree, report the disagreement instead of forcing the prediction to look correct.

## 17. Quality criteria for a UXYS analysis

A strong analysis is:

- intent-specific;
- evidence-grounded;
- route-based;
- cross-intent aware;
- conservative about deletion;
- clear about uncertainty;
- concrete in recommendations;
- stable enough that repeated inspection of the same unchanged page yields materially similar intents and priority findings;
- understandable without exposing the full internal model.

A weak analysis is a familiar UX checklist with UXYS vocabulary pasted on top.
