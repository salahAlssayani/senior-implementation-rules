Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# RULES_HINTS — System Adapter (binds ADMR to this system)

> Copy this file to the adopting system's repo root as `RULES_HINTS.md` and fill every
> section. The AI reads it at session start (ADP-01/02). Framework-specific rules live
> here ONLY — core rule files are never modified (ADP-03).

## 1. System identity
- Name: <system> · Version: <x.y.z> · Rules version pinned: <ADMR VERSION>

## 2. Stack
- Language/runtime: <> · Framework (backend): <> · Framework (frontend): <> · DB: <> · Cache/queue: <> · Infra: <>

## 3. Commands (must all exist and run green)
| Purpose | Command |
|---|---|
| Build | <e.g. make build / npm run build> |
| Lint | <> |
| Unit tests | <> |
| Full test suite | <> |
| Coverage report | <> |
| Migration run | <> |
| Migration rollback (rehearsal) | <> |
| Secret scan | <e.g. gitleaks detect> |
| Dependency vulnerability scan | <e.g. npm audit / govulncheck> |
| Dead-element scan | <system-specific inventory test> |
| Benchmark | <> |

## 4. Paths
- Base dirs: src/ <> · docs/phases/ <> · docs/sessions/ <> · tests/ <>
- Entry files present: ENTRY.md, RULES.md (in senior-rules/), mind_map.md, architecture.md,
  agents.md, memory.md, development_phases_entry.md, all_in_one_track.md, session_track.md, CHANGELOG.md
- Main security spec: <path> · Main architecture file: <path>

## 5. Conventions
- Branch prefix: <> · Module boundaries: <> · Naming: <> · Env/config management: <>

## 6. Overrides (may tighten, may NOT loosen without user approval)
- Coverage: <default ≥80% / 100% critical> · Perf budgets: <defaults from core/01 or stricter>
- Supported locales/RTL: <> · Accessibility target: <default WCAG 2.1 AA>

## 7. System-specific rules (stack-level only)
<SYS-01 …> e.g. "All SQL via sqlc-generated code", "All UI via the design-system package".

## 8. Sign-off
- Prepared by: <name/email> · Date: <> · Reviewed by: <>
