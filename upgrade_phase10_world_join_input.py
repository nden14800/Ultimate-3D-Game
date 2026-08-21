from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
html = path.read_text()

# Replace the direct-title entry point with a world browser and a distinct pre-join setup flow.
old_title = '''    <div id="title-screen" class="game-overlay" role="dialog" aria-modal="true" aria-label="タイトル画面">
        <main class="title-card">
            <div class="kicker">CREATIVE CITY SANDBOX</div>
            <h2>ULTIMATE<br><em>3D CITY</em></h2>
            <p>乗り物に乗って、街を走って、好きな場所に好きなものを置こう。自由に遊べる高速サンドボックス。</p>
            <div class="title-features"><span>乗り物</span><span>自由配置</span><span>モバイル対応</span><span>高品質描画</span></div>
            <button id="start-game-button" class="title-primary"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#play-fill"></use></svg>街へ入る</button>
            <button id="title-help-button" class="title-secondary">操作ガイドを見る</button>
        </main>
    </div>'''
new_title = '''    <div id="title-screen" class="game-overlay" role="dialog" aria-modal="true" aria-label="City Worlds">
        <main id="world-browser" class="world-browser-shell">
            <section class="world-browser-intro"><div class="world-browser-kicker">CITY WORLDS</div><h2>SELECT A<br><em>PLACE TO PLAY.</em></h2><p>好きな都市スタイルを選び、環境を整えてから自由探索へ参加します。固定ミッションはありません。</p><div class="world-browser-legend"><span><i></i>ローカルセッション</span><span><i></i>City Score</span><span><i></i>モバイル対応</span></div><button id="title-help-button" class="title-secondary world-help" type="button">操作ガイドを見る</button></section>
            <section class="world-card-grid" aria-label="選択可能なワールド">
                <button class="world-card selected" type="button" data-world-id="harbor"><span class="world-card-top"><b>HARBOR<br>HEART</b><span class="world-card-score">94% CITY SCORE</span></span><span class="world-card-copy">海辺の高層街。交通と建築をバランスよく楽しめます。</span><span class="world-card-meta"><span>12 LOCAL</span><span>24 NPC</span><span>PREMIUM</span></span></button>
                <button class="world-card" type="button" data-world-id="neon"><span class="world-card-top"><b>NEON<br>AVENUE</b><span class="world-card-score">91% CITY SCORE</span></span><span class="world-card-copy">夜景と公共交通を中心にした、光量の多い都市エリアです。</span><span class="world-card-meta"><span>8 LOCAL</span><span>32 NPC</span><span>VISUAL</span></span></button>
                <button class="world-card" type="button" data-world-id="green"><span class="world-card-top"><b>GREEN<br>DISTRICT</b><span class="world-card-score">96% CITY SCORE</span></span><span class="world-card-copy">公園、住宅、屋内探索をゆっくり楽しむ明るい街区です。</span><span class="world-card-meta"><span>16 LOCAL</span><span>18 NPC</span><span>BALANCED</span></span></button>
                <button id="open-join-setup" class="world-browser-primary" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#sliders2"></use></svg>選択したワールドを設定する</button>
            </section>
        </main>
        <main id="join-setup" class="join-setup-shell hidden" aria-label="参加前設定">
            <section class="join-setup-intro"><button id="join-setup-back" class="join-back" type="button" aria-label="ワールド選択へ戻る">←</button><div class="world-browser-kicker">JOIN SETUP</div><h2>MAKE IT<br><em>YOUR CITY.</em></h2><p id="join-world-description">HARBOR HEARTへ参加する前に、描画と街の活動を調整できます。</p><div class="join-world-summary"><span id="join-world-name">HARBOR HEART</span><span id="join-world-live">12 LOCAL · 24 NPC</span></div></section>
            <section class="join-settings-panel"><div class="join-setting"><label for="join-quality-select">描画品質</label><select id="join-quality-select"><option value="performance">軽量 — 反応性優先</option><option value="balanced" selected>プレミアム — 推奨</option><option value="visual">ウルトラ — 詳細優先</option></select></div><div class="join-setting"><label for="join-weather-select">開始時の天気</label><select id="join-weather-select"><option value="sunny" selected>晴れ</option><option value="cloudy">くもり</option><option value="rainy">雨</option><option value="snowy">雪</option></select></div><div class="join-setting"><label for="join-time-select">開始時刻</label><select id="join-time-select"><option value="9">09:00</option><option value="12" selected>12:00</option><option value="18">18:00</option><option value="22">22:00</option></select></div><label class="join-toggle"><input id="join-traffic-toggle" type="checkbox" checked><span>公共交通と交通車両を有効にする</span></label><label class="join-toggle"><input id="join-npc-toggle" type="checkbox" checked><span>街のNPCアクティビティを有効にする</span></label><button id="join-world-button" class="join-world-button" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#play-fill"></use></svg><span>このワールドに参加</span><small>HARBOR HEART</small></button><p class="join-note">参加人数とCity Scoreは、この端末上のローカルセッション情報です。</p></section>
        </main>
    </div>'''
if old_title not in html:
    raise SystemExit('title block not found')
html = html.replace(old_title, new_title)

