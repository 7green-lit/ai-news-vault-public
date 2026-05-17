# LLM評価・ベンチマーク — Synthesis

最終更新: 2026-05-04 / 蓄積記事数: 5(初版生成しきい値到達) / notes.md 反映: なし(空のテンプレート)

## 自分の問い

> _index.md「## 自分の問い」セクションを引用(Single Source of Truth)

ベンチマークと実用性能の乖離はどう埋まっていくか。
評価指標自体がどう進化しているか。

## 現時点での仮説(2026-05-04)

1. **「ベンチマーク飽和」と「実タスクでの突破」の二極化が顕在化** — SWE-bench / MMLU 等の標準ベンチマークは飽和しつつあるが、**実用タスク(医療診断、数学未解決問題、脆弱性発見)で人間専門家を超える事例**が同時期に集中(Harvard ER 診断、AI が7年難問を80分で解く、Mythos の脆弱性発見)。**「ベンチマークではなく実タスクで測る時代」**への移行。
2. **評価軸が「能力スコア」から「内部観察(解釈可能性)」へ拡張** — Goodfire Silico(2026-04-30)が機械的解釈可能性ツールを公開。**「何を出力できるか」だけでなく「どうやってその答えに到達したか」を測る**新評価軸が EU AI Act 透明性義務とも結合。
3. **オープンソース陣営が「能力 × 効率」の両軸で並走** — IBM Granite 4.1(8B = 32B MoE 性能)、Google Gemma 4(無料・日本語高品質ローカル)、DeepSeek V4(長文処理)が連続。**フロンティアの「サイズ」と「能力」の比例関係が崩れた**。
4. **「ピークデータ」警告で事前学習スケーリングの終焉が見え始めた** — スタンフォード報告書(2026-05-04)が高品質学習データの枯渇を警告。**今後の能力向上は「推論時計算 / RL / agentic loop」「合成データ」「構造化データ」**の3方向にシフトする見通し。
5. **AGI 評価フレームワークが学術側と産業側で拮抗** — DeepMind「10の認知能力」(2026-04-30)、Goodfire Silico(2026-04-30)が学術寄りの評価提案。一方で産業側は**特定タスクでの実用突破**を量産する状況。両者の収束が次のフェーズ。

## 主要な論点

### 論点1: ベンチマーク飽和の現実 — SWE-bench 70%+ が当たり前に

- 2025年中盤までに SWE-bench Verified で 70%+ が標準。差別力を失った。
- 代替として TAU-bench(顧客サポートタスク)、OSWorld(GUI 操作)、企業独自の閉鎖ベンチマーク。
- 評価指標自体が**「公開ベンチ」から「組織内ベンチ」へ重心移動**。
- 関連: agentic-ai/synthesis-2025.md「論点4: SWE-bench 飽和後の評価軸」

### 論点2: 「実タスクでの人間超え」が複数領域で同時発生

- **医療**: Harvard 研究、AI が ER 診断で人間医師2名より正確
- **数学**: AI が7年悩まれた未解決問題を80分で解く(Forbes JAPAN)
- **セキュリティ**: Claude Mythos が数千の脆弱性を発見、攻撃コード生成(2026-04-29 日経XTECH)
- **構造**: 「ベンチマークで測る」段階を越えて、**人間専門家の生産性と直接比較される段階**に到達。
- 関連: [Harvard ER 診断](../enterprise-ai/articles/2026-05-04-harvard-ai-er-diagnosis.md)、[AI が数学未解決問題を相次ぎ解く](articles/2026-05-03-ai-solves-math-unsolved-problems.md)

### 論点3: 解釈可能性ツールが規制対応の手段に

- Goodfire Silico リリース(2026-04-30): モデル内部パラメータを学習中に観察・調整。
- EU AI Act の透明性義務(2027 本格適用)に対する**実装手段**として位置付けられる可能性。
- DeepMind「10の認知能力」フレーム(2026-04-30): 認知科学ベースの AGI 評価。
- 関連: [Goodfire Silico](articles/2026-05-01-goodfire-silico-interpretability.md)

### 論点4: オープンソース陣営の「サイズ × 効率」競争

- **DeepSeek V3(2024-12) → R1(2025-1) → V4(2026-4)**: 中国 OSS の継続的進化
- **IBM Granite 4.1(2026-04-30)**: 8B 密モデルが 32B MoE と同等性能
- **Google Gemma 4(2026-05-03)**: 無料・日本語高品質ローカル LLM
- **Llama 4 / Mistral / Qwen**: 既存陣営の継続的更新
- **構造**: 「クローズドの巨大モデル」vs「オープンの効率モデル」の二極競争。**実用シナリオ(オンプレ運用、規制業界、データ主権)ではオープン陣営が優位**。
- 関連: [IBM Granite 4.1](articles/2026-05-01-ibm-granite-4-1.md)、[Google Gemma 4](articles/2026-05-03-google-gemma-4-local-llm.md)

