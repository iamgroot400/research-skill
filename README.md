# 🧪 Research Lab Skills

**Turn Claude into a small research lab, not a product engineer.**

Most AI coding setups are tuned for shipping products: defensive code, edge cases, scale. Research needs something else: **readable code you can check against the paper, explicit assumptions, honest disagreement, and theory, code and results that stay aligned as ideas change.**

This repo is a set of [Agent Skills](https://docs.claude.com/en/docs/claude-code/skills) that give Claude distinct lab roles. They share one plain-markdown **lab notebook** that lives in your project.

## The lab

| Skill | Role | Ask it things like |
|-------|------|--------------------|
| `lab-setup` | Opens the lab | "set up the lab for my project on X" |
| `pi` | Lab head, your right hand | "daily briefing", "are we drifting?", "funding ideas" |
| `grad-student` | Ideas, experiments, POCs, paper drafts | "propose directions", "design an experiment for H2", "draft the method section" |
| `intern` | Data prep, EDA, scouting, side experiments | "clean this dataset", "quick EDA", "find datasets on ..." |
| `lab-engineer` | Review, POC → reproducible release | "review this for bugs that change results", "prep the code release" |
| `qa-check` | Theory ↔ code ↔ results ↔ references | "fact-check the draft before submission" |
| `lab-debate` | Structured disagreement and red-teaming | "argue against using method X", "what would reviewer 2 say?" |
| `lab-ops` | Deadlines, checklists, travel, paperwork | "NeurIPS submission checklist", "visa letter draft" |
| `lab-comms` | Announcements, newsletter, talks, venues | "announcement thread for the paper", "where can I present this?" |
| `research-code` | House coding style (runs automatically) | used by every role that writes code |

## Two research modes

You declare the mode once at `lab-setup`. It is stored in `lab/charter.md`, and every role adapts to it.

| | **Synthesis** | **Discovery** |
|---|---|---|
| Goal | Literature reviews, synthesizing existing knowledge | Novel research, unsolved problems, new hypotheses |
| `qa-check` | Hallucination police: every claim tied to a verified source, no invented science | Alignment police: equations ↔ code, `A`/`E` tags, challenges untested assumptions |
| `lab-engineer` | Support tooling only | Fully active: POCs → reproducible releases |
| `grad-student` | Finds gaps in the literature, writes cited reviews | Proposes hypotheses, designs and runs experiments |

Switching modes is a logged decision in `lab/decisions.md`.

## Core ideas

- **Shared memory, not shared chat.** Every role reads `lab/` before acting and appends to it after, so context survives across sessions and between roles.
- **Assumptions are first-class.** Every modelling choice gets an ID (`A3`) in `lab/assumptions.md` and a `# ASSUME A3:` tag in the code. QA checks that the two stay in sync.
- **Predictions before results.** Experiment cards record what would falsify a hypothesis *before* the code runs.
- **Dissent is recorded.** Decisions keep their strongest unrefuted counterargument and a "revisit if" trigger.
- **Research code ≠ production code.** Linear scripts, paper-shaped names, `assert` over `try/except`, no speculative abstraction.
- **Agents draft, humans decide.** No role submits, posts, pays or edits the charter on its own.

```
lab/
  charter.md         question, hypotheses (H1..), scope - human-owned
  assumptions.md     assumption register (A1..)
  decisions.md       decision log with dissent (D1..)
  deadlines.md       dated deadlines + internal milestones
  experiments/E*.md  experiment cards (E1..)
  notebook/DATE.md   daily log, every role appends
  qa/  comms/  data/ reports from qa-check, lab-comms, intern
results/E*/          experiment outputs, never overwritten
```

## Install

### Claude Code (plugin, recommended)

```
/plugin marketplace add iamgroot400/research-skill
/plugin install research-lab@research-skill
```

### Claude Code (copy the skills)

Copy the folders in `skills/` to `~/.claude/skills/` (all your projects) or `<project>/.claude/skills/` (one project).

### Claude.ai / Claude desktop

Zip each folder in `skills/` on its own (the zip should contain the folder with `SKILL.md` inside), then upload it under **Settings → Capabilities → Skills**.

## A typical day

1. `set up the lab` → answer 4 questions once.
2. `PI, daily briefing` → status, concerns, top 3 tasks with an owner each.
3. `grad-student: propose directions for H1` → ranked ideas, each with the cheapest experiment that could kill it.
4. `red-team direction 2` → `lab-debate` argues it out and logs the decision and its dissent.
5. `grad-student: design and POC E1` → prediction first, then minimal code tagged with assumptions.
6. `lab-engineer: review E1` → bugs that would change results.
7. Before submitting: `qa-check` → `lab-ops` checklist → `lab-comms` announcement pack.

## Contributing

PRs welcome, especially new roles (e.g. a statistician or ethics reviewer), field-specific variants (wet lab, social science, theory-only), and venue checklists. Keep each `SKILL.md` short: the `description` decides when the skill fires, and the body is read in full every time it runs.

## License

MIT