# Add authoritative CSS after the accumulated legacy rules, keeping game presentation compact and touch-safe.
css = r'''
        /* Phase 10: City Worlds, input recovery, and decluttered HUD. */
        #title-screen { display:grid; place-items:center; padding:clamp(14px,3vw,44px); background:linear-gradient(105deg,rgba(2,13,32,.88),rgba(7,44,88,.48) 52%,rgba(3,14,32,.50)),url('assets/title-skyline.png') center/cover; overflow:auto; }
        .world-browser-shell,.join-setup-shell { width:min(1180px,100%); display:grid; grid-template-columns:minmax(280px,.78fr) minmax(520px,1.22fr); gap:clamp(22px,4vw,72px); align-items:center; color:#eef9ff; }
        .world-browser-intro,.join-setup-intro { position:relative; padding:clamp(20px,3vw,42px); border:1px solid rgba(183,230,255,.22); border-radius:28px; background:linear-gradient(145deg,rgba(4,30,68,.90),rgba(9,68,116,.68)); box-shadow:0 20px 72px rgba(0,0,0,.28); backdrop-filter:blur(18px); }
        .world-browser-kicker { color:#87e4ff; font-size:11px; font-weight:900; letter-spacing:.18em; } .world-browser-kicker::before { display:inline-block; width:8px; height:8px; margin-right:8px; border-radius:50%; background:#60e4a8; box-shadow:0 0 16px #60e4a8; content:''; }
        .world-browser-intro h2,.join-setup-intro h2 { margin:16px 0; color:#fff; font-size:clamp(42px,6vw,76px); line-height:.88; letter-spacing:-.075em; } .world-browser-intro h2 em,.join-setup-intro h2 em { color:#8ddcff; font-style:normal; }
        .world-browser-intro p,.join-setup-intro p { max-width:420px; margin:0; color:#c7eaff; font-size:14px; font-weight:650; line-height:1.75; }
        .world-browser-legend { display:grid; gap:9px; margin:26px 0; } .world-browser-legend span { display:flex; align-items:center; gap:8px; color:#e4f7ff; font-size:11px; font-weight:800; } .world-browser-legend i { width:8px; height:8px; border-radius:50%; background:#6ee6b0; box-shadow:0 0 12px #6ee6b0; }
        .world-help { margin-top:0; text-align:left; }
        .world-card-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:14px; } .world-card { position:relative; display:flex; min-height:205px; flex-direction:column; justify-content:space-between; gap:16px; overflow:hidden; padding:20px; border:2px solid rgba(232,248,255,.50); border-radius:22px; color:#eff9ff; background:linear-gradient(145deg,rgba(15,79,129,.88),rgba(5,33,74,.94)); box-shadow:0 9px 0 rgba(0,15,45,.26),0 20px 38px rgba(0,0,0,.24); text-align:left; transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease; } .world-card::before { position:absolute; inset:auto -20% -54% auto; width:190px; height:190px; border:1px solid rgba(139,225,255,.34); border-radius:50%; box-shadow:0 0 0 24px rgba(139,225,255,.05),0 0 0 48px rgba(139,225,255,.03); content:''; } .world-card:nth-child(2){background:linear-gradient(145deg,rgba(82,45,126,.93),rgba(13,27,70,.96));}.world-card:nth-child(3){background:linear-gradient(145deg,rgba(25,105,87,.92),rgba(8,52,74,.96));}.world-card:hover,.world-card:focus-visible,.world-card.selected { transform:translateY(-4px); border-color:#a9eeff; box-shadow:0 13px 0 rgba(0,15,45,.26),0 26px 48px rgba(0,0,0,.28),0 0 0 3px rgba(105,219,255,.19); outline:none; } .world-card-top { position:relative; z-index:1; display:flex; align-items:start; justify-content:space-between; gap:10px; } .world-card-top b { font-size:24px; line-height:.86; letter-spacing:-.05em; } .world-card-score { padding:5px 7px; border:1px solid rgba(255,255,255,.34); border-radius:99px; color:#caffed; background:rgba(2,24,44,.25); font-size:8px; font-weight:900; letter-spacing:.06em; white-space:nowrap; } .world-card-copy { position:relative; z-index:1; max-width:240px; color:#d8efff; font-size:12px; font-weight:650; line-height:1.5; } .world-card-meta { position:relative; z-index:1; display:flex; flex-wrap:wrap; gap:6px; } .world-card-meta span { padding:5px 7px; border-radius:7px; color:#d9f5ff; background:rgba(1,20,48,.34); font-size:8px; font-weight:900; letter-spacing:.05em; }
        .world-browser-primary { grid-column:1/-1; min-height:60px; display:flex; align-items:center; justify-content:center; gap:9px; border:2px solid #dff7ff; border-radius:18px; color:#123e6b; background:linear-gradient(180deg,#e7fbff,#7cd4ff); box-shadow:0 7px 0 #1766b8,0 14px 35px rgba(0,31,78,.30); font-size:14px; font-weight:950; } .world-browser-primary:active,.join-world-button:active { transform:translateY(4px); box-shadow:0 2px 0 #1766b8; }
        .join-setup-shell.hidden,.world-browser-shell.hidden { display:none; } .join-back { width:42px; height:42px; margin-bottom:22px; border:1px solid rgba(188,231,255,.42); border-radius:13px; color:#e8f8ff; background:rgba(255,255,255,.09); font-size:22px; } .join-world-summary { display:flex; flex-wrap:wrap; gap:7px; margin-top:25px; } .join-world-summary span { padding:7px 9px; border-radius:9px; color:#ccefff; background:rgba(0,24,55,.28); font-size:10px; font-weight:900; letter-spacing:.06em; }
        .join-settings-panel { display:grid; gap:14px; padding:clamp(20px,3vw,38px); border:2px solid rgba(255,255,255,.72); border-radius:28px; color:#173f6f; background:linear-gradient(145deg,rgba(253,254,255,.98),rgba(217,241,255,.96)); box-shadow:0 18px 0 rgba(0,23,58,.24),0 30px 68px rgba(0,0,0,.24); } .join-setting { display:grid; grid-template-columns:minmax(130px,.58fr) minmax(0,1.42fr); align-items:center; gap:14px; padding:12px 0; border-bottom:1px solid #d8e8f4; } .join-setting label { color:#2a5e91; font-size:11px; font-weight:900; letter-spacing:.06em; } .join-setting select { min-width:0; min-height:44px; padding:0 12px; border:1px solid #bdd8ed; border-radius:12px; color:#1c507f; background:#fff; font:inherit; font-size:12px; font-weight:800; } .join-toggle { display:flex; align-items:center; gap:10px; min-height:42px; padding:0 2px; color:#315e89; font-size:12px; font-weight:800; } .join-toggle input { width:18px; height:18px; accent-color:#2585ef; } .join-world-button { min-height:66px; display:grid; grid-template-columns:auto 1fr auto; align-items:center; gap:10px; margin-top:6px; padding:0 18px; border:2px solid #fff; border-radius:18px; color:#fff; background:linear-gradient(180deg,#57abff,#2273e7); box-shadow:0 7px 0 #1558b4,0 15px 28px rgba(8,62,135,.25); font-size:15px; font-weight:950; text-align:left; } .join-world-button small { color:#d5f4ff; font-size:9px; font-weight:900; letter-spacing:.06em; } .join-note { margin:0; color:#6689aa; font-size:10px; line-height:1.5; }
        /* Only one compact HUD is persistent. Secondary panels open on demand. */
        #world-readout { z-index:35; top:calc(66px + env(safe-area-inset-top)); left:calc(12px + env(safe-area-inset-left)); width:178px; padding:8px; border-radius:14px; box-shadow:0 6px 20px rgba(4,29,66,.18); } #world-readout .readout-row { grid-template-columns:1fr 1fr; gap:4px; } #world-readout .readout-chip { min-width:0; padding:5px; } #world-readout .readout-chip small { font-size:7px; } #world-readout .readout-chip strong { font-size:8px; white-space:normal; overflow:visible; } #build-status { z-index:34; top:calc(66px + env(safe-area-inset-top)); max-width:calc(100vw - 220px); padding:7px 10px; } #build-status span { display:none; }
        #city-desk-button { z-index:42; top:calc(12px + env(safe-area-inset-top)); right:calc(74px + env(safe-area-inset-right)); } #game-topbar { z-index:41; inset:calc(10px + env(safe-area-inset-top)) calc(10px + env(safe-area-inset-right)) auto calc(10px + env(safe-area-inset-left)); } .brand-lockup { display:none; } .top-actions .round-button { width:50px; padding:0; } .top-actions .button-label { display:none; }
        #context-actions { z-index:37; right:calc(12px + env(safe-area-inset-right)); bottom:calc(202px + env(safe-area-inset-bottom)); } .context-action { width:50px; min-height:48px; padding:0; } .context-label { display:none; } .ui-container { z-index:50; top:calc(70px + env(safe-area-inset-top)); right:calc(12px + env(safe-area-inset-right)); width:min(360px,calc(100vw - 24px)); max-height:calc(100dvh - 150px); } #chat-ui.conversation-dock { z-index:36; left:calc(12px + env(safe-area-inset-left)); bottom:calc(96px + env(safe-area-inset-bottom)); width:min(430px,calc(100vw - 218px)); min-width:0; } #chat-ui.conversation-dock.collapsed { transform:translateY(calc(100% - 44px)); } #build-belt { z-index:39; bottom:calc(10px + env(safe-area-inset-bottom)); width:min(630px,calc(100vw - 28px)); }
        #map-container { z-index:38; right:calc(12px + env(safe-area-inset-right)); bottom:calc(12px + env(safe-area-inset-bottom)); width:150px; height:150px; border-radius:22px; cursor:pointer; } #map-container::before { content:'CITY RADAR · TAP'; }
        #mobile-action-rail { display:none !important; } @media (pointer:coarse),(max-width:760px) { #world-readout { width:142px; } #world-readout .readout-row { grid-template-columns:1fr; } #world-readout .readout-chip:nth-child(2) { display:none; } #build-status { top:calc(63px + env(safe-area-inset-top)); max-width:calc(100vw - 166px); font-size:9px; } #city-desk-button { right:calc(66px + env(safe-area-inset-right)); min-width:44px; padding:0 8px; font-size:0; } #city-desk-button .bi-icon { margin:0; } #map-container { right:calc(10px + env(safe-area-inset-right)); bottom:calc(94px + env(safe-area-inset-bottom)); width:126px; height:126px; } #context-actions { display:none; } #chat-ui.conversation-dock { left:calc(10px + env(safe-area-inset-left)); bottom:calc(15px + env(safe-area-inset-bottom)); width:min(330px,calc(100vw - 152px)); } #chat-ui.conversation-dock.collapsed { transform:translateY(calc(100% - 42px)); } #build-belt { bottom:calc(10px + env(safe-area-inset-bottom)); left:50%; width:calc(100vw - 24px); max-width:none; padding:4px; border-radius:16px; } #build-belt .belt-slot { min-width:44px; min-height:47px; padding:4px; font-size:7px; } #build-belt .slot-key { display:none; } #mobile-action-rail { position:fixed; z-index:43; right:calc(10px + env(safe-area-inset-right)); bottom:calc(236px + env(safe-area-inset-bottom)); display:grid !important; grid-template-columns:repeat(2,52px); gap:7px; pointer-events:auto; } #mobile-action-rail .mobile-action { display:none; width:52px; min-height:48px; border-radius:14px; font-size:8px; } #mobile-action-rail #mobile-interact-button,#mobile-action-rail #mobile-camera-button,#mobile-action-rail #mobile-map-button,#mobile-action-rail #mobile-pause-button { display:flex; } #joystick-container { bottom:calc(14px + env(safe-area-inset-bottom)); left:calc(12px + env(safe-area-inset-left)); transform:scale(.84); transform-origin:bottom left; } #run-button { right:calc(16px + env(safe-area-inset-right)); bottom:calc(22px + env(safe-area-inset-bottom)); width:64px; height:64px; } }
        @media (max-width:820px) { .world-browser-shell,.join-setup-shell { grid-template-columns:1fr; max-width:620px; } .world-browser-intro { padding:24px; } .world-browser-intro h2,.join-setup-intro h2 { font-size:clamp(40px,12vw,60px); } .world-card-grid { grid-template-columns:1fr; } .world-card { min-height:142px; } .world-browser-primary { grid-column:auto; } .join-setting { grid-template-columns:1fr; gap:7px; } #title-screen { align-items:start; padding:calc(14px + env(safe-area-inset-top)) 12px max(14px,env(safe-area-inset-bottom)); } }
'''
html = html.replace('        </style>', css + '\n        </style>')

