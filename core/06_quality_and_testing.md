Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-06 — Quality & Testing Doctrine

## 6.1 Test pyramid enforced per phase (TST-01)
| Level | Scope | Minimum per phase |
|---|---|---|
| Unit | Function/class | Every new function: happy path + validation failure (+ authz where applicable, TST-02) |
| Component | UI component / module in isolation | Every new UI component renders + interacts |
| Integration | Module ↔ DB ↔ external services | Every new transaction/CRUD end-to-end through real DB (test container) |
| System | Whole feature flows | Every use case main flow |
| End-user/UAT | Real user scenarios | Every use case alternate + exception flow scripted |
| Performance | Budgets (core/01) | Critical endpoints benchmarked |
| Security | SEC test cases | Every matrix row + injection suite |

## 6.2 Hard rules
- No silently skipped tests (DOD-03). A skip needs a ticket reference and an expiry.
- Coverage per DOD-04: ≥80% overall, 100% on critical paths.
- Every bug found gets: severity, root cause, fix, and a regression test (TST-05).
- Regression suite gates every commit (TST-03): red = no merge.

## 6.3 QA attributes file (TST-04) — per phase
Correctness, reliability, usability, performance, security, maintainability, portability —
each attribute gets: definition, metric, target, measured result, verdict.
