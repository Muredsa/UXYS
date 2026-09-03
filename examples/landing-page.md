# Worked Example — SaaS Landing Page

This example demonstrates the *shape* of UXYS reasoning without depending on a real brand.

## Page

A SaaS landing page has:

1. header navigation;
2. hero value proposition;
3. large product-results screenshot;
4. primary “Start project” CTA;
5. feature explanation;
6. case studies;
7. pricing;
8. FAQ;
9. final CTA.

The product-results screenshot is visually dominant and contains convincing metrics, but is not itself interactive.

## 1. Likely intents

### Ready to act

Destination: start project/signup.

Minimum sufficient route:

`Orientation → Primary action`

### Understand the offer

Destination: understand what the product does well enough to decide whether to continue.

Minimum sufficient route:

`Orientation → Core mechanism/value → Next step`

### Evaluate fit

Destination: decide whether the product fits the visitor's use case.

Minimum sufficient route:

`Orientation → Capabilities → Relevant proof/conditions → Decision`

### Build confidence

Destination: obtain enough evidence to trust the product and proceed.

Minimum sufficient route:

`Orientation → Value → Proof → Risk/objection resolution → Action`

## 2. Intent-relative block roles

| Block | Ready to act | Understand | Evaluate fit | Build confidence |
|---|---|---|---|---|
| Hero value proposition | NECESSARY | NECESSARY | NECESSARY | NECESSARY |
| Product-results screenshot | DIVERSION/SUPPORTING | SUPPORTING | SUPPORTING | NECESSARY |
| Primary CTA | DESTINATION | SUPPORTING | DESTINATION after evidence | DESTINATION |
| Features | OPTIONAL | NECESSARY | NECESSARY | SUPPORTING |
| Cases | DIVERSION | OPTIONAL | SUPPORTING | NECESSARY |
| Pricing | SUPPORTING | OPTIONAL | NECESSARY when price matters | SUPPORTING |
| FAQ | OPTIONAL | OPTIONAL | SUPPORTING | NECESSARY only for relevant objections |

## 3. Key conflict

The product-results screenshot is useful evidence, but it visually dominates the first decision area.

For **Ready to act**, it adds attention/semantic cost before the direct action.

For **Build confidence**, removing it would damage the route because the screenshot provides concrete proof.

Therefore:

**Do not remove it merely because it distracts Ready-to-act visitors.**

## 4. Counterfactuals

### Candidate A — remove proof screenshot

- Ready to act: route becomes cleaner.
- Build confidence: route loses required proof.
- Evaluate fit: loses useful evidence.

Verdict: reject.

### Candidate B — keep screenshot, make CTA visually direct

- Ready to act: direct destination remains obvious.
- Evaluate fit: proof remains available.
- Build confidence: necessary evidence remains intact.

Verdict: strong candidate.

### Candidate C — move all proof far below the fold

- Ready to act: clean route.
- Build confidence: proof becomes expensive to find.

Verdict: weaker tradeoff than B.

## 5. Human-facing output

### SCREEN 1 — Hero

**KEEP — Value proposition**  
Why: It orients every modeled intent and explains why the visitor is in the right place.  
Change: none unless the wording is unclear in the actual page.

**DE-EMPHASIZE — Product-results visual**  
Why: It is valuable evidence for evaluation and confidence, but it can visually interrupt visitors who are already ready to start.  
Helps: Evaluate fit, Build confidence.  
Interferes with: Ready to act.  
Change: keep the proof, but preserve a visually direct path to the primary CTA.

**EMPHASIZE — Primary action**  
Why: It is a destination for multiple routes and should remain immediately identifiable even when proof is visually rich.  
Change: ensure it is the strongest actionable element in this decision area.

## 6. What not to do

Do not conclude:

> “The screenshot is distracting, so remove it.”

That optimizes one route and breaks another.

The UXYS conclusion is:

> Preserve the block's cross-intent value while reducing route interference for visitors who do not need that evidence yet.
