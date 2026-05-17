# Agentic AI — 2025年動向レビュー(v2、notes.md 反映)

最終更新: 2026-05-11(v2、notes.md の3問いを反映した増分付録 v2 追加)
性質: モデル知識ベースの年次総括 + ユーザー notes の問いへの応答セクション

## 自分の問い(再掲)

AIエージェントは「デモから実用」へどう移行していくか。
信頼性・コスト・人間との協調設計の観点で何が成功要因か。

---

## v2 増分付録 — notes.md の3問いへの応答

ユーザーが notes.md に書いた**3つのもっと知りたい論点**に応える追加セクション。

### 付録 A: Anthropic / OpenAI / Google の公式エージェント運用ガイドライン(2026-05-11時点要約)

#### A.1 Anthropic「Building effective agents」(基本指針、随時更新)

- **設計原則**: シンプルなパターンから始める(LLM × ツール × メモリの最小構成)、複雑な「自律エージェント」より「**ワークフロー + LLM**」が多くのケースで上回る
- **主要パターン**: Prompt Chaining、Routing、Parallelization、Orchestrator-workers、Evaluator-optimizer、**Agents(本格自律実行)**
- **Computer Use(2024-10〜)**: PC 操作の汎用エージェント、Computer Use Tool API
- **Claude Code(2025-02〜)**: ターミナル統合、長時間自律実行(2025-06 Claude 4 で公式推奨)
- **Cowork(2026-04-09〜)**: デスクトップエージェント、有料プラン全ユーザー
- **Claude Security(2026-04-30 PB)**: コード脆弱性検出+修正のエンタープライズ向けエージェント
- **Mythos(2026-04 限定)**: 数千の脆弱性発見+攻撃コード生成能力、信頼アクター限定
- **MCP(2024-11 公開、業界事実標準)**: ツール接続プロトコル
- **Responsible Scaling Policy(RSP)**: 能力レベル別の運用ガード
- **長時間自律実行の推奨**: 数時間スケールのタスクは「サブエージェント分割」「中間レビュー」「Cost cap」「Rollback path」を必須

#### A.2 OpenAI「Practical guide to building agents」(2025 更新、Codex Academy 内)

- **基本3要素**: Model + Tools + Instructions
- **オーケストレーション**: 「Single-agent ループ」を起点、複雑化したら「Manager + Workers」へ
- **GPT-5(2025-08)以降**: 推論モデル(o1/o3 系)を内部統合した**ルーター方式**、エージェントが自動的に reasoning モードに切替
- **Operator(2025-Q1〜)**: ブラウザ操作エージェント、商用提供
- **Codex CLI / Cloud Agents(2025-05〜)**: コーディング特化、issue tracker 連携
- **【v2 重要】Symphony 仕様(2026-04-23 GPT-5.5 と同時発表)**: issue tracker → agent の標準仕様(下記 B 詳述)
- **Codex Academy(2026-04-23)**: 10章の運用教材
- **Advanced Account Security + Yubico**: エージェント認証の Hardware Key 統合(2026-04-30)
- **GPT-5.5-Cyber(2026-04-30)**: 信頼アクター限定提供
- **Preparedness Framework**: 能力評価+運用制限の枠組み

#### A.3 Google DeepMind / Google Cloud「Gemini Enterprise Agent Platform」(2026-04-22 発表)

- **ローコード基盤**: 業務エージェントをローコードで構築
- **Agentic Data Cloud(2026-04-22)**: AWS DB / Azure DB / SaaS を横断統合
- **Spanner Omni**: オンプレ実行可能 RDB、エージェントのデータ基盤
- **6プロトコル整理(2026-04-30)**: MCP / A2A / UCP / AP2 / A2UI / AG-UI を Google が解説、業界標準化に介在
- **DeepMind「10の認知能力」AGI 評価フレーム(2026-04-30)**: エージェント能力を認知科学ベースで測定
- **DeepMind co-clinician(2026-04-30)**: 医療補助エージェント、特化ユースケース提供
- **Gemini in Cars(2026-04-30)**: 車載 AI アシスタント

