<p align="center">
  <img src="assets/banner.svg" alt="Research Skill: an agents research lab for Claude" width="100%">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue.svg"></a>
  <img alt="Skills" src="https://img.shields.io/badge/skills-25-8b5cf6">
  <img alt="Claude Code plugin" src="https://img.shields.io/badge/Claude%20Code-plugin-d97757">
  <a href="https://github.com/iamgroot400/research-skill/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/iamgroot400/research-skill?style=social"></a>
</p>

# Research Skill

A set of skills that make Claude behave more like a small research group than a software engineer.

I'm an undergrad (physics, stats and math) trying to get a first paper out, and I kept running into the same problem: AI coding tools are built to ship products. They write long, defensive code, bury your assumptions, and agree with everything you say. Research needs the opposite. You want short code you can check against the paper, assumptions written down where you can find them, and someone willing to tell you your idea has a hole in it.

So this repo gives Claude a set of lab roles (a PI, a grad student, an intern, a QA checker and so on) that share one folder of plain markdown notes. Nothing fancy, no database, no service to run. If you can read a text file, you can see exactly what the agents know.

> **Status:** early and still changing. The skill files are validated, but I haven't run them through many real projects yet. If something misfires, please open an issue.

## Contents

[What's in the box](#whats-in-the-box) · [Install](#install) · [Try it](#try-it) · [Three switches you set once](#three-switches-you-set-once) · [How the notebook works](#how-the-notebook-works) · [The idea-ranking loop](#the-idea-ranking-loop) · [Honest limits](#honest-limits) · [Contributing](#contributing)

## What's in the box

<p align="center">
  <img src="assets/lab-diagram.svg" alt="Every role reads and writes one shared lab notebook" width="90%">
</p>

**The lab roles**

| Skill | What it does | Try saying |
|---|---|---|
| `lab` | The front door: sets up the lab if there isn't one, otherwise gives a briefing and a menu | "Open the lab" |
| `next` | The mentor: reads your notebook and says the one thing to do next | "What next?" or "I'm stuck" |
| `lab-setup` | Creates the shared `lab/` notebook for your project | "Set up the lab for my project on X" |
| `pi` | Keeps the big picture: daily briefing, drift checks, what to do next | "PI, daily briefing" |
| `grad-student` | Proposes ideas, designs experiments, builds quick prototypes | "Propose directions for H1" |
| `intern` | Cleans data, does quick exploratory analysis, finds papers and datasets | "Quick EDA on this dataset" |
| `lab-engineer` | Reviews code for bugs that change results, makes it reproducible | "Review E1 for bugs" |
| `qa-check` | Checks that theory, code, numbers and references agree | "Fact-check my draft" |
| `lab-debate` | Argues against your idea on purpose, then records the disagreement | "Red-team this approach" |
| `lab-ops` | Deadlines, submission checklists, travel and paperwork drafts | "Submission checklist for <venue>" |
| `lab-comms` | Announcement threads, newsletters, talk and poster outlines | "Announcement thread for the paper" |
| `research-code` | The coding style the roles follow: short, readable, assumptions tagged | applied automatically |

**For finding and testing ideas** (inspired by Google's [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) post)

| Skill | What it does |
|---|---|
| `research-plan` | Turns a goal into success criteria, a pipeline and a budget |
| `literature-review` | Reviews papers and only cites ones it actually opened |
| `hypothesis-tournament` | Generates ideas, critiques them, ranks them head to head |
| `reflect` | Critiques a single idea: novelty, plausibility, testability |
| `evolve` | Improves a promising idea by repairing, simplifying or combining |
| `experiment-protocol` | Controls, sample size, analysis plan and decision rules, written before you run anything |
| `meta-review` | Looks across all your notes for repeated mistakes and gives each role feedback |

**For a first paper**

| Skill | What it does |
|---|---|
| `first-paper` | Picks a project you can actually finish, sets a realistic timeline, nudges you toward a mentor |
| `math-check` | Checks derivations: units, limiting cases, numeric spot checks |
| `stats-review` | Checks your method fits, your sample is big enough, and your claims hold up |
| `publish-path` | Finds legitimate places to publish and screens out predatory ones |
| `paper-coach` | Coaches your writing and reviews your drafts without writing them |
| `paper-draft` | Writes a full draft from your recorded evidence (only when you choose that) |

## Install

**Claude Code, as a plugin** (updates come with `/plugin marketplace update research-skill`):

```text
/plugin marketplace add iamgroot400/research-skill
/plugin install research-lab@research-skill
```

**Claude Code, copy the folders.** Put the folders from [`skills/`](skills) in `~/.claude/skills/` for all projects, or in `<project>/.claude/skills/` for one. Don't do this and the plugin install both, or you'll get every skill twice.

**Claude.ai and Claude desktop.** Zip each folder in `skills/` on its own (the folder with its `SKILL.md` inside) and upload it under Settings, then Capabilities, then Skills.

## Try it

Open Claude Code in your research folder and say:

> Use the lab-setup skill. Beginner, discovery mode, coach writing. My topic is *your topic*.

Replace *your topic* with a real one, or leave it out and the skill will draft a topic from your project files and ask you to confirm. Saying just "open the lab" also works and routes to the right skill.

It will ask a few questions once, create the notebook, and from then on every role reads it first. A good first week looks like this:

1. `first-paper`: pick the project and set the timeline.
2. `literature-review`: find out what's already known and where the gaps are.
3. `hypothesis-tournament`: rank candidate ideas, then you choose.
4. `experiment-protocol`: write down what you'll test and what would count as a failure, before you run it.
5. Do the work. Use `math-check` and `stats-review` as you go.
6. `qa-check`, then `paper-coach` or `paper-draft`, then `publish-path`.

Want an audit of work you've already done? Run `lab-setup` in that folder, then ask for `qa-check`, `math-check`, `stats-review`, `lab-engineer` and finally `meta-review`. New skills load when a session starts, so open a fresh session after installing.

<p align="center">
  <img src="assets/session.svg" alt="Illustrative example of a research lab session" width="90%">
</p>

<sub>That picture is a mock-up of what a session looks like, not a recording of a real run.</sub>

## Three switches you set once

`lab-setup` asks for these and saves them in `lab/charter.md`. Every role reads them.

**Research mode**

<p align="center">
  <img src="assets/modes.svg" alt="Synthesis mode versus discovery mode" width="90%">
</p>

- *Synthesis* is for reviewing what's known. `qa-check` hunts for claims without a source and nobody invents new science.
- *Discovery* is for new questions. `lab-engineer` builds prototypes, and `qa-check` makes sure equations match code and assumptions are tested.

**Experience level.** *Beginner* makes every role explain the why, give a hint before an answer, and keep things short. *Experienced* means act and report.

**Writing mode.** *Coach*: you write, the agents critique. *Draft*: `paper-draft` writes a full draft, but only from what your experiments actually produced. It leaves `[TODO]` for missing numbers and `[CITE]` for missing sources instead of guessing, and you review it and own it. Either way, nobody makes up results or citations.

Changing a switch later is a logged decision, so you can see when and why it happened.

## How the notebook works

```text
lab/
├── charter.md          mode, question, hypotheses, scope (you own this)
├── assumptions.md      every assumption, numbered A1, A2, ...
├── decisions.md        decisions, with the strongest objection kept on record
├── deadlines.md        dates, with time zones
├── experiments/        one card per experiment, E1, E2, ...
├── notebook/           a daily log every role adds to
└── qa/ comms/ data/    reports from the checking and writing roles
results/E*/             outputs, never overwritten
```

A few habits it builds in:

- **Assumptions get numbers.** In code you write `# ASSUME A3: features are linear`, and the same assumption lives in `assumptions.md`. `qa-check` flags it when the two drift apart.
- **Predictions come first.** Each experiment card says what result would count as failure *before* you run it, which stops you quietly rewriting the hypothesis afterwards.
- **Disagreement is kept.** When you decide something, the best argument against it is saved along with a "revisit if" trigger.
- **Research code isn't product code.** Short scripts, names from the paper, `assert` instead of `try/except`, no features nobody asked for.
- **You decide.** No role submits, posts, pays, or changes your charter on its own.

<details>
<summary>Example: an assumption tag in code</summary>

```python
SEED = 0  # every seed is set at the top; outputs go to results/E1/<timestamp>/

# ASSUME A2: features are linearly decodable from layer activations
probe = LogisticRegression(max_iter=1000).fit(train_x, train_y)

assert train_x.shape[0] == train_y.shape[0]   # fail loudly, not quietly
print(f"layer {layer}: acc={probe.score(test_x, test_y):.3f}")  # Eq. 4
```

</details>

<details>
<summary>Example: an experiment card</summary>

```markdown
# E1 - Cross-layer probe transfer
- Status: planned
- Tests hypothesis: H1
- Prediction (written BEFORE running): if H1 holds, a probe trained on layer 6
  keeps more than 80% of its accuracy on layer 8. Below 50% means H1 is in trouble.
- Assumptions relied on: A2
- Results: results/E1/
```

</details>

## The idea-ranking loop

The newer skills follow the shape of Google Research's [AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/): plan, generate ideas, critique them, remove duplicates, rank them in head-to-head debates, improve the winners, repeat. The ranking uses Elo ratings, and a small script ([`elo.py`](skills/hypothesis-tournament/elo.py)) does the arithmetic so the model doesn't have to.

<p align="center">
  <img src="assets/coscientist-loop.svg" alt="Generate, reflect, rank and evolve hypotheses, then protocol, run, QA and meta-review" width="90%">
</p>

This is my own open-source version of the idea, written as prompts and files. It isn't Google's system, isn't affiliated with Google, and doesn't use Gemini.

## Honest limits

- **Elo here is a model's opinion, not evidence.** It ranks ideas by how convincing the debates were. Only experiments tell you if an idea is true.
- **The agents can be wrong.** `qa-check`, `math-check` and `stats-review` catch a lot, but they are not a replacement for a human mentor reading your work. Get one.
- **Drafts need your eyes.** If you use `paper-draft`, you are responsible for every claim in the paper. Check your venue's rules on AI-assisted writing and disclose what you used. `paper-draft` writes the disclosure note for you to review.
- **A first paper in a first year is possible but unusual.** `first-paper` helps you pick something small enough to finish. That matters more than any tool here.

## Repository layout

```text
research-skill/
├── .claude-plugin/     plugin.json and marketplace.json
├── skills/             one folder per skill, each with a SKILL.md
└── assets/             the images used in this README
```

## Contributing

Pull requests are welcome, especially new roles (a statistician, an ethics reviewer), variants for other fields (wet lab, social science, pure theory), and venue checklists for `lab-ops`. Please keep each `SKILL.md` short. The `description` line decides when a skill kicks in, and the body is read in full every time.

## License

[MIT](LICENSE), Aashik Khatri.
