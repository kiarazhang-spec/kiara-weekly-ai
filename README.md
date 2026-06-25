# Kiara Weekly · AI news speedrun

> A curated weekly digest of the AI industry — model launches, product moves, capital signals, and infra shifts — written from a product marketing perspective.

🌐 **Read it live → [kiarazhang-spec.github.io/kiara-weekly-ai](https://kiarazhang-spec.github.io/kiara-weekly-ai/)**

每周一发布上周（周一至周日 PT）的 AI 行业精选简报，Stratechery 式极简学术风。每期包含本周 Top 5、三大主题、四类子分类（🧠 模型 / 🛠️ 产品 / 💰 商业 / ⚙️ Infra）、下周看点。

---

## ✨ Why this exists

市面上 AI 周报大多是两种极端：要么是聚合所有新闻的"水分巨大的清单"，要么是只关心论文的"研究员视角"。这份周报试图填补一个空位：**对产品和市场决策有用的、由人工筛选过的、带有产品营销视角的 AI 行业信号**。

每条新闻都来自 OpenAI / Anthropic / DeepMind / TechCrunch / Bloomberg 等一手或英文一线来源，每条都有可点击的具体原文链接，**没有幻觉链接**。

---

## 📐 How it's built

一个零成本的纯静态站点，托管在 GitHub Pages，靠 GitHub Actions 自动归档：

```
kiara-weekly-ai/
├── index.html                  # 首页（用 fetch 读 manifest.json 渲染）
├── posts/
│   ├── 2026-06-15.html         # 每期文章（文件名 = 监测周期周一日期）
│   └── manifest.json           # 期数索引（Actions 自动维护）
├── assets/style.css            # 全站样式
└── .github/workflows/deploy.yml  # 扫描 posts/ → 重算 manifest → 部署 Pages
```

技术栈：纯 HTML/CSS，零 JS 框架，零后端。**这就是 JAMstack 最朴素的形态。**

---

## 🧪 Want to start your own newsletter?

> 👉 **想做自己的周报？用更干净的模板**：[`ai-weekly-template`](https://github.com/kiarazhang-spec/ai-weekly-template) — 同样的架构，但内容是 placeholder，不绑定任何 AI 工具，5 步上线。本 repo 是"成品橱窗"，那个 repo 是"工具脚手架"。

或者直接从本 repo Fork：

```bash
# 1. Fork or "Use this template" on GitHub
# 2. 改 index.html 里的标题和说明
# 3. 改 assets/style.css :root 里的 --green 换主题色
# 4. 启用 Pages：Settings → Pages → Source: GitHub Actions
# 5. 写第一期 HTML 放进 posts/YYYY-MM-DD.html
# 6. git push — Actions 会自动重算 manifest 并部署
```

新增一期的最小流程：

```bash
git add posts/2026-06-29.html
git commit -m "post: AI weekly 2026-06-29"
git push
# ~3 分钟后访问 https://<your-username>.github.io/<repo>/posts/2026-06-29.html
```

每期 HTML 的结构（8 段）：报头 → 一句话总览 → 🎯 Top 5 → 🔍 三大主题 → 📰 其他值得看的 → 📅 下周关注 → ⚠️ 信息来源说明 → 📋 关于本简报。

> ⚙️ 自动化部分由 [`ai-weekly-publish`](https://github.com/kiarazhang-spec/ai-weekly-publish) skill 驱动（agent workflow，独立 repo，敬请期待）。手写也完全可以，模板是普通 HTML。

---

## 🎨 Design system

- 主题色：`#2D8B3E` 一抹绿（仅用于链接、强调数字、章节锚线、视角块边框）
- 字体：系统衬线（中文），系统无衬线 fallback
- 容器宽度：760px（学术阅读宽度）
- 视角块：浅灰底 + 绿色左边框
- 一句话总览块：浅绿底 `#E8F3EA`
- 列表项：绿色实心圆点

修改全站颜色：编辑 `assets/style.css` 顶部 `:root` 里的 `--green` 变量。

---

## 📝 Feedback

如果发现事实错误、链接失效，或者想推荐你觉得值得收录的信源——欢迎开 [Issue](https://github.com/kiarazhang-spec/kiara-weekly-ai/issues)。

---

## ⚠️ Disclaimer · 免责声明

**请以一手原文为准。** 本简报是个人对公开信息的二次整理与解读，目的是帮助读者快速识别值得深入阅读的原始材料。每条新闻都标注了原文链接，**请务必点击原文阅读**，不要把这份简报当作事实本身。

- 📌 **不构成投资、商业或法律建议**。涉及上市公司、融资、股价、产品定价、监管动向等内容仅供参考，不构成任何形式的投资建议或商业决策依据。
- 📌 **观点 = 个人观点**。每期中的"💡 视角"等评论性段落仅代表作者个人在写作时的理解，不代表任职机构立场，也可能随后续信息更新而失效。
- 📌 **可能存在事实误差**。AI 行业变化极快，简报内容基于发布时点公开报道，可能在事后被官方更正或推翻。如发现错误，欢迎开 Issue 指出。
- 📌 **不要曲解或断章取义**。引用本简报内容时，请同时附上对应的原文链接，并清楚标注哪些是原文事实、哪些是作者观点。
- 📌 **商标与版权归原所有方**。文中提及的公司、产品、模型名称均为各自所有方的商标或注册商标，简报仅作非商业性引用与评论。
- 📌 **如有侵权请联系**。本简报遵循合理使用原则进行引用与摘录，如内容所有方认为存在不当使用，请开 Issue 或联系作者，将在合理时间内处理。

---

## 📄 License

- **内容**（`posts/` 目录下的所有简报文本与 `index.html` 的展示文案）：[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — 允许转载与改编，请注明出处链接。
- **代码**（HTML 结构 / CSS / GitHub Actions 脚本）：[MIT](./LICENSE) — 随便用，保留版权声明即可。

简报内容的版权归作者 Kiara Zhang 所有。转载或引用请注明 "Source: Kiara Weekly · AI news speedrun" 并附本站链接。
