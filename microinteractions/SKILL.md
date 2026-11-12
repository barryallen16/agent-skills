---
name: microinteractions
description: Implement and refine tactile, restrained UI microinteractions and animations using studied patterns from microinteractions.dev. Use when designing or coding button transitions, label swaps, tab indicators, hold-to-confirm buttons, drag-to-reorder lists, table drag-selection, slider tooltips, gooey radio buttons, or accordions, or when needing exact timing curves, CSS transitions, and shadcn component installation commands.
license: MIT
---

# Microinteractions

Design and implement restrained, tactile UI microinteractions based on empirical studies from microinteractions.dev.
Each study provides exact timing, easing curves, accessibility handling, and complete implementations in HTML/CSS, Tailwind, and React (via shadcn).

## Core Principles

- Restraint over spectacle.
Avoid bouncy springs, elastic overshoot, SaaS landing-page fluff, and decorative motion that slows users down.
- Zero layout shift.
Animate transforms and opacity rather than width, height, or padding.
Use CSS Grid single-cell stacking (`grid-area: 1 / 1`) to fit dynamic label widths without measuring with JavaScript.
- Direct physical tracking.
Drag handles, slider tooltips, and scroll scrubbers follow the pointer 1:1 without animation lag during active manipulation.
- Accessibility first.
Respect `prefers-reduced-motion: reduce` by replacing spatial transitions with instant jumps or fast crossfades.
Gate hover-only effects behind `@media (hover: hover) and (pointer: fine)`.
Provide clear `:focus-visible` states and full keyboard navigation for every interactive element.

## Curated Easing Curves

```css
/* Quick exit and soft deceleration for hover feedback and settlements */
--ease-out-quint: cubic-bezier(0.23, 1, 0.32, 1);

/* Snappy acceleration for repeated navigation actions */
--ease-out-expo: cubic-bezier(0.19, 1, 0.22, 1);

/* Smooth liquid and fluid transfers */
--ease-in-out-cubic: cubic-bezier(0.65, 0, 0.35, 1);

/* Asymmetric acceleration and deceleration for sliding panels */
--ease-panel: cubic-bezier(0.64, 0, 0.2, 1);
```

For damped physical vibrations such as plucked strings, use a sampled CSS `linear()` curve:
```css
--ease-damped: linear(0, 0.157, 0.424, 0.741, 1.051, 1.304, 1.471, 1.536, 1.506, 1.401, 1.247, 1.078, 0.923, 0.804, 0.734, 0.718, 0.749, 0.815, 0.9, 0.989, 1.065, 1.119, 1.146, 1.146, 1.122, 1.083, 1.036, 0.991, 0.954, 0.931, 0.922, 0.926, 0.942, 0.965, 0.989, 1.012, 1);
```

## Catalog of Studies

### Actions

1. **Text Swap Button (`text-swap`)**
Swap button labels on hover without resizing the button or causing layout shift.
Stack current and next label in `grid-area: 1 / 1`.
Duration: 220ms.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/text-swap.json`

2. **Hold to Confirm Button (`hold-confirm`)**
Hold button for 1,200ms to confirm a destructive or irreversible action.
Release early to cancel with an 180ms retract transition.
Keyboard interaction activates without animation delay.
Duration: 1,200ms hold, 160ms confirm.
Easing: `linear` for progress, `cubic-bezier(0.23, 1, 0.32, 1)` for settle.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/hold-confirm.json`

3. **Drag to Reorder (`drag-reorder`)**
Reorder list items with a rippling gap that nudges nearby rows apart.
Displacement follows `8px * 0.7^n` where `n` is distance from gap, staggered by 24ms per step.
Duration: 250ms.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/drag-reorder.json`

### Navigation

1. **Tab Indicator (`tab-indicator`)**
Slide an underline indicator to the selected tab without moving text labels.
Animate a single transform using `translateX` and `scaleX`.
Bold the selected label without triggering layout shifts.
Duration: 250ms.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/tab-indicator.json`

2. **Chevron Morph Buttons (`chevron-morph`)**
Extend a navigation chevron into a full directional arrow on hover.
Use SVG transforms and opacity on the arrow shaft.
Duration: 190ms.
Easing: `cubic-bezier(0.19, 1, 0.22, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/chevron-morph.json`

3. **Plucked Underline (`plucked-underline`)**
Animate a link underline like a vibrating string tuned by the link length.
Duration: 400ms to 1,200ms (13ms per pixel of width).
Easing: CSS `linear()` damped oscillation.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/plucked-underline.json`

4. **Worm Dots (`worm-dots`)**
Scrub carousel slides by dragging across navigation dots.
A fluid worm indicator stretches and shrinks directly with the scroll offset.
Release snaps to the nearest slide in 180ms.
Duration: 1:1 scroll tracking; 180ms snap.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/worm-dots.json`

5. **FAQ Panel (`faq-panel`)**
Accordion with a single shared sliding panel that resizes to fit the active answer.
Uses FLIP (`translateY` and `height`) via the Web Animations API.
Duration: 300ms panel slide, 140ms old text fade-out, 210ms new text fade-in.
Easing: `cubic-bezier(0.64, 0, 0.2, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/faq-panel.json`

### Controls and Manipulation

1. **Gooey Radio Group (`gooey-radio-group`)**
Pour selection liquid between radio buttons using an SVG filter and WAAPI.
Head of drop leads and tail follows with a 60ms offset.
Duration: 480ms.
Easing: `cubic-bezier(0.65, 0, 0.35, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/gooey-radio-group.json`

2. **Edge-Aware Tooltip (`edge-aware-tooltip`)**
Keep a slider value tooltip inside its parent container without clipping or viewport overflow.
Built with CSS anchor positioning (`anchor-center` and `anchor(center)`) plus clamp fallback.
Duration: 0ms (1:1 direct tracking).
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/edge-aware-tooltip.json`

3. **Drag to Select (`drag-select`)**
Select contiguous rows in a table by dragging down checkboxes.
A preview band tracks the cursor in 90ms while checkboxes check in 160ms.
Supports Shift+arrow navigation and Escape to cancel.
Duration: 90ms band, 160ms checkmark draw.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/drag-select.json`

4. **Resize Handle (`resize-handle`)**
Divider grip handle appears at the exact vertical position where the pointer touches the line.
Grip appears in 120ms after a 60ms hover delay; width adjusts 1:1 during drag.
Duration: 120ms reveal, 240ms collapse settle.
Easing: `cubic-bezier(0.23, 1, 0.32, 1)`.
Shadcn install: `npx shadcn@latest add https://microinteractions.dev/r/resize-handle.json`

## Workflow for Agents

1. Identify the interaction needed.
Match the user requirement against the catalog above.
2. For React with shadcn projects:
Run the install command:
```sh
npx shadcn@latest add https://microinteractions.dev/r/<id>.json
```
The component integrates directly with standard shadcn tokens (`bg-primary`, `text-muted-foreground`, etc.).
3. For Tailwind or Vanilla CSS projects:
Fetch the complete study source from the markdown endpoint:
```text
https://microinteractions.dev/markdown/<id>.md
```
Or read local source files from the cloned repository at `src/components/tailwind/` or `src/components/`.
4. Apply accessibility guardrails:
Check that `prefers-reduced-motion` provides an instant or crossfade fallback.
Ensure screen readers receive appropriate ARIA roles (`role="tablist"`, `aria-selected`, `aria-live`).
Verify focus rings and keyboard triggers operate cleanly without pointer dependencies.
