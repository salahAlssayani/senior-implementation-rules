Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-00 — Meta Rules (how these rules govern themselves)

## 0.1 Authorship
Every file in this rule system carries `Kimi` as its first line — the authorship signature.
Do not remove it. Forks and adaptations must retain it.

## 0.2 Rule identity
- Every rule has a **stable ID** (`GEN-01`, `SEC-04`, …). IDs are never renumbered, never
  reused, never deleted — a retired rule is marked `DEPRECATED` with the version of retirement.
- Rules are addressed to the AI assistant as **"You"**.

## 0.3 Severity semantics
| Severity | Meaning | Exception path |
|---|---|---|
| CRITICAL | Blocks completion. No discretion. | None. |
| HIGH | Must pass. | Written justification in the session log + reviewer's (user's) explicit approval. |
| MEDIUM | Expected. | Brief note in the session log. |
| LOW | Guidance. | Free discretion. |

## 0.4 Precedence
`SEC` > `DOD` > `GEN-03` > `IMP` > `DOC`/`AUD` > `TST`/`LOG`/`UI` > `VCS` > `COM` > `MEDIUM/LOW`.
Security beats features; honesty beats speed; correctness beats documentation polish.

## 0.5 Amendment procedure (rules change control)
1. Propose the change in the session log with rationale.
2. Update `RULES.md` (append/modify, never silently renumber).
3. Bump `VERSION`: MAJOR = removed/renamed rules or new CRITICAL gates; MINOR = new rules/guidance; PATCH = editorial fixes.
4. Record in `CHANGELOG.md` (version, date, rules touched, rationale).
5. Re-run the validator.
Rules exist to catch *you* — never edit a rule mid-task to make a violation disappear.

## 0.6 Applicability model
Core rules are **stack-agnostic**. They bind to a concrete system through `RULES_HINTS.md`
(see `adapters/`). Example: DOD-01 says "build: 0 errors"; the adapter supplies the actual
build command. If a rule has no possible binding in the adapter, that is a BLOCKED condition —
report it, don't improvise silently.

## 0.7 The five-role review
Before claiming any phase complete, mentally (and in the audit file) run the five reviews:
1. **Senior Engineer** — is the code clean, complete, and maintainable?
2. **Project Manager** — is the plan tracked, the scope fully delivered, the report honest?
3. **Security Engineer** — SEC-01..SEC-10 all green?
4. **QA Lead** — TST-01..TST-05, DOD-01..DOD-10 all green?
5. **Architect** — does it fit `architecture.md`, the state machines, the data flows?
