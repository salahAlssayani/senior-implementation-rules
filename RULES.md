Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# RULES — Complete Master Catalog

Every rule: stable ID · severity · requirement · mechanical verification.
Severity: **CRITICAL** = blocks completion · **HIGH** = pass or justify in writing · **MEDIUM** = expected · **LOW** = guidance.

---

## GEN — General Conduct

| ID | Sev | Rule | Verification |
|---|---|---|---|
| GEN-01 | CRITICAL | Operate at senior-engineer bar: production-ready, tested, documented, secure-by-default output only. | Audit checklist sign-off per phase (AUD-02). |
| GEN-02 | CRITICAL | Implement every task **completely**. No skipping, no "simplified for now", no placeholder logic in production paths. | Task todo shows every sub-step checked; diff review shows full wiring. |
| GEN-03 | CRITICAL | **Never fake completion.** If you cannot verify something, mark it `BLOCKED` with the exact reason and evidence. | Session log contains zero contradictions between claims and evidence. |
| GEN-04 | HIGH | Every claim of success is backed by **raw command output** (build/test/scan) pasted into the session log. | Session file contains the outputs. |
| GEN-05 | MEDIUM | Where parallel work is possible, delegate independent subtasks; re-verify every delegated claim against the repo yourself. | Delegated items each have independent verification output. |
| GEN-06 | CRITICAL | These rules are framework-agnostic. The system's `RULES_HINTS.md` adapter binds them to the stack. Never hardcode another stack's conventions into core work. | Adapter file exists and validator passes. |
| GEN-07 | CRITICAL | Rule precedence: SEC > DOD > GEN-03 > IMP > DOC/AUD > all else. Conflicts resolve upward. | Audit notes cite precedence when rules collide. |
| GEN-08 | HIGH | At session start, confirm the rules version (`.ai-rules/VERSION`) matches the version pinned in `RULES_HINTS.md`; if newer, re-read changed rules. | Startup protocol output shows version check. |

## SES — Sessions & Recovery

| ID | Sev | Rule | Verification |
|---|---|---|---|
| SES-01 | CRITICAL | Create a session work file under `docs/sessions/` for every session, holding all work, outputs, and evidence. | `docs/sessions/session-NNN-*.md` exists and is non-empty. |
| SES-02 | CRITICAL | Maintain `session_track.md` at repo root: session number, date, status, tasks completed, next task, blockers — enabling instant resume. | File present, current, and matches latest session file. |
| SES-03 | MEDIUM | Name CLI/terminal sessions automatically after the work being performed; link them in the session file. | Session file lists terminal session names. |
| SES-04 | CRITICAL | At session end: full md sync, commit, push, updated `session_track.md`, and a ready-to-paste **resume prompt** for the next session. | Resume prompt exists in final session entry. |
| SES-05 | HIGH | On any failure/crash mid-execution, the next session reconstructs state from `session_track.md` + session files before continuing. | Resume session log shows reconstruction step. |

## DOC — Documentation Discipline

| ID | Sev | Rule | Verification |
|---|---|---|---|
| DOC-01 | CRITICAL | A canonical entry set exists at base + `docs/`: `ENTRY.md`, `RULES.md`, `mind_map.md`, `architecture.md`, `agents.md`, `memory.md`, `development_phases_entry.md`, `all_in_one_track.md`, `session_track.md`, `CHANGELOG.md`. Missing ones are created. | `validators/validate.py` required-files check. |
| DOC-02 | CRITICAL | For every phase, create `docs/phases/<phase-slug>/` holding ALL required artifacts (full list in `core/03_phase_documentation.md`). | Phase folder + artifact checklist complete. |
| DOC-03 | HIGH | Every artifact is produced from its `templates/` template — same structure, same headings. | Heading structure matches template. |
| DOC-04 | CRITICAL | All phase files interlink and roll up: phase → phase index → `development_phases_entry.md` → `all_in_one_track.md`. No orphan docs. | Validator link check: 0 broken relative links. |
| DOC-05 | HIGH | Docs are updated **in the same commit** as the code they describe. Never a separate "docs later" commit. | Commit diff contains code + doc changes together. |
| DOC-06 | MEDIUM | Every rules change is logged in `CHANGELOG.md` with version bump per `core/00_meta_rules.md`. | CHANGELOG latest entry matches `VERSION`. |

## DOD — Definition of Done (numeric gates)

