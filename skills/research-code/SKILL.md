---
name: research-code
description: House style for research code - readable, linear, assumption-tagged and easy to change as the science evolves, NOT production-grade. Use whenever writing or editing code for experiments, analyses, simulations, proofs-of-concept, notebooks, plots or figures in a research project, and whenever the user says code is over-engineered, too defensive, too long, or hard to follow.
---

# Research code style

Research code is a lab instrument, not a product. Optimize for two things:
1. **A reader can check that the code does what the paper says.**
2. **It is cheap to change tomorrow, when the hypothesis changes.**

Edge-case coverage, scalability and API polish come last, and only when asked for.

## Rules

1. **Plan before bulk.** Before writing more than ~50 lines, give a 3-6 bullet plan and wait for a nod, unless the user asked you to just go.
2. **Script first.** Write a top-to-bottom script or notebook cells. Add a function only when a block is reused or needs a name to be understood. Add a class only when state really travels together. No config frameworks: put constants in CAPS at the top of the file.
3. **Paper-shaped names.** Use the paper's notation when there is one (`theta`, `x_t`, `K`, `lam`), and link it with a short comment: `# Eq. 3`, `# Alg. 1 line 4`.
4. **Tag every assumption.** Every modelling choice, simplification, data filter or unjustified number gets `# ASSUME A<n>: <one line>` and a matching row in `lab/assumptions.md`. If no row exists, add one. **This is the most important rule.**
5. **Fail loud, not safe.** Use `assert` for what must be true (shapes, ranges, no NaN, probabilities sum to 1). Never write a try/except that hides an error, a silent fallback, or a default that papers over missing data. A crash is information.
6. **No speculative generality.** Do not add CLI flags, plugin systems, abstract base classes, retry logic, logging frameworks, heavy type wrappers or "for later" parameters unless asked.
7. **Reproducible by default.** Set every seed at the top. Print the run's config at start-up. Write outputs to `results/<E-id>/<timestamp>/` together with that config, and never overwrite an earlier run.
8. **Smallest thing that produces a number.** Get one end-to-end number first, run it, then grow.
9. **Vectorize when it reads better, not by reflex.** A clear loop beats a clever einsum unless speed matters for this experiment.

## When defensive code IS allowed

1. **Checkpoint expensive compute.** Any loop or training run expected to take longer than 30 minutes saves its intermediate state or weights to disk at regular intervals.
2. **Validate data at the boundaries, not internal logic.** Write defensive checks where external datasets, scraped pages or API responses come in (e.g. assert no missing values, check dtypes). Once data is inside the pipeline, let internal math fail loud.
3. **Prevent silent statistical corruption.** Assert mathematical invariants that won't crash the program but would ruin the theory, e.g. `assert np.isclose(probs.sum(), 1.0)`. Use a tolerance for floats, never `==`.
4. **No catch-all exceptions.** Never suppress generic errors to keep a script running. An unexpected error must crash immediately and print the stack trace, so the assumptions can be updated.

## Before you hand back

- Could a grad student check this against the paper in 10 minutes? If not, simplify.
- List the new or changed assumption IDs in your reply.
- Name the edge cases you deliberately skipped, in one line.
