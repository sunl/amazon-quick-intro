#!/usr/bin/env python3
"""Build the Amazon Quick introduction deck as an editable PPTX.

Slide content, narration and sources live in content.py; this file only lays them out.

Usage (from the project root):
    python3.12 -m venv .venv && .venv/bin/pip install python-pptx==1.0.2 imageio-ffmpeg==0.6.0 pypdfium2
    .venv/bin/python build_deck.py            # -> docs/Amazon-Quick-介绍.pptx (narration in speaker notes)

build_video.py imports this module and calls build(video=True), which emits one slide per
narration step with the element being discussed highlighted.
"""
import datetime
import math
import re
import sys
import unicodedata
from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

import content

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "docs"
OUT = DIST / "Amazon-Quick-介绍.pptx"
FONT = "Microsoft YaHei"

INK = RGBColor(0x0F, 0x17, 0x2A)
INK2 = RGBColor(0x33, 0x41, 0x55)
MUTED = RGBColor(0x64, 0x74, 0x8B)
FAINT = RGBColor(0x94, 0xA3, 0xB8)
LINE = RGBColor(0xE2, 0xE8, 0xF0)
CARD = RGBColor(0xF8, 0xFA, 0xFC)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
ORANGE = RGBColor(0xFF, 0x99, 0x00)
ORANGE_TXT = RGBColor(0xC2, 0x41, 0x0C)
HL_BG = RGBColor(0xFF, 0xF4, 0xE0)
NAVY = RGBColor(0x0B, 0x17, 0x30)
NAVY2 = RGBColor(0x1E, 0x3A, 0x66)
BLUE = RGBColor(0x1D, 0x4E, 0xD8)
BLUE_BG = RGBColor(0xEE, 0xF4, 0xFF)
TEAL = RGBColor(0x0F, 0x76, 0x6E)

SW, SH = 13.333, 7.5
ML = 0.6
CW = SW - 2 * ML
BODY_BOTTOM = 6.36
WARN = []
# LibreOffice (used to render the video frames) adds its own Asian/Latin spacing, so the video
# variant drops the typed space between CJK and Latin text to avoid double gaps.
VIDEO_TEXT = {"on": False}
_CJK_GAP = re.compile(r"(?<=[\u3400-\u9fff\uff00-\uffef\u3000-\u303f]) (?=[A-Za-z0-9$])|(?<=[A-Za-z0-9%)]) (?=[\u3400-\u9fff])")


def vt(text: str) -> str:
    return _CJK_GAP.sub("", text) if VIDEO_TEXT["on"] else text


# ----------------------------------------------------------------------------- text helpers
def units(text: str) -> float:
    """Approximate rendered width in em: CJK/full-width = 1, other = 0.56."""
    return sum(1.0 if unicodedata.east_asian_width(c) in ("W", "F") else 0.56 for c in text)


def est_lines(text: str, width_in: float, pt: float) -> int:
    per_line = max(width_in * 72 / pt, 1)
    return max(1, math.ceil(units(text) / per_line - 0.02))


def check_fit(where, paras, width_in, height_in):
    """paras: [(text, pt, spacing_factor, space_before_pt)] -> warn when the estimate overflows."""
    need = 0.0
    for text, pt, lf, sb in paras:
        need += est_lines(text, width_in, pt) * pt * lf + sb
    need_in = need / 72
    if need_in > height_in + 0.02:
        WARN.append(f"{where}: needs ~{need_in:.2f}in, box is {height_in:.2f}in")
    return need_in


def set_par(p, text, pt, color=INK, bold=False, align=None, lf=1.28, sb=0, link=None, italic=False):
    p.text = ""
    r = p.add_run()
    r.text = vt(text)
    f = r.font
    f.size = Pt(pt)
    f.bold = bold
    f.italic = italic
    f.name = FONT
    f.color.rgb = color
    rpr = r._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        el = rpr.find(qn(tag))
        if el is None:
            el = rpr.makeelement(qn(tag), {})
            rpr.append(el)
        el.set("typeface", FONT)
    if link:
        r.hyperlink.address = link
    p.line_spacing = Pt(round(pt * lf, 1))
    if sb:
        p.space_before = Pt(sb)
    if align is not None:
        p.alignment = align
    return r


