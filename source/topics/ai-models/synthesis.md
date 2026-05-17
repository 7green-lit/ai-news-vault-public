# AI Model — Synthesis(横断分析)

最終更新: 2026-05-04 / 蓄積記事数: 0(初版、モデル知識ベース)/ notes.md 反映: なし(空のテンプレート)
補助文書: `model-evolution-timeline.md`(プロバイダ別の時系列年表)
表記: ✅=確定/公式 / 🟡=報道ベース / ⚠️=見通し・解釈

## 自分の問い

> _index.md「## 自分の問い」セクションを引用(Single Source of Truth)

主要な汎用LLM(ChatGPT/GPT、Claude、Gemini、Llama、Mistral、DeepSeek、Grok 等)が
**いつ・どのモデルが・どんな更新を行い・どんな成果(精度・スピード・コンテキスト・マルチモーダル等)
をもたらしたか**を、プロバイダ横断で時系列把握する。
モデル世代交代のパターン(Big jump vs incremental)、能力軸の進化(text→multimodal→reasoning→agentic)、
オープン vs クローズドの競争構造を整理する。

---

## 0. エグゼクティブサマリ(5つの整理)

1. **2022-11(ChatGPT)から3年半で5世代の能力転換** — テキスト対話 → マルチモーダル(GPT-4o、2024-05) → 推論モデル(o1、2024-09) → 長時間エージェント(Claude 4、2025-06) → 限定能力モデル(Mythos / GPT-5.5-Cyber、2026-04)。**約6〜9ヶ月ごとに主役の能力軸が入れ替わった**。
2. **「サイズ × 性能」の比例関係が崩壊**(2024年末〜) — DeepSeek-V3 / R1 が訓練コスト $5.6M で米フロンティア級、IBM Granite 4.1 で 8B = 32B MoE 性能。**「もっと大きく」から「もっと賢く・効率的に」**へ業界の重心が移動。
3. **コンテキスト長は4K→10M(2,500倍、2.5年)で実質無制限化** — Llama 4 Scout の 10M、Gemini 1.5 Pro の 1-2M、Claude Sonnet Plus の 1M で**「文書全体を AI に読ませる」が常態化**。これは RAG の必要性を弱めるか、あるいは依然として補完的かが論点。
4. **3階層フォーマット(Opus/Sonnet/Haiku 系)が業界標準に** — Anthropic が始めた「ハイエンド/中位/軽量」の3層構成を、OpenAI(GPT-4 / 4-Turbo / 4o-mini / o1 / o1-mini)、Google(Pro / Flash / Lite)、Meta(8B / 70B / 405B)、Mistral(Large / Small)、DeepSeek(各サイズ)が踏襲。**コスト×性能のメニュー設計**が業界共通言語に。
5. **2025-2026 はオープン陣営の躍進、ただしフロンティア能力は依然クローズド優位** — DeepSeek R1 / V4、Llama 4、Gemma 4、IBM Granite 4.1、Mistral がオープン側で「実用的な性能」を量産。一方、Mythos / GPT-5.5-Cyber / Opus 4.7 のような**特定能力での突破**はクローズドフロンティアが先行。**両者の競争構造が「コスト優位 vs 能力優位」で安定化**しつつある。

---

## 1. 主要な論点

### 論点1: 「事前学習スケーリング」の終焉と次の主軸

- **GPT-4(2023-03)から GPT-4.5 / 5(2025)までは事前学習スケーリングが主軸**。データ・パラメータ・コンピュートの比例的拡大で性能が上がる時代。
- **2025-2026 で事前学習スケールの逓減が顕在化** — GPT-4.5(Orion、2025-02 プレビュー)が「事前学習スケーリング最終世代」と位置付けられ、以降は推論時計算/RL/合成データへ重心移動。
- **スタンフォード「ピークデータ」警告**(2026-05、`llm-evaluation` で蓄積)が学習データ枯渇を理論化。
- 関連: GPT-5 の「ルーター方式」、Claude 3.7 の extended thinking、o1/o3 の推論時計算が**スケーリングの代替軸**として確立。

### 論点2: 推論モデル(reasoning)の3世代

