---
name: next
description: Mentor that reads the project's lab notebook, works out which research stage it is in, and says the one thing to do next, why, and which skill to run for it. Calls out when the user is stuck or off track. Use whenever the user asks "what next", "what should I do now", "I'm stuck", "where am I", "am I on track", "what's my next step", or "what am I missing".
---

# Next

Give the user one clear next action, not a list. Be a calm, honest mentor.

## Read

`lab/charter.md` (mode, experience level, writing mode), `lab/plan.md`, `lab/first-paper-plan.md`, `lab/deadlines.md`, `lab/experiments/*`, `lab/assumptions.md`, the latest files in `lab/qa/` and `lab/meta/`, and the last few `lab/notebook/` entries. If there is no `lab/`, the next step is **lab** (set it up), and you are done.

## Find the stage

Pick the first stage that is not yet true:

1. **Scoped.** There is a one-sentence question and a plan. If not, run **first-paper** or **research-plan**.
2. **Grounded.** The literature is reviewed and sources verified. If not, run **literature-review**.
3. **Hypothesis chosen.** One hypothesis is signed off. If not, run **hypothesis-tournament** or **reflect**.
4. **Protocol written.** The prediction and decision rules exist before any run. If not, run **experiment-protocol**.
5. **Evidence exists.** Experiments have results on disk. If not, build and run them (**grad-student**, then **lab-engineer**).
6. **Checked.** No open blockers from **qa-check**, **math-check** or **stats-review**. If not, run the missing check or fix the blockers.
7. **Written.** A draft exists. If not, use **paper-coach** or **paper-draft** per the Writing mode.
8. **Ready to submit.** The mentor has read it and the venue checks are done. If not, run **publish-path** and **lab-ops**.

## Flag trouble

Check these and mention any that apply, in one line each:

- a deadline within 3 weeks, and the stage still early
- an experiment with no prediction written, or a result with no E-ID
- an untested assumption under a headline claim
- no notebook entry for 7 or more days
- a plan that has grown beyond what the time left allows (suggest cutting scope, not hours)
- no human mentor named anywhere

## Answer in this shape

```markdown
**Where you are:** <stage, one sentence>
**Do this next:** <one concrete action, small enough for this week>
**Why:** <one or two sentences>
**Run:** <skill name and the exact request to give it>
**Watch out for:** <up to two flags from above, or "nothing urgent">
```

If the experience level is `beginner`, keep the words plain and define any term you use. If the user says they are stuck, ask one question about what exactly is blocking them before suggesting a fix. Never invent progress that the files do not show.
