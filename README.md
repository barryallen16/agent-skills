# agent-skills

Writing skills I built, one folder each. Copy a folder into your agent's skills directory and the agent loads it from its `SKILL.md`.

## Skills

| Skill | What it does |
| --- | --- |
| [writing-that-works](writing-that-works/SKILL.md) | Drafts and edits business prose so the reader knows what to do, by when, and why. Merges Thompson's clarity rules, Roman and Raphaelson's effectiveness rules, and Ogilvy's persuasion rules into one file. |

## Install

Copy the skill folder into your agent's skills directory:

```
~/.agents/skills/<skill-name>/
```

The directory name varies by agent. Each folder holds one `SKILL.md`, and its frontmatter gives the skill a name and a description of when to use it. That description is what the agent reads to decide whether to load the rest.

## Archive

`archive/` holds two of the source files that `writing-that-works` merged from: `write_skill.md` (Roman and Raphaelson) and `ogilvy_skill.md` (Ogilvy). They are kept for reference and are not installed as skills.
