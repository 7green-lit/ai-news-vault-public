#!/usr/bin/env python3
"""
Generate single-page HTML version of topics-overview deck v3.

PPTX(`generate_topics_overview_deck_v3.py`)の TOPICS データを再利用し
GitHub Pages で公開するための1ページ目次型 HTML を `docs/index.html` に出力する。

- 全16セクション(全体俯瞰 + 14トピック)を1ページに収載
- 左固定の目次から各セクションへアンカージャンプ(モバイルは折りたたみ)
- フォント: Noto Sans JP(Google Fonts CDN)
- カラー: PPTX と同じ「落ち着いたトーン」パレット

Usage:
    python scripts/generate_topics_overview_html.py
Output:
    docs/index.html
"""
from __future__ import annotations
import html
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_topics_overview_deck_v3 import TOPICS as _ALL_TOPICS

# Topics excluded from public HTML(個別事情で公開しないもの)
EXCLUDED_SLUGS = {""}
_TOPICS_BASE = [t for t in _ALL_TOPICS if t["slug"] not in EXCLUDED_SLUGS]

# ---------- 編集可能なソース MD から問いを上書き読み取り ----------
# - `docs/source/topics/<slug>/_index.md` の「## 自分の問い」セクションがあれば
#   Python TOPICS dict の q を上書き(=共同編集者の修正が反映される)
def _resolve_source_topics_dir() -> Path | None:
    """docs/source/topics/ ディレクトリを探索。なければ None。
    優先順:
    1) 環境変数 TOPICS_SOURCE_DIR (GitHub Actions 用)
    2) <repo_root>/source/topics/ (GitHub Actions / リポジトリ内ファイル配置)
    3) <project_root>/docs/source/topics/ (ローカル実行時)
    """
    import os
    env = os.environ.get("TOPICS_SOURCE_DIR")
    if env and Path(env).exists():
        return Path(env)
    here = Path(__file__).resolve()
    # candidate A: parent/.../docs/source/topics/(ローカル)
    proj_root = here.parent.parent
    cand = proj_root / "docs" / "source" / "topics"
    if cand.exists():
        return cand
    # candidate B: scripts/ が repo 直下にある(GitHub Actions context)
    cand = here.parent.parent / "source" / "topics"
    if cand.exists():
        return cand
    return None

