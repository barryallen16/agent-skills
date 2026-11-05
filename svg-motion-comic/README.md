# SVG Motion Comic

Turn static multi-panel comic SVGs, manga pages, and storyboards into animated vertical motion videos (9:16 MP4).
This folder contains the agent skill definition, CLI scripts, and a working demo.

## Demo

The reference project `singam-story` turns a static 1080x1920 SVG into an animated vertical motion comic.

| Input (Static SVG) | Output (Animated Preview) |
| :---: | :---: |
| <img src="assets/singam-story/input.svg" width="300" alt="Input Comic SVG" /> | <img src="assets/singam-story/demo_preview.gif" width="300" alt="Motion Comic Preview" /> |

Direct file links:
- [View Input SVG (7.7 MB)](assets/singam-story/input.svg)
- [Download Final Video with Audio (620 KB MP4)](assets/singam-story/final.mp4)

## Files

- [SKILL.md](SKILL.md): Agent instructions for camera math, SVG grouping, easing curves, and audio synthesis.
- [scripts/](scripts/): Zero-dependency Python SFX generator, headless Playwright renderer, and CLI.
- [assets/singam-story/](assets/singam-story/): Demo input and output assets.

## Quick Start

```sh
# Inspect comic layers
uv run python scripts/comic_cli.py inspect singam-story

# Build HTML animator and synthesize audio
uv run python scripts/comic_cli.py build singam-story

# Render MP4 video
uv run python scripts/comic_cli.py render singam-story
```