def add_run(p, text, pt, color=INK, bold=False, link=None):
    r = p.add_run()
    r.text = vt(text)
    f = r.font
    f.size = Pt(pt)
    f.bold = bold
    f.name = FONT
    f.color.rgb = color
    rpr = r._r.get_or_add_rPr()
    el = rpr.makeelement(qn("a:ea"), {"typeface": FONT})
    rpr.append(el)
    if link:
        r.hyperlink.address = link
    return r


def bulletize(p, indent_in=0.17, char="•"):
    ppr = p._p.get_or_add_pPr()
    ppr.set("marL", str(int(Inches(indent_in))))
    ppr.set("indent", str(-int(Inches(indent_in))))
    for tag in ("a:buNone", "a:buChar", "a:buFont"):
        for el in ppr.findall(qn(tag)):
            ppr.remove(el)
    bf = ppr.makeelement(qn("a:buFont"), {"typeface": "Arial"})
    bc = ppr.makeelement(qn("a:buChar"), {"char": char})
    ppr.append(bf)
    ppr.append(bc)


def textbox(slide, x, y, w, h, anchor=MSO_ANCHOR.TOP, margins=(0, 0, 0, 0)):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    tf.vertical_anchor = anchor
    tf.margin_left, tf.margin_top, tf.margin_right, tf.margin_bottom = (Inches(m) for m in margins)
    return tb, tf


def rect(slide, x, y, w, h, fill=CARD, line=LINE, lw=1.0, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06):
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = radius
    if fill is None:
        s.fill.background()
    else:
        s.fill.solid()
        s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(lw)
    s.shadow.inherit = False
    style = s._element.find(qn("p:style"))
    if style is not None:  # drop the theme style so no renderer adds its shadow or font colour
        s._element.remove(style)
    s.text_frame.text = ""
    return s


def line(slide, x1, y1, x2, y2, color=LINE, lw=1.5):
    c = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y1), Inches(x2), Inches(y2))
    c.line.color.rgb = color
    c.line.width = Pt(lw)
    return c


def is_on(key, hl):
    return hl is not None and key is not None and key in hl


def card_box(slide, x, y, w, h, key, hl, fill=CARD):
    on = is_on(key, hl)
    return rect(slide, x, y, w, h, fill=HL_BG if on else fill, line=ORANGE if on else LINE, lw=2.5 if on else 1.0)


# ----------------------------------------------------------------------------- chrome
def chrome(slide, s, page, total):
    _, tf = textbox(slide, ML, 0.3, 7.0, 0.3)
    set_par(tf.paragraphs[0], s.get("section", ""), 11, ORANGE_TXT, bold=True)
    _, tf = textbox(slide, SW - ML - 4.0, 0.3, 4.0, 0.3)
    set_par(tf.paragraphs[0], f"Amazon Quick 介绍  ·  {page:02d} / {total:02d}", 10, FAINT, align=PP_ALIGN.RIGHT)
    _, tf = textbox(slide, ML, 0.56, CW, 0.66, anchor=MSO_ANCHOR.MIDDLE)
    set_par(tf.paragraphs[0], s["title"], 26, INK, bold=True, lf=1.15)
    check_fit(f"p{page} title", [(s["title"], 26, 1.15, 0)], CW, 0.66)
    rect(slide, ML, 1.25, 0.72, 0.06, fill=ORANGE, line=None, shape=MSO_SHAPE.RECTANGLE)
    top = 1.5
    if s.get("lead"):
        _, tf = textbox(slide, ML, 1.38, CW, 0.5)
        set_par(tf.paragraphs[0], s["lead"], 14, INK2, lf=1.3)
        check_fit(f"p{page} lead", [(s["lead"], 14, 1.3, 0)], CW, 0.5)
        top = 1.98
    src = s.get("src") or []
    if src:
        _, tf = textbox(slide, ML, 6.45, CW, 0.52)
        p = tf.paragraphs[0]
        set_par(p, "来源：", 9, MUTED, lf=1.35)
        wn_done = False
        parts = []
        for i, k in enumerate(src):
            label, url = content.SRC[k]
            if i:
                add_run(p, "  ·  ", 9, FAINT)
            if label.startswith("What's New "):  # print the "What's New" prefix once per footer
                label = label[len("What's New "):]
                if not wn_done:
                    add_run(p, "What's New ", 9, MUTED)
                    wn_done = True
            add_run(p, label, 9, BLUE, link=url)
            parts.append(label)
        txt = "来源：What's New " + "  ·  ".join(parts)
        check_fit(f"p{page} sources", [(txt, 9, 1.35, 0)], CW, 0.52)
    if VIDEO_TEXT["on"]:  # the video burns subtitles into this band
        return top
    _, tf = textbox(slide, ML, 7.04, CW, 0.3)
    set_par(tf.paragraphs[0], content.FOOTER, 8.5, FAINT)
    return top


