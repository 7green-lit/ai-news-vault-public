# フィジカル AI・AI ロボティクス — 歴史・現状・見通し(2026-05-15 v1 初版)

> 「マルチモーダル・動画生成」トピック(2026-05-01〜2026-05-13)を本日 `_archived/` に退避し、
> その後継として「身体性(フィジカル AI)に焦点を絞った」本トピックを設置。
> マルチモーダルのうち**動画生成・音声・コンテンツ権利**等は `ai-models` / `enterprise-ai` / `ai-regulation` で扱う。

## 0. 自分の問い(_index.md より)

フィジカル AI(ヒューマノイドロボット・産業ロボティクス・自律機械)が物理空間でどんな速度で実用化されるか。
VLA(視覚言語動作)モデルとロボットハードウェアの統合は誰が主導するか。
国産路線 vs 海外大手の競争構造はどう決着するか。

---

## 1. 業界マッピング(2026-05 時点の主要プレイヤー)

| 層 | 海外大手 | 国産 |
|---|---|---|
| **ヒューマノイドスタートアップ** | Figure(Brett Adcock)/ 1X / Optimus(Tesla)/ Apptronik / Sanctuary AI / Agility Robotics | KyoHA(SEIMEI 検証機)、Sony(布石段階) |
| **既存ロボティクス** | Boston Dynamics(Hyundai)/ ABB / KUKA(Midea) | **ファナック・安川電機**(産業ロボ世界トップ)/ 川崎重工 / 三菱電機 / オムロン |
| **AI 基盤(VLA/VLM)** | NVIDIA Isaac / Google Gemini Robotics / DeepMind / OpenAI(Operator)/ Meta(humanoid 買収) | NEC(3D 点群90%軽量化)/ PFN(PLaMo + ロボ) |
| **製造業 × AI 連携** | Mercedes × Apptronik / Hyundai × Boston Dynamics | アクセンチュア × 日本精工 / 三菱電機・オムロン SDA / 尾形哲也 AI ロボット協会 |

---

## 2. 2023〜2025 までの前史(モデル知識ベース)

### 2.1 ヒューマノイド出発点(2023-2024)
- 2023: Tesla Optimus(Gen 1)、Figure 設立、1X 設立
- 2023-2024: Apptronik Apollo、Sanctuary AI Phoenix、Agility Digit
- ChatGPT 後の「LLM × 身体性」期待で大型調達ラッシュ($600M Figure/Microsoft/OpenAI 等)

### 2.2 産業ロボティクスの「フィジカル AI」化(2024-2025)
- Boston Dynamics Atlas 電動化(2024-04)、量産化準備
- NVIDIA Isaac Sim/ROS/Foundation Models で AI 統合プラットフォーム
- ファナック・安川電機が独自 AI(国産基盤)路線を準備
- 三菱電機・オムロン が SDA(Software-Defined Automation)へ転換検討

### 2.3 VLA(Vision-Language-Action)モデルの出現(2024-2025)
- RT-2(Google DeepMind、2023)→ RT-X / OpenVLA(2024)
- Anthropic Computer Use(2024-10、PC GUI の代理操作)
- Physical Intelligence(π0、2024-09)— ロボット向け基盤モデル
- Figure Helix(2025、ヒューマノイド向け統合モデル)

---

## 3. 2026-04〜2026-05 の現状(累計0記事 + 周辺ニュース)

### 3.1 同月の主要動向

#### A. 海外ヒューマノイドスタートアップの量産化準備
- **Meta が humanoid robotics スタートアップ買収**(2026-05-02)→ AI×身体性 に本格参入
- Figure / 1X / Optimus が大型調達 + 工場立ち上げ + パイロット顧客拡大
- Apptronik × Mercedes、Boston Dynamics × Hyundai の OEM 連携が深化

#### B. 国内ヒューマノイドの「構想段階」露呈
- **京都 KyoHA SEIMEI 公開**(2026-05-12、純国産ヒューマノイド検証機)
  - 「**動的デモ未達(足首パーツ破損)**」を隠さず公開、覚悟を示す姿勢
- **Sony CEO「TSMC 提携 + フィジカル AI 布石」**(2026-05-12)
  - 半導体メモリ供給不足を踏まえつつ、将来戦略として明示

#### C. 産業ロボティクスの「国産基盤死守」戦略
- **ファナック・安川電機フィジカル AI 表明**(2026-05-11、日経ビジネス特集)
  - 「**国産基盤で情報資源死守**」を公式キーワードに
- **三菱電機・オムロン SDA でデータ事業へ転換**(2026-05-12)
  - 欧米FA大手3社の「ソフト継続課金」転換に対抗
- 欧米FA大手の「ハード売り切り → ソフト課金」継続課金転換(2026-05-12)

#### D. AI 基盤レイヤ(VLA/VLM)の競争
- **NEC 独自 AI で 3D 点群90%軽量化**(2026-05-12、世界初)
  - フィジカル AI 連動、車載・ロボット・建築 BIM 等の応用
- **DeepMind co-clinician**(医療補助 AI、2026-05-01)
- **尾形哲也 AI ロボット協会**(AI とロボットの共進化、2026-05-03)

---

## 4. 横断視点 — 4軸分化仮説

