# AI 每周简报 · kiara-weekly-ai

> 由 Kiara Zhang 主编 · 每周一太平洋时间早 8 点更新

经过筛选的 AI 行业每周精选简报，覆盖模型、产品、商业、Infra 四个维度。Stratechery 极简学术风。

🌐 **公开访问**：https://kiarazhang-spec.github.io/kiara-weekly-ai/

---

## 📁 目录结构

```
kiara-weekly-ai/
├── index.html              # 首页（含动态归档列表）
├── posts/
│   ├── manifest.json       # 期数清单（自动维护）
│   ├── 2026-W21.html       # 单期文件
│   ├── 2026-W20.html
│   └── ...
├── assets/
│   └── style.css           # 全站公用样式
└── .github/workflows/
    └── deploy.yml          # GitHub Actions：自动 manifest + 部署 Pages
```

---

## ➕ 如何新增一期

把新一期 HTML 放进 `posts/`，命名为 `YYYY-WXX.html`（如 `2026-W22.html`），然后：

```bash
git add posts/2026-W22.html
git commit -m "feat: add 2026 W22"
git push
```

GitHub Actions 会自动：
1. 扫描 `posts/` 目录
2. 更新 `posts/manifest.json`
3. 重新部署 Pages

约 1-2 分钟后新一期就会出现在首页"最新一期"和"历史归档"区。

> **提示**：自动抽取的标题/摘要可能不够精准，可以手动编辑 `manifest.json` 里对应记录的 `title` 和 `summary` 字段，再 push 一次即可。手动编辑过的字段在后续 Actions 运行时会被保留。

---

## 🎨 视觉系统

参考风格：Stratechery 极简学术
- 主题色：`#2D8B3E` 一抹绿（仅用于链接、强调数字、章节锚线、视角块边框）
- 正文：深灰 `#1F2937` / 次级 `#4B5563`
- 背景：白底 + 浅灰强调块 `#F8F9FA` / 浅绿一句话总览 `#E8F3EA`
- 字号：H1 30 / H2 22 / H3 17 / 正文 15.5px
- 容器宽度：760px（学术阅读宽度）

修改全站颜色：编辑 `assets/style.css` 顶部 `:root` 里的 `--green` 变量。

---

## 🔧 单期 HTML 模板

每一期都是独立的 HTML 文件，结构固定：

1. **报头** masthead（kicker + 标题 + 监测周期）
2. **本周一句话总览** lead（浅绿底引用块）
3. **🎯 本周 Top 5**（每条：编号标题 + 来源 + 3 句摘要 + 产品技术视角）
4. **🔍 本周三大主题**（主题 + 支撑新闻 + 趋势研判）
5. **📰 其他值得看的**（🧠 模型 / 🛠️ 产品 / 💰 商业 / ⚙️ Infra）
6. **📅 下周值得关注**
7. **⚠️ 信息来源说明** + **📋 关于本简报**

---

## 📝 反馈

如发现事实错误或链接失效，请提 Issue 或通过其他渠道告知。