# ----------------------------------------------------------------------------- body layouts
def note_bar(slide, s, x, y, w, h, hl):
    n = s["note"]
    key = n.get("key", "note")
    on = is_on(key, hl)
    box = rect(slide, x, y, w, h, fill=HL_BG if on else BLUE_BG, line=ORANGE if on else None, lw=2.0,
               radius=0.12)
    rect(slide, x, y, 0.09, h, fill=ORANGE if on else BLUE, line=None, shape=MSO_SHAPE.RECTANGLE)
    _, tf = textbox(slide, x + 0.25, y, w - 0.4, h, anchor=MSO_ANCHOR.MIDDLE)
    p = tf.paragraphs[0]
    if n.get("label"):
        set_par(p, n["label"] + "  ", 14.5, ORANGE_TXT if on else BLUE, bold=True, lf=1.3)
        add_run(p, n["text"], 14.5, INK)
    else:
        set_par(p, n["text"], 14.5, INK, lf=1.3)
    check_fit(f"note '{n['text'][:12]}'", [((n.get("label", "") + "  " + n["text"]), 14.5, 1.3, 0)], w - 0.4, h)
    return box


def body_area(s, top):
    bottom = BODY_BOTTOM
    note_h = s.get("note", {}).get("h", 0.62) if s.get("note") else 0
    if note_h:
        bottom -= note_h + 0.18
    return top, bottom, note_h


def card_text(slide, c, x, y, w, h, where, title_pt=17.5, body_pt=14.5, pad=0.18):
    _, tf = textbox(slide, x + pad, y + pad * 0.85, w - 2 * pad, h - 1.6 * pad)
    paras = []
    p = tf.paragraphs[0]
    first = True
    if c.get("tag"):
        set_par(p, c["tag"], 12, ORANGE_TXT, bold=True, lf=1.3)
        paras.append((c["tag"], 12, 1.3, 0))
        first = False
    if c.get("title"):
        if not first:
            p = tf.add_paragraph()
        set_par(p, c["title"], title_pt, INK, bold=True, lf=1.25, sb=0 if first else 1)
        paras.append((c["title"], title_pt, 1.25, 0 if first else 1))
        first = False
    if c.get("text"):
        if not first:
            p = tf.add_paragraph()
        set_par(p, c["text"], body_pt, INK2, lf=1.36, sb=0 if first else 4)
        paras.append((c["text"], body_pt, 1.36, 0 if first else 4))
        first = False
    for b in c.get("bullets", []):
        if not first:
            p = tf.add_paragraph()
        set_par(p, b, body_pt, INK2, lf=1.34, sb=0 if first else 3.5)
        bulletize(p)
        paras.append((b, body_pt, 1.34, 0 if first else 3.5))
        first = False
    check_fit(where, paras, w - 2 * pad - 0.17, h - 1.6 * pad)


