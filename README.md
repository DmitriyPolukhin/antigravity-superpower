# 🦸 Superpower for Antigravity (Gemini)

> **The ultimate agentic workflow, ported to Antigravity.**
> Based on the original [Superpowers for Claude Code](https://github.com/obra/superpowers) by [@obra](https://github.com/obra).

This is a full port of the disciplined software engineering capability system ("Skills") for the Antigravity (Gemini) agent. It forces the agent (and you) to follow a rigorous process: **Brainstorm → Plan → Execute (TDD) → Review**.

## 🚀 Features

*   **Brainstorming:** Structured Socratic dialogue to refine requirements before coding.
*   **Git Worktrees:** Automated isolation. Never mess up your main branch again.
*   **Planning:** Generates detailed implementation plans (`implementation_plan.md`).
*   **Strict TDD:** The agent is *forbidden* from writing implementation code without failing tests. Enforced by scripts.
*   **Subagent Execution:** (Experimental) Dispatch sub-tasks to fresh contexts.

## 📦 Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/DmitriyPolukhin/antigravity-superpower.git
    ```

2.  Install into your Antigravity skills directory:
    ```bash
    mkdir -p ~/.gemini/skills/superpower
    cp -R antigravity-superpower/* ~/.gemini/skills/superpower/
    ```

3.  **Verify:**
    Tell Antigravity: *"Open Superpower skill"* or *"View file ~/.gemini/skills/superpower/SKILL.md"*

## 🛠️ Usage

Simply ask Antigravity to help you with a task using the skill:

> "Use Superpower to build a new React component for the login form."

The agent will load the Router (`SKILL.md`) and guide you through the phases:

1.  **Brainstorm:** It will ask questions until the design is clear.
2.  **Worktree:** It will run `scripts/worktree.py` to create a clean environment.
3.  **Plan:** It will draft a plan.
4.  **Execute:** It will enforce TDD using `scripts/verify.py`.

## 📂 Structure

*   `SKILL.md`: The Master Router.
*   `modules/`: 14 specialized skills (Brainstorming, Debugging, Reviews, etc.).
*   `scripts/`: Python automation tools.
    *   `worktree.py`: Manages git worktrees and dependencies.
    *   `verify.py`: Enforces TDD (checks for test existence).
    *   `plan.py`: Generates plan templates.

## ⚖️ Credits & License

*   Original Concept & Skills: [Jesse Vincent (@obra)](https://github.com/obra)
*   Antigravity Port: [Dmitriy Polukhin](https://github.com/DmitriyPolukhin)

MIT License.