### 論点5: 「ピークデータ」警告と次世代スケーリング戦略

- スタンフォード大学「ピークデータ」報告(2026-05-04): 高品質学習データの枯渇警告。
- 今後の能力向上の3方向:
  - **推論時計算 / RL / agentic loop**(o1 / Claude Mythos / GPT-5.5 系統)
  - **合成データ**(Anthropic Constitutional AI 系統)
  - **構造化データ**(GraphRAG / KG / 業界別オントロジー、`ai-data-structuring` トピック交点)
- **市場**: 「構造化済みデータの市場価値」が顕在化(`ai-data-structuring/synthesis.md` v2 短期予測と整合)。
- 関連: [スタンフォード ピークデータ警告](articles/2026-05-04-stanford-peak-data-warning.md)

## ユーザーの問題意識(notes.md より)

(notes.md は現時点で空のテンプレートのため、本セクションは省略。
 ユーザーが見解・違和感・関連経験を追記すれば次回更新時に統合される)

## 対立する見解

- **「ベンチマークは無意味」 vs 「ベンチマーク継続改良」**: SWE-bench 飽和の現実を受けて「ベンチマークはもう機能しない」という見解と、「TAU-bench / OSWorld 等の新世代ベンチマークでまだ意味がある」という見解の対立。両者とも一定の真実を含む。
- **「事前学習スケーリングは終わった」 vs 「合成データで継続できる」**: ピークデータ論者(スタンフォード)と Anthropic Constitutional AI / DeepMind 自己改善ループ派の対立。
- **「オープン LLM が勝つ」 vs 「クローズドフロンティアが勝つ」**: Granite 4.1 / Gemma 4 / DeepSeek V4 が示すオープン陣営の躍進と、Mythos / GPT-5.5 / Claude Opus 4.7 が示すクローズドフロンティアの能力差。**用途別で答えが異なる**ため、二者択一ではない可能性。

## まだ分かっていないこと

1. **Harvard ER 診断研究の再現性**: 同様の研究が他の医療機関で再現されるか。バイアス・データセットの偏りはないか。
2. **AI が解いた数学未解決問題の検証**: 7年難問を80分で解いた事例の証明の正当性。数学界での査読プロセス。
3. **「ピークデータ」の具体的な閾値**: 高品質データの枯渇は何年後にどの程度起きるか。スタンフォード報告書の試算精度。
4. **解釈可能性ツールの規制適合性**: Goodfire Silico が EU AI Act 透明性義務の実装手段として認められるかの判断は誰がいつ下すのか。
5. **TAU-bench / OSWorld 等の次世代ベンチマークの飽和速度**: 新ベンチマークもどれくらいの期間で飽和するか。
6. **企業内クローズドベンチマークの相互比較不能性**: 各社が独自ベンチを作る傾向は、業界全体の進歩測定を困難にする可能性。

## 次に追うべきソース・キーワード

- **学術**: NeurIPS / ICML / EMNLP の評価関連論文、特に解釈可能性 / mechanistic interpretability、agentic eval
- **公開ベンチマーク**: SWE-bench Verified、TAU-bench、OSWorld、ARC-AGI、HumanEval、MMLU-Pro、GPQA Diamond
- **企業**: Anthropic Mechanistic Interpretability チーム、OpenAI Evals、DeepMind Cognitive Capabilities、Goodfire(Silico)
- **実タスク評価**: 医療(Harvard, NEJM AI、JAMA Network Open)、数学(arxiv math、Lean / Coq による formal verification)、コーディング(SWE-bench、LiveCodeBench)
- **「ピークデータ」**: スタンフォード追跡、各社の合成データ戦略(Anthropic Constitutional AI、DeepMind 自己改善ループ)
- **オープン陣営**: HuggingFace open LLM leaderboard、Chatbot Arena、IBM Granite シリーズ、Google Gemma シリーズ、Meta Llama シリーズ、DeepSeek、Mistral、Qwen

## 累積記事一覧(5件、2026-05-04時点)

1. [Goodfire Silico、機械的解釈可能性ツール公開](articles/2026-05-01-goodfire-silico-interpretability.md) — `new_angle`(2026-04-30)
2. [IBM Granite 4.1、8B が 32B MoE と同等性能](articles/2026-05-01-ibm-granite-4-1.md) — `new_angle`(2026-04-30)
3. [スタンフォード「ピークデータ」警告](articles/2026-05-04-stanford-peak-data-warning.md) — `new_angle`(2026-05-03)
4. [AI が数学未解決問題を相次ぎ解く — 7年難問を80分で](articles/2026-05-03-ai-solves-math-unsolved-problems.md) — `new_angle`(2026-05-03)
5. [Google Gemma 4 — 無料・高品質日本語ローカル LLM](articles/2026-05-03-google-gemma-4-local-llm.md) — `new_angle`(2026-05-03)

