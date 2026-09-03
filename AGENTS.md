# Repository Instructions for AI Contributors

This repository publishes the UXYS methodology as an installable agent skill.

## Source of truth

- `SKILL.md` is the executable entrypoint.
- `references/` contains canonical method detail.
- `evals/cases.md` defines behavioral regression expectations.
- `README.md`, `README.ru.md`, and `README.zh-CN.md` are public-facing documentation, not separate executable methodologies.

## Editing rules

When changing UXYS behavior:

1. Preserve the architecture: **Intent → Evidence → Shortest sufficient route → Friction → Destination**.
2. Do not replace intent-first reasoning with a generic UX checklist.
3. Preserve intent-relative block roles and cross-intent utility/interference.
4. Preserve the distinction between attention, semantic, and action transitions.
5. Preserve Predicted vs Observed separation.
6. Do not add unsupported numeric probabilities, user shares, or conversion uplift.
7. Add or update an eval case for any meaningful behavior change.
8. Keep the default output simpler than the internal method.

## Release discipline

If behavior changes materially, decide whether the version requires PATCH, MINOR, or MAJOR according to `CONTRIBUTING.md`.

For a release update:

- update `VERSION`;
- update `CHANGELOG.md`;
- update version badges in all three READMEs;
- run `python scripts/validate_skill.py`;
- keep installation/update instructions backward-compatible where possible.

## Scope discipline

Do not add unrelated application code, SaaS backend features, analytics collectors, or a scoring engine to this repository. UXYS here is a portable skill/method. Host-specific integrations belong in separate adapters or repositories unless they are small reference workflows.
