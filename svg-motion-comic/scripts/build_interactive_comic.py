import os

def build_html(svg_path=None):
    if svg_path is None:
        candidates = [
            'Instagram story - 1.svg',
            os.path.join('projects', 'singam-story', 'Instagram story - 1.svg'),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'singam-story', 'input.svg'),
        ]
        svg_path = next((p for p in candidates if os.path.exists(p)), 'Instagram story - 1.svg')
    with open(svg_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line0 = '<svg id="comic-svg" width="1080" height="1920" viewBox="0 0 1080 1920" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n'
    line1 = lines[1]
    bg = lines[2]
    bird = f'<g id="bird" data-ox="116" data-oy="74">\n{lines[3]}</g>\n'
    panel1 = f'<g id="panel-1">\n{lines[4]}</g>\n'
    bubble1 = f'<g id="bubble-1" data-ox="549" data-oy="266">\n{lines[5]}{lines[6]}</g>\n'
    panel2 = f'<g id="panel-2">\n{lines[7]}</g>\n'
    bubble2 = f'<g id="bubble-2" data-ox="704" data-oy="836">\n{lines[8]}{lines[26]}</g>\n'
    panel3_left = f'<g id="panel-3-left">\n{lines[9]}{lines[10]}{lines[11]}</g>\n'
    bubble3a = f'<g id="bubble-3a" data-ox="164" data-oy="1163">\n{lines[12]}{lines[13]}</g>\n'
    panel3_right = f'<g id="panel-3-right">\n{"".join(lines[14:21])}</g>\n'
    bubble3b = f'<g id="bubble-3b" data-ox="965" data-oy="1365">\n{lines[21]}{lines[22]}</g>\n'
    panel4 = f'<g id="panel-4">\n{lines[23]}</g>\n'
    bubble4 = f'<g id="bubble-4" data-ox="184" data-oy="1627">\n{lines[24]}{lines[25]}</g>\n'
    rest = "".join(lines[27:])

    svg_assembled = (
        line0 +
        line1 +
        bg +
        bird +
        panel1 +
        panel2 +
        panel3_left +
        panel3_right +
        panel4 +
        bubble1 +
        bubble2 +
        bubble3a +
        bubble3b +
        bubble4 +
        rest
    )

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Singam Motion Comic - TXT App</title>
  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    body {{
      background: #0d0e12;
      color: #fff;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      overflow: hidden;
    }}
    #stage-container {{
      position: relative;
      width: 1080px;
      height: 1920px;
      max-height: 90vh;
      max-width: calc(90vh * 9 / 16);
      aspect-ratio: 9 / 16;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), 0 0 0 1px rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      overflow: hidden;
      background: #000;
    }}
    #comic-svg {{
      width: 100%;
      height: 100%;
      display: block;
      pointer-events: none;
    }}
    #fx-canvas {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.08s ease;
    }}
    #controls {{
      position: fixed;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
      display: flex;
      align-items: center;
      gap: 14px;
      background: rgba(20, 22, 28, 0.88);
      backdrop-filter: blur(16px);
      padding: 10px 20px;
      border-radius: 30px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 12px 32px rgba(0, 0, 0, 0.6);
      z-index: 100;
    }}
    button {{
      background: #e62117;
      color: #fff;
      border: none;
      padding: 8px 18px;
      font-size: 14px;
      font-weight: 600;
      border-radius: 20px;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: transform 0.1s, background 0.15s;
    }}
    button:hover {{
      background: #ff3326;
      transform: scale(1.04);
    }}
    button:active {{
      transform: scale(0.96);
    }}
    #scrubber {{
      width: 280px;
      accent-color: #e62117;
      cursor: pointer;
    }}
    #time-display {{
      font-family: monospace;
      font-size: 13px;
      color: #aaa;
      min-width: 90px;
    }}
    body.render-mode {{
      background: #000 !important;
      margin: 0 !important;
      padding: 0 !important;
      overflow: hidden !important;
    }}
    body.render-mode #stage-container {{
      width: 1080px !important;
      height: 1920px !important;
      max-width: none !important;
      max-height: none !important;
      border-radius: 0 !important;
      box-shadow: none !important;
    }}
    body.render-mode #controls {{
      display: none !important;
    }}
  </style>
