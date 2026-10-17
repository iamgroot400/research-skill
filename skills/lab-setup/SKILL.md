---
name: lab-setup
description: Scaffold a research "lab notebook" (a lab/ folder) in the current project - research charter, assumption register, decision log, experiment cards, deadlines and a daily notebook - that every other research-lab role reads before acting and writes to after. Use when starting a research project, when the user says "set up the lab", "init lab", "start a new project/paper", or when another lab skill finds no lab/ folder.
---

# Lab setup

The `lab/` folder is the lab's shared memory. Every role (PI, grad student, intern, engineer, QA, ops, comms) reads it before acting and appends to it after. It is plain markdown so it diffs in git and the human can edit it by hand.

## Steps

1. If `lab/` already exists, do not overwrite anything. List what is there and offer to add only the missing files.
2. Ask the user, in ONE message, for:
   - **Research mode (required, cannot be skipped):**
     - `synthesis`: literature reviews and synthesis of existing knowledge. No new science is invented. QA polices hallucinations and checks that every claim is tied to a source.
     - `discovery`: novel research, unsolved problems, creative hypotheses. lab-engineer builds POCs. QA polices theory-code alignment (A-/E-tags) and challenges experimental assumptions.
   - **Experience level (required):** `beginner` (first research project: roles explain, ask and coach) or `experienced` (roles act and report). Default to `beginner` if unsure.
   - working title, the core research question, 1-3 hypotheses (each with what would falsify it), target venue + deadline. These may be "skip": leave a `TODO` in their place.

   If the mode is missing or unclear, ask again. Do not create files until it is set.
3. Copy the files from the `templates/` folder next to this SKILL.md into the project, filling in the answers:

   ```
   lab/
     charter.md          # research mode, question, hypotheses, scope - changes need the human's sign-off
     assumptions.md      # assumption register (A1, A2, ...) - linked to `# ASSUME A<n>` tags in code
     decisions.md        # append-only decision log with recorded dissent (D1, D2, ...)
     deadlines.md        # dated deadlines and internal milestones
     experiments/
       _template.md      # experiment card (E1, E2, ...) - prediction written BEFORE running
     notebook/
       <YYYY-MM-DD>.md   # one file per day; every role appends a short entry
   results/              # create empty; experiment outputs go to results/E<n>/
   ```

4. Create today's notebook file with a first entry (format below).
5. If the project is a git repo, suggest committing `lab/`. Do not commit without asking.
6. Show the tree and one line per file on what it is for. Then suggest the next step: `pi` for a first briefing, or `grad-student` to propose directions.

## Notebook entry format (shared by all roles)

```markdown
### HH:MM - <role> - <one-line summary>
- Did: ...
- Result: ... (cite E-/A-/D-IDs)
- Open questions: ...
- Next: ...
```

## Research mode (shared by all roles)

`lab/charter.md` holds a line `**Research mode:** synthesis | discovery`. Every role reads it first and follows its own skill's mode rules. Only the human changes the mode, and each change is logged as a D-entry in `decisions.md`. A project can move from synthesis (map the field) to discovery (attack the gap).

## Experience level (shared by all roles)

`lab/charter.md` holds `**Experience level:** beginner | experienced`. When it is `beginner`, every role:
- explains the *why* in a sentence or two, in plain language, and defines terms the first time they appear
- offers a hint or a question before an answer, and lets the student do the key step (derivation, analysis choice, interpretation)
- never writes paper prose, results or conclusions. Writing goes through **paper-coach**
- keeps its output short and ends with one small next step
- reminds the student to get a human mentor to review before anything is shared or submitted

For a first paper, start with **first-paper**.

## ID conventions (shared by all roles)

- `H1..` hypotheses (charter.md), `A1..` assumptions, `D1..` decisions, `E1..` experiments.
- IDs are never reused or renumbered. A dead item gets a status, not deleted.
- In code: `# ASSUME A3: <one line>`. In LaTeX: `% A3` / `% E5` next to the sentence it supports.
