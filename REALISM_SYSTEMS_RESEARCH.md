# Realism Systems Research and Integration Plan

## 調査の結論

今回の更新では、既存の単一HTML・静的Cloudflare Pages構成を保つ。3Dモデルを大量に外部ロードするのではなく、近傍の重要建物、車両、入り口、屋内空間をPBR対応の複合プロシージャルメッシュで高密度化し、遠景チャンクは既存インスタンシングを維持する。この分離により、タイトル画面の明るい都市アート方向へ近づけながら、無限チャンクの描画負荷を制御する。

| 項目 | 調査結果 | 統合方針 |
|---|---|---|
| 高品質モデル | Three.jsの`GLTFLoader`はglTF 2.0およびPBR関連の拡張を扱える。[1] | 将来のglTF差し替えを可能にする設計にしつつ、今回は依存・通信量を増やさない複合メッシュを使う。 |
| PBR品質 | glTFは金属度、粗さ、透過、エミッシブなどのPBR属性を扱える。[2] | 建物の外壁、窓、車体、屋内設備へ`MeshStandardMaterial`／`MeshPhysicalMaterial`相当の材質差を導入する。 |
| 衝突判定 | `Box3.setFromObject`は子メッシュを含む変換後の境界を計算でき、`intersectsBox`でAABB同士を判定できる。[3] | チャンク生成時に建物・配置物の足元矩形を登録し、プレイヤー・車両の移動候補を軽量な2D AABBで判定する。 |
| ローカルAI | WebLLMはブラウザ内のWebGPU推論、非同期初期化、OpenAI互換チャット補完、ストリーミングに対応する。[4] | 複数エンジンを同時起動せず、**1個のローカル推論エンジン**へキューを設け、NPCごとの人格・会話履歴を分離する。 |

## 統合設計

車両は徒歩と同じ「画面上方向＝前進」のカメラ相対方向を使い、ハンドル入力は速度に応じて旋回する。既存の車両回転軸に依存した符号差は廃止し、前進ベクトルをカメラ基準へそろえる。プレイヤーと車両の移動は、候補位置を衝突登録済みの建物・配置物・屋内壁と照合してから確定する。歩道や道路には進入でき、壁、車両、建築モジュールには侵入できない。

建物内探索は、入り口を持つ「City Hub」建物を近傍チャンクに決定論的に出現させる。入口に近づくと`E`またはモバイルのインタラクトボタンが有効化され、屋内ロビー、階段、窓、照明、家具を持つ専用空間へ遷移する。屋内は退出ポータルを持ち、入口へ戻る。歩行・車両とも屋内壁をすり抜けない。

一時停止は従来の小型カードを廃止し、ポーズボタンから全画面の「City Pause Hub」を開く。ここに再開、Field Pack、ワールド、車両、会話、操作ガイド、タイトルへ戻る導線を集約し、従来の右上メニューボタンは補助表示のみとする。

モバイルには、建築、削除、回転、Field Pack、乗降／屋内入室、会話欄開閉、ポーズ、視点切替のすべてに画面操作を設ける。キーボード入力を検知した端末では、最後の入力から一定時間モバイルジョイスティックを隠し、タッチ入力で直ちに再表示する。入力方式が変わっても機能差は設けない。

LOCAL AIは利用者の明示的な起動後にのみ推論する。起動済みなら、近くにいる複数NPCが短い間隔で一対一の会話を始める。各NPCは個別の人格・直近発話を保持し、AI要求は直列化する。プレイヤーの発話は近傍会話の文脈に追加され、そのNPCが優先して返答する。WebGPU未対応時やモデル未起動時は、現在の端末内テンプレート会話を複数NPC間にも適用する。

## 参照

[1] [Three.js — GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html)

[2] [Khronos — glTF, the 3D Asset Delivery Format](https://www.khronos.org/gltf/)

[3] [MDN — Bounding Volume Collision Detection with Three.js](https://developer.mozilla.org/en-US/docs/Games/Techniques/3D_collision_detection/Bounding_volume_collision_detection_with_THREE.js)

[4] [WebLLM — Basic Usage](https://webllm.mlc.ai/docs/user/basic_usage.html)
