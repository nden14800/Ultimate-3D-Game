from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()


def replace_once(old, new, label):
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    text = text.replace(old, new, 1)


def replace_between(start_marker, end_marker, replacement, label):
    global text
    start = text.find(start_marker)
    if start < 0:
        raise RuntimeError(f'{label}: start marker not found')
    end = text.find(end_marker, start)
    if end < 0:
        raise RuntimeError(f'{label}: end marker not found')
    text = text[:start] + replacement + text[end:]


css = r'''

        /* Phase 14: CC0 character, atmosphere, city props, and CityLink device. */
        #city-phone { position:fixed; z-index:181; right:calc(20px + env(safe-area-inset-right)); bottom:calc(18px + env(safe-area-inset-bottom)); width:min(372px,calc(100vw - 32px)); max-height:calc(100dvh - 36px); color:#eaf8ff; pointer-events:auto; transition:opacity .18s ease,transform .18s ease; }
        #city-phone.hidden { opacity:0; pointer-events:none; transform:translateY(24px) scale(.96); visibility:hidden; }
        .city-phone-shell { position:relative; overflow:hidden; border:4px solid #07131f; border-radius:38px; background:radial-gradient(circle at 20% 0%,rgba(72,188,255,.38),transparent 30%),linear-gradient(155deg,#082746,#0c5075 46%,#07182d); box-shadow:0 14px 0 rgba(0,0,0,.46),0 35px 80px rgba(0,0,0,.5),inset 0 0 0 2px rgba(182,239,255,.22); }
        .city-phone-shell::after { position:absolute; z-index:0; inset:0; background:linear-gradient(110deg,rgba(255,255,255,.12),transparent 23%,transparent 76%,rgba(126,218,255,.10)); content:''; pointer-events:none; }
        .city-phone-top { position:relative; z-index:1; display:flex; justify-content:space-between; align-items:center; min-height:31px; padding:8px 42px 4px 16px; color:#d8f7ff; font-size:10px; font-weight:900; letter-spacing:.06em; } .city-phone-sensors { position:absolute; z-index:2; top:9px; left:50%; width:92px; height:18px; transform:translateX(-50%); border-radius:999px; background:#02080f; box-shadow:inset 0 1px 2px rgba(255,255,255,.08); }
        #city-phone-close { position:absolute; z-index:3; top:7px; right:8px; width:29px; height:29px; border:1px solid rgba(215,248,255,.5); border-radius:10px; color:#eafaff; background:rgba(2,21,39,.54); font-size:18px; line-height:1; }
        .city-phone-main { position:relative; z-index:1; display:grid; gap:10px; padding:8px 13px 14px; } .city-phone-brand { display:flex; align-items:end; justify-content:space-between; gap:8px; padding:4px 3px; } .city-phone-brand b { display:block; color:#fff; font-size:22px; letter-spacing:-.06em; } .city-phone-brand small { display:block; color:#8fe3ff; font-size:8px; font-weight:900; letter-spacing:.13em; }
        .phone-weather-card { display:grid; grid-template-columns:auto 1fr auto; align-items:center; gap:10px; min-height:66px; padding:11px; border:1px solid rgba(181,237,255,.35); border-radius:19px; background:linear-gradient(135deg,rgba(73,177,246,.3),rgba(6,46,82,.72)); box-shadow:inset 0 1px 0 rgba(255,255,255,.13); } .phone-weather-icon { display:grid; width:42px; height:42px; place-items:center; border-radius:14px; background:rgba(183,242,255,.17); font-size:24px; } .phone-weather-card b { display:block; font-size:13px; } .phone-weather-card span { display:block; margin-top:3px; color:#b6eaff; font-size:10px; font-weight:700; } .phone-weather-card strong { color:#fff; font-size:17px; }
        .city-phone-apps { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; } .phone-app { display:flex; min-height:64px; flex-direction:column; align-items:center; justify-content:center; gap:4px; border:1px solid rgba(213,249,255,.34); border-radius:16px; color:#effbff; background:rgba(4,33,59,.62); box-shadow:inset 0 1px 0 rgba(255,255,255,.11); font-size:8px; font-weight:900; } .phone-app .bi-icon { width:19px; height:19px; color:#8fe6ff; } .phone-app:active { transform:scale(.96); background:rgba(57,163,222,.56); }
        .phone-live-grid { display:grid; grid-template-columns:1fr 1fr; gap:7px; } .phone-live-cell { min-width:0; padding:8px; border-radius:12px; background:rgba(0,12,27,.35); } .phone-live-cell small { display:block; color:#8fc9e2; font-size:8px; font-weight:850; letter-spacing:.1em; } .phone-live-cell b { display:block; overflow:hidden; margin-top:4px; color:#f3fcff; font-size:10px; text-overflow:ellipsis; white-space:nowrap; }
        .city-phone-note { margin:0; color:#a5d8ed; font-size:8px; font-weight:700; line-height:1.45; text-align:center; } .asset-credit { margin:10px 0 0; color:#7aa3bf; font-size:9px; line-height:1.5; }
        #quick-phone { color:#174e83; } #quick-phone .bi-icon { color:#176db0; }
        @media (pointer:coarse),(max-width:760px) { #city-phone { right:calc(8px + env(safe-area-inset-right)); bottom:calc(8px + env(safe-area-inset-bottom)); width:min(350px,calc(100vw - 16px)); } .city-phone-shell { border-radius:32px; } #mobile-action-rail #mobile-phone-button { display:flex; } }
'''
replace_once('\n        </style>\n', css + '\n        </style>\n', 'phase14 css')

