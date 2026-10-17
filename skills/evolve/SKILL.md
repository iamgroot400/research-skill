---
name: evolve
description: Improves a promising hypothesis or method by producing several better variants - fixing the weaknesses a reviewer found, simplifying it, combining it with another candidate, or reframing it from a different angle - and records the lineage. Use when the user says "improve this idea", "make this stronger", "combine these", "fix the weakness reviewer found", or when hypothesis-tournament selects top candidates for the next round.
---

# Evolve

Take a candidate (and, ideally, its **reflect** review) and produce 3 variants. Do not just polish wording. Each variant must change something that matters.

## Moves

Pick the moves that fit the critique:

- **Repair:** fix the specific objection from the review. Say which objection.
- **Simplify:** remove a component. Keep the claim if the simpler version still works.
- **Combine:** merge the strongest part of two candidates. Name which part came from where.
- **Reframe:** state the same question from a different angle (a different level of abstraction, an analogy from another field, an inverse question).
- **Inspiration:** borrow a mechanism from a different candidate or another field, and say what was borrowed and why it should transfer.
- **Extend:** push the idea into the next question it opens (a new setting, a harder case, a prediction it makes that nobody has tested).
- **Sharpen:** turn a vague claim into one with a number, a direction, or a named condition so it can be falsified.

## Output

For each variant:

```markdown
### C<new id> (from C<parent>[ + C<parent2>]) - <move>
- Claim:
- What changed and why:
- New assumptions: A?: ...
- Cheapest killing experiment:
```

## Rules

- Keep lineage. The pool file records each variant's parent(s) and move, so the history of an idea stays readable.
- Never delete the parent. A variant can be worse than what it came from.
- Don't add complexity to dodge an objection without saying so. If the repair makes the idea unfalsifiable, call that out.
- Send the new variants back through **reflect** before they are ranked. Do not rank an unreviewed variant.
