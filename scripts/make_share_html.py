#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_share_html.py — 把站点版周报 HTML 转成「分享版」单文件 HTML。
用途：发邮件/发人用。特点：CSS 全内联（双击即看、排版不崩）、零 GitHub 痕迹、无死链。

用法：
    python3 make_share_html.py <站点版html路径>
例：
    python3 make_share_html.py /Users/kiarazhang/kiara-weekly-ai/posts/2026-08-31.html

输出：~/Downloads/AI周报_{YYYY-MM-DD}_分享版.html

规则（务必看懂再改）：
- 只抹「指向 Kiara 自己 GitHub 的痕迹」：返回首页死链、"GitHub Issues 反馈"这类自引用。
- 新闻正文里客观提到的 GitHub（如"IBM 分发于 GitHub"、"S 级信源含 GitHub release"）属行业事实，保留。
"""
import re, sys, os, pathlib

def main():
    if len(sys.argv) < 2:
        print("用法: python3 make_share_html.py <站点版html路径>"); sys.exit(1)
    src = pathlib.Path(sys.argv[1]).resolve()
    if not src.exists():
        print(f"找不到文件: {src}"); sys.exit(1)

    html = src.read_text(encoding="utf-8")
    root = src.parent.parent  # posts/ 的上一级 = 项目根
    m = re.search(r"(\d{4}-\d{2}-\d{2})", src.name)
    date = m.group(1) if m else "unknown"

    # 1) 内联外部 CSS：把 <link rel=stylesheet href=../assets/style.css> 换成 <style>文件内容</style>
    def inline_css(match):
        href = match.group(1)
        css_path = (src.parent / href).resolve()
        if css_path.exists():
            css = css_path.read_text(encoding="utf-8")
            return f"<style>\n/* inlined from {href} */\n{css}\n</style>"
        return ""  # 找不到就直接去掉这行 link
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="([^"]+)"\s*/?>', inline_css, html)

    # 2) 删「← 返回首页」死链（分享版是孤立文件，没有 index.html）
    #    把整个包住"返回首页"的 <a ...>...</a> 连同前面的 " · " 分隔符去掉
    html = re.sub(r'\s*·\s*<a\s+href="[^"]*index\.html"[^>]*>[^<]*返回首页[^<]*</a>', '', html)

    # 3) 抹掉指向自己 GitHub 的自引用："请通过 GitHub Issues 反馈" → 中性措辞
    html = html.replace("请通过 GitHub Issues 反馈", "欢迎回信指正")

    # 4) 兜底：如仍残留 kiarazhang / github.io（本不该有），报警但不静默通过
    leaks = re.findall(r"kiarazhang|github\.io", html, flags=re.I)
    if leaks:
        print(f"⚠️ 警告：仍检测到自引用痕迹 {set(leaks)}，请人工检查！")

    out = pathlib.Path.home() / "Downloads" / f"AI周报_{date}_分享版.html"
    out.write_text(html, encoding="utf-8")
    print(f"✅ 分享版已生成: {out}")
    print(f"   大小: {round(out.stat().st_size/1024,1)} KB")

    # 自检报告
    final = out.read_text(encoding="utf-8")
    print("   自检:")
    print(f"     - CSS 已内联: {'是' if '<style>' in final and 'inlined from' in final else '否'}")
    print(f"     - 无返回首页死链: {'是' if 'index.html' not in final else '否（需检查）'}")
    print(f"     - 无 GitHub Issues 自引用: {'是' if 'GitHub Issues' not in final else '否（需检查）'}")

if __name__ == "__main__":
    main()
