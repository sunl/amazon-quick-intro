#!/usr/bin/env python3
"""Build the narrated walkthrough video from the same slides as the PPTX.

Pipeline (intermediate files under build/video/):
  1. build_deck.build(video=True) writes a deck with one slide per narration step, the element
     being discussed highlighted; LibreOffice renders it to PDF, pypdfium2 to 1920x1080 PNG frames;
  2. Amazon Polly (neural, Zhiyu) speaks the narration sentence by sentence (cached by hash);
  3. sentences are laid out on one timeline -> narration.wav plus .srt / .ass subtitles;
  4. ffmpeg (imageio-ffmpeg) encodes frames + narration, subtitles burned in.

Output: docs/Amazon-Quick-介绍.mp4 and docs/Amazon-Quick-介绍.srt

Usage (from the project root):
  .venv/bin/python build_video.py --profile <aws-profile>          # full build
  .venv/bin/python build_video.py --frames-only                    # render frames only, no TTS
Needs: soffice (LibreOffice), Noto Sans CJK fonts under ~/.local/browser-libs, AWS CLI with
polly:SynthesizeSpeech.
"""
import argparse
import concurrent.futures
import hashlib
import html
import os
import re
import subprocess
import sys
import wave
from pathlib import Path

import build_deck
import render_preview

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build" / "video"
DIST = ROOT / "docs"
OUT_NAME = "Amazon-Quick-介绍"
FPS = 30
SAMPLE_RATE = 24000

# Speech-only rewrites (subtitles keep the original text). Latin keys match whole words only.
TTS_REPLACE = [
    ("aws.com/quick", "aws 点 com 斜杠 quick"), ("S&P Global", "S and P Global"), ("Q&A", "Q and A"),
    ("SKILL.md", "skill 点 MD"), ("Sites.Selected", "Sites 点 Selected"), ("@", "艾特"),
    ("QuickSight", "Quick Sight"), ("OAuth", "O Auth"), ("IAM", "I A M"), ("macOS", "Mac O S"), ("iOS", "i O S"),
    ("CloudWatch", "Cloud Watch"), ("CloudTrail", "Cloud Trail"), ("GovCloud", "Gov Cloud"),
    ("SharePoint", "Share Point"), ("OneDrive", "One Drive"), ("PowerPoint", "Power Point"),
    ("ServiceNow", "Service Now"), ("PagerDuty", "Pager Duty"), ("OpenAPI", "Open API"), ("dLocal", "D Local"),
    ("GoDaddy", "Go Daddy"), ("Tradeshift", "Trade shift"), ("FactSet", "Fact Set"), ("PubMed", "Pub Med"),
    ("SOW", "S O W"), ("RFP", "R F P"), ("RAG", "R A G"), ("SaaS", "sass"), ("AD", "A D"), ("KMS", "K M S"),
    ("SCP", "S C P"), ("SQL", "S Q L"), ("DLP", "D L P"), ("ACL", "A C L"), ("SPICE", "spice"), ("UI", "U I"),
    ("PPT", "P P T"), ("HTTP", "H T T P"), ("MCP", "M C P"), ("BI", "B I"), ("CRM", "C R M"), ("FAQ", "F A Q"),
    ("VPC", "V P C"), ("SAP", "S A P"), ("IDC", "I D C"), ("SDK", "S D K"), ("API", "A P I"), ("PDF", "P D F"),
    ("Kitsa", "Kit sa"), ("Aderant", "Ad er ant"), ("Jabil", "Ja bil"), ("persona", "persona"),
    ("“", ""), ("”", ""),
]


def tts_text(text: str) -> str:
    out = text
    for a, b in TTS_REPLACE:
        if a[0].isascii() and a[0].isalnum():
            out = re.sub(rf"(?<![A-Za-z]){re.escape(a)}(?![A-Za-z])", b, out)
        else:
            out = out.replace(a, b)
    return out


def sentences(text: str):
    parts = re.findall(r"[^。！？；]+[。！？；]?", text)
    return [p.strip() for p in parts if p.strip()]


def cue_chunks(sentence: str, limit=24):
    text = sentence.rstrip("。；！？")
    pieces = re.findall(r"[^，、：,]+[，、：,]?", text) or [text]
    chunks, cur = [], ""
    for p in pieces:
        if cur and build_deck.units(cur) + build_deck.units(p) > limit:
            chunks.append(cur)
            cur = p
        else:
            cur += p
    if cur:
        chunks.append(cur)
    return [c.rstrip("，、：,") for c in chunks]


def ffmpeg_exe():
    import imageio_ffmpeg

    return imageio_ffmpeg.get_ffmpeg_exe()


def synth(text, cache: Path, args):
    spoken = tts_text(text)
    ssml = f"<speak><prosody rate='{args.rate}'>{html.escape(spoken, quote=False)}</prosody></speak>"
    key = hashlib.sha1(f"{args.voice}|neural|{ssml}".encode("utf-8")).hexdigest()
    pcm = cache / f"{key}.pcm"
    if pcm.exists():
        return pcm.read_bytes()
    mp3 = cache / f"{key}.mp3"
    cmd = ["aws", "polly", "synthesize-speech", "--engine", "neural", "--voice-id", args.voice,
           "--output-format", "mp3", "--sample-rate", str(SAMPLE_RATE), "--text-type", "ssml", "--text", ssml,
           "--region", args.region, str(mp3)]
    if args.profile:
        cmd[1:1] = ["--profile", args.profile]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode:
        raise RuntimeError(f"polly failed for {text[:30]}…: {res.stderr.strip()[-300:]}")
    subprocess.run([ffmpeg_exe(), "-y", "-loglevel", "error", "-i", str(mp3), "-f", "s16le", "-ac", "1",
                    "-ar", str(SAMPLE_RATE), str(pcm)], check=True)
    mp3.unlink()
    return pcm.read_bytes()


