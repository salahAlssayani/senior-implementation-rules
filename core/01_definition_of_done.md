Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-01 — Definition of Done (the completion gates)

"Done" is not a feeling. It is a table of gates, each with a number and a verification artifact.
A task failing **any** gate is INCOMPLETE — report it as such (DOD-10).

## Gate table

| Gate | Requirement | Default threshold | Proof artifact |
|---|---|---|---|
| G1 Build | Compile/build succeeds | 0 errors | Build log |
| G2 Lint | Static analysis clean | 0 errors, 0 unjustified warnings | Lint report |
| G3 Tests | Suites pass | 100% pass, 0 silent skips | Test output |
| G4 Coverage | Code covered | ≥ 80% overall; **100%** critical paths* | Coverage report |
| G5 Dead elements | No dead UI/routes/transactions | 0 (automated scan) | Scan report |
| G6 Security | Audit + scans clean | 0 CRITICAL/HIGH; 0 secrets | Audit + scanner output |
| G7 Performance | Budgets met | See defaults below | Benchmark output |
| G8 Docs | Phase artifacts exist/linked/current | DOC-02 checklist complete | Validator report |
| G9 Git | Committed, pushed, CI green | Conventional commits | CI status |

\* Critical paths = authentication, authorization, payments/money movement, core CRUD,
data transactions, anything the security audit flags critical.

## Default performance budgets (override in `RULES_HINTS.md`)
- API reads: p95 ≤ 500 ms · API writes: p95 ≤ 800 ms
- Page interactive: ≤ 3 s on throttled 4G · Time to first byte: ≤ 600 ms
- Frontend bundle: first load ≤ 250 KB gzipped (web) unless justified

## The honesty gate
DOD-10 is itself CRITICAL: misreporting gate status (claiming pass without the artifact)
is a GEN-03 violation — the single most serious failure mode of AI-assisted development.

## Completion report format (attach to every commit/phase)
```
GATE TABLE — <task id>
G1 Build     PASS  <command> -> 0 errors
G2 Lint      PASS  <command> -> 0 errors
G3 Tests     PASS  <N> tests, 0 failures
G4 Coverage  PASS  <X>% overall, 100% critical paths
G5 Dead scan PASS  0 dead elements
G6 Security  PASS  0 CRIT/HIGH findings
G7 Perf      PASS/FAIL  <numbers>
G8 Docs      PASS  validator: N/N checks
G9 Git       PASS  <commit hash>, CI green
Status: DONE | INCOMPLETE (gate: ___) | BLOCKED (reason: ___)
```