replace_once(
    '<aside id="context-actions" aria-label="すばやいアクション"><button id="quick-camera" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#camera-reels-fill"></use></svg><span class="context-label">視点</span></button><button id="quick-car" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#car-front-fill"></use></svg><span class="context-label">乗り物</span></button><button id="quick-map" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#map-fill"></use></svg><span class="context-label">マップ</span></button></aside>',
    '<aside id="context-actions" aria-label="すばやいアクション"><button id="quick-camera" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#camera-reels-fill"></use></svg><span class="context-label">視点</span></button><button id="quick-car" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#car-front-fill"></use></svg><span class="context-label">乗り物</span></button><button id="quick-map" class="context-action"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#map-fill"></use></svg><span class="context-label">マップ</span></button><button id="quick-phone" class="context-action" type="button" aria-label="CityLink端末を開く"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#phone-fill"></use></svg><span class="context-label">端末</span></button></aside>',
    'desktop phone action'
)

replace_once(
    '<button id="mobile-pause-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#pause-fill"></use></svg>ポーズ</button></aside>',
    '<button id="mobile-pause-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#pause-fill"></use></svg>ポーズ</button><button id="mobile-phone-button" class="mobile-action" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#phone-fill"></use></svg>端末</button></aside>',
    'mobile phone action'
)

phone_html = r'''
    <section id="city-phone" class="hidden" aria-label="CityLink端末" role="dialog" aria-modal="true">
        <div class="city-phone-shell">
            <div class="city-phone-sensors" aria-hidden="true"></div><button id="city-phone-close" type="button" aria-label="端末を閉じる">×</button>
            <div class="city-phone-top"><span id="phone-time">12:00</span><span id="phone-status">CITYLINK · LOCAL</span></div>
            <div class="city-phone-main"><div class="city-phone-brand"><div><small>CITYLINK OS · SANDBOX EDITION</small><b>CityLink S26</b></div><small>IN-GAME DEVICE</small></div>
                <div class="phone-weather-card"><span id="phone-weather-icon" class="phone-weather-icon">☀</span><div><b id="phone-weather-label">晴れ</b><span id="phone-weather-detail">街の探索に適した空模様</span></div><strong id="phone-weather-temp">22°</strong></div>
                <div class="city-phone-apps"><button class="phone-app" type="button" data-phone-action="map"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#map-fill"></use></svg>ATLAS</button><button class="phone-app" type="button" data-phone-action="weather"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#cloud-sun-fill"></use></svg>WEATHER</button><button class="phone-app" type="button" data-phone-action="social"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#chat-square-text-fill"></use></svg>PEOPLE</button><button class="phone-app" type="button" data-phone-action="settings"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#gear-fill"></use></svg>SETTINGS</button></div>
                <div class="phone-live-grid"><div class="phone-live-cell"><small>POSITION</small><b id="phone-coords">X 0 · Z 0</b></div><div class="phone-live-cell"><small>RESIDENTS</small><b id="phone-npcs">0 ACTIVE</b></div><div class="phone-live-cell"><small>MODE</small><b id="phone-mode">ON FOOT</b></div><div class="phone-live-cell"><small>QUALITY</small><b id="phone-quality">PREMIUM</b></div></div>
                <p class="city-phone-note">Galaxy S26風のサイズ感を採用した、ブランド非提携・独自設計のゲーム内端末です。</p>
            </div>
        </div>
    </section>
'''
replace_once('\n    <div id="zoom-readout" class="zoom-readout" aria-live="polite">視点 1.0×</div>\n', phone_html + '\n    <div id="zoom-readout" class="zoom-readout" aria-live="polite">視点 1.0×</div>\n', 'phone DOM')

replace_once(
    '<div class="track-readout"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#soundwave"></use></svg><span><b>Neon City Drift</b><br>完全オリジナル・インストゥルメンタル</span></div>',
    '<div class="track-readout"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#soundwave"></use></svg><span><b>Neon City Drift</b><br>完全オリジナル・インストゥルメンタル</span></div><p class="asset-credit">環境音クレジット: Strong Wind Blowing — Flixberry Entertainment (CC BY 3.0/4.0)</p>',
    'wind credit'
)

