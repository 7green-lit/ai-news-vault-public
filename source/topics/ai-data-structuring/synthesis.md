# AI活用のための構造化 — 歴史・現状・見通し(v3 増分)

最終更新: 2026-05-11(累計13記事+ notes.md 反映で v3 増分更新)
旧版: `_synthesis_history/2026-05-01-initial-6articles.md`(初版)、本ファイル前バージョン(v2、2026-05-01午後)
性質: モデル知識ベース(歴史)+RSS蓄積記事(現状)+ユーザー notes 仮説(見通し)
信頼度表記: ✅=確定/標準解 / 🟡=報道・観察ベース / ⚠=見通し・解釈

> **v3 増分更新(2026-05-11)**: notes.md にユーザーが書いた**「MCP × 文脈を含む構造化(Anthropic スキル)」**仮説と、追加記事(MIT Operationalizing AI Aconnect 関連)を反映。**ユーザーの中心仮説を本 synthesis の主軸に格上げ**。

## 自分の問い(再掲)

LLMを業務で機能させるためのデータ・知識・スキーマの「構造化」は歴史的にどう積み上がり
現状どこまで来ていて、今後どう進むか。特に国内エンタープライズで何がボトルネックで
どんな突破口が見えているか。

---

## v3 のユーザー中心仮説(notes.md より、本 synthesis の中核に格上げ)

> **MCP の登場により、これまで PDF 等のデータベースでのデータの構造化が、対象となるデータの範囲が大幅に広がる。データ構造化は現在文脈を含めた構造化がなされておらず(PDF 等の資料を読み込んで AI が活用できるようにするだけ)、この文脈を含めた構造化(Anthropic 社が言う**いわゆるスキル**)のパターン化が各業種や業界、業務内容によって形式立てられ、一気にエージェント化が進むと考えられる**

### この仮説の重要性

これは **`ai-data-structuring` トピックで最も重要な見通し**を提示している。3つのレイヤーに分解:

1. **MCP が「データ構造化の対象範囲」を拡張する** — 従来は PDF/Excel 等の静的データ、MCP で**API・SaaS・社内システム・コミュニケーションログ**まで範囲が広がる
2. **「文脈を含めた構造化」= Anthropic スキル概念** — 単なるデータの読み込みではなく、**業務文脈・社内ルール・職人技・暗黙知**を AI が呼び出せる「スキル」として整理
3. **業種・業務別パターン化 → エージェント化加速** — 各業界(製造業、金融、保険、教育、医療等)で「業界別スキル」が定式化されると、**Aconnect/Sakana のような業務エージェント**が一気に普及

### ユーザー仮説と既存蓄積の整合

- ** Aconnect**(製造業 R&D 向け業務スキル化)はまさに**「業界別スキルパターン化」の先駆例**
- Anthropic の **MCP**(2024-11 公開)+ **Skills 仕様**(Claude 3.5 Computer Use 系統)は、ユーザーの言う「スキル」概念と整合
- Google の **6プロトコル整理(MCP / A2A / UCP / AP2 / A2UI / AG-UI)**(2026-04-30)は、スキル流通の標準化フェーズの幕開け
- **MIT Tech Review「Operationalizing AI」**(2026-05-02)が「データ主権 × AI 運用」を論じたのは、この**「文脈を含む構造化を運用化する」**段階の業界誌的整理

### ユーザーが追加で知りたい論点(notes.md より)

- 業界別のデータ構造化進度・手法の違い
- 海外の構造化進展状況と日本との差異

---

## v3 で追加する3つの新論点(ユーザー仮説の発展)

### 新論点A: 「PDF構造化」から「文脈構造化(スキル化)」への進化軸

