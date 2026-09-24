Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-03 — Phase Documentation (the complete artifact set)

When a phase is scheduled and has no folder yet: create `docs/phases/<phase-slug>/`
from `templates/` and fill **every** artifact below. Each artifact = one file, from its
template, interlinked, rolling up to the phase index and system entries (DOC-04).

## Required artifacts per phase
| # | Artifact | Template | Covers original rule |
|---|---|---|---|
| 1 | Implementation plan | `TEMPLATE_phase_implementation_plan.md` | (a), (l), (m) |
| 2 | Task todo (per task, + phase master todo) | `TEMPLATE_task_todo.md` | (m), (l) |
| 3 | Architecture delta (merged into main `architecture.md`) | section spec below | (c), (p) |
| 4 | Use case file — all functionality, every operation | section spec below | (d) |
| 5 | Use case descriptions + flow of actions + flow of events | section spec below | (e), (j) |
| 6 | Data flow diagram (with DB transactions) | section spec below | (f) |
| 7 | Non-functional requirements (metrics per function) | section spec below | (g) |
| 8 | QA file (quality attributes met) | section spec below | (h) |
| 9 | Security audit + specifications (per main security spec) | section spec below | (i) |
| 10 | State machine(s) — zero-to-end states, transitions, data | section spec below | (n) |
| 11 | Sequence diagram (separate file) | section spec below | (o) |
| 12 | Activity diagram (separate file) | section spec below | (o) |
| 13 | UI/UX specification (if UI involved; HCI-conformant) | section spec below | (k) |
| 14 | Test plan + test cases (all levels) | `TEMPLATE_test_plan.md` | (r) |
| 15 | Permissions/roles matrix | `TEMPLATE_permissions_matrix.md` | rule 8 |
| 16 | Phase audit + tracking | `TEMPLATE_phase_audit.md` | (b), rules 5/16 |

## Roll-up linkage (mandatory)
Each phase folder contains `_index.md` linking all 16 artifacts → linked from
`docs/phases/README.md` → linked from `development_phases_entry.md` → summarized in
`all_in_one_track.md`. The validator checks this chain (DOC-04).

## Content standards for specification-type artifacts (items 3–13)
Each must contain: purpose, scope, actors/roles, preconditions, main flow, alternate flows,
exception flows, postconditions, data entities touched (with tables/columns), invariants,
and open questions (COM-01 format). Diagrams as Mermaid in the md file (sequence/activity/state/DFD).

## Technology recommendation (original rule s)
For each phase, recommend the top best-fit current technology. Recommendation lives in the
implementation plan § "Technology decisions" with: options compared, choice, rationale,
and conformity check against the adapter's stack (ADP-01). If the best-fit differs from the
adapter stack, flag it for user decision — do not silently switch stacks.