#### A.4 3社のガイドラインの共通点・相違点

| 観点 | Anthropic | OpenAI | Google |
|---|---|---|---|
| **「シンプルから始める」原則** | 強調(Building effective agents) | 強調(Practical guide) | あまり明示せず |
| **マルチエージェント設計** | Orchestrator-workers パターン | Manager-workers | Agent Engine + ローコード |
| **長時間自律実行** | Claude 4 で公式推奨 | Codex Cloud で実装 | Gemini Enterprise Agent Platform |
| **限定能力モデル** | Mythos(限定提供) | GPT-5.5-Cyber(信頼アクター) | (限定モデル未公表) |
| **ツール接続** | MCP(業界事実標準を提唱) | Function Calling、Symphony | 6プロトコル整理(中立リーダー) |
| **エンタープライズ** | Trust Center、Claude Security | Bedrock 解禁、Account Security | Spanner Omni、Agentic Data Cloud |
| **解釈可能性** | Mechanistic Interpretability 研究 | (限定的) | DeepMind AGI 評価フレーム |

**共通の構造**: 3社とも「**シンプル設計 → マルチエージェント協調 → 長時間自律実行 → 限定能力モデル**」の進化パス。**MCP + 自社プロトコル拡張**が共通の競争ポイント。

---

### 付録 B: OpenAI Symphony 仕様の詳細(notes.md ユーザー問い)

> ユーザーの問い: 「2026年4月時点で OpenAI が Symphony を発表し『issue tracker→agent』の標準仕様を提案、再競争のラウンドが始まった」という点が理解できず、issue tracker→agent の仕様はどんな内容で他と何が違うのか?

#### Symphony 仕様の概要

- **発表**: 2026-04-23(GPT-5.5 と同時)、OpenAI 公式「open-source spec for orchestration: Symphony」
- **基本コンセプト**: **「issue tracker をエージェントへの入力源・進捗追跡先として使う」**標準仕様
- **具体的な動作**:
  1. 開発者が GitHub Issues / Linear / Jira などの**issue を作成**
  2. Symphony 対応エージェント(Codex Cloud Agent 等)が **issue を自動的に取得・解析**
  3. エージェントが**コードを書き、PR を作成、issue にコメントで進捗報告**
  4. 完了時に issue を自動的にクローズ
- **オープン仕様**: OpenAI 主導で公開、他社実装も歓迎(GitHub Actions 拡張、Linear 公式統合、Cursor 等が対応予測)

#### 他の仕様との違い

| 仕様 | スコープ | 主な対象 | 提唱者 |
|---|---|---|---|
| **MCP**(2024-11) | LLM ⇄ ツール / リソース接続 | ツール提供者・LLM 提供者 | Anthropic |
| **Symphony**(2026-04) | **issue tracker ⇄ agent** | 開発組織・コーディングエージェント | OpenAI |
| **A2A**(Agent-to-Agent) | エージェント間通信 | エージェントオーケストレーター | Google |
| **AGNTCY** | エージェント間通信(対抗) | OSS コミュニティ | Cisco Outshift |
| **AP2 / UCP / A2UI / AG-UI** | 個別シナリオ別 | 用途別 | 各社 |

#### Symphony の戦略的意義

- **「ソフトウェア開発ワークフローへのエージェント常駐化」**を狙う仕様
- 既存の開発組織のワークフロー(issue 駆動の開発)を**そのまま使える**ので採用障壁が低い
- **Cognition Devin、Claude Code、Cursor との競合**: これらはエージェント側の実装、Symphony は**統合プロトコル側**
- **「issue を作るだけでエージェントが完成させる」**フローが標準化されると、エンジニアの作業は**issue を書くこと**にシフト

---

### 付録 C: SWE-bench 飽和後の評価軸(notes.md ユーザー問い)