- **第1世代(2023-2024)**: PDF を OCR + 埋め込み → ベクトル検索(単純 RAG)。「データの中身を AI が読める形に」
- **第2世代(2024-2025)**: GraphRAG / KG で関係性を構造化。「データ同士のつながりを構造化」
- **第3世代(2025-2026)**: **MCP + スキル**で**業務文脈の構造化**。「**業務をやる手順・判断ルール・暗黙知**を AI が呼び出せる」← **ユーザー仮説の核心**
- **第4世代(2026-2027 予測)**: **業界別スキルのパッケージ化と流通** —  Aconnect 系の業界別エージェント、MCP マーケットプレイス、Salesforce Headless 360 のエージェント機能と接続

### 新論点B: 業界別「文脈構造化」の進度マップ(ユーザー知りたい論点1への応答)

| 業界 | 文脈構造化の進度 | 代表事例 | 残課題 |
|---|---|---|---|
| **製造業 R&D** | 先進(★★★) |  Aconnect、ライオン採用、アクセンチュア×NSK、横浜ゴム VLM | FMEA / 故障対応の標準化、暗黙知抽出方法論 |
| **金融** | 開始(★★) | Sakana×SMBC、提案書6エージェント | アクチュアリー、リスク管理、コンプラのスキル化 |
| **教育・研究** | 部分的(★★) | 神田外語大 Aconnect、Google AI Pro 立教 | 研究ノウハウのスキル化 |
| **医療** | 限定(★) | DeepMind co-clinician、Anthropic BioMysteryBench | 医療規制との適合 |
| **法務** | 限定(★) | Legora、Harvey | 判例理解、業界別カスタマイズ |
| **公共・行政** | 開始(★★) | デジタル庁、東京都×ソウル | データ主権、機密対応 |
| **小売・流通** | 限定(★) | 楽天 Rakuten AI、Choco(OpenAI 事例) | サプライチェーンの動的最適化 |

### 新論点C: 海外との差異(ユーザー知りたい論点2への応答)

| 観点              | 米国                                                     | 中国                     | 日本                              |
| --------------- | ------------------------------------------------------ | ---------------------- | ------------------------------- |
| **データ整備のリード時間** | 1-2年(企業側投資が早い)                                         | 1年(国家主導で速い)            | 3-5年(Last Mile 問題が深い)           |
| **スキル化の進度**     | OpenAI / Anthropic API + 個別実装                          | Alibaba / Tencent 自社統合 |  Aconnect / Sakana が先行 |
| **データ主権**       | クラウド集中(米国内)                                            | 国家主導集中                 | データ主権意識高、Oracle Alloy / Gemma 4 |
| **業界標準化**       | 進行中(Salesforce / ServiceNow / Microsoft Agentic Suite) | 進行中(BAT 系)             | 開始(国内 SI が動き始めた)                |

**観察**: 日本は**データ整備で遅れている**が、**業界別スキルパターン化では先行する可能性**(製造業 R&D が世界的に独自)。

---

## 0. v2の更新ハイライト(初版からの差分)

国内強化フィードから4記事を追加した結果、以下の論点が**大きく前進**または**新規追加**された:

1. **「データ主権 × 分散クラウド」が国内トップベンダー戦略の焦点に** — 日本オラクル CEO が「最高の AI は最高のデータが支える」と発言、Oracle Alloy 国内採用5社拡大。Google Spanner Omni と並ぶ第二の選択肢として顕在化。
2. **MCP分裂が「リスク」から「現実」へ** — Google が **6つのAIプロトコル(MCP / A2A / UCP / AP2 / A2UI / AG-UI)** を整理した解説を出した。初版で予測したリスクが2週間で現実化。
3. **国内 SI ビジネスモデル変革** — 富士ソフトの「人月商売脱却」、アジアクエストの Databricks SI コンサルティングパートナー認定。**国内 SI が AI 構造化の実装パートナー網**として動き始めた。
4. **国内ペネトレーションテスト先行** — イエラエが AI エージェント / RAG 専用ペンテストを発表(`ai-regulation` で別途蓄積)。**サービス供給網が政策に先行**する構造。

---

## 1. 歴史 — 「AIに食わせるための構造化」40年史

(v1 と同じ。新記事に歴史的修正情報なし)

### 1.1 第1期: ルールと知識(1970s-1980s) — 完全構造化の試み

