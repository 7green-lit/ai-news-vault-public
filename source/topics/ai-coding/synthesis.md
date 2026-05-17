# AIコーディング・開発支援(初版、2026-05-13 PPTX 同期)

slug: `ai-coding`
作成日: 2026-05-13

## 0. このドキュメントの位置付け

ai-coding トピックは、PPTX v3 連動で初版を作成。Codex / Claude Code / Cursor / Devin / Zed 等の AI コーディングツールが業務に侵食する範囲と、SI/コンサル人月モデルへの構造的圧力を継続観察する。

詳細な観察と含意は本ファイル末尾の「2026-05-13 MECE 観察+含意 視点」セクションを参照。

## 1. 自分の問い(_index.md より)

Codex / Claude Code / Cursor / Devin / Zed が業務にどこまで侵食するか。SI/コンサル人月モデルへの構造的圧力はどう進むか。

## 2. キーワード

Codex / Claude Code / Cursor / Devin / Zed / GitHub Copilot / Lovable / Replit / Continue.dev / バイブコーディング / vibe-coding / Forward Deployment / 人月モデル / SI / 成果報酬

## 3. 関連トピック

- `agentic-ai`: コーディングエージェントの記憶・自走力
- `consulting-ai`: SI/コンサル人月モデルへの構造的圧力
- `enterprise-ai`: エンタープライズでのコーディング AI 採用
- `ai-companies`: OpenAI Codex、Anthropic Claude Code、Cursor、Cognition Devin の競争


---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> Codex/Claude Code/Cursor/Devin/Zed が業務に侵食する範囲。SI/コンサル人月モデルへの構造的圧力。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: 開発ツール層はバイブコーディング+自律エンジニアが主流化

**概要**:
- Cursor / Lovable / Zed 1.0 / Replit / vibe-coded widgets が個人開発者層を席巻
- Cognition Devin / OpenAI Codex / Anthropic Claude Code が企業向け自律エージェントを提供
- 「最後まで自走する力」が GPT-5.5 熱狂の鍵に

**事例詳細**:
- Zed 1.0 リリース(2026-05-11、Rust 製 AI 共同編集 IDE)
- Bun が Claude を使って Zig → Rust 移行中(2026-05-11)
- ジョイゾー「スキル39」で kintone を AI 改修(2026-05-12)

#### 観察2: OSS 品質を AI が抜本的に変える実証段階に到達

**概要**:
- Claude Mythos × Firefox で20年前バグ含む271件修正、修正数が約15倍
- GitHub MCP コミット前認証情報スキャンで「うっかりコミット」を防止
- 一方で HackerOne「AI 生成ゴミ脆弱性報告」殺到で受付停止の負の側面も

**事例詳細**:
- Mozilla × Claude Mythos が Firefox 271件のバグ発掘(2026-05-08)
- GitHub MCP Server コミット前スキャン(2026-05-07)
- HackerOne 受付停止(2026-05-11)

#### 観察3: エンタープライズガバナンス層が JetBrains/OpenAI/GitHub で整備期へ

**概要**:
- JetBrains Central、OpenAI「Running Codex safely」で運用ガイドが揃う
- Anthropic Claude Code 利用上限引き上げ(SpaceX DC 経由で計算リソース確保)
- 国内では富士ソフト人月脱却が「AI 駆動 SI」のビジネスモデル先行例

**事例詳細**:
- JetBrains Central(2026-05-08)
- OpenAI Running Codex safely(2026-05-08)
- Anthropic Claude Code 利用上限引き上げ(2026-05-06)

#### 観察4: 人材市場は「Python 一択ではない」へ再編、年収と試験区分が同時変化

**概要**:
- TypeScript 平均年収952万円が Python 857万円を上回る
- 情報処理技術者試験が大改定、応用・高度試験が消滅(2027年度〜)
- 「AI ネイティブ就活生」がエントリーシート・面接練習で AI を当たり前に活用

**事例詳細**:
- INSTANTROOM 調査 TypeScript 952万円(2026-05-08)
- 情報処理技術者試験大改定(2026-05-11、日経クロステック)
- 2027卒 AI ネイティブ就活生調査(2026-05-11)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- OSS 品質革新と人材市場再編が同時進行
- 国内 SI が「人月脱却 vs 規模拡大」で戦略分岐

**事例**:
- 2026-05-12  Google「Create My Widget」vibe-coded widgets
- 2026-05-12  CUDA-oxide(Rust → CUDA 公式コンパイラ、HN 387 pts)
- 2026-05-11  TanStack npm サプライチェーン侵害(HN 685 pts)
- 2026-05-11  「AI なら Python 不要?」HN 326 pts

### 次の注視点

**概要**:
- コーディングエージェントの企業ガバナンス標準化
- SI/コンサル収益モデルへの構造的圧力の定量化

**事例/論点**:
- 富士ソフト成果報酬移行の実数値(2026 Q2 決算)
- 日立 GlobalLogic 統合 × AI 案件の北米成果
- 国内 SI 中堅(TIS/SCSK/BIPROGY/CTC)の人月モデル対応
