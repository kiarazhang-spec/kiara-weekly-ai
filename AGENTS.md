# AGENTS.md

> Instructions for AI agents (Codex, Claude Code, Cursor, WorkBuddy, etc.) working in this repository.
> Human contributors: see [README.md](./README.md).

## Project overview

This is **Kiara Weekly · AI news speedrun** — a static, zero-backend archive of a weekly AI industry newsletter, hosted on GitHub Pages and auto-deployed via GitHub Actions.

- **Stack:** plain HTML + CSS, no JS framework, no build step.
- **Hosting:** GitHub Pages (branch: `main`, deploy via Actions).
- **Live site:** https://kiarazhang-spec.github.io/kiara-weekly-ai/

## Repository layout

```
.
├── index.html                    # Homepage — fetches posts/manifest.json at runtime
├── posts/
│   ├── YYYY-MM-DD.html           # One file per issue. Filename = Monday of the covered week (Pacific Time).
│   └── manifest.json             # Index of all issues. **AUTO-GENERATED. DO NOT EDIT BY HAND.**
├── assets/
│   └── style.css                 # Global stylesheet, single source of design tokens.
├── .github/workflows/deploy.yml  # Rebuilds manifest.json and deploys Pages on push to main.
├── README.md                     # Human-facing intro.
├── AGENTS.md                     # This file.
└── LICENSE                       # MIT for code; content under CC BY 4.0 (see README).
```

## ⛔ Hard rules — do NOT violate

1. **Never hand-edit `posts/manifest.json`.** It is recomputed on every push by `.github/workflows/deploy.yml`. Any manual edits will be overwritten on the next push and may cause merge conflicts. If you need to change what appears on the homepage, rename / move the corresponding HTML file in `posts/` instead.
2. **Never invent source URLs.** Every link in a newsletter post must be a real, clickable, verified URL pointing to the original article. If you cannot find a real link for a claim, drop the claim. No exceptions.
3. **Never fabricate facts, quotes, statistics, model benchmarks, funding amounts, or dates.** If unsure, search for the primary source. If still unsure, omit.
4. **Never put inline `style="..."` on the `.meta-line` (source attribution row).** Styling must come from `assets/style.css` only, to keep visual consistency across issues.
5. **Do not change the `posts/YYYY-MM-DD.html` filename convention.** `YYYY-MM-DD` is the Monday (Pacific Time) of the week being covered.
6. **Do not introduce a JS framework, build step, or backend** unless explicitly instructed. The project's value proposition includes "JAMstack at its most minimal".

## ✅ Writing rules for newsletter content (`posts/*.html`)

When generating or editing a weekly issue, follow these in order of priority:

### Source tier — 一手源铁律 (ironclad)

A **primary-source** link is required for every Top 5 item and every featured story. Primary sources are:

- **S-tier (best):** Official company blog or research page — `openai.com/blog`, `anthropic.com/news`, `deepmind.google/discover`, `ai.meta.com/blog`, `mistral.ai/news`, `huggingface.co/blog`, `developer.apple.com/news`, etc.
- **A-tier English (acceptable):** TechCrunch, The Verge, Bloomberg, Reuters, The Information, Financial Times, Wired, MIT Technology Review, Axios, The New York Times, The Wall Street Journal.
- **B-tier (use sparingly, only for context):** 机器之心, 量子位, 36Kr, 财联社, 腾讯科技, etc.

**Do not lead with B-tier sources.** A Chinese tech-media aggregator may be cited as a secondary "background" link if the primary source is also linked, but never as the only link.

### Content structure (8 sections per issue)

1. Header (title + subtitle + meta-line)
2. One-sentence overview (浅绿底块)
3. 🎯 Top 5 (5 items, each with link + one-line "why it matters")
4. 🔍 三大主题 (3 longer thematic write-ups with embedded links and 💡 视角 commentary)
5. 📰 其他值得看的 (categorized: 🧠 模型 / 🛠️ 产品 / 💰 商业 / ⚙️ Infra)
6. 📅 下周关注 (2-3 forward-looking items)
7. ⚠️ 信息来源说明 (source-tier disclosure for this issue)
8. 📋 关于本简报 (boilerplate footer)

### Word count

1000–1500 Chinese characters total per issue. Top 5 items: 1–2 sentences each. Theme write-ups: 80–150 characters each.

### Voice

Concise, analytic, product-marketing perspective. No hype words ("震撼", "颠覆"). Use specific numbers ($X billion, Y% growth, Z parameters) only when you have a verified source for them.

## 🔧 Workflow conventions

### Adding a new issue

```bash
# 1. Create posts/YYYY-MM-DD.html (Monday of the covered week, PT).
# 2. Verify every <a href> opens a real article.
# 3. Stage, commit, push.
git add posts/2026-06-29.html
git commit -m "post: AI weekly 2026-06-29"
git push
# 4. Wait ~3 minutes for Actions to rebuild manifest.json and deploy.
```

### After a push

GitHub Actions will:
1. Scan `posts/*.html` and rebuild `posts/manifest.json` (commits it back to `main` as `github-actions[bot]`).
2. Deploy the static site to GitHub Pages.

Because of step 1, your **next local action must be** `git pull --rebase` before any new commit, or push will be rejected.

### Commit message format

- `post: AI weekly YYYY-MM-DD` — new newsletter issue
- `style: <what>` — CSS / visual changes
- `docs: <what>` — README / AGENTS.md / LICENSE
- `fix: <what>` — bug fix (broken link, typo, etc.)
- `chore: <what>` — config, workflow, infra

### Branching

Single `main` branch. No PR flow required for solo work; just push directly. If working on a risky change, branch off as `wip/<short-name>`.

## 🎨 Design tokens (do not invent new ones)

Defined in `assets/style.css :root`:

- `--green: #2D8B3E` — sole accent color (links, emphasis numbers, section underlines, 视角 block left border)
- `--green-soft: #E8F3EA` — one-sentence overview block background
- `--text: #1a1a1a` — body text
- `--muted: #6b6b6b` — meta, captions
- `--bg: #ffffff` — page background
- Container max-width: **760px** (academic reading width — do not widen)
- Body font: system serif (Songti, Source Han Serif, etc.)
- Heading font: system sans-serif fallback

To re-theme, change `--green` only. Do not introduce additional accent colors.

## 🚫 Things agents have gotten wrong before (avoid these)

- Editing `manifest.json` manually → got overwritten, caused merge conflicts.
- Linking to aggregator Chinese sites (财联社 / 腾讯科技) as the only source → violates 一手源铁律.
- Using `style="..."` on `.meta-line` → broke visual consistency.
- Inventing model benchmark numbers without a real source → hallucinations.
- Pushing without `git pull --rebase` after Actions bot commit → push rejected.
- Adding emojis to commit messages or filenames → keep machine-parseable.

## 📜 License reminder

When generating any content, remember:
- **Newsletter text (`posts/*.html`):** CC BY 4.0. Attribution required when republished.
- **Code (HTML scaffolding, CSS, Actions YAML):** MIT.
- **Do not copy long verbatim passages from source articles.** Summarize, link to original. Quote sparingly and always with attribution.

## 📬 Questions

This file is the source of truth for agents. If something here conflicts with another instruction, prefer this file. If something is missing, open an Issue or ask the human maintainer (Kiara) before making structural changes.