# Add camera state variables and replace the input routines with a single Pointer Events path for all camera modes.
html = html.replace("        let cameraZoom = 1, freeCamSpeed = 16, freeCamAnchor = new THREE.Vector3();", "        let cameraZoom = 1, freeCamSpeed = 16, freeCamAnchor = new THREE.Vector3();\n        let activeLookPointerId = null, freeCamYaw = 0, freeCamPitch = -0.18, firstPersonPitch = 0;\n        const freeCamDirection = new THREE.Vector3(), freeCamLookTarget = new THREE.Vector3();\n        let selectedWorldId = 'harbor';")

old_pointer = '''        function onPointerDown(event) {
            if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement?.tagName)) return;
            if (event.target !== renderer.domElement) return;
            if (event.pointerType === 'touch') {
                event.preventDefault();
                renderer.domElement.setPointerCapture?.(event.pointerId);
            }
            if (event.button === 2) { if (placeMode || removeMode) removePropAtPointer(event); return; }
            if (event.button !== 0) return;
            if (removeMode) { removePropAtPointer(event); return; }
            if (placeMode) { placePropAtPointer(event); return; }
            isPointerDown = true;
            pointerPosition.x = event.clientX;
            pointerPosition.y = event.clientY;
        }
        function onPointerMove(event) {
            if (event.pointerType === 'touch') event.preventDefault();
            if (placeMode || removeMode) updateBuildGhost(event);
            if (!isPointerDown || currentCameraIndex === 2) return;
            const deltaX = event.clientX - pointerPosition.x;
            const deltaY = event.clientY - pointerPosition.y;

            if (currentCameraIndex === 1) {
                playerGroup.rotation.y -= deltaX * 0.002;
            } else {
                cameraOffsetSpherical.theta -= deltaX * 0.005;
                cameraOffsetSpherical.phi -= deltaY * 0.005;
                cameraOffsetSpherical.phi = Math.max(0.1, Math.min(Math.PI - 0.5, cameraOffsetSpherical.phi));
            }
            pointerPosition.x = event.clientX;
            pointerPosition.y = event.clientY;
        }
        function onPointerUp(event) {
            if (event?.pointerType === 'touch') {
                event.preventDefault();
                if (renderer.domElement.hasPointerCapture?.(event.pointerId)) renderer.domElement.releasePointerCapture?.(event.pointerId);
            }
            isPointerDown = false;
        }'''
