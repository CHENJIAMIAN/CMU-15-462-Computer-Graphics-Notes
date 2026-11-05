# -*- coding: utf-8 -*-
"""校验 24 篇分集总结的完整性，并生成总索引 INDEX.md"""
import re
from pathlib import Path

SUM = Path(r"D:\Desktop\20261105-CMU图形学字幕\summaries")
OUT = Path(r"D:\Desktop\20261105-CMU图形学字幕")

SECTIONS = ["一句话概括", "本集主题与目标", "核心概念", "关键公式", "讲解脉络",
            "重点结论", "字幕含糊", "与前后集的衔接"]

files = sorted(SUM.glob("P*.md"))
print(f"共 {len(files)} 个文件\n")

rows, problems = [], []
for f in files:
    text = f.read_text(encoding="utf-8", errors="replace")
    missing = [s for s in SECTIONS if f"## {s}" not in text and s not in text]
    body = re.sub(r"\s", "", text)
    cn = len(re.findall(r"[\u4e00-\u9fff]", text))
    # 抽取一句话概括
    m = re.search(r"##\s*一句话概括\s*\n+(.+?)(?:\n\s*\n|\n##)", text, re.S)
    brief = re.sub(r"\s+", "", m.group(1))[:160] if m else "（未提取到）"
    rows.append((f.stem, len(text), cn, brief, missing))
    if missing:
        problems.append((f.name, missing))

print(f"{'文件':<38}{'字节':>8}{'汉字':>7}  缺章节")
for name, size, cn, brief, missing in rows:
    print(f"{name:<38}{size:>8,}{cn:>7}  {'、'.join(missing) if missing else '-'}")

if problems:
    print("\n有问题的文件：")
    for n, m in problems:
        print(f"  {n}: 缺 {m}")
else:
    print("\n全部 24 篇章节结构完整。")

# 生成索引
md = ["# CMU 15-462/662 计算机图形学 · 分集总结索引", "",
      f"共 {len(rows)} 篇，每篇对应一集字幕（P25 学生作品展示无字幕，无总结）。", ""]
for name, size, cn, brief, missing in rows:
    md.append(f"## {name}")
    md.append("")
    md.append(brief)
    md.append("")
(OUT / "summaries" / "INDEX.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(f"\n索引已写入 {OUT / 'summaries' / 'INDEX.md'}")