replace_once(
    "        import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';\n",
    "        import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';\n        import { clone as cloneSkeleton } from 'three/addons/utils/SkeletonUtils.js';\n",
    'skeleton clone import'
)

replace_once(
    "        let selectedWorldId = 'harbor';\n        const externalModelTemplates = new Map();\n        let externalModelsReady = false;\n        const EXTERNAL_MODEL_SOURCES = {\n            hatchback: 'assets/models/kenney/car/hatchback-sports.glb',\n            delivery: 'assets/models/kenney/car/delivery.glb',\n            taxi: 'assets/models/kenney/car/taxi.glb',\n            buildingA: 'assets/models/kenney/city/building-type-a.glb',\n            buildingF: 'assets/models/kenney/city/building-type-f.glb'\n        };\n",
    "        let selectedWorldId = 'harbor';\n        const externalModelTemplates = new Map();\n        const externalModelAnimations = new Map();\n        let externalModelsReady = false;\n        let playerMixer = null, currentPlayerAnimation = null, phoneVisual = null, cityPhoneOpen = false;\n        const npcMixers = new Map();\n        let lastFootstepAt = 0;\n        const EXTERNAL_MODEL_SOURCES = {\n            hatchback: 'assets/models/kenney/car/hatchback-sports.glb',\n            delivery: 'assets/models/kenney/car/delivery.glb',\n            taxi: 'assets/models/kenney/car/taxi.glb',\n            buildingA: 'assets/models/kenney/city/building-type-a.glb',\n            buildingF: 'assets/models/kenney/city/building-type-f.glb',\n            character: 'assets/models/cc0-characters/animated-platformer-character.glb',\n            cloudCluster: 'assets/models/cc0-weather/cloud-cluster.glb',\n            treeDetailed: 'assets/models/kenney/nature/tree-detailed.glb',\n            treeOak: 'assets/models/kenney/nature/tree-oak.glb',\n            treePine: 'assets/models/kenney/nature/tree-pine.glb',\n            bushDetailed: 'assets/models/kenney/nature/bush-detailed.glb',\n            rockLarge: 'assets/models/kenney/nature/rock-large.glb',\n            streetlight: 'assets/models/kenney/roads/streetlight.glb',\n            streetSign: 'assets/models/kenney/roads/street-sign.glb',\n            roadBarrier: 'assets/models/kenney/roads/road-barrier.glb',\n            smartphone: 'assets/models/cc0-props/smartphone.glb'\n        };\n",
    'external model sources'
)

replace_once(
    "        let weatherParticles, cloudLayer = null, directionalLight, ambientLight, hemisphereLight, sandboxGround;\n",
    "        let weatherParticles, cloudLayer = null, directionalLight, ambientLight, hemisphereLight, sandboxGround;\n        const weatherAudio = { rain:null, wind:null };\n        const sfxAudio = new Map();\n",
    'audio state'
)

replace_once(
    "                const visible = wanted.has(key);\n                chunk.group.visible = visible;\n                if (!visible && Math.max(Math.abs(chunk.cx - focus.cx), Math.abs(chunk.cz - focus.cz)) > retainRadius) unloadChunk(key);\n",
    "                const visible = wanted.has(key);\n                chunk.group.visible = visible;\n                if (visible && externalModelsReady) { decorateChunkWithExternalBuilding(chunk); decorateChunkWithExternalScenery(chunk); }\n                if (!visible && Math.max(Math.abs(chunk.cx - focus.cx), Math.abs(chunk.cz - focus.cz)) > retainRadius) unloadChunk(key);\n",
    'chunk scenery streaming'
)

replace_once(
    "            const entries=specs.map(spec=>({position:spec.entrance.clone(),label:spec.label,spec,chunkKey:chunkKey(cx,cz),visible:true}));buildings.push(...entries);const colliders=specs.map(spec=>({minX:spec.x-spec.size*.53,maxX:spec.x+spec.size*.53,minZ:spec.z-spec.size*.53,maxZ:spec.z+spec.size*.53,kind:'building'}));let hub=null;if(cx===0&&cz===0){hub=createCityHubExterior(new THREE.Vector3(20,0,20));group.add(hub.group);colliders.push(...hub.colliders);activeCityHub=hub;}mapObjects.add(group);const chunkRecord={cx,cz,group,ground,specs,entries,colliders,hub,buildingVisuals:{buildingMesh,roofMesh,roofUnits,facadeMesh,entryMesh},externalBuildingAdded:false};loadedChunks.set(chunkKey(cx,cz),chunkRecord);if(externalModelsReady)decorateChunkWithExternalBuilding(chunkRecord);sandboxGround=ground;chunkLoadCount++;\n",
    "            const entries=specs.map(spec=>({position:spec.entrance.clone(),label:spec.label,spec,chunkKey:chunkKey(cx,cz),visible:true}));buildings.push(...entries);const colliders=specs.map(spec=>({minX:spec.x-spec.size*.53,maxX:spec.x+spec.size*.53,minZ:spec.z-spec.size*.53,maxZ:spec.z+spec.size*.53,kind:'building'}));let hub=null;if(cx===0&&cz===0){hub=createCityHubExterior(new THREE.Vector3(20,0,20));group.add(hub.group);colliders.push(...hub.colliders);activeCityHub=hub;}mapObjects.add(group);const chunkRecord={cx,cz,group,ground,specs,entries,colliders,hub,buildingVisuals:{buildingMesh,roofMesh,roofUnits,facadeMesh,entryMesh},externalBuildingAdded:false,externalSceneryAdded:false};loadedChunks.set(chunkKey(cx,cz),chunkRecord);if(externalModelsReady){decorateChunkWithExternalBuilding(chunkRecord);decorateChunkWithExternalScenery(chunkRecord);}sandboxGround=ground;chunkLoadCount++;\n",
    'chunk scenery record'
)