new_pointer = '''        function onPointerDown(event) {
            if (!gameStarted || gamePaused || event.target !== renderer.domElement) return;
            if (event.pointerType === 'touch') event.preventDefault();
            if (event.button === 2) { if (placeMode || removeMode) removePropAtPointer(event); return; }
            if (event.button !== 0) return;
            if (removeMode) { placeMode = false; removePropAtPointer(event); return; }
            if (placeMode) { placePropAtPointer(event); return; }
            activeLookPointerId = event.pointerId;
            isPointerDown = true;
            pointerPosition.set(event.clientX, event.clientY);
            renderer.domElement.setPointerCapture?.(event.pointerId);
            renderer.domElement.focus?.({ preventScroll:true });
        }
        function onPointerMove(event) {
            if (event.pointerType === 'touch') event.preventDefault();
            if (placeMode || removeMode) updateBuildGhost(event);
            if (!isPointerDown || activeLookPointerId !== event.pointerId) return;
            const deltaX = event.clientX - pointerPosition.x;
            const deltaY = event.clientY - pointerPosition.y;
            const lookScale = event.pointerType === 'touch' ? 0.0054 : 0.0042;
            if (Math.abs(deltaX) + Math.abs(deltaY) < 0.01) return;
            if (currentCameraIndex === 0) {
                cameraOffsetSpherical.theta -= deltaX * lookScale;
                cameraOffsetSpherical.phi = THREE.MathUtils.clamp(cameraOffsetSpherical.phi - deltaY * lookScale, 0.18, Math.PI - 0.52);
            } else if (currentCameraIndex === 1) {
                const actor = getControlledObject();
                actor.rotation.y -= deltaX * lookScale;
                firstPersonPitch = THREE.MathUtils.clamp(firstPersonPitch - deltaY * lookScale, -1.32, 1.32);
            } else {
                freeCamYaw -= deltaX * lookScale;
                freeCamPitch = THREE.MathUtils.clamp(freeCamPitch - deltaY * lookScale, -1.42, 1.42);
                applyFreeCamLook();
            }
            pointerPosition.set(event.clientX, event.clientY);
        }
        function onPointerUp(event) {
            if (event?.pointerType === 'touch') event.preventDefault();
            if (activeLookPointerId !== null && (!event || event.pointerId === activeLookPointerId)) {
                if (event && renderer.domElement.hasPointerCapture?.(event.pointerId)) renderer.domElement.releasePointerCapture?.(event.pointerId);
                activeLookPointerId = null;
                isPointerDown = false;
            }
        }
        function applyFreeCamLook() {
            const cp = Math.cos(freeCamPitch);
            freeCamDirection.set(-Math.sin(freeCamYaw) * cp, Math.sin(freeCamPitch), -Math.cos(freeCamYaw) * cp).normalize();
            freeCamLookTarget.copy(cameras.freeLook.position).add(freeCamDirection);
            cameras.freeLook.lookAt(freeCamLookTarget);
        }'''