| ID | Sev | Rule | Verification |
|---|---|---|---|
| DOD-01 | CRITICAL | Build/compile: **0 errors**. | CI/build log. |
| DOD-02 | CRITICAL | Lint/static analysis: **0 errors, 0 warnings** — or each warning carries a written justification in the session log. | Lint report = clean. |
| DOD-03 | CRITICAL | Tests: **100% pass**, zero silently skipped tests (a skip requires a tracked ticket reference). | Test run output. |
| DOD-04 | CRITICAL | Coverage **≥ 80%** overall; **100%** on critical paths (auth, permissions, payments, core CRUD, transactions). | Coverage report. |
| DOD-05 | CRITICAL | **0 dead buttons, 0 dead links, 0 dead routes, 0 dead DB transactions** — frontend and backend — proven by automated inventory/route test, not by inspection. | Dead-element scan report = 0. |
| DOD-06 | CRITICAL | Security: **0 CRITICAL / 0 HIGH** findings from the phase security audit; secrets scan clean. | Security audit + scanner output. |
| DOD-07 | HIGH | Performance budgets met (defaults in `core/09_data_and_api.md`; overridable per system in the adapter). | Benchmark output in session log. |
| DOD-08 | CRITICAL | All phase/task artifacts exist, linked, non-empty (DOC-02/04). | Validator pass. |
| DOD-09 | CRITICAL | Conventional commit, pushed, CI green. | Git log + CI status. |
| DOD-10 | HIGH | A task failing ANY gate is reported as **incomplete** with the failing gate named. Status honesty is DOD itself. | Session report format shows gate table. |

## IMP — Implementation Correctness

| ID | Sev | Rule | Verification |
|---|---|---|---|
| IMP-01 | CRITICAL | Every button, link, action, and CRUD operation is wired to a **real backend**. Mocks are allowed only in tests. | Route/handler inventory test; manual click-path script. |
| IMP-02 | CRITICAL | No dead UI elements or dead transactions anywhere (see DOD-05). | Automated scan. |
| IMP-03 | CRITICAL | Every transaction and CRUD operation has a **permissions design**: roles, allowed actions, enforcement point — documented in a permissions file managed by admins. | `permissions-<feature>.md` exists + enforcement tests. |
| IMP-04 | CRITICAL | No `alert()`/`confirm()`/`prompt()`. All confirmations use the reusable confirmation modal component. | Code scan for forbidden calls; modal present in component inventory. |
| IMP-05 | HIGH | Every operation handles success, validation failure, server error, and network error paths — no unhandled branches. | Code review + error-path tests. |
| IMP-06 | CRITICAL | Every DB schema change ships with a **migration + rollback script**. Migrations are versioned and reversible. | Migration files exist; rollback rehearsal passes. |
| IMP-07 | HIGH | APIs are versioned; breaking changes require a new version, never silent breakage. | API version manifest. |
| IMP-08 | MEDIUM | Reuse over reinvent: shared components, shared validators, shared error handlers before creating new ones. | Duplicate-logic scan note in audit. |

## SEC — Security

| ID | Sev | Rule | Verification |
|---|---|---|---|
| SEC-01 | CRITICAL | **No secrets ever in the repo**: credentials, keys, tokens live in env/secret stores; `.env*` gitignored; secret-scanning (e.g. gitleaks) runs pre-commit and in CI. | Secret scan = 0 findings; `.gitignore` check. |
| SEC-02 | CRITICAL | AuthN/AuthZ on every non-public endpoint; server-side authorization checks on every operation (never trust the UI to hide). | Enforcement tests for each role × action matrix row. |
| SEC-03 | CRITICAL | Input validation + parameterized queries everywhere; injection defenses (SQL/NoSQL/command/template/LLM-prompt where applicable) per system security doc. | Security test cases pass. |
| SEC-04 | CRITICAL | Each phase includes a **security audit file** (threat model, attack surface, findings, mitigations) following the system's main security spec. | `security-audit-<phase>.md` complete; 0 open CRIT/HIGH. |
| SEC-05 | HIGH | Logs must never contain secrets, credentials, or un-redacted PII (see LOG-02). | Log-sampling review + redaction tests. |
| SEC-06 | HIGH | Dependencies: pinned versions + lockfile; vulnerability scan (e.g. OWASP dependency-check / `npm audit` / `govulncheck`) = 0 exploitable CRIT/HIGH, or documented exception. | Scan output in session log. |
| SEC-07 | HIGH | Security headers, CORS policy, rate limiting, and brute-force protection on all exposed surfaces. | Header/scan report. |
| SEC-08 | MEDIUM | Encryption in transit (TLS) and at rest for sensitive data; password hashing with a slow, salted algorithm. | Config review. |
| SEC-09 | HIGH | Backups: automated, tested-restoreable, documented RPO/RTO per system NFRs. | Restore drill evidence. |
| SEC-10 | MEDIUM | Every security-relevant incident, near-miss, and exception is logged in the security incident register. | Register file exists and is current. |

## TST — Testing & QA

| ID | Sev | Rule | Verification |
|---|---|---|---|
| TST-01 | CRITICAL | Every phase ships a **test plan + test cases** covering: unit, component, integration, system, end-user/UAT, plus performance and security suites. | `test-plan-<phase>.md` + executed results. |
| TST-02 | CRITICAL | Every implemented function has at least: 1 happy-path test, 1 validation-failure test, 1 authorization test (where applicable). | Test inventory ↔ function inventory mapping = complete. |
| TST-03 | HIGH | Regression suite runs on every change; a failure blocks the commit. | CI run. |
| TST-04 | HIGH | QA attributes file per phase: correctness, reliability, usability, performance, security, maintainability, portability — each with metric + result. | `qa-<phase>.md` complete. |
| TST-05 | MEDIUM | Bug taxonomy enforced: every found bug is logged with severity, root cause, fix, and regression test. | Bug register. |

