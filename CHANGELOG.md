# Changelog

All notable changes to UXYS are documented here.

The project follows [Semantic Versioning](https://semver.org/). While the project is below `1.0.0`, the methodology is considered experimental.

## [Unreleased]

### Planned

- Additional page-type evals.
- More counterfactual redesign cases.
- Observed-vs-predicted validation patterns.

## [0.1.1] - 2026-09-04

### Fixed

- Fixed `SKILL.md` YAML frontmatter for strict skill registries by quoting the description and keeping only portable `name` / `description` metadata.
- Hardened the zero-dependency validator so invalid unquoted `: ` YAML scalars and unsupported frontmatter keys cannot silently pass CI again.

## [0.1.0] - 2026-09-04

### Added

- Initial public UXYS skill.
- Intent → Evidence → Shortest sufficient route → Friction → Destination core model.
- Multi-intent route analysis and intent-relative block roles.
- Attention / semantic / action transition separation.
- Cross-intent utility and route-interference model.
- Conservative block removal gate.
- Counterfactual redesign protocol.
- Browser, vision, DOM/source, image-editing, code-editing, and analytics tool workflows.
- Decision-oriented output contract with KEEP / EMPHASIZE / ADJUST / DE-EMPHASIZE / MOVE / REMOVE / ADD.
- Method regression cases.
- English, Russian, and Simplified Chinese public documentation.
- Semantic version file and automated repository validation.

[Unreleased]: https://github.com/Muredsa/UXYS/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/Muredsa/UXYS/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Muredsa/UXYS/releases/tag/v0.1.0