def _parse_question_from_index_md(md_path: Path) -> str | None:
    """_index.md の `## 自分の問い` セクション本文を抽出。
    `>` ブロッククォートや空行を除去して連結。
    """
    if not md_path.exists():
        return None
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return None
    m = re.search(
        r"^##\s*自分の問い\s*$(.*?)(?=^##\s|\Z)",
        text, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    body = m.group(1).strip()
    # ブロッククォート(> で始まる注記行)を除外
    lines = []
    for ln in body.splitlines():
        s = ln.strip()
        if not s:
            continue
        if s.startswith(">"):
            continue
        # 箇条書きの先頭 "- " を除去して可読化(オプション)
        if s.startswith("- "):
            s = s[2:]
        lines.append(s)
    # 連結。長くなりすぎる場合は最初の段落だけにする等の調整は将来検討
    return " ".join(lines).strip() or None

def _apply_source_overrides(topics: list[dict]) -> list[dict]:
    """docs/source/topics/<slug>/_index.md の問いを TOPICS dict に上書き反映"""
    src_dir = _resolve_source_topics_dir()
    if src_dir is None:
        return topics
    out = []
    for t in topics:
        new_q = _parse_question_from_index_md(src_dir / t["slug"] / "_index.md")
        if new_q and new_q != t.get("q"):
            t = {**t, "q": new_q}  # immutable update
        out.append(t)
    return out

TOPICS = _apply_source_overrides(_TOPICS_BASE)

JST = timezone(timedelta(hours=9))
GEN_AT = datetime.now(JST).strftime("%Y-%m-%d %H:%M JST")

# ---------- Daily highlights auto-detection ----------
def find_latest_daily_md(root: Path) -> Path | None:
    """daily/YYYY-MM-DD.md の中で最新のものを返す。なければ None。"""
    daily_dir = root / "daily"
    if not daily_dir.exists():
        return None
    candidates = []
    for p in daily_dir.glob("*.md"):
        m = re.match(r"^(\d{4}-\d{2}-\d{2})\.md$", p.name)
        if m:
            candidates.append((m.group(1), p))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    return candidates[0][1]

def parse_daily_highlights(md_path: Path, max_items: int = 8) -> tuple[str, list[tuple[str, str, str]]]:
    """Daily MD を解析し、(日付, [(head, body, url), ...]) を返す。

    "## 🔥 重要度・高" 配下の "### " 見出し項目を取り出し
    各項目から 要約(- **要約**: )本文 と 最初のソース URL を抽出する。
    """
    date = md_path.stem  # YYYY-MM-DD
    items: list[tuple[str, str, str]] = []
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return date, []

    # "## 🔥 重要度・高" セクションを切り出す(次の "## " まで)
    high_match = re.search(
        r"##\s*[🔥⚡]?\s*重要度・高\s*\n(.*?)(?=\n##\s|\Z)",
        text, re.DOTALL)
    if not high_match:
        return date, []
    section = high_match.group(1)

    # "### タイトル" → 次の "### " または末尾までを1ブロックに
    blocks = re.split(r"\n(?=###\s)", section)
    for block in blocks:
        b = block.strip()
        if not b.startswith("###"):
            continue
        # タイトル行
        title_line = b.split("\n", 1)[0].lstrip("#").strip()
        # 「— サブタイトル」がある場合は em-dash 前を主タイトルに
        title = re.split(r"\s*[—–-]\s*", title_line, maxsplit=1)[0].strip()

        # 要約行
        body = ""
        m_summary = re.search(r"-\s*\*\*要約\*\*\s*:\s*(.+?)(?=\n-\s\*\*|\n\Z)",
                              b, re.DOTALL)
        if m_summary:
            raw = m_summary.group(1).strip()
            # Markdown 装飾を簡易除去
            raw = re.sub(r"\*+", "", raw)
            raw = re.sub(r"\s+", " ", raw).strip()
            # 100字程度で要約
            body = raw[:140] + ("…" if len(raw) > 140 else "")

        # 最初のソース URL を抽出
        url = ""
        m_src = re.search(r"-\s*\*\*ソース\*\*\s*:(.+?)(?=\n-\s\*\*|\Z)",
                          b, re.DOTALL)
        if m_src:
            src_line = m_src.group(1)
            m_url = re.search(r"\((https?:/[^\)\s]+)\)", src_line)
            if m_url:
                url = m_url.group(1)

        if title:
            items.append((title, body, url))
        if len(items) >= max_items:
            break

    return date, items

# Fallback: 自動抽出に失敗した場合に使うハードコード版
FALLBACK_DAILY_DATE = "2026-05-13"
FALLBACK_DAILY_ITEMS = [
    ("Anthropic Claude for Legal 一斉ローンチ",
     "20+ コネクタ / 12 プラクティスエリアプラグイン / Thomson Reuters CoCounsel 連携。",
     "https://techcrunch.com/2026/05/12/the-ai-legal-services-industry-is-heating-up-anthropic-is-getting-in-on-the-action/"),
]

# ---------- Trends data (mirrors PPTX combined slide) ----------
TRENDS = [
    {
        "num": "01",
        "title": "コンサル × AIベンダー × 業界Tier1 — 3軸の同時進行",
        "summary": [
            "AIベンダーがコンサル業界に「取り込み(a)」「中抜き(b)」「業界直結(c)」の3軸で侵入",
            "コンサルは「中抜きされる側 + 取り込まれる側」の両ポジションに",
            "業界 Tier1 は AI ベンダー直結のスピード vs コンサル経由の総合性で選別する局面",
        ],
        "axes": [
            ("(a) AIベンダー × コンサル",
             "アクセンチュア × Anthropic 国内 / NEC × Anthropic / OpenAI Deployment Co + Tomoro(中抜き型)"),
            ("(b) AIベンダー × 業界Tier1",
             "Anthropic Claude for Legal × Big Law / OpenAI × PwC / Sakana × SMBC / Stripe × OpenAI"),
            ("(c) コンサル × 業界Tier1",
             "アクセンチュア × SAP ADVANCE / アクセンチュア × 日本精工 / 富士ソフト人月脱却"),
        ],
    },
    {
        "num": "02",
        "title": "業務代替型AI解雇とAIネイティブ企業の台頭",
        "summary": [
            "「AI効率化型解雇」がCEO公言レベルに達し、AIネイティブ企業が既存SaaS/SI/コンサルを構造的に置換",
            "Gartner 28% CEO が「AI が最大の収益リスク」と回答",
            "国内では「人月脱却 / 規模拡大 / 米AI 提携」の3戦略分岐で対応",
        ],
        "axes": [
            ("段階1: AI効率化型解雇",
             "Cloudflare 1,100 / Coinbase 14% / GM 数百名 / GitLab / Oracle 退職金問題"),
            ("段階2: AIネイティブ企業の侵入",
             "Cognition AI 日本法人 / OpenAI Deployment Co + Tomoro / Sierra AI / Decart / Lovable / Cursor"),
            ("段階3: 経営層の認識転換",
             "Gartner CEO 28% AI 収益リスク / @IT「AI 業務浸食予想以上」/ AINOW 意識改革6ステップ"),
        ],
    },
    {
        "num": "03",
        "title": "国内 AI 主権体制の同時成立(2026-05-11週)",
        "summary": [
            "法律 / 基盤製品 / 米AI 提携 / 製造業適応の4層が単一週で同時表面化",
            "EU 規制重視・米自由市場とは別の「公共財型 AI 戦略」が形成",
            "国内 AI ベンダー・SI・シンクタンクが規制対応と実装の両面で再編",
        ],
        "axes": [
            ("層1: 法律", "日本初 AI 特化法律(2026-05-11) / サイバー対処強化法10月施行"),
            ("層2: 基盤製品", "IBM Sovereign Core 一般提供(2026-05-05/11) / IBM Enterprise Advantage 拡充"),
            ("層3: 米AI提携", "NEC × Anthropic / アクセンチュア × Anthropic / Claude Platform on AWS"),
            ("層4: 製造業適応", "ファナック・安川フィジカルAI / 三菱電機・オムロン SDA SAT"),
        ],
    },
]

# ---------- Daily highlights (mirrors PPTX right column) ----------
DAILY_THEMES = ["最新版", "自動更新", "リンク付き", "アーカイブ可", "公開"]

# ----------  Impact data (mirrors PPTX last slide) ----------
# NOTE: 旧  Impact データブロックは削除済み(根本的な公開停止のため)

# ---------- HTML helpers ----------
def esc(s: str) -> str:
    return html.escape(s, quote=True)

def render_trend(t: dict) -> str:
    """3つの大潮流カード"""
    summary_html = "\n".join(f"<li>{esc(s)}</li>" for s in t["summary"])
    axes_html = "\n".join(
        f"<div class=\"axis\"><div class=\"axis-label\">{esc(label)}</div>"
        f"<div class=\"axis-body\">{esc(body)}</div></div>"
        for label, body in t["axes"]
    )
    return f"""
    <article class="trend">
      <div class="trend-num">{t['num']}</div>
      <div class="trend-body">
        <h3>{esc(t['title'])}</h3>
        <h4>概要</h4>
        <ul class="trend-summary">{summary_html}</ul>
        <h4>事例詳細</h4>
        <div class="axes">{axes_html}</div>
      </div>
    </article>
    """

def render_daily_item(i: int, head: str, body: str, url: str = "") -> str:
    link_html = ""
    if url:
        link_html = (
            f'<a class="daily-link" href="{esc(url)}" target="_blank" rel="noopener">'
            f'記事を開く ↗</a>'
        )
    return f"""
    <li class="daily-item">
      <div class="daily-num">{i+1:02d}</div>
      <div class="daily-content">
        <div class="daily-head">{esc(head)}</div>
        <div class="daily-body">{esc(body)}</div>
        {link_html}
      </div>
    </li>
    """

# ---------- AI Models: special rendering from llm-3services-comparison.md ----------
def render_ai_models_from_comparison(topic: dict, index: int) -> str:
    """ai-models トピックを `topics/ai-models/llm-3services-comparison.md`
    の内容(3LLM比較表)に置き換えて表示。今後、その MD を更新するだけで
    HTML にも自動反映される。
    """
    root = Path(__file__).resolve().parent.parent
    # 優先: source/topics/ai-models/ の編集可能版 → fallback: ローカル topics/
    src_dir = _resolve_source_topics_dir()
    md_path = None
    if src_dir is not None:
        cand = src_dir / "ai-models" / "llm-3services-comparison.md"
        if cand.exists():
            md_path = cand
    if md_path is None:
        cand = root / "topics" / "ai-models" / "llm-3services-comparison.md"
        if cand.exists():
            md_path = cand
    if md_path is None:
        # フォールバック: 比較 MD がない場合は通常レンダリング
        return render_topic_standard(topic, index)

    md_text = md_path.read_text(encoding="utf-8")

    # markdown ライブラリで HTML に変換(table / fenced code 拡張)
    try:
        import markdown
        html_body = markdown.markdown(
            md_text,
            extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
            output_format="html5")
    except ImportError:
        # markdown 未インストール時のフォールバック
        html_body = (
            f'<pre style="white-space:pre-wrap;font-size:11px;">{esc(md_text)}</pre>'
        )

    slug = topic["slug"]
    title = esc(topic["title"])
    version = esc(topic["version"])
    articles = topic["articles"]
    total = len(TOPICS) + 2

    return f"""
    <section id="topic-{slug}" class="topic-section ai-models-comparison">
      <header class="topic-header">
        <div class="topic-eyebrow">TOPIC · {esc(slug)} · 3LLM 比較表(llm-3services-comparison.md 連動) · articles: {articles} · {index:02d} / {total:02d}</div>
        <h2>{title} — 3大汎用 LLM 比較(Gemini / Claude / ChatGPT)</h2>
      </header>
      <div class="topic-q">
        <span class="q-label">運用ルール</span>
        <p>本セクションは <code>topics/ai-models/llm-3services-comparison.md</code> の内容を自動レンダリングしています。
        MD を更新すれば次回 HTML 再生成時にここに自動反映されます。</p>
      </div>
      <div class="comparison-body">
        {html_body}
      </div>
    </section>
    """

def render_topic(topic: dict, index: int) -> str:
    """Dispatcher: ai-models のみ比較表 MD から読み込み、それ以外は標準レンダリング。"""
    if topic["slug"] == "ai-models":
        return render_ai_models_from_comparison(topic, index)
    return render_topic_standard(topic, index)

def render_topic_standard(topic: dict, index: int) -> str:
    slug = topic["slug"]
    title = esc(topic["title"])
    version = esc(topic["version"])
    articles = topic["articles"]
    q = esc(topic["q"])

    points_html = ""
    for i, pt in enumerate(topic["points"]):
        summary_li = "\n".join(f"<li>{esc(s)}</li>" for s in pt["summary"])
        cases_li = "\n".join(f"<li>{esc(c)}</li>" for c in pt["cases"])
        points_html += f"""
        <article class="point">
          <div class="point-num">{i+1:02d}</div>
          <div class="point-body">
            <h4 class="point-head">{esc(pt['head'])}</h4>
            <div class="point-block">
              <div class="block-label">概要</div>
              <ul class="summary-list">{summary_li}</ul>
            </div>
            <div class="point-block">
              <div class="block-label cases">事例詳細</div>
              <ul class="cases-list">{cases_li}</ul>
            </div>
          </div>
        </article>
        """

    sig_summary = "\n".join(f"<li>{esc(s)}</li>" for s in topic["signals_summary"])
    sig_cases = "\n".join(f"<li>{esc(s)}</li>" for s in topic["signals_cases"])
    focus_summary = "\n".join(f"<li>{esc(s)}</li>" for s in topic["focus_summary"])
    focus_cases = "\n".join(f"<li>{esc(s)}</li>" for s in topic["focus_cases"])

    return f"""
    <section id="topic-{slug}" class="topic-section">
      <header class="topic-header">
        <div class="topic-eyebrow">TOPIC · {esc(slug)} · synthesis {version} · articles: {articles} · {index:02d} / {len(TOPICS)+2:02d}</div>
        <h2>{title}</h2>
      </header>
      <div class="topic-q">
        <span class="q-label">自分の問い</span>
        <p>{q}</p>
      </div>
      <div class="topic-body">
        <div class="topic-main">
          <h3 class="section-h">主要論点(問い検証の観察+含意)</h3>
          {points_html}
        </div>
        <aside class="topic-aside">
          <div class="aside-box">
            <h3 class="section-h">直近の重要シグナル(2026-04〜05)</h3>
            <div class="block-label">概要</div>
            <ul class="summary-list">{sig_summary}</ul>
            <div class="block-label cases">事例</div>
            <ul class="cases-list">{sig_cases}</ul>
          </div>
          <div class="aside-box terracotta">
            <h3 class="section-h terracotta">次の注視点</h3>
            <div class="block-label">概要</div>
            <ul class="summary-list">{focus_summary}</ul>
            <div class="block-label cases">事例/論点</div>
            <ul class="cases-list">{focus_cases}</ul>
          </div>
        </aside>
      </div>
    </section>
    """

# NOTE: 旧 render__section() は削除済み(根本的な公開停止のため)

def render_combined_section(daily_date: str, daily_items: list[tuple[str, str, str]]) -> str:
    """1枚目: 全体俯瞰 × 最新Daily(縦並びに展開)"""
    trends_html = "\n".join(render_trend(t) for t in TRENDS)
    theme_pills = "\n".join(
        f'<span class="pill pill-{i % 2}">{esc(t)}</span>'
        for i, t in enumerate(DAILY_THEMES)
    )
    daily_html = "\n".join(
        render_daily_item(i, *item) for i, item in enumerate(daily_items)
    )
    archive_note = (
        '<p class="archive-note">'
        f'過去の Daily Digest は <a href="archive.html">アーカイブ</a> から閲覧できます。'
        '</p>'
    )
    return f"""
    <section id="overview" class="topic-section overview-section">
      <header class="topic-header">
        <div class="topic-eyebrow">AI NEWS VAULT · TOPIC OVERVIEW + DAILY {esc(daily_date)} · 01 / {len(TOPICS)+2:02d}</div>
        <h2>AI業界の潮流 × 最新の Daily ハイライト</h2>
      </header>
      <div class="overview-grid">
        <div class="overview-left">
          <h3 class="section-h">13トピック横断 — AI業界の3つの大潮流</h3>
          <div class="trends">{trends_html}</div>
        </div>
        <div class="overview-right">
          <h3 class="section-h terracotta">最新のハイライト  {esc(daily_date)}(自動抽出 {len(daily_items)} 件)</h3>
          <div class="theme-pills">{theme_pills}</div>
          <ol class="daily-list">{daily_html}</ol>
          {archive_note}
        </div>
      </div>
    </section>
    """

def build_toc() -> str:
    items = ['<li><a href="#overview">01. AI業界の潮流 × 本日のハイライト</a></li>']
    for i, t in enumerate(TOPICS):
        items.append(
            f'<li><a href="#topic-{esc(t["slug"])}">{i+2:02d}. {esc(t["title"])}</a></li>'
        )
    return "\n".join(items)

# ---------- Page template ----------
def build_page(daily_date: str, daily_items: list[tuple[str, str, str]]) -> str:
    toc = build_toc()
    combined = render_combined_section(daily_date, daily_items)
    topics_html = "\n".join(render_topic(t, i + 2) for i, t in enumerate(TOPICS))
    _html = ""  # 公開停止のため空

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="13トピックを横断したAI業界の構造的潮流と本日のハイライトをまとめた俯瞰資料。GitHub Pages で自動更新されます。">
  <title>AI業界の潮流 × トピック俯瞰 — ai-news-vault</title>
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
      --ink: #1A1A1A;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; scroll-padding-top: 70px; }}
    body {{
      margin: 0;
      font-family: 'Noto Sans JP', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--cream);
      color: var(--slate);
      line-height: 1.65;
      font-size: 14px;
    }}
    a {{ color: var(--sage); text-decoration: none; }}
    a:hover {{ color: var(--terracotta); }}
    ul, ol {{ padding-left: 1.2em; margin: 0.4em 0; }}
    li {{ margin: 0.25em 0; }}
    h2, h3, h4 {{ color: var(--indigo); margin: 0.4em 0; }}

    /* Top bar (fixed) */
    .topbar {{
      position: fixed; top: 0; left: 0; right: 0; height: 56px;
      background: var(--indigo); color: var(--white);
      display: flex; align-items: center; padding: 0 16px;
      z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }}
    .topbar .brand {{
      font-weight: 700; font-size: 14px; letter-spacing: 0.02em;
    }}
    .topbar .brand .sub {{
      font-weight: 400; color: var(--stone-mid); margin-left: 12px; font-size: 11px;
    }}
    .topbar .nav-links {{ margin-left: auto; display: flex; gap: 16px; align-items: center; }}
    .topbar .nav-links a {{
      color: var(--stone-mid); font-size: 12px; font-weight: 500;
      padding: 6px 10px; border-radius: 3px; transition: background 0.15s;
    }}
    .topbar .nav-links a:hover {{ background: rgba(255,255,255,0.1); color: var(--white); }}
    .topbar .gen {{ font-size: 11px; color: var(--soft-gray); }}
    .toc-toggle {{
      display: none;
      background: var(--sage); color: var(--white); border: none;
      padding: 6px 12px; border-radius: 4px; cursor: pointer;
      font-family: inherit; margin-right: 12px;
    }}

    /* Layout */
    .layout {{
      display: grid; grid-template-columns: 260px 1fr;
      max-width: 1400px; margin: 56px auto 0; padding: 0;
      gap: 0;
    }}
    .toc-sidebar {{
      position: sticky; top: 56px; align-self: start;
      height: calc(100vh - 56px); overflow-y: auto;
      padding: 24px 20px; border-right: 1px solid var(--stone-mid);
      background: var(--cream);
    }}
    .toc-sidebar h3 {{
      font-size: 11px; text-transform: uppercase; color: var(--sage);
      letter-spacing: 0.08em; margin: 0 0 12px;
    }}
    .toc-sidebar ol {{
      list-style: none; padding: 0; margin: 0;
    }}
    .toc-sidebar li {{ margin: 4px 0; }}
    .toc-sidebar a {{
      display: block; padding: 6px 10px; border-radius: 4px;
      color: var(--slate); font-size: 12px; line-height: 1.4;
      transition: background 0.15s;
    }}
    .toc-sidebar a:hover {{ background: var(--stone-light); color: var(--indigo); }}

    .content {{ padding: 24px 36px 60px; min-width: 0; }}

    /* Sections */
    .topic-section {{
      background: var(--white); padding: 24px 28px;
      border-radius: 6px; margin-bottom: 24px;
      border-left: 4px solid var(--sage);
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}
    .topic-section.-impact {{ border-left-color: var(--terracotta); }}
    .topic-section.overview-section {{ border-left-color: var(--indigo); }}
    .topic-header {{ border-bottom: 1px solid var(--stone-mid); padding-bottom: 12px; margin-bottom: 16px; }}
    .topic-eyebrow {{
      font-size: 10px; color: var(--sage); text-transform: uppercase;
      font-weight: 700; letter-spacing: 0.05em; margin-bottom: 4px;
    }}
    .topic-section h2 {{ font-size: 22px; margin: 0; }}
    .topic-q {{
      background: var(--stone-light); padding: 12px 16px; border-radius: 4px;
      margin-bottom: 18px;
    }}
    .q-label {{
      font-size: 10px; font-weight: 700; color: var(--sage);
      text-transform: uppercase; letter-spacing: 0.05em;
    }}
    .topic-q p {{ margin: 4px 0 0; color: var(--indigo); font-size: 13px; }}

    .section-h {{
      font-size: 13px; font-weight: 700; color: var(--sage);
      margin: 18px 0 10px; padding-bottom: 4px;
      border-bottom: 1px dashed var(--stone-mid);
    }}
    .section-h.terracotta {{ color: var(--terracotta); }}

    /* Topic body grid */
    .topic-body {{
      display: grid; grid-template-columns: 1.6fr 1fr; gap: 20px;
    }}

    /* Points */
    .point {{
      display: grid; grid-template-columns: 36px 1fr; gap: 8px;
      margin-bottom: 16px; padding-bottom: 14px;
      border-bottom: 1px dotted var(--stone-mid);
    }}
    .point:last-child {{ border-bottom: none; }}
    .point-num {{
      font-size: 18px; font-weight: 700; color: var(--terracotta);
      line-height: 1;
    }}
    .point-head {{
      font-size: 13px; font-weight: 700; color: var(--indigo);
      margin: 0 0 8px;
    }}
    .point-block {{ margin: 6px 0; }}
    .block-label {{
      display: inline-block; font-size: 10px; font-weight: 700;
      color: var(--sage); text-transform: uppercase; letter-spacing: 0.05em;
      margin-top: 4px;
    }}
    .block-label.cases {{ color: var(--terracotta); }}
    .summary-list, .cases-list {{ font-size: 12px; margin: 4px 0 0; }}
    .cases-list li::marker {{ color: var(--terracotta); }}

    /* Aside */
    .aside-box {{
      background: var(--stone-light); padding: 14px 16px;
      border-radius: 4px; margin-bottom: 12px;
    }}
    .aside-box.terracotta {{ background: #F5EAE3; }}

    /* Overview section */
    .overview-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 24px;
    }}
    .trends {{ display: flex; flex-direction: column; gap: 14px; }}
    .trend {{
      display: grid; grid-template-columns: 48px 1fr; gap: 12px;
      background: var(--stone-light); padding: 14px 18px; border-radius: 4px;
    }}
    .trend-num {{
      font-size: 26px; font-weight: 700; color: var(--sage); line-height: 1;
    }}
    .trend-body h3 {{ font-size: 14px; margin: 0 0 6px; }}
    .trend-body h4 {{
      font-size: 10px; color: var(--sage); margin: 8px 0 4px;
      text-transform: uppercase; letter-spacing: 0.05em;
    }}
    .trend-summary {{ font-size: 12px; margin: 0; }}
    .axes {{ display: flex; flex-direction: column; gap: 4px; margin-top: 4px; }}
    .axis {{
      display: grid; grid-template-columns: 180px 1fr; gap: 8px;
      font-size: 11px;
    }}
    .axis-label {{ color: var(--terracotta); font-weight: 700; }}
    .axis-body {{ color: var(--slate); }}

    /* Daily list */
    .theme-pills {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 14px; }}
    .pill {{
      display: inline-block; padding: 3px 10px; border-radius: 12px;
      font-size: 11px; font-weight: 700; color: var(--white);
    }}
    .pill-0 {{ background: var(--sage); }}
    .pill-1 {{ background: var(--terracotta); }}
    .daily-list {{ list-style: none; padding: 0; margin: 0; }}
    .daily-item {{
      display: grid; grid-template-columns: 32px 1fr; gap: 10px;
      margin-bottom: 10px; padding-bottom: 8px;
      border-bottom: 1px dotted var(--stone-mid);
    }}
    .daily-num {{
      background: var(--indigo); color: var(--white);
      font-size: 11px; font-weight: 700; text-align: center;
      padding: 4px 0; border-radius: 3px; height: 22px; line-height: 14px;
    }}
    .daily-head {{ font-weight: 700; color: var(--indigo); font-size: 12px; }}
    .daily-body {{ font-size: 11px; color: var(--slate); margin-top: 2px; }}
    .daily-link {{
      display: inline-block; margin-top: 4px; font-size: 10px; font-weight: 700;
      color: var(--terracotta); text-decoration: none;
      padding: 2px 8px; border: 1px solid var(--terracotta); border-radius: 3px;
      transition: background 0.15s, color 0.15s;
    }}
    .daily-link:hover {{ background: var(--terracotta); color: var(--white); }}
    .archive-note {{
      margin-top: 12px; padding: 10px 14px; background: var(--stone-light);
      border-radius: 4px; font-size: 11px; color: var(--slate);
    }}
    .archive-note a {{ font-weight: 700; }}

    /* ai-models comparison rendering (markdown -> HTML) */
    .comparison-body {{ font-size: 13px; line-height: 1.7; }}
    .comparison-body h1 {{ font-size: 20px; color: var(--indigo); margin-top: 0; }}
    .comparison-body h2 {{ font-size: 17px; color: var(--indigo); margin-top: 28px; padding-bottom: 6px; border-bottom: 1px solid var(--stone-mid); }}
    .comparison-body h3 {{ font-size: 14px; color: var(--sage); margin-top: 22px; }}
    .comparison-body h4 {{ font-size: 13px; color: var(--terracotta); margin-top: 16px; }}
    .comparison-body p {{ margin: 0.5em 0; }}
    .comparison-body blockquote {{
      border-left: 3px solid var(--sage); padding: 8px 14px;
      background: var(--stone-light); margin: 12px 0; font-size: 12px;
    }}
    .comparison-body table {{
      border-collapse: collapse; width: 100%; margin: 12px 0;
      font-size: 11px; background: var(--white);
    }}
    .comparison-body table thead th {{
      background: var(--indigo); color: var(--white); padding: 8px 10px;
      text-align: left; font-weight: 700; font-size: 10px;
      border: 1px solid var(--indigo); white-space: nowrap;
    }}
    .comparison-body table tbody td {{
      padding: 8px 10px; border: 1px solid var(--stone-mid);
      vertical-align: top; line-height: 1.5;
    }}
    .comparison-body table tbody tr:nth-child(even) td {{
      background: var(--stone-light);
    }}
    .comparison-body table tbody tr:hover td {{ background: #FAF8F2; }}
    .comparison-body table tbody td:first-child {{
      font-weight: 700; color: var(--indigo); background: #F8F5EE;
    }}
    .comparison-body code {{
      background: var(--stone-light); padding: 1px 6px; border-radius: 3px;
      font-size: 11px; font-family: 'Consolas', 'Monaco', monospace;
      color: var(--terracotta);
    }}
    .comparison-body pre {{
      background: var(--indigo); color: var(--stone-mid); padding: 12px 16px;
      border-radius: 4px; font-size: 11px; overflow-x: auto;
      line-height: 1.5; font-family: 'Consolas', 'Monaco', monospace;
    }}
    .comparison-body pre code {{
      background: transparent; color: inherit; padding: 0;
    }}
    .comparison-body ul, .comparison-body ol {{ padding-left: 1.6em; margin: 0.4em 0; }}
    .comparison-body li {{ margin: 0.3em 0; font-size: 12px; }}
    .comparison-body strong {{ color: var(--indigo); }}
    /* Override: keep bold text visible on dark backgrounds (table headers) */
    .comparison-body table thead th strong,
    .comparison-body table thead th b {{
      color: var(--white);
    }}
    .comparison-body table thead th {{
      color: var(--white);
      font-size: 11px;
    }}
    .comparison-body hr {{
      border: none; border-top: 1px dashed var(--stone-mid); margin: 24px 0;
    }}
    /* Wide tables overflow handling */
    .comparison-body {{ overflow-x: auto; }}

    /*  impact */
    .impact-grid {{
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;
      margin-bottom: 24px;
    }}
    .impact-card {{
      background: var(--stone-light); padding: 16px 18px; border-radius: 4px;
      border-top: 3px solid var(--terracotta);
    }}
    .impact-num {{ font-size: 22px; font-weight: 700; color: var(--sage); line-height: 1; }}
    .impact-card h3 {{ font-size: 13px; margin: 6px 0 8px; }}

    .fit-table {{ width: 100%; border-collapse: collapse; font-size: 12px; margin-bottom: 20px; }}
    .fit-table th {{
      background: var(--indigo); color: var(--white); padding: 10px;
      text-align: left; font-weight: 700; font-size: 11px;
    }}
    .fit-table td {{
      padding: 10px; border-bottom: 1px solid var(--stone-mid);
      vertical-align: top;
    }}
    .fit-table tr:nth-child(even) td {{ background: var(--stone-light); }}
    .eval-good {{ color: #1f7a4a; }}
    .eval-mid {{ color: #b58d2b; }}
    .eval-care {{ color: var(--terracotta); }}

    .actions-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 16px;
    }}
    .action-box {{
      background: var(--stone-light); padding: 14px 18px; border-radius: 4px;
    }}
    .action-box h4 {{
      font-size: 12px; color: var(--terracotta); margin: 0 0 8px;
      text-transform: uppercase; letter-spacing: 0.05em;
    }}

    /* Footer */
    .footer {{
      max-width: 1400px; margin: 40px auto 0;
      padding: 24px 36px 60px; color: var(--soft-gray); font-size: 11px;
      border-top: 1px solid var(--stone-mid);
    }}

    /* Responsive */
    @media (max-width: 1024px) {{
      .topic-body, .overview-grid, .impact-grid, .actions-grid {{
        grid-template-columns: 1fr;
      }}
      .layout {{ grid-template-columns: 1fr; }}
      .toc-sidebar {{
        position: relative; height: auto; max-height: 280px;
        border-right: none; border-bottom: 1px solid var(--stone-mid);
        display: none;
      }}
      .toc-sidebar.open {{ display: block; }}
      .toc-toggle {{ display: inline-block; }}
      .content {{ padding: 16px 16px 40px; }}
      .topic-section {{ padding: 18px 18px; }}
      .axis {{ grid-template-columns: 1fr; gap: 2px; }}
      .axis-label {{ font-size: 10px; }}
    }}

    @media print {{
      .topbar, .toc-sidebar, .toc-toggle {{ display: none; }}
      .layout {{ display: block; margin-top: 0; }}
      .content {{ padding: 0; }}
      .topic-section {{
        page-break-inside: avoid; break-inside: avoid;
        margin-bottom: 12px; box-shadow: none;
      }}
    }}
  </style>
</head>
<body>
  <header class="topbar">
    <button class="toc-toggle" onclick="document.querySelector('.toc-sidebar').classList.toggle('open')">☰ 目次</button>
    <div class="brand">
      AI NEWS VAULT
      <span class="sub">Topic Overview × Daily Highlights</span>
    </div>
    <nav class="nav-links">
      <a href="index.html">最新版</a>
      <a href="archive.html">アーカイブ</a>
      <span class="gen">Generated: {GEN_AT}</span>
    </nav>
  </header>

  <div class="layout">
    <nav class="toc-sidebar">
      <h3>目次</h3>
      <ol>{toc}</ol>
    </nav>
    <main class="content">
      {combined}
      {topics_html}
      {_html}
    </main>
  </div>

  <footer class="footer">
    <p>
      <strong>ai-news-vault</strong> — 13トピックを横断したAI業界の構造的潮流まとめ。
      <br>
      4/7/9/12時の Daily 自動取得時に再生成され GitHub Pages で公開されます(常に最新の Daily 反映)。
      <br>
      Last generated: {GEN_AT}
    </p>
  </footer>
</body>
</html>
"""

def main():
    root = Path(__file__).resolve().parent.parent
    out_dir = root / "docs"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"

    # 最新の daily/*.md を検出して解析
    latest = find_latest_daily_md(root)
    if latest is None:
        print("WARN: no daily/*.md found — falling back to hardcoded sample")
        daily_date = FALLBACK_DAILY_DATE
        daily_items = FALLBACK_DAILY_ITEMS
    else:
        daily_date, daily_items = parse_daily_highlights(latest, max_items=8)
        if not daily_items:
            print(f"WARN: failed to parse highlights from {latest} — falling back")
            daily_items = FALLBACK_DAILY_ITEMS
        else:
            print(f"Parsed {len(daily_items)} highlights from {latest}")

    out_path.write_text(build_page(daily_date, daily_items), encoding="utf-8")
    print(f"Saved: {out_path}")

if __name__ == "__main__":
    main()
