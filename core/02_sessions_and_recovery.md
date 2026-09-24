Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-02 — Sessions, Tracking & Recovery

AI sessions die mid-flight. This doctrine guarantees **zero-context-loss resume**.

## 2.1 Session work files
- Location: `docs/sessions/`
- Name: `session-NNN-<slug>.md` (zero-padded, sequential, never reused).
- Content: goal, rules version, tasks attempted, **raw command outputs** (evidence),
  files touched, findings, blockers, next steps.
- CLI/terminal sessions are named after the work (e.g. `term-053-migration-test`) and
  listed inside the session file for cross-reference.

## 2.2 `session_track.md` (repo root) — the resume index
```markdown
| # | Date | Status | Tasks completed | Next task | Blockers | Session file |
|---|------|--------|-----------------|-----------|----------|--------------|
| 53 | 2026-09-18 | CLOSED | Phase 1-4 remediation | Final re-audit | none | docs/sessions/session-053-*.md |
| 54 | 2026-09-20 | OPEN   | …                 | …         | …        | …            |
```
Status: OPEN / CLOSED / BLOCKED.

## 2.3 Resume prompt (produced at every session end — SES-04)
A paste-ready block for the next session:
```markdown
RESUME PROMPT — paste into new session:
Read ENTRY.md, RULES.md, RULES_HINTS.md, session_track.md, and development_phases_entry.md.
Continue from session <NNN> (docs/sessions/session-NNN-*.md).
Next task: <exact task>. Last completed: <task>. Blockers: <none/list>.
Run validators/validate.py first and report its output before starting.
```

## 2.4 Failure recovery protocol
1. New session reads `session_track.md` → latest OPEN/BLOCKED row.
2. Opens the referenced session file; replays the evidence to establish ground truth.
3. Re-runs the validator + failing gate commands to reproduce state independently
   (**never trust the previous session's claims** — verify against the repo).
4. Only then continues implementation.
