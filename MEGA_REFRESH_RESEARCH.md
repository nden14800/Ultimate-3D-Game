# 大規模刷新に関する公式調査記録

## UI・UX設計

Roblox Creator HubのUI/UX資料は、ゲームUIを情報階層、注意誘導、視覚言語、慣習、一貫性で最適化することを勧めている。[1] 特に、プレイヤーの文脈に必要な操作だけを提示して混雑を避けること、色・サイズ・余白・近接で注意を制御すること、閉じる`X`や無効状態の灰色表示などの一般的な慣習を一貫して使うことを重視している。[1]

今回のUIでは、ゲーム中は最小限のHUDと小さな「ULTIMATE 3D SANDBOX」展開ボタンだけを表示し、ポーズ、ガイド、設定、マップ、NPC会話はそれぞれ全画面として扱う。全画面画面は共通の見出し、左上の文脈説明、右上の閉じる操作、主操作の強い視覚優先度を持つ。近接する車両・建物・NPCには、`E`／「使う」形式の文脈プロンプトを採用する。[1]

## 公開3Dアセットの判断

Poly Havenは、テクスチャ、HDRI、3DモデルをCC0として公開しており、商用利用・再配布・製品への同梱ができ、帰属表示を要求しないと説明している。[2] KenneyのCar Kitは45種類の3D輸送アセットをCreative Commons CC0で配布している。[3] KhronosのglTF Sample Assetsは、モデルごとにライセンス情報を示し、glTF機能の検証・統合を目的としたキュレーションされた公開モデル集である。[4]

本ゲームは単一HTML・静的配信・モバイル性能を維持する必要があるため、近傍の重要車両・公共交通・City Hubのみに高密度メッシュまたはCC0 PBR素材を使い、遠景はインスタンシングを保つ。モデルを導入する場合にはライセンス情報がCC0である個別アセットだけを採用し、不要な巨大ファイルは避ける。

## 参考資料

