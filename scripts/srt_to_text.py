# -*- coding: utf-8 -*-
"""把 srt 字幕合并成连续可读文本：碎句按标点归并，输出单集 txt 与总 md。"""
import re
import sys
from pathlib import Path

SUBS = Path(r"D:\Desktop\20261105-CMU图形学字幕\subs")
OUT = Path(r"D:\Desktop\20261105-CMU图形学字幕")
TXT_DIR = OUT / "txt"
TXT_DIR.mkdir(exist_ok=True)

TS = re.compile(r"^(\d\d):(\d\d):(\d\d),(\d+)\s*-->\s*(\d\d):(\d\d):(\d\d),(\d+)")

END_PUNCT = "。！？!?…"
SOFT_PUNCT = "，、；：,;:"


def parse_srt(path: Path):
    cues = []
    raw = path.read_text(encoding="utf-8-sig", errors="replace")
    blocks = re.split(r"\r?\n\r?\n+", raw.strip())
    for b in blocks:
        lines = [l.strip() for l in b.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        idx = 0
        m = TS.match(lines[0])
        if not m:
            if len(lines) >= 3:
                m = TS.match(lines[1])
                idx = 1
            if not m:
                continue
        start = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
        text = " ".join(lines[idx + 1:]).strip()
        if text:
            cues.append((start, text))
    return cues


def clean(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)          # 去 html 标签
    text = re.sub(r"\{\\[^}]*\}", "", text)      # 去 ass 标签
    text = text.replace("\u200b", "").strip()
    return text


def merge(cues):
    """把碎句拼成自然段落：遇到句末标点收句，超长再按软标点断。"""
    out, buf = [], ""
    for _, t in cues:
        t = clean(t)
        if not t:
            continue
        if not buf:
            buf = t
        else:
            # 中文直接相连，英文之间补空格
            if re.search(r"[A-Za-z0-9]$", buf) and re.match(r"[A-Za-z0-9]", t):
                buf += " " + t
            else:
                buf += t
        if len(buf) >= 60 and buf[-1] in END_PUNCT:
            out.append(buf)
            buf = ""
        elif len(buf) >= 150:
            # 太长就在最后一个软标点处断开；连标点都没有就硬断，保证段落可读
            cut = max(buf.rfind(c) for c in SOFT_PUNCT)
            if cut > 60:
                out.append(buf[: cut + 1])
                buf = buf[cut + 1:]
            else:
                out.append(buf)
                buf = ""
    if buf:
        out.append(buf)
    # 去重相邻完全相同的句子（AI 字幕常见重复）
    dedup = []
    for s in out:
        if not dedup or s != dedup[-1]:
            dedup.append(s)
    return dedup


def main():
    files = sorted(SUBS.glob("P*.srt"))
    if not files:
        print("没有找到字幕文件", file=sys.stderr)
        return 1
    md = ["# CMU 15-462/662 计算机图形学 · 全课程字幕（中文）", "",
          "> 来源：B站 BV1yVfwBtEot「卡内基梅隆大学【中英⚡计算机图形学|15-462, Computer Graphics】」",
          "> 字幕类型：B站 AI 自动生成中文字幕（原课为英文授课，此为 AI 转写并翻译）",
          "> 共 24 集有字幕；P25「学生作品展示」无旁白字幕。", ""]
    total_cues = 0
    for f in files:
        cues = parse_srt(f)
        total_cues += len(cues)
        paras = merge(cues)
        title = f.stem
        txt = TXT_DIR / f"{title}.txt"
        txt.write_text("\n\n".join(paras) + "\n", encoding="utf-8")
        md.append(f"## {title}")
        md.append("")
        md.extend(paras)
        md.append("")
        print(f"{title}: {len(cues)} 条字幕 -> {len(paras)} 段, {len(''.join(paras))} 字")
    (OUT / "全部字幕-中文纯文本.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\n总字幕条数 {total_cues}，总 md 大小 {(OUT / '全部字幕-中文纯文本.md').stat().st_size / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
