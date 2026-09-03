# UXYS Method Regression Cases

These cases are conceptual evals. A methodology change should preserve the expected behavior unless the change intentionally redefines the method.

## Case 1 — Proof that distracts one route but is needed by another

Page: SaaS hero with a strong product-results visual and a primary “Start” CTA.

Intents:
- Ready to act → start signup.
- Build confidence → see credible proof, then start signup.

Expected:
- Proof visual is a **DIVERSION or SUPPORTING** element for Ready to act depending on its dominance.
- Proof visual is **NECESSARY or strong SUPPORTING** evidence for Build confidence.
- UXYS must **not** recommend removal solely because it adds a step to Ready to act.
- Preferred recommendation is usually preserve proof while keeping a direct CTA route, or de-emphasize/reposition proof if it dominates.

Failure: “The proof block is not on the shortest route, remove it.”

## Case 2 — Shortest is not sufficient

Page: expensive service with H1, CTA, cases, guarantees, process, FAQ.

Intent: Build confidence before requesting a quote.

Expected:
- `H1 → CTA` is rejected as insufficient.
- Minimum sufficient route includes orientation/value plus credible proof or risk reduction before the action.
- Cases/guarantees are judged by whether they provide required evidence, not by page length alone.

Failure: optimizing only for fewest blocks.

## Case 3 — Low utility + high interference

Page: landing page with a large unrelated newsletter promotion placed between core value and the primary CTA.

Intents: Ready to act, Understand offer, Evaluate fit, Build confidence.

Expected:
- Newsletter promo has low utility for these page intents and high route interference.
- **REMOVE**, **MOVE**, or strong **DE-EMPHASIZE** is justified.
- Recommendation explains which routes it interrupts.

Failure: keeping it merely because it is visually polished.

## Case 4 — Image contents are not fake action nodes

Page: hero contains a screenshot of another dashboard with visible tabs and labels; the screenshot itself is not interactive.

Expected:
- Vision may treat internal labels as attention/semantic evidence.
- DOM/interaction evidence prevents UXYS from inventing action transitions to those labels.
- Parent screenshot can still be proof, supporting evidence, or a diversion depending on intent.

Failure: “User will click the admin-wiki tab” when it is only pixels.

## Case 5 — Helpful to one intent, intrusive to another

Page: pricing comparison table appears before basic product explanation.

Intents:
- Compare options → comparison table is NECESSARY.
- Understand offer → early comparison can be DIVERSION or premature choice.

Expected:
- UXYS identifies route interference, not an absolute good/bad block.
- Likely action: MOVE or restructure sequence, not remove comparison capability.

## Case 6 — Missing route evidence

Page: novel product explains features and immediately asks for payment, but provides no proof, demo, guarantee, or trust evidence.

Intent: Build confidence.

Expected:
- Mark a **MISSING** evidence stage.
- Recommend **ADD** with the kind of evidence needed.
- Do not “solve” the route by simply making the purchase CTA stronger.

## Case 7 — Observed data contradicts prediction

Prediction: a secondary card is likely to divert users from the primary CTA.
Observed data supplied by user: repeated experiment shows the card is rarely used and primary CTA behavior is stable.

Expected:
- Keep PREDICTED and OBSERVED separate.
- Explicitly say the observed evidence weakens/falsifies the diversion hypothesis.
- Do not rewrite history as if UXYS predicted the observation.

## Case 8 — Mobile route differs

Desktop: CTA sits next to proof visual.
Mobile: proof visual becomes a full-screen section before CTA.

Expected:
- Model mobile separately.
- A block can be SUPPORTING on desktop but high-interference on mobile because exposure cost changed.

## Case 9 — Avoid generic checklist regression

Prompt: “Analyze this landing page with UXYS.”

Expected first reasoning structure:
1. page purpose;
2. intents and destinations;
3. shortest sufficient routes;
4. actual evidence/routes;
5. block roles and cross-intent conflicts;
6. concrete actions.

Failure opening: “The CTA should have more contrast, whitespace could improve, add testimonials...” before route modeling.

## Case 10 — Do not invent quantitative behavior

No analytics or calibrated scoring model supplied.

Expected:
- qualitative predictions and confidence language;
- no “73% of users,” “0.82 attention probability,” or invented conversion uplift.

Failure: false precision presented as measured behavior.
