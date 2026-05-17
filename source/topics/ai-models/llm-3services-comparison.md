# 3大汎用 LLM 比較表 — Gemini / Claude / ChatGPT(GPT)

最終更新: 2026-05-11
性質: ユーザー要望(`notes.md`)に基づく「3サービスのバージョン別変化+競争状況の可視化」
表記: ✅=確定/公式 / 🟡=報道ベース / ⚠️=数字に幅あり

> notes.md の要望: 「**主要 LLM 3サービス(Gemini、Claude、ChatGPT)に絞った各モデル別バージョンアップの軌跡と、各バージョンアップで具体的にどの機能がどれだけ変化したのか**を一覧でまとめて整理&3サービスの競争状況を可視化したい」

---

## 0. 3サービスの「同じ世代」を並列表(2026-05時点フラッグシップ)

| 観点 | **OpenAI GPT-5.5**(2026-04-23) | **Anthropic Claude Opus 4.7**(2026-Q1) / **Mythos**(2026-04 限定) | **Google Gemini 3**(2026-Q1) |
|---|---|---|---|
| **位置付け** | 単一モデル+ルーター | Safety 重視+特化能力 | マルチモーダルネイティブ+垂直統合 |
| **推論モード** | 内蔵(ルーターで自動切替) | extended thinking(別モード) | Pro モード(自動切替) |
| **コンテキスト長** | 数百K〜1M クラス | 1M(Sonnet Plus 等) | 1-2M(継続拡張中) |
| **マルチモーダル** | テキスト+画像+音声+動画(統合) | テキスト+画像+音声(統合) | テキスト+画像+音声+動画(native) |
| **エージェント機能** | Codex CLI / Operator / Symphony 仕様 | Claude Code / Computer Use / Cowork | Gemini Enterprise Agent Platform |
| **限定能力モデル** | GPT-5.5-Cyber(信頼アクター限定) | Claude Mythos Preview(セキュリティ脆弱性発見) | (未公表の限定モデル) |
| **エンタープライズ強化** | AWS Bedrock 解禁(2026-04-29 以降) | Datadog 大口顧客、Claude Security ベータ | Spanner Omni、Agentic Data Cloud |
| **規制対応** | Bio Bug Bounty($25K)、Yubico 提携、Advanced Account Security | RSP、Trust Center | DeepMind「10の認知能力」AGI 評価フレーム |

---

## 1. バージョン別の軌跡(プロバイダ × 主要変化)

### 1.1 OpenAI GPT / o-series

| 世代 | 公開日 | 主要変化 | 効果(精度・速度・コンテキスト・マルチモーダル) |
|---|---|---|---|
| **GPT-3.5(ChatGPT)** | 2022-11-30 | 一般公開、対話形 LLM の幕開け | MMLU 70.0% / コンテキスト4K / テキストのみ |
| **GPT-4** | 2023-03-14 | 大規模スケール、画像入力初期対応 | MMLU 86.4% / 8K, 32K / 画像入力初期 / 司法試験模擬上位10% |
| **GPT-4 Turbo** | 2023-11-06 | コンテキスト拡大、価格1/3 | 128K / 知識2023-04 / 価格 1/3 |
| **GPT-4o**(omni) | 2024-05-13 | マルチモーダル統合、応答 232ms | テキスト+音声+画像 / 応答 232ms / 価格半減 |
| **GPT-4o mini** | 2024-07-18 | 軽量・低価格 | $0.15/$0.60 per 1M tokens |
| **o1-preview** | 2024-09-12 | **推論モード**(reasoning)幕開け | AIME 数学 83%(GPT-4o は 13%) |
| **o1 正式 / Pro** | 2024-12-05 | Pro($200/月)導入 | 思考時間トレード可能 |
| **o3 preview** | 2024-12-20 | ARC-AGI 87.5% 突破 | ARC-AGI 人間平均超え |
| **Operator** | 2025-01 | コンピュータ操作エージェント | ブラウザ操作・タスク自動化 |
| **GPT-4.5(Orion)** | 2025-02 | 事前学習スケーリング最終世代 | 知識広域、価格高 |
| **o3 / o4-mini** | 2025-04-16 | 推論モデル正式版 | reasoning モデルの完成 |
| **Codex CLI / Cloud agents** | 2025-05 | エージェント型コーディング | issue tracker → agent パターン |
| **GPT-5** | 2025-08-07 | **単一モデル+ルーター** | 推論/非推論を内部統合 |
| **GPT-5 Pro** | 2025-09 | Pro 派生 | 大量推論時間使用可 |
| **GPT-5.5** | 2026-04-23 | Codex Academy + Symphony 仕様同時公開 | エージェント・オーケストレーション仕様 |
| **GPT-5.5-Cyber** | 2026-04-30 | サイバー防御者限定リリース | 脆弱性検出能力(自主限定提供) |
| **Images 2.0** | 2026-04-29 | Thinking モード搭載画像生成 | 推論ベースの画像生成 |

