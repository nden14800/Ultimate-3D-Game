from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()

css = r'''
        /* Mega refresh: camera, mobile parity, and compact HUD. */
        #mobile-action-rail { display:none; } .zoom-readout { position:absolute; z-index:28; left:50%; top:66px; transform:translateX(-50%); display:none; min-width:84px; padding:7px 10px; border:1px solid rgba(255,255,255,.72); border-radius:12px; color:#175188; background:rgba(250,254,255,.92); box-shadow:0 5px 14px rgba(1,42,83,.16); font-size:10px; font-weight:900; text-align:center; pointer-events:none; }
        body.keyboard-active #joystick-container, body.keyboard-active #run-button, body.keyboard-active #mobile-action-rail { display:none !important; } body.keyboard-active .zoom-readout { display:block; }
        @media (pointer:coarse),(max-width:760px) { .zoom-readout { display:block; top:calc(60px + env(safe-area-inset-top)); } #mobile-action-rail { position:fixed; z-index:29; right:calc(9px + env(safe-area-inset-right)); top:calc(214px + env(safe-area-inset-top)); display:grid; grid-template-columns:repeat(2,58px); gap:7px; pointer-events:auto; } .mobile-action { min-height:50px; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2px; padding:3px; border:2px solid rgba(255,255,255,.84); border-radius:15px; color:#164e83; background:rgba(250,254,255,.94); box-shadow:0 4px 0 rgba(5,50,102,.16); font-size:8px; font-weight:900; line-height:1.05; } .mobile-action .bi-icon { width:16px; height:16px; } #map-container { top:calc(60px + env(safe-area-inset-top)); bottom:auto; } #joystick-container { bottom:calc(20px + env(safe-area-inset-bottom)); } #run-button { right:calc(16px + env(safe-area-inset-right)); bottom:calc(22px + env(safe-area-inset-bottom)); } #world-readout { max-width:170px; } #world-readout .readout-title { font-size:8px; } #world-readout small { font-size:7px; } #world-readout strong { font-size:9px; } }
'''
if 'Mega refresh: camera, mobile parity' not in text:
    text = text.replace('        </style>', css + '\n        </style>', 1)

old_rail = '''    <aside id="mobile-action-rail" class="mobile-ui" aria-label="モバイル追加操作"><button id="mobile-interact-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-in-right"></use></svg>使う</button><button id="mobile-build-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-seam-fill"></use></svg>建築</button><button id="mobile-chat-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#chat-square-text-fill"></use></svg>会話</button></aside>'''
new_rail = '''    <aside id="mobile-action-rail" class="mobile-ui" aria-label="モバイル追加操作"><button id="mobile-interact-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-in-right"></use></svg>使う</button><button id="mobile-build-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-seam-fill"></use></svg>建築</button><button id="mobile-chat-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#chat-square-text-fill"></use></svg>会話</button><button id="mobile-map-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#map-fill"></use></svg>地図</button><button id="mobile-camera-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#camera-reels-fill"></use></svg>視点</button><button id="mobile-zoom-in-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#zoom-in"></use></svg>拡大</button><button id="mobile-zoom-out-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#zoom-out"></use></svg>縮小</button><button id="mobile-pack-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#backpack4-fill"></use></svg>パック</button><button id="mobile-pause-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#pause-fill"></use></svg>ポーズ</button></aside>
    <div id="zoom-readout" class="zoom-readout" aria-live="polite">視点 1.0×</div>'''
if old_rail in text:
    text = text.replace(old_rail, new_rail, 1)

text = text.replace("const cameraTypes = ['Third Person', 'First Person', 'Free Look'];", "const cameraTypes = ['Third Person', 'First Person', 'Free Cam'];", 1)
text = text.replace("let nextNpcChatTime = 0;", "let nextNpcChatTime = 0;\n        let cameraZoom = 1, freeCamSpeed = 16, freeCamAnchor = new THREE.Vector3();", 1)

text = text.replace("""                if (!e.repeat && key === 'b') togglePlaceMode();""", """                if (!e.repeat && key === 'b') togglePlaceMode();
                if (!e.repeat && (key === '=' || key === '+')) adjustCameraZoom(1);
                if (!e.repeat && key === '-') adjustCameraZoom(-1);""", 1)

text = text.replace("""            document.getElementById('mobile-chat-button').addEventListener('click', () => { document.getElementById('chat-ui').classList.remove('collapsed'); document.getElementById('chat-input').focus(); });""", """            document.getElementById('mobile-chat-button').addEventListener('click', () => { document.getElementById('chat-ui').classList.remove('collapsed'); document.getElementById('chat-input').focus(); });
            document.getElementById('mobile-map-button').addEventListener('click', openCityAtlas);
            document.getElementById('mobile-camera-button').addEventListener('click', changeCamera);
            document.getElementById('mobile-zoom-in-button').addEventListener('click', () => adjustCameraZoom(1));
            document.getElementById('mobile-zoom-out-button').addEventListener('click', () => adjustCameraZoom(-1));
            document.getElementById('mobile-pack-button').addEventListener('click', () => toggleFieldPack(true));
            document.getElementById('mobile-pause-button').addEventListener('click', togglePause);""", 1)