- **Expert System**: MYCIN(1976、医療診断)、DENDRAL、XCON(DEC、年商 $4000万削減)
- 構造化の方法: **手動でルールベース化**(IF-THEN ルール)
- 限界: knowledge engineering bottleneck。Cyc(1984-)が数百万ルールを目指したが商用化限定。
- 国内: 第5世代コンピュータ計画(1982-1992、ICOT)、Prolog ベース推論。

### 1.2 第2期: Semantic Web とオントロジー(1998-2010s前半)

- Tim Berners-Lee 提案(1998)、**RDF / OWL / SPARQL** が W3C 標準化。
- DBpedia(2007-)、Freebase(2007、後 Google KG)、Wikidata(2012-)。
- オントロジー: Gene Ontology、SNOMED CT。**専門家手作業が職人技**。

### 1.3 第3期: Big Data とデータレイク(2010s) — 「構造化を諦める」運動

- Hadoop(2006-)、Spark(2014-)、**schema-on-read**。
- Snowflake(2014-)、Databricks(2013-)= データレイクハウス。
- KG 側は Google Knowledge Graph(2012)、Microsoft Satori 等が水面下で運用。
- 国内: Excel/Access/独自パッケージが温存、データレイク本格化は2020年前後。

### 1.4 第4期: Embedding とベクトル検索(2017-2022)

- word2vec(2013)→ BERT(2018)→ Sentence-BERT(2019)。
- **「ベクトルにすれば類似度で検索できる」**=スキーマ設計不要。
- ベクトルDB: Faiss(2017)→ Pinecone(2020-)、Weaviate、Qdrant、Milvus。

### 1.5 第5期: RAG 爆発期(2023-2024)

- **RAG (Retrieval-Augmented Generation)** が業務 AI のデファクトに(Lewis et al. 2020 が原典)。
- LangChain(2022-10)、LlamaIndex(2022-11)。
- **Function Calling**(OpenAI 2023-06)、**Structured Output / JSON mode**(2023-11)、**Tool Use**(Claude 2024-04)。
- 課題: 単純 RAG の失敗事例集(チャンク分割、リランキング不足、ハルシネーション、長文脆弱性)。

### 1.6 第6期: GraphRAG と MCP(2024-2026)

- **GraphRAG**(Microsoft Research、2024-04)
- **MCP**(Anthropic、2024-11、業界事実標準)
- **Salesforce Headless 360**(2026-04)、**Cloudflare Artifacts**(2026-04)、**ServiceNow AI 社員**(2026-04)
- **【v2 追記】** Google が 2026-04-30 に **6プロトコル(MCP/A2A/UCP/AP2/A2UI/AG-UI)** の解説を出し、**「プロトコル乱立期」が公式に開幕**。

---

## 2. 現状(2026-05時点)— 何がどこまで来たか

### 2.1 主流パターン(✅)

| レイヤー | 主流アプローチ | 主要プレイヤー |
|---|---|---|
| **検索/RAG** | ハイブリッド検索(BM25 + ベクトル + リランカー) | Pinecone、Weaviate、Qdrant、Elastic、Vespa |
| **構造化出力** | JSON Schema / Pydantic / OpenAI structured output | OpenAI、Anthropic、Google 全社対応 |
| **ツール接続** | **MCP**(2024-11〜、業界事実標準) | Anthropic 主導、Salesforce Headless 360 等 |
| **エージェント間通信** | A2A(Google 推進、対 AGNTCY)等で**競合中**【v2新規】 | Google A2A、コミュニティ AGNTCY 等 |
| **知識グラフ** | GraphRAG、Neo4j・Memgraph・TigerGraph | Microsoft Research、Neo4j、Stardog |
| **データ基盤** | データレイクハウス(構造化+非構造化一元管理) | Databricks、Snowflake、Google Spanner Omni、Oracle Alloy【v2新規】 |
| **エージェント記憶** | ファイルシステム+グラフ+ベクトル | Cloudflare Artifacts、Anthropic 内製 |
| **エージェント決済** | スキーマ化された支出承認 | Stripe Link(2026-04) |
| **国内 SI 実装** | 中堅 SI 経由のリセラー / コンサルティング【v2新規】 | アジアクエスト(Databricks)、NTTデータ(Snowflake)、富士ソフト(独自再定義中) |