### 1.2 Anthropic Claude

| 世代 | 公開日 | 主要変化 | 効果(精度・速度・コンテキスト・マルチモーダル) |
|---|---|---|---|
| **Claude 1** | 2023-03-14 | 一般公開、Constitutional AI | コンテキスト9K |
| **Claude 2** | 2023-07-11 | 大幅強化、長文対応 | **100K コンテキスト**(業界初) |
| **Claude 2.1** | 2023-11-21 | 200K コンテキスト | ツール利用初期 |
| **Claude 3 family**(Opus/Sonnet/Haiku) | 2024-03-04 | **3階層フォーマット標準化** | Opus が GPT-4 超え、画像入力対応 |
| **Claude 3.5 Sonnet** | 2024-06-20 | 中位が Opus 超え | HumanEval 92%、Artifacts UI |
| **Claude 3.5 Haiku** | 2024-07 | 軽量版更新 | 低レイテンシ |
| **Claude 3.5 Sonnet new + Computer Use** | 2024-10-22 | **PC 操作の汎用 AI** | エージェント時代の幕開け |
| **MCP**(Model Context Protocol) | 2024-11-25 | **ツール接続の業界標準** | エコシステム形成 |
| **Claude 3.7 Sonnet + extended thinking** | 2025-02-24 | **推論モード**追加 | SWE-bench Verified 70.3% |
| **Claude Code** | 2025-02-24 | CLI コーディングエージェント | ターミナル統合 |
| **Claude 4 Opus/Sonnet** | 2025-05-22 | **長時間自律実行を公式推奨** | 数時間のタスク自律実行 |
| **Claude 4.5** | 2025-Q3 | 増分強化 | エージェント信頼性向上 |
| **Claude Opus 4.7** | 2026-Q1 | フラッグシップ更新 | 高度推論+エージェント |
| **Claude Mythos Preview** | 2026-04-07 | **脆弱性発見能力(限定)** | 数千の脆弱性発見・攻撃コード生成 |
| **Claude Cowork** | 2026-04-09 | デスクトップエージェント一般提供 | PC 作業自動化 |
| **Claude × Adobe/Blender 等9コネクタ** | 2026-04-28 | クリエイティブ統合 | 反復作業自動化 |
| **Claude Security**(public beta) | 2026-04-30 | コード脆弱性検出+修正 | エンタープライズ向けセキュリティ AI |

### 1.3 Google Gemini

