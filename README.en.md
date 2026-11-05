# CMU 15-462/662 Computer Graphics · Chinese Study Notes

**简体中文** | [English](README.en.md)

This repository turns CMU 15-462/662 *Computer Graphics* (all 24 lectures) into Chinese study material that you can read directly or feed to an LLM: **per-lecture subtitles + per-lecture summaries + the conversion scripts**.

- Original course: [15462.courses.cs.cmu.edu](http://15462.courses.cs.cmu.edu/) (CMU 15-462/662, Computer Graphics, taught by Keenan Crane)
- Chinese video source: [Bilibili BV1yVfwBtEot](https://www.bilibili.com/video/BV1yVfwBtEot)

> **Upfront disclaimer**: this repository contains **no** course videos, slides, or assignments. It only has subtitles extracted from the Chinese video and Chinese summaries written on top of them. Copyright in the original course belongs to CMU and its authors — see [Copyright and Scope](#copyright-and-scope).

---

## What's inside

| Directory | Content | Good for |
|---|---|---|
| [`summaries/`](summaries/) | **24 detailed per-lecture summaries** (≈2,200–4,200 Chinese characters each) + `INDEX.md` | Quickly grasping the flow, key concepts and formulas of a lecture |
| [`txt/`](txt/) | 24 plain-text transcripts, fragmented cues merged into paragraphs | Full-text search, asking an LLM questions |
| [`subs/`](subs/) | 24 SRT subtitle files with timestamps | Playing alongside a video player |
| [`全部字幕-中文纯文本.md`](全部字幕-中文纯文本.md) | All 24 lectures combined (~1 MB) | One-shot full-text search |
| [`scripts/`](scripts/) | Fetch → merge → verify pipeline | Reproducing the work, or reusing it on another course |

Every summary follows the same 8-section structure:

```
One-line summary / Topic & goal / Key concepts / Key formulas·algorithms·data structures
Lecture flow / Key takeaways / Ambiguous or possibly wrong subtitles / Links to neighbouring lectures
```

The **"Ambiguous or possibly wrong subtitles"** section turned out to be unexpectedly valuable — the AI-generated subtitles contain many mistranslations, and each summary lists the obvious ones with corrections:

| Subtitle as-is | Should be |
|---|---|
| 德尔斯利 / 亲爱的施莱 (P24) | Dirichlet |
| 氖 (P24) | Neumann |
| SweetSparse (P24) | SuiteSparse |
| 反根函数 (P20) | radical inverse |
| 柯尔莫哥洛夫定理 (P20) | Koksma–Hlawka |
| 豌豆 (P20) | PDF |
| 访问权限 (P20) | axis-aligned |
| 区域光圈 (P20) | zone plate |

---

## Lecture list

| P | Title | Duration |
|---|---|---|
| P01 | Welcome | 5 min |
| P02 | Course Overview | 64 min |
| P03 | Linear Algebra Review | 103 min |
| P04 | Vector Calculus Review | 90 min |
| P05 | Drawing Triangles & Sampling | 70 min |
| P06 | Spatial Transformations | 79 min |
| P07 | 3D Rotations & Complex Numbers | 61 min |
| P08 | Perspective Projection & Texture Mapping | 90 min |
| P09 | Depth & Transparency | 53 min |
| P10 | Introduction to Geometry | 75 min |
| P11 | Meshes & Manifolds | 68 min |
| P12 | Digital Geometry Processing | 79 min |
| P13 | Geometric Queries | 70 min |
| P14 | Spatial Data Structures | 82 min |
| P15 | Color | 81 min |
| P16 | Radiometry | 67 min |
| P17 | The Rendering Equation | 46 min |
| P18 | Numerical Integration | 58 min |
| P19 | Monte Carlo Rendering | 76 min |
| P20 | Variance Reduction | 94 min |
| P21 | Introduction to Animation | 69 min |
| P22 | Dynamics & Time Integration | 100 min |
| P23 | Optimization | 96 min |
| P24 | Physically-Based Animation & PDEs | 71 min |
| P25 | Student Showcase (no narration, no subtitles) | 8 min |

Three main blocks: **rasterization & transforms (P05–P09) → geometry (P10–P14) → rendering & animation (P15–P24)**; P03/P04 are math prerequisites.

---

## Quality caveats (read first)

1. **Chinese only, no English original.** The Bilibili compilation has no CC track, only an AI-generated Chinese track (`ai-zh`). The English subtitles live on the original YouTube video, which was not reachable during extraction.
2. **AI subtitles are always imperfect.** Misheard words, inconsistent terminology, and garbled formula dictation are common. Verify against the video before quoting.
3. **Coverage verified.** All 24 subtitle tracks reach the end of their video (99.7%–100%); nothing is truncated.
4. **P25 has no subtitles.** It is a student showcase, visuals only.

---

## Reproducing

Requirements: `yt-dlp` and a logged-in Bilibili cookie (the subtitle API needs `SESSDATA`; anonymously you only get danmaku).

```powershell
# 1. Fetch subtitles (raw SRT)
yt-dlp --cookies cookies.txt --skip-download --write-subs `
  --sub-langs "ai-zh" --convert-subs srt `
  -o "subs/P%(playlist_index)02d - %(title)s.%(ext)s" `
  "https://www.bilibili.com/video/BV1yVfwBtEot"

# 2. SRT -> merged paragraphs + combined markdown
python scripts/srt_to_text.py

# 3. Verify summary completeness + build the index
python scripts/check_summaries.py
```

`cookies.txt` uses the Netscape cookie file format; a `Cookie:` header exported from a browser converts directly (see [`scripts/`](scripts/)).

---

## Copyright and Scope

- **Copyright in the original course belongs to Carnegie Mellon University and Professor Keenan Crane.** Course videos, slides, and assignments are **not** included here — get them from the [official course site](http://15462.courses.cs.cmu.edu/).
- The **subtitle text** derives from Bilibili's AI-generated captions and is a derivative of the original course content. The **per-lecture summaries** and **scripts** are new work created for study purposes and are released under the MIT License.
- This repository is for **personal study and teaching reference only**. No commercial use, and no redistribution of original course content.
- If any rights holder objects to this repository, the affected content will be removed immediately on request.

## Related

- Course website: <http://15462.courses.cs.cmu.edu/>
- Keenan Crane's homepage: <https://www.cs.cmu.edu/~kmcrane/>
- Scotty3D course framework: <https://github.com/CMU-Graphics/Scotty3D>
