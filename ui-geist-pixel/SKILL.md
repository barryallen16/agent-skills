---
name: ui-geist-pixel
description: Build interfaces that feel like a terminal tool - sharp, monochrome, slightly retro, with pixel-display headings and 24px pixel icons. Use whenever the user asks for a terminal, dev-tool, or retro-pixel aesthetic, mentions Geist Pixel, Geist font, or pixelarticons, or wants a monochrome dashboard with one accent color. Reach for it even when the user only describes the vibe ("make it feel like a CLI", "pixel font headers") without naming the font or icon set.
---

# Geist Pixel UI

Sharp, monochrome, slightly retro, still clean. Two faces, one accent, pixel icons on a 24px grid.

## Fonts

Two faces, nothing else:
- Headings, brand, button labels: "Geist Pixel".
- Everything else: "Geist", weights 300-600.

Geist Pixel ships at weight 400 only. Setting 500 or higher makes the browser synthesize bold, which smears the pixel grid. Keep headings at 400 and get hierarchy from size and color instead.

```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@300;400;500;600&family=Geist+Pixel&display=swap" rel="stylesheet" />
```

```css
h1, h2, h3, .brand { font-family: "Geist Pixel", monospace; font-weight: 400; letter-spacing: 1px; }
body { font-family: "Geist", system-ui, sans-serif; }
```

Keep headings to a few words. Pixel glyphs lose legibility as strings get long, and uppercase only helps at small sizes.

## Icons: pixelarticons

MIT, 1000+ icons on a 24x24 grid. Fetch by kebab-case name:

```
https://raw.githubusercontent.com/halfmage/pixelarticons/master/svg/<name>.svg
```

Reliable names: `search`, `send`, `user`, `database`, `message-text`, `robot-face`, `sparkles`, `arrow-right`.

Inline the SVG so `fill="currentColor"` inherits text color, and size with CSS. Render at 24px or 16px only. Pixel art has no sub-pixel geometry, so odd sizes blur.

```html
<span class="icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="currentColor">...</svg></span>
```
```css
.icon { width: 24px; height: 24px; display: inline-flex; color: var(--accent); }
```

## Color and layout

Default dark palette. Swap the values, keep the structure:
- background `#0b0c10`, panels `#13141a`, lines `#26272f`
- exactly one accent, `#7c5cff`
- 1px borders, 6-8px radius, no shadows, no gradients

Shell: fixed sidebar + flexible main, collapsing to one column under 720px.

## UX laws that matter for this aesthetic

Pixel type and monochrome palettes have specific failure modes. Design against them:
- **Contrast:** pixel stems are thin, so text needs more contrast than a normal sans. Body copy at `#e6e7eb` on `#0b0c10`, never gray-on-gray.
- **Hit areas (Fitts):** a 24px glyph is a small target. Every icon button gets at least a 40x40 hit area, even when the glyph stays 16 or 24.
- **One accent (Von Restorff):** the accent is the only emphasis you get. Two accent-colored elements means neither reads as primary.
- **Spacing carries hierarchy (Proximity, Prägnanz):** no shadows to lean on. Group with space and 1px lines, and do not box every section.
- **Feedback (Doherty):** terminal UIs invite fast clicking. Every action produces a visible change within 400ms - a pressed state, a spinner, or a line in the log.
- **One primary action (Von Restorff):** only ONE element per screen gets the accent fill. Secondary actions (copy, cancel, dismiss, retry) are outline or ghost buttons, never accent-filled. If a screen has two accent-filled buttons, one of them is wrong.

For the full set of 20 laws, use the `ux-design` skill alongside this one.

## Self-check before finishing

- Geist Pixel loads and headings are still weight 400
- every icon is 24px or 16px, inlined, inheriting `currentColor`
- one accent color, no gradients, no large shadows
- every interactive element has a `:focus-visible` outline
- exactly one accent-filled element per screen
