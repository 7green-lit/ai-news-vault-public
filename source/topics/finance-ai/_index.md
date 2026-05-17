# 金融×AI(銀行・証券・保険・資産運用・決済の AI 適用)

slug: `finance-ai`
作成日: 2026-05-04

## 自分の問い

> このセクションが**問いの Single Source of Truth**。
> Obsidian 等で自由に書き換えてOK。次回 synthesis 更新時に自動反映される。

金融業界(銀行・証券・保険・資産運用・決済)で AI が**業務プロセスのどこに、どの粒度で組み込まれていくか**。
日本のメガバンク・地銀・信託・生損保の AI 採用は、米欧の先行事例と何が同じで何が違うか。
規制(金融庁ガイドライン、Basel、IFRS、米OCC、EU AI Act)が AI 採用速度をどう左右するか。
AI が金融機関の競争優位を変えるか、それとも「全員が同じツールを使う」結果競争優位は別の場所に移るか。

## キーワード

銀行、証券、保険、資産運用、決済、提案書、メガバンク、地銀、信用金庫、フィンテック、
bank、banking、finance、insurance、SMBC、三井住友、三菱UFJ、みずほ、野村、大和、SBI、
楽天証券、PayPay、Stripe Link、Goldman、JPMorgan、BlackRock、Sakana AI(金融特化案件)

## 関連トピック

- `ai-companies`: AI 提供側(Sakana、Anthropic、PKSHA)の戦略
- `enterprise-ai`: B2B 業務適用の他業界との比較
- `agentic-ai`: マルチエージェントによる提案書自動生成、エージェント決済
- `ai-data-structuring`: 金融データ整備、Last Mile 問題、Oracle Alloy 採用5社(規制業界含む)
- `ai-regulation`: Goldman 香港 Claude 禁止、金融庁 AI ガバナンス、Basel 等

## メモ・見解

[notes.md](notes.md) にユーザーの見解・仮説・違和感を蓄積。
次回 `synthesis.md` を再生成するときに `topic-curator` スキルが自動的に articles と統合する。

---

## 蓄積記事

(`articles/<日付>-<short-slug>.md` の形式で蓄積。
 メガバンク等の主要金融機関名を含む場合は `articles/<日付>-<bank>-<slug>.md` の命名規則を採用)

## 履歴

- 2026-05-04: トピック作成、`Sakana AI × SMBC 提案書自動生成` の深掘り記事を初期蓄積(累計1件)
  - [Sakana AI × SMBC、複数AIエージェント提案書自動生成(WebFetch深掘り)](articles/2026-05-03-sakana-smbc-multi-agent-proposal-generation.md) — `new_angle`(基盤事例)
- 2026-05-11: notes.md の充実(5段階モデル、PoC 連鎖、海外比較、品質・責任・規制論点)を反映して **synthesis 初版を先行生成**
  - ユーザー暫定回答(営業 → アクチュアリー → 定常 → スタンダード化 → 寡占化)を5段階モデル化
  - 海外(米国/中国)との比較、品質評価・責任分界・金融庁ガイドライン整合の論点を整理
  - 国内 AI ベンダー間の金融市場分割仮説、業界寡占化シナリオを提示
- 2026-05-11(午後): 5/5-5/11 ダイジェストから3記事追加(累計4件)
  - [MUFG × Google、商品選び〜決済 AI 化](articles/2026-05-07-mufg-google-commerce-payment-ai.md) — `new_angle`(コマース × 金融 × AI 統合)
  - [三菱UFJ信託 × Snowflake データマネジメントサービス](articles/2026-05-07-mufg-trust-snowflake-data-platform.md) — `new_angle`(信託銀行 × データ基盤)
  - [マネーフォワード GitHub 侵害で銀行連携停止](articles/2026-05-11-moneyforward-github-breach.md) — `contradicts`(Fintech × AI 拡大の脆弱性露呈)
