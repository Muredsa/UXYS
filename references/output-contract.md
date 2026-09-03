# Human-Facing Output Contract

UXYS may use a complex internal route model, but the default report must be simple enough that a website owner can act without learning the model vocabulary.

## Default order

### 1. What the page is trying to do

One or two sentences.

State the page's apparent purpose and the main destination(s). If this is uncertain, say so.

### 2. Main visitor intents

Use a compact list. For each intent show its destination, not a long explanation.

Example:

- **Ready to act** → start signup.
- **Evaluate fit** → understand whether the product matches the need.
- **Compare options** → reach an informed comparison/choice.
- **Build confidence** → obtain enough proof to proceed.

Do not attach invented percentages.

### 3. Route snapshot

Show only the most important routes by default.

Format:

**Ready to act**  
Minimum sufficient: `Orientation → Action`  
Page exposes: `Orientation → Proof visual → Action`  
Issue: one extra attention/semantic step before the destination.

Prefer semantic stages over DOM selectors.

### 4. Screen-by-screen / section-by-section decisions

For each meaningful section, use block verdicts.

#### SCREEN 1 — Hero

**KEEP — Value proposition**  
Why: Required orientation for all modeled intents and currently clear.  
Helps: all intents.  
Change: none.

**DE-EMPHASIZE — Product proof visual**  
Why: Useful evidence for evaluation and confidence, but it competes with the direct action route for visitors already ready to start.  
Helps: Evaluate fit, Build confidence.  
Interferes with: Ready to act.  
Change: preserve the proof, but reduce its visual dominance or keep the CTA visually direct.

**EMPHASIZE — Primary action**  
Why: It is the destination for several routes but loses attention to nearby content.  
Helps: Ready to act, Evaluate fit after evidence.  
Change: make it the clearest actionable element in this decision area.

### 5. Top changes

Return approximately 3–7 actions, ordered by network-level impact.

Good:

1. Keep the proof block, but reduce its dominance in the first viewport so the direct signup path remains uninterrupted.
2. Move comparison detail after core product-fit evidence; it currently adds a decision branch too early.
3. Add one compact proof/result element before the final CTA for the confidence route.

Bad:

- Improve visual hierarchy.
- Simplify the page.
- Make the UX more intuitive.

### 6. Keep these

Explicitly protect high-value blocks that might look “unnecessary” from one fast route.

Example:

> **Do not remove the product proof visual.** It is unnecessary for the Ready-to-act route, but it is necessary/supporting evidence for evaluation and confidence. The problem is exposure, not existence.

This section prevents over-optimization toward an empty page.

### 7. Evidence / uncertainty

Only include limitations that change confidence.

Examples:

- “Only a desktop screenshot was available; mobile route order was not inspected.”
- “The CTA destination could not be opened, so the post-click route is outside this analysis.”
- “No observed analytics were supplied; all routes are predicted hypotheses.”

## Block verdict vocabulary

Use these exact primary actions unless the user requests another format:

- **KEEP**
- **EMPHASIZE**
- **ADJUST**
- **DE-EMPHASIZE**
- **MOVE**
- **REMOVE**
- **ADD**

Translate the labels when writing in another language if that improves comprehension, but preserve the conceptual distinction.

## Explain “why” in route language, not jargon

Prefer:

> This block is useful for visitors comparing options, but it appears before the direct action and creates an unnecessary choice for visitors already ready to proceed.

Avoid:

> The section has excessive salience and degrades hierarchical coherence.

## Scores

Do not default to a single UX score.

If a host system already provides measured or deterministic metrics, use them as supporting evidence and name what they measure.

Never create precise numeric scores merely to make the report look objective.

Prefer statements such as:

- 4 of 5 modeled intents have a sufficient route;
- comparison route contains several unnecessary exposed stages;
- confidence route is missing required proof;
- one high-value block interferes with two direct-action routes.

## Technical deep dive

Only when requested, add:

- intent × block role matrix;
- attention / semantic / action transition breakdown;
- cross-intent utility matrix;
- detailed counterfactual comparison;
- DOM/source evidence;
- predicted vs observed comparison;
- implementation notes.

Keep the default report decision-oriented.

## Language

Respond in the user's language unless asked otherwise.

Do not translate product labels, button text, URLs, or quoted interface copy when exact wording is evidence; quote them as they appear and explain them in the user's language.