### 2.2 現状の3つの問題(🟡)

1. **「単純 RAG の限界」と「GraphRAG の運用コスト」の挟み撃ち** — 中間解として LLM 自身が KG を抽出するハイブリッドが普及中。
2. **MCP サーバーのキュレーション問題** — Cloudflare Artifacts 等のホスティング解が登場、**しかし v2 で確認された 6 プロトコル乱立**で問題はさらに複雑化。
3. **企業データの「Last Mile」問題(国内特に深刻)** — アクセンチュア×SAP "ADVANCE"(2026-04)、富士ソフト人月商売脱却(2026-04 v2)、NEC「AI投資数百億円」(2026-04)で **複数主要 SIer が同時に動き始めた**ことが、ボトルネック認識の業界共通化を示す。

### 2.3 国内の特殊性(🟡)— v2で大幅拡充

- **行政データ民間開放**: デジタル庁が2026-04-29 に法改正案提出。
- **多重下請け構造のリスクと改善**:
  - 日経XTECH「Mythos に対応せざるを得ない」が指摘した脆弱性側面に加え
  - **【v2新規】富士ソフト「人月商売脱却」(2026-04-30)** が示すように **SIer 自身が業務モデル変革を宣言**。多重下請けの解消が AI 導入の前提として認識され始めた。
- **国内 SI が AI 構造化の主戦場に**【v2新規】:
  - **アジアクエスト**: Databricks SI コンサルティングパートナーに認定(2026-04-30)
  - **アクセンチュア×SAP**: ADVANCE 国内本格展開(2026-04-30)
  - **NTTデータ・富士通・NEC**: 同方向の発表が今後数四半期に集中する見込み
- **データ主権 × 分散クラウド**【v2新規】:
  - **Oracle Alloy** が国内採用5社拡大(2026-04-30)、シシリア CEO「最高の AI は最高のデータが支える」
  - **Google Spanner Omni** がローカル実行可能 RDB として(2026-04-22)
  - 規制業界(金融・通信・医療・公共)で「クラウド出せないデータ × AI 活用」のニーズが二強+α 競争に
- **生成AI 運用の3つの使いどころ**(日経XTECH 2026-04-30): 平時運用 / トラブル対応 / 入出力安全性 — すべて構造化前提
- **NEC・SoftBank・楽天・スクールバス空間設計**: B2B 業務データを「LLM が叩ける形に整える」フェーズに明確に進入(2026-04 〜 2026-05 集中)
- **国内 SaaS の MCP 対応**: 2026-05時点で**未対応**(サイボウズ kintone、freee、マネーフォワード、SmartHR)。海外の Salesforce Headless 360 / Cloudflare Artifacts に大きく出遅れ。

---

## 3. 見通し — 今後12〜36ヶ月の展開予測(⚠️)

### 3.1 短期(〜12ヶ月、2026-Q4まで)

1. **MCP サーバーマーケットプレイスの台頭** — 公式レジストリ + 認証スキーム
2. **GraphRAG の "PaaS 化"** — Neo4j AuraDB、TigerCloud、Memgraph
3. **国内 SaaS の MCP 対応開始** — kintone、freee、マネーフォワード、SmartHR の第一波
4. **「構造化済みデータ」の市場価値が顕在化**
5. **エージェント決済の標準化加速** — Visa / Mastercard / JCB / 楽天Pay / PayPay
6. **【v2新規】6プロトコル戦争の収束初期**: MCP は不動だが、A2A / UCP / AP2 のうち2つが脱落、Google A2A vs コミュニティ AGNTCY の二強化が進行
7. **【v2新規】国内 SI による Databricks / Snowflake / Oracle Alloy 並列認定パートナー網**: 中堅 SI(アジアクエスト、BeeX、クラウドエース系)が複数ベンダー対応を加速
8. **【v2新規】国内 SIer の人月商売脱却の波**: 富士ソフトの先行が功を奏した場合、TIS、SCSK、NTTデータ ビジネスソリューションが追随

