# BGMと全画面World Settingsの検証記録

ローカルゲームを開始後、WORLDタブから`World Settings`を開いた。従来の右側カードではなく、World Atmosphere、Render Profile、Original Soundtrack、City Activityを含む全画面の集中設定画面が表示され、天候、時刻、品質、描画チャンク、交通、BGMオン／オフ、音量が一画面に揃うことを確認した。

開発者ツール上では`#world-settings-screen`がビューポートと同じ1280×1100px、`left/right/top/bottom=0px`、`position:absolute`、`z-index=175`で配置され、既存ゲームの右側操作パネル（`z-index=28`）より上のレイヤーにあることを確認した。画面の背景は濃色の全画面オーバーレイで、設定操作が優先される。

BGMはタイトル画面では再生せず、ゲーム開始のユーザー操作後に再生を試み、World Settingsを開いた時には音量をダッキングする仕様である。音量スライダーとオン／オフ切替はOriginal Soundtrackセクションに配置した。
World Settingsを固定配置・最高優先度レイヤーへ調整後、全画面の濃色背景がゲーム画面を覆い、World Atmosphere、Render Profile、Original Soundtrack、City Activityの4セクションが集中画面として表示されることを視覚確認した。BGM切替では、オフ操作で状態が`BGM OFF`へ、再度オンにすると`BGM PLAYING`へ即時更新されることを確認した。これは音源の再生状態と設定UIが接続されていることを示す。
390×844pxの実機相当キャプチャでは、World Settingsの閉じるボタン、見出し、状態チップ、World Atmosphere、Render Profile、Original Soundtrackが左右の安全領域内に収まり、カードが一列に積み上がった。BGMトグルと音量スライダーはタップ可能なサイズで表示され、下部のCity Activityとゲーム復帰ボタンには縦スクロールで到達できる設計である。
