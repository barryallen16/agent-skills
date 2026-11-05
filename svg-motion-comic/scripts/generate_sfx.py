import math
import struct
import wave
import random

def generate_sfx(sample_rate=44100, total_duration=21.0):
    num_samples = int(sample_rate * total_duration)
    # Stereo buffers
    left = [0.0] * num_samples
    right = [0.0] * num_samples

    def add_sample(t_sec, val_l, val_r=None):
        if val_r is None:
            val_r = val_l
        idx = int(t_sec * sample_rate)
        if 0 <= idx < num_samples:
            left[idx] += val_l
            right[idx] += val_r

    # Pop generator (comic bubble pop)
    def trigger_pop(start_time, volume=0.75, pitch_factor=1.0):
        duration = 0.18
        n = int(duration * sample_rate)
        phase = 0.0
        for i in range(n):
            t = i / sample_rate
            freq = (850 * math.exp(-22 * t) + 220) * pitch_factor
            phase += 2 * math.pi * freq / sample_rate
            amp = volume * math.exp(-18 * t)
            sample = amp * math.sin(phase)
            add_sample(start_time + t, sample, sample)

    # Whoosh generator (whip pan)
    def trigger_whoosh(start_time, duration=0.32, volume=0.6, pan=0.0):
        n = int(duration * sample_rate)
        phase = 0.0
        for i in range(n):
            t = i / sample_rate
            env = math.sin(math.pi * (t / duration)) ** 1.5
            freq = 200 + 600 * math.sin(math.pi * (t / duration))
            phase += 2 * math.pi * freq / sample_rate
            noise = (random.random() * 2 - 1) * 0.4
            sample = env * volume * (0.6 * math.sin(phase) + noise)
            l_gain = 0.5 * (1.0 - pan)
            r_gain = 0.5 * (1.0 + pan)
            add_sample(start_time + t, sample * l_gain, sample * r_gain)

    # Comic impact / hit
    def trigger_impact(start_time, volume=0.85):
        duration = 0.45
        n = int(duration * sample_rate)
        phase = 0.0
        for i in range(n):
            t = i / sample_rate
            freq = 110 * math.exp(-12 * t) + 40
            phase += 2 * math.pi * freq / sample_rate
            env = math.exp(-10 * t)
            snap = math.exp(-60 * t) * (random.random() * 2 - 1) * 0.8
            sample = volume * (env * math.sin(phase) + snap)
            add_sample(start_time + t, sample, sample)

    # Cinematic bass drop for outro
    def trigger_outro_bass(start_time, duration=1.6, volume=0.9):
        n = int(duration * sample_rate)
        phase = 0.0
        for i in range(n):
            t = i / sample_rate
            freq = 80 * math.exp(-2.2 * t) + 32
            phase += 2 * math.pi * freq / sample_rate
            env = (math.sin(math.pi * min(1.0, t / 0.1)) if t < 0.1 else 1.0) * math.exp(-1.8 * t)
            sample = volume * env * math.sin(phase)
            add_sample(start_time + t, sample, sample)

    # Storyboard Cues (Snappy 21s Timeline):
    # 0.0s - 3.4s: Panel 1
    trigger_impact(0.08, volume=0.8)
    trigger_pop(0.4, volume=0.75, pitch_factor=1.0)

    # 3.4s - 7.8s: Panel 2
    trigger_whoosh(3.45, duration=0.32, volume=0.65, pan=0.0)
    trigger_impact(3.75, volume=0.85)
    trigger_pop(4.1, volume=0.85, pitch_factor=1.1)

    # 7.8s - 11.2s: Panel 3 Left
    trigger_whoosh(7.85, duration=0.28, volume=0.55, pan=-0.3)
    trigger_pop(8.4, volume=0.7, pitch_factor=1.15)

    # 11.2s - 14.8s: Panel 3 Right
    trigger_whoosh(11.25, duration=0.3, volume=0.65, pan=0.3)
    trigger_impact(11.55, volume=0.8)
    trigger_pop(11.8, volume=0.75, pitch_factor=1.2)

    # 14.8s - 19.2s: Panel 4
    trigger_whoosh(14.85, duration=0.32, volume=0.6, pan=0.0)
    trigger_pop(15.5, volume=0.8, pitch_factor=0.95)

    # 19.2s - 21.0s: Cinematic Pullback Reveal
    trigger_whoosh(19.25, duration=0.5, volume=0.7)
    trigger_outro_bass(19.4, duration=1.6, volume=0.9)

    # Write WAV file
    with wave.open('comic_audio.wav', 'wb') as wav:
        wav.setnchannels(2)
        wav.setsampwidth(2)
        wav.setframerate(sample_rate)

        max_val = max(max(abs(x) for x in left), max(abs(y) for y in right), 1.0)
        gain = 0.9 / max_val if max_val > 1.0 else 0.85

        frames = bytearray()
        for l, r in zip(left, right):
            sl = max(-32767, min(32767, int(l * gain * 32767)))
            sr = max(-32767, min(32767, int(r * gain * 32767)))
            frames.extend(struct.pack('<hh', sl, sr))
        wav.writeframes(frames)
    print("comic_audio.wav (21s) generated successfully.")

if __name__ == '__main__':
    generate_sfx()
