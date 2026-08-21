# Ultimate 3D Sandbox

**Ultimate 3D Sandbox** は、ブラウザ上で自由に街を歩き、視点・天候・時間・NPC・自動移動を調整し、車両や配置オブジェクトを扱える3Dサンドボックスです。単一の静的HTMLとして配信されるため、ビルド工程やサーバーを必要とせず、Cloudflare Pages上でそのまま動作します。

> この更新では、前コミット版の**自由探索・視点切替・キャラクター変更・マップ指定のテレポート／自動運転・NPC数／NPCチャット・描画距離・天候・時間・モバイル操作・チャット**を保持し、固定ミッション要素は採用していません。

## 機能

| 区分 | 内容 |
|---|---|
| 自由探索 | 徒歩でのWASD／矢印キー移動、走行、三人称・一人称・フリールック視点、マウス／タッチでのカメラ操作を提供します。 |
| ナビゲーション | ミニマップクリックで目的地を指定できます。テレポート、経路探索、自動運転、自動運転中の走行設定を利用できます。 |
| NPCとチャット | NPC数と会話頻度を調整でき、プレイヤーとNPCの発言は画面内ログと吹き出しで表示されます。 |
| 環境 | 天候（晴れ・くもり・雨・雪）、時刻、描画距離をリアルタイムに変更できます。夜間には街灯とビルの発光表現が切り替わります。 |
| 車両 | クルーザー、スポーツカー、ホバーバイクを生成して乗車できます。運転中はWASD／矢印キーで加減速・操舵し、`E` で降車します。交通車両は表示・停止を切り替えられます。 |
| ワールド編集 | 配置モードで地面をクリックし、色と高さがランダムなブロックを追加できます。配置済みブロックは一括削除できます。 |
| UIアイコン | [Bootstrap Icons v1.13.1](https://icons.getbootstrap.com/) の公式SVGスプライトを同梱し、車両・カメラ・配置・ヘルプなどの操作ボタンに使用しています。[1] [2] |

## 操作方法

| 操作 | キー／ジェスチャー |
|---|---|
| 徒歩移動 | `W` `A` `S` `D` または矢印キー |
| 走る | `Shift` |
| 視点操作 | ゲーム画面をマウスドラッグまたはタッチスワイプ |
| 視点切替 | 左側パネルの「視点切り替え」 |
| マップ指定 | 右上ミニマップをクリック |
| 乗車／降車 | 乗り物の近くで `E`、または「乗車／降車」ボタン |
| 車両生成 | 左側パネルで車種を選び、「乗り物を出す」 |
| 車両運転 | 乗車中に `W` `A` `S` `D` または矢印キー |
| 配置モード | 「ブロック配置」または `B`。有効時、ゲーム画面の地面をクリック |
| 配置を削除 | 「配置を消す」 |

## ローカル確認

プロジェクト直下をHTTPサーバーで配信してください。ES Modulesを使用するため、`file://` で直接開くのではなくHTTP経由で確認します。

```bash
python3 -m http.server 4173
```

起動後、`http://localhost:4173/` を開きます。

## Cloudflare Pages

本リポジトリは静的HTMLサイトです。既存のCloudflare Pagesプロジェクト `ultimate-3d-game` は `main` ブランチを本番として監視しており、GitHubへのプッシュごとに自動デプロイされます。[3] 公開先は [ultimate-3d-game.pages.dev](https://ultimate-3d-game.pages.dev/) です。

| 項目 | 設定 |
|---|---|
| Pagesプロジェクト | `ultimate-3d-game` |
| 本番ブランチ | `main` |
| ビルドコマンド | なし（静的HTMLを直接配信） |
| 出力ディレクトリ | リポジトリ直下 |
| SVGアイコン | `assets/bootstrap-icons.svg`（Bootstrap Icons v1.13.1／MIT） |

## 技術構成

| 区分 | 採用内容 |
|---|---|
| 3D描画 | [Three.js](https://threejs.org/) `r157` と公式アドオン |
| UI | フレームワーク不要のHTML/CSS/JavaScript |
| SVGアイコン | Bootstrap Icons `v1.13.1` の公式SVGスプライト |
| インフラ | Cloudflare Pages + GitHub連携 |

## 参考資料

[1] [Bootstrap Icons — Official site](https://icons.getbootstrap.com/)

[2] [Bootstrap Icons v1.13.1 release](https://github.com/twbs/icons/releases/tag/v1.13.1)

[3] [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