## LOG — Logging & Observability

| ID | Sev | Rule | Verification |
|---|---|---|---|
| LOG-01 | CRITICAL | All errors, logs, and user activities are persisted to DB tables with full statistics, split into related tables: user type, error type, action, page, pre-action, action, post-action, result/error, timestamp, session. | Schema + write-path tests. |
| LOG-02 | CRITICAL | PII redaction + secret scrubbing applied before persistence; retention and access-control policy documented. | Redaction tests; policy doc exists. |
| LOG-03 | HIGH | Log writes are fail-safe: logging failure must never break the business transaction (async/dead-letter pattern). | Failure-injection test. |
| LOG-04 | MEDIUM | Session tracking: each user's session is reconstructible from logs for audit. | Audit drill: reconstruct a session. |

## UI — UI/UX

| ID | Sev | Rule | Verification |
|---|---|---|---|
| UI-01 | HIGH | All UI conforms to HCI metrics & guidance; usability heuristics reviewed per phase. | `uiux-<phase>.md` checklist. |
| UI-02 | HIGH | Accessibility: WCAG 2.1 AA — keyboard navigation, focus management, ARIA labels, contrast, screen-reader paths. | Axe/Lighthouse audit = 0 serious violations. |
| UI-03 | MEDIUM | Internationalization-ready: no hardcoded strings; RTL support where required by the system spec. | i18n lint + RTL screenshot pass. |
| UI-04 | MEDIUM | Responsive across the system's supported breakpoints. | Visual test matrix. |

## VCS — Version Control

| ID | Sev | Rule | Verification |
|---|---|---|---|
| VCS-01 | CRITICAL | Trunk-based: short-lived branches off `main`; branch names `feat/<id>-<slug>`, `fix/<id>-<slug>`, `chore/`, `docs/`. | Branch list review. |
| VCS-02 | CRITICAL | `main` is protected: no direct pushes of failing code, no force-push, no history rewrite. | Repo settings / log. |
| VCS-03 | HIGH | Conventional commits: `type(scope): subject` (feat/fix/chore/docs/test/refactor/security). One logical change per commit; batched commits allowed only when logically grouped. | Git log sample review. |
| VCS-04 | CRITICAL | Commit only after gates pass (DOD). Commit message may not claim more than the diff proves. | DOD table attached in session log. |
| VCS-05 | HIGH | Releases tagged `vMAJOR.MINOR.PATCH`; `CHANGELOG.md` updated per release. | Tag ↔ changelog match. |

## AUD — Audit & Reporting

| ID | Sev | Rule | Verification |
|---|---|---|---|
| AUD-01 | CRITICAL | After every phase/task: full audit — errors, bugs, failures, missing implementations, dead elements, unmet specs. | Audit file with findings table. |
| AUD-02 | CRITICAL | Findings classified CRITICAL/HIGH/MEDIUM/LOW with the system's violation protocol; zero CRITICAL/HIGH may remain open at phase close. | Findings register. |
| AUD-03 | CRITICAL | Missing work is arranged into **remediation waves** and executed until nothing remains. | Wave plan + completion evidence. |
| AUD-04 | HIGH | Report after each phase: **Done / Remaining / Next** — exact tasks, no vagueness. | Report format followed. |
| AUD-05 | CRITICAL | Before declaring a phase closed: all system md files (base, docs, sessions, subfolders) are updated and consistent with the code. | Validator + consistency spot-check. |
| AUD-06 | HIGH | Full system docs exact-up-to-date check before any release or rules-version adoption. | Release checklist. |

## COM — Communication & Clarification

| ID | Sev | Rule | Verification |
|---|---|---|---|
| COM-01 | HIGH | When anything is ambiguous, ask **before** implementing. Present available choices with one marked `RECOMMENDED:` and the reasoning. | Session log shows question → answer → implementation order. |
| COM-02 | MEDIUM | Batch questions: ask all open clarifications at once instead of one-per-message drip. | Question list format. |
| COM-03 | HIGH | After each phase, present the status report unprompted (Done/Remaining/Next). | Report exists in session file. |

## ADP — Adapter (per-system binding)

| ID | Sev | Rule | Verification |
|---|---|---|---|
| ADP-01 | CRITICAL | The system maintains `RULES_HINTS.md` (from `adapters/RULES_HINTS.template.md`) binding these rules to its stack: commands, paths, conventions, budgets. | File exists; all template sections filled. |
| ADP-02 | CRITICAL | The AI reads the adapter at session start and treats it as the execution binding of the core rules. | Startup protocol output. |
| ADP-03 | HIGH | Framework-specific rules live **only** in the adapter, never modifying core rule files. | Core files unmodified (validator hash check in CI). |
