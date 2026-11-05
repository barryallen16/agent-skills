---
name: svg-motion-comic
description: Convert multi-panel comic SVGs, manga pages, and storyboards into animated vertical motion videos (9:16 MP4). Use when creating animated reels from static comic strips, choreographing SVG viewBox camera pans and zooms, popping speech bubbles with sound effects, or synthesizing audio effects without external dependencies.
license: MIT
---

# SVG Motion Comic

Convert static multi-panel comic strips, manga pages, and storyboards exported as SVGs into animated vertical motion videos (9:16 MP4).
This skill covers layer decomposition, camera math, audio synthesis, and headless browser rendering.

## 1. Demo and Reference Assets

The skill includes a full working reference project in `assets/singam-story/`.

- Input SVG: [input.svg](assets/singam-story/input.svg) (1080x1920 vertical canvas with 4 comic panels and vector speech bubbles)
- Output MP4: [final.mp4](assets/singam-story/final.mp4) (21-second rendered video at 30 fps with camera moves, bubble pops, and sound effects)
- Case study recipe: [build_interactive_comic.py](scripts/build_interactive_comic.py)

## 2. Pipeline Overview

The pipeline transforms a multi-panel SVG into an MP4 video without dedicated video editing software.

```
SVG Input (Figma or Illustrator)
   │
   ├── 1. Structural Analysis (layers, patterns, paths, bounding boxes)
   ├── 2. HTML5 Stage Assembly (DOM grouping, SVG viewBox camera, canvas FX)
   ├── 3. Audio Synthesis (stdlib Python wave: whoosh, comic pop, bass thump)
   ├── 4. Headless Frame Rendering (Playwright Edge or Chromium at 30 fps)
   └── 5. FFmpeg Multiplexing (H.264 High Profile + AAC stereo MP4)
```

## 3. Project Organization

Group each design in its own directory under `projects/<project-id>/`.
Keep generated output videos inside `projects/<project-id>/videos/`.

```
workspace/
├── comic_cli.py               # AXI CLI entry point
├── projects/
│   ├── singam-story/          # Comic project directory
│   │   ├── Instagram story - 1.svg
│   │   └── videos/            # Rendered video outputs
│   │       └── comic_motion.mp4
├── .gitignore                 # Ignores *.mp4 and projects/*/videos/
```

Always add output video paths to `.gitignore` when working locally:

```gitignore
*.mp4
videos/
projects/*/videos/
```

## 4. SVG Decomposition and Layer Grouping

Figma and Illustrator export nested groupings with pattern fills and outlined text.

### Handling Namespaces

When parsing SVGs with Python `xml.etree.ElementTree`, register the standard namespaces before serializing.
Unregistered namespaces generate prefixes such as `<ns0:defs>`, which break browser pattern fills and render black fills.

```python
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.w3.org/2000/svg')
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
```

### Element Grouping

Wrap logical layers into tagged groups with anchor coordinates:
- `panel-<n>`: Frame borders and artwork for a specific panel.
- `bubble-<n>`: Speech bubble shapes and text paths. Include `data-ox` and `data-oy` coordinates for pop origins.
- `mascot` or `logo`: Header marks displayed only during the final reveal.

## 5. Camera Math (viewBox Dynamic Cropping)

Animate the SVG `viewBox="minX minY width height"` instead of transforming DOM containers.
The browser scales vector paths smoothly without raster pixelation or clipping boundaries.

Use this formula for a camera centered at `(cx, cy)` with zoom factor `zoom`:

```javascript
const width = 1080 / zoom;
const height = 1920 / zoom;
const minX = cx - width / 2;
const minY = cy - height / 2;
svg.setAttribute('viewBox', `${minX.toFixed(2)} ${minY.toFixed(2)} ${width.toFixed(2)} ${height.toFixed(2)}`);
```

### Zoom Guidelines

- Full board overview (outro): `zoom = 1.0` (viewBox: `0 0 1080 1920`).
- Standard horizontal panel: `zoom = 1.15` to `1.25`. This preserves dialogue within standard safe zones.
- Split half-panel: `zoom = 1.50` to `1.65`. Centers on the speaker and corresponding dialogue bubble.
- Close-up: `zoom = 2.0` to `2.4`. Useful for sound effect words or character expressions.

## 6. Comic Animation Choreography

### Sequential Panel Reveals

Keep upcoming panels hidden using `display: none` or zero opacity.
Make each panel visible as the camera reaches it, accompanied by an arrival sound.

### Elastic Speech Bubble Pops

Reveal dialogue bubbles 0.3 to 0.5 seconds after the camera settles on a panel.
Use an overshoot curve so the bubble expands to 1.15x before resting at 1.0x:

```javascript
function easeOutElastic(x) {
  if (x <= 0) return 0;
  if (x >= 1) return 1;
  const c1 = 2.4;
  const c3 = c1 + 1;
  return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2);
}
```

### Screen Shake

Apply decaying sine offsets to `cx` and `cy` on impacts:

```javascript
if (t >= impactTime && t <= impactTime + 0.3) {
  const decay = (impactTime + 0.3 - t) / 0.3;
  shakeX = Math.sin(t * 65) * 12 * decay;
  shakeY = Math.cos(t * 80) * 8 * decay;
}
```

### Pacing Guidelines

- Short reaction (3 to 6 words): 2.5 to 3.2 seconds.
- Moderate dialogue (7 to 14 words): 3.5 to 4.2 seconds.
- Long dialogue (15+ words): 4.5 to 5.2 seconds.
- Outro board view: 1.5 to 2.5 seconds.
- Total video duration for short vertical reels: 18 to 24 seconds.

## 7. Audio Synthesis Without Dependencies

Synthesize sound effects with the Python standard library `wave` and `math` modules.

- Comic Pop: Frequency drops from 850 Hz to 220 Hz over 0.18s with steep exponential volume decay.
- Whoosh: Filtered noise and frequency sweep modulated over 0.35s with stereo panning.
- Punch Thud: 110 Hz tone decaying to 40 Hz with an initial transient click.
- Sub-Bass Outro: 80 Hz sine wave decaying to 32 Hz over 1.8s for the full board reveal.

## 8. Headless Frame Capture and Video Encoding

Render frames via Playwright and pipe raw PNG byte streams directly to FFmpeg.
This eliminates frame drops and guarantees audio sync.

```python
cmd = [
    'ffmpeg', '-y',
    '-f', 'image2pipe',
    '-vcodec', 'png',
    '-r', '30',
    '-i', '-',
    '-i', 'comic_audio.wav',
    '-c:v', 'libx264',
    '-pix_fmt', 'yuv420p',
    '-preset', 'fast',
    '-crf', '18',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-shortest',
    'comic_motion.mp4'
]
```

## 9. CLI Usage

Run the project CLI tool with `uv`:

```sh
# Show registered projects and commands
uv run python comic_cli.py

# Inspect SVG structure, dimensions, and layer counts
uv run python comic_cli.py inspect singam-story

# Build HTML animator and synthesize WAV sound effects
uv run python comic_cli.py build singam-story --duration 21.0

# Render MP4 video at 30 fps
uv run python comic_cli.py render singam-story --fps 30
```
