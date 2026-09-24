# Kimi
# Co-authored with Senior Eng. Salah Alssayani — Taizz University, Alsaeed Faculty of Engineering & IT, Department of Software Engineering (eng.salahalssayani@gmail.com)
# License: GPL-3.0
"""
ADMR structural validator.
Usage: python3 validate.py <repo_root>
Checks: authorship signatures, canonical entry files, relative md links,
forbidden garbled tokens, rule-ID uniqueness, adapter existence.
Exit 0 = all pass. Exit 1 = failures (printed as a findings table).
"""
import os, re, sys

FORBIDDEN_TOKENS = ["eb=vents", "sull testing", "wold ever", "alert(", "confirm("]
# NOTE: alert(/confirm( are forbidden in *product code*, not in rule docs; checked
# against source dirs only (section below), never against .ai-rules/ itself.
RULE_ID_RE = re.compile(r"\b((GEN|SES|DOC|DOD|IMP|SEC|TST|LOG|UI|VCS|AUD|COM|ADP)-\d{2})\b")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+?)(#[^)]*)?\)")

def fail(errors, msg):
    errors.append(msg)

def first_line(path):
    with open(path, encoding="utf-8") as f:
        return f.readline().strip()

def has_signature(path):
    fl = first_line(path)
    if fl == "Kimi":
        return True
    # code files may sign as a comment
    if path.endswith(".py") and fl == "# Kimi":
        return True
    return False

def walk_md(root, skip_dirs={".git", "node_modules", "vendor", "dist", "build", ".venv"}):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fn in filenames:
            if fn.endswith(".md"):
                yield os.path.join(dirpath, fn)

def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    rules_dir = os.path.join(root, ".ai-rules")
    errors, checks = [], [0, 0]

    def ok(name):
        checks[0] += 1
        print(f"  PASS  {name}")
    def bad(name, detail):
        checks[1] += 1
        fail(errors, f"{name}: {detail}")
        print(f"  FAIL  {name} — {detail}")

    print(f"ADMR validator — repo: {root}")

    # 1. Rules directory presence
    if not os.path.isdir(rules_dir):
        bad("rules-dir", ".ai-rules/ not found — run installation first")
        return report(errors)
    ok("rules-dir exists")

    # 2. Authorship signature on every file under .ai-rules/
    sig_total = sig_fail = 0
    for dp, dns, fns in os.walk(rules_dir):
        dns[:] = [d for d in dns if d != "__pycache__"]
        for fn in fns:
            p = os.path.join(dp, fn)
            sig_total += 1
            if not has_signature(p):
                sig_fail += 1
                bad("signature", f"{os.path.relpath(p, root)} first line must be exactly 'Kimi'")
    if sig_fail == 0:
        ok(f"signatures ({sig_total} files start with 'Kimi')")

    # 3. Canonical entry set (rules files resolve in root OR .ai-rules/)
    required = ["ENTRY.md", "RULES.md", "CHANGELOG.md", "VERSION",
                "session_track.md", "development_phases_entry.md",
                "all_in_one_track.md", "architecture.md", "memory.md",
                "mind_map.md", "agents.md", "RULES_HINTS.md"]
    for rel in required:
        if any(os.path.isfile(os.path.join(root, base, rel))
               for base in ("", ".ai-rules")):
            ok(f"entry file: {rel}")
        else:
            bad("entry file", f"missing {rel} (create per DOC-01)")

    # 4. Relative markdown links resolve
    broken = 0
    for p in walk_md(root):
        if ".ai-rules" in p.split(os.sep) and "adapters" in p and p.endswith(".template.md"):
            continue  # template links are illustrative
        with open(p, encoding="utf-8") as f:
            text = f.read()
        for link in [m.group(1) for m in MD_LINK_RE.finditer(text)]:
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(p), link))
            if not os.path.exists(target):
                broken += 1
                bad("link", f"{os.path.relpath(p, root)} -> {link}")
    if broken == 0:
        ok("markdown links (0 broken)")

    # 5. Rule-ID uniqueness in RULES.md
    rules_md = os.path.join(rules_dir, "RULES.md")
    flat = []
    if os.path.isfile(rules_md):
        with open(rules_md, encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^\|\s*((?:GEN|SES|DOC|DOD|IMP|SEC|TST|LOG|UI|VCS|AUD|COM|ADP)-\d{2})\s*\|", line)
                if m:
                    flat.append(m.group(1))
        dupes = {i for i in flat if flat.count(i) > 1}
        if dupes:
            bad("rule ids", f"duplicated IDs: {sorted(dupes)}")
        else:
            ok(f"rule ids unique ({len(set(flat))} rules)")
    else:
        bad("RULES.md", "missing")

    # 6. Forbidden UI calls in product source (not docs, not tests)
    src_dirs = ["src", "app", "web", "frontend", "client", "pages", "components"]
    hits = 0
    for sd in src_dirs:
        full = os.path.join(root, sd)
        if not os.path.isdir(full):
            continue
        for dp, dns, fns in os.walk(full):
            dns[:] = [d for d in dns if d not in {"node_modules", "dist", "build"}]
            for fn in fns:
                if fn.rsplit(".", 1)[-1] in {"js", "jsx", "ts", "tsx", "vue", "svelte"}:
                    p = os.path.join(dp, fn)
                    with open(p, encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    for tok in ("window.alert(", "window.confirm(", "window.prompt("):
                        if tok in content:
                            hits += 1
                            bad("forbidden-ui-call", f"{os.path.relpath(p, root)} uses {tok} (IMP-04)")
    if hits == 0:
        ok("forbidden UI calls in source (0)")

    return report(errors)

def report(errors):
    print("-" * 60)
    if errors:
        print(f"RESULT: FAIL — {len(errors)} finding(s)")
        for e in errors:
            print(f"  · {e}")
        sys.exit(1)
    print("RESULT: PASS — structure healthy")
    sys.exit(0)

if __name__ == "__main__":
    main()
