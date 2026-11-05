#!/usr/bin/env python3
"""Render a PPTX to PNG pages with LibreOffice + pypdfium2 (also used by build_video.py).

Usage: .venv/bin/python render_preview.py docs/Amazon-Quick-介绍.pptx OUT_DIR [--sheets]
--sheets also writes 2x2 contact sheets (sheet-01.png ...) for a quick layout review.
"""
import os
import subprocess
import sys
from pathlib import Path

import pypdfium2 as pdfium
from PIL import Image

ROOT = Path(__file__).resolve().parent
FONTS_CONF = ROOT / "build" / "fonts.conf"
CJK_DIR = Path.home() / ".local" / "browser-libs" / "root" / "usr" / "share" / "fonts"
W, H = 1920, 1080

FONTS_XML = f"""<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>
  <dir>{CJK_DIR}</dir>
  <cachedir>{Path.home() / ".cache" / "fontconfig-browser"}</cachedir>
  <alias binding="same"><family>Microsoft YaHei</family><prefer><family>Noto Sans CJK SC</family></prefer></alias>
  <alias><family>sans-serif</family><prefer><family>Noto Sans CJK SC</family><family>DejaVu Sans</family></prefer></alias>
  <alias><family>Arial</family><prefer><family>DejaVu Sans</family></prefer></alias>
</fontconfig>
"""


def font_env():
    FONTS_CONF.parent.mkdir(parents=True, exist_ok=True)
    FONTS_CONF.write_text(FONTS_XML, encoding="utf-8")
    env = dict(os.environ)
    env["FONTCONFIG_FILE"] = str(FONTS_CONF)
    return env


def to_pdf(pptx: Path, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(pptx)],
                   check=True, env=font_env(), capture_output=True, timeout=900)
    return out_dir / (pptx.stem + ".pdf")


def to_pngs(pdf_path: Path, out_dir: Path, prefix="page"):
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf = pdfium.PdfDocument(str(pdf_path))
    paths = []
    for i in range(len(pdf)):
        page = pdf[i]
        w, _ = page.get_size()
        img = page.render(scale=W / w).to_pil().convert("RGB")
        if img.size != (W, H):
            img = img.resize((W, H), Image.LANCZOS)
        p = out_dir / f"{prefix}-{i + 1:03d}.png"
        img.save(p)
        paths.append(p)
    return paths


def sheets(paths, out_dir: Path):
    for n in range(0, len(paths), 4):
        sheet = Image.new("RGB", (W, H), "white")
        for j, p in enumerate(paths[n:n + 4]):
            im = Image.open(p).resize((W // 2 - 6, H // 2 - 6), Image.LANCZOS)
            sheet.paste(im, ((j % 2) * (W // 2) + 3, (j // 2) * (H // 2) + 3))
        sheet.save(out_dir / f"sheet-{n // 4 + 1:02d}.png")


if __name__ == "__main__":
    src, out = Path(sys.argv[1]), Path(sys.argv[2])
    pngs = to_pngs(to_pdf(src, out), out)
    if "--sheets" in sys.argv:
        sheets(pngs, out)
    print(f"{len(pngs)} pages -> {out}")
