# Ultimate 3D Sandbox

**Ultimate 3D Sandbox** は、無限に続く創作都市を歩き、乗り物を運転し、建築し、NPCと会話できる3Dブラウザサンドボックスです。Three.jsを使う単一の静的HTMLとして配信され、ビルド工程やゲームサーバーなしにCloudflare Pagesで動作します。

> 固定ミッションはありません。自由探索、無限チャンク、車両、天候、時刻、テレポート、自動運転、NPC、建築、モバイル操作を一つの自由な街として提供します。

## 主な機能

| 区分 | 内容 |
|---|---|
| 無限都市 | 64×64単位の決定論的チャンクを、プレイヤーまたは操作中の車両の周辺に生成・保持・解放します。固定マップの端はありません。 |
| 統一した操作 | 徒歩と車両のいずれも、**画面の上方向が前進**となるカメラ相対操作です。WASD、矢印キー、モバイルジョイスティックで同じ移動の期待にそろえています。 |
| 衝突 | 建物、City Hubの外壁、配置済みモジュール、車両、屋内壁を軽量な境界判定の対象にします。壁をすり抜けず、移動時は壁沿いに滑るよう解決します。 |
| City Hub | 近傍チャンクに高密度のCity Hubを配置します。入口の近くで`E`または「使う」を選ぶとロビーへ入館でき、退出ゲートで街へ戻れます。ロビーにはカーテンウォール、レセプション、植栽、照明、出口ゲートがあります。 |
| 都市と車両の表現 | 遠景はインスタンシングで軽く保ち、City Hubとプレイヤー車両にはPBR系マテリアル、階層化外壁、窓、庇、植栽、独立した車輪、ガラス、バンパー、フードなどを加えています。 |
| Build Belt | 画面下中央の独自クイックバーで、五つの建築素材、回転、削除、Field Packを即時に操作できます。既存作品のUI・名称・アセットには依存しません。 |
| Field Pack | `Tab`またはBuild Beltから開く創作インベントリです。Turf Deck、Stone Core、Timber Stack、Clear Prism、Alloy Moduleを選択できます。 |
| 建築 | グリッドにスナップするゴースト表示を使い、左クリックで素材別モジュールを配置します。`R`で90度回転し、右クリックまたはRemoveモードで除去できます。セッションごとに最大240個を配置できます。 |
| 全画面ポーズハブ | 右上のポーズ、`Esc`、`P`で**City Pause Hub**を開きます。再開、Field Pack、ワールド、乗り物、会話とAI、操作ガイド、タイトル復帰を一画面に集約しています。 |
| モバイル完全操作 | ジョイスティック、走る、使う、建築、会話、Build Belt、視点、乗り物、マップ、ポーズから全主要機能に到達できます。キーボードを使う端末では移動用モバイルUIを自動で隠し、タッチで再表示します。 |
| NPC行動AI | NPCは道路・歩道を目的地として巡回・散策し、到着時は待機します。プレイヤー、車両、他NPC、配置物への近接を回避し、会話中の状態も持ちます。 |
| Conversation Dock | 左下の広い会話ドックに会話履歴、近隣NPC、活動人数、ローカルAI状態を表示します。モバイルでは初期状態を折り畳み、開いた時は安全領域内で全幅表示します。 |
| 複数ローカルAI | WebGPU対応端末では、明示的にLOCAL AIを開始した後、複数NPCが人格別の履歴を保ちながら自律会話します。プレイヤーの発言には近傍NPCの応答が優先されます。推論は一つのブラウザ内エンジンへ順番に送るため、複数モデルを同時に読み込みません。 |
| 環境と品質 | 天候、時刻、描画距離、軽量・プレミアム・ウルトラ品質を切り替えられます。PCFソフト影、トーンマッピング、近傍影キャスター、描画更新の間引きで軽さと視認性を両立します。 |

## 操作方法

| 操作 | キーボード | タッチ／画面操作 |
|---|---|---|
| 徒歩移動 | `W` `A` `S` `D` または矢印キー | 左下ジョイスティック |
| 走る | `Shift` | 右下の「走る」を長押し |
| 視点操作 | マウスドラッグ | ゲーム画面をスワイプ |
| 視点切替 | メニュー内の視点 | Context Actionsの「視点」 |
| 一時停止 | `Esc`または`P` | 右上の「ポーズ」 |
| 乗車／降車 | 近くの車両で`E` | メニューまたは「使う」 |
| City Hub入退室 | 入口／退出ゲートの近くで`E` | 「使う」 |
| 車両生成 | メニューから車種を選択 | Context Actionsの「乗り物」またはメニュー |
| 素材選択 | Build Beltの`1`〜`5` | Build BeltまたはField Pack内の素材カード |
| 建築モード | `B` | モバイルの「建築」またはメニュー |
| 配置 | 建築モード中に左クリック | 建築モード中に地面をタップ |
| 回転 | `R` | Build BeltのRotate |
| 削除 | 右クリックまたは`7` | Build BeltのRemoveを選び対象をタップ |
| Field Pack | `Tab` | Build BeltのPack |
| NPC会話 | Conversation Dockへ入力して送信 | Conversation Dockを開いて入力・送信 |
| LOCAL AI | Conversation Dockの「LOCAL AIを開始」 | 同左 |
| マップ指定 | City Radarをクリック | City Radarをタップ |

## ローカルAIの利用条件

WebLLMはWebGPUを利用してブラウザ内で推論を行い、OpenAI互換のストリーミングチャットAPIを提供します。[1] 本ゲームでは`Qwen2.5-0.5B-Instruct-q4f16_1-MLC`を、利用者がConversation Dockで明示操作した時だけ読み込みます。公式設定上の必要VRAM目安は約944.62MBです。[2]

LOCAL AIが起動すると、NPCごとの人格・履歴を分けながら一つの推論エンジンを共有します。ゲーム開始時にはモデルを自動ロードしません。WebGPU非対応、モデル取得失敗、端末メモリ不足の場合も、テンプレート会話によるNPC間の発言とプレイヤー応答へフォールバックし、建築・探索・NPC行動を含むゲーム本体は通常どおり利用できます。

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

[3] [Three.js — GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)

[4] [MDN — Bounding Volume Collision Detection with Three.js](https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_collision_detection/bounding_volume_collision_detection_with_THREE.js)

[5] [Three.js — InstancedMesh](https://threejs.org/docs/pages/InstancedMesh.html)

[6] [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/configuration/git-integration/)
