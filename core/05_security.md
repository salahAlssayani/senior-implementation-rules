Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# CORE-05 — Security Doctrine

The system's own security specification (main security md file) is the supreme security
reference; this doctrine is the baseline every system inherits. Where the system spec is
stricter, the stricter rule wins (GEN-07: SEC precedence).

## 5.1 Secrets management (SEC-01)
- Secrets live in environment/secret managers only. Repo contains **zero** secrets.
- `.env*` gitignored on day zero; committed `.env.example` with placeholder values documents required keys.
- Pre-commit + CI secret scanning (gitleaks or equivalent). Any hit = stop, rotate, purge history, then continue.

## 5.2 Identity & access (SEC-02)
- AuthN on every non-public endpoint; AuthZ checked **server-side per operation** against the
  permissions matrix (`TEMPLATE_permissions_matrix.md`).
- UI hiding is not authorization. Every role × action cell in the matrix has an enforcement test.

## 5.3 Injection & input defense (SEC-03)
- Parameterized queries / ORM bindings only; never string-concatenated SQL.
- Input validation at the boundary (schema validation), output encoding at rendering.
- Command/path/template injection defenses; if the system uses LLM features, prompt-injection
  defenses per the system security spec.

## 5.4 Per-phase security audit (SEC-04)
Artifact `security-audit-<phase>.md`: assets, threat model (STRIDE-lite), attack surface,
findings table (severity, status), mitigations, residual risk. 0 open CRITICAL/HIGH at phase close.

## 5.5 Supply chain (SEC-06)
- Pinned dependencies + lockfile committed. Vulnerability scan in CI = 0 exploitable CRIT/HIGH
  or documented exception with expiry date.

## 5.6 Transport & data (SEC-07/08)
- TLS everywhere; secure headers (CSP, HSTS, X-Frame-Options…); minimal CORS allowlist.
- Rate limiting + brute-force protection on auth surfaces.
- Sensitive data encrypted at rest; passwords: slow salted hashing only.

## 5.7 Resilience (SEC-09)
- Automated backups; restore drill evidence per phase; RPO/RTO defined in system NFRs.
- Security incident register (SEC-10): every incident, near-miss, exception — logged, dated, dispositioned.