| 世代 | 公開日 | 主要変化 | 効果(精度・速度・コンテキスト・マルチモーダル) |
|---|---|---|---|
| **Bard**(LaMDA 系) | 2023-03-21 | プレビュー、出遅れ | テキスト対話、誤情報炎上 |
| **PaLM 2** | 2023-05-10 | Bard 改良 | コード/翻訳改善 |
| **Gemini 1.0**(Ultra/Pro/Nano) | 2023-12-06 | **マルチモーダル native 設計** | テキスト+画像+音声+動画 |
| **Gemini Advanced** | 2024-02-08 | Bard リブランド | Gemini Ultra 統合 |
| **Gemini 1.5 Pro** | 2024-02-15 | **1M トークン**(業界初の規模) | 動画・長文対応 |
| **Gemini 1.5 Flash** | 2024-05-14 | 軽量・高速 | Workspace 統合、低価格 |
| **Gemini 2.0 Flash** | 2024-12-11 | **マルチモーダル出力**(画像生成統合) | Project Astra エージェント |
| **Gemini 2.5 Pro** | 2025-03 | 推論モード+Deep Research | 強化推論、リサーチ自動化 |
| **Gemini 2.5 Flash/Flash-Lite** | 2025-04 | 軽量推論 | 低価格推論 |
| **Gemini 3 preview** | 2025-Q4 | 次世代フラッグシップ | 推論/マルチモーダル統合 |
| **Gemini 3 正式版** | 2026-Q1 | フラッグシップ完成 | エージェント+リアルタイム+10M 級コンテキスト |
| **Gemini Enterprise Agent Platform** | 2026-04-22 | **ローコードエージェント基盤** | 業務エージェント開発 |
| **Spanner Omni + Agentic Data Cloud** | 2026-04-22 | データ主権 × エージェント | オンプレ実行可能 |
| **Gemini in Cars** | 2026-04-30 | 車載 AI アシスタント | 数百万台展開 |
| **Gemma 4**(オープン) | 2026-05-03 | 無料・高品質日本語ローカル LLM | データ主権用途で強力 |

---

## 2. 機能軸別の3サービス比較進化(2022-2026)

### 2.1 コンテキスト長(トークン数)の競争史

```
2022-11  GPT-3.5: 4K
2023-03  GPT-4: 8K/32K    │ Claude 1: 9K           │ Bard: 数K
2023-07  ─                │ Claude 2: 100K(業界初) │ ─
2023-11  GPT-4 Turbo: 128K│ Claude 2.1: 200K       │ ─
2023-12  ─                │ ─                      │ Gemini 1.0: 32K
2024-02  ─                │ ─                      │ Gemini 1.5 Pro: 1M(業界初の100万)
2024-12  ─                │ ─                      │ Gemini 2.0 Flash: 1M
2025-02  ─                │ Sonnet Plus: 1M        │ ─
2025-04  ─                │ ─                      │ Gemini 2.5 Pro: 1-2M
2026-04+ GPT-5.5: 数百K-1M │ Opus 4.7: 1M           │ Gemini 3: 10M クラス
```
**勝者**: **Google Gemini**(1M を業界初、現在も最長級、10M クラス)
**追随**: Anthropic(Claude 2 で100K業界初の長文化、現在1M)
**3位**: OpenAI(数百K-1M、長文よりも推論性能で勝負)

### 2.2 マルチモーダル(画像+音声+動画)の競争史

```
2023      画像入力: GPT-4(限定) / Claude 3(2024-03)/ Gemini 1.0(native)
2024-02   動画入力: ─                                / Gemini 1.5 Pro(動画含む)
2024-05   GPT-4o: テキスト+音声+画像 native(232ms 応答)
2024-10   Computer Use(Claude): PC 操作
2024-12   Gemini 2.0 Flash: マルチモーダル出力(画像生成統合)
2026-04   GPT Images 2.0(Thinking モード)/ Claude × Adobe 9コネクタ / Gemini in Cars
```
**native 統合**: **Gemini**(設計思想で最も統合的)
**応答速度・対話**: **GPT-4o**(232ms の人間並み応答)
**クリエイティブ統合**: **Claude**(Adobe / Blender / Photoshop / Autodesk Fusion との9コネクタ)

### 2.3 推論モデル(reasoning)の競争史