### 3.2 中期(12〜24ヶ月、2027前半まで)

1. **「業務 SoR + AI スキーマ層」の二重構造の標準化**
2. **LLM-Native な業務システムの登場**(Salesforce Agentforce、Microsoft Copilot、Google Gemini Enterprise の三つ巴)
3. **解釈可能性ツール × 構造化の統合**(Goodfire Silico 系)
4. **「構造化監査ロール」の出現**(アクセンチュア×SAP ADVANCE の発展形)
5. **国内: データオーナーシップ法制度の整備**
6. **【v2新規】国内ペネトレーションテストの市場形成**: イエラエの先行(2026-05)に、GMO サイバーセキュリティ全体・NRI セキュア・S&J 等が追随。**「AI 監査」の事業カテゴリが法制度化に先行して市場形成**
7. **【v2新規】Oracle Alloy 採用が国内で30社規模に**: 規制業界での「データ主権案件」が標準化、Google Spanner Omni と並走

### 3.3 長期(24〜36ヶ月、2028前半まで)

1. **「文書のないオフィス」への移行**
2. **エージェント間プロトコル(A2A 等)の標準化**【v2追記】 — Google A2A が事実上の標準として固定化する可能性 vs コミュニティ AGNTCY との二極化
3. **オントロジーの再評価**(LLM 自動生成 + 人間レビューのハイブリッド)
4. **構造化 = 規制対応の最大手段**(EU AI Act、米能力ベース輸出規制、日本 AI 推進法)
5. **国内: AI 構造化投資の "Big Push"**

### 3.4 リスク要因(⚠️)— v2で大幅更新

- **【v2 重要更新】MCPの分裂が現実化済み**: 2026-04-30 時点で6プロトコル並立。当初予測「方言化リスク」より深刻、**「役割の異なる別プロトコル」が並立**する複雑化が起きた。エコシステム参加者の学習コスト・実装コストが上昇。
- **Vector DB の淘汰**: Pinecone / Weaviate / Qdrant / Milvus / Chroma のうち2社程度しか生き残らない可能性。
- **国内の遅れ拡大** — **v2で部分的に解消傾向**: 富士ソフト人月商売脱却・アジアクエスト Databricks 認定・Oracle Alloy 採用拡大 の同時並行は、**遅れが急速に取り戻されている**ことを示すポジティブシグナル。
- **過剰なオントロジー設計回帰**: 1980s Expert System の轍。
- **【v2新規】国内 SaaS の MCP 対応遅延**: サイボウズ kintone、freee、マネーフォワード等の国内 SaaS が MCP 対応せず、**「LLM が触れない国内データ」**として残ると、海外クラウドへのデータ流出リスクが顕在化。

---

## 4. このトピックで継続的に追いたい問い

1. **MCP サーバーのキュレーション標準は誰が握るか**
2. **国内 SaaS の MCP 対応速度**
3. **GraphRAG の運用コスト vs ROI のクロスポイント**
4. **LLM-Native ERP** の国内上陸のタイミング
5. **行政データ民間開放法**(2026-04 提出)の実効性
6. **「構造化済みデータ」の売買市場**
7. **解釈可能性ツール(Goodfire Silico 系)が EU AI Act 透明性義務の実装手段として認められるか**
8. **【v2新規】6 プロトコル(MCP/A2A/UCP/AP2/A2UI/AG-UI)のうち、生き残るのはどれか**
9. **【v2新規】国内 SI の人月商売脱却が AI 構造化に与える影響**(富士ソフト先行、NTTデータ・富士通・NEC が追随するか)
10. **【v2新規】Oracle Alloy / Google Spanner Omni / Microsoft Fabric の「データ主権分散クラウド」3強競争の国内シェア**

---

## 5. 次に追うべきソース