| 世代 | 代表モデル | 特徴 |
|---|---|---|
| **第1世代** | OpenAI o1(2024-09)/ o1-preview | Chain-of-Thought をモデル内蔵化、AIME 数学 83% |
| **第2世代** | DeepSeek R1(2025-01)、Claude 3.7 ext. thinking(2025-02) | OSS 化、思考時間トレード可能、SWE-bench 70%+ |
| **第3世代** | GPT-5 ルーター方式(2025-08)、Claude 4 長時間自律(2025-06) | 推論と非推論を統合、エージェント運用前提 |

**観察**: 推論モデルは2年で「特殊機能 → デフォルト統合」へ移行。次の問いは**「人間並みの数学・科学解決」の境界**(AI が7年難問を80分で解く事例、2026-05)。

### 論点3: マルチモーダル統合の3段階

- **段階1: 機能追加**(2023-2024 前半) — GPT-4 V、Claude 3 で画像入力、Whisper / TTS で音声を別 API として追加
- **段階2: ネイティブ統合**(2024-05 GPT-4o、Gemini 2.0、2024-Q4) — 単一モデルが**テキスト+画像+音声+動画**を低遅延で扱う
- **段階3: 業務領域統合**(2025-2026) — 車載(Gemini in cars 2026-04)、医療(DeepMind co-clinician 2026-04)、教育、ロボット(Meta humanoid 2026-05)

**今後**: 「身体性・具現化」(embodied AI)で物理世界とのインタラクションが次の主戦場。

### 論点4: オープン vs クローズドの安定化した競争構造

| 軸 | クローズド優位 | オープン優位 |
|---|---|---|
| **フロンティア能力** | Mythos、GPT-5.5、Opus 4.7、Gemini 3 | — |
| **コスト効率** | — | DeepSeek V3/V4、Granite 4.1、Mistral |
| **長文処理** | Gemini 1.5 Pro(1M)、Claude Sonnet Plus(1M) | Llama 4 Scout(10M) |
| **データ主権・オンプレ** | — | Gemma 4、Llama 4、Granite、Mistral |
| **特定領域専門** | Mythos(セキュリティ)、Cowork(エージェント) | Granite(IBM 業界対応) |
| **規制業界対応** | Cohere×Aleph Alpha、Anthropic Trust Center | — |

**観察**: 2025年中盤までは「クローズドが圧倒的に優位」の見方が強かったが、2026年4月時点で**用途別の住み分け**が成立。**完全 OSS で運用可能な性能の閾値が上がり続けている**。

### 論点5: 3階層フォーマットの業界共通言語化

Anthropic が 2024-03 の Claude 3 family で確立した **Opus / Sonnet / Haiku** の3階層が、各社の「ハイエンド/中位/軽量」メニュー設計の標準形になった。

| プロバイダ | ハイエンド | 中位 | 軽量 |
|---|---|---|---|
| **Anthropic** | Opus 4.7 | Sonnet 4.5 | Haiku 3.5 |
| **OpenAI** | GPT-5.5 / o3 | GPT-5 / o3-mini | GPT-4o-mini / o1-mini |
| **Google** | Gemini 3 Pro | Gemini 3 Flash | Gemini 3 Lite |
| **Meta** | Llama 4 Behemoth | Llama 4 Maverick | Llama 4 Scout |
| **DeepSeek** | V4 / R1 | (V3) | (R1-distilled) |
| **Mistral** | Mistral Large 3 | Mistral Medium | Mistral Small |

**意義**: ユーザーが「どの会社でも同じ階層感覚で選べる」ようになった。コスト最適化が容易、ベンダーロックインが弱まる。

### 論点6: 中国オープン陣営の継続的存在感

- DeepSeek V3(2024-12)→ R1(2025-01、NVIDIA急落)→ V4(2026-04)で**継続的に米フロンティアを追い上げ**
- Alibaba Qwen 3、Tencent Hunyuan、Moonshot Kimi、Zhipu GLM が並列で進化
- **米中分断のグレーゾーン**: Tencent × Anthropic 技術協力(2026-04 報道)、xAI が OpenAI モデルから distillation(Musk 法廷証言、2026-04)
- 関連: `ai-regulation/synthesis.md` の「論点3: distillation の合法性」

### 論点7: 日本勢の独自ポジション

- **Sakana AI**: 進化アルゴリズム×LLM、研究先行から**メガバンク本格採用(SMBC、2026-04)**で B2B 現金化フェーズへ(`finance-ai` トピック)
- **PKSHA Technology**: 国内エンタープライズ B2B、ツクルバ資本提携で事業会社内部化を支援
- **Preferred Networks**: 自前 PLaMo + 製造業/自動運転/科学計算の特化
- **ELYZA**(KDDI 傘下): ELYZA-Japanese-Llama 系統、エンタープライズ向け
- **NTT tsuzumi**: 軽量日本語特化、IOWN との接続

