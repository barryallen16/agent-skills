# agent-skills

Skills I built, one folder each. Copy a folder into your agent's skills directory and the agent loads it from its `SKILL.md`.

## Skills

| Skill | What it does |
| --- | --- |
| [ui-geist-pixel](ui-geist-pixel/SKILL.md) | Builds interfaces with a terminal-tool aesthetic: sharp monochrome, pixel-display headings, 24px pixel icons, one accent color. |
| [ux-design](ux-design/SKILL.md) | Applies 20 cognitive and UX laws to layouts, navigation, forms, and dashboards to reduce effort and mistakes. |
| [writing-that-works](writing-that-works/SKILL.md) | Drafts and edits business prose so the reader knows what to do, by when, and why. Merges Thompson's clarity rules, Roman and Raphaelson's effectiveness rules, and Ogilvy's persuasion rules into one file. |

## Install

Copy the skill folder into your agent's skills directory:

```
~/.agents/skills/<skill-name>/
```

The directory name varies by agent. Each folder holds one `SKILL.md`, and its frontmatter gives the skill a name and a description of when to use it. That description is what the agent reads to decide whether to load the rest.

## Related

- [ats-resume-creation-skill](https://github.com/barryallen16/ats-resume-creation-skill) is a separate agent skill. It writes ATS-friendly software engineer resumes as real `.docx` and `.pdf` files, tailored to a job description, and keeps a persistent candidate profile that grows across sessions, tracks every application, and flags duplicates for the same company and role.

## Archive

`archive/` holds two of the source files that `writing-that-works` merged from: `write_skill.md` (Roman and Raphaelson) and `ogilvy_skill.md` (Ogilvy). They are kept for reference and are not installed as skills.