- **国内**: ITmedia エンタープライズ、@IT、AINOW、日経XTECH AI、サイボウズ式、Publickey、Sakana AI 公式、PKSHA IR、Preferred Networks ブログ、**【v2新規】GMO Cybersecurity by Ierae(イエラエ)、富士ソフト IR、NTTデータ・富士通・NEC の AI/SI 関連発表**
- **海外**: MIT Technology Review、Andreessen Horowitz Data Stack、Anthropic / Google MCP関連発表、Cloudflare Workers / Artifacts、Microsoft Research GraphRAG
- **公文書**: デジタル庁、経産省 AI 戦略、EU AI Office、米 NIST AI Risk Management Framework
- **学術**: NeurIPS / ICML / EMNLP / SIGMOD / VLDB
- **企業 IR**: Snowflake、Databricks、MongoDB、Salesforce、Cloudflare、Datadog、**【v2新規】Oracle、富士ソフト、PKSHA**

---

## 6. 累積記事一覧(2026-05-01時点、10件)

1. [Rebuilding the data stack for AI(MIT Tech Review、2026-04-27)](articles/2026-04-27-mit-rebuilding-data-stack.md) — `reinforces`
2. [AI needs a strong data fabric(MIT Tech Review、2026-04-22)](articles/2026-04-22-mit-data-fabric-ai.md) — `reinforces`
3. [アクセンチュア×SAP「ADVANCE」国内本格展開(ITmedia、2026-04-30)](articles/2026-04-30-accenture-sap-advance-japan.md) — `new_angle`
4. [Salesforce Headless 360(Publickey、2026-04-19)](articles/2026-04-19-salesforce-headless-360-mcp.md) — `new_angle`
5. [Cloudflare Artifacts(Publickey、2026-04-19)](articles/2026-04-19-cloudflare-artifacts-agent-fs.md) — `new_angle`
6. [Google Cloud Next: Spanner Omni / Agentic Data Cloud(Publickey、2026-04-22)](articles/2026-04-22-google-cloud-spanner-omni-agentic-data.md) — `new_angle`
7. **【v2新規】**[Oracle CEO「最高のAIは最高のデータが支える」(ITmedia、2026-04-30)](articles/2026-05-01-oracle-ceo-best-ai-best-data.md) — `reinforces`
8. **【v2新規】**[MCP/A2A/UCP/AP2 — 6プロトコル乱立(@IT、2026-04-30)](articles/2026-05-01-mcp-a2a-ucp-ap2-protocol-proliferation.md) — `reinforces`
9. **【v2新規】**[アジアクエスト、Databricks SI パートナー認定(2026-04-30)](articles/2026-05-01-asiaquest-databricks-si-partner.md) — `new_angle`
10. **【v2新規】**[富士ソフト、SIer 人月商売脱却(ITmedia、2026-04-30)](articles/2026-05-01-fujisoft-sier-new-business-model.md) — `new_angle`

---

> 次回 synthesis 更新: 累計15記事到達時、または「contradicts」判定の記事追加時。

---

## v4 増分付録(2026-05-11): 「AI 主権基盤」が製品レイヤとして確立

### 蓄積記事(累計13→16件)
- [IBM Sovereign Core 一般提供開始](articles/2026-05-11-ibm-sovereign-core-launch.md) — `reinforces`
- [Fivetran「エージェント型 AI 準備状況指数」2026年版](articles/2026-05-08-fivetran-agentic-ai-readiness-index.md) — `new_angle`
- [ファナック・安川電機もフィジカル AI、国産基盤で情報資源死守](articles/2026-05-11-fanuc-yaskawa-physical-ai-japan.md) — `new_angle`

### 論点 J: IBM Sovereign Core = v3 仮説の製品実装
**v3 までの仮説**: 「**MCP × 文脈含む構造化**(Anthropic Skill 型)が業界別パターン化される」(notes.md 中核仮説)。

