#!/usr/bin/env python3
"""
Generate docs/archive.html — past daily digests + trend syntheses index.

過去の Daily Digest と Trends Synthesis を一覧表示するアーカイブページ。
- docs/daily/ にコピー済みの MD/HTML へのリンクを表示
- docs/synthesis/ にコピー済みの trends synthesis MD へのリンクを表示
- ダウンロードボタン(MD)+ HTML 開くボタンの2系統

Usage:
    python scripts/generate_archive_html.py
Output:
    docs/archive.html
"""
from __future__ import annotations
import html
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

JST = timezone(timedelta(hours=9))
GEN_AT = datetime.now(JST).strftime("%Y-%m-%d %H:%M JST")


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def extract_headline(md_path: Path) -> str:
    """Daily MD の `> 本日のハイライト:` 行から先頭部分を抽出して見出しに使う。"""
    try:
        with md_path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("> 本日のハイライト"):
                    # 「:」以降を取得、Markdown 装飾を除去、80字に丸め
                    body = line.split(":", 1)[-1] if ":" in line else line
                    body = re.sub(r"\*+", "", body)
                    body = body.strip()
                    return body[:140] + ("…" if len(body) > 140 else "")
                if line.startswith("> 横断 Synthesis") or line.startswith("> **横断"):
                    continue
        return "(本日のハイライト行なし)"
    except FileNotFoundError:
        return "(本文未取得)"


def render_daily_row(date: str, md_exists: bool, html_exists: bool, headline: str) -> str:
    md_btn = (
        f'<a class="btn btn-md" href="daily/{date}.md" download>📄 MD</a>'
        if md_exists else '<span class="btn btn-disabled">MD なし</span>'
    )
    html_btn = (
        f'<a class="btn btn-html" href="daily/{date}.html" target="_blank">🌐 HTML を開く</a>'
        if html_exists else '<span class="btn btn-disabled">HTML なし</span>'
    )
    return f"""
    <tr>
      <td class="date">{esc(date)}</td>
      <td class="headline">{esc(headline)}</td>
      <td class="actions">{md_btn} {html_btn}</td>
    </tr>
    """


def render_trends_row(filename: str, md_exists: bool) -> str:
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})-trends\.md", filename)
    date = date_match.group(1) if date_match else filename
    md_btn = (
        f'<a class="btn btn-md" href="synthesis/{filename}" download>📄 MD</a>'
        if md_exists else '<span class="btn btn-disabled">MD なし</span>'
    )
    return f"""
    <tr>
      <td class="date">{esc(date)}</td>
      <td class="headline">3つの大潮流 横断 Synthesis</td>
      <td class="actions">{md_btn}</td>
    </tr>
    """