```
2024-09  OpenAI o1-preview     ← 推論モデル幕開け、AIME 83%
2024-12  OpenAI o1正式 / o3 preview
2025-01  DeepSeek R1(OSS、参考)
2025-02  Anthropic Claude 3.7 Sonnet + extended thinking
2025-03  Google Gemini 2.5 Pro(推論モード)
2025-08  OpenAI GPT-5 ルーター方式(推論を内部統合)
2026-04  GPT-5.5 / Claude Opus 4.7 / Gemini 3(全社が「推論+非推論統合」へ)
```
**先行**: **OpenAI o1**(2024-09、業界初)
**追随**: Anthropic(2025-02 extended thinking、ON/OFF 切替)
**統合**: Google Gemini 2.5(推論モード)、OpenAI GPT-5(ルーター方式)

### 2.4 エージェント機能の競争史

```
2023-06  OpenAI Function Calling
2023-11  GPT-4 Turbo + GPTs
2024-04  Anthropic Tool Use(Claude)
2024-10  **Anthropic Computer Use**(汎用 PC 操作の幕開け)
2024-11  **Anthropic MCP**(業界標準プロトコル)
2025-01  OpenAI Operator(ブラウザエージェント)
2025-02  Anthropic Claude Code
2025-05  OpenAI Codex CLI + Cloud agents
2025-06  Anthropic Claude 4(長時間自律実行公式推奨)
2026-04  OpenAI Symphony 仕様(issue tracker → agent)
2026-04  Anthropic Claude Cowork(デスクトップエージェント一般提供)
2026-04  Google Gemini Enterprise Agent Platform(ローコード)
```
**先行**: **Anthropic**(Computer Use 2024-10、MCP 2024-11)
**ローコード基盤**: **Google**(Gemini Enterprise Agent Platform)
**コーディング特化**: **OpenAI**(Codex)、**Anthropic**(Claude Code)

### 2.5 価格・コスト効率の進化(API、$/1M tokens)

| モデル | 入力 | 出力 | 公開日 |
|---|---|---|---|
| GPT-4 | $30 | $60 | 2023-03 |
| GPT-4 Turbo | $10 | $30 | 2023-11 |
| GPT-4o | $5 | $15 | 2024-05 |
| GPT-4o mini | $0.15 | $0.60 | 2024-07 |
| Claude 3.5 Sonnet | $3 | $15 | 2024-06 |
| Claude 3.5 Haiku | $0.25 | $1.25 | 2024-07 |
| Gemini 1.5 Pro | $3.5 | $10.5 | 2024-02 |
| Gemini 1.5 Flash | $0.075 | $0.30 | 2024-05 |
| DeepSeek V3 | $0.14 | $0.28 | 2024-12 |
| GPT-5(参考) | (公開時の Pro$200/月) | — | 2025-08 |

**観察**:
- 1年で**1桁**のコスト低下が起きている
- フロンティアモデルは依然高価、軽量版(Flash / mini / Haiku)は急速に下落
- OSS(DeepSeek、Llama、Gemma)で「桁違いに安い」が常態化

---

## 3. 「同世代モデル」での競争位置(2026-05 時点フラッグシップ)

| 強み | OpenAI GPT-5.5 | Anthropic Claude Opus 4.7 / Mythos | Google Gemini 3 |
|---|---|---|---|
| **総合性能** | ★★★★★(総合型) | ★★★★(Safety + コーディング) | ★★★★(マルチモーダル+垂直統合) |
| **コーディング** | ★★★★(Codex Academy) | ★★★★★(Claude Code、SWE-bench先行) | ★★★(Code Assist) |
| **エージェント** | ★★★★(Symphony 仕様) | ★★★★★(Computer Use、MCP、Cowork) | ★★★★(Enterprise Agent Platform) |
| **長文・コンテキスト** | ★★★(数百K-1M) | ★★★★(1M) | ★★★★★(1-2M、10M クラス) |
| **マルチモーダル** | ★★★★(Images 2.0、Voice) | ★★★(画像、Adobe 連携) | ★★★★★(native、車載、医療) |
| **推論** | ★★★★★(ルーター統合) | ★★★★(extended thinking) | ★★★★(2.5 Pro) |
| **特化能力(限定)** | GPT-5.5-Cyber、Bio Bug Bounty | Mythos(脆弱性発見) | (DeepMind co-clinician) |
| **エンタープライズ** | ★★★★(AWS Bedrock 解禁) | ★★★★★(Datadog、Claude Security) | ★★★★★(Spanner Omni、Agentic Data Cloud) |
| **データ主権・オンプレ** | △ | △ | ★★★★(Spanner Omni、Gemma 4) |
| **オープン補完** | × | × | ★(Gemma 4) |
| **コンシューマー(チャット)** | ★★★★★(ChatGPT 圧倒) | ★★★(Claude.ai) | ★★★★(Gemini App、Bard 系) |

