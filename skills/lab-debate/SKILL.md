---
name: lab-debate
description: Structured disagreement inside the lab. Red-teams a claim, method, design or decision by having independent advocate and skeptic roles argue it out. A judge then separates factual disputes from value disputes, names the cheapest experiment that would settle the facts, and records the decision with its surviving dissent. Use when the user is making a research decision, is unsure about an approach, wants critique, or says "argue against this", "steelman", "devil's advocate", "red team", or "what would reviewer 2 say", and when lab roles disagree.
---

# Lab debate

Agreeing with the human is the default failure mode of an AI collaborator. This skill forces real disagreement and keeps a record of it.

## Steps

1. **Proposition.** State it precisely in one sentence, for example: "Use a contrastive loss instead of MSE in E4." If it is ambiguous, confirm it with the user first.
2. **Context.** Gather the charter, the relevant A-/E-/D-IDs, and the code or text involved.
3. **Opening arguments.** When the Agent tool is available, spawn two subagents **in parallel**, each with its own context so they don't anchor on each other. Give each the same proposition and context:
   - **Advocate:** the strongest case FOR, with specific evidence, plus "what would change my mind".
   - **Skeptic (Reviewer 2):** the strongest case AGAINST, covering alternative explanations, confounds, cheaper alternatives and prior work, plus "what would change my mind".
   Without the Agent tool, write both yourself, skeptic first, and argue to win.
4. **One rebuttal round** each, short.
5. **Judge.** Write:
   - what is now settled, and why
   - which remaining disputes are about **facts** and which are about **values or priorities**
   - the **cheapest experiment that would settle the factual part** (draft it as an E-card if useful)
6. **Decide.** The human decides. Then append to `lab/decisions.md`: D-ID, decision, why, alternatives, **dissent** (the strongest unrefuted counterargument, written in its best form), and a **revisit trigger** ("revisit if E7 shows ...").

## Rules

- No strawmen. Each side argues from specifics in this project, not generic pros and cons.
- The skeptic must really try to win. "Both have merits" is not a valid outcome of step 3.
- Never delete dissent later. If it is resolved, add a line saying how.