**観察**: 日本勢は「**汎用フロンティア競争では遅れている**が、**研究先行(Sakana)+ B2B 業界特化(PKSHA)+ インフラ統合(NTT)+ 日本語特化(ELYZA)**」の4軸で独自ポジションを保つ。

---

## 2. ユーザーの問題意識(notes.md より)

(notes.md は現時点で空のテンプレートのため、本セクションは省略。
 ユーザーが見解・違和感・関連経験を追記すれば次回更新時に統合される)

---

## 3. 対立する見解

- **「スケーリング is dead」 vs 「合成データ・RL でスケール継続」**: ピークデータ論者(スタンフォード)と Anthropic Constitutional AI / DeepMind 自己改善派の対立。両者ともに一定の真実を含む。
- **「OSS が勝つ」 vs 「クローズドフロンティアが勝つ」**: DeepSeek / Llama / Gemma の躍進と、Mythos / GPT-5.5 / Opus 4.7 の能力突破。**用途別で答えが異なる**。
- **「推論モデルが標準化される」 vs 「推論モデルは特殊用途のまま」**: GPT-5 が推論統合する一方、Anthropic は extended thinking を別モードで残す。両アプローチが共存中。
- **「マルチモーダルが業務の主戦場」 vs 「テキストが依然中心」**: 業務領域(車載・医療・教育)はマルチモーダル依存だが、エンタープライズ業務(法務・金融・SI)は依然テキスト中心。

---

## 4. まだ分かっていないこと

1. **GPT-5.5 / Mythos 後の「次のジャンプ」**: 4世代目以降の reasoning model がどんな能力突破を持ってくるか
2. **OSS フロンティアが「能力でも追いつく」時期**: コスト効率は並んだが、能力差は何ヶ月か
3. **日本勢の汎用フロンティア参入可能性**: Sakana が evolutionary approach で既存スケール戦略を破る可能性、Sovereign AI 政策との結合
4. **マルチモーダル**(特に動画・3D)の**コストと品質のクロスポイント**: Sora / Veo / Runway の実用化フェーズ
5. **エージェント能力の評価標準**: TAU-bench / OSWorld 等の次世代ベンチがいつ飽和するか
6. **「特化能力モデル」(Mythos / Cyber)の業界化**: 医療特化、法務特化、生物学特化などが各社から出るパターン

---

## 5. 次に追うべきソース・キーワード

