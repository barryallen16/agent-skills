---
name: call-it
description: >
  Generate distinct, memorable names for products, repos, CLIs, and tools.
  Enforces Watkins' SMILE and SCRATCH filters and Altman's tactile naming heuristics.
  Eliminates AI naming slop, generic Latin affixes, and corporate jargon.
argument-hint: "[product or repo description]"
user-invocable: true
metadata:
  version: "1.0.0"
---

# Naming Skill

Generate human, memorable, and durable names for tools, open-source repos, and products.
This skill rejects generic machine-generated clichés and uses proven branding mechanics from Alexandra Watkins and Eli Altman.

## 1. The Anti-AI Slop Gate

Instantly reject any candidate matching these patterns:

1. Latinate and trendy suffixes: `-ify`, `-ly`, `-io`, `-ai`, `-ster`, `-flow`, `-sync`.
2. Corporate prefix slop: `Omni-`, `Cogni-`, `Intelli-`, `Smart-`, `Auto-`, `Hyper-`, `Neuro-`, `Syn-`.
3. Generic compound mashups: `PromptCraft`, `IdeaForge`, `TaskMaster`, `BrainWave`.
4. Empty abstract nouns: `Synergy`, `Vanguard`, `Apex`, `Nexus`, `Horizon`.
5. CamelCase styling: tools and repos must work in clean lowercase in terminal environments.

## 2. Watkins SCRATCH Filter (Dealbreakers)

Discard any name that fails any of these 7 checks:

- Spelling-challenged: Not spelled how it sounds, or altered just to grab a domain.
- Copycat: Closely resembles a competitor or copies temporary industry fads.
- Restrictive: Locks the project into an implementation detail that hinders future evolution.
- Annoying: Forced puns, contrived portmanteaus, or cutesy spellings.
- Tame: Sterile, flat descriptions that reveal zero perspective or craft.
- Curse of knowledge: Meaning is buried under insider jargon or academic papers.
- Hard to pronounce: Stumbles when spoken aloud or has ambiguous syllable emphasis.

## 3. Watkins SMILE Goals (Target Qualities)

Prioritize candidates that hit these 5 traits:

- Suggestive: Hints at the purpose, posture, or spirit rather than reciting the specification.
- Meaningful: Anchors to concepts and vocabulary users already understand.
- Imagery: Evokes a concrete physical picture in the mind.
- Legs: Gives room for a theme, sub-commands, companion tools, or community memes.
- Emotional: Prompts a subtle reaction, a nod, or a smile.

## 4. Altman Tactile Principles

Apply these execution heuristics from *Don't Call It That*:

1. The Singularity Rule:
A name can only carry one idea well.
Trying to make a name convey speed, security, intelligence, and simplicity results in mush.
Never force "trust" into a name; asserting trust upfront creates suspicion.

2. Favor Real Words:
Real words already carry subconscious texture and emotional baggage.
Invented words require heavy marketing spend to build meaning from nothing.
Pairing two ordinary words into an unexpected combination creates sticking power without spelling errors.

3. The Radio Test:
Say the name aloud in a sentence.
If another person cannot type it accurately into a browser or terminal on the first try, discard it.

4. The Monospace Test:
Evaluate how the name looks in plain lowercase monospace text: `repo-name`, `npm install name`, or `git clone`.
It must look balanced, short, and uncluttered.

## 5. Naming Archetypes

Group candidate generation across these four proven patterns:

1. Physical Tool or Tangible Object:
Anchors the software to a physical equivalent in the real world.
Examples: `docker`, `stripe`, `linear`, `anvil`, `treehouse`, `hairline`.

2. Plain Intent or Spoken Idiom:
Names derived from literal intent, direct instructions, or conversational phrases.
Examples: `no-mistakes`, `backpass`, `gnhf`, `dont-starve`, `make`.

3. Role or Crew Persona:
Frames the software as an actor with a specific job or attitude.
Examples: `firstmate`, `scout`, `concierge`, `porter`, `butler`.

4. Punchy Monosyllabic Root:
Short, tactile Anglo-Saxon roots with hard consonants.
Examples: `git`, `slack`, `bun`, `rust`, `curl`.

## 6. Execution Workflow

When naming a project, execute these steps:

1. Extract the Single Essence:
State in one sentence what the tool physically does for the human user.
Strip all buzzwords ("leverages AI", "cutting-edge", "next-gen").

2. Generate 12 to 16 Candidates:
Draft 3 to 4 options across each of the 4 Archetypes.
Run each candidate through the Anti-AI Slop Gate and the Watkins SCRATCH filter.

3. Screen the Top 4:
Run the Radio Test and the Monospace Test on the survivors.
Check availability in package registries (`npm`, `pypi`, `crates.io`) and GitHub.

4. Deliver Recommendation:
Present the top 4 candidates with their archetype, mental image, and CLI ergonomics.
Do not deliver a generic list; provide concrete rationale based on the filters above.