external_library = r'''        function cloneExternalTemplate(key) {
            const template = externalModelTemplates.get(key);
            return template ? cloneSkeleton(template) : null;
        }

        function createExternalCloudClusters() {
            if (!cloudLayer || cloudLayer.userData.externalCloudsAdded || !externalModelTemplates.has('cloudCluster')) return;
            cloudLayer.userData.externalCloudsAdded = true;
            for (let index = 0; index < 8; index++) {
                const cloud = normalizeExternalObject(cloneExternalTemplate('cloudCluster'), 20 + hash2D(index, 9, 701) * 13, 7.5);
                cloud.name = 'cc0-cloud-cluster';
                cloud.position.set((hash2D(index, 13, 709) - .5) * 160, 30 + hash2D(index, 17, 719) * 26, (hash2D(index, 21, 727) - .5) * 160);
                cloud.rotation.y = hash2D(index, 23, 733) * Math.PI * 2;
                cloud.userData.phase = hash2D(index, 29, 739) * Math.PI * 2;
                cloud.traverse(node => { if (node.isMesh) { node.castShadow = false; node.receiveShadow = false; } });
                cloudLayer.add(cloud);
            }
        }

        function decorateChunkWithExternalScenery(chunk) {
            if (!externalModelsReady || chunk.externalSceneryAdded) return;
            const center = new THREE.Vector3(chunk.cx * CHUNK_SIZE + CHUNK_SIZE / 2, 0, chunk.cz * CHUNK_SIZE + CHUNK_SIZE / 2);
            if (center.distanceToSquared(playerGroup.position) > (CHUNK_SIZE * 2.15) ** 2) return;
            const addProp = (key, x, z, footprint, height, colliderRadius = 0, rotation = 0) => {
                const visual = cloneExternalTemplate(key);
                if (!visual) return;
                normalizeExternalObject(visual, footprint, height);
                visual.position.x += x; visual.position.z += z; visual.rotation.y = rotation;
                visual.name = `cc0-${key}-scenery`;
                visual.traverse(node => { if (node.isMesh) { node.castShadow = qualityMode === 'visual'; node.receiveShadow = true; } });
                chunk.group.add(visual);
                if (colliderRadius > 0) chunk.colliders.push({ minX:x-colliderRadius, maxX:x+colliderRadius, minZ:z-colliderRadius, maxZ:z+colliderRadius, kind:'cc0-scenery' });
            };
            for (let index = 0; index < 4; index++) {
                const x = chunk.cx * CHUNK_SIZE + 6 + hash2D(chunk.cx, chunk.cz, 801 + index) * (CHUNK_SIZE - 12);
                const z = chunk.cz * CHUNK_SIZE + 6 + hash2D(chunk.cx, chunk.cz, 811 + index) * (CHUNK_SIZE - 12);
                if (isRoadCoordinate(x) || isRoadCoordinate(z) || chunk.specs.some(spec => Math.abs(spec.x - x) < spec.size + 1.7 && Math.abs(spec.z - z) < spec.size + 1.7)) continue;
                const key = ['treeDetailed', 'treeOak', 'treePine'][index % 3];
                addProp(key, x, z, 2.5 + hash2D(chunk.cx, chunk.cz, 821 + index) * 1.5, 7, 1.05, hash2D(chunk.cx, chunk.cz, 831 + index) * Math.PI * 2);
                if (index % 2 === 0) addProp('bushDetailed', x + 2.2, z - 1.3, 1.3, 1.35, .44, hash2D(chunk.cx, chunk.cz, 841 + index) * Math.PI * 2);
            }
            const origin = chunkOrigin(chunk.cx, chunk.cz);
            for (let n = 0; n < 2; n++) {
                const road = n === 0 ? Math.ceil(origin.x / ROAD_INTERVAL) * ROAD_INTERVAL : Math.ceil(origin.z / ROAD_INTERVAL) * ROAD_INTERVAL;
                const side = n === 0 ? (hash2D(chunk.cx, chunk.cz, 851) > .5 ? 1 : -1) : (hash2D(chunk.cx, chunk.cz, 853) > .5 ? 1 : -1);
                const x = n === 0 ? road + side * (ROAD_WIDTH * .5 + .7) : origin.x + 16;
                const z = n === 0 ? origin.z + 16 : road + side * (ROAD_WIDTH * .5 + .7);
                addProp('streetlight', x, z, .8, 7.5, .32, n === 0 ? 0 : Math.PI / 2);
                if ((chunk.cx + chunk.cz + n) % 2 === 0) addProp('streetSign', x + (n === 0 ? 1.3 : 0), z + (n === 0 ? 0 : 1.3), .8, 2.4, .25, n === 0 ? 0 : Math.PI / 2);
                if ((chunk.cx - chunk.cz + n) % 3 === 0) addProp('roadBarrier', x + (n === 0 ? 2.5 : 0), z + (n === 0 ? 0 : 2.5), 1.5, 1.1, .5, n === 0 ? 0 : Math.PI / 2);
            }
            chunk.externalSceneryAdded = true;
        }

        function decorateExternalScenery() { loadedChunks.forEach(decorateChunkWithExternalScenery); }

        function initializePhoneVisual() {
            if (phoneVisual || !externalModelTemplates.has('smartphone')) return;
            phoneVisual = normalizeExternalObject(cloneExternalTemplate('smartphone'), .62, 1.15);
            phoneVisual.name = 'cc0-citylink-s26-device';
            phoneVisual.position.set(.59, -.46, -1.12);
            phoneVisual.rotation.set(.07, Math.PI, -.16);
            phoneVisual.visible = false;
            phoneVisual.traverse(node => { if (node.isMesh) { node.castShadow = false; node.receiveShadow = false; } });
        }

        function syncPhoneVisual() {
            if (!phoneVisual || !currentCamera) return;
            if (cityPhoneOpen && phoneVisual.parent !== currentCamera) currentCamera.add(phoneVisual);
            phoneVisual.visible = cityPhoneOpen;
        }

        function loadExternalModelLibrary() {
            const loader = new GLTFLoader();
            const entries = Object.entries(EXTERNAL_MODEL_SOURCES);
            Promise.allSettled(entries.map(([key, url]) => new Promise((resolve, reject) => {
                loader.load(url, gltf => {
                    const root = gltf.scene || gltf.scenes?.[0];
                    if (!root) { reject(new Error(`No scene in ${url}`)); return; }
                    externalModelTemplates.set(key, prepareExternalTemplate(root));
                    externalModelAnimations.set(key, gltf.animations || []);
                    resolve(key);
                }, undefined, reject);
            }))).then(results => {
                const loaded = results.filter(result => result.status === 'fulfilled').map(result => result.value);
                const failed = results.filter(result => result.status === 'rejected');
                externalModelsReady = loaded.length > 0;
                applyExternalVehicleModels();
                decorateExternalBuildings();
                decorateExternalScenery();
                createExternalCloudClusters();
                applyExternalCharacterModels();
                initializePhoneVisual();
                if (failed.length) console.warn('一部のCC0モデルを読み込めなかったため、標準モデルを維持します。', failed);
                if (gameStarted) setSandboxMessage(`CC0外部モデル ${loaded.length}/${entries.length} 件を適用しました。`);
            }).catch(error => console.warn('CC0モデルの初期化に失敗したため、標準モデルを使用します。', error));
        }

'''
replace_between('        function loadExternalModelLibrary() {', '        function createVehicleModel(type, traffic = false) {', external_library, 'external model library')