def silence(seconds):
    return b"\x00\x00" * int(SAMPLE_RATE * seconds)


def fmt_srt(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def fmt_ass(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Noto Sans CJK SC,40,&H00FFFFFF,&H00FFFFFF,&H3030170B,&H3030170B,0,0,0,0,100,100,0,0,3,10,0,2,80,80,16,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def render_frames():
    deck, plan, warns = build_deck.build(video=True, out=BUILD / "video-steps.pptx")
    for w in warns:
        print("  WARN", w)
    frames_dir = BUILD / "frames"
    for old in frames_dir.glob("page-*.png"):
        old.unlink()
    pdf = render_preview.to_pdf(deck, BUILD)
    frames = render_preview.to_pngs(pdf, frames_dir)
    if len(frames) != len(plan):
        raise SystemExit(f"rendered {len(frames)} pages, expected {len(plan)}")
    return list(zip(frames, plan))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", default=os.environ.get("AWS_PROFILE"))
    ap.add_argument("--region", default=os.environ.get("POLLY_REGION", "us-east-1"))
    ap.add_argument("--voice", default="Zhiyu")
    ap.add_argument("--rate", default="110%", help="Polly prosody rate")
    ap.add_argument("--frames-only", action="store_true")
    ap.add_argument("--no-burn", action="store_true", help="do not burn subtitles into the video")
    args = ap.parse_args()

    tts_dir = BUILD / "tts"
    for d in (BUILD, tts_dir, DIST):
        d.mkdir(parents=True, exist_ok=True)
    steps = render_frames()
    print(f"{len(build_deck.content.SLIDES)} slides, {len(steps)} frames")
    if args.frames_only:
        return 0

    all_sentences = sorted({x for _, (_, _, texts, _) in steps for t in texts for x in sentences(t)})
    print(f"synthesising {len(all_sentences)} sentences ({sum(len(x) for x in all_sentences)} characters)")
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        audio = dict(zip(all_sentences, pool.map(lambda x: synth(x, tts_dir, args), all_sentences)))

    pcm, t = bytearray(), 0.0
    frames_list, srt, ass, chapters = [], [], [], []
    cue_no = 0
    for k, (frame, (page, si, texts, kind)) in enumerate(steps):
        start = t
        last_of_slide = k == len(steps) - 1 or steps[k + 1][1][0] != page
        lead = 0.8 if k == 0 else 0.35
        tail = (1.1 if kind in ("cover", "end") else 0.8) if last_of_slide else 0.35
        if si == 0:
            chapters.append((t, page, build_deck.content.SLIDES[page - 1]["title"]))
        pcm += silence(lead)
        t += lead
        for text in texts:
            for sent in sentences(text):
                data = audio[sent]
                dur = len(data) / 2 / SAMPLE_RATE
                chunks = cue_chunks(sent)
                weights = [max(build_deck.units(c), 1) for c in chunks]
                ct = t
                for c, wgt in zip(chunks, weights):
                    cd = dur * wgt / sum(weights)
                    cue_no += 1
                    srt.append(f"{cue_no}\n{fmt_srt(ct)} --> {fmt_srt(ct + cd)}\n{c}\n")
                    ass.append(f"Dialogue: 0,{fmt_ass(ct)},{fmt_ass(ct + cd)},Default,,0,0,0,,{c}")
                    ct += cd
                pcm += data
                t += dur
                pcm += silence(0.22)
                t += 0.22
        pcm += silence(tail)
        t += tail
        frames_list.append((frame, t - start))

    wav = BUILD / "narration.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SAMPLE_RATE)
        w.writeframes(bytes(pcm))
    (DIST / f"{OUT_NAME}.srt").write_text("\n".join(srt), encoding="utf-8")
    ass_path = BUILD / "subtitles.ass"
    ass_path.write_text(ASS_HEAD + "\n".join(ass) + "\n", encoding="utf-8")
    (BUILD / "chapters.txt").write_text(
        "\n".join(f"{int(c // 60):02d}:{int(c % 60):02d}  {p:02d}  {title}" for c, p, title in chapters) + "\n",
        encoding="utf-8")

    concat = BUILD / "frames.txt"
    lines = ["ffconcat version 1.0"]
    for path, dur in frames_list:
        lines += [f"file '{path}'", f"duration {dur:.3f}"]
    lines.append(f"file '{frames_list[-1][0]}'")
    concat.write_text("\n".join(lines) + "\n", encoding="utf-8")

    vf = f"fps={FPS},format=yuv420p"
    if not args.no_burn:
        vf += f",ass={ass_path}:fontsdir={render_preview.CJK_DIR / 'google-noto-cjk'}"
    out = DIST / f"{OUT_NAME}.mp4"
    cmd = [ffmpeg_exe(), "-y", "-loglevel", "error", "-stats", "-f", "concat", "-safe", "0", "-i", str(concat),
           "-i", str(wav), "-vf", vf, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-tune", "stillimage",
           "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-shortest", str(out)]
    print(f"encoding {t / 60:.1f} minutes -> {out}")
    subprocess.run(cmd, check=True, env=render_preview.font_env())
    print(f"done: {out} ({out.stat().st_size / 1e6:.1f} MB, {t / 60:.1f} min), subtitles: {DIST / (OUT_NAME + '.srt')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
