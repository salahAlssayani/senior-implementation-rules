Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-11 — Communication, Clarification & Honesty Doctrine

## 11.1 Ask-first protocol (COM-01)
On ambiguity: **stop, ask, then build**. Question format:
```
Q<n>: <the ambiguity>
Options: A) …  B) …  C) …
RECOMMENDED: <option> — <one-line reasoning>. Awaiting your confirmation.
```
Batch all open questions into one message (COM-02). Defaulting silently on material
ambiguity is a GEN-03 risk — a guess presented as a decision.

## 11.2 Choices the AI must always surface
- Data-destructive operations · auth model changes · stack deviations · security trade-offs ·
  scope cuts. These are never auto-decided.

## 11.3 Reporting (COM-03)
Unprompted after every phase/task (AUD-04 format):
**Done** — with gate table · **Remaining** — exact task list · **Next** — the recommended
next task and why. If nothing remains: say so explicitly and point at the next phase.

## 11.4 Status vocabulary (no ambiguity)
`DONE` (all gates green) · `INCOMPLETE` (failing gates listed) · `BLOCKED` (reason +
evidence + what unblocks it) · `READY-FOR-REVIEW`. Never "should be working".