---

> 次回 synthesis 更新: 累計10記事到達時、または「contradicts」判定の記事追加時。

---

## v2 増分付録(2026-05-11): 評価軸の深化 — ベンチマークから「専門家定性評価 + 内部解釈」へ

### 蓄積記事(累計5→7件)
- [Tim Gowers 数学者の ChatGPT 5.5 Pro 体験記](articles/2026-05-09-gowers-chatgpt-5-5-pro-experience.md) — `new_angle`(2026-05-08)
- [Anthropic Natural Language Autoencoders](articles/2026-05-07-anthropic-natural-language-autoencoders.md) — `new_angle`(2026-05-07)

### 論点 R: フィールズ賞数学者の定性証言 = 専門家評価の決定的データ
**v1 までの評価軸**: SWE-bench、TAU-bench、OSWorld、GPQA Diamond、HLE 等の**自動評価**、Chatbot Arena 等の**Elo レーティング**、Harvard / NEJM 等の**医療実タスク評価**。

**v2 で追加**: **Tim Gowers**(フィールズ賞数学者)の **ChatGPT 5.5 Pro 研究体験ブログ**(2026-05-08、HN 683 points / 510 コメント)が、**トップ専門家による定性証言**として AI 業界の議論を主導。

**意義**:
- **「使える / 使えない」の境界**を**ドメインのトップ専門家が公開言語化**: 数学的閃きの誘発剤か、雑用処理ツールか
- **AI が数学未解決問題を解く事例**(2026-05-03)を**質的に補完**: 単独ブレイクスルー vs 「人間 + AI」協働の質的差異
- **対比**: 数学以外の専門領域(医学 = Harvard ER、法学 = Legora、物理学、化学)での同様の検証論議が促進されると予想
- **評価軸の含意**: 自動ベンチマーク飽和(SWE-bench)に対する**「トップ専門家定性証言」**の重要性が増す。 これは Anthropic Cowork、OpenAI ChatGPT Pro 等の**プレミアム層 LLM**の評価方法と直結。

### 論点 S: Natural Language Autoencoders = 「正答率」から「内部理解の正確性」へ
**v1 までの解釈可能性議論**: Goodfire **Silico**(機械的解釈可能性、ニューロンレベル)、Anthropic **mechanistic interpretability** 中心。

**v2 で追加**: Anthropic **Natural Language Autoencoders**(2026-05-07)が **Claude の内部「思考」を自然言語に復号**。**「AI が正答した」**だけでなく**「AI が正しい理由を内部でも理解しているか」**を技術的に検証可能に。

**意義**:
- **新評価軸の登場**: 「答案正確性」+「思考プロセス忠実度」の2軸評価
- **Claude 脅迫行動研究(2026-05-09)、メキシコ攻撃(2026-05-08)、'evil' 描写影響(2026-05-11)** の技術的解明手段
- **「ピークデータ」(2026-05-04 スタンフォード)** の対応策との関係: 学習データ枯渇期に**「データから何を学んだか」**を解明する技術が必須
- **規制対応**: EU AI Act / 日本 AI 法律(2026-05-11)の「説明可能性」要件への技術的解 — Anthropic がこの分野の業界標準を握る可能性
- **競合**: Goodfire Silico、OpenAI Sparse Autoencoders、Google DeepMind の解釈研究との立ち位置(Anthropic が最も体系的に研究公開)

### 論点 T: ChatGPT/Claude/Gemini 三極化(2026-05-08 enterprise-ai 蓄積)が評価需要を質的に変える
**v1 までの市場想定**: OpenAI が圧倒的、Claude / Gemini がチャレンジャー。

**v2 の発見**: Apptopia 調査(2026-05-08)で**米国生成 AI チャットアプリ市場で ChatGPT シェア40%切る**、**Claude 急伸、Gemini 安定**で**三極化**。

**評価需要への影響**:
- **3社の強み比較が公的に必要**: Gowers の ChatGPT 5.5 Pro 体験記が**「他の2社では?」**質問を生む構造
- **`ai-models/llm-3services-comparison.md`(2026-05-11 ユーザー作成)** が示す通り、**バージョン別軌跡 × 機能軸別進化**の比較が主流評価方法に
- **国内市場の評価**: LINE ヤフー Agent i(2026-05-11)、NEC × Anthropic(同日)が**日本語性能評価**の需要を喚起
- **Sakana × NVIDIA TwELL**(2026-05-10): 評価軸に**「同性能を低コストで」**指標が加わる