def render_cards(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    cards = s["cards"]
    cols = s.get("cols", min(len(cards), 3))
    rows = math.ceil(len(cards) / cols)
    gap = s.get("gap", 0.22)
    cw = (CW - gap * (cols - 1)) / cols
    ch = (bottom - top - gap * (rows - 1)) / rows
    for i, c in enumerate(cards):
        r, k = divmod(i, cols)
        x = ML + k * (cw + gap)
        y = top + r * (ch + gap)
        span = c.get("span", 1)
        w = cw * span + gap * (span - 1)
        card_box(slide, x, y, w, ch, c.get("key"), hl)
        if c.get("num"):
            on = is_on(c.get("key"), hl)
            b = rect(slide, x + 0.16, y + 0.16, 0.42, 0.42, fill=ORANGE if on else NAVY, line=None,
                     shape=MSO_SHAPE.OVAL)
            tf = b.text_frame
            tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            set_par(tf.paragraphs[0], str(c["num"]), 13, INK if on else WHITE, bold=True, align=PP_ALIGN.CENTER,
                    lf=1.0)
            cc = dict(c)
            card_text(slide, {"title": cc.pop("title", "")}, x + 0.5, y, w - 0.5, 0.75, f"p{page} card{i} title",
                      title_pt=s.get("title_pt", 17.5))
            rest = {k2: v for k2, v in c.items() if k2 in ("text", "bullets")}
            card_text(slide, rest, x, y + 0.62, w, ch - 0.62, f"p{page} card{i}", body_pt=s.get("body_pt", 14.5))
        else:
            card_text(slide, c, x, y, w, ch, f"p{page} card{i}", title_pt=s.get("title_pt", 17.5),
                      body_pt=s.get("body_pt", 14.5))
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_table(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    head, rows = s["head"], s["rows"]
    widths = s["widths"]
    scale = CW / sum(widths)
    widths = [w * scale for w in widths]
    pt = s.get("pt", 13.5)
    hpt = s.get("hpt", 14)
    nrow = len(rows) + 1
    gt = slide.shapes.add_table(nrow, len(head), Inches(ML), Inches(top), Inches(CW), Inches(0.4))
    tbl = gt.table
    tbl.first_row = True
    tblpr = gt._element.graphic.graphicData.tbl.tblPr
    style = tblpr.find(qn("a:tableStyleId"))
    if style is None:
        style = tblpr.makeelement(qn("a:tableStyleId"), {})
        tblpr.append(style)
    style.text = "{5940675A-B579-460E-94D1-54222C63F5DA}"  # "No Style, Table Grid"
    for j, w in enumerate(widths):
        tbl.columns[j].width = Inches(w)
    est_total = 0.0
    margin = 0.09

    def fill_cell(cell, text, size, color, bold, bg):
        cell.margin_left = cell.margin_right = Inches(margin)
        cell.margin_top = Inches(0.05)
        cell.margin_bottom = Inches(0.05)
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
        cell.fill.solid()
        cell.fill.fore_color.rgb = bg
        parts = text.split("\n")
        tf = cell.text_frame
        tf.word_wrap = True
        for pi, part in enumerate(parts):
            p = tf.paragraphs[0] if pi == 0 else tf.add_paragraph()
            set_par(p, part, size, color, bold=bold, lf=1.3)

    for j, h in enumerate(head):
        fill_cell(tbl.cell(0, j), h, hpt, WHITE, True, NAVY)
    hh = max(sum(est_lines(x, widths[j] - 2 * margin, hpt) for x in h.split("\n")) for j, h in enumerate(head))
    tbl.rows[0].height = Inches(hh * hpt * 1.3 / 72 + 0.12)
    est_total += hh * hpt * 1.3 / 72 + 0.12
    row_h = []
    for i, row in enumerate(rows, 1):
        key = s.get("row_keys", [None] * len(rows))[i - 1] or f"r{i}"
        on = is_on(key, hl)
        bg = HL_BG if on else (WHITE if i % 2 else CARD)
        lines_max = 1
        for j, txt in enumerate(row):
            first_col = j == 0
            fill_cell(tbl.cell(i, j), txt, pt, INK if first_col else INK2, first_col and s.get("bold_first", True), bg)
            n = sum(est_lines(x, widths[j] - 2 * margin, pt) for x in txt.split("\n"))
            lines_max = max(lines_max, n)
        row_h.append(lines_max * pt * 1.3 / 72 + 0.16)
    head_h = hh * hpt * 1.3 / 72 + 0.12
    est_total += sum(row_h)
    if est_total > bottom - top + 0.02:
        WARN.append(f"p{page} table: needs ~{est_total:.2f}in, area {bottom - top:.2f}in")
    # stretch body rows to use the available height (at most 1.6x), so short tables do not leave a gap
    grow = max(1.0, min(1.6, (bottom - top - head_h) / max(sum(row_h), 0.01)))
    row_h = [h * grow for h in row_h]
    for i, h in enumerate(row_h, 1):
        tbl.rows[i].height = Inches(h)
    if hl:
        # orange marker left of highlighted rows
        y = top + head_h
        for i, rh in enumerate(row_h, 1):
            key = s.get("row_keys", [None] * len(rows))[i - 1] or f"r{i}"
            if is_on(key, hl):
                rect(slide, ML - 0.12, y, 0.07, rh, fill=ORANGE, line=None, shape=MSO_SHAPE.RECTANGLE)
            y += rh
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_timeline(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    items = s["items"]
    n = len(items)
    mid = top + (bottom - top) / 2
    line(slide, ML, mid, ML + CW, mid, color=FAINT, lw=2)
    step = CW / n
    bw = min(step * 2 - 0.3, 2.5)
    for i, it in enumerate(items):
        cx = ML + step * (i + 0.5)
        key = it.get("key", f"t{i + 1}")
        on = is_on(key, hl)
        d = 0.24 if on else 0.18
        rect(slide, cx - d / 2, mid - d / 2, d, d, fill=ORANGE if on else NAVY, line=WHITE, lw=1.5,
             shape=MSO_SHAPE.OVAL)
        above = i % 2 == 0
        h = (bottom - top) / 2 - 0.22
        y = top if above else mid + 0.22
        line(slide, cx, mid - 0.22 if above else mid + 0.12, cx, mid - 0.12 if above else mid + 0.22,
             color=ORANGE if on else FAINT, lw=1.5)
        x = max(ML, min(cx - bw / 2, ML + CW - bw))
        if on:
            rect(slide, x - 0.04, y - 0.04, bw + 0.08, h + 0.08, fill=HL_BG, line=ORANGE, lw=2.0)
        _, tf = textbox(slide, x + 0.06, y + 0.02, bw - 0.12, h - 0.04,
                        anchor=MSO_ANCHOR.BOTTOM if above else MSO_ANCHOR.TOP)
        p = tf.paragraphs[0]
        set_par(p, it["date"], 14, ORANGE_TXT, bold=True, align=PP_ALIGN.CENTER, lf=1.25)
        p = tf.add_paragraph()
        set_par(p, it["title"], 16.5, INK, bold=True, align=PP_ALIGN.CENTER, lf=1.25, sb=2)
        paras = [(it["date"], 14, 1.25, 0), (it["title"], 16.5, 1.25, 2)]
        if it.get("text"):
            p = tf.add_paragraph()
            set_par(p, it["text"], 13.5, INK2, align=PP_ALIGN.CENTER, lf=1.32, sb=3)
            paras.append((it["text"], 13.5, 1.32, 3))
        check_fit(f"p{page} timeline{i}", paras, bw - 0.12, h - 0.04)
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_layers(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    layers = s["layers"]
    n = len(layers)
    gap = 0.14
    h = (bottom - top - gap * (n - 1)) / n
    lw_ = s.get("label_w", 2.55)
    for i, L in enumerate(layers):
        y = top + i * (h + gap)
        key = L.get("key", f"l{i + 1}")
        on = is_on(key, hl)
        rect(slide, ML, y, lw_, h, fill=ORANGE if on else NAVY, line=None, radius=0.1)
        _, tf = textbox(slide, ML + 0.15, y, lw_ - 0.3, h, anchor=MSO_ANCHOR.MIDDLE)
        set_par(tf.paragraphs[0], L["label"], 17, INK if on else WHITE, bold=True, lf=1.2)
        if L.get("sub"):
            p = tf.add_paragraph()
            set_par(p, L["sub"], 12, INK if on else RGBColor(0xCB, 0xD5, 0xE1), lf=1.25, sb=2)
        check_fit(f"p{page} layer{i} label", [(L["label"], 17, 1.2, 0), (L.get("sub", ""), 12, 1.25, 2)],
                  lw_ - 0.3, h)
        x0 = ML + lw_ + 0.16
        avail = CW - lw_ - 0.16
        chips = L["chips"]
        cgap = 0.12
        cwid = (avail - cgap * (len(chips) - 1)) / len(chips)
        for j, c in enumerate(chips):
            x = x0 + j * (cwid + cgap)
            rect(slide, x, y, cwid, h, fill=HL_BG if on else CARD, line=ORANGE if on else LINE,
                 lw=1.8 if on else 1.0, radius=0.1)
            title, _, sub = c.partition("|")
            _, tf = textbox(slide, x + 0.1, y, cwid - 0.2, h, anchor=MSO_ANCHOR.MIDDLE)
            set_par(tf.paragraphs[0], title, 15, INK, bold=True, align=PP_ALIGN.CENTER, lf=1.2)
            paras = [(title, 15, 1.2, 0)]
            if sub:
                p = tf.add_paragraph()
                set_par(p, sub, 12.5, INK2, align=PP_ALIGN.CENTER, lf=1.25, sb=2)
                paras.append((sub, 12.5, 1.25, 2))
            check_fit(f"p{page} layer{i} chip{j}", paras, cwid - 0.2, h)
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_flow(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    steps = s["steps"]
    n = len(steps)
    arrow = 0.34
    w = (CW - arrow * (n - 1)) / n
    h = s.get("flow_h", bottom - top)
    y = top
    for i, st in enumerate(steps):
        x = ML + i * (w + arrow)
        key = st.get("key", f"s{i + 1}")
        on = is_on(key, hl)
        card_box(slide, x, y, w, h, key, hl)
        b = rect(slide, x + 0.16, y + 0.18, 0.46, 0.46, fill=ORANGE if on else NAVY, line=None, shape=MSO_SHAPE.OVAL)
        tf = b.text_frame
        tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        set_par(tf.paragraphs[0], str(i + 1), 14, INK if on else WHITE, bold=True, align=PP_ALIGN.CENTER, lf=1.0)
        _, tf = textbox(slide, x + 0.7, y + 0.12, w - 0.82, 0.6, anchor=MSO_ANCHOR.MIDDLE)
        set_par(tf.paragraphs[0], st["title"], s.get("title_pt", 17.5), INK, bold=True, lf=1.2)
        check_fit(f"p{page} flow{i} title", [(st["title"], s.get("title_pt", 17.5), 1.2, 0)], w - 0.82, 0.6)
        card_text(slide, {k: v for k, v in st.items() if k in ("text", "bullets", "tag")}, x, y + 0.72, w,
                  h - 0.72, f"p{page} flow{i}", body_pt=s.get("body_pt", 14.5))
        if i < n - 1:
            a = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x + w + 0.06), Inches(y + h / 2 - 0.13),
                                       Inches(arrow - 0.12), Inches(0.26))
            a.fill.solid()
            a.fill.fore_color.rgb = FAINT
            a.line.fill.background()
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_quotes(slide, s, top, hl, page):
    top, bottom, note_h = body_area(s, top)
    qs = s["quotes"]
    cols = s.get("cols", 2)
    rows = math.ceil(len(qs) / cols)
    gap = 0.22
    cw = (CW - gap * (cols - 1)) / cols
    ch = (bottom - top - gap * (rows - 1)) / rows
    for i, q in enumerate(qs):
        r, k = divmod(i, cols)
        x = ML + k * (cw + gap)
        y = top + r * (ch + gap)
        key = q.get("key", f"q{i + 1}")
        on = is_on(key, hl)
        card_box(slide, x, y, cw, ch, key, hl, fill=WHITE)
        rect(slide, x, y, 0.08, ch, fill=ORANGE if on else TEAL, line=None, shape=MSO_SHAPE.RECTANGLE)
        _, tf = textbox(slide, x + 0.3, y + 0.16, cw - 0.5, ch - 0.3)
        p = tf.paragraphs[0]
        set_par(p, q["company"], 19, INK, bold=True, lf=1.25)
        p = tf.add_paragraph()
        set_par(p, q["who"], 12.5, MUTED, lf=1.3, sb=1)
        p = tf.add_paragraph()
        set_par(p, "“" + q["quote"] + "”", 15, INK2, lf=1.38, sb=6)
        paras = [(q["company"], 19, 1.25, 0), (q["who"], 12.5, 1.3, 1), (q["quote"] + "“”", 15, 1.38, 6)]
        if q.get("use"):
            p = tf.add_paragraph()
            set_par(p, q["use"], 13, TEAL, bold=True, lf=1.3, sb=8)
            paras.append((q["use"], 13, 1.3, 8))
        check_fit(f"p{page} quote{i}", paras, cw - 0.5, ch - 0.3)
    if note_h:
        note_bar(slide, s, ML, bottom + 0.18, CW, note_h, hl)


def render_refs(slide, s, top, hl, page):
    keys = s["refs"]
    cols = 2
    per = math.ceil(len(keys) / cols)
    cw = (CW - 0.4) / cols
    for c in range(cols):
        _, tf = textbox(slide, ML + c * (cw + 0.4), top, cw, BODY_BOTTOM - top + 0.4)
        first = True
        for k in keys[c * per:(c + 1) * per]:
            label, url = content.SRC[k]
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            set_par(p, label, s.get("pt", 10), BLUE, link=url, lf=1.3, sb=0 if first else 2.5)
            bulletize(p, 0.14)
            first = False


def render_cover(slide, s, page, total, hl):
    bg = rect(slide, 0, 0, SW, SH, fill=NAVY, line=None, shape=MSO_SHAPE.RECTANGLE)
    glow = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(7.6), Inches(-2.6), Inches(8.5), Inches(8.5))
    glow.fill.solid()
    glow.fill.fore_color.rgb = NAVY2
    glow.line.fill.background()
    rect(slide, ML + 0.02, 2.05, 0.9, 0.08, fill=ORANGE, line=None, shape=MSO_SHAPE.RECTANGLE)
    _, tf = textbox(slide, ML, 2.3, 11.5, 1.2)
    set_par(tf.paragraphs[0], s["title"], 44, WHITE, bold=True, lf=1.15)
    _, tf = textbox(slide, ML, 3.5, 11.5, 1.0)
    set_par(tf.paragraphs[0], s["subtitle"], 22, RGBColor(0xE2, 0xE8, 0xF0), lf=1.35)
    _, tf = textbox(slide, ML, 4.75, 11.5, 1.0)
    p = tf.paragraphs[0]
    for i, ln in enumerate(s.get("meta", [])):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        set_par(p, ln, 14, RGBColor(0xCB, 0xD5, 0xE1), lf=1.5)
    if VIDEO_TEXT["on"]:  # the video burns subtitles into this band
        return
    _, tf = textbox(slide, ML, 7.04, CW, 0.3)
    set_par(tf.paragraphs[0], content.FOOTER, 8.5, RGBColor(0x94, 0xA3, 0xB8))


def render_end(slide, s, page, total, hl):
    rect(slide, 0, 0, SW, SH, fill=NAVY, line=None, shape=MSO_SHAPE.RECTANGLE)
    rect(slide, ML + 0.02, 1.0, 0.9, 0.08, fill=ORANGE, line=None, shape=MSO_SHAPE.RECTANGLE)
    _, tf = textbox(slide, ML, 1.25, 11.5, 0.9)
    set_par(tf.paragraphs[0], s["title"], 34, WHITE, bold=True)
    items = s["items"]
    y = 2.4
    for i, it in enumerate(items):
        key = it.get("key", f"e{i + 1}")
        on = is_on(key, hl)
        rect(slide, ML, y, CW, 0.78, fill=RGBColor(0x2A, 0x3D, 0x5E) if on else RGBColor(0x14, 0x24, 0x44),
             line=ORANGE if on else None, lw=2.0, radius=0.12)
        _, tf = textbox(slide, ML + 0.3, y, CW - 0.6, 0.78, anchor=MSO_ANCHOR.MIDDLE)
        p = tf.paragraphs[0]
        set_par(p, it["title"] + "  ", 20, ORANGE, bold=True, lf=1.3)
        add_run(p, it["text"], 17, RGBColor(0xE2, 0xE8, 0xF0))
        check_fit(f"p{page} end{i}", [(it["title"] + "  " + it["text"], 17.5, 1.3, 0)], CW - 0.6, 0.78)
        y += 0.92
    if VIDEO_TEXT["on"]:  # the video burns subtitles into this band
        return
    _, tf = textbox(slide, ML, 7.04, CW, 0.3)
    set_par(tf.paragraphs[0], content.FOOTER, 8.5, RGBColor(0x94, 0xA3, 0xB8))


BODY = {"cards": render_cards, "table": render_table, "timeline": render_timeline, "layers": render_layers,
        "flow": render_flow, "quotes": render_quotes, "refs": render_refs}
FULL = {"cover": render_cover, "end": render_end}


# ----------------------------------------------------------------------------- build
def steps_of(s):
    """Group consecutive narration segments by highlight key -> [(hl_set_or_None, [text, ...])]."""
    out = []
    for seg in s["say"]:
        key, text = (seg if isinstance(seg, tuple) else (None, seg))
        hl = None if key is None else frozenset(key.split(","))
        if out and out[-1][0] == hl:
            out[-1][1].append(text)
        else:
            out.append((hl, [text]))
    return out


def narration(s):
    return "\n\n".join(seg[1] if isinstance(seg, tuple) else seg for seg in s["say"])


def add_slide(prs, s, page, total, hl):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    kind = s["kind"]
    if kind in FULL:
        FULL[kind](slide, s, page, total, hl)
    else:
        top = chrome(slide, s, page, total)
        BODY[kind](slide, s, top, hl, page)
    return slide


def build(video=False, out=None):
    WARN.clear()
    VIDEO_TEXT["on"] = video
    prs = Presentation()
    prs.slide_width = Emu(int(Inches(SW)))
    prs.slide_height = Emu(int(Inches(SH)))
    # replace the python-pptx template's metadata (author name, 2013 dates)
    cp = prs.core_properties
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0, tzinfo=None)
    cp.title, cp.subject = "Amazon Quick 介绍", "主要功能、应用场景与最佳实践"
    cp.author = cp.last_modified_by = "sunl"
    cp.comments = ""
    cp.created = cp.modified = now
    cp.revision = 1
    slides = content.SLIDES
    total = len(slides)
    plan = []
    for page, s in enumerate(slides, 1):
        if video:
            for si, (hl, texts) in enumerate(steps_of(s)):
                add_slide(prs, s, page, total, hl)
                plan.append((page, si, texts, s["kind"]))
        else:
            slide = add_slide(prs, s, page, total, None)
            slide.notes_slide.notes_text_frame.text = narration(s)
    out = out or OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(out)
    return out, plan, list(WARN)


def main():
    out, _, warns = build()
    chars = sum(len(narration(s)) for s in content.SLIDES)
    print(f"wrote {out} ({len(content.SLIDES)} slides, narration {chars} chars)")
    for w in warns:
        print("  WARN", w)
    return 1 if warns and "--strict" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
