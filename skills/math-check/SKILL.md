---
name: math-check
description: Verifies a derivation, formula or proof from physics or mathematics by independent means - dimensional analysis, limiting cases, symmetry and conservation checks, numeric spot tests against the formula, and a step-by-step audit that marks each step as verified, plausible or unjustified. Use when the user says "check my derivation", "is this proof right", "sanity check this formula", "do the units work", "verify this result", or after deriving anything that a paper will rely on.
---

# Math check

You are the second pair of eyes, not the author. Find where the derivation could be wrong and prove or disprove it by a method that does not just repeat the same algebra. For a beginner, explain each check so they learn to run it themselves (see the experience level in `lab/charter.md`).

## Checks

Run all that apply, and say which you skipped and why.

1. **Restate.** Write down the claim and every assumption it needs. Add each assumption to `lab/assumptions.md` as an A-ID.
2. **Step audit.** Go line by line. Mark each step **verified** (you re-derived it), **plausible** (looks right, not checked), or **unjustified** (a leap, a hidden assumption, a division by something that could be zero, an exchange of limit and integral without a reason).
3. **Dimensional analysis** (physics). Every term in an equation has the same units, and the final result has the units it should. Report any mismatch.
4. **Limiting cases.** Take parameters to 0, to infinity, or to a known special case. The result must reduce to something known or sensible. A formula that gives the wrong answer in an easy limit is wrong.
5. **Symmetry and conservation.** Does the result respect the symmetries and conservation laws of the problem? Is it invariant where it should be?
6. **Numeric spot check.** Write a short script (numpy or sympy) that evaluates the formula at several random values and compares it with a brute-force, independent calculation: numerical integration, direct simulation, series summation, or a symbolic simplification. Report the maximum difference. Use `# ASSUME` tags where the script depends on a choice.
7. **Special cases and counterexamples** (mathematics). Test the claim on the simplest nontrivial example, and try to break it with edge cases (empty set, zero, negative numbers, non-convergent series, degenerate matrices).
8. **Proof structure.** For proofs, check that each lemma is actually used, that the quantifiers are in the right order, that induction has a valid base case and step, and that the conclusion is the stated claim and not a weaker one.

## Output

A table with one row per check: what was done, the result, and the evidence (the script or the substitution). End with a verdict: **holds**, **holds under these extra assumptions**, or **has an error at step N**. Never say "correct" when you only judged it plausible.

## Rules

- A script that agrees with the formula only confirms the formula where you tested it. Say which values were tested.
- Don't fix the derivation silently. Point to the step and explain the issue, and let the student correct it.
- Save useful checks as `checks/<name>.py`, so the paper's claims stay reproducible.
- Append a notebook entry that links the A-IDs and any new E-IDs.
