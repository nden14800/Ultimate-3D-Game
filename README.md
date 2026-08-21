# NEON HORIZON — 3D City Explorer

**NEON HORIZON** は、ブラウザだけで起動する軽量な3Dシティ探索ゲームです。プレイヤーは近未来の都市を歩き、天候・時刻・カメラを変えながら、散らばった信号ビーコンを調査します。サーバー、ビルド工程、ユーザー登録を必要としない完全な静的サイトとして構成しています。

> 現行の公開先は [ultimate-3d-game.pages.dev](https://ultimate-3d-game.pages.dev/) です。`main` ブランチへの反映後は、Cloudflare PagesのGit連携により本番デプロイが自動で実行されます。[1]

## 主な機能

| 領域 | 実装内容 |
|---|---|
| 探索体験 | 三人称チェイス／俯瞰カメラ、WASD・矢印キー移動、走行、マウス・タッチの視点操作を提供します。 |
| ミッション | 都市内の3つの黄色いビーコンに近づき、`E` キーで同期する短い探索目標を実装しています。 |
| 都市演出 | 時刻による空・霧・太陽光の変化、雨・雪・曇天、車両と歩行者、ランドマーク、ミニマップを備えます。 |
| パフォーマンス | 建物・街灯・植生はインスタンシング中心で描画し、品質選択とピクセル比の上限で幅広い端末に対応します。`InstancedMesh` は描画呼び出しの削減に適したThree.jsの公式機能です。[2] |
| UX・アクセシビリティ | 起動画面、設定、キーボードショートカット、モバイル向けレイアウト、ARIAラベル、WebGL失敗時のフォールバックを実装しています。 |

## 操作方法

| 操作 | キー／ジェスチャー |
|---|---|
| 移動 | `W` `A` `S` `D` または矢印キー |
| 走る | `Shift` |
| 視点操作 | ゲーム画面をドラッグ、またはマウスホイールでズーム |
| カメラ切替 | `C` |
| ビーコン同期 | `E` |
| ミッションの再初期化 | `R` |
| 一時停止 | `P` |

## ローカルでの確認

このリポジトリは `index.html` を入口とする静的サイトです。任意のローカルHTTPサーバーでプロジェクト直下を配信してください。ES Modulesの仕様上、`file://` で直接開くのではなくHTTP経由で確認します。

```bash
python3 -m http.server 4173
```

起動後、`http://localhost:4173` を開きます。Pythonがない環境では、同等の静的ファイルサーバーを利用してください。

## Cloudflare Pages

Cloudflare Pagesは静的HTMLサイトをそのまま配信でき、GitHubリポジトリと接続したPagesプロジェクトではブランチへのプッシュごとにビルド・デプロイを行えます。[1] [3] このリポジトリの既存プロジェクトは以下の設定です。

| 項目 | 設定 |
|---|---|
| Cloudflare Pagesプロジェクト | `ultimate-3d-game` |
| 本番ブランチ | `main` |
| 公開URL | `https://ultimate-3d-game.pages.dev/` |
| ビルドコマンド | なし（静的HTMLを直接配信） |
| 出力ディレクトリ | リポジトリ直下 |

## 技術構成

| 区分 | 採用内容 |
|---|---|
| 3D描画 | [Three.js](https://threejs.org/) `r160.1`（ES Module） |
| アプリ構造 | フレームワーク不要の単一HTMLエントリ、純粋なJavaScript |
| インフラ | Cloudflare Pages + GitHub連携 |
| 外部アセット | Three.js CDNのみ。画像・音声・追跡SDK・サーバーAPIは使用しません。 |

## 参考資料

[1] [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)

[2] [Three.js — InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)

[3] [Cloudflare Pages — Static HTML](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/)
