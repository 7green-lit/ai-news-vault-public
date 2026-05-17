# AI Model — 主要汎用LLMの進化変遷

slug: `ai-models`
作成日: 2026-05-04

## 自分の問い

> このセクションが**問いの Single Source of Truth**。
> Obsidian 等で自由に書き換えてOK。次回 synthesis 更新時に自動反映される。

主要な汎用LLM(ChatGPT/GPT、Claude、Gemini、Llama、Mistral、DeepSeek、Grok 等)が
**いつ・どのモデルが・どんな更新を行い・どんな成果(精度・スピード・コンテキスト・マルチモーダル等)
をもたらしたか**を、プロバイダ横断で時系列把握する。
モデル世代交代のパターン(Big jump vs incremental)、能力軸の進化(text→multimodal→reasoning→agentic)、
オープン vs クローズドの競争構造を整理する。

## キーワード

GPT(GPT-3.5/4/4o/5/5.5)、ChatGPT、Codex、o1/o3/o4 シリーズ、
Claude(2/3/3.5/3.7/4/4.5/Opus/Sonnet/Haiku/Mythos)、
Gemini(1.0/1.5/2.0/2.5/3)、Gemma、PaLM、
Llama(1/2/3/4)、Mistral / Mixtral、
DeepSeek(V2/V3/R1/V4)、Qwen、
Grok(1/2/3/4)、Phi、DBRX、Granite、Cohere Command、
benchmark、context length、reasoning model、推論モデル、multimodal model

## 関連トピック

- `ai-companies`: 各プロバイダ企業の戦略・評価額(モデル開発の経済的背景)
- `llm-evaluation`: ベンチマーク・解釈可能性・実タスク評価
- `agentic-ai`: モデル世代がエージェント能力にどう波及するか
- `ai-data-structuring`: 学習データ整備・MCP・構造化出力との連動
- `ai-regulation`: モデル能力ベースの規制(Mythos / GPT-5.5-Cyber 限定提供等)

## メモ・見解

[notes.md](notes.md) にユーザーの見解・仮説・違和感を蓄積。
次回 `synthesis.md` を再生成するときに `topic-curator` スキルが自動的に articles と統合する。

---

## 蓄積記事

(`articles/<日付>-<provider>-<model>.md` の形式で蓄積。
 例: `2024-05-13-openai-gpt-4o.md`、`2026-04-23-openai-gpt-5-5.md`)

## 主要ドキュメント

- `synthesis.md` — モデル進化の**横断的構造分析**(能力軸・世代パターン・競争構造)
- `model-evolution-timeline.md` — **プロバイダ別の時系列年表**(2022-11 GPT-3.5 〜 2026-05 まで)
- 累計5記事到達でこの synthesis を全面再構成

## 履歴

- 2026-05-04: トピック作成、`synthesis.md`(横断分析)+ `model-evolution-timeline.md`(時系列年表)初版執筆
- 2026-05-11: ユーザー notes.md 要望(Gemini/Claude/ChatGPT 3社比較)を反映して `llm-3services-comparison.md` 追加
  - バージョン別軌跡、機能軸別進化(コンテキスト/マルチモーダル/推論/エージェント/価格)、3社の戦略差、強み弱み比較表
- 2026-05-11(午後): 5/5-5/11 ダイジェストから4記事を初期蓄積(累計4件)
  - [ChatGPT シェア40%切る、Claude 急伸 — 生成 AI 三極化の兆し](articles/2026-05-08-chatgpt-claude-gemini-tripolar.md) — `new_angle`(LLM 市場構造変曲点)
  - [GPT-5.5-Cyber Trusted Access for Cyber](articles/2026-05-07-gpt-5-5-cyber-trusted-access.md) — `new_angle`(用途特化型 LLM 派生)
  - [OpenAI 次世代音声 API群 — GPT-Realtime-2/Translate/Whisper](articles/2026-05-08-openai-realtime-voice-models.md) — `new_angle`(音声 AI 3層化)
  - [Sakana AI × NVIDIA「TwELL」新フォーマット — LLM 推論30%高速化](articles/2026-05-10-sakana-nvidia-twell-format.md) — `new_angle`(国産研究 × NVIDIA 効率化協業)