| 軸 | 担い手 | 競争優位 | リスク |
|---|---|---|---|
| **ヒューマノイドB2C 量産化** | Figure / 1X / Optimus / Apptronik / Boston Dynamics | 大型資金 + 米国製造拠点 + AI 統合スピード | 量産時の品質・コスト課題、法的責任未整理 |
| **産業ロボB2B 既存統合** | ファナック / 安川 / KUKA / ABB | 数十年の現場知見 + グローバル販路 | SDA 化遅延、ハード売切り依存からの脱却 |
| **VLA/VLM 基盤モデル** | NVIDIA Isaac / DeepMind / Figure / Physical Intelligence | AI 性能 + シミュレーション環境 + データ規模 | 物理的安全性、ロボハードとの統合難易度 |
| **データ主権・国産基盤** | ファナック・安川・KyoHA・Sony・PFN・NEC | 産業政策的追い風 + 国内製造業との信頼関係 | グローバル展開での競争力、量産投資 |

---

## 5. 国内 vs 海外 — 構造比較

| 観点 | 海外(米欧) | 日本 |
|---|---|---|
| ヒューマノイド量産化 | 2026 量産化準備(Figure/1X/Apptronik) | 検証機段階(KyoHA SEIMEI、Sony 布石) |
| 産業ロボティクス | OEM 連携深化(Boston × Hyundai 等) | 国産基盤死守(ファナック・安川)+ SDA(三菱・オムロン) |
| AI 基盤モデル | NVIDIA Isaac / DeepMind / Figure Helix | NEC(3D 点群)/ PFN(PLaMo + ロボ) |
| データ主権 | 課題意識低、データ集約集中 | 強い課題意識、国内 AI ベンダー連携機運 |
| 産業政策 | 個別連携・PE 主導 | 国産基盤推進、日本初 AI 法律と整合 |

**国内の特殊性**:
1. **既存産業ロボ世界トップ**(ファナック・安川)を抱えながら、ヒューマノイドでは出遅れ
2. **データ主権意識が強い** → 海外大手に「動作データを渡さない」設計を選好
3. **AI 基盤(国産 LLM)とロボの接続**は技術的にはこれから、産業政策的に追い風

---

## 6. 見通し

### 6.1 短期(2026 Q3-Q4)
- Figure / 1X / Optimus の **量産モデル発表**(数万台レベルの製造ライン公開)
- 三菱電機・オムロンの **SDA プロダクト具体化**
- KyoHA SEIMEI の **動的デモ達成**(足首問題解決後)
- Sony フィジカル AI **具体プロダクト**(PSN 生みの親未来予想図、2026-05-11 の延長)

### 6.2 中期(2027)
- ヒューマノイドの **B2C 量産化開始**(住宅・介護・店舗向け)
- ファナック・安川 × 国産 AI(PFN/Sakana)**正式連携プロダクト**
- VLA モデル × ロボハード統合の **業界標準化**(プロトコル協議)

### 6.3 長期(2028+)
- ヒューマノイド + 産業ロボの **ハイブリッド工場**標準化
- AGI 級モデル × フィジカル AI で「**自律産業システム**」の前段に到達
- 国産路線が **製造業 × AI 主権**で独自ポジション確立 or 海外大手に吸収

---

## 7. まだ分かっていないこと

1. **ヒューマノイド量産時のコスト**: Figure / 1X / Optimus の単価予測幅が広い($20K-$200K)
2. **VLA モデル × 既存ロボの統合速度**: ファナック・安川が NVIDIA Isaac を受容するか独自路線か
3. **データ主権 × 連邦学習**: 国産基盤死守と AI 性能向上の両立方法
4. **規制対応**: ヒューマノイドの労働安全衛生、PL 法、責任分界
5. **ソニーの具体戦略**: PSN 生みの親「未来予想図」の具体プロダクトロードマップ
6. **物流×フィジカル AI**: `logistics-ai` トピックとの境界(本トピックは「身体性」、logistics は「業務」)

---

## 8. 関連トピック横断視点

- `logistics-ai`: 倉庫ピッキング・配送ラストマイル等の業務応用
- `ai-companies`: NVIDIA / Figure / 1X / Apptronik / Boston Dynamics / Sony の企業動向
- `ai-data-structuring`: ロボット動作データ・センサーデータの構造化(VLA 学習データ規格)
- `ai-models`: VLA / VLM 等の基盤モデル進化(現状 `ai-models` 比較表は GPT/Claude/Gemini のみ、今後 VLA も追加余地)
- `enterprise-ai`: 製造業 × フィジカル AI の ROI(三井化学労災6割減、ダイセル 1.3倍 等)

---

## 9. 次に追うべきソース・キーワード

- **海外大手**: Figure(Brett Adcock)、1X、Tesla Optimus、Apptronik、Boston Dynamics、Sanctuary AI、Agility Robotics
- **国産**: ファナック、安川電機、川崎重工、三菱電機、オムロン、Sony、KyoHA、PFN(PLaMo + ロボ)、ZMP
- **AI 基盤**: NVIDIA Isaac、DeepMind、Physical Intelligence(π0)、Figure Helix、Google Gemini Robotics
- **業界団体**: AI ロボット協会(尾形哲也)、ロボット革命・産業 IoT イニシアティブ(RRI)、日本ロボット工業会

---

> 次回 synthesis 更新: 累計5記事到達時、または「contradicts」判定の記事追加時。