text = text.replace("""            renderer.domElement.addEventListener('contextmenu', (e) => { if (placeMode || removeMode) e.preventDefault(); });""", """            renderer.domElement.addEventListener('contextmenu', (e) => { if (placeMode || removeMode) e.preventDefault(); });
            renderer.domElement.addEventListener('wheel', (e) => { if (!gameStarted || gamePaused || e.ctrlKey) return; e.preventDefault(); adjustCameraZoom(e.deltaY < 0 ? 1 : -1, Math.abs(e.deltaY) > 80 ? 1.4 : 0.65); }, { passive:false });""", 1)

old_change = '''        function changeCamera() {
            currentCameraIndex = (currentCameraIndex + 1) % cameraTypes.length;
            const cameraName = cameraTypes[currentCameraIndex];
            orbitControls.enabled = (cameraName === 'Free Look');
            currentCamera = (cameraName === 'Third Person') ? cameras.thirdPerson : (cameraName === 'First Person') ? cameras.firstPerson : cameras.freeLook;
            document.getElementById('change-camera-btn').innerHTML = '<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#camera-reels-fill"></use></svg>視点: ' + cameraName;
            onWindowResize();
        }'''
new_change = '''        function updateZoomReadout() {
            const node = document.getElementById('zoom-readout');
            if (!node) return;
            const label = currentCamera === cameras.thirdPerson ? `距離 ${cameraOffsetSpherical.radius.toFixed(1)}m` : `視野 ${Math.round(currentCamera.fov)}°`;
            node.textContent = label;
        }
        function adjustCameraZoom(direction, magnitude = 1) {
            if (currentCamera === cameras.thirdPerson) {
                cameraOffsetSpherical.radius = THREE.MathUtils.clamp(cameraOffsetSpherical.radius - direction * magnitude * 1.25, 4.2, 20);
                cameraZoom = 8 / cameraOffsetSpherical.radius;
            } else {
                currentCamera.fov = THREE.MathUtils.clamp(currentCamera.fov - direction * magnitude * 4.5, 42, 88);
                currentCamera.updateProjectionMatrix();
                cameraZoom = 75 / currentCamera.fov;
            }
            updateZoomReadout();
        }
        function beginFreeCamNearActor() {
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
        }
        function changeCamera() {
            currentCameraIndex = (currentCameraIndex + 1) % cameraTypes.length;
            const cameraName = cameraTypes[currentCameraIndex];
            currentCamera = (cameraName === 'Third Person') ? cameras.thirdPerson : (cameraName === 'First Person') ? cameras.firstPerson : cameras.freeLook;
            if (cameraName === 'Free Cam') beginFreeCamNearActor();
            orbitControls.enabled = (cameraName === 'Free Cam');
            document.getElementById('change-camera-btn').innerHTML = '<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#camera-reels-fill"></use></svg>視点: ' + cameraName;
            updateZoomReadout();
            onWindowResize();
        }
        function updateFreeCam(delta) {
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
if old_change in text:
    text = text.replace(old_change, new_change, 1)
else:
    raise SystemExit('changeCamera block not found')

old_walk_start = '''            const driving = updateControlledVehicle(delta);
            if (!driving) {
                isRunning = keys['Shift'] || isRunning;'''
new_walk_start = '''            const driving = updateControlledVehicle(delta);
            if (!driving && currentCamera === cameras.freeLook) {
                updateFreeCam(delta);
            } else if (!driving) {
                isRunning = keys['Shift'] || isRunning;'''
if old_walk_start in text:
    text = text.replace(old_walk_start, new_walk_start, 1)
else:
    raise SystemExit('walk start not found')

text = text.replace("""            } else {
                orbitControls.update();
            }
            updateDynamicShadow(controlledObject.position, time);""", """            } else {
                orbitControls.update();
            }
            updateDynamicShadow(currentCamera === cameras.freeLook ? cameras.freeLook.position : controlledObject.position, time);""", 1)

text = text.replace("""            cameras.freeLook = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, initialFar);
            cameras.freeLook.position.set(10, 10, 15);""", """            cameras.freeLook = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, initialFar);
            cameras.freeLook.position.set(10, 10, 15);""", 1)
text = text.replace("""            renderer.setAnimationLoop(animate);""", """            updateZoomReadout();
            renderer.setAnimationLoop(animate);""", 1)

path.write_text(text)
print('Applied mobile parity, zoom, and Free Cam')
