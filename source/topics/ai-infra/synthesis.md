# AIインフラ・GPU・コスト(初版、2026-05-13 PPTX 同期)

slug: `ai-infra`
作成日: 2026-05-13

## 0. このドキュメントの位置付け

ai-infra トピックは、PPTX v3 連動で初版を作成。GPU / データセンター / 半導体の地政学が
AI 産業の競争を決定する局面で、コスト下落 vs 使用量爆発の均衡点を継続観察する。

詳細な観察と含意は本ファイル末尾の「2026-05-13 MECE 観察+含意 視点」セクションを参照。

## 1. 自分の問い(_index.md より)

GPU/データセンター/半導体の地政学が AI 産業の競争を決定する局面。コスト下落 vs 使用量爆発の均衡点。

## 2. キーワード(自動振り分け用)

GPU / NVIDIA / Arm / x86 / Intel / AMD / Stargate / SpaceX / Terafab / SpaceX × Anthropic /
TPU / Willow / 量子 / Jevons パラドックス / 銅鉱山 / 半導体メモリ / ネオクラウド / CoreWeave / Lambda

## 3. 関連トピック

- `ai-companies`: NVIDIA / Microsoft / Google / Amazon / SpaceX の戦略
- `ai-regulation`: NVIDIA 独占への独禁法調査、AI 物資争奪の地政学
- `ai-data-structuring`: Sovereign Cloud / データ基盤との接点
- `ai-models`: 推論コストとモデル効率の関係


---

## 2026-05-13 MECE 観察+含意 視点(PPTX v3 連動)

> 関連 PPTX: [topics-overview-2026-05-13-v3.pptx](../_meta/topics-overview-2026-05-13-v3.pptx)
> 関連潮流: [2026-05-13 AI業界の3つの大潮流](../../daily/_synthesis/2026-05-13-trends.md)
> 関連 Daily: [2026-05-13](../../daily/2026-05-13.md)

### 自分の問い(_index.md より)

> GPU/データセンター/半導体の地政学が AI 産業の競争を決定する局面。コスト下落 vs 使用量爆発の均衡点。

### 問い検証視点での観察と含意(MECE 3-4 論点)

#### 観察1: GPU/半導体層は NVIDIA 独占に Arm 連合 + SpaceX が割り込み

**概要**:
- Arm × Meta「AGI CPU」で x86 → Arm 系データセンター CPU 拡大
- SpaceX Terafab $55B(Texas)で Musk が独自 AI 半導体メーカーへ
- Intel 1.8nm Intel 18A で低価格 MPU まで最先端化

**事例詳細**:
- SpaceX Terafab $55B(2026-05-08)
- Arm × Meta AGI CPU 共同開発(2026-05-08)
- Intel 株 490%上昇 + 1.8nm 全面化(2026-05-12)

#### 観察2: データセンター層は「Pentagon 不在の Anthropic が Musk DC 借用」など政治と物理が交錯

**概要**:
- SpaceX × Anthropic で Musk が「evil」呼ばわりした Anthropic に GPU 提供
- Google × SpaceX で軌道上 AI データセンターの協議(地球外進出)
- AWS 中東 UAE 復旧に数カ月、紛争影響でクラウド可用性が地政学に依存

**事例詳細**:
- SpaceX × Anthropic データセンター提携(2026-05-06〜07)
- Google × SpaceX 軌道上 AI DC 協議(2026-05-12)
- AWS UAE 復旧2カ月ぶり報告(2026-05-06)

#### 観察3: コスト動学は「単価90%下落 + 使用量爆発」のJevons パラドックスへ

**概要**:
- Gartner 2030年に1兆パラメータ LLM 推論コスト90%下落予測
- ただしエージェント普及で総支出は増加、ROI 計算が複雑化
- Sakana × NVIDIA TwELL 30%高速化など効率改善が並走

**事例詳細**:
- Gartner「推論90%下落+総支出増」予測(2026-05-12)
- Sakana × NVIDIA TwELL(2026-05-10)
- Cloudflare 1,100 解雇で AI 効率化と過去最高売上が両立(2026-05-08)

#### 観察4: 資源・電力層が「銅・水・電力」の争奪戦化

**概要**:
- Amazon が銅鉱山と直接契約、米テック大手の物資争奪が本格化
- Everpure CEO「半導体メモリ4-10倍急騰」で価格70%値上げ
- Stargate / SoftBank Roze / NTT データセンター譲渡で日本も巻き込まれる

**事例詳細**:
- Amazon 銅鉱山と直接契約(2026-05-11)
- Everpure 半導体4-10倍急騰(2026-05-11)
- NTT データG データセンター譲渡で51%増益(2026-05-08)

### 直近の重要シグナル(2026-04〜2026-05)

**概要**:
- AI インフラの地政学化と物理コスト爆発が同時進行
- 宇宙データセンターという新フロンティア論議が始動

**事例**:
- 2026-05-12  Google × SpaceX 軌道上 DC 協議
- 2026-05-12  Google TPU 8i/8t + Willow 量子
- 2026-05-12  Cloud Storage Rapid / クラウド Q1 35%成長
- 2026-05-11  Amazon 銅鉱山直接契約

### 次の注視点

**概要**:
- NVIDIA 独占への独禁法調査(FTC/EC)の動向
- Jevons パラドックスの企業財務影響

**事例/論点**:
- 国内 AI インフラ供給(NTT/SoftBank/ファナック・安川)の主権度合い
- 宇宙 DC の実現可能性とコスト推移
- 半導体争奪戦下のサプライチェーン再編
