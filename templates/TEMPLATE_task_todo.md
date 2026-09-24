Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# Task Todo — <task id>: <title>

> Every box must be checked or the task is INCOMPLETE (GEN-02, rule 12 of origin).
> Each step, when finished, must conform to system specs: no missing implementation,
> no errors, no bugs, no dead elements (DOD gates at bottom are mandatory).

## Implementation steps
- [ ] 1. <step — exact, verifiable>
- [ ] 2. <step>
- [ ] …

## Wiring verification (rules 6–7)
- [ ] Every button/link/action wired to a real backend handler
- [ ] 0 dead buttons / links / routes / DB transactions (automated scan attached)
- [ ] Permissions enforced server-side for each operation (matrix row referenced)

## Gates (paste outputs as evidence — GEN-04)
- [ ] G1 Build: <command> → 0 errors
- [ ] G2 Lint: <command> → clean
- [ ] G3 Tests: <command> → 100% pass
- [ ] G4 Coverage: <command> → ≥80% / 100% critical
- [ ] G5 Dead-element scan: <command> → 0
- [ ] G6 Security: audit + scans → 0 CRIT/HIGH, 0 secrets
- [ ] G7 Performance: budgets met
- [ ] G8 Docs: artifacts updated in same commit
- [ ] G9 Git: conventional commit pushed, CI green

## Status
DONE | INCOMPLETE (gate ___) | BLOCKED (reason + evidence)
