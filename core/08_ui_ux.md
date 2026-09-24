Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-08 — UI/UX Doctrine

## 8.1 Confirmation pattern (original rule 14 — strengthened)
- `alert()`, `confirm()`, `prompt()` are **forbidden** in production code (IMP-04; scan-enforced).
- One reusable confirmation modal component system-wide: title, message, consequence
  warning, confirm/cancel, keyboard accessible, focus-trapped, ARIA-dialog.
- The modal component itself has unit + a11y tests (L-2 gap fix).

## 8.2 HCI & accessibility (UI-01/02)
- Every phase with UI ships `uiux-<phase>.md`: heuristics review, task-effort estimates,
  error-message quality, consistency audit.
- WCAG 2.1 AA enforced: keyboard-only pass, visible focus, contrast ≥ 4.5:1, labelled
  controls, screen-reader path for critical flows. Automated axe/Lighthouse = 0 serious.

## 8.3 Internationalization & responsiveness (UI-03/04)
- No hardcoded user-facing strings; RTL layouts verified where the system requires them.
- Supported breakpoints matrix tested visually per phase.

## 8.4 Dead-UI prevention (IMP-01/02 + DOD-05)
- Every button/link/action rendered must map to a wired handler → real backend route.
- Automated inventory test diffs the UI element registry against the route/handler registry.
