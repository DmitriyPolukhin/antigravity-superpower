---
name: Superpower
description: The ultimate agentic coding workflow (Brainstorm -> Worktree -> Plan -> Execute)
version: 3.0.0 (Full Port)
---

# 🦸 Superpower V3.0 (Full Port)

This skill is a **Meta-Router**. It connects you to 14 specialized modules for disciplined software engineering.

## 🧭 Navigation
Depending on your current task, load the appropriate module by reading the Markdown file.

| Phase | Task | Module (Path to read) |
|-------|------|-----------------------|
| **1. Init** | Brainstorming features | `~/.gemini/skills/superpower/modules/brainstorming/SKILL.md` |
| | Creating isolated workspace | `~/.gemini/skills/superpower/scripts/worktree.py` (Run script) |
| **2. Plan** | Writing implementation plans | `~/.gemini/skills/superpower/modules/writing-plans/SKILL.md` |
| **3. Execute** | **Standard TDD Loop** | `~/.gemini/skills/superpower/modules/test-driven-development/SKILL.md` |
| | **Agent-Driven Dev** (Complex) | `~/.gemini/skills/superpower/modules/subagent-driven-development/SKILL.md` |
| | Systematic Debugging | `~/.gemini/skills/superpower/modules/systematic-debugging/SKILL.md` |
| **4. Review** | Requesting Code Review | `~/.gemini/skills/superpower/modules/requesting-code-review/SKILL.md` |
| **5. Finish** | Merging/Cleaning up | `~/.gemini/skills/superpower/modules/finishing-a-development-branch/SKILL.md` |

## 🕹️ Quick Actions

### 🌳 New Feature (Clean Workspace)
1. Run `python3 ~/.gemini/skills/superpower/scripts/worktree.py <feature-name> auto`
2. `cd` into the new directory.
3. Start Brainstorming.

### 📝 Plan First
Before writing ANY code, you MUST write a plan using `writing-plans` (or the `scripts/plan.py` helper).

### 🔴🟢 TDD Only
You are forbidden from writing implementation code without a failing test. Use `scripts/verify.py` to check yourself.

## 📜 Full Module List
- `brainstorming`
- `writing-plans`
- `executing-plans`
- `subagent-driven-development`
- `test-driven-development`
- `systematic-debugging`
- `verification-before-completion`
- `requesting-code-review`
- `receiving-code-review`
- `using-git-worktrees`
- `finishing-a-development-branch`
- `dispatching-parallel-agents`
- `writing-skills`
- `using-superpowers`

To use any module: `view_file ~/.gemini/skills/superpower/modules/<module-name>/SKILL.md`