- **公式発表**: OpenAI Blog、Anthropic Blog、Google DeepMind Blog、Meta AI Blog、Mistral Blog、DeepSeek Tech Reports、xAI Blog
- **ベンチマーク**: SWE-bench Verified、TAU-bench、OSWorld、ARC-AGI、HumanEval、MMLU-Pro、GPQA Diamond、HLE(Humanity's Last Exam)
- **市場分析**: Artificial Analysis、Chatbot Arena(LMSYS)、HuggingFace Open LLM Leaderboard
- **モデルカード**: 各社の System Card / Model Card は能力・制約の正確な記述源
- **学術**: NeurIPS / ICML / EMNLP / ICLR / ACL の主要論文、特に Mechanistic Interpretability、Reasoning、Multimodal、Agentic 系
- **国内**: AINOW、ITmedia AI+、@IT、ZDNet Japan(廃止)、日経クロステック AI、Sakana AI / PKSHA / PFN / ELYZA / NTT 公式

---

## 6. 関連蓄積(他トピックの参照)

- `ai-companies/synthesis.md` — 各プロバイダの事業戦略・評価額
- `ai-companies/ma-timeline-2024-2026.md` — 資金調達と人材移動
- `llm-evaluation/synthesis.md` — ベンチマーク・解釈可能性・実タスク評価
- `agentic-ai/synthesis-2025.md` — エージェント能力の進化(モデル進化と密接)
- `ai-data-structuring/synthesis.md` — MCP・構造化出力・データ整備
- `ai-regulation/synthesis.md` — Mythos / GPT-5.5-Cyber 限定提供、Musk distillation 訴訟
- `finance-ai/articles/2026-05-03-sakana-smbc-multi-agent-proposal-generation.md` — Sakana AI のメガバンク現金化

---

## 7. 補助文書

**`model-evolution-timeline.md`** — プロバイダ別(OpenAI / Anthropic / Google / Meta / DeepSeek / Mistral / xAI / その他)の時系列年表。各モデル発表日・特徴・主要成果を網羅。本 synthesis の参照用データ層として機能。

---

> 次回 synthesis 更新: 累計5記事到達時、または「contradicts」判定の記事追加時。
> 蓄積記事が増えたら、この知識ベースの retrospective を articles と統合した v2 に再構成する。


---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> GPT/Claude/Gemini の三極化、ローカル LLM 進化、特化モデル、シンボリック学習。次世代の評価軸は何か。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: フロンティア競争は三極化が安定状態へ、新規参入は破壊的差別化が必要

**概要**:
- ChatGPT/Claude/Gemini で全方位機能差は縮小、差は「業界特化」「効率」「文脈」に
- Anthropic は法務、OpenAI は CFO/金融、Google は消費者 OS、と特化軸が見え始める
- Moonshot AI Kimi など中国系が破壊的設計で割り込みを狙う

**事例詳細**:
- ChatGPT シェア40%切る、Claude 急伸、Gemini 安定(2026-05-08)
- Anthropic Claude for Legal / OpenAI × PwC / Google Android Show(2026-05-12)
- Moonshot AI Kimi の LLM 根幹設計に Musk も驚き(2026-05-12)

#### 観察2: ローカル/エッジ層が「ChatGPT 5.5 Pro 接近」レベルに到達

**概要**:
- Llama 4 / Qwen3 / DeepSeek-R1 / Gemma 4 が無料でフロンティア接近
- Tool Calling 専用蒸留(Needle 26M)が現実的になり、スマホ・IoT 上で実用
- 「Local AI needs to be the norm」が HN で大バズ(2026-05-11、399 pts)

**事例詳細**:
- Needle 26M Gemini Tool Calling 蒸留(2026-05-12)
- ローカル LLM 進化解説(ギズモード、2026-05-10)
- Google Gemma 4 無料・高品質日本語 LLM(2026-05-03)

#### 観察3: アーキ革新は「音声リアルタイム」「効率フォーマット」「同時聴き話し」が同時進行

**概要**:
- OpenAI Realtime API 3モデルで音声推論・翻訳・転写がコモディティ化
- Sakana × NVIDIA TwELL で推論30%高速化・H100メモリ24%削減
- Thinking Machines「interaction models」で同時聴き話し AI が実装段階

**事例詳細**:
- OpenAI 次世代音声 API3モデル(2026-05-08)
- Sakana × NVIDIA TwELL(2026-05-10)
- Thinking Machines interaction models(2026-05-11〜12)

#### 観察4: ドメイン特化モデルが「業界別評価ベンチマーク」を新たに要求

**概要**:
- GPT-5.5-Cyber、Claude for Legal、Anthropic Agents for FS など特化版が増加
- 東芝 反事実波形のような「異常検知の根拠説明」が産業応用へ
- 日本語トークン効率(約1.5倍コスト)解消のため国産特化 LLM が経済合理性

**事例詳細**:
- OpenAI GPT-5.5-Cyber Trusted Access(2026-05-07)
- 東芝 反事実波形生成技術(2026-05-12)
- @IT「日本語 AI は約1.5倍高い」実測(2026-05-12)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- 三極化の安定 + ローカル LLM 急進歩が同時進行
- 業界特化モデルとシンボリック学習が次世代評価軸を要請

**事例**:
- 2026-05-12  François Chollet シンボリック学習で新 AI 開発(Ndea)
- 2026-05-12  Google Cloud Storage Rapid で AI 学習効率改善
- 2026-05-12  Threads × Meta AI / Rivian AI Voice / Gboard Gemini
- 2026-05-08  OpenAI Voice Realtime-2/Translate/Whisper

### 次の注視点

**概要**:
- 三極化の安定性と「業界特化軸」の確立タイミング
- 国産 LLM(ELYZA/NEC cotomi/PFN PLaMo/Sakana)の経済合理性

**事例/論点**:
- Apple Intelligence の巻き返し(390億円和解後)
- Moonshot/DeepSeek/Qwen の中国系破壊的モデル
- シンボリック学習(François Chollet)の商用化時期
