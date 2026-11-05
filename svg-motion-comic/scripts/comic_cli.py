#!/usr/bin/env python3
"""
Agent eXperience Interface (AXI) CLI for SVG Motion Comic Video Generation.
Complies with AXI specification: content-first, token-efficient TOON output,
minimal schemas, non-interactive flags, and actionable help.
"""

import sys
import os
import argparse
import subprocess
import json
import xml.etree.ElementTree as ET

VERSION = "1.0.0"

def fast_version_check():
    if len(sys.argv) == 2 and sys.argv[1] in ("-v", "-V", "--version"):
        print(f"comic-cli {VERSION}")
        sys.exit(0)

fast_version_check()

def find_projects(workspace_dir="."):
    projects_dir = os.path.join(workspace_dir, "projects")
    projects = []
    if os.path.isdir(projects_dir):
        for item in os.listdir(projects_dir):
            p_path = os.path.join(projects_dir, item)
            if os.path.isdir(p_path):
                svgs = [f for f in os.listdir(p_path) if f.lower().endswith(".svg")]
                video_dir = os.path.join(p_path, "videos")
                videos = [f for f in os.listdir(video_dir) if f.lower().endswith(".mp4")] if os.path.isdir(video_dir) else []
                projects.append({
                    "id": item,
                    "path": p_path,
                    "svg": svgs[0] if svgs else "none",
                    "videos_count": len(videos),
                    "latest_video": videos[0] if videos else "none"
                })
    return projects

def cmd_home():
    projects = find_projects(".")
    print(f"bin: uv run python comic_cli.py")
    print(f"description: Turn multi-panel comic SVGs into animated vertical motion videos (MP4)")
    print(f"count: {len(projects)} projects registered")
    if projects:
        print(f"projects[{len(projects)}]{{id,svg,status,latest_video}}:")
        for p in projects:
            status = "rendered" if p["videos_count"] > 0 else "ready"
            print(f'  {p["id"]},{p["svg"]},{status},{p["latest_video"]}')
    else:
        print("projects: 0 projects found in projects/ directory")
    print(f"help[3]:")
    print(f'  Run `uv run python comic_cli.py inspect <project>` to analyze SVG layers and layout')
    print(f'  Run `uv run python comic_cli.py build <project> [--duration <sec>]` to generate player & audio')
    print(f'  Run `uv run python comic_cli.py render <project> [--fps 30]` to export MP4 video')

def resolve_project_svg(target):
    # Target can be project id, folder, or svg file
    if os.path.isfile(target) and target.lower().endswith(".svg"):
        return os.path.dirname(target) or ".", target
    if os.path.isdir(os.path.join("projects", target)):
        p_dir = os.path.join("projects", target)
        svgs = [f for f in os.listdir(p_dir) if f.lower().endswith(".svg")]
        if svgs:
            return p_dir, os.path.join(p_dir, svgs[0])
    if os.path.isdir(target):
        svgs = [f for f in os.listdir(target) if f.lower().endswith(".svg")]
        if svgs:
            return target, os.path.join(target, svgs[0])
    # Check root for svg
    root_svgs = [f for f in os.listdir(".") if f.lower().endswith(".svg")]
    if root_svgs:
        return ".", root_svgs[0]
    return None, None

def cmd_inspect(target):
    p_dir, svg_file = resolve_project_svg(target)
    if not svg_file or not os.path.exists(svg_file):
        print(f"error: project or SVG not found for `{target}`")
        print(f"help: provide a valid project folder or SVG path: `uv run python comic_cli.py inspect <project>`")
        sys.exit(1)

    with open(svg_file, "r", encoding="utf-8") as f:
        content = f.read()

    tree = ET.parse(svg_file)
    root = tree.getroot()
    viewbox = root.attrib.get("viewBox", "0 0 1080 1920")
    images = len(root.findall(".//{http://www.w3.org/2000/svg}image"))
    paths = len(root.findall(".//{http://www.w3.org/2000/svg}path"))
    rects = len(root.findall(".//{http://www.w3.org/2000/svg}rect"))

    print(f"project: {target}")
    print(f"svg_file: {svg_file} ({len(content) / (1024*1024):.2f} MB)")
    print(f"viewBox: {viewbox}")
    print(f"stats: {images} images, {rects} rectangles, {paths} vector paths")
    print(f"help: Run `uv run python comic_cli.py build {target}` to compile the animation")

def get_script_path(name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    candidate = os.path.join(base_dir, name)
    if os.path.exists(candidate):
        return candidate
    scripts_candidate = os.path.join(base_dir, "scripts", name)
    if os.path.exists(scripts_candidate):
        return scripts_candidate
    return name

def cmd_build(target, duration=21.0):
    p_dir, svg_file = resolve_project_svg(target)
    if not svg_file:
        print(f"error: project or SVG `{target}` not found")
        sys.exit(1)

    print(f"status: building animation for `{target}` (duration: {duration:.1f}s)...")
    subprocess.run(["uv", "run", "python", get_script_path("generate_sfx.py")], check=True)
    subprocess.run(["uv", "run", "python", get_script_path("build_interactive_comic.py")], check=True)
    print(f"output: index.html and comic_audio.wav updated")
    print(f"help: Run `uv run python comic_cli.py render {target}` to render to MP4")

def cmd_render(target, fps=30):
    p_dir, svg_file = resolve_project_svg(target)
    if not svg_file:
        print(f"error: project or SVG `{target}` not found")
        sys.exit(1)

    print(f"status: rendering {target} to MP4 via Playwright and FFmpeg (fps: {fps})...")
    subprocess.run(["uv", "run", "python", get_script_path("render_video.py")], check=True)
    video_dir = os.path.join(p_dir, "videos")
    os.makedirs(video_dir, exist_ok=True)
    target_mp4 = os.path.join(video_dir, "comic_motion.mp4")
    if os.path.exists("comic_motion.mp4"):
        import shutil
        shutil.copy("comic_motion.mp4", target_mp4)
    file_size = os.path.getsize(target_mp4) if os.path.exists(target_mp4) else 0
    print(f"result: success")
    print(f"video: {target_mp4} ({file_size / (1024*1024):.2f} MB)")
    print(f"help: open `{target_mp4}` in any video player to review output")

def main():
    if len(sys.argv) == 1:
        cmd_home()
        sys.exit(0)

    parser = argparse.ArgumentParser(
        prog="comic",
        description="Transform multi-panel comic SVGs into animated vertical motion videos (MP4)",
        add_help=True
    )
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List comic projects in the workspace")

    # inspect
    inspect_parser = subparsers.add_parser("inspect", help="Inspect comic SVG structure, dimensions, and layers")
    inspect_parser.add_argument("project", help="Project identifier or SVG path")

    # build
    build_parser = subparsers.add_parser("build", help="Build interactive HTML animator and synthesize audio")
    build_parser.add_argument("project", help="Project identifier or SVG path")
    build_parser.add_argument("--duration", type=float, default=21.0, help="Total animation duration in seconds")

    # render
    render_parser = subparsers.add_parser("render", help="Render MP4 video via Playwright & FFmpeg")
    render_parser.add_argument("project", help="Project identifier or SVG path")
    render_parser.add_argument("--fps", type=int, default=30, help="Frames per second (default: 30)")

    args = parser.parse_args()

    if args.command == "list":
        cmd_home()
    elif args.command == "inspect":
        cmd_inspect(args.project)
    elif args.command == "build":
        cmd_build(args.project, duration=args.duration)
    elif args.command == "render":
        cmd_render(args.project, fps=args.fps)
    else:
        cmd_home()

if __name__ == "__main__":
    main()