character_prefix = r'''        function installCharacterAnimation(group, visual, isNpc) {
            const clips = externalModelAnimations.get('character') || [];
            if (!clips.length) return;
            const mixer = new THREE.AnimationMixer(visual);
            const actions = {};
            ['Idle', 'Walk', 'Run'].forEach(name => {
                const clip = clips.find(candidate => candidate.name.endsWith(`|${name}`) || candidate.name === name);
                if (clip) { const action = mixer.clipAction(clip); action.enabled = true; action.setLoop(THREE.LoopRepeat, Infinity); actions[name] = action; }
            });
            if (!actions.Idle) return;
            group.userData.animationController = { mixer, actions, active:null, isNpc };
            if (isNpc) npcMixers.set(group, mixer); else playerMixer = mixer;
            setCharacterAnimation(group, 'Idle', true);
        }

        function setCharacterAnimation(group, requested, force = false) {
            const controller = group?.userData?.animationController;
            if (!controller) return;
            const actionName = controller.actions[requested] ? requested : 'Idle';
            if (!force && controller.active === actionName) return;
            const next = controller.actions[actionName];
            const previous = controller.active && controller.actions[controller.active];
            if (previous && previous !== next) previous.fadeOut(.16);
            next.reset().setEffectiveWeight(1).fadeIn(.16).play();
            controller.active = actionName;
            if (!controller.isNpc) currentPlayerAnimation = actionName;
        }

        function createExternalCharacter(type, isNpc) {
            const visual = cloneExternalTemplate('character');
            if (!visual) return null;
            const group = new THREE.Group();
            normalizeExternalObject(visual, isNpc ? 1.12 : 1.18, 2.15);
            visual.rotation.y = Math.PI;
            visual.traverse(node => { if (node.isMesh) { node.castShadow = !isNpc || qualityMode === 'visual'; node.receiveShadow = true; } });
            group.add(visual);
            installCharacterAnimation(group, visual, isNpc);
            return group;
        }

        function applyExternalCharacterModels() {
            if (!externalModelTemplates.has('character')) return;
            if (playerGroup && character) {
                playerGroup.remove(character);
                if (playerMixer) { playerMixer.stopAllAction(); playerMixer = null; }
                character = createCharacter(currentCharacterType, false);
                playerGroup.add(character);
            }
            npcs.slice().forEach((npc, index) => {
                const modern = createCharacter(index % 6, true);
                if (!modern) return;
                modern.position.copy(npc.position); modern.quaternion.copy(npc.quaternion);
                modern.userData = { ...modern.userData, ...npc.userData };
                npcMixers.delete(npc);
                scene.remove(npc); scene.add(modern); npcs[index] = modern;
            });
        }

        function updateCharacterMotion(delta) {
            if (character) {
                const action = (controlledVehicle || ridingTransit || currentSpeedMs < .15) ? 'Idle' : (currentSpeedMs > 7.2 ? 'Run' : 'Walk');
                setCharacterAnimation(character, action);
                character.userData?.animationController?.mixer.update(delta);
            }
            npcMixers.forEach((mixer, npc) => mixer.update(delta));
        }

'''
replace_once('        function createCharacter(type, isNpc = false) {\n', character_prefix + '        function createCharacter(type, isNpc = false) {\n            const externalCharacter = createExternalCharacter(type, isNpc);\n            if (externalCharacter) {\n                const chatDiv = document.createElement(\'div\'); chatDiv.className = \'chat-bubble\';\n                const chatLabel = new CSS2DObject(chatDiv); chatLabel.position.set(0, 2.2, 0); chatLabel.visible = false; externalCharacter.add(chatLabel);\n                return externalCharacter;\n            }\n', 'external character entry')

