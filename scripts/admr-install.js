#!/usr/bin/env node
/**
 * admr-install — Install ADMR rules into any project via npm.
 * Usage: npx @salahalssayani/ai-development-master-rules
 *        or: npm run install:rules
 *        or: node scripts/admr-install.js
 */
const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const RULES_SRC = path.join(__dirname, '..');
const TARGET_DIR = path.join(process.cwd(), 'senior-rules');

function copyDir(src, dest) {
  if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);
    if (entry.isDirectory()) {
      copyDir(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

function main() {
  console.log('═══ ADMR Installer v2.0.0 ═══');
  console.log(`Source: ${RULES_SRC}`);
  console.log(`Target: ${TARGET_DIR}`);
  console.log();

  // Check if target already exists
  if (fs.existsSync(TARGET_DIR)) {
    console.log('⚠  senior-rules/ already exists. Backing up to senior-rules-backup/');
    const backup = path.join(process.cwd(), 'senior-rules-backup');
    if (fs.existsSync(backup)) fs.rmSync(backup, { recursive: true });
    fs.renameSync(TARGET_DIR, backup);
  }

  // Copy all rules files
  copyDir(RULES_SRC, TARGET_DIR);
  console.log('✓ Rules copied to senior-rules/');

  // Create RULES_HINTS.md from template
  const templatePath = path.join(TARGET_DIR, 'adapters', 'RULES_HINTS.template.md');
  const hintsPath = path.join(TARGET_DIR, 'RULES_HINTS.md');
  if (fs.existsSync(templatePath) && !fs.existsSync(hintsPath)) {
    fs.copyFileSync(templatePath, hintsPath);
    console.log('✓ RULES_HINTS.md created from template');
  }

  // Create AGENTS.md instruction if it doesn't exist
  const agentsPath = path.join(process.cwd(), 'AGENTS.md');
  if (!fs.existsSync(agentsPath)) {
    const agentsContent = `# AI Assistant Instructions

> **AI ASSISTANT INSTRUCTION:** Before any work, read \`ENTRY.md\` at the repository root and obey every rule in it. The rules in `senior-rules/` are binding. `RULES_HINTS.md` adapts them to this system. Run `senior-rules/validators/validate.py` after every implementation phase.

---

## Installed via npm: @salahalssayani/ai-development-master-rules v2.0.0
`;
    fs.writeFileSync(agentsPath, agentsContent);
    console.log('✓ AGENTS.md created with AI instruction');
  } else {
    console.log('ℹ  AGENTS.md already exists — add the AI instruction manually if needed');
  }

  console.log();
  console.log('═══ Installation Complete ═══');
  console.log('Next steps:');
  console.log('  1. Edit senior-rules/RULES_HINTS.md with your stack details');
  console.log('  2. Run: python3 senior-rules/validators/validate.py .');
  console.log('  3. Start working with your AI coding assistant');
}

main();
