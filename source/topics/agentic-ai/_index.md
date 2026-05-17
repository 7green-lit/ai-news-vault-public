# AIエージェント・Agentic AI

slug: `agentic-ai`
作成日: 2026-04-30

## 自分の問い

AIエージェントは「デモから実用」へどう移行していくか。
信頼性・コスト・人間との協調設計の観点で何が成功要因か。

## キーワード

agent, agentic, autonomous, エージェント, 自律, tool use, function calling

## 関連トピック

- `ai-coding`: コーディング系エージェント(Claude Code、Cursor、Devin、Codex)
- `ai-companies`: 各社のエージェント戦略の差分
- `enterprise-ai`: 業務適用とROI
- `llm-evaluation`: SWE-bench / TAU-bench / OSWorld などの評価軸

## メモ・見解

[notes.md](notes.md) にユーザーの見解・仮説・違和感を蓄積。
次回 `synthesis.md` を再生成するときに `topic-curator` スキルが自動的に articles と統合する。

---

## 蓄積記事

(articles/ 配下に追加されると、必要に応じてここに索引を作る)

## 主要ドキュメント

- `synthesis-2025.md` — 2025年の動向を年次レビューとしてまとめたもの(2026-04-30作成)
- `synthesis.md` — 累積記事から導いた継続的考察(`topic-curator` スキルが更新)

## 履歴

- 2026-04-30: トピック作成、`synthesis-2025.md`(年次レビュー)初版
- 2026-05-01: 4記事を追加(累計4件)
  - [Stripe Link でエージェント決済対応](articles/2026-05-01-stripe-link-agent-payment.md) — `new_angle`(エージェント金融インフラ層の追加)
  - [Anthropic Claude Security パブリックベータ](articles/2026-05-01-anthropic-claude-security-beta.md) — `reinforces`(攻撃 vs 防御の構造)
  - [ServiceNow「AI社員」管理環境強化](articles/2026-05-01-servicenow-ai-employee.md) — `reinforces`(マルチエージェント協調)
  - [Anthropic 公式調査: How people ask Claude](articles/2026-05-01-anthropic-personal-guidance-research.md) — `tangential`
- 2026-05-01(午後): 国内強化フィードから2記事追加(累計6件)
  - [Gartner: 企業の60%が AI エージェント自動化(@IT)](articles/2026-05-01-agent-ai-it-infra-ops-transition.md) — `reinforces`(運用フェーズ移行の定量データ)
  - [PocketOS の悲劇 — エージェントが本番+バックアップを9秒で破壊(@IT)](articles/2026-05-01-pocketos-9-second-disaster.md) — `reinforces`(権限分離不足が根本原因の分析)
- 2026-05-05: 蓄積指示で1記事追加(累計7件)
  - [Bloomberg「AI 疲れが人生の時間を奪う」 — Claude を第二の脳とする統合の裏](articles/2026-05-04-bloomberg-ai-fatigue-claude-second-brain.md) — `reinforces`(人間との協調設計の負荷)
- 2026-05-11: notes.md の3問い(公式エージェント運用ガイドライン/Symphony 仕様/SWE-bench 後評価軸)に応える v2 増分付録を `synthesis-2025.md` に追加
  - 付録 A: Anthropic / OpenAI / Google の公式ガイドライン要約と共通点・相違点
  - 付録 B: OpenAI Symphony 仕様の詳細(issue tracker → agent 標準仕様)と他仕様との違い
  - 付録 C: SWE-bench 飽和後の代替評価軸(TAU-bench / OSWorld / GPQA Diamond / HLE / 実タスク評価)
- 2026-05-11(午後): 5/5-5/11 ダイジェストから3記事追加(累計10件、しきい値到達 → 次回 synthesis 再生成候補)
  - [Anthropic Claude Managed Agents「dream」機能](articles/2026-05-06-claude-managed-agents-dream.md) — `new_angle`(エージェント休止時の振り返り学習)
  - [LINE ヤフー AI エージェント「Agent i」](articles/2026-05-11-line-yahoo-agent-i.md) — `new_angle`(データ寡占の優位性、対 AI 大手)
  - [Anthropic Natural Language Autoencoders](articles/2026-05-08-anthropic-natural-language-autoencoders.md) — `new_angle`(エージェント内部思考の言語化)
