# Amazon Quick 介绍：PPT 与讲解视频

介绍 Amazon Quick 的主要功能、应用场景和最佳实践，重点是 Quick 桌面版（第 7–20 页）。共 36 页，讲解视频约 31 分钟，中文配音并带字幕。

内容依据 AWS 英文官方文档、定价页、What's New 和 AWS 博客整理，资料截至 2026-10-31；桌面版部分按 2026-11-03、套餐页（第 6 页）按 2026-11-05 的英文文档复核。每页底部列出该页内容的英文来源链接。本仓库不是 AWS 官方材料，功能、区域与价格以 AWS 官方页面为准。

## 下载

| 内容 | 文件 |
|---|---|
| 演示文稿（可编辑，讲稿在演讲者备注中） | [docs/Amazon-Quick-介绍.pptx](docs/Amazon-Quick-%E4%BB%8B%E7%BB%8D.pptx) |
| 讲解视频（1920×1080，约 31 分钟，字幕已烧录） | [Amazon-Quick-intro-zh.mp4](https://github.com/sunl/amazon-quick-intro/releases/latest/download/Amazon-Quick-intro-zh.mp4)（在 [Releases](https://github.com/sunl/amazon-quick-intro/releases) 中） |
| 字幕文件 | [docs/Amazon-Quick-介绍.srt](docs/Amazon-Quick-%E4%BB%8B%E7%BB%8D.srt) |

视频文件约 80 MB，放在 Releases 里，不随仓库克隆下载。

## 视频章节

| 时间 | 章节 | 页码 |
|---|---|---|
| 00:00 | 开场与议程 | 1–2 |
| 00:42 | 01 产品概览：定位、工作原理、关键演进、开通与套餐 | 3–6 |
| 04:32 | 02 Quick 桌面版：界面、Chat 进阶、Activity feed、Agents 与 routines、Skills、Connectors、My context、场景、安全与部署 | 7–20 |
| 20:30 | 03 其他主要功能：Chat、Spaces、Quick Sight、Research、Flows 与 Automate、Apps、集成与治理 | 21–28 |
| 25:49 | 04 应用场景：按部门的场景与客户案例 | 29–30 |
| 27:24 | 05 最佳实践与上手路径 | 31–34 |
| 30:14 | 参考资料与总结 | 35–36 |

## 目录结构

```
amazon-quick-intro/
├── README.md                    本说明
├── LICENSE                      MIT 许可
├── .gitignore                   不提交中间产物（build/、.venv/ 与本地视频文件）
│
├── docs/                        交付物
│   ├── Amazon-Quick-介绍.pptx   演示文稿，36 页，讲稿在演讲者备注中
│   └── Amazon-Quick-介绍.srt    讲解视频的字幕
│
├── content.py                   每页的标题、内容、讲稿和英文来源链接（修改内容只改这里）
├── build_deck.py                版式引擎：生成 PPTX
├── build_video.py               生成视频：逐步高亮的画面、Amazon Polly 配音、字幕、ffmpeg 合成
└── render_preview.py            用 LibreOffice 把 PPTX 渲染成 PNG（预览和视频画面共用）
```

## 重新生成

修改 `content.py` 后，按下面的步骤重新生成 PPT 和视频：

```bash
python3.12 -m venv .venv
.venv/bin/pip install python-pptx==1.0.2 imageio-ffmpeg==0.6.0 pypdfium2
.venv/bin/python build_deck.py                           # 生成 docs/Amazon-Quick-介绍.pptx
.venv/bin/python build_video.py --profile <aws-profile>  # 生成 docs/ 下的 MP4 与 SRT
```

- 生成视频需要 LibreOffice（`soffice`）、Noto Sans CJK 字体，以及有 `polly:SynthesizeSpeech` 权限的 AWS profile。字体目录在 `render_preview.py` 的 `CJK_DIR` 中设置。
- 中间文件写在 `build/`：视频画面、按句缓存的配音、字幕和章节时间（`build/video/chapters.txt`）。只改动少量讲稿时，只会重新合成改动的句子。

## 说明

- PPTX 使用 Microsoft YaHei 字体；视频画面用 LibreOffice 渲染，字体替换为 Noto Sans CJK SC，所以视频中的字形和换行与 PowerPoint 中的显示略有差异。
- 客户案例中的引述和数字为 AWS 客户页与博客原文的中文转述。
- 配音由 Amazon Polly（Zhiyu，neural）合成。

## 许可

[MIT](LICENSE)