if old_pointer not in html:
    raise SystemExit('pointer block not found')
html = html.replace(old_pointer, new_pointer)

old_cam = '''        function beginFreeCamNearActor() {
            const actor = getControlledObject();
            const forward = new THREE.Vector3();
            cameras.thirdPerson.getWorldDirection(forward); forward.y = 0; if (forward.lengthSq() < .001) forward.set(0,0,-1); forward.normalize();
            freeCamAnchor.copy(actor.position);
            cameras.freeLook.position.copy(actor.position).addScaledVector(forward, -10).add(new THREE.Vector3(0,6,0));
            orbitControls.target.copy(actor.position).add(new THREE.Vector3(0,1.4,0));
            orbitControls.enableDamping = true;
            orbitControls.dampingFactor = 0.075;
            orbitControls.enablePan = true;
            orbitControls.minDistance = 1;
            orbitControls.maxDistance = 90;
            orbitControls.update();
        }'''
new_cam = '''        function beginFreeCamNearActor() {
            const actor = getControlledObject();
            const forward = new THREE.Vector3();
            cameras.thirdPerson.getWorldDirection(forward);
            if (forward.lengthSq() < .001) forward.set(0,0,-1);
            forward.normalize();
            freeCamAnchor.copy(actor.position);
            cameras.freeLook.position.copy(actor.position).addScaledVector(forward, -10).add(new THREE.Vector3(0,5.2,0));
            freeCamYaw = Math.atan2(-forward.x, -forward.z);
            freeCamPitch = Math.asin(THREE.MathUtils.clamp(forward.y, -0.92, 0.92));
            orbitControls.enabled = false;
            applyFreeCamLook();
        }'''
if old_cam not in html:
    raise SystemExit('free cam block not found')
html = html.replace(old_cam, new_cam)
html = html.replace("            orbitControls.enabled = (cameraName === 'Free Cam');", "            orbitControls.enabled = false;")
old_free_update = '''        function updateFreeCam(delta) {
            const inputX = ((keys.d || keys.ArrowRight) ? 1 : 0) - ((keys.a || keys.ArrowLeft) ? 1 : 0) + mobileInput.x;
            const inputZ = ((keys.s || keys.ArrowDown) ? 1 : 0) - ((keys.w || keys.ArrowUp) ? 1 : 0) + mobileInput.z;
            const inputY = (keys.e ? 1 : 0) - (keys.q ? 1 : 0);
            const forward = new THREE.Vector3(); currentCamera.getWorldDirection(forward); forward.y = 0; if (forward.lengthSq() < .001) forward.set(0,0,-1); forward.normalize();
            const right = new THREE.Vector3().crossVectors(forward, WORLD_UP).normalize();
            const move = new THREE.Vector3().addScaledVector(forward, -inputZ).addScaledVector(right, inputX).addScaledVector(WORLD_UP, inputY);
            if (move.lengthSq() > .001) { move.normalize().multiplyScalar(freeCamSpeed * (keys.Shift ? 1.8 : 1) * delta); currentCamera.position.add(move); orbitControls.target.add(move); freeCamAnchor.add(move); }
            currentSpeedMs = move.lengthSq() ? freeCamSpeed : 0;
            orbitControls.update();
        }'''
