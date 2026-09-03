# Counterfactual UX Protocol

Counterfactual analysis asks:

> If this block were changed, how would the network of intent routes change?

It is a structured design hypothesis, not an A/B test and not measured conversion lift.

## When to use it

Use counterfactual analysis when:

- a block has high utility and high interference;
- removal is tempting but cross-intent value is unclear;
- two actions compete for attention;
- required evidence appears at the wrong stage;
- the user asks what to change rather than only what is wrong;
- image/code tools allow the variant to be rendered and inspected.

Do not simulate dozens of arbitrary redesigns. Start from a specific route conflict.

## Candidate interventions

For one disputed block, consider only plausible low-dimensional changes:

1. **Remove** — eliminate the block.
2. **Move** — change when it appears in the semantic sequence.
3. **De-emphasize** — preserve access while reducing attention capture.
4. **Emphasize** — make necessary evidence or destination easier to detect.
5. **Merge** — combine redundant or complementary evidence.
6. **Progressive disclosure** — keep optional depth accessible without exposing it to every route.
7. **Direct bypass** — preserve the block but keep an uninterrupted path for visitors ready to act.
8. **Rewrite** — make the same block satisfy more intents or route stages.

## Evaluation loop

For each serious candidate:

1. Keep the same intent set unless the change fundamentally alters the product/task.
2. Re-check the destination for each intent.
3. Re-check whether the minimum sufficient route changed semantically.
4. Re-map the variant's exposed route.
5. Re-evaluate the changed block's role per intent.
6. Re-evaluate cross-intent utility and interference.
7. Check whether any new evidence gap, choice, or diversion was created.
8. Compare the variant with the current design using qualitative route effects.

## Comparison vocabulary

Prefer:

- shorter / longer exposed route;
- sufficient / insufficient;
- less / more route interference;
- stronger / weaker destination access;
- removes / creates a choice point;
- preserves / loses required evidence;
- improves / degrades shared evidence leverage;
- clearer / less clear semantic sequence.

Avoid unsupported statements such as:

- “conversion will increase 18%”;
- “users will be 32% more likely to click”;
- “attention probability becomes 0.81.”

Unless those values come from a real model or experiment supplied in context, they are false precision.

## Cross-intent guardrail

Never choose a variant only because it produces the shortest route for the fastest intent.

Example:

Current proof block:

- Ready to act: DIVERSION
- Evaluate fit: SUPPORTING
- Build confidence: NECESSARY

Removing it may improve Ready to act while making Build confidence insufficient.

A better candidate may be:

- keep the proof;
- ensure the CTA is directly visible;
- reduce proof dominance for the first viewport;
- preserve full proof for visitors who continue evaluating.

## Use real visual variants when possible

If image editing or code execution is available, prefer inspecting rendered variants over purely verbal speculation.

Suggested loop:

`current screenshot → targeted edit → variant screenshot → same UXYS analysis → compare`

If source code is available and implementation is requested:

`current → targeted code change → render → inspect → adjust → verify`

## Multi-candidate selection

When comparing several candidates, choose the one that produces the best network-level tradeoff:

- fixes the target issue;
- improves or preserves multiple important intents;
- does not remove necessary evidence;
- reduces route interference;
- avoids creating new dominant diversions;
- is proportionate to the problem.

If candidates trade off different intents and no business priority is known, present the tradeoff instead of inventing a single objectively “best” design.

## Counterfactual output

Keep it compact:

**Current conflict**  
What happens and for which intents.

**Candidate change**  
What would be altered.

**Likely route effect**  
Which routes become shorter, clearer, or less sufficient.

**Tradeoff**  
What useful evidence or route could weaken.

**Recommendation**  
Adopt / reject / test, with one sentence why.

When real experiments are available later, explicitly distinguish the original counterfactual prediction from the observed result.
