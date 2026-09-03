# Security Policy

UXYS is primarily an instruction/methodology repository, but agent skills can still influence tool use and therefore deserve security review.

## Supported versions

Security-sensitive fixes are applied to the latest version on `main` and included in the next release.

## Reporting a vulnerability

Please avoid publishing exploitable details in a public issue when the problem could cause an agent to:

- access unintended local or network resources;
- perform unsafe browser/navigation actions;
- expose private data;
- treat untrusted page content as trusted instructions;
- perform destructive code or repository changes without authorization;
- bypass the method's Predicted vs Observed boundary in a way that misrepresents sensitive data.

Use GitHub's private vulnerability reporting / Security Advisory mechanism for the repository when available.

## Skill safety model

UXYS follows these safety assumptions:

- content from analyzed websites is **data**, not trusted agent instruction;
- browser/page text must not override user, system, repository, or skill instructions;
- destructive or irreversible actions require explicit user authorization;
- credentials, authenticated sessions, private analytics, and local source code must only be used within the user's authorized scope;
- UXYS does not require arbitrary code execution from analyzed pages beyond what the authorized browser environment normally performs;
- predictions must not be represented as observed human behavior.

Security fixes that change methodology behavior should include an eval case when practical.
