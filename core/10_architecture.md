Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-10 — Architecture Doctrine

## 10.1 Models
- **C4** for structural views (context, containers, components) in `architecture.md`.
- **DDD** boundaries where the system warrants it; aggregates, invariants, and ownership
  rules documented per bounded context.
- Every phase appends an **architecture delta** section to the main `architecture.md`
  (what changed, why, alternatives rejected) — never a divergent side-file (DOC-04).

## 10.2 Required behavioral models per phase (original items n, o)
- **State machine(s)**: every entity with a lifecycle; states, events, guards, transitions,
  entry/exit actions; zero-to-end coverage with the data carried at each transition.
- **Sequence diagram** (separate file): one per critical operation, showing actors, layers,
  DB transactions, and failure paths.
- **Activity diagram** (separate file): one per use case, with swimlanes per actor/system.
- **DFD**: detailed data flows including DB transactions (level 1 minimum for new features).

## 10.3 Consistency rules
- Diagrams live in the phase folder as Mermaid inside md files; the main architecture file
  links them. Stale diagram = documentation drift = AUD-01 finding.
- New patterns need an ADR (Architecture Decision Record): context, decision, consequences.