</head>
<body>
  <div id="stage-container">
    {svg_assembled}
    <canvas id="fx-canvas" width="1080" height="1920"></canvas>
  </div>

  <div id="controls">
    <button id="btn-play">Play</button>
    <button id="btn-restart">Restart</button>
    <input type="range" id="scrubber" min="0" max="21.0" step="0.033" value="0">
    <span id="time-display">00.00 / 21.00</span>
  </div>

  <audio id="sfx-audio" src="comic_audio.wav" preload="auto"></audio>

  <script>
    const DURATION = 21.0;
    const svg = document.getElementById('comic-svg');
    const fxCanvas = document.getElementById('fx-canvas');
    const fxCtx = fxCanvas.getContext('2d');
    const btnPlay = document.getElementById('btn-play');
    const btnRestart = document.getElementById('btn-restart');
    const scrubber = document.getElementById('scrubber');
    const timeDisplay = document.getElementById('time-display');
    const audio = document.getElementById('sfx-audio');

    // Comic Panels & Bubbles
    const bird = document.getElementById('bird');
    const panel1 = document.getElementById('panel-1');
    const panel2 = document.getElementById('panel-2');
    const panel3Left = document.getElementById('panel-3-left');
    const panel3Right = document.getElementById('panel-3-right');
    const panel4 = document.getElementById('panel-4');

    const bubble1 = document.getElementById('bubble-1');
    const bubble2 = document.getElementById('bubble-2');
    const bubble3a = document.getElementById('bubble-3a');
    const bubble3b = document.getElementById('bubble-3b');
    const bubble4 = document.getElementById('bubble-4');

    // Camera Keyframes (t, cx, cy, zoom) - Snappy 21s timeline
    // 0.0 - 3.4: Panel 1
    // 3.8 - 7.8: Panel 2
    // 8.2 - 11.2: Panel 3 Left
    // 11.6 - 14.8: Panel 3 Right
    // 15.2 - 19.2: Panel 4
    // 20.0 - 21.0: Full Outro
    const cameraKeyframes = [
      {{ t: 0.0,  cx: 540, cy: 410,  zoom: 1.25 }},
      {{ t: 3.4,  cx: 540, cy: 415,  zoom: 1.23 }},
      {{ t: 3.8,  cx: 545, cy: 865,  zoom: 1.18 }},
      {{ t: 7.8,  cx: 545, cy: 871,  zoom: 1.16 }},
      {{ t: 8.2,  cx: 280, cy: 1260, zoom: 1.55 }},
      {{ t: 11.2, cx: 280, cy: 1266, zoom: 1.53 }},
      {{ t: 11.6, cx: 770, cy: 1270, zoom: 1.55 }},
      {{ t: 14.8, cx: 770, cy: 1276, zoom: 1.53 }},
      {{ t: 15.2, cx: 480, cy: 1620, zoom: 1.12 }},
      {{ t: 19.2, cx: 480, cy: 1626, zoom: 1.10 }},
      {{ t: 20.0, cx: 540, cy: 960,  zoom: 1.0 }},
      {{ t: 21.0, cx: 540, cy: 960,  zoom: 1.0 }}
    ];

    function easeInOutCubic(x) {{
      return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
    }}

    function easeOutElastic(x) {{
      if (x <= 0) return 0;
      if (x >= 1) return 1;
      const c1 = 2.4;
      const c3 = c1 + 1;
      return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2);
    }}

    function getCamera(t) {{
      let k1 = cameraKeyframes[0];
      let k2 = cameraKeyframes[cameraKeyframes.length - 1];

      for (let i = 0; i < cameraKeyframes.length - 1; i++) {{
        if (t >= cameraKeyframes[i].t && t <= cameraKeyframes[i + 1].t) {{
          k1 = cameraKeyframes[i];
          k2 = cameraKeyframes[i + 1];
          break;
        }}
      }}

      const span = k2.t - k1.t;
      const progress = span > 0 ? (t - k1.t) / span : 0;
      const eased = easeInOutCubic(progress);

      const cx = k1.cx + (k2.cx - k1.cx) * eased;
      const cy = k1.cy + (k2.cy - k1.cy) * eased;
      const zoom = k1.zoom + (k2.zoom - k1.zoom) * eased;

      // Screen shakes on punch impacts
      let shakeX = 0;
      let shakeY = 0;

      // Intro impact shake (0.08 to 0.32s)
      if (t >= 0.08 && t <= 0.32) {{
        const decay = (0.32 - t) / 0.24;
        shakeX = Math.sin(t * 60) * 10 * decay;
        shakeY = Math.cos(t * 70) * 7 * decay;
      }}
      // Panel 2 arrival impact (3.75 to 4.05s)
      if (t >= 3.75 && t <= 4.05) {{
        const decay = (4.05 - t) / 0.30;
        shakeX = Math.sin(t * 65) * 14 * decay;
        shakeY = Math.cos(t * 80) * 10 * decay;
      }}
      // Panel 3B whip arrival impact (11.55 to 11.85s)
      if (t >= 11.55 && t <= 11.85) {{
        const decay = (11.85 - t) / 0.30;
        shakeX = Math.sin(t * 70) * 12 * decay;
        shakeY = Math.cos(t * 85) * 8 * decay;
      }}

      return {{
        cx: cx + shakeX,
        cy: cy + shakeY,
        zoom: zoom
      }};
    }}

    function setBubbleTransform(el, scale, opacity) {{
      if (!el) return;
      const ox = parseFloat(el.getAttribute('data-ox'));
      const oy = parseFloat(el.getAttribute('data-oy'));
      if (scale <= 0.001 || opacity <= 0.001) {{
        el.setAttribute('transform', `translate(${{ox}}, ${{oy}}) scale(0) translate(${{-ox}}, ${{-oy}})`);
        el.style.opacity = '0';
        el.style.display = 'none';
      }} else {{
        el.style.display = '';
        el.setAttribute('transform', `translate(${{ox}}, ${{oy}}) scale(${{scale.toFixed(4)}}) translate(${{-ox}}, ${{-oy}})`);
        el.style.opacity = Math.min(1.0, opacity).toFixed(3);
      }}
    }}

    function drawSpeedLines(intensity, angle = 0) {{
      fxCtx.clearRect(0, 0, 1080, 1920);
      if (intensity <= 0.05) {{
        fxCanvas.style.opacity = '0';
        return;
      }}
      fxCanvas.style.opacity = intensity.toString();
      fxCtx.save();
      fxCtx.translate(540, 960);
      fxCtx.rotate(angle);
      fxCtx.translate(-540, -960);

      fxCtx.strokeStyle = 'rgba(255, 255, 255, 0.45)';
      fxCtx.lineWidth = 4;
      for (let i = 0; i < 28; i++) {{
        const x = (i * 41) % 1080;
        const yStart = (i * 73) % 400;
        const len = 350 + (i * 37) % 500;
        fxCtx.beginPath();
        fxCtx.moveTo(x, yStart);
        fxCtx.lineTo(x, yStart + len);
        fxCtx.stroke();
      }}
      fxCtx.restore();
    }}

    window.renderFrame = function(t) {{
      t = Math.max(0, Math.min(DURATION, t));

      // 1. Camera ViewBox
      const cam = getCamera(t);
      const w = 1080 / cam.zoom;
      const h = 1920 / cam.zoom;
      const minX = cam.cx - w / 2;
      const minY = cam.cy - h / 2;
      svg.setAttribute('viewBox', `${{minX.toFixed(2)}} ${{minY.toFixed(2)}} ${{w.toFixed(2)}} ${{h.toFixed(2)}}`);

      // 2. Sequential Panel Appearance (Focus one panel at a time)
      function evalPanelAlpha(revealTime, duration = 0.18) {{
        if (t < revealTime) return 0;
        if (t < revealTime + duration) return (t - revealTime) / duration;
        return 1.0;
      }}

      function setPanelVisibility(el, alpha) {{
        if (!el) return;
        if (alpha <= 0.001) {{
          el.style.opacity = '0';
          el.style.display = 'none';
        }} else {{
          el.style.display = '';
          el.style.opacity = Math.min(1.0, alpha).toFixed(3);
        }}
      }}

      // Panel 1: visible from start
      setPanelVisibility(panel1, 1.0);
      // Panel 2: reveals with whip pan at 3.45s
      setPanelVisibility(panel2, evalPanelAlpha(3.45));
      // Panel 3 Left: reveals at 7.85s
      setPanelVisibility(panel3Left, evalPanelAlpha(7.85));
      // Panel 3 Right: reveals at 11.25s
      setPanelVisibility(panel3Right, evalPanelAlpha(11.25));
      // Panel 4: reveals at 14.85s
      setPanelVisibility(panel4, evalPanelAlpha(14.85));

      // Red Bird: reveals during outro pullback (19.2s)
      if (t < 19.2) {{
        setBubbleTransform(bird, 0, 0);
      }} else if (t < 19.55) {{
        const p = (t - 19.2) / 0.35;
        const s = easeOutElastic(p);
        setBubbleTransform(bird, s, Math.min(1.0, p * 2));
      }} else {{
        setBubbleTransform(bird, 1.0, 1.0);
      }}

      // 3. Speech Bubble Pop helper
      function evalBubble(triggerTime, popDuration = 0.28) {{
        if (t < triggerTime) {{
          return {{ scale: 0, opacity: 0 }};
        }} else if (t < triggerTime + popDuration) {{
          const p = (t - triggerTime) / popDuration;
          const s = easeOutElastic(p);
          return {{ scale: s, opacity: Math.min(1.0, p * 3) }};
        }} else {{
          return {{ scale: 1.0, opacity: 1.0 }};
        }}
      }}

      // Bubble 1: t = 0.4s
      const b1 = evalBubble(0.4);
      setBubbleTransform(bubble1, b1.scale, b1.opacity);

      // Bubble 2: t = 4.1s
      const b2 = evalBubble(4.1);
      setBubbleTransform(bubble2, b2.scale, b2.opacity);

      // Bubble 3A: t = 8.4s
      const b3a = evalBubble(8.4);
      setBubbleTransform(bubble3a, b3a.scale, b3a.opacity);

      // Bubble 3B: t = 11.8s
      const b3b = evalBubble(11.8);
      setBubbleTransform(bubble3b, b3b.scale, b3b.opacity);

      // Bubble 4: t = 15.5s
      const b4 = evalBubble(15.5);
      setBubbleTransform(bubble4, b4.scale, b4.opacity);

      // 4. Whip pan speedline accents
      if (t >= 3.45 && t <= 3.8) {{
        const p = 1.0 - Math.abs((t - 3.62) / 0.18);
        drawSpeedLines(p * 0.75, 0);
      }} else if (t >= 11.25 && t <= 11.6) {{
        const p = 1.0 - Math.abs((t - 11.42) / 0.18);
        drawSpeedLines(p * 0.75, -0.4);
      }} else if (t >= 19.25 && t <= 19.8) {{
        const p = 1.0 - Math.abs((t - 19.52) / 0.28);
        drawSpeedLines(p * 0.5, 0);
      }} else {{
        drawSpeedLines(0);
      }}

      // Update Scrubber UI
      if (scrubber) {{
        scrubber.value = t;
        const sec = Math.floor(t).toString().padStart(2, '0');
        const cs = Math.floor((t % 1) * 100).toString().padStart(2, '0');
        timeDisplay.textContent = `${{sec}}.${{cs}} / 21.00`;
      }}
    }};

    let isPlaying = false;
    let startTime = 0;
    let animId = null;

    function play() {{
      if (isPlaying) return;
      isPlaying = true;
      btnPlay.textContent = 'Pause';
      const curT = parseFloat(scrubber.value);
      if (curT >= DURATION) {{
        startTime = performance.now();
      }} else {{
        startTime = performance.now() - curT * 1000;
      }}
      audio.currentTime = Math.min(audio.duration || DURATION, (performance.now() - startTime) / 1000);
      audio.play().catch(() => {{}});

      function tick() {{
        const elapsed = (performance.now() - startTime) / 1000;
        if (elapsed >= DURATION) {{
          window.renderFrame(DURATION);
          pause();
          return;
        }}
        window.renderFrame(elapsed);
        animId = requestAnimationFrame(tick);
      }}
      animId = requestAnimationFrame(tick);
    }}

    function pause() {{
      isPlaying = false;
      btnPlay.textContent = 'Play';
      if (animId) cancelAnimationFrame(animId);
      audio.pause();
    }}

    btnPlay.addEventListener('click', () => {{
      if (isPlaying) pause();
      else play();
    }});

    btnRestart.addEventListener('click', () => {{
      pause();
      window.renderFrame(0);
      play();
    }});

    scrubber.addEventListener('input', (e) => {{
      pause();
      window.renderFrame(parseFloat(e.target.value));
    }});

    window.renderFrame(0);
  </script>
</body>
</html>
"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("Clean index.html (21s snappy cut) assembled successfully.")

if __name__ == '__main__':
    build_html()