new_free_update = '''        function updateFreeCam(delta) {
            const inputX = ((keys.d || keys.ArrowRight) ? 1 : 0) - ((keys.a || keys.ArrowLeft) ? 1 : 0) + mobileInput.x;
            const inputZ = ((keys.s || keys.ArrowDown) ? 1 : 0) - ((keys.w || keys.ArrowUp) ? 1 : 0) + mobileInput.z;
            const inputY = (keys.e ? 1 : 0) - (keys.q ? 1 : 0);
            const forward = new THREE.Vector3(-Math.sin(freeCamYaw), 0, -Math.cos(freeCamYaw)).normalize();
            const right = new THREE.Vector3().crossVectors(forward, WORLD_UP).normalize();
            const move = new THREE.Vector3().addScaledVector(forward, -inputZ).addScaledVector(right, inputX).addScaledVector(WORLD_UP, inputY);
            if (move.lengthSq() > .001) { move.normalize().multiplyScalar(freeCamSpeed * (keys.Shift ? 1.8 : 1) * delta); currentCamera.position.add(move); freeCamAnchor.add(move); }
            currentSpeedMs = move.lengthSq() ? freeCamSpeed : 0;
            applyFreeCamLook();
        }'''
if old_free_update not in html:
    raise SystemExit('free update block not found')
html = html.replace(old_free_update, new_free_update)
html = html.replace("                currentCamera.position.copy(controlledObject.position).add(new THREE.Vector3(0, controlledVehicle ? 1.2 : 1.5, 0));\n                currentCamera.quaternion.copy(controlledObject.quaternion);", "                currentCamera.position.copy(controlledObject.position).add(new THREE.Vector3(0, controlledVehicle ? 1.2 : 1.5, 0));\n                firstPersonEuler.set(firstPersonPitch, controlledObject.rotation.y, 0, 'YXZ');\n                currentCamera.quaternion.setFromEuler(firstPersonEuler);")
html = html.replace("            } else {\n                orbitControls.update();\n            }\n            updateDynamicShadow", "            } else {\n                applyFreeCamLook();\n            }\n            updateDynamicShadow")

# Keep player-facing prompt labels equivalent across keyboard and touch, and block the old mini-map destination action.
html = html.replace("prompt.element.innerHTML=`<b>E</b><span>${target.label} に入る</span><small>BUILDING ENTRY</small>`;", "prompt.element.innerHTML=`<b>E / 使う</b><span>${target.label} に入る</span><small>BUILDING ENTRY</small>`;")
html = html.replace("hint.textContent='Eで降車 · City Atlasで車両自動運転';", "hint.textContent='E / 使うで降車 · City Atlasで車両自動運転';")
html = html.replace("hint.textContent='近くの乗り物・公共交通に E';", "hint.textContent='近くの乗り物・公共交通に E / 使う';")
html = html.replace("setSandboxMessage('乗り物を近くに出しました。Eキーで乗車できます。');", "setSandboxMessage('乗り物を近くに出しました。Eキーまたはモバイルの「使う」で乗車できます。');")

# Change title entry event and add world-browser wiring at the end of normal listener setup.
html = html.replace("            document.getElementById('start-game-button').addEventListener('click', startGame);", "            document.getElementById('start-game-button').addEventListener('click', openWorldBrowser);")
needle = "            renderer.domElement.addEventListener('wheel', (e) => { if (!gameStarted || gamePaused || e.ctrlKey) return; e.preventDefault(); adjustCameraZoom(e.deltaY < 0 ? 1 : -1, Math.abs(e.deltaY) > 80 ? 1.4 : 0.65); }, { passive:false });"
addition = '''            renderer.domElement.addEventListener('wheel', (e) => { if (!gameStarted || gamePaused || e.ctrlKey) return; e.preventDefault(); adjustCameraZoom(e.deltaY < 0 ? 1 : -1, Math.abs(e.deltaY) > 80 ? 1.4 : 0.65); }, { passive:false });
            document.querySelectorAll('.world-card').forEach(card => card.addEventListener('click', () => selectWorld(card.dataset.worldId)));
            document.getElementById('open-join-setup').addEventListener('click', openJoinSetup);
            document.getElementById('join-setup-back').addEventListener('click', openWorldBrowser);
            document.getElementById('join-world-button').addEventListener('click', joinSelectedWorld);
            mapCanvas.addEventListener('click', (e) => { if (!gameStarted) return; e.preventDefault(); e.stopImmediatePropagation(); openCityAtlas(); }, true);'''
if needle not in html:
    raise SystemExit('event insertion point not found')
html = html.replace(needle, addition)

