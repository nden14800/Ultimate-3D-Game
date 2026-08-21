# Ultimate 3D Sandbox

**Ultimate 3D Sandbox** は、ブラウザ上で無限に続く創作都市を歩き、乗り物を運転し、街を建築できる3Dサンドボックスです。Three.jsによる単一の静的HTMLとして配信されるため、ビルド工程やバックエンドを必要とせず、Cloudflare Pagesでそのまま動作します。

> 固定ミッションは採用していません。自由探索、無限チャンク、車両、天候、時刻、テレポート、自動運転、NPC、モバイル操作を維持したまま、独自の建築・会話システムを拡張しています。

## 主な機能

| 区分 | 内容 |
|---|---|
| 無限都市 | 64×64単位の決定論的な都市チャンクを、プレイヤーまたは操作中の車両周辺に生成・保持・解放します。固定マップの端はありません。 |
| 自由探索 | WASD／矢印キー／モバイルジョイスティックによるカメラ相対移動を提供します。三人称・一人称・フリールックを切り替えられます。 |
| Build Belt | 画面下中央の独自クイックバーで、五つの建築素材、回転、削除、Field Packを即時に操作できます。既存作品のUI・名称・アセットには依存しません。 |
| Field Pack | `Tab`またはBuild Beltから開く創作インベントリです。Turf Deck、Stone Core、Timber Stack、Clear Prism、Alloy Moduleを選択できます。 |
| 建築 | グリッドにスナップするゴースト表示を使い、左クリックで素材別モジュールを配置します。`R`で90度回転し、右クリックまたはRemoveモードで除去できます。セッションごとに最大240個を配置できます。 |
| 明るい都市表現 | タイトルとプレイ中で、青空、緑地、淡い暖色・寒色の建築、明るい道路を共有するアート方向に統一しています。遠景の建築はインスタンシングで描画します。 |
| 車両 | クルーザー、スポーツカー、ホバーバイクを出現させ、近づいて`E`で乗降できます。交通車両の有効・無効も切り替えられます。 |
| NPC行動AI | NPCは道路・歩道を目的地として巡回・散策し、到着時は待機します。プレイヤー、車両、他NPC、配置物への近接を回避し、会話中の状態も持ちます。 |
| Conversation Dock | 左下の広い会話ドックに会話履歴、近隣NPC、活動人数、ローカルAI状態を表示します。NPCの発言はワールド内の吹き出しにも反映されます。 |
| 任意起動ローカルAI | WebGPU対応端末では、Conversation Dockの**LOCAL AIを開始**からWebLLMを明示的に起動できます。モデル推論はブラウザ内で行われ、APIキーやゲームサーバーは使用しません。[1] [2] |
| 環境と品質 | 天候、時刻、描画距離、軽量・プレミアム・ウルトラ品質を切り替えられます。PCFソフト影、トーンマッピング、近傍影キャスター、描画更新の間引きで軽さと視認性を両立します。 |

## 操作方法

| 操作 | キー／操作 |
|---|---|
| 徒歩移動 | `W` `A` `S` `D` または矢印キー。画面上方向が常に前進するカメラ基準操作です。 |
| 走る | `Shift`。徒歩は16 km/h、走行は64 km/hです。 |
| モバイル移動 | 左下ジョイスティック。右下の「走る」を長押しすると走ります。 |
| 視点操作 | ゲーム画面のマウスドラッグまたはタッチスワイプ。 |
| 視点切替 | Context Actionsまたはメニュー内の「視点」。 |
| 一時停止 | 右上の「ポーズ」、または `Esc`／`P`。 |
| 乗車／降車 | 乗り物の近くで`E`、またはメニューの乗車／降車ボタン。 |
| 車両生成 | メニューから車種を選び「乗り物を出す」、またはContext Actionsの「乗り物」。 |
| 素材選択 | Build Beltの`1`〜`5`、またはField Pack内の素材カード。選択時に建築モードになります。 |
| 建築モード | `B`でオン・オフ。ゴーストがシアンなら配置可能、赤なら近接物との干渉などで配置不可です。 |
| 配置 | 建築モード中に左クリック。 |
| 回転 | `R`またはBuild BeltのRotate。90度ずつ向きが変わります。 |
| 削除 | 右クリック、またはBuild BeltのRemoveを選んで左クリック。 |
| Field Pack | `Tab`またはBuild BeltのPack。 |
| NPC会話 | Conversation Dockへ入力して送信。LOCAL AI未起動・未対応・ロード失敗時は端末内のテンプレート会話へ安全にフォールバックします。 |
| LOCAL AI | Conversation Dockの「LOCAL AIを開始」。初回のみモデル取得に時間がかかる場合があります。ゲーム起動時に自動ロードはしません。 |
| マップ指定 | 右下のCity Radarをクリック。テレポート設定時は即時移動、通常時は目的地設定です。 |

