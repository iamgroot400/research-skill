---
name: paper-draft
description: Writes a full research paper draft from the lab's recorded evidence - outline, figures and tables generated from result files, every section in order, claim and assumption tags on each statement, verified citations only, honest limitations, and an AI-use disclosure note - then runs the audits and lists what the author must personally verify. Use only when the charter's Writing mode is `draft`, and when the user says "write the paper", "draft the paper", "write the method section", or "turn my results into a paper". It never invents results, numbers or citations.
---

# Paper draft

The agents write; the author owns. A paper is only as good as its evidence, so this skill drafts **from** the lab's records and refuses to go beyond them.

## Preconditions

- `lab/charter.md` says `**Writing mode:** draft`. If it says `coach`, stop and use **paper-coach**, unless the human changes the mode (log it in `decisions.md`).
- There are finished experiments with results on disk (`lab/experiments/*`, `results/E*/`). If the evidence is thin, say exactly what is missing and what to run next. Do not pad a paper that has no result.

## Steps

1. **Claim ledger.** Write `lab/paper/claims.md`: every claim the evidence supports, each with its E-ID, result file, and the assumptions (A-IDs) it depends on. Mark claims **strong** (replicated, tested), **moderate**, or **weak**. Only strong and moderate claims go in the abstract.
2. **Outline.** Section list, the core claim in two sentences, and which figure carries each claim. Show it to the human and wait for approval.
3. **Figures and tables from code.** Generate them with scripts in `paper/figures/` that read `results/`, never from typed numbers. Include units, readable labels, and uncertainty.
4. **Draft in this order:** methods, results, related work, introduction, discussion and limitations, abstract last. Use the venue's template if known (ask), else a plain LaTeX article in `paper/`.
5. **Tag as you write.** Every empirical sentence carries a `% E<n>` comment and every method choice a `% A<n>`. A missing number is `[TODO: E3 result]`. A claim needing a source is `[CITE: <claim>]`.
6. **Citations only from `lab/literature/sources.md`** entries marked verified (see **literature-review**). If a source is not there, leave `[CITE]`. Never write a reference from memory.
7. **Honest limitations.** Build the limitations section from `assumptions.md` (untested or violated rows), the claim ledger's weak rows, and any failed or null experiments. Report negative results too.
8. **Disclosure.** Write `paper/ai-disclosure.md` stating what the AI did, in the wording the target venue requires (check its policy, see **publish-path**). The author reviews and signs off on it.
9. **Audit loop.** Run **qa-check**, **math-check** (any derivation) and **stats-review** on the draft. Fix what they find. Repeat until there are no blockers.
10. **Handover.** List the 5-10 claims and numbers the author must personally verify before submitting, and recommend a mentor read.

## Rules

- No invented results, numbers, quotes, citations or related work. Ever. A gap is a `[TODO]`, not a guess.
- Do not claim more than the ledger supports. Watch "prove", "novel", "significant", "state of the art".
- Keep the author's notation and voice if they have already written anything. Ask for a sample.
- The author is responsible for the paper's content. Say so in the handover.
- Append a notebook entry after each pass.