> ユーザーの問い: 「SWE-bench 飽和後の評価軸」について、これまでどんな評価軸・評価方法があって、現状ある代替の評価軸・方法を知りたい

#### C.1 これまでの主要評価軸(2022-2025)

| 時期 | 主要ベンチマーク | 評価対象 | 飽和状況 |
|---|---|---|---|
| 2022-2023 | **MMLU**(Massive Multitask Language Understanding) | 一般知識・推論 | GPT-4 で 86%、現在 90% 超で飽和 |
| 2022-2024 | **HumanEval**(コーディング) | Python 関数生成 | GPT-4 で 67%、Claude 3.5 Sonnet で 92%、飽和 |
| 2023-2024 | **GSM8K**(数学) | 小学算数文章題 | GPT-4 で 92%、現在 95%+ で飽和 |
| 2023-2024 | **HellaSwag**(常識推論) | 文脈完成 | GPT-4 で 95%、飽和 |
| 2024 | **MATH**(競技数学) | 高校数学 | o1 で 94%、GPT-5 でほぼ完璧、飽和 |
| 2024-2025 | **SWE-bench Verified**(実プロジェクト修正) | GitHub issues 解決 | **2025-中盤で 70% 超が当たり前、差別力低下** |
| 2024-2025 | **ARC-AGI** | 抽象推論パターン | o3 が 87.5% で人間平均超え、飽和に近づく |
| 2025-2026 | **AIME**(数学コンテスト) | 大学レベル数学 | o1で83%、o3で 95%+、飽和 |

#### C.2 SWE-bench 飽和後の代替評価軸(現状の主役)

