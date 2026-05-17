# AI活用のための構造化(データ・知識・スキーマ)

slug: `ai-data-structuring`
作成日: 2026-05-01

## 自分の問い

LLMを業務で機能させるためのデータ・知識・スキーマの「構造化」は
歴史的にどう積み上がり、現状どこまで来ていて、今後どう進むか。
特に業界別・業種別に進化が進むと考えられ、国内エンタープライズで何がボトルネックで、どんな突破口が見えているか。

## なぜこのトピックを立てるか

ニュースは「モデルの性能」「企業の評価額」「規制」に偏りがちだが、
**実用に効くかどうかは「モデルが触るデータ・知識・スキーマがどれだけ整っているか」で決まる**
ことが、2024-2026の導入事例の成否で繰り返し確認されている(MIT Tech Review
"Rebuilding the data stack for AI" 2026-04-27、"AI needs a strong data fabric"
2026-04-22 等)。地味だが ROI を分ける軸として継続蓄積する。

## キーワード

RAG / retrieval / vector database / knowledge graph / GraphRAG / structured output /
JSON mode / function calling / tool use / **MCP (Model Context Protocol)** / schema /
data fabric / データ基盤 / データレイクハウス / ETL / 文書構造化 / ontology / semantic /
embedding / chunking / Salesforce Headless 360 / Cloudflare Artifacts / Informatica /
Spanner Omni / Agentic Data Cloud

## 関連トピック

- `enterprise-ai`: 業務適用 / ROI(構造化はその前段)
- `agentic-ai`: エージェントの記憶・ツール接続(MCP / Artifacts)
- `ai-companies`: Salesforce / Cloudflare / Informatica / Datadog 等の構造化レイヤー提供者
- `llm-evaluation`: 解釈可能性ツール(Goodfire Silico)と構造化の接続
- `ai-regulation`: EU AI Act の透明性義務と「学習データ構造化」

## メモ・見解

[notes.md](notes.md) にユーザーの見解・仮説・違和感を蓄積。
次回 `synthesis.md` を再生成するときに `topic-curator` スキルが自動的に articles と統合する。

---

## 蓄積記事

(`articles/<日付>-<slug>.md` の形式で蓄積)

## 主要ドキュメント

- `synthesis.md` — **歴史(1970s〜2026)・現状(2026-04時点)・見通し** をまとめた基幹文書(モデル知識ベース+RSS蓄積のハイブリッド)
- 累計5記事到達でこの synthesis を全面再構成(`topic-curator` の `synthesis_update_interval`)

## 履歴

- 2026-05-01: トピック作成、`synthesis.md` 初版執筆、6記事を初期蓄積(累計6件)
  - [Rebuilding the data stack for AI(MIT Tech Review)](articles/2026-04-27-mit-rebuilding-data-stack.md) — `reinforces`
  - [AI needs a strong data fabric(MIT Tech Review)](articles/2026-04-22-mit-data-fabric-ai.md) — `reinforces`
  - [アクセンチュア×SAP「ADVANCE」国内本格展開](articles/2026-04-30-accenture-sap-advance-japan.md) — `new_angle`(国内最終マイル投資)
  - [Salesforce Headless 360 — 全機能を API/CLI/MCP で](articles/2026-04-19-salesforce-headless-360-mcp.md) — `new_angle`(SaaS側のMCP対応先行)
  - [Cloudflare Artifacts — AIエージェント向けFS](articles/2026-04-19-cloudflare-artifacts-agent-fs.md) — `new_angle`(エージェント記憶層)
  - [Google Cloud Next 2026 — Agentic Data Cloud / Spanner Omni](articles/2026-04-22-google-cloud-spanner-omni-agentic-data.md) — `new_angle`(データ+エージェント縦断戦略)
- 2026-05-01: 累計6件で `synthesis_update_interval=5` を超えているが、初版 synthesis.md は今日執筆済みのため次回更新は累計10件で実施予定
- 2026-05-01(午後): 国内強化フィードからさらに4記事追加(累計10件、しきい値到達 → synthesis.md を再構成)
  - [オラクルCEO「最高のAIは最高のデータが支える」](articles/2026-05-01-oracle-ceo-best-ai-best-data.md) — `reinforces`(国内データ主権論)
  - [MCP/A2A/UCP/AP2 — 6プロトコル乱立の整理(@IT)](articles/2026-05-01-mcp-a2a-ucp-ap2-protocol-proliferation.md) — `reinforces`(MCPの分裂リスクが現実化)
  - [アジアクエスト、Databricks SI コンサルティングパートナー認定](articles/2026-05-01-asiaquest-databricks-si-partner.md) — `new_angle`(国内 SI 経由の Databricks 攻勢)
  - [富士ソフト、AI時代の SIer 新体制(人月商売脱却)](articles/2026-05-01-fujisoft-sier-new-business-model.md) — `new_angle`(国内 SI ビジネスモデル変革)
- 2026-05-04: 5/2-5/3 ダイジェストから2記事追加(累計12件、次回 synthesis 更新は累計15件)
  - [アクセンチュア × 日本精工(NSK)、AI で間接業務改革と製造現場自動化](articles/2026-05-03-accenture-nsk-manufacturing-ai.md) — `new_angle`(製造業 Last Mile)
  - [東京都 × ソウル市、AI・データ基盤行政で業務協約](articles/2026-05-02-tokyo-seoul-ai-data-government-mou.md) — `new_angle`(自治体間 AI 連携)
- 2026-05-05: 蓄積指示で1記事追加(累計13件)
  - [MIT Tech Review Operationalizing AI — データ主権 × AI 運用](articles/2026-05-02-mit-operationalizing-ai-data-sovereignty.md) — `reinforces`
- 2026-05-11: notes.md ユーザー中心仮説(MCP × 文脈含む構造化 = Anthropic スキル、業界別パターン化)を本 synthesis の中核に格上げ
  - v3 増分付録: 「PDF 構造化 → 文脈構造化(スキル化)」進化軸、業界別文脈構造化進度マップ、海外との差異
- 2026-05-11(午後): 5/5-5/11 ダイジェストから3記事追加(累計16件、しきい値超え → 次回 synthesis.md v4 再生成候補)
  - [IBM Sovereign Core 一般提供開始 — AI 時代のデジタル主権基盤](articles/2026-05-11-ibm-sovereign-core-launch.md) — `reinforces`(IBM CEO 発言の製品化)
  - [Fivetran「エージェント型 AI 準備状況指数」2026年版発表](articles/2026-05-08-fivetran-agentic-ai-readiness-index.md) — `new_angle`(AI Readiness 指標化潮流)
  - [ファナック・安川電機もフィジカル AI、国産基盤で情報資源死守](articles/2026-05-11-fanuc-yaskawa-physical-ai-japan.md) — `new_angle`(製造×AI×データ主権の3軸)
