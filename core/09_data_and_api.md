Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-09 — Data, Transactions & API Doctrine

## 9.1 Migrations (IMP-06)
- Every schema change = versioned `up` + `down` script, applied through the system's migration tool.
- Rollback is **rehearsed**, not theoretical — evidence in the session log.
- Destructive changes require: backup confirmation + expand/contract pattern note.

## 9.2 Transactions
- Multi-write operations are atomic; failure rolls back completely.
- Every transaction is represented in the phase DFD and state machine (CORE-03 items 6, 10).

## 9.3 API discipline (IMP-07)
- Versioned APIs (`/v1/...`); breaking change = new version; deprecations announced in CHANGELOG.
- Contracts documented (OpenAPI/GraphQL schema); contract tests in the integration suite.

## 9.4 Performance budgets
Defaults in `core/01_definition_of_done.md`; the adapter may tighten, not loosen, without user approval.
