# Kiara Weekly · AI

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

整个仓库可以当作脚手架直接 Fork：

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

## 📄 License

内容（`posts/` 目录下的所有简报文本）：CC BY 4.0 — 允许转载，请注明出处链接。
代码（HTML / CSS / GitHub Actions 脚本）：MIT。
