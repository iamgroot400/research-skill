---
name: meta-review
description: Periodic synthesis across the whole lab notebook. Finds recurring problems in QA reports, reviews and decisions, writes a research overview of where the project stands, and turns the patterns into concrete feedback for each lab role. Use weekly, at the end of a research phase, before a submission, or when the user asks "what keeps going wrong", "summarize the project so far", "research overview", "lessons learned", or "meta-review".
---

# Meta-review

One role looks across everything the others produced and asks what the pattern is. This is the feedback loop that makes the lab improve instead of repeating mistakes. It follows the meta-review idea in Google's AI co-scientist.

## Read

`lab/charter.md`, `lab/plan.md`, all of `lab/decisions.md`, `lab/assumptions.md`, `lab/experiments/*`, `lab/qa/*`, `lab/hypotheses/*` if present, and the notebook entries since the last meta-review (find it in `lab/meta/`).

## Write `lab/meta/<YYYY-MM-DD>-meta-review.md`

1. **Research overview (≤ 300 words).** Question, what has been tried, what is supported, what failed, what is open. Cite E-/A-/D-IDs for every statement. This can seed the paper's introduction or a progress report.
2. **Recurring patterns.** Problems that appeared at least twice, with the IDs where they appeared. Examples: assumptions found untested late, results with no prediction recorded, the same bug class, reviewer-style objections that keep returning, decisions revisited.
3. **Feedback per role.** For each role that acted in this period, give one or two specific instructions grounded in a pattern. Example: "grad-student: write the prediction before running, it was missing in E3 and E5."
4. **Stalled and dead ends.** Hypotheses or experiments with no activity, and a recommendation: continue, park or kill.
5. **Suggested updates** to `lab/plan.md` or the charter, written as a diff for the human to approve. Never edit the charter yourself.

## Rules

- Evidence over impression. Every pattern needs two or more concrete instances.
- Be honest about low-value work. If the project is not converging, say so.
- Give the feedback to the human as well as saving it. Roles read it next session from `lab/meta/`.
- Append a notebook entry that points to the review.