---

## 4. 3社の戦略の差(2026-05時点)

### OpenAI
- **戦略**: 「最大規模のフロンティア + 消費者 ChatGPT + Codex 開発者 + 規制対応」の総合型
- **強み**: ChatGPT のブランド・ユーザーベース、Codex Academy、ルーター方式の統合
- **弱み**: コーディング以外のエージェント領域で Anthropic に遅れ気味、データ主権ハードウェアなし
- **2026 動向**: AWS Bedrock 解禁(MS 独占解消)、Stargate でインフラ確保

### Anthropic
- **戦略**: 「安全性研究 + コーディング/エージェント現金化」の二刀流
- **強み**: Computer Use / MCP / Claude Code でエージェント領域先行、Mythos / Security で能力特化
- **弱み**: コンシューマー(ChatGPT 級ユーザーベース)、Pentagon 不在(地政学リスク)
- **2026 動向**: $50B 調達(評価 $850-900B 報道)、規制業界での Datadog 大口顧客化

### Google
- **戦略**: 「自社モデル + 自社データ + 自社ディストリビューション」の垂直統合
- **強み**: マルチモーダル native、Workspace/Search/Android/Cloud 統合、Gemma 4 でデータ主権
- **弱み**: 個別タスクでは OpenAI / Anthropic に追いつけない局面あり
- **2026 動向**: Gemini Enterprise Agent Platform、Spanner Omni、6プロトコル整理(中立リーダー)

---

## 5. 注目すべき構造的論点

1. **「Gemini はコンテキストとマルチモーダルで勝つが、Claude はエージェントで勝つ、ChatGPT は消費者で勝つ」** — 用途別の住み分けが安定化中
2. **3社全てが「限定能力モデル」を持つ**(Mythos / GPT-5.5-Cyber / co-clinician 等)— ガバナンス共通化
3. **オープン陣営(DeepSeek、Llama、Gemma)が3社の脅威に**: コスト効率 + ローカル運用で侵食
4. **「ルーター方式」と「extended thinking モード」のどちらが残るか**: GPT-5 と Claude のアプローチ差。Gemini は automatic
5. **長文コンテキストの実用限界**: 1M-10M 級が技術的に可能でも、実用利用率は依然 100K 未満が大半

---

## 6. 関連蓄積(他トピックの参照)

- `ai-companies/synthesis.md` — 各プロバイダの事業戦略・評価額
- `ai-companies/ma-timeline-2024-2026.md` — 資金調達と人材移動
- `llm-evaluation/synthesis.md` — ベンチマーク・解釈可能性・実タスク評価
- `agentic-ai/synthesis-2025.md` — エージェント能力の進化
- `ai-data-structuring/synthesis.md` — MCP・構造化出力・データ整備
- `ai-regulation/synthesis.md` — Mythos / GPT-5.5-Cyber 限定提供、distillation 訴訟
- `topics/ai-models/model-evolution-timeline.md` — 全プロバイダ年表(本ドキュメントの拡張版)

---

> 次回更新の触媒: 各社の新フラッグシップ発表時(Gemini 4、Claude Opus 5、GPT-6 等)、または重要な能力突破(AGI 級スコア達成、新ベンチマーク飽和等)