replace_once(
    '                npc.userData = { name: "NPC " + (npcIndex + 1), id: 1000 + npcIndex + 1, persona: NPC_PERSONAS[npcIndex % NPC_PERSONAS.length] };\n',
    '                npc.userData = { ...npc.userData, name: "NPC " + (npcIndex + 1), id: 1000 + npcIndex + 1, persona: NPC_PERSONAS[npcIndex % NPC_PERSONAS.length] };\n',
    'preserve npc animation controller'
)

replace_once(
    '                const npcToRemove = npcs.pop();\n                scene.remove(npcToRemove);\n',
    '                const npcToRemove = npcs.pop();\n                npcMixers.delete(npcToRemove);\n                scene.remove(npcToRemove);\n',
    'remove npc mixer'
)

replace_once(
    '                if ((brain.state === \'wait\' || brain.state === \'talk\') && time < brain.stateUntil) continue;\n',
    '                if ((brain.state === \'wait\' || brain.state === \'talk\') && time < brain.stateUntil) { setCharacterAnimation(npc, \'Idle\'); continue; }\n',
    'npc idle state'
)

replace_once(
    '                if (toTarget.lengthSq() < 2.25) { enterNpcWait(npc, time); continue; }\n',
    '                if (toTarget.lengthSq() < 2.25) { enterNpcWait(npc, time); setCharacterAnimation(npc, \'Idle\'); continue; }\n',
    'npc arrival idle'
)

replace_once(
    '                npc.position.addScaledVector(desired, brain.speed * delta * stride);\n                const targetAngle = Math.atan2(desired.x, desired.z);\n',
    '                npc.position.addScaledVector(desired, brain.speed * delta * stride);\n                setCharacterAnimation(npc, brain.speed > 1.6 ? \'Run\' : \'Walk\');\n                const targetAngle = Math.atan2(desired.x, desired.z);\n',
    'npc locomotion animation'
)

