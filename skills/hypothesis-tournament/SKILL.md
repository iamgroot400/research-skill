---
name: hypothesis-tournament
description: Generate-debate-evolve loop for research hypotheses. Generates many candidate hypotheses, critiques each, removes near-duplicates, ranks them in pairwise debates scored with Elo ratings, evolves the winners, and hands a short ranked list to the human. Use when the user wants new hypotheses or research directions for an open problem, says "brainstorm and rank ideas", "find the best hypothesis", "tournament", or "co-scientist".
---

# Hypothesis tournament

A loop of generate → reflect → dedupe → rank → evolve, adapted from the multi-agent design in Google's AI co-scientist. More rounds usually give better candidates, but the ranking is a **model's opinion, not ground truth**. Only experiments settle things.

## Before starting

Read `lab/plan.md` (offer **research-plan** if missing), `lab/charter.md` and `lab/assumptions.md`. This skill is for **discovery** mode. In synthesis mode, use it only to rank gaps in the literature, never to invent findings.

## Files

```
lab/hypotheses/
  pool.md          candidates C1, C2, ... (never renumbered)
  matches.jsonl    one line per debate: {"a":"C1","b":"C4","winner":"C4","why":"..."}
  ratings.md       latest Elo table from elo.py
  seeds.md         the human's own ideas (optional, human-edited)
  human-feedback.md  the human's running notes; reflect applies them first
  feedback.md      win/loss patterns and limits, rewritten each round
```

## The loop (default 3 rounds, or what `plan.md` budgets)

1. **Generate.** Start from the human's own seed ideas in `lab/hypotheses/seeds.md` if any (the human can add, review or discuss ideas at any point), and from gaps found by **literature-review**. Write 8-12 candidates, and stress-test each with a short simulated debate between a proposer and a skeptic before it enters the pool. Each: claim, mechanism, what it assumes, how it could be false, closest prior work. Vary the approaches on purpose (analogy, contradiction-hunting, combining fields, simplifying a known method).
2. **Reflect.** Run **reflect** on every candidate. Drop any that is already published (fully), untestable, or contradicts a verified result.
3. **Dedupe (proximity).** Group candidates that are the same idea in different words. Keep the clearest one per group and note the others as merged. This keeps the tournament from rewarding repetition.
4. **Rank.** Pair candidates (every candidate plays at least 3 matches; pair similar-rated ones more often as ratings emerge). For each pair, argue both sides briefly, then judge on: novelty, plausibility, testability, and fit with the plan's success criteria. When the Agent tool is available, use one subagent per debate so they do not share bias; otherwise argue each side honestly yourself. Append each result to `matches.jsonl`, then run:

   ```bash
   python <this skill folder>/elo.py lab/hypotheses/matches.jsonl > lab/hypotheses/ratings.md
   ```
5. **Feedback.** Summarize the limits and the win/loss patterns of this round in `lab/hypotheses/feedback.md` (for example: "candidates that assume X keep losing on testability"). Generate, reflect and evolve read this file next round, which is how the loop improves itself.
6. **Evolve.** Run **evolve** on the top 3 to create improved variants. Add them to the pool as new IDs, with their lineage, and give them matches.
7. **Repeat** from step 2 until the budget or stop rule in `plan.md` is hit.

## Output to the human

Show a short research overview (what was explored and what the ranking shows), then the top 3-5 as a table: ID, one-line claim, Elo, strongest objection, and the **cheapest experiment that could kill it**. Ask for feedback on the list and save it to `human-feedback.md` for the next round. Then stop. The human chooses what moves forward. A chosen candidate becomes an `H` entry in the charter and an experiment card, both with the human's sign-off.

## Rules

- Say in the output that Elo here measures preference among generated ideas, not truth. Don't present it as evidence.
- Keep losing candidates in `pool.md`. They record what was tried.
- Never cite a paper you did not verify. Mark unverified prior work as such.
- Append a notebook entry with rounds run, candidates generated, and what changed in the ranking.