## ローカルAIの利用条件

WebLLMはWebGPUを利用してブラウザ内で推論を行い、OpenAI互換のストリーミングチャットAPIを提供します。[1] 本ゲームでは低リソース対応として登録されている`Qwen2.5-0.5B-Instruct-q4f16_1-MLC`を、ユーザーの明示操作時だけ読み込みます。公式設定上の必要VRAM目安は約944.62MBです。[2]

このため、LOCAL AIはネットワーク上の生成APIを呼び出さず、APIキーも不要です。ただし、初回のモデル取得、WebGPU対応、端末メモリ、ブラウザの設定には依存します。条件を満たさない場合も、建築・探索・NPC行動を含むゲーム全体は通常どおり利用できます。

## パフォーマンス設定

| プリセット | 主な設定 | 推奨用途 |
|---|---|---|
| 軽量 | 最大1.2倍ピクセル比、影なし、NPC上限80、既定半径1チャンク | 動作の軽さを最優先する場合。 |
| プレミアム（推奨） | 最大1.65倍ピクセル比、1024px PCFソフト影、NPC上限120、既定半径2チャンク | 画質と軽さのバランスを取る場合。 |
| ウルトラ画質 | 最大2.0倍ピクセル比、1536px PCFソフト影、NPC上限180、既定半径3チャンク | GPU性能に余裕がある場合。 |

## ローカル確認

ES Modulesを使うため、`file://`ではなくHTTPサーバーで確認してください。

```bash
python3 -m http.server 4173
```

起動後、[http://localhost:4173/](http://localhost:4173/) を開きます。検証用には、JavaScript構文、DOM参照、Bootstrap Iconsスプライト、WebLLMモジュールURLを確認する`validate_refresh.py`も用意しています。

```bash
python3 validate_refresh.py
```

## Cloudflare Pages

本リポジトリは静的HTMLサイトです。Cloudflare Pagesプロジェクト`ultimate-3d-game`は`main`ブランチを本番として監視し、GitHubへのプッシュごとに自動デプロイされます。[6] 公開先は[ultimate-3d-game.pages.dev](https://ultimate-3d-game.pages.dev/)です。

| 項目 | 設定 |
|---|---|
| Pagesプロジェクト | `ultimate-3d-game` |
| 本番ブランチ | `main` |
| ビルドコマンド | なし（静的HTMLを直接配信） |
| 出力ディレクトリ | リポジトリ直下 |
| 3D描画 | Three.js `r157` と公式アドオン |
| UIアイコン | `assets/bootstrap-icons.svg`（Bootstrap Icons v1.13.1／MIT） |

## 参考資料

[1] [WebLLM — Basic Usage](https://webllm.mlc.ai/docs/user/basic_usage.html)

[2] [WebLLM official model configuration](https://raw.githubusercontent.com/mlc-ai/web-llm/main/src/config.ts)

[3] [Three.js — InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)

[4] [Three.js — Cleanup](https://threejs.org/manual/en/cleanup.html)

[5] [Roblox Creator Hub — UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)

[6] [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
