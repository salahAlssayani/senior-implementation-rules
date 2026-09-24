Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# Permissions & Roles — <feature/phase>

> Managed by the system admin (original rule 8). Enforcement is server-side (SEC-02);
> every row needs an automated authorization test.

| Role | Operation (CRUD/action) | Resource | Allow? | Enforcement point | Test id |
|---|---|---|---|---|---|
| admin | * | * | yes | middleware:<name> | AUTHZ-001 |
| manager | update | <resource> | yes | service:<method> | AUTHZ-002 |
| user | read | own:<resource> | yes | policy:<name> | AUTHZ-003 |
| guest | create | <resource> | no | 403 default | AUTHZ-004 |

## Notes
- UI hiding is presentation only — never counted as authorization.
- New roles/operations appended here in the same commit that adds the operation.
