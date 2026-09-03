# Contributing to UXYS

Thanks for helping improve UXYS.

UXYS is a methodology skill, not a collection of generic UX tips. Contributions should strengthen the method's reliability, explainability, portability, or resistance to common reasoning failures.

## Principles for changes

A good methodology change should do at least one of these:

- reduce generic-checklist behavior;
- improve intent or destination modeling;
- improve shortest-sufficient-route reasoning;
- handle a real cross-intent conflict more correctly;
- reduce over-removal or false simplification;
- improve tool-grounded evidence collection;
- improve counterfactual redesign quality;
- improve the simplicity/actionability of final output;
- add a regression case for a demonstrated failure mode.

Avoid adding rules simply because they are common UX best practices. A rule belongs in UXYS only when it fits the intent/route architecture.

## Before opening a pull request

1. Read `SKILL.md` and the relevant files in `references/`.
2. Add or update a case in `evals/cases.md` for any behavioral change.
3. Keep `SKILL.md` procedural; put deep definitions and edge cases in `references/`.
4. Preserve the Predicted vs Observed boundary.
5. Do not add fake numeric scoring or user-prevalence claims.
6. Run:

```bash
python scripts/validate_skill.py
```

## Versioning

Use Semantic Versioning.

- PATCH: wording/bug fixes that preserve behavior.
- MINOR: backward-compatible capability or contract additions.
- MAJOR: incompatible change to the core method or output behavior.

For a versioned release:

1. update `VERSION`;
2. update the version badge in all three README files;
3. move release notes from `[Unreleased]` into a new changelog section;
4. run the validator;
5. after merge, publish a matching Git tag/release (`vX.Y.Z`) through GitHub.

## Languages

`SKILL.md` and `references/` are canonical in English to prevent three executable methodologies from drifting.

Public documentation is maintained in:

- `README.md` — English;
- `README.ru.md` — Russian;
- `README.zh-CN.md` — Simplified Chinese.

If public behavior, installation, versioning, or positioning changes, update all three READMEs.

## Pull request guidance

Keep PRs focused. Explain:

- the failure mode or capability gap;
- the method change;
- the eval case that demonstrates the expected behavior;
- whether the version should bump.

Methodology PRs without a concrete reasoning problem are likely to be rejected.
