# Vidu vs Seedance 2.0 · 视频效果对比

同一提示词下 Vidu 与 Seedance 2.0 的视频直出效果逐组对比（14 组、28 段视频）。浅色编辑评测风，左右并排、一键同步播放。

## 结构
- `public/` — 部署产物（静态站）：`index.html` + `videos/`（28 段压缩后视频，约 71MB）
- `build/` — 源文件：`template.html`（页面模板）、`site_data.json`（14 组数据）、`build.py`（注入数据生成 `public/index.html`）

## 重新生成
改完 `build/template.html` 后运行：`python3 build/build.py`

## 部署
纯静态站，发布目录 `public/`，无需构建命令。
