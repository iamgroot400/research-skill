---
name: research-plan
description: Supervisor that turns a plain-language research goal into a concrete research plan configuration - success criteria, constraints, preferences, which lab roles run in what order, and a compute/time budget - and saves it to lab/plan.md. Use when the user states a new research goal, says "plan this", "break this goal down", "how should we approach X", or before running hypothesis-tournament on a new goal.
---

# Research plan (supervisor)

Parse the goal once, up front, so every later role works toward the same target. Inspired by the supervisor agent in Google's AI co-scientist.

## Steps

1. Read `lab/charter.md` (mode and question) and `lab/assumptions.md`. If there is no `lab/`, offer **lab-setup**.
2. Restate the goal in one sentence and ask the human to correct it. Do not continue until it is confirmed.
3. Write `lab/plan.md`:

```markdown
# Research plan - <goal in one sentence>
- **Mode:** synthesis | discovery
- **Success criteria:** what result would make the human say "this worked"
- **Hard constraints:** data, compute, ethics, time, tools that are off limits
- **Preferences:** methods or framings the human likes or dislikes (and why)
- **Known prior work:** 3-5 items, each marked verified or unverified
- **Pipeline:** the ordered roles and what each produces (see below)
- **Budget:** wall-clock, compute, human review hours; and a stop rule ("stop if no candidate beats baseline after N rounds")
- **Delegation:** which steps can run in parallel as subagents (e.g. one per debate or per paper), and the maximum number at once
- **Checkpoints:** where the human reviews before the next stage
```

4. Choose the pipeline from the mode:
   - **discovery:** `literature-review` → `hypothesis-tournament` (generate, reflect, rank, evolve) → human picks → `experiment-protocol` → `grad-student` / `lab-engineer` → `qa-check` → `meta-review`
   - **synthesis:** `literature-review` → `reflect` on gaps → `qa-check` (hallucination focus) → `meta-review`
5. Log the plan as a D-entry in `lab/decisions.md` and append a notebook entry.

## Rules

- Success criteria must be checkable. "Understand X better" is not a criterion.
- Put the stop rule in writing now. Open-ended loops burn budget.
- The human owns the goal and the checkpoints. You may suggest changes but never edit them silently.