# Add world selection functions before startGame.
needle = "        function startGame() {\n"
world_functions = '''        const WORLD_PROFILES = {
            harbor:{name:'HARBOR HEART',live:'12 LOCAL · 24 NPC',description:'海辺の高層街。交通と建築をバランスよく楽しめます。',quality:'balanced',weather:'sunny',time:'12',traffic:true,npcs:true},
            neon:{name:'NEON AVENUE',live:'8 LOCAL · 32 NPC',description:'夜景と公共交通を中心にした、光量の多い都市エリアです。',quality:'visual',weather:'cloudy',time:'22',traffic:true,npcs:true},
            green:{name:'GREEN DISTRICT',live:'16 LOCAL · 18 NPC',description:'公園、住宅、屋内探索をゆっくり楽しむ明るい街区です。',quality:'balanced',weather:'sunny',time:'9',traffic:true,npcs:true}
        };
        function selectWorld(id) {
            const profile = WORLD_PROFILES[id] || WORLD_PROFILES.harbor;
            selectedWorldId = id in WORLD_PROFILES ? id : 'harbor';
            document.querySelectorAll('.world-card').forEach(card => card.classList.toggle('selected', card.dataset.worldId === selectedWorldId));
            document.getElementById('join-world-name').textContent = profile.name;
            document.getElementById('join-world-live').textContent = profile.live;
            document.getElementById('join-world-description').textContent = `${profile.name}へ参加する前に、描画と街の活動を調整できます。`;
            document.getElementById('join-quality-select').value = profile.quality;
            document.getElementById('join-weather-select').value = profile.weather;
            document.getElementById('join-time-select').value = profile.time;
            document.getElementById('join-traffic-toggle').checked = profile.traffic;
            document.getElementById('join-npc-toggle').checked = profile.npcs;
            document.querySelector('#join-world-button small').textContent = profile.name;
        }
        function openWorldBrowser() {
            document.getElementById('world-browser').classList.remove('hidden');
            document.getElementById('join-setup').classList.add('hidden');
            selectWorld(selectedWorldId);
        }
        function openJoinSetup() {
            document.getElementById('world-browser').classList.add('hidden');
            document.getElementById('join-setup').classList.remove('hidden');
            selectWorld(selectedWorldId);
        }
        function joinSelectedWorld() {
            const quality = document.getElementById('join-quality-select').value;
            const weather = document.getElementById('join-weather-select').value;
            const hour = Number(document.getElementById('join-time-select').value);
            document.getElementById('quality-select').value = quality;
            setQuality(quality);
            document.getElementById('weather-select').value = weather;
            changeWeather(weather);
            document.getElementById('time-slider').value = hour;
            updateTime(hour);
            document.getElementById('traffic-toggle').checked = document.getElementById('join-traffic-toggle').checked;
            trafficEnabled = document.getElementById('traffic-toggle').checked;
            const npcToggle = document.getElementById('join-npc-toggle').checked;
            if (!npcToggle) { document.getElementById('npc-slider').value = 0; updateNpcCount(); }
            else if (Number(document.getElementById('npc-slider').value) === 0) { document.getElementById('npc-slider').value = 12; updateNpcCount(); }
            startGame();
            setSandboxMessage(`${WORLD_PROFILES[selectedWorldId].name}へ参加しました。ドラッグ／スワイプで視点を動かせます。`);
        }

'''
if needle not in html:
    raise SystemExit('start game marker not found')
html = html.replace(needle, world_functions + needle)

# Ensure returning to the title resets the flow to the card browser.
html = html.replace("            document.getElementById('title-screen').classList.remove('hidden');\n            toggleDrawer(false);", "            document.getElementById('title-screen').classList.remove('hidden');\n            openWorldBrowser();\n            toggleDrawer(false);")