| ベンチマーク/方法 | 評価対象 | 特徴 | 主要プレイヤー |
|---|---|---|---|
| **TAU-bench** | 顧客サポートタスク全工程 | 業務ドメイン縦断、ツール利用評価 | 学術+各社 |
| **OSWorld** | GUI 操作のエンドツーエンド | デスクトップ操作の難しさを測定 | 学術+Anthropic Computer Use |
| **GPQA Diamond** | 大学院レベル科学(物理/化学/生物) | 知識・推論を実用学術タスクで測定 | OpenAI 等 |
| **HLE(Humanity's Last Exam)** | あらゆる分野の専門家レベル設問 | 飽和しにくいよう構築 | Center for AI Safety |
| **MMLU-Pro** | MMLU の難化版 | より深い推論を要求 | 学術 |
| **企業独自の閉鎖ベンチマーク** | 自社業務の実タスク | 公開せず自社採用判断に使う | 各エンタープライズ |
| **実タスク評価(Choco Aconnect、SMBC 提案書等)** | 実業務での効果検証 | 数値だけでなく ROI、ユーザー満足度 | 実装企業 |
| **解釈可能性ベース評価(Goodfire Silico)** | モデル内部のメカニズム観察 | 「なぜその答えに到達したか」を測定 | Goodfire 等の専門ベンダー |
| **DeepMind「10の認知能力」AGI 評価フレーム** | 認知科学ベースの能力分解 | 「どの能力が、どの程度ある」を構造化 | DeepMind(2026-04-30 発表) |
| **生物学/化学/サイバー特化評価**(Anthropic BioMysteryBench、OpenAI Bio Bug Bounty) | 危険能力の検出+制限 | 規制対応と能力測定の統合 | Anthropic、OpenAI |

#### C.3 評価のパラダイムシフト(SWE-bench 飽和の本質的意味)

1. **公開ベンチマーク → 組織内ベンチマーク**: 各企業が自社業務で測定、外部公表せず採用判断に使う
2. **数値スコア → 業務 ROI**: 「正答率」より「業務効率化%」「顧客満足度」「コスト削減額」
3. **静的タスク → 動的環境(エージェント評価)**: 単一質問への回答ではなく、**ツール利用・複数ステップ・例外対応**を評価
4. **能力測定 → 安全性測定の同時化**: 高能力モデル(Mythos / Cyber)では「能力を測ると同時に危険性を測る」
5. **モデル単体 → エコシステム評価**: モデル + ツール + ガードレール + 運用設計の総合パフォーマンス

#### C.4 国内文脈

- **Sakana×SMBC 提案書効果**(1〜2週間→数十分)は実タスク評価の好例
- ** JSAI2026 論文**「複雑文書読解 VLM の限界」は**企業特化文書での評価**
- **Harvard ER 診断 AI が人間医師2名より正確**は実タスク評価の先進事例(2026-05-03)

---

## v2 増分の関連蓄積

- [Bloomberg「AI 疲れ」(2026-05-04)](articles/2026-05-04-bloomberg-ai-fatigue-claude-second-brain.md) — Claude 第二の脳・人間の認知負荷
- ai-models/llm-3services-comparison.md — 3社比較(本付録 A の元データ)
- ai-models/model-evolution-timeline.md — 全プロバイダ年表
- llm-evaluation/synthesis.md — ベンチマーク評価の詳細

---

---

## 1. 2025年の構造変化(3つ)

### A. 「単発タスク」から「長時間自律実行」へ
- 2024年10月の Anthropic Computer Use は「PC を操作するデモ」レベル。
- 2025年2月の Claude Code、その後の Claude 4 系で**数時間〜半日の連続実行**が公式推奨ユースケースに。
- 2025年後半までに「24時間自律で動くエージェント」の事例(OpenAI Operator、xAI Grok Agent、Manus)が常態化。
- ただし「長時間=高品質」ではない。長くなるほどコンテキスト圧縮、サブエージェント分割、自己訂正ループが必須になり、設計コストが指数的に増加した。

### B. MCP のデファクト標準化
- 2024年11月の Anthropic MCP(Model Context Protocol)公開が、2025年中盤までに OpenAI / Google / Microsoft も対応する**異例の業界統一**を実現。
- これは LLM とツール接続のレイヤーで OAuth に相当するインフラ層を作った意味で、2025年の最も静かな勝利。
- 副作用: MCP サーバーが数百規模で乱立し「どれが安全か」のキュレーション課題が発生。Cloudflare Artifacts(2026-4)などが「セキュアなホスティング」基盤として登場。

### C. コーディングエージェントの覇権争いが「IDE +モデル+クラウド」三層に
- **IDE(統合開発環境) 側**: Cursor、Windsurf(後 Codeium)、Zed、VS Code(GitHub Copilot)、Replit
- **モデル側**: Claude(Anthropic)、GPT(OpenAI Codex)、Gemini Code Assist、DeepSeek
- **エージェント・オーケストレーション側**: Claude Code(CLI/IDE)、Devin(Cognition)、Codex CLI(OpenAI)、Aider(OSS)
- 2025年中盤までに「IDE は中立、モデルは選択可能、Agent runner は OS 寄り」という形が定着。**2026年4月時点で OpenAI が Symphony を発表**し「issue tracker→agent」の標準仕様を提案、再競争のラウンドが始まった。

---

## 2. 2025年のマイルストーン(時系列ハイライト)

| 時期 | 出来事 | 意味 |
|---|---|---|
| 2025-01 | DeepSeek R1 リリース | OSS reasoning model のショック。「エージェントの脳」を低コスト化する道筋が見えた |
| 2025-01 | Stargate 発表($500B) | エージェント運用のための長期コンピュート確保 |
| 2025-01-02 | OpenAI Operator | ブラウザ操作エージェントの初期一般提供 |
| 2025-02 | Anthropic Claude Code 一般提供 | ターミナル常駐エージェントの本格普及 |
| 2025-03 | Manus(中国 Monica)バズ | 「Devin より使いやすい」と話題になった汎用エージェント |
| 2025-Q2 | Replit Agent / Cursor v0.x → v1 | プロトタイピングのデフォルト体験変化 |
| 2025-06 | Anthropic Claude 4 Opus / Sonnet | 長時間自律実行を初めて公式推奨 |
| 2025-Q3 | サブエージェント / Multi-agent パターン公式化 | Anthropic / OpenAI 両社がベストプラクティスとして文書化 |
| 2025-08 | OpenAI GPT-5 | 単一モデル+ルーターでモード切替を内包、エージェント側は単純化 |
| 2025-Q4 | TAU-bench / OSWorld 等のエージェント特化ベンチマーク本格普及 | 「SWE-bench 飽和」を経て次の評価軸が確立 |
| 2026-01 | OpenAI Codex Academy / Symphony | エージェント教育・運用のメソドロジ標準化 |
| 2026-04 | Claude×Cursor DB 全削除事件 | 「エージェントは事故を起こす」が世論レベルに |
| 2026-04 | Anthropic Cowork 一般提供 | デスクトップ常駐エージェントが Claude 有料層へ |
| 2026-04 | Cloudflare 自律ドメイン購入機能 | エージェントが組織的に稼働するインフラ整備 |

---

## 3. 主要論点(現時点での仮説)

### 論点1: 「信頼性」は仕様で解決できるのか、ガバナンスでしか解決できないのか
- 2025年中盤までは「モデル能力向上で事故が減る」という楽観論。
- 2026年4月の Claude×Cursor DB 削除事件で、**能力の高さが事故の規模を拡大する**という構造が顕在化。
- 現時点での合意点: **権限の細分化**(ファイルシステム / ネットワーク / DB 操作の個別承認)と**ロールバック前提**(全操作にアンドゥパス)が必須。
- 未解決: 連続実行を止めずに権限を絞ると生産性が落ちる、という根本トレードオフ。

### 論点2: コスト構造が「予測可能 SaaS」と相性が悪い
- Claude Code が 2026-4 に推奨予算見積もりを倍増させた事例が象徴的。
- エージェントは**思考トークンを消費する**ため、人間1人作業の十数倍のトークンが必要なケースも珍しくない。
- 業界の対応:
  - 上限付き定額(Cursor、Claude の各プラン): 軽量利用者には魅力、重量利用者には不足。
  - 従量課金(Anthropic API、OpenAI API、AWS Bedrock): 予算管理が組織に重い。
  - **2026年Q1 時点で「ハイブリッド」(seat 上限 + 超過分 metered)が主流化**。

### 論点3: 「人間との協調設計」は単独設計より遅れている
- 2025年は「自律時間を伸ばす」競争で、UI / UX 側は後回し。
- 2026年に入り、**長時間タスクの中間レビュー**(Anthropic の thinking sharing、OpenAI の Codex のステップ表示)、**人間の差し戻し方の標準**(approval / reject / amend / restart)が整備期に。
- 特に**「あと何分かかるか」の予測**が信頼の起点。これができない UX は continued use されない。

### 論点4: SWE-bench 飽和後の評価軸
- 2025年中盤までに SWE-bench Verified で 70%+ が当たり前になり、評価としての差別力を失った。
- 代替として:
  - **TAU-bench**: 顧客サポートタスクのドメイン縦断評価。
  - **OSWorld**: GUI 操作のエンドツーエンド評価。
  - **企業独自の閉鎖ベンチマーク**: 各社内部で「自社業務での成功率」を測定し、外部公表せず採用判断にだけ使う。
- 評価指標自体が**「公開ベンチ」から「組織内ベンチ」へ重心移動**しているのが2025-2026の最大の変化。

---

## 4. 成功パターン(2025年中盤以降に見えてきた)

1. **狭く深い**: コードレビュー専用、特定 SaaS ワークフロー専用、特定の言語・フレームワーク専用。汎用エージェントより成功率が高い。
2. **人間の差し戻しを設計の中心に置く**: 「自律で完走」ではなく「8割完走 + 人間の最終承認」を前提にしたツールが定着率高い。
3. **タスク粒度の標準化**: 1 タスク = 5〜30分の作業を、エージェントが30秒〜数分で処理する粒度。これより大きいと事故、小さいと使う意味がない。
4. **コスト透明性**: 「このタスクは平均 $0.X」を事前に示すツールが信頼を獲得。

## 5. 失敗パターン(避けるべき設計)

1. **エンドツーエンド完全自律を売りにする**: 2024-2025年の Devin が代表的。デモは強いが運用に移せない。
2. **すべてのツールを「ペルソナ化」する**: 営業エージェント、CFO エージェント、CTO エージェント等の擬人化系。タスク粒度が肥大化して制御不能。
3. **トークン消費を隠す UX**: ユーザーが事後請求でショックを受け、解約する典型パターン。

---

## 6. まだ分かっていないこと

1. **長時間自律実行(数時間以上)の事故率の現実値**は公開されていない。各社の事例は selection bias がかかっている可能性が高い。
2. **エージェントの「停止条件」**: タスク完了 / 失敗 / 予算超過 / タイムアウト の4軸以外に、「自分が間違っているかもしれない」という自己疑念で止まれるか、はまだ研究段階。
3. **複数エージェントの協調**(チーム編成、衝突解決、リーダー交代)は理論先行で実用化はこれから。
4. **法的責任の構造**: エージェントが第三者に損害を与えた場合、モデル提供者 / IDE 提供者 / 利用者 / 雇用主のどこに責任が発生するか、判例ほぼなし。

---

## 7. 次に追うべきソース・キーワード

- Anthropic / OpenAI / Google の **公式エージェント運用ガイドライン**(随時更新される)
- **TAU-bench / OSWorld** のリーダーボード変動
- **MCP サーバーのキュレーション**(Cloudflare、GitHub、Anthropic 公式リスト)
- **エージェント保険 / 監査**ベンダーの登場(現時点でほぼゼロだが2026年中に出現する可能性)
- **「エージェント インシデント レポート」**: 業界全体での事故公開の動き(航空 / 医療 のインシデント開示モデルを参考にした議論あり)
- DeepMind の認知能力フレームワーク(2026-4 発表)とエージェント能力評価への展開

---

## 8. 個別記事として深掘りしたい候補

このレビューを契機に、以下の個別記事を `topics/agentic-ai/articles/` に蓄積する候補とする(`topic-curator` スキルが起動された際の出発点):

- Claude×Cursor DB削除事件の詳細(The Guardian、Tom's Hardware)
- Cloudflare Artifacts / Email Service / 自律ドメイン購入(2026-4)
- Anthropic Cowork 一般提供(2026-4)
- OpenAI Symphony 仕様(2026-4)
- Google Gemini Enterprise Agent Platform(2026-4)
- DeepSeek R1 / V4 のエージェント文脈での影響
- Devin 開発元 Cognition AI 日本法人設立(2026-4)
- Anthropic の Claude Code トークン見積もり倍増(2026-4)

---

## 9. v3 増分付録(2026-05-11): エージェントの「自己進化」「内部解釈可能性」「ローカル化」

### 蓄積記事(累計7→10件)
- [Claude Managed Agents「dream」機能](articles/2026-05-06-claude-managed-agents-dream.md) — `new_angle`
- [LINE ヤフー AI エージェント「Agent i」](articles/2026-05-11-line-yahoo-agent-i.md) — `new_angle`
- [Anthropic Natural Language Autoencoders](articles/2026-05-08-anthropic-natural-language-autoencoders.md) — `new_angle`

### 9.1 「dream」機能 — エージェント休止時の振り返り学習
v2 までは「エージェントの長期記憶」議論は **Cloudflare Artifacts**(エージェント FS)+ **MCP プロトコル**(外部ツール接続)+ **OpenAI Symphony**(issue tracker 標準仕様)の3層で進行していた。

**v3 で追加される新軸**: **「dream」(2026-05-06、Claude Managed Agents)**は**エージェントが休止中に過去タスクを振り返り学習・最適化**する第4層。

**意義**:
- **「メモリ」から「内省」へ**: Artifacts が外部ファイル、MCP が外部ツール、Symphony が公式ワークフロー、dream が**内省的最適化**
- **計算コスト設計**: 休止中とは言え推論コストは発生、稼働率設計の新課題
- **「学習権」問題**: 顧客データを「dream」で学習する場合のデータ主権論
- **悪用リスク**: Claude メキシコ攻撃(2026-05-08)で dream が**攻撃ツールの自己改良**に応用される可能性
- 競合: OpenAI Symphony、Google Gemini Enterprise Agent、Anthropic Cowork が**同様の自己改善層**を導入するか

### 9.2 Natural Language Autoencoders — エージェントの「内部独白」を可視化
v2 までの解釈可能性議論は **Goodfire Silico**(機械的解釈)、**Anthropic Skills**(振る舞い指示)中心。

**v3 で追加**: Anthropic **Natural Language Autoencoders**(2026-05-07)が **Claude の内部思考を自然言語に復号**。**エージェント挙動の「意図レベル」検査**が可能に。

**意義**:
- **デバッグツール化**: エージェントの誤動作を「意図」レベルで分析
- **規制対応**: EU AI Act / 日本 AI 法律(2026-05-11)の「説明可能性」要件への技術的解
- **Claude 脅迫行動研究(2026-05-09)、メキシコ攻撃(2026-05-08)** の解明手段
- **PocketOS 9秒破壊事件(2026-04)** の根本原因(権限分離不足)を「**意図解析**」で予防可能に
- **エージェント運用ガイドラインへの組込**: Appendix A の3社ガイドラインが Autoencoder ベースの透明性義務へ進化する可能性

### 9.3 LINE ヤフー Agent i — 国内データ寡占型エージェントの参戦
v2 までの議論はグローバル AI 大手(Anthropic、OpenAI、Google)+ 国内 SI(Cognition AI 日本法人、PFN、Sakana)中心。

**v3 で追加**: **LINE ヤフー Agent i**(2026-05-11)が**ユーザーデータ寡占の優位性**で参戦。9,000万 MAU からワンタップで AI エージェント利用、PayPay 決済、Yahoo! ショッピングデータが直接活用可能。

**意義**:
- **「ユーザー文脈の囲い込み」**: Perplexity Personal Computer(2026-05-08)、Claude in Chrome(2026-05-11)、ChatGPT Atlas に対する**国内データ層**で対抗
- **エージェント MAU 規模競争**: 性能差を補う**個人データ × エージェント**の戦略
- **NEC × Anthropic(同日)** との棲み分け: NEC が B2B、LINE ヤフーが B2C
- **OpenClaw(2026-05-11)** との対比: スーパーアプリ × エージェント vs OSS 個人開発者
- **日本初 AI 法律(同日)** が個人向けエージェントの規制設計を要請する圧力

### 9.4 v3 統合視点 — agentic-ai が「成熟期」入り
| 軸 | v1 (2026-04 まで) | v2 (2026-05-04 まで) | v3 (2026-05-11) |
|---|---|---|---|
| メモリ層 | Cloudflare Artifacts | Artifacts + MCP | Artifacts + MCP + dream(内省) |
| 解釈可能性 | Goodfire Silico | Skills + ガイドライン | Natural Language Autoencoders(内部独白) |
| ガバナンス | PocketOS 教訓 | 3社ガイドライン公式化 | JetBrains Central + 日本 AI 法律 |
| 評価軸 | SWE-bench 飽和 | TAU/OSWorld/GPQA/HLE | + dream 効果評価 + 実エンタープライズ ROI |
| 国内勢 | Cognition 日本法人 | Sakana × SMBC | LINE ヤフー Agent i、NEC × Anthropic |

**結論**: 2026-05-11 は agentic-ai トピックが「**自己進化(dream) × 内部解釈可能性(Autoencoder) × ユーザー文脈囲い込み(Agent i)**」の3軸で**成熟期入り**したマイルストン。次回 v4 候補:
- 「dream + Autoencoder の組合 = 自己最適化 + 内省検査」のセキュリティ含意
- LINE ヤフー Agent i 等の**消費者向けエージェント MAU 競争**の構図
- Claude メキシコ攻撃事件後の**エージェント武器化**規制の具体化(国際協調が必要か)

---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> メモリ・解釈可能性・ユーザー文脈寡占の3軸でエージェントが成熟期入り。標準化はいつ完成するか。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: 記憶層は「外部記憶 + ツール接続 + 内省」の3層化で長期記憶問題が技術的に解決へ

**概要**:
- Artifacts(外部FS)+ MCP(ツール)+ dream(内省学習)で多層化
- 計算コスト設計・データ主権・武器化リスクが新規論点として浮上
- Claude メキシコ攻撃の自己改良パターンと正反対の「自己改善」が共存

**事例詳細**:
- Claude Managed Agents「dream」機能(2026-05-06)
- Cloudflare Artifacts(エージェント FS、2026-04-19)
- OpenAI Symphony issue tracker 標準仕様(2026-04)

#### 観察2: 解釈可能性層は「内部独白の自然言語復号」で安全テストが技術化

**概要**:
- Natural Language Autoencoders で Claude 内部思考を可視化
- EU AI Act + 日本AI法律の「説明可能性」要件の技術的解
- Anthropic がこの分野の業界標準を握る可能性が高い

**事例詳細**:
- Anthropic Natural Language Autoencoders 公開(2026-05-07)
- Anthropic 隠れ推論可視化ツール公開(2026-05-12)
- MIT Tech Review が機械論的解釈可能性を解説(2026-05-12)

#### 観察3: ユーザー文脈層は「データ寡占 vs 性能差」の競争へ

**概要**:
- Perplexity Personal Computer・Claude in Chrome・ChatGPT Atlas が個人 AI 環境を取り合う
- LINE ヤフー Agent i が「9,000万 MAU × ユーザーデータ」で対抗
- 国内では NEC(B2B) × LINE ヤフー(B2C)の棲み分けが進行

**事例詳細**:
- LINE ヤフー AI エージェント「Agent i」(2026-05-11)
- Perplexity Personal Computer for Mac 一般開放(2026-05-08)
- Claude in Chrome 拡張(2026-05-11)

#### 観察4: 標準化は「公式ガイドライン×実装層ツール×評価基準」の3層が2026 Q4 で揃う見込み

**概要**:
- 公式: 3社ガイドライン(2026-04)、日本 AI 法律、EU AI Act
- 実装: JetBrains Central、GitHub MCP、Anthropic Cowork
- 評価: Autoencoder + ベンチマーク後の「実エンタープライズ ROI」評価

**事例詳細**:
- JetBrains Central(2026-05-08)
- GitHub MCP コミット前認証情報スキャン(2026-05-07)
- OpenClaw(OSS エージェント基盤、2026-01 → 2026-05-11 日経クロステック解説)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- エージェントの内省・解釈可能性が同月で複数進展
- 武器化リスク(メキシコ攻撃/ClaudeBleed)が並行して顕在化

**事例**:
- 2026-05-12  ClaudeBleed 脆弱性(Claude for Chrome)
- 2026-05-12  Needle 26M Tool Calling 蒸留(HN)
- 2026-05-11  LINE ヤフー Agent i / OpenClaw 解説
- 2026-05-08  Claude メキシコ攻撃 17,000行ツール公表

### 次の注視点

**概要**:
- dream + Autoencoder の組合せが規制執行ツールとして採用されるか
- 消費者向けエージェント MAU 競争の決着時期

**事例/論点**:
- エージェント武器化規制の国際協調(国連レベル議論の可能性)
- 「dream の学習権」と顧客データ主権の整理
- Sierra AI、Cognition Devin の国内導入実績
