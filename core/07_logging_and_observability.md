Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-07 — Logging & Observability Doctrine (rule 13, hardened)

## 7.1 Relational log schema (LOG-01)
Split into related tables (exact DDL per system adapter):
- `users`, `user_sessions` — identity & session tracking
- `actions` — page, action type, pre-action context, action payload, post-action result
- `errors` — error type, stack/trace, correlation id, user/session FKs
- `activity_stats` — aggregated statistics per user type, action, page, time window
Every record: timestamp, actor FK, session FK, correlation id, result status.
Purpose: full reconstruction of any user's session for audit (LOG-04 drill).

## 7.2 Privacy & safety (LOG-02 — the gap in the original rule)
- Redact PII and secrets **before** persistence; scrubber enforced in the log pipeline.
- Retention & access-control policy documented; log tables readable only by admin/audit roles.

## 7.3 Fail-safe logging (LOG-03)
A logging failure must never fail the business operation: async writes, local spool,
dead-letter queue, and an alert when the log pipeline itself breaks.

## 7.4 Verification per phase
- Write-path tests prove every action type lands in the right table with relations.
- Failure-injection test proves fail-safe behavior.
- Audit drill: reconstruct one full user session from logs (LOG-04).