# Replace the City Atlas renderer with a high-contrast district map and readable hierarchy.
old_draw_start = html.index('        function drawCityAtlas() {')
old_draw_end = html.index('        function atlasPointerToWorld', old_draw_start)
new_draw = '''        function drawCityAtlas() {
            if (!cityAtlasCanvas || document.getElementById('city-atlas-screen').classList.contains('hidden')) return;
            const ctx = cityAtlasCtx, w = cityAtlasCanvas.width, h = cityAtlasCanvas.height, range = atlasRange();
            ctx.clearRect(0,0,w,h);
            const grd=ctx.createLinearGradient(0,0,w,h);grd.addColorStop(0,'#102f50');grd.addColorStop(.55,'#0b223c');grd.addColorStop(1,'#06182e');ctx.fillStyle=grd;ctx.fillRect(0,0,w,h);
            const scale=w/range, roadStartX=Math.floor((cityAtlasCenter.x-range/2)/ROAD_INTERVAL)*ROAD_INTERVAL, roadStartZ=Math.floor((cityAtlasCenter.z-range/2)/ROAD_INTERVAL)*ROAD_INTERVAL;
            ctx.save();ctx.strokeStyle='rgba(91,163,202,.18)';ctx.lineWidth=1;for(let g=0;g<=w;g+=64){ctx.beginPath();ctx.moveTo(g,0);ctx.lineTo(g,h);ctx.stroke();ctx.beginPath();ctx.moveTo(0,g);ctx.lineTo(w,g);ctx.stroke();}ctx.restore();
            loadedChunks.forEach(chunk=>{const origin=chunkOrigin(chunk.cx,chunk.cz),p=atlasWorldToPixel(origin),s=CHUNK_SIZE*scale;ctx.fillStyle='rgba(57,122,158,.22)';ctx.fillRect(p.x,p.y,s,s);ctx.strokeStyle='rgba(145,218,250,.22)';ctx.lineWidth=2;ctx.strokeRect(p.x,p.y,s,s);});
            ctx.strokeStyle='#6f8795';ctx.lineWidth=Math.max(7,ROAD_WIDTH*scale);ctx.lineCap='round';for(let x=roadStartX;x<=cityAtlasCenter.x+range/2;x+=ROAD_INTERVAL){const p=atlasWorldToPixel(new THREE.Vector3(x,0,cityAtlasCenter.z));ctx.beginPath();ctx.moveTo(p.x,0);ctx.lineTo(p.x,h);ctx.stroke();}for(let z=roadStartZ;z<=cityAtlasCenter.z+range/2;z+=ROAD_INTERVAL){const p=atlasWorldToPixel(new THREE.Vector3(cityAtlasCenter.x,0,z));ctx.beginPath();ctx.moveTo(0,p.y);ctx.lineTo(w,p.y);ctx.stroke();}
            ctx.strokeStyle='rgba(235,250,255,.30)';ctx.lineWidth=1.5;for(let x=roadStartX;x<=cityAtlasCenter.x+range/2;x+=ROAD_INTERVAL){const p=atlasWorldToPixel(new THREE.Vector3(x,0,cityAtlasCenter.z));ctx.setLineDash([8,9]);ctx.beginPath();ctx.moveTo(p.x,0);ctx.lineTo(p.x,h);ctx.stroke();}for(let z=roadStartZ;z<=cityAtlasCenter.z+range/2;z+=ROAD_INTERVAL){const p=atlasWorldToPixel(new THREE.Vector3(cityAtlasCenter.x,0,z));ctx.setLineDash([8,9]);ctx.beginPath();ctx.moveTo(0,p.y);ctx.lineTo(w,p.y);ctx.stroke();}ctx.setLineDash([]);
            buildings.forEach(b=>{if(!b.visible)return;const p=atlasWorldToPixel(b.position);if(p.x<-20||p.x>w+20||p.y<-20||p.y>h+20)return;ctx.fillStyle=b.userData?.buildingType==='park'?'#2f9c70':'#6ba7c4';ctx.fillRect(p.x-8,p.y-8,16,16);ctx.strokeStyle='rgba(218,246,255,.45)';ctx.lineWidth=1;ctx.strokeRect(p.x-8,p.y-8,16,16);});
            if(document.getElementById('atlas-layer-npcs').checked){npcs.forEach(n=>{const p=atlasWorldToPixel(n.position);ctx.fillStyle='#d5ecff';ctx.fillRect(p.x-3,p.y-3,6,6);});}
            if(document.getElementById('atlas-layer-transit').checked){trafficVehicles.forEach(v=>{const p=atlasWorldToPixel(v.position);ctx.fillStyle=v.userData?.transit?'#ffd166':'#fd9b68';ctx.beginPath();ctx.moveTo(p.x,p.y-7);ctx.lineTo(p.x+6,p.y+5);ctx.lineTo(p.x-6,p.y+5);ctx.closePath();ctx.fill();});}
            if(path.length>1){ctx.strokeStyle=isAutoDriving?'#4de5ff':'#ff8d77';ctx.shadowColor=ctx.strokeStyle;ctx.shadowBlur=12;ctx.lineWidth=6;ctx.lineCap='round';ctx.beginPath();let p=atlasWorldToPixel(path[0]);ctx.moveTo(p.x,p.y);for(let i=1;i<path.length;i++){p=atlasWorldToPixel(path[i]);ctx.lineTo(p.x,p.y);}ctx.stroke();ctx.shadowBlur=0;}
            if(destination){const p=atlasWorldToPixel(destination);ctx.strokeStyle='#fff';ctx.lineWidth=3;ctx.fillStyle='#ff735f';ctx.beginPath();ctx.arc(p.x,p.y,13,0,Math.PI*2);ctx.fill();ctx.stroke();ctx.beginPath();ctx.moveTo(p.x,p.y-29);ctx.lineTo(p.x,p.y-12);ctx.stroke();}
            const actor=getControlledObject(),p=atlasWorldToPixel(actor.position),heading=actor.rotation?.y||0;ctx.save();ctx.translate(p.x,p.y);ctx.rotate(-heading);ctx.fillStyle='#fff';ctx.beginPath();ctx.moveTo(0,-16);ctx.lineTo(10,11);ctx.lineTo(0,7);ctx.lineTo(-10,11);ctx.closePath();ctx.fill();ctx.fillStyle='#1a9dec';ctx.beginPath();ctx.arc(0,3,4,0,Math.PI*2);ctx.fill();ctx.restore();
            ctx.fillStyle='rgba(221,246,255,.92)';ctx.font='900 21px system-ui';ctx.fillText('N',w/2-7,28);ctx.strokeStyle='rgba(185,233,255,.48)';ctx.beginPath();ctx.moveTo(w/2,36);ctx.lineTo(w/2,62);ctx.stroke();
            ctx.fillStyle='rgba(220,247,255,.92)';ctx.font='800 18px system-ui';ctx.fillText(`RADIUS ${Math.round(range/2)}m`,20,h-24);document.getElementById('atlas-zoom-label').textContent=`ZOOM ${cityAtlasZoom.toFixed(1)}× · ${Math.round(range)}m`;document.getElementById('atlas-destination-readout').textContent=destination?`目的地 X:${destination.x.toFixed(0)} Z:${destination.z.toFixed(0)} · ${path.length} points`:'地図をタップして目的地を置く';
        }
'''
html = html[:old_draw_start] + new_draw + html[old_draw_end:]

path.write_text(html)
print('Applied Phase 10 input, world browser, HUD, and atlas update.')