[1] [Roblox Creator Hub — UI and UX design](https://create.roblox.com/docs/production/game-design/ui-ux-design)

[2] [Poly Haven — Asset License](https://polyhaven.com/license)

[3] [Kenney — Car Kit](https://kenney.nl/assets/car-kit)

[4] [Khronos — glTF Sample Assets](https://github.khronos.org/glTF-Assets/)

## 高性能ローカルAIと持続キャッシュ

WebLLMは`CreateMLCEngine()`または`MLCEngine.reload()`でモデルを非同期に読み込む。初回のモデル取得には時間がかかるため、進捗コールバックを表示することが公式に推奨されている。[5] WebLLMの公式設定では既定のキャッシュバックエンドはCache APIであり、Cache APIが最も検証済みとされる。[6] ChromeのAI on the web資料も、モデルの持続キャッシュにCache APIを推奨し、初回以外の読み込みを速くすること、`navigator.storage.persist()`で永続化を要求できることを説明している。[7]

現行の0.5Bモデルは高速だが会話品質に限界があるため、選択可能な標準モデルを追加する。既定はモバイル互換の`Qwen2.5-0.5B-Instruct-q4f16_1-MLC`、高品質は`Hermes-3-Llama-3.2-3B-Instruct-q4f16_1-MLC`（公式設定で約2263.69MBのVRAM目安）、最高品質は`Llama-3.1-8B-Instruct-q4f16_1-MLC`（約5001MB）とし、端末での初期化失敗時には一段小さいモデルまたはテンプレート会話へフォールバックする。[6] モデルの選択、ダウンロード完了、永続化の状態を`localStorage`へ保存し、WebLLM自体が使うCache APIと併用する。従って同一モデルを選んだ次回以降は、ブラウザの保存領域が残っている限り、再ダウンロードを回避できる。

[5] [WebLLM — Basic Usage](https://webllm.mlc.ai/docs/user/basic_usage.html)

[6] [WebLLM — Official model configuration](https://raw.githubusercontent.com/mlc-ai/web-llm/main/src/config.ts)

[7] [Chrome for Developers — Cache models in the browser](https://developer.chrome.com/docs/ai/cache-models)

## 描画、品質、実測FPS

Three.jsの`MeshStandardMaterial`はMetallic-Roughnessワークフローの物理ベース材質であり、より正確な見た目を得られる一方、旧来のLambert/Phong材質より計算量が増える。公式資料は、最良の結果のために環境マップを指定することを勧めている。[8] `WebGLRenderer`は出力色空間、トーンマッピング、露出、影マップ、フレーム当たりのdraw callsと三角形数を含む`renderer.info`を提供する。[9]

実装では、最低品質は適度な解像度・限定影・簡略化した雲と樹木、中間品質はPCFソフト影と高密度の近傍モデル、最高品質は高いピクセル比、PBR素材、近傍の高解像度影、改善された空・雲・霧・環境反射を適用する。無限都市全体に高価な影をかけず、プレイヤー周辺だけをシャドーキャスターにする。FPSは表示用の固定値ではなく、`requestAnimationFrame`の実測時間を指数平滑化して1秒単位でHUDへ表示し、draw callsも`renderer.info.render.calls`から取得する。[9]

[8] [Three.js — MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html)

[9] [Three.js — WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html)

## Phase 5: 車両・公共交通の実装根拠

Three.jsの車両物理サンプルでは、ホイール軸・駆動・追従カメラを分離して扱い、キーボード入力とフレーム時間を用いた更新を行っている。[10] 本作は単一HTMLかつ軽量性を維持するため、外部物理エンジンは増やさず、同じ責務分離を簡略化した操舵角、加速、制動、抵抗、車輪回転の状態モデルとして実装する。

公共交通については、SUMOの公式チュートリアルが、バスと路面電車を明示的なルート、停留所、停車時間、繰返し走行として構成している。[11] 本作では道路グリッドへ循環ルートと停車区間を対応付け、シティバス・路面電車・タクシーを低コストで持続走行させる。操作可能な車両と自律交通を同じ移動基盤に接続し、車両乗車中の目的地自動運転も実現する。

[10] [Three.js Tutorials — Car Physics](https://sbcode.net/threejs/physics-car/)

[11] [SUMO Documentation — Public Transport Tutorial](https://sumo.dlr.de/docs/Tutorials/PublicTransport.html)

## Phase 6: 都市品質と軽量描画の実装根拠

Three.js公式資料は、`MeshStandardMaterial`がMetallic-RoughnessによるPBR材質であり、古いLambert/Phong材質より現実的な応答を得る代わりに計算コストが増えること、最良の結果には環境マップを指定すべきことを明示している。[12] そこで、本作は近傍の建物・車両・植生へ粗さ・金属感・窓の発光を持つ材質を適用し、遠景の軽量インスタンシングを残す。

`WebGLRenderer`の公式資料は、`renderer.info`でフレームごとのdraw calls・三角形数等を監視でき、解像度はピクセル比に基づく描画バッファサイズへ反映されることを説明している。[13] 最高品質だけを一律に重くせず、品質プリセットごとに影、クラウド粒子、植生密度、ピクセル比を段階化する。影はLightShadowのbias/normalBias調整と近傍チャンクへの限定により、自己シャドーの見え方と性能を両立させる。

[12] [Three.js — MeshStandardMaterial](https://threejs.org/docs/pages/MeshStandardMaterial.html)

[13] [Three.js — WebGLRenderer](https://threejs.org/docs/pages/WebGLRenderer.html)

## Phase 7: LOCAL AIの選択・永続化と会話UIの実装根拠

WebLLM公式の基本使用法は、モデル一覧を`prebuiltAppConfig.model_list`から参照できること、`CreateMLCEngine()`または`MLCEngine.reload()`によるモデル選択・非同期読込、OpenAI互換のストリーミング会話APIを示している。[14] 本作は0.5B、3B、8Bのモデルを明示的に選択可能にし、読込進行、メモリ目安、失敗時のテンプレート会話フォールバックをUI化する。

Chromeの公式資料は、端末内AIモデルの再起動を速くするためのCache APIを推奨し、`navigator.storage.persist()`で保存領域の保持を要求できることを説明している。[15] MDNはCache APIがウィンドウ側からも利用可能なRequest/Responseの永続的ストレージであり、名前付きキャッシュのバージョン管理と容量上限をアプリ側で考慮すべきであると説明している。[16] WebLLMが扱う実体キャッシュを補完するため、本作では選択済みモデルIDと読込成功状態を`localStorage`へ保存し、保存領域の永続化も要求する。これは初回取得後の再起動で既存キャッシュを優先利用するための状態管理であり、モデル本体の重複保存は行わない。

[14] [WebLLM — Basic Usage](https://webllm.mlc.ai/docs/user/basic_usage.html)

[15] [Chrome for Developers — Cache models in the browser](https://developer.chrome.com/docs/ai/cache-models)

[16] [MDN — Cache](https://developer.mozilla.org/en-US/docs/Web/API/Cache)

## 操作不能・モバイル視点修正の実装根拠

Three.js公式のOrbitControls資料は、左ボタンまたは1本指の移動を回転に割り当て、ズームとパンを入力種別に応じて扱えること、減衰を有効にした場合は描画ループで`update()`を呼ぶ必要があることを示している。[17] 本作ではゲームキャンバスに独立したPointer Eventsベースの視点処理を持たせ、UI要素上の操作は誤ってカメラへ渡さず、キャンバス上のドラッグはPCとモバイルの両方で確実に視点へ渡す。

W3C Pointer Events仕様は、`pointerdown`、`pointermove`、`pointerup`をマウス、タッチ、ペンに共通の入力モデルとして定義し、同じ処理で複数の入力装置へ対応できると説明している。[18] 乗降などの近接操作はキーボードの`E`に限定せず、モバイルの常設「使う」操作と3D近接ボタンの両方から同一処理を呼び出す。

[17] [Three.js — OrbitControls](https://threejs.org/docs/pages/OrbitControls.html)

[18] [W3C — Pointer Events](https://www.w3.org/TR/pointerevents/)