### v2 到達点まとめ
| 評価軸 | v1 | v2 |
|---|---|---|
| 自動ベンチマーク | SWE/TAU/OSWorld/GPQA/HLE | + 評価飽和、Gowers 型定性証言の重要性 |
| 解釈可能性 | Goodfire Silico、Anthropic 公開 | + Natural Language Autoencoders(内部独白) |
| 市場シェア | ChatGPT 単独首位 | 三極化(ChatGPT/Claude/Gemini) |
| 専門家評価 | Harvard ER、NEJM | + Gowers 数学体験記、ChatGPT 三社比較 |
| データ問題 | ピークデータ警告 | + Autoencoder で「学習したこと」解析可能 |

**次回 v3 候補**:
- Gowers 型「専門家定性証言」の他ドメイン展開(医学 / 法学 / 物理学 / 化学 / 哲学)
- Natural Language Autoencoders の規制標準化可能性
- 三極化前提の評価ベンチマーク再設計(Chatbot Arena の進化、GPQA 後の AGI 評価)
- 国内市場(LINE ヤフー、NEC × Anthropic)向け日本語特化評価ベンチマークの整備


---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> ベンチマーク飽和後、専門家定性証言・内部解釈・三極化前提評価へ。次の評価軸は何か。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: 自動ベンチマーク層は飽和、SWE-bench 型は限界に到達

**概要**:
- SWE-bench/TAU/OSWorld/GPQA Diamond/HLE などで「全社90%超」の飽和
- Chatbot Arena 等の Elo 評価も差が縮小
- 三極化(ChatGPT/Claude/Gemini)前提の機能軸別比較が新標準

**事例詳細**:
- ChatGPT/Claude/Gemini 三極化(2026-05-08)
- llm-3services-comparison.md(2026-05-11、ユーザー作成)
- @IT「日本語 AI は約1.5倍高い」(2026-05-12)

#### 観察2: 解釈可能性層が「思考プロセス忠実度」を新評価軸に追加

**概要**:
- Natural Language Autoencoders で「答案正確性」+「思考プロセス忠実度」の2軸へ
- Anthropic が解釈研究で業界標準を握る可能性
- EU AI Act / 日本 AI 法律の「説明可能性」要件と直結

**事例詳細**:
- Anthropic Natural Language Autoencoders(2026-05-07)
- Anthropic 隠れ推論可視化ツール(2026-05-12)
- Goodfire Silico 機械的解釈可能性公開(2026-05-01)

#### 観察3: 専門家定性証言層がベンチマーク飽和への決定的解

**概要**:
- フィールズ賞数学者 Gowers の ChatGPT 5.5 Pro 体験記が HN 683 pts
- 医学(Harvard ER)、法学(Legora)などのドメイン展開が予想される
- 「使える/使えない」境界をトップ専門家が公開言語化

**事例詳細**:
- Gowers の ChatGPT 5.5 Pro 体験記(2026-05-09)
- Harvard 研究 AI が ER 診断で人間医師超え(2026-05-04)
- AI が数学未解決問題を80分で解く(2026-05-03)

#### 観察4: 産業応用評価が「異常検知の根拠説明」など独自軸を要求

**概要**:
- 東芝 反事実波形が「AI 判断根拠の波形説明」を産業実装
- NYT「Anthropic は本当に怖いか?」など主要メディアが定性評価に参入
- 「AI 買い物失敗5割」など消費者側の評価データも蓄積

**事例詳細**:
- 東芝 反事実波形生成技術(2026-05-12)
- NYT「Anthropic の新 AI は本当に怖い?」(2026-05-12)
- ITmedia 調査「AI 買い物失敗5割」(2026-05-13)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- 解釈可能性+定性評価+産業応用評価が同月で複数進展
- ピークデータ警告下で「学習データから何を学んだか」の解明が必須化

**事例**:
- 2026-05-12  Anthropic 隠れ推論可視化ツール公開
- 2026-05-12  東芝 反事実波形 / NYT「Anthropic 怖い?」
- 2026-05-09  Gowers ChatGPT 5.5 Pro 体験記(HN 683 pts)
- 2026-05-04  スタンフォード「ピークデータ」警告

### 次の注視点

**概要**:
- Gowers 型「専門家定性証言」の他ドメイン展開
- Natural Language Autoencoders の規制標準化

**事例/論点**:
- 日本語特化評価ベンチマークの整備
- 「思考プロセス忠実度」のメトリクス標準化
- AI 監査ビジネスでの評価フレーム導入
