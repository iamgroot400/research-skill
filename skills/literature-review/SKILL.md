---
name: literature-review
description: Grounded literature review where every claim is tied to a source that was actually opened. Searches, reads, builds a claim-to-source table, maps agreement and contradiction across papers, and lists open gaps. Primary skill for synthesis mode and the first stage of discovery. Use when the user asks for a literature review, related work, state of the art, "what is known about X", "find gaps", or needs a verified reference list.
---

# Literature review

The risk here is fabrication: invented papers, wrong numbers, claims a paper does not make. Every rule below exists to prevent that.

## Before starting

Read `lab/charter.md` (mode, question) and `lab/plan.md`. Tell the user which search tools you have. With no web access, say that you can only work from papers the user provides, and do not fill gaps from memory.

## Steps

1. **Scope.** Restate the question, the time window, and inclusion rules. Confirm with the human if the scope is broad.
2. **Search** several query phrasings. Record each query and where you searched in `lab/literature/search-log.md`, so the search can be repeated.
3. **Read, don't guess.** For each paper you use, open it (abstract at minimum, the relevant section for any claim). Record in `lab/literature/sources.md`:

   | Key | Citation | Link | What was opened | Verified |
   |---|---|---|---|---|

   `What was opened` is `full text`, `abstract only` or `provided by user`. Anything not opened is **unverified** and may be listed as a lead, never cited as support.
4. **Claim table.** For every substantive statement, one row: claim, source key, location (page, section or table), and whether the source states it directly or you inferred it. Inferences are labeled as such.
5. **Synthesize.** Group by theme. For each theme: where papers agree, where they conflict (with the reason, if known), and the quality of evidence (sample, method, replication).
6. **Gaps.** List open questions the literature leaves, each marked as: not studied, studied but contradictory, or studied only in a narrow setting. In discovery mode, hand the best gaps to **hypothesis-tournament**.
7. **Self-audit.** Reopen 3 random claim-table rows and re-check them against the source. Report the result.

## Rules

- Never invent a citation, DOI, quote or number. If you are not sure it exists, it goes under "leads to verify".
- Paraphrase in your own words. Quote only short phrases, in quotation marks, with a location.
- Don't state a consensus that a single paper does not establish.
- Hand the draft to **qa-check** (hallucination focus) before the human relies on it.
- Append a notebook entry.
