---
name: writing-core
description: Drafts and edits prose through a four-stage pipeline - voice DNA and objection mining, structure, persuasion (commercial only), and AI-tell removal with style-whitelist protection. Use for developer READMEs, technical launch posts, emails, memos, reports, proposals, and landing pages that must sound like an authentic human builder. Invoke as /writing-core.
disable-model-invocation: true
license: MIT
metadata:
  version: "2.0.0"
  stages: "4"
---

# Writing Core

Four stages chained into an authentic writing engine.
This file coordinates routing and precedence.
It duplicates no source content.

| Stage | Skill / Module | Path | Purpose |
|---|---|---|---|
| 0 | Voice DNA & Objection Mining | Built-in / `agent-reach` | Extract author voice constraints (L1-L6) and mine live user objections from Reddit/X |
| 1 | writing-that-works + Dev Formats | `~/.agents/skills/writing-that-works/SKILL.md` | Determine structure, document layout, and delivery format |
| 2 | mindfluence + scientific-advertising | `~/.agents/skills/mindfluence/` & `~/.agents/skills/scientific-advertising/` | Persuasion gate: commercial offer architecture, proof, and switching economics |
| 3 | humanizer (with Whitelist Precedence) | `~/.agents/skills/humanizer/SKILL.md` | Strip universal chatbot tells while protecting authentic author style quirks |

Read the stage file before executing that stage.
Do not work from this summary table alone.

## Stage 0: Voice DNA and Objection Pre-Flight

Run Stage 0 before selecting any structure or writing a word.

### 1. Voice Distillation (When an author or samples are available)
Deconstruct the author into a 6-layer operational stack:
- **L1 Surface Language**: Average sentence length (target word count), short-sentence punchline ratio, punctuation habits, and active verbs.
- **L2 Structure**: Opening hook mechanics (empirical datum, scene, bold assertion) under 200 words, transition timing, and closure shape.
- **L3 Topic Logic**: Point of view, explicit exclusions, and taboo topics.
- **L4 Evidence Strategy**: Primary observations, benchmark logs, code diffs, and screen recordings over secondary assertions.
- **L5 Cognitive Worldview**: Core engineering theses and evaluation standards for good work.
- **L6 Visual Rhythm**: Pacing per 1,000 words, code block density, and heading tiers.

Output from L1-L6 creates an **Active Style Whitelist**.
Any authentic author habit (such as sentence fragments, parenthetical asides, or specific punctuation) recorded on this whitelist is exempt from Stage 3 cleanup.

### 2. Objection Mining (When drafting public launches or commercial copy)
Do not guess customer friction from model weights.
Use `agent-reach` or web search to capture exact verbatim phrases from Reddit (`r/ExperiencedDevs`, `r/programming`, `r/localllama`) and X using high-tension query operators:
- `"<competitor> annoying OR broken OR frustrated"` -> captures current breaking points.
- `"alternatives to <competitor>"` -> captures feature trade-offs users actively seek.
- `"the only thing stopping me <category>"` -> captures adoption and installation blockers.

Classify all mined quotes into the 7 Core Developer Objections:
1. Competitor comparison (why not incumbent X?)
2. Stack and environment compatibility
3. Clarity of primary utility
4. Benchmark reproducibility
5. Data privacy and telemetry boundaries
6. Token usage and recurring costs
7. Project maintenance and abandonment risk

Neutralize the identified objections directly in Stage 1 and Stage 2.

## Stage 1: Document Formats

For traditional business writing, follow `~/.agents/skills/writing-that-works/SKILL.md` (emails, memos, letters, decks, proposals, resumes).
For software, devtools, and engineering releases, use the native developer templates below:

### 1. The 6-Part Developer README
1. **Hook (Fold 1)**: Single sentence declaring exact utility and target developer. No hype adjectives ("blazing-fast", "next-gen"). Clean badges: CI, license, release version.
2. **Visual Demo (Fold 1/2)**: 30-second unedited terminal GIF or MP4 showing immediate input-to-output execution.
3. **Zero-Friction Install (Fold 2)**: One copy-pasteable command (`uv tool install <pkg>` or `pnpm i -g <pkg>`). No mandatory account signups or API keys for local runs.
4. **Mechanism (Fold 3)**: Concrete architecture diagram (Mermaid or ASCII flow) explaining how the internals solve the problem.
5. **Receipts & Honest Limits (Fold 4)**: Verifiable benchmark figures with reproducible test scripts. Prominent "Works with / Doesn't work with yet" matrix. Transparent privacy and telemetry disclosure.
6. **The Ask (Fold 5)**: Permissive OSS license, repository link, and an invitation to test a specific subsystem or submit debug logs.

### 2. Hacker News Show HN
- **Title**: `Show HN: <Name> - <Specific, concrete, factual technical utility>`
- **Author Comment**:
  - Sentence 1: Why you built it (specific personal friction with existing tools).
  - Sentence 2: Exact interface and architecture.
  - Bullet points: Concrete technical differences vs incumbents (runs locally, no cloud relay, zero telemetry).
  - Honest limits: Current edge cases, scale thresholds, and reproducible benchmark commands.
  - License and repository link.

### 3. Technical Launch Thread (X / Twitter)
- **Tweet 1 (Hook & Media)**: Name the tool, the specific pain it removes, and attach the 30-second unedited demo video. Zero outbound links in Tweet 1.
- **Tweet 2 (Mechanism)**: Explain the architectural trick that makes it work where naive solutions break.
- **Tweet 3 (Stack & Limits)**: List supported environments and honest edge cases.
- **Tweet 4 (Install Command)**: The exact 10-second command to run it locally.
- **Tweet 5 (The Ask & Link)**: Repository link, license, and invitation for feedback on issues.

## Stage 2 Gate: Persuasion & Offer Architecture

**Run Stage 2** when the artifact is public or commercial:
Developer README, Show HN post, launch thread, landing page, pricing page, sales copy, case study, or cold outreach.

**Skip Stage 2** for internal documents:
Memos, reports, internal emails, technical RFCs, postmortems, code comments, and resumes.

When Stage 2 runs:
- Consult `~/.agents/skills/mindfluence/decision-matrix.md` for cognitive bias priorities.
- Pair with `~/.agents/skills/scientific-advertising/SKILL.md` for offer architecture: specific metrics over superlatives, risk-reversal mechanics, and full-story completeness.
- **Developer Rule**: For developer audiences, replace emotional manipulation with switching economics, transparent boundaries, and verifiable proof.

## Stage 3: Tell Removal & Whitelist Precedence

Stage 3 runs on every artifact.

### The Conflict Precedence Rule
`humanizer` removes statistical chatbot tells: "delve", "crucial", "testament", "not X but Y", staged run-ups ("Let's dive in"), forced triads, and chatbot residue.
However, authentic human writing contains intentional quirks.
The precedence rule is strict:
1. **Chatbot Residue (§22), Knowledge Disclaimers (§23), and AI Words (§12)** are always stripped.
2. **The Active Style Whitelist (Stage 0) overrides structural linter bans**:
   - If the author's DNA uses sentence fragments, keep them.
   - If the author's DNA uses short punchlines or specific punctuation, keep them.
   - If the author naturally uses parenthetical asides or casual phrasing, do not smooth them into corporate gray paste.
3. Without a Stage 0 profile, apply `humanizer` standard rules with the known conflict resolutions:
   - "Not X, but Y": keep only when correcting a real belief held by the reader with factual data.
   - Fragment stacking: keep when carrying sensory or technical detail; cut when purely dramatic.
   - Bold labels: keep in structural diagrams and tables; remove from standard prose.

## Editing Discipline

Never invent, estimate, or hallucinate metrics, benchmarks, latencies, dataset sizes, or percentages.
Every figure must trace directly to verified repository benchmarks, committed code, or user input.
If necessary numbers are missing, formulate a concrete command to measure them, present it to the user, and wait for confirmation.
Social proof requires verifiable attribution; otherwise, state the claim without the phantom quote.
