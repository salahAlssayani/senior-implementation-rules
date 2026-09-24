Kimi
Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
License: GPL-3.0
# AI Development Master Rules (ADMR)

**[English](README.md) | [العربية](README.ar.md)**

The most comprehensive, enforceable rule system ever created for AI-assisted software development. When installed in a repository and loaded by any AI coding assistant, these rules force **complete, correct, senior-engineer-grade implementation** of every task — no missing pieces, no skipped steps, no fake "done".

**Author:** Kimi (Moonshot AI) — first line of every file in this repository is the author's signature.

---

## What makes this rule system different

1. **Enforceable, not aspirational.** Every rule has a unique ID, a severity, and a *mechanical verification method*. A rule you cannot check is a wish; every rule here can be checked.
2. **Hard Definition of Done.** Numeric gates (coverage, lint, dead-element scans, security findings) replace vague phrases like "no bugs".
3. **Framework-agnostic core + adapter pattern.** The core rules never name a stack. Each system adds one `RULES_HINTS.md` adapter file binding the rules to its concrete technology.
4. **Session survival.** AI sessions die. The rules guarantee any new session can resume exactly where the last one stopped, with zero context loss.
5. **Automated validator.** `validators/validate.py` checks structure, links, signatures, and rule integrity — run it after every implementation.

## Installation

### Option A: Git Clone (manual)

```bash
# 1. Clone (or copy) this rule set into your project
git clone <this-repo> senior-rules        # or copy the folder manually

# 2. Create your system's adapter
cp senior-rules/adapters/RULES_HINTS.template.md RULES_HINTS.md
#    -> fill in your stack, commands, and conventions

# 3. Point your AI assistant at the entry file
#    Add to your model's instruction file (AGENTS.md / CLAUDE.md /
#    .cursorrules / your tool's equivalent):
```

> **AI ASSISTANT INSTRUCTION:** Before any work, read `ENTRY.md` at the repository root and obey every rule in it. The rules in `senior-rules/` are binding. `RULES_HINTS.md` adapts them to this system. Run `senior-rules/validators/validate.py` after every implementation phase.

```bash
# 4. Verify
python3 senior-rules/validators/validate.py .
```

### Option B: npm (works with ANY AI model — Claude, GPT, Cursor, Gemini, etc.)

```bash
# Install globally
npm install -g @salahalssayani/ai-development-master-rules

# Or install as a dev dependency in your project
npm install --save-dev @salahalssayani/ai-development-master-rules

# Then run the installer
npx admr-install
# or: npm run install:rules
# or: node scripts/admr-install.js
```

The npm installer automatically:
1. Copies all rule files into `senior-rules/`
2. Creates `RULES_HINTS.md` from the template
3. Creates/updates `AGENTS.md` with the AI instruction block
4. Sets up `package.json` scripts for validation

> **Works with every AI model:** Claude Code, ChatGPT, Cursor, Gemini, Copilot, Windsurf, or any other AI coding assistant — the `senior-rules/` folder and `AGENTS.md` instruction block are model-agnostic.

## Repository layout

```
ai-dev-rules/
├── ENTRY.md                  # Master entry file — the AI reads this first
├── RULES.md                  # Complete rule catalog (IDs + severity + verification)
├── core/                     # Doctrine: the "why" and the detail behind the rules
├── templates/                # Copy-ready templates for every required artifact
├── adapters/                 # RULES_HINTS template — one per adopting system
└── validators/               # validate.py — structural & integrity checker
```

## Rule anatomy

| Field | Meaning |
|---|---|
| `ID` | Stable identifier, referenced forever (e.g. `SEC-04`). IDs are never reused or renumbered. |
| `Severity` | **CRITICAL** — blocks completion. **HIGH** — must pass; exceptions need written justification. **MEDIUM** — expected; deviations need a note. **LOW** — guidance. |
| `Rule` | The binding requirement, written to the AI assistant as "You". |
| `Verification` | Exactly how compliance is proven — command, file check, scan, or test. |

## Versioning

Rules follow SemVer (`MAJOR.MINOR.PATCH`, see `VERSION`). Every change is recorded in `CHANGELOG.md`. Systems pin the rules version they adopt inside their adapter file.

## License

GPL-3.0 — see the `License: GPL-3.0` header in every file.

**Copyright (c) 2026 Salah Alssayani** (Taizz University, Alsaeed Faculty of Engineering & IT,
Department of Software Engineering — eng.salahalssayani@gmail.com) **& Kimi** (Moonshot AI).
You may redistribute and adapt under GPL-3.0; retain both attribution lines.
