# GitHub Pages セットアップ手順(ローカル用メモ)

このディレクトリ(`docs/`)は **GitHub に公開する HTML 専用の git リポジトリ**です。OneDrive 上のソース(notes / synthesis / daily markdown / 生 JSONL)は git 管理外で、生成された HTML だけがここに置かれます。

## 初回セットアップ(一度だけ)

### Step 1: GitHub でリポジトリ作成

1. https://github.com/new を開く
2. 設定:
   - **Repository name**: `ai-news-vault-public`(または好みの名前)
   - **Visibility**: **Public**(GitHub Pages 無料プランで必須)
   - **DO NOT** check "Add a README file"(既にローカルにある)
   - **DO NOT** add .gitignore or license
3. 「Create repository」をクリック

### Step 2: 認証セットアップ

**HTTPS + PAT(推奨、簡単)**:
1. https://github.com/settings/tokens を開く
2. 「Generate new token (classic)」
3. 設定:
   - Note: `ai-news-vault publishing`
   - Expiration: 90 days(または "No expiration"、好みで)
   - Scopes: ☑ `repo`(必須)
4. Generate → トークンをコピー(一度しか表示されないので注意)
5. Windows Credential Manager に保存:
   ```powershell
   git config --global credential.helper manager
   ```
6. 初回 push 時に GitHub Username と PAT を入力 → 自動保存される

**SSH を既に設定済みの場合**: スキップして OK

### Step 3: ローカルからリモート設定 + 初回 push

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\nanan\Downloads\ai-news-vault\scripts\setup_github_remote.ps1
```

対話的に repo 名・ユーザー名・認証方式を聞かれます。

### Step 4: GitHub Pages 有効化

1. リポジトリの **Settings** → **Pages**(左サイドバー)
2. 設定:
   - **Source**: `Deploy from a branch`
   - **Branch**: `main`、フォルダ: `/ (root)`
3. **Save**
4. 1-2 分後、リポジトリ上部に Pages URL が表示される:
   ```
   https://7green-lit.github.io/ai-news-vault-public/
   ```

## 通常運用(セットアップ後)

### 自動更新

Windows Task Scheduler の `AINewsVault_DailyFetch` タスクが**毎日 4/7/9/12 時**に起動:

1. RSS 取得
2. JST 日付ごとに分割
3. **HTML 再生成**(`docs/index.html` を上書き)
4. **git commit + push**(変更があれば)
5. GitHub Pages が自動デプロイ(数十秒〜2分)

PC が眠っていた場合は、起床後の最寄りのトリガーで実行(`StartWhenAvailable: True`)。

### 手動更新

任意のタイミングで生成し直したい場合:

```powershell
# HTML だけ再生成
python C:\Users\nanan\Downloads\ai-news-vault\scripts\generate_topics_overview_html.py

# Daily 取得 + HTML 生成 + push まで一括
powershell -ExecutionPolicy Bypass -File C:\Users\nanan\Downloads\ai-news-vault\scripts\daily_run.ps1
```

### 更新確認

- 公開 URL を再読込(キャッシュ強制更新: Ctrl+F5)
- 右上「Generated: YYYY-MM-DD HH:MM JST」が最新時刻になっていれば成功
- ログ: `daily/raw/_log/YYYY-MM-DD.log`(`[git push] To https://github.com/...` の行があれば push 成功)

## トラブルシューティング

| 症状 | 原因 | 対処 |
|---|---|---|
| push 時に "Authentication failed" | PAT 未登録 or 期限切れ | https://github.com/settings/tokens で再発行 |
| Pages の URL が 404 | 有効化直後の初期化中 | 2-3分待ってリトライ |
| HTML が更新されない | git push が失敗している | `daily/raw/_log/YYYY-MM-DD.log` で `[git push]` 行をチェック |
| 4時に走らない | バッテリー駆動+Modern Standby | 7/9/12時のいずれかで補完される(StartWhenAvailable) |

## ファイル構成

```
ai-news-vault/         (OneDrive、git 管理外)
├── daily/             ← Daily markdown(非公開)
├── topics/            ← トピック synthesis(非公開)
├── scripts/           ← 各種スクリプト(非公開)
└── docs/              ← GitHub Pages 公開対象(別 git リポジトリ)
    ├── .git/          ← git メタデータ
    ├── .nojekyll      ← Jekyll 無効化フラグ
    ├── README.md      ← GitHub リポジトリのトップ表示
    ├── SETUP.md       ← このファイル
    └── index.html     ← 自動生成(全16セクション、約120KB)
```
