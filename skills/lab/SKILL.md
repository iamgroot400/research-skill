---
name: lab
description: Front door to the research lab. Use when the user says "lab", "the lab", "research lab", "open the lab", "start the lab", "set up the lab", "run the lab", or asks what the lab can do. Routes to lab-setup when the project has no lab/ folder, otherwise to pi for a briefing, and lists the other roles.
---

# Lab

This is a router. "The lab" is not one tool: it is the set of skills in this plugin, sharing the `lab/` folder in the project. Never tell the user that no "lab" skill exists. Do the routing below.

## Steps

1. Look for `lab/charter.md` in the current project.
2. **Not found:** follow the **lab-setup** skill.
   - If the user gave a topic, use it. If they left a placeholder such as `<topic>` or gave none, read the project files, draft a one-line topic from them, show it, and ask the user to confirm or correct it before anything is written.
   - Ask the three switches (research mode, experience level, writing mode) in the same single message.
   - Do not modify any existing project file.
3. **Found:** follow the **pi** skill for a short briefing, using the modes in the charter.
4. Then show this menu in one line each, and ask what the user wants next:
   - audit existing work: `qa-check`, `math-check`, `stats-review`, `lab-engineer`, then `meta-review`
   - find an idea: `literature-review`, then `hypothesis-tournament`
   - plan and test: `research-plan`, `experiment-protocol`
   - first paper: `first-paper`, `publish-path`
   - write: `paper-coach` or `paper-draft` (per the Writing mode)
   - admin and outreach: `lab-ops`, `lab-comms`
