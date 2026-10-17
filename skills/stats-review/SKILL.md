---
name: stats-review
description: Statistical design and analysis reviewer. Checks that a method fits the question and data, that test assumptions hold, that sample size and power are justified, that uncertainty and effect sizes are reported, that multiple comparisons and p-hacking are controlled, and validates methods by simulation with a known ground truth. Use when the user says "is this analysis valid", "which test should I use", "how many samples", "check my statistics", "is this significant", "confidence interval", or before reporting any statistical result.
---

# Stats review

Statistics is where first papers most often go wrong without anyone noticing. Review the *plan* first, because mistakes in design cannot be fixed afterwards. When the experience level in `lab/charter.md` is `beginner`, explain each point in plain language and let the student choose the fix.

## Review the plan (before the data is analyzed)

1. **Question to estimand.** What exact quantity is being estimated or compared? Write it in one sentence. If it cannot be stated, the analysis cannot be judged.
2. **Method fit.** Does the method match the data type, the structure (independent, paired, clustered, time series, spatial), and the question? Note the assumptions it needs and add them to `lab/assumptions.md`.
3. **Sample size and power.** How many observations or runs, and what is the smallest effect worth detecting? Compute power or the expected interval width, with a script if possible. If the data is already fixed, say what effects it can and cannot detect.
4. **Decisions made before looking.** Which metric, which test, which exclusions, which comparisons. Put them in the experiment card now. Anything chosen after seeing results is **exploratory** and must be labeled that way.
5. **Leakage and independence.** No repeated measures treated as independent samples, no test data used in tuning, no peeking.

## Review the results

1. **Assumption checks.** Plots and diagnostics for the assumptions above (residuals, normality where it matters, variance, outliers, autocorrelation). Note what happens to the conclusion if an assumption fails.
2. **Uncertainty and effect size.** Every estimate has an interval, and the paper reports the effect size, not only a p-value. Explain what the interval does and does not mean.
3. **Multiple comparisons.** Count all the comparisons made, including the ones not reported. Apply a correction or label the findings exploratory.
4. **Honest reporting.** All runs, seeds and datasets are reported, not just the best. No selective stopping. Null results stay in.
5. **Simulation check (recommended).** Generate synthetic data with a **known** truth, run the method, and see whether it recovers it and whether intervals have the stated coverage. A short script (`checks/sim_<name>.py`) is enough. This catches bugs and misuse of the method before real data is touched.
6. **Robustness.** Does the conclusion survive a reasonable alternative method, a different seed, a resample (bootstrap), or dropping a suspicious point? Report it either way.

## Output

A list ordered by how much it could change a conclusion: severity (**blocker** / **major** / **minor**), where, the issue in plain words, and the suggested fix. End with whether the statistical claims in the draft are supported, supported with caveats, or unsupported.

## Rules

- Don't pick the analysis that gives the nicest p-value. If asked to, refuse and explain.
- Never invent a p-value, interval or sample size. Compute it, or say it needs computing.
- Save any code in `checks/` and tag assumptions with `# ASSUME A<n>`.
- Append a notebook entry.
