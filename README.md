# ai-news-vault-public

[ai-news-vault](https://github.com/7green-lit) プロジェクトで生成された **AI業界トピック俯瞰ページ** を GitHub Pages で公開しています。

- 公開URL: <https://7green-lit.github.io/ai-news-vault-public/>
- 更新頻度: 毎日4/7/9/12時の Daily 取得時に自動再生成 + ソース MD 編集時にも GitHub Actions で自動再生成
- 構成: 全体俯瞰(3大潮流 + 本日のDaily)+ 14トピック1枚ずつ

---

## 共同編集者向けガイド

### 編集できるファイル

| 対象 | パス | 編集方法 |
|---|---|---|
| **Daily Digest 本文** | `daily/<YYYY-MM-DD>.md` | GitHub Web エディタ |
| **トピックの「自分の問い」** | `source/topics/<slug>/_index.md` | GitHub Web エディタ |
| **トピックの観察点 / 論点(分析)** | `source/topics/<slug>/synthesis.md` | GitHub Web エディタ |
| **3LLM 比較表(GPT/Claude/Gemini)** | `source/topics/ai-models/llm-3services-comparison.md` | GitHub Web エディタ |

### 編集手順(GitHub Web エディタ)

1. **編集したいファイルを開く**
   - 例:Daily 2026-05-15 → <https://github.com/7green-lit/ai-news-vault-public/blob/main/daily/2026-05-15.md>
2. 右上の **✏️(鉛筆アイコン)**をクリック → エディタモードに
3. 直接編集
4. 下部の「**Commit changes**」をクリック → コミットメッセージを書いて保存

### 編集が反映されるまで

- **`source/` 以下を編集した場合**: GitHub Actions が自動起動 → 数分後に `index.html` が更新
- **Daily MD を編集した場合**: 次の4/7/9/12時の Daily 実行で HTML に反映される(約1-4時間)

### 編集時の注意

- **`notes.md` と `strategy-hypothesis.md`** はリポジトリに含まれていません(ユーザー個人のワーキングメモリのため非公開)
- リンク先 URL が変わったり、フォーマット崩れがあれば Issue でお知らせください
- 構造を大幅に変更する場合は事前に管理者にご相談ください

### 議論・質問・要望

- Issues: <https://github.com/7green-lit/ai-news-vault-public/issues>

---

## 技術構成

- **GitHub Pages**: main ブランチのルートからホスト
- **GitHub Actions**(`.github/workflows/regenerate.yml`): `source/`、`daily/*.md`、`scripts/` への push で自動 HTML 再生成
- **ローカル daily_run.ps1**(管理者側): 4/7/9/12時に RSS 取得 + 分割 + HTML 再生成 + 自動 push
- **双方向同期**: ローカル変更と GitHub 上の collaborator 編集の両方を反映(mtime ベース)
- **フォント**: Noto Sans JP
- **カラーパレット**: Cream / Deep Indigo / Slate / Sage / Terracotta(落ち着いたトーン)
- **構造**: 1ページ目次型(縦スクロール)、レスポンシブ対応
