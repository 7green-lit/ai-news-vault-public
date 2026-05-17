# 物流×AI(倉庫・配送・自動運転・サプライチェーン)

slug: `logistics-ai`
作成日: 2026-05-04

## 自分の問い

> このセクションが**問いの Single Source of Truth**。
> Obsidian 等で自由に書き換えてOK。次回 synthesis 更新時に自動反映される。

物流業界(倉庫・配送・自動運転トラック・ドローン・サプライチェーン)で AI が
**労働力不足・配送コスト・最適化**の3課題をどう解決していくか。
労働力不足・配送コストのメインは、AI/ロボットが現実解になる範囲。
まず最適化領域におけるホワイト人材領域の管理業務がAIエージェントにより代替されている方向性ではないか。
米国先行(Amazon Robotics、Symbotic、Aurora 等)と日本(ヤマト、佐川、楽天、SBS、SoftBank Roze 等)
の戦略の差はどこにあり、今後数年でどう進化するか。

## キーワード

物流、倉庫、配送、宅配、ラストワンマイル、自動運転、ドローン配送、サプライチェーン、
warehouse robotics、Amazon Robotics、Symbotic、Locus Robotics、Dexterity、AutoStore、
Aurora、Kodiak、TuSimple、Zipline、Wing、Prime Air、Flexport、project44、FourKites、
2024年問題、ヤマト、佐川、日本郵便、SBSホールディングス、大和ハウス、楽天物流、ZMP

## 関連トピック

- `ai-companies`: SoftBank Roze、Amazon Robotics、Symbotic 等の企業戦略
- `agentic-ai`: 倉庫・配送のマルチエージェント協調、自動運転の意思決定層
- `enterprise-ai`: 物流大手の AI 導入 ROI 事例
- `ai-data-structuring`: サプライチェーンデータの構造化、 demand forecasting の前段
- `multimodal`: 画像認識(ピッキング)、音声指示、車両センサー融合

## メモ・見解

[notes.md](notes.md) にユーザーの見解・仮説・違和感を蓄積。
次回 `synthesis.md` を再生成するときに `topic-curator` スキルが自動的に articles と統合する。

---

## 蓄積記事

(`articles/<日付>-<short-slug>.md` の形式で蓄積)

## 主要ドキュメント

- `synthesis.md` — **2023〜2026の主要動向 × 米国/日本の対比 × 見通し** をまとめた基幹文書
- 累計5記事到達でこの synthesis を全面再構成

## 履歴

- 2026-05-04: トピック作成、`synthesis.md` 初版執筆(モデル知識ベースの retrospective)
- 2026-05-11: notes.md のユーザー仮説(ルールベース機械のアップデート vs エージェンティック AI、ステップ的導入)を反映して synthesis v2 増分更新
  - 新論点 A: 「ルールベース AI 化」vs「エージェンティック AI」の区別を表に整理
  - 新論点 B: 物流オペレーション AI 化の7ステップ別難易度マップ
  - 新論点 C: 画一化業務 → AI 導入のスムーズさ仮説の検証フレーム
- 2026-05-11(午後): 5/5-5/11 ダイジェストから2記事を初期蓄積(累計2件)
  - [Loop 物流データ基盤刷新 — AI で輸送コスト可視化](articles/2026-05-08-loop-logistics-data-platform.md) — `new_angle`(国内版 FourKites/project44)
  - [ファナック・安川電機もフィジカル AI、国産基盤で情報資源死守](articles/2026-05-11-fanuc-yaskawa-physical-ai.md) — `new_angle`(物流ロボティクス × データ主権)