def build_archive(docs_dir: Path) -> str:
    # Daily digests
    daily_dir = docs_dir / "daily"
    daily_rows: list[str] = []
    if daily_dir.exists():
        md_files = sorted(daily_dir.glob("*.md"), key=lambda p: p.name, reverse=True)
        for md_path in md_files:
            date = md_path.stem
            html_path = md_path.with_suffix(".html")
            headline = extract_headline(md_path)
            daily_rows.append(render_daily_row(
                date, True, html_path.exists(), headline
            ))

    daily_table = "\n".join(daily_rows) if daily_rows else (
        '<tr><td colspan="3" class="empty">まだ Daily Digest はアーカイブされていません。'
        '次回の daily_run.ps1 実行時にコピーされます。</td></tr>'
    )

    # Trends syntheses
    synth_dir = docs_dir / "synthesis"
    synth_rows: list[str] = []
    if synth_dir.exists():
        md_files = sorted(synth_dir.glob("*-trends.md"), key=lambda p: p.name, reverse=True)
        for md_path in md_files:
            synth_rows.append(render_trends_row(md_path.name, True))

    synth_table = "\n".join(synth_rows) if synth_rows else (
        '<tr><td colspan="3" class="empty">まだ Trends Synthesis はアーカイブされていません。</td></tr>'
    )

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>アーカイブ — ai-news-vault</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --cream: #F5F1E8;
      --indigo: #2C3E50;
      --slate: #4A5568;
      --sage: #7A9B85;
      --terracotta: #B5705F;
      --stone-light: #ECE7DC;
      --stone-mid: #D4CFC4;
      --soft-gray: #A8B0BA;
      --white: #FFFFFF;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; font-family: 'Noto Sans JP', sans-serif;
      background: var(--cream); color: var(--slate);
      line-height: 1.6; font-size: 14px;
    }}
    a {{ color: var(--sage); text-decoration: none; }}
    a:hover {{ color: var(--terracotta); }}
    h2 {{ color: var(--indigo); margin-top: 0; }}

    .topbar {{
      position: fixed; top: 0; left: 0; right: 0; height: 56px;
      background: var(--indigo); color: var(--white);
      display: flex; align-items: center; padding: 0 16px;
      z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    .topbar .brand {{ font-weight: 700; font-size: 14px; }}
    .topbar .brand .sub {{ font-weight: 400; color: var(--stone-mid); margin-left: 12px; font-size: 11px; }}
    .topbar .nav-links {{ margin-left: auto; display: flex; gap: 16px; align-items: center; }}
    .topbar .nav-links a {{
      color: var(--stone-mid); font-size: 12px; font-weight: 500;
      padding: 6px 10px; border-radius: 3px; transition: background 0.15s;
    }}
    .topbar .nav-links a.active {{ background: var(--sage); color: var(--white); }}
    .topbar .nav-links a:hover {{ background: rgba(255,255,255,0.1); color: var(--white); }}
    .topbar .gen {{ font-size: 11px; color: var(--soft-gray); }}

    .container {{ max-width: 1100px; margin: 56px auto 0; padding: 24px 24px 60px; }}
    .intro {{ background: var(--white); padding: 20px 24px; border-radius: 6px; border-left: 4px solid var(--sage); margin-bottom: 24px; }}
    .intro h1 {{ color: var(--indigo); margin: 0 0 8px; font-size: 22px; }}
    .intro p {{ margin: 8px 0 0; font-size: 13px; }}

    section {{ background: var(--white); padding: 20px 24px; border-radius: 6px; margin-bottom: 24px; }}
    section h2 {{ font-size: 18px; padding-bottom: 8px; border-bottom: 1px solid var(--stone-mid); }}
    table {{ width: 100%; border-collapse: collapse; font-size: 13px; }}
    thead th {{
      background: var(--indigo); color: var(--white); text-align: left;
      padding: 10px 12px; font-weight: 700; font-size: 12px;
    }}
    tbody td {{ padding: 12px; border-bottom: 1px solid var(--stone-mid); vertical-align: top; }}
    tbody tr:nth-child(even) td {{ background: var(--stone-light); }}
    tbody tr:hover td {{ background: #FAF8F2; }}
    td.date {{ font-weight: 700; color: var(--indigo); white-space: nowrap; width: 110px; }}
    td.headline {{ font-size: 12px; color: var(--slate); line-height: 1.5; }}
    td.actions {{ white-space: nowrap; width: 280px; text-align: right; }}
    td.empty {{ text-align: center; color: var(--soft-gray); padding: 28px 12px; font-style: italic; }}

    .btn {{
      display: inline-block; padding: 5px 10px; border-radius: 3px;
      font-size: 11px; font-weight: 700; margin-left: 4px;
      transition: background 0.15s, color 0.15s;
      border: 1px solid;
    }}
    .btn-md {{ color: var(--terracotta); border-color: var(--terracotta); }}
    .btn-md:hover {{ background: var(--terracotta); color: var(--white); }}
    .btn-html {{ color: var(--sage); border-color: var(--sage); }}
    .btn-html:hover {{ background: var(--sage); color: var(--white); }}
    .btn-disabled {{
      color: var(--soft-gray); border-color: var(--stone-mid);
      background: var(--stone-light);
    }}

    .footer {{ max-width: 1100px; margin: 32px auto 0; padding: 24px; color: var(--soft-gray); font-size: 11px; border-top: 1px solid var(--stone-mid); }}

    @media (max-width: 760px) {{
      td.actions {{ width: auto; white-space: normal; }}
      .btn {{ display: block; margin: 4px 0; text-align: center; }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <div class="brand">
      AI NEWS VAULT
      <span class="sub">Archive</span>
    </div>
    <nav class="nav-links">
      <a href="index.html">最新版</a>
      <a href="archive.html" class="active">アーカイブ</a>
      <span class="gen">Generated: {GEN_AT}</span>
    </nav>
  </header>

  <div class="container">
    <div class="intro">
      <h1>アーカイブ — 過去の蓄積を MD / HTML でダウンロード</h1>
      <p>
        <strong>最新版は <a href="index.html">トップページ</a>(自動更新)から</strong>。
        本ページでは過去の Daily Digest と横断 Synthesis を一覧表示します。
        <strong>📄 MD</strong> ボタンでマークダウンファイルをダウンロード(Obsidian 等で開けます)、
        <strong>🌐 HTML を開く</strong> ボタンで整形済みページを別タブで表示します。
      </p>
    </div>

    <section>
      <h2>Daily Digest(日次まとめ)</h2>
      <table>
        <thead>
          <tr>
            <th>日付</th>
            <th>本日のハイライト(冒頭抜粋)</th>
            <th style="text-align:right">アクション</th>
          </tr>
        </thead>
        <tbody>
          {daily_table}
        </tbody>
      </table>
    </section>

    <section>
      <h2>横断 Synthesis(複数日横断の潮流まとめ)</h2>
      <table>
        <thead>
          <tr>
            <th>日付</th>
            <th>内容</th>
            <th style="text-align:right">アクション</th>
          </tr>
        </thead>
        <tbody>
          {synth_table}
        </tbody>
      </table>
    </section>
  </div>

  <footer class="footer">
    <p>
      <strong>ai-news-vault Archive</strong> — 過去の Daily Digest と横断 Synthesis をダウンロード可能な形式で公開しています。
      <br>
      4/7/9/12 時の Daily 自動取得時に再生成され、新しい Digest が追加されます。
      <br>
      Last generated: {GEN_AT}
    </p>
  </footer>
</body>
</html>
"""


def main():
    root = Path(__file__).resolve().parent.parent
    docs_dir = root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    out_path = docs_dir / "archive.html"
    out_path.write_text(build_archive(docs_dir), encoding="utf-8")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
