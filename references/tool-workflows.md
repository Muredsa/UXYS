# Tool Workflows

UXYS is a reasoning method first. Tools increase evidence quality; they do not replace the method.

Use the strongest workflow the host environment supports.

## 1. Live browser workflow

Use for a public URL or a locally running interface when browser control is available.

### Capture protocol

1. Open the requested page in a clean session.
2. Confirm the final URL and visible page state.
3. Let fonts and visible media settle.
4. Inspect the initial viewport before scrolling.
5. Scroll through the full page in controlled steps so lazy-loaded content can render.
6. Inspect important sticky/fixed/overlay behavior.
7. Capture or retain enough full-page context to segment meaningful sections.
8. Repeat on a mobile viewport when responsive behavior is relevant.
9. Interact only when an intent depends on a state: menu, tab, form, modal, checkout step, etc.
10. Do not submit destructive, paid, private, or irreversible actions unless the user explicitly requested and authorized them.

Do not use “network idle” as the only proof that a modern page is visually stable. Long-lived requests and delayed media can make it unreliable. Prefer actual visual/DOM readiness signals available in the host.

### What to record conceptually

- major sections;
- primary and secondary actions;
- order of evidence;
- viewport-level visual dominance;
- available action transitions;
- route changes after responsive rearrangement;
- overlays/obstructions;
- interaction states required to complete an intent.

## 2. Screenshot + vision workflow

Use screenshots to judge visual attention and hierarchy, not to invent interaction semantics.

### Rules

- Analyze the page as rendered, not as an imagined design system.
- Treat OCR text inside images as visual/semantic evidence unless DOM or interaction inspection proves it is separately interactive.
- Do not claim a pixel-level element is clickable merely because it resembles a UI control inside a screenshot.
- Prefer full-context screenshots plus viewport/section crops when long-page scaling makes details unreadable.
- Compare desktop and mobile separately when layout/order changes.

### Useful questions

- What wins first attention in this viewport?
- Is that focal point useful to the selected intent now?
- Does the primary destination compete with proof, navigation, imagery, promotion, or utility controls?
- Is supporting evidence visible at the moment it is needed?
- Does a lower-value block consume disproportionate visual area?

Vision judgment is evidence within the route model, not a substitute for intent modeling.

## 3. DOM / accessibility tree / source workflow

Use structural inspection to verify what visual inspection cannot safely infer.

Helpful evidence:

- link/button destinations;
- form actions and fields;
- element labels;
- heading hierarchy;
- DOM order versus visual order;
- hidden/collapsed content;
- interactive vs decorative controls;
- sticky/fixed positioning;
- source component boundaries;
- responsive conditions.

Do not turn UXYS into a DOM lint report. Structural evidence matters only when it changes the route, accessibility of evidence, or interpretation of a block.

## 4. Image-editing workflow

When image editing is available and the user wants redesign help, use it for **counterfactual visualization**.

Preferred sequence:

1. Identify one high-value route conflict.
2. Define a small, reversible change.
3. Edit the screenshot or create a visual variant.
4. Re-run the same intent/route questions on the variant.
5. Compare what improved and what became worse.
6. Show the user the variant and the tradeoff.

Examples:

- reduce a proof visual so the direct CTA remains dominant;
- move a comparison block after core explanation;
- strengthen a necessary CTA;
- collapse optional detail;
- remove a low-utility promotion;
- insert missing trust evidence.

Do not present the edited image as proof of real conversion improvement.

## 5. Source-code editing workflow

When the user provides or authorizes a repository and asks to implement a redesign:

`inspect → model → propose → implement → render → verify`

After implementation:

- render the real page again;
- verify the changed block visually and functionally;
- re-evaluate the affected intents;
- check mobile/responsive impact;
- ensure the change did not create new route interference.

Avoid rewriting unrelated components merely to satisfy a UX suggestion.

## 6. Analytics / observed-data workflow

If real behavior data is available, create two separate views:

### PREDICTED

What UXYS inferred from the interface.

### OBSERVED

What the supplied data actually shows.

Then compare:

- predicted strong destinations vs actual click/navigation events;
- predicted diversions vs observed exits/branches;
- predicted missing evidence vs repeated backtracking or information-seeking;
- desktop/mobile predictions vs device-specific observed behavior.

Do not infer gaze from mouse movement unless the underlying research method explicitly justifies it.

Do not claim causal effects from observational data alone.

## 7. When tools disagree

Prefer the evidence appropriate to the question:

- DOM proves whether something is actually interactive;
- screenshot/vision proves what is visually prominent;
- source proves implementation/state logic;
- analytics proves observed events within its coverage;
- none of these alone proves user motivation.

If visual evidence and DOM semantics disagree, report the distinction rather than forcing one layer to explain the other.

## 8. Efficient tool use

Do not collect everything merely because a tool can.

Use tools to answer uncertainty that can change a route verdict.

Examples:

- Need to know if the “button” inside a hero screenshot is clickable? Inspect DOM.
- Need to know whether a CTA is actually visible before a proof block on mobile? Render mobile.
- Need to know whether moving a section improves cross-intent balance? Create a counterfactual variant.

This keeps UXYS focused on decision-relevant evidence instead of producing a giant technical audit.
