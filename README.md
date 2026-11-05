# CMU 15-462/662 计算机图形学 · 中文学习资料

[English](README.en.md) | **简体中文**

把 CMU 15-462/662《Computer Graphics》整门课（24 讲）整理成可以直接读、可以直接喂给 AI 的中文材料：**逐讲字幕 + 逐讲总结 + 转换脚本**。

- 原课程：[15462.courses.cs.cmu.edu](http://15462.courses.cs.cmu.edu/)（CMU 15-462/662, Computer Graphics，Keenan Crane 主讲）
- 中文视频：[B站 BV1yVfwBtEot](https://www.bilibili.com/video/BV1yVfwBtEot)（UP 主：常青藤中英字幕课程）

> **先说清楚**：本仓库**不含**原课视频、课件、作业。只有从中文视频提取的字幕、以及对字幕的中文总结。原课程的著作权归 CMU 及原作者，详见 [版权说明](#版权与使用边界)。

---

## 这里有什么

| 目录 | 内容 | 适合做什么 |
|---|---|---|
| [`summaries/`](summaries/) | **24 篇分集详细总结**（每篇约 2,200–4,200 汉字）+ `INDEX.md` 总索引 | 想快速了解某一讲的脉络、核心概念、公式 |
| [`txt/`](txt/) | 24 篇纯文本字幕，碎句已合并成段落 | 全文检索、丢给 LLM 做问答 |
| [`subs/`](subs/) | 24 个 SRT 字幕，带时间轴 | 挂播放器看、做双语对照 |
| [`全部字幕-中文纯文本.md`](全部字幕-中文纯文本.md) | 24 讲合并版（约 1 MB） | 一次性全文搜索 |
| [`scripts/`](scripts/) | 字幕抓取→合并→校验的脚本 | 复现、或拿去处理别的 B站课程 |

每篇总结固定 8 个章节：

```
一句话概括 / 本集主题与目标 / 核心概念 / 关键公式·算法·数据结构
讲解脉络 / 重点结论 / 字幕含糊或可能有误处 / 与前后集的衔接
```

其中「**字幕含糊或可能有误处**」是这套材料的意外收获——AI 字幕错译不少，各篇都把明显的识别错误挑出来并给了纠正，比如：

| 字幕原文 | 实际应为 |
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

## 课程目录

| P | 标题 | 时长 |
|---|---|---|
| P01 | 欢迎视频 | 5 min |
| P02 | 课程概述 | 64 min |
| P03 | 线性代数（预）复习 | 103 min |
| P04 | 向量微积分（预）复习 | 90 min |
| P05 | 绘制三角形与采样简介 | 70 min |
| P06 | 空间变换 | 79 min |
| P07 | 三维旋转与复数表示 | 61 min |
| P08 | 透视投影与纹理映射 | 90 min |
| P09 | 深度与透明度 | 53 min |
| P10 | 几何学导论 | 75 min |
| P11 | 网格与流形 | 68 min |
| P12 | 数字几何处理 | 79 min |
| P13 | 几何查询 | 70 min |
| P14 | 空间数据结构 | 82 min |
| P15 | 颜色 | 81 min |
| P16 | 辐射度量学 | 67 min |
| P17 | 渲染方程 | 46 min |
| P18 | 数值积分 | 58 min |
| P19 | 蒙特卡洛渲染 | 76 min |
| P20 | 方差缩减 | 94 min |
| P21 | 动画导论 | 69 min |
| P22 | 动力学与时间积分 | 100 min |
| P23 | 优化 | 96 min |
| P24 | 基于物理的动画与偏微分方程 | 71 min |
| P25 | 学生作品展示（无旁白，无字幕） | 8 min |

课程三大块：**光栅化与变换（P05–P09）→ 几何（P10–P14）→ 渲染与动画（P15–P24）**，P03/P04 是数学预复习。

---

## 字幕的质量边界（务必先读）

1. **只有中文，没有英文原文。** B站合集没有上传 CC 字幕，只有 AI 自动生成的中文轨（`ai-zh`）。原视频的英文字幕在 YouTube 原链接上，本次未能获取。
2. **AI 字幕必然有错。** 识别错误、术语译法不统一、公式口述被听错都很常见，引用前请对照视频画面。
3. **覆盖率已验证。** 24 讲的字幕时间轴均覆盖到片尾（99.7%–100%），没有截断。
4. **P25 无字幕。** 那是学生作品展示，纯画面。

---

## 复现方法

需要：`yt-dlp`、一个已登录的 B站 cookie（字幕接口需要 `SESSDATA`，匿名只能拿到弹幕）。

```powershell
# 1. 抓字幕（裸 SRT -> 合并文本）
yt-dlp --cookies cookies.txt --skip-download --write-subs `
  --sub-langs "ai-zh" --convert-subs srt `
  -o "subs/P%(playlist_index)02d - %(title)s.%(ext)s" `
  "https://www.bilibili.com/video/BV1yVfwBtEot"

# 2. srt -> 合并段落文本 + 总 md
python scripts/srt_to_text.py

# 3. 总结完整性校验 + 生成索引
python scripts/check_summaries.py
```

`cookies.txt` 的格式是 Netscape cookie 文件，从浏览器导出的 `Cookie:` 头可以直接转换（脚本见 [`scripts/`](scripts/)）。

---

## 版权与使用边界

- **原课程的著作权属于卡内基梅隆大学（CMU）及 Keenan Crane 教授**，课程视频、讲义、作业均未包含在本仓库中，请到[课程官方主页](http://15462.courses.cs.cmu.edu/)获取。
- 本仓库的**字幕文本**来自 B站视频的 AI 自动生成字幕，是原课内容的衍生品；**分集总结**和**转换脚本**是为学习目的整理的新增内容，以 MIT 协议发布。
- 本仓库仅供**个人学习与教学研究**使用，不得用于任何商业用途，不得用于二次分发原课内容。
- 如果原作者或权利人认为本仓库不妥，提出后我会立即删除相关内容。

## 相关

- 原课程官网：<http://15462.courses.cs.cmu.edu/>
- Keenan Crane 的个人主页：<https://www.cs.cmu.edu/~kmcrane/>
- 课程作业框架 Scotty3D：<https://github.com/CMU-Graphics/Scotty3D>
