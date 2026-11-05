# SVG Motion Comic

Turn static multi-panel comic SVGs, manga pages, and storyboards into animated vertical motion videos (9:16 MP4).
This folder contains the agent skill definition, CLI scripts, and a working demo.

## Demo

The reference project `singam-story` turns a static 1080x1920 SVG into an animated 21-second vertical motion comic.

| Input (Static SVG) | Output (Animated Motion Comic) |
| :---: | :---: |
| <img src="assets/singam-story/input.svg" width="340" alt="Input Comic SVG" /> | <video src="assets/singam-story/final.mp4" width="340" controls></video> |

Direct file links:
- [View Input SVG (7.7 MB)](assets/singam-story/input.svg)
- [Download Final Video (1.8 MB MP4)](assets/singam-story/final.mp4)

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
