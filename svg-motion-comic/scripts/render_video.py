import os
import subprocess
import time
from playwright.sync_api import sync_playwright

def render(html_path='index.html', audio_path='comic_audio.wav', output_mp4='comic_motion.mp4', fps=30, duration=21.0):
    html_abs = os.path.abspath(html_path).replace('\\', '/')
    audio_abs = os.path.abspath(audio_path)
    output_abs = os.path.abspath(output_mp4)
    scratch_dir = os.environ.get('SCRATCH_DIR')

    total_frames = int(fps * duration)
    print(f"Starting render: {total_frames} frames ({duration}s @ {fps}fps)...")

    cmd = [
        'ffmpeg', '-y',
        '-f', 'image2pipe',
        '-vcodec', 'png',
        '-r', str(fps),
        '-i', '-',
        '-i', audio_abs,
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'fast',
        '-crf', '18',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-shortest',
        output_abs
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

    edge_paths = [
        os.environ.get('EDGE_PATH'),
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
    ]
    edge_executable = next((p for p in edge_paths if p and os.path.exists(p)), None)
    launch_kwargs = {'headless': True}
    if edge_executable:
        launch_kwargs['executable_path'] = edge_executable

    t0 = time.time()
    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        page = browser.new_page(viewport={'width': 1080, 'height': 1920})
        page.goto(f'file:///{html_abs}')
        page.evaluate('document.body.classList.add("render-mode")')

        # Warm up
        page.evaluate('window.renderFrame(0)')
        time.sleep(0.5)

        for frame_idx in range(total_frames):
            t = frame_idx / fps
            page.evaluate(f'window.renderFrame({t})')
            img_bytes = page.screenshot(type='png')
            proc.stdin.write(img_bytes)

            if scratch_dir and os.path.isdir(scratch_dir) and frame_idx in [10, 60, 200, 330, 450, 600, 720]:
                preview_file = os.path.join(scratch_dir, f'preview_frame_{frame_idx}.png')
                with open(preview_file, 'wb') as pf:
                    pf.write(img_bytes)

            if frame_idx % 60 == 0:
                elapsed = time.time() - t0
                pct = (frame_idx / total_frames) * 100
                fps_render = (frame_idx + 1) / max(0.001, elapsed)
                print(f"Rendered frame {frame_idx}/{total_frames} ({pct:.0f}%) - {fps_render:.1f} fps")

        browser.close()

    proc.stdin.close()
    stderr_out = proc.stderr.read().decode('utf-8', errors='ignore')
    proc.wait()

    total_time = time.time() - t0
    print(f"Render completed in {total_time:.1f}s. ffmpeg exit code: {proc.returncode}")
    if proc.returncode != 0:
        print("FFmpeg stderr:\n", stderr_out)
    else:
        file_size = os.path.getsize(output_abs)
        print(f"Output MP4: {output_abs} ({file_size / (1024*1024):.2f} MB)")

if __name__ == '__main__':
    render()
