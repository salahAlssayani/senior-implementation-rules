Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CHANGELOG — AI Development Master Rules

Follows SemVer per core/00_meta_rules.md §0.5.

## [2.0.0] — 2026-09-20
Complete professional rebuild of the original rule set (Taizz University, Eng. Salah Alssayani).
- **Fixed**: all typos and garbled phrases ("flow of eb=vents", "sull testing", "wold ever",
  "CEM"); unified the rule voice to address the AI as "You".
- **Fixed**: triple-duplicated update/commit/push instructions merged into single rules
  (VCS/DOC/AUD); overlapping report rules merged (AUD-04).
- **Added**: numeric Definition of Done (DOD-01..10) with 9 gates; version-control
  discipline (VCS-01..05); secrets management (SEC-01); CI/CD gate enforcement;
  data migration + rollback (IMP-06); API versioning (IMP-07); dependency supply-chain
  scanning (SEC-06); backup/DR (SEC-09); PII redaction + retention in logs (LOG-02);
  fail-safe logging (LOG-03); performance budgets (DOD-07); rule versioning + amendment
  procedure + precedence order (GEN-07, core/00); BLOCKED-not-fake-done protocol (GEN-03);
  adapter pattern for framework-agnostic adoption (ADP-01..03, adapters/);
  automated validator (validators/validate.py); copy-ready templates (templates/).
- **Preserved**: every original rule intent — sessions & recovery, per-phase artifact set
  (a–u), no-dead-elements, real-backend CRUD, permissions matrices, relational activity
  logging, confirmation-modal-only UI, audit waves, ask-first clarification, doc roll-up
  linkage, technology recommendations, five-role completion review.
