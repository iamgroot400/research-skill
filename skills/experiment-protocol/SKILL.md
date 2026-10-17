---
name: experiment-protocol
description: Turns a chosen hypothesis into a detailed, checkable experimental protocol - variables, controls, baselines, sample size or power reasoning, analysis plan, pre-registered success and failure criteria, and risks. Use when the user has picked a hypothesis and asks "how do we test this", "design the study", "write a protocol", "pre-register", or "what controls do we need". Works for computational and lab experiments.
---

# Experiment protocol

The protocol is written **before** any data is collected, and it is not edited afterwards except through a logged amendment. This is what keeps results honest.

## Before starting

Read the hypothesis, `lab/assumptions.md`, `lab/plan.md` (constraints and budget) and any existing `lab/experiments/` cards. Check that the human has signed off the hypothesis. If not, ask.

## Write `lab/experiments/E<n>-<slug>.md` (extends the experiment card)

Fill the standard card, then add:

1. **Hypothesis and prediction.** Direction and rough size of the expected effect.
2. **Variables.** Independent, dependent, and everything held fixed.
3. **Controls and baselines.** The fair ones a reviewer would demand, each given equal tuning effort. Include a negative control (should show nothing) and a positive control (should show the effect) wherever one exists.
4. **Sample size and power.** How many runs, seeds, samples or replicates, and why. State the smallest effect worth detecting. If you cannot justify the size, say so plainly.
5. **Confounds and leakage.** Everything else that could produce the same result, and how the design rules each out (randomization, blinding, held-out data, splits by subject or time).
6. **Analysis plan.** The exact metric, test or comparison, the multiple-comparison handling, and the plots. Decide it now, not after seeing the data.
7. **Decision rules.** What result **supports**, **contradicts**, or leaves the hypothesis **inconclusive**. Pre-commit to all three.
8. **Assumptions relied on** (A-IDs) and what happens to the conclusion if one is violated.
9. **Risks and cost.** Compute, time, money, ethics or safety review needs, and a stop rule.
10. **Amendments.** An empty log section. Any later change goes here with a date and the reason.

## Rules

- Safety and ethics: for human or animal subjects, hazardous materials, or personal data, flag that approval (IRB, ethics board, biosafety) is needed and hand the paperwork to **lab-ops**. Do not suggest skipping review.
- Don't pad the protocol. Every section must change what someone would actually do.
- For code experiments, finish by telling the human to run **grad-student** to implement it in research-code style.
- Append a notebook entry.