audio_phone_functions = r'''
        const SFX_ASSETS = { tap:'assets/audio/sfx/ui-tap.ogg', confirm:'assets/audio/sfx/ui-confirm.ogg', back:'assets/audio/sfx/ui-back.ogg', error:'assets/audio/sfx/ui-error.ogg', concrete:'assets/audio/sfx/footstep-concrete.ogg', grass:'assets/audio/sfx/footstep-grass.ogg', snow:'assets/audio/sfx/footstep-snow.ogg' };
        function playSfx(name, volume = .34) {
            const source = SFX_ASSETS[name]; if (!source) return;
            const base = sfxAudio.get(name) || new Audio(source); base.preload = 'auto'; sfxAudio.set(name, base);
            const instance = base.paused ? base : base.cloneNode(true);
            instance.volume = Math.max(0, Math.min(1, volume));
            instance.currentTime = 0;
            instance.play().catch(() => {});
        }
        function ensureWeatherAudio(kind, source, volume) {
            if (!weatherAudio[kind]) { const audio = new Audio(source); audio.loop = true; audio.preload = 'metadata'; audio.volume = volume; weatherAudio[kind] = audio; }
            return weatherAudio[kind];
        }
        function syncWeatherAudio(weather = document.getElementById('weather-select')?.value) {
            const rain = ensureWeatherAudio('rain', 'assets/audio/weather/rain-gutter-loop.mp3', .23);
            const wind = ensureWeatherAudio('wind', 'assets/audio/weather/strong-wind-blowing.mp3', .12);
            const wanted = { rain: weather === 'rainy', wind: weather === 'snowy' || weather === 'cloudy' };
            Object.entries(weatherAudio).forEach(([kind, audio]) => {
                if (!audio) return;
                if (wanted[kind] && gameStarted && !gamePaused && !cityPhoneOpen) audio.play().catch(() => {});
                else audio.pause();
            });
        }
        function pauseWeatherAudio() { Object.values(weatherAudio).forEach(audio => audio?.pause()); }
        function updateFootsteps(time) {
            if (controlledVehicle || ridingTransit || currentSpeedMs < .25 || !characterDirection || characterDirection.lengthSq() < .001) return;
            const cadence = currentSpeedMs > 7.2 ? 270 : 420;
            if (time - lastFootstepAt < cadence) return;
            lastFootstepAt = time;
            const weather = document.getElementById('weather-select')?.value;
            const key = weather === 'snowy' ? 'snow' : (isRoadCoordinate(playerGroup.position.x) || isRoadCoordinate(playerGroup.position.z) ? 'concrete' : 'grass');
            playSfx(key, .18);
        }
        function updateCityPhoneUi() {
            const phone = document.getElementById('city-phone'); if (!phone) return;
            const weather = document.getElementById('weather-select')?.value || 'sunny';
            const meta = { sunny:['☀','晴れ','澄んだ都市の空','22°'], cloudy:['☁','くもり','穏やかな雲の流れ','18°'], rainy:['☔','雨','雨音と路面の反射','15°'], snowy:['❄','雪','静かな降雪と風','-1°'] }[weather];
            const target = getControlledObject?.() || playerGroup;
            const time = document.getElementById('world-time-readout')?.textContent || document.getElementById('time-label')?.textContent || '12:00';
            document.getElementById('phone-time').textContent = time;
            document.getElementById('phone-weather-icon').textContent = meta[0]; document.getElementById('phone-weather-label').textContent = meta[1]; document.getElementById('phone-weather-detail').textContent = meta[2]; document.getElementById('phone-weather-temp').textContent = meta[3];
            document.getElementById('phone-coords').textContent = target ? `X ${target.position.x.toFixed(0)} · Z ${target.position.z.toFixed(0)}` : 'X 0 · Z 0';
            document.getElementById('phone-npcs').textContent = `${npcs.length} ACTIVE`;
            document.getElementById('phone-mode').textContent = controlledVehicle ? 'DRIVING' : ridingTransit ? 'TRANSIT' : 'ON FOOT';
            document.getElementById('phone-quality').textContent = ({ performance:'LIGHT', balanced:'PREMIUM', visual:'ULTRA' })[qualityMode] || 'PREMIUM';
        }
        function setCityPhoneOpen(value) {
            if (!gameStarted && value) return;
            cityPhoneOpen = Boolean(value); Object.keys(keys).forEach(key => { keys[key] = false; }); mobileInput.x = mobileInput.z = 0;
            document.getElementById('city-phone').classList.toggle('hidden', !cityPhoneOpen);
            if (cityPhoneOpen) { updateCityPhoneUi(); syncWeatherAudio(); playSfx('tap', .25); }
            else { syncWeatherAudio(); playSfx('back', .23); }
            syncPhoneVisual();
        }
        function toggleCityPhone() { setCityPhoneOpen(!cityPhoneOpen); }
        function handlePhoneAction(action) {
            if (action === 'map') { setCityPhoneOpen(false); openCityAtlas(); return; }
            if (action === 'weather') { const values=['sunny','cloudy','rainy','snowy']; const field=document.getElementById('weather-select'); field.value=values[(values.indexOf(field.value)+1)%values.length]; changeWeather(field.value); updateCityPhoneUi(); playSfx('confirm'); return; }
            if (action === 'social') { setCityPhoneOpen(false); document.getElementById('chat-ui').classList.remove('collapsed'); document.getElementById('chat-input').focus(); return; }
            if (action === 'settings') { setCityPhoneOpen(false); openWorldSettings(); }
        }
'''
replace_once('        function updateTime(hour) {\n', audio_phone_functions + '\n        function updateTime(hour) {\n', 'audio and phone functions')