**v4 の発見**: IBM が **Sovereign Core**(2026-05-05 GA、2026-05-11 国内提供開始)を発表、**アクセス統制 + 暗号化 + 監査 + AI 運用機能を統合**した**「AI 主権基盤」を製品レイヤ**として確立。IBM CEO「ソフト産業の従来型成長困難、AI データ基盤に注力」(2026-05-06)発言の製品化。

**含意**:
- **`/strategy-hypothesis.md` v2 の「SAT = データ基盤」軸と完全一致**:  の戦略仮説が IBM レベルで業界共通認識化
- **「AI 主権スタック層」の確立**: Salesforce Headless 360 / Cloudflare Artifacts / Spanner Omni / Oracle Alloy / IBM Sovereign Core SAT が同一カテゴリへ収斂
- **競合**: Microsoft Sovereign Cloud、Oracle Sovereign Cloud、AWS GovCloud が同月内で動く可能性
- **国内最終マイル**: NEC × Anthropic(2026-05-11)が Sovereign Core 上で運用するシナリオ

### 論点 K: Fivetran「AI Readiness 指数」 = 構造化の指標化元年
**Fivetran 2026年版指数**(2026-05-08)が、企業の **エージェント型 AI 準備状況**を**業界ベンチマーク化**。データパイプライン専業 Fivetran が**「Readiness の指標化」**で業界標準を狙う。

**含意**:
- 投資家・経営層向け説明指標として AI Readiness 指数が浸透 → **「AI Ready 企業」のプレミアム化**
- 同様の指数を Salesforce、Snowflake、Databricks、IBM、Oracle が独自に発表する競争へ
- ** が指数評価される場合の高スコア期待**: notes.md「業界別文脈構造化進度マップ」(v3 増分)の外部実証
- **AI 法律(2026-05-11)** が「AI Readiness 要件」を法的義務化する可能性

### 論点 L: ファナック・安川電機 = フィジカル AI × データ主権の3軸戦略
**従来の構造化対象**: ドキュメント(SAT)、SaaS データ(Salesforce/Snowflake)、エージェント記憶(Artifacts)。

**v4 で追加される軸**: **ロボット動作・センサーデータ**。ファナック・安川電機(2026-05-11、日経ビジネス)が「**フィジカル AI 国産基盤で情報資源死守**」を表明、**製造現場の動作データを学習データとして外部に渡さない**設計を公言。

**含意**:
- **構造化対象の境界拡張**: テキスト → 表 → 画像 → 動作 → 全マルチモーダル へ
-  × ファナック・安川(製造現場動作)の補完可能性
- **ジオポリティクス**: FOIP デジタル回廊(2026-05-10)、日本初 AI 法律(2026-05-11)、Sovereign Core(同日)と複合した「**国内製造データ × AI 主権**」体制
- 競合: Nvidia Isaac、Figure、1X、Sanctuary AI 等の海外勢に対し、**国産 OEM × 国産 AI(PFN、Sakana)** の組合が浮上

### 論点 M: 「2026-05 国内 AI 主権成立週」の構造分析
**2026-05-11 単日に同時発生したイベント**:
1. **日本初 AI 法律成立**(法的枠組み)
2. **IBM Sovereign Core 国内提供開始**(基盤製品)
3. **NEC × Anthropic 対談公開**(国内×米AI 提携)
4. **ファナック・安川フィジカル AI 国産基盤**(製造業適応)

これは「**法律 → 基盤製品 → 米AI 提携 → 製造業適応**」が**同時相転移**したことを意味する。前史:
- 2026-04-30 アクセンチュア × SAP「ADVANCE」国内本格展開
- 2026-04-30 富士ソフト SIer 人月商売脱却
- 2026-05-01 アジアクエスト Databricks SI 認定
- 2026-05-04 デジタル庁安全 AI 輸出
- 2026-05-06 IBM CEO「AI データ基盤」発言
- 2026-05-10 FOIP デジタル回廊構想
- 2026-05-11 4イベント同時表面化

