Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-04 — Version Control Discipline

## 4.1 Model
Trunk-based development. `main` is always releasable.

## 4.2 Branches
- Pattern: `feat/<task-id>-<slug>` · `fix/<task-id>-<slug>` · `chore/<slug>` · `docs/<slug>` · `security/<slug>`
- Lifetime: hours-to-days, never weeks. Rebased on `main` before merge.

## 4.3 Commits
- Conventional Commits: `type(scope): subject` — feat, fix, chore, docs, test, refactor, security, perf.
- One logical change per commit; batching allowed only when commits are independently coherent.
- A commit message may claim **only** what its diff + attached gate table prove (VCS-04).
- Commit happens only when the DOD gates for that work pass.

## 4.4 Protected main
- No force-push, no history rewrite, no direct push of unverified code.
- Merge = gates green + validator green + docs updated in the same merge (DOC-05).

## 4.5 Releases
- Tags `vMAJOR.MINOR.PATCH`; `CHANGELOG.md` entry per release (VCS-05).
- Release checklist = AUD-06 (all system docs exactly up-to-date).

## 4.6 Evidence discipline
Raw command output (build, test, scan, validator) is pasted into the session file **before**
the commit that claims success (GEN-04).