replace_once(
    "if(cloudLayer)cloudLayer.visible=weather!=='sunny'||qualityMode==='visual';\n        }\n",
    "if(cloudLayer)cloudLayer.visible=weather!=='sunny'||qualityMode==='visual';syncWeatherAudio(weather);updateCityPhoneUi();\n        }\n",
    'weather audio synchronization'
)

replace_once(
    "                if (!e.repeat && (key === 'Escape' || key === 'p') && gameStarted && !editable) { e.preventDefault(); togglePause(); return; }\n",
    "                if (!e.repeat && key === 'Escape' && cityPhoneOpen) { e.preventDefault(); setCityPhoneOpen(false); return; }\n                if (!e.repeat && (key === 'Escape' || key === 'p') && gameStarted && !editable) { e.preventDefault(); togglePause(); return; }\n",
    'phone escape'
)

replace_once(
    "                if (!e.repeat && key === 'Tab') { e.preventDefault(); toggleFieldPack(); return; }\n",
    "                if (!e.repeat && key === 'f') { e.preventDefault(); toggleCityPhone(); return; }\n                if (!e.repeat && key === 'Tab') { e.preventDefault(); toggleFieldPack(); return; }\n",
    'phone key'
)

replace_once(
    "            document.getElementById('quick-map').addEventListener('click', () => { document.getElementById('map-container').classList.toggle('map-emphasis'); setSandboxMessage('ミニマップをクリックして目的地を決められます。'); });\n",
    "            document.getElementById('quick-map').addEventListener('click', () => { document.getElementById('map-container').classList.toggle('map-emphasis'); setSandboxMessage('ミニマップをクリックして目的地を決められます。'); });\n            document.getElementById('quick-phone').addEventListener('click', toggleCityPhone);\n",
    'desktop phone listener'
)

replace_once(
    "            document.getElementById('mobile-pause-button').addEventListener('click', togglePause);\n",
    "            document.getElementById('mobile-pause-button').addEventListener('click', togglePause);\n            document.getElementById('mobile-phone-button').addEventListener('click', toggleCityPhone);\n            document.getElementById('city-phone-close').addEventListener('click', () => setCityPhoneOpen(false));\n            document.querySelectorAll('[data-phone-action]').forEach(button => button.addEventListener('click', () => handlePhoneAction(button.dataset.phoneAction)));\n            document.addEventListener('click', event => { const button = event.target.closest('button'); if (button && !button.closest('#city-phone')) playSfx(button.id?.includes('close') || button.id?.includes('back') ? 'back' : 'tap', .16); }, { passive:true });\n",
    'phone and generic sfx listeners'
)

replace_once(
    "            playBgm();\n            setSandboxMessage('街へようこそ。好きなように遊ぼう！');\n",
    "            playBgm();\n            syncWeatherAudio();\n            setSandboxMessage('街へようこそ。Fキーまたは端末ボタンでCityLinkを開けます。');\n",
    'start weather audio'
)

replace_once(
    "            duckBgm(value);\n            if (value) {\n",
    "            duckBgm(value);\n            if (value) { pauseWeatherAudio(); if (cityPhoneOpen) setCityPhoneOpen(false); } else syncWeatherAudio();\n            if (value) {\n",
    'pause weather audio'
)

replace_once(
    "            pauseBgm();\n            document.getElementById('title-screen').classList.remove('hidden');\n",
    "            pauseBgm();\n            pauseWeatherAudio();\n            if (cityPhoneOpen) setCityPhoneOpen(false);\n            document.getElementById('title-screen').classList.remove('hidden');\n",
    'return title weather audio'
)

replace_once(
    "            if (!gameStarted || gamePaused) {\n                renderer.render(scene, currentCamera);\n                return;\n            }\n",
    "            if (!gameStarted || gamePaused || cityPhoneOpen) {\n                syncPhoneVisual();\n                renderer.render(scene, currentCamera);\n                return;\n            }\n",
    'phone gameplay pause'
)

replace_once(
    "            updateCloudLayer(time, controlledObject.position);\n            handleNpcChat(time);\n",
    "            updateCloudLayer(time, controlledObject.position);\n            updateCharacterMotion(delta);\n            updateFootsteps(time);\n            syncPhoneVisual();\n            handleNpcChat(time);\n",
    'character motion and footstep loop'
)

path.write_text(text)
print('Phase 14 CC0 asset, animation, audio, and CityLink integration applied.')
