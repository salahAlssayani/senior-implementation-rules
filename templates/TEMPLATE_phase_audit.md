Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# Phase Audit & Tracking — <phase>

- Phase: <slug> · Audited in session <NNN> · Rules version: <v>

## 1. Gate results (DOD)
<G1..G9 table with PASS/FAIL + evidence links>

## 2. Findings (rules 16a–c)
| ID | Severity (CRITICAL/HIGH/MEDIUM/LOW) | Finding | Rule violated | Status | Fix evidence |
|---|---|---|---|---|---|
| F-01 | … | … | <rule id> | OPEN/FIXED | … |

## 3. Remediation waves (rule 16f)
- Wave 1: <CRITICAL+HIGH findings> — owner, ETA
- Wave 2: <MEDIUM/LOW> — …
Completion evidence required per wave; phase cannot close with open CRITICAL/HIGH.

## 4. Dead-element verification (rule 16e)
- Scan command + output: <attached>. Result: 0 dead buttons/links/routes/transactions.

## 5. Report (rules 5, 16d — Done / Remaining / Next)
- **Done:** <exact tasks with gate table>
- **Remaining:** <exact tasks>
- **Next:** <recommended next task + why>

## 6. Docs consistency (rule 16b, AUD-05)
- [ ] All base + docs + sessions md files updated and consistent with code
- [ ] Validator run: <output attached>
- [ ] Committed & pushed: <hash>