**結論**: notes.md ユーザー仮説「**MCP × 文脈構造化 = Anthropic Skill 型**」は、より広範な「**AI 主権スタック構造**」の一部として収斂しつつある。次回 v5 候補:
- 国内 AI ベンダー(PFN、Sakana、NEC、IBM、富士通)の Sovereign Core 上での棲み分け
- Microsoft / AWS / GCP の Sovereign Cloud 動向と国内対応
- 「フィジカル AI × 構造化」の具体的データ標準(VLA モデルの学習データ規格)

---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> RAG/MCP/データ基盤/Sovereign スタックが「AI 主権基盤」としてどう収斂するか。「文脈の構造化(Skill化)」が次の中核論点か。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: データ層は「文書構造化(PDF)」→「文脈構造化(Skill)」へ進化中

**概要**:
- PDF/表/DB の抽出は既に成熟、業界別「文脈+判断ルール」の構造化が次の競争領域
- Anthropic Skill 型(振る舞いプロンプト+ツール)が事実上の標準化候補
- 国内では が先行モデル

**事例詳細**:
- Salesforce Headless 360 で SaaS データを MCP 経由公開(2026-04-19)
- HEROZ ASK が MCP 対応開始(国内法人 SaaS 第一号、2026-05-12)

#### 観察2: プロトコル層は MCP × Anthropic Skill が事実上の標準へ収斂中

**概要**:
- MCP/A2A/UCP/AP2 の6プロトコル乱立から、MCP が大手SaaS統合で勝ち抜き
- 業界別「文脈 Skill」を Anthropic が CoCounsel 連携等で先行プラットフォーム化
- Google Gemini API skills(GitHub OSS 版)が対抗、競合は中立規格作りを志向

**事例詳細**:
- GitHub MCP Server コミット前認証情報スキャン(2026-05-07)
- Anthropic Claude for Legal 20+ コネクタ + Thomson Reuters CoCounsel(2026-05-12)
- Google Gemini API skills GitHub 公開(2026-05-08)

#### 観察3: 主権/ガバナンス層は「AI 主権スタック」という新カテゴリへ昇格

**概要**:
- アクセス統制+暗号化+監査+AI 運用を統合した製品が大手から登場
-  / IBM Sovereign Core / Oracle Alloy / Salesforce Headless 360 が同カテゴリへ
- 規制業界(金融・公共・医療)向けに主権ニーズが顕在化

**事例詳細**:
- IBM Sovereign Core 一般提供開始(2026-05-05 GA、2026-05-11 国内提供)
- Fivetran AI Readiness 指数2026年版(2026-05-08)で評価軸の指標化
- Zenmu 秘密分散 × RAG 特許出願(2026-05-12)

#### 観察4: 構造化対象の境界が「テキスト/表/画像」から「動作・センサー」へ拡張

**概要**:
- ファナック・安川「フィジカル AI」で動作データが構造化対象に
- 東芝「反事実波形」など説明可能性技術が産業応用へ
- VLA モデル(視覚言語動作)向けデータ規格が次の競争軸

**事例詳細**:
- ファナック・安川電機フィジカル AI(2026-05-11)
- 東芝 反事実波形生成技術で異常検知の根拠説明(2026-05-12)
- NEC 独自 AI で 3D 点群90%軽量化(2026-05-12)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- 国内製造業データ主権の機運が同月内で複数事例化
- Big4 監査領域でも「AI 主権基盤」採用が始動

**事例**:
- 2026-05-12  HEROZ ASK MCP 対応開始
- 2026-05-12  オーエスジー × Microsoft Fabric データ基盤刷新
- 2026-05-11  ファナック・安川フィジカル AI 国産基盤
- 2026-05-07  三菱UFJ信託 × Snowflake データマネジメント

### 次の注視点

**概要**:
- Sovereign Cloud 各社(Microsoft / AWS / Oracle)の国内対応動向
- VLA モデル学習データ規格の標準化レース

**事例/論点**:
- 国内 AI ベンダー(PFN/Sakana/NEC)の Sovereign Core 連携
- MCP 分裂(A2A/UCP/AP2)の収斂タイミング
- フィジカル AI 文脈構造化の具体的データ標準
