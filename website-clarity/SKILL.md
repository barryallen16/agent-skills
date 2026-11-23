---
name: website-clarity
description: Builds or audits high-converting websites and landing pages through an anti-slop 4-step pipeline. Combines clarity and writing-core for copy, stitch-design-taste for visual tokens, modern-web-guidance for native platform standards, and interaction-design for tactile polish.
license: MIT
metadata:
  version: "2.0.0"
  stages: "4"
---

# Website Clarity: Anti-Slop Build Pipeline

Use this skill to audit, rewrite, or build landing pages and hero sections from scratch.
Visual polish cannot rescue copy that fails to explain the product.
Great copy falls flat if presented inside a generic, AI-generated template.
This skill coordinates a 4-step sequential pipeline with locked intermediate artifacts to prevent agents from averaging out into generic marketing slop.

## The 4-Step Pipeline Architecture

```
[ Step 1: The Message ]      [ Step 2: The System ]        [ Step 3: The Build ]         [ Step 4: The Feel ]
writing-core                 stitch-design-taste           modern-web-guidance           interaction-design
website-clarity              (or impeccable:shape)         + impeccable:persuade
       |                                |                            |                             |
Produces COPY.md             Produces DESIGN.md            Produces clean HTML/CSS       Adds tactile states
```

Do not run these steps in parallel.
Each phase depends on the locked output of the phase before it.

---

## Step 1: Message and Strategy (website-clarity + writing-core)

Focus entirely on audience, messaging hierarchy, and friction removal before writing code.

### 1. The 5-Second Clarity Test
The above-the-fold content must answer four fundamental questions immediately:
- **What do you do?** State the product or service in plain, unambiguous words.
- **Who is it for?** Identify the exact user or specific pain point.
- **What is the outcome?** State the concrete result the user achieves.
- **What happens next?** Provide exactly one primary call to action.
Remove competing buttons and secondary links from the hero.

### 2. Copy Architecture and Objection Mining
Pass the messaging requirements into `writing-core`:
- Mine actual user friction and objections rather than guessing from model weights.
- Enforce the receipts rule: require verifiable benchmark numbers, actual install commands, or transparent boundaries.
Never invent fake customer logos, fake review counts, or phantom testimonials.
- Run the copy through `humanizer` to eliminate chatbot words ("seamless", "elevate", "unleash", "delve") and forced structures.

### Deliverable: `COPY.md`
Lock the output in a `COPY.md` document.
Once written, the copy is frozen.
Later stages cannot rewrite, summarize, or edit the wording.

---

## Step 2: Visual System Specification (stitch-design-taste)

Define the visual world and strict aesthetic boundaries before generating markup.
Run `stitch-design-taste` (prefer for landing pages; use `impeccable:shape` only for full apps) to create a comprehensive `DESIGN.md`.

### 1. Palette and Typography Rules
- **Color:** Maximum 1 high-contrast accent color with saturation below 80%.
Base surfaces must use neutral zinc or slate tones.
Pure black (`#000000`) is banned.
- **Typography:** Choose a distinctive font stack (such as `Geist`, `Satoshi`, or modern serifs like `Fraunces` for editorial layouts).
Generic system fonts and standard `Inter` are banned for creative surfaces.
- **Layout Rhythm:** Use asymmetric balance or clean left-aligned grids.
Centered hero sections and generic 3-column equal card layouts are banned.

### 2. Anti-Slop Visual Bans
Explicitly ban the standard AI tropes:
- No purple or blue neon button glows.
- No floating glassmorphism cards with faint borders and blurred backgrounds.
- No decorative emojis in headings or labels.
- No generic 3D floating blobs or isometric cartoon illustrations.
- No filler instructions like "Scroll to explore" or bouncing chevron arrows.

### Deliverable: `DESIGN.md`
Lock the design rules, hex tokens, and layout guidelines in `DESIGN.md`.

---

## Step 3: Platform Assembly (modern-web-guidance + impeccable)

Implement the interface in semantic HTML with Tailwind CSS, strictly adhering to `COPY.md` and `DESIGN.md`.
Colocate utility classes directly on markup to prevent stylesheet drift, dead selectors, and arbitrary pixel sizing.

### 1. Native Web Platform Standards
Query `modern-web-guidance` before implementing UI patterns:
- Use native HTML elements (such as `<dialog>` and Popover API) instead of bloated external libraries.
- Use CSS container queries and `:has()` for component responsiveness.
- Use `min-h-[100dvh]` instead of `h-screen` to prevent iOS Safari viewport jumps.
- Add `fetchpriority="high"` and explicit aspect ratios to hero images to protect Largest Contentful Paint (LCP).

### 2. Responsive Layout and Craft Floor
Use `impeccable` in `Persuade` mode to execute the layout with Tailwind CSS:
- Enforce calibrated Tailwind spacing and typography scales (`p-6`, `gap-8`, `text-sm`, `zinc-950`).
Do not use arbitrary one-off pixel values like `p-[19px]`.
- Collapse all multi-column sections to a clean single-column layout on mobile screens (`grid-cols-1 md:grid-cols-2`).
- Guarantee zero horizontal scroll on mobile viewports.
- Maintain a minimum tap target of 44px for all buttons and interactive controls.
- Verify color contrast ratios to meet WCAG AA standards.

### Deliverable: Clean HTML + Tailwind CSS Implementation
The page markup is fully rendered with zero client-side JavaScript hydration overhead.

---

## Step 4: Tactile Polish (interaction-design)

Add physical feedback and motion after the layout and markup are stable.
Run `interaction-design` to apply tactile polish without disrupting layout structure.

### 1. Motion Rules and Micro-Interactions
- **Timing:** Keep hover and click feedback between 100ms and 150ms.
Transitions between 200ms and 300ms.
- **Physics:** Use spring easing (`stiffness: 100, damping: 20`) instead of linear or artificial timing curves.
- **Button Feedback:** Apply subtle active states (such as a 1px downward translate or slight scale change) on press.

### 2. Motion Accessibility
Wrap all CSS transitions and JavaScript animations in reduced-motion guards:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

### Deliverable: Final Interactive Surface
The completed website is responsive, fast, tactile, and free of AI tells.
