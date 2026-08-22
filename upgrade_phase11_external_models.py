from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()

def replace_once(old, new, label):
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected exactly 1 match, found {count}')
    text = text.replace(old, new, 1)

replace_once(
"        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';\n",
"        import { CSS2DRenderer, CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';\n        import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';\n",
"GLTFLoader import",
)

replace_once(
"        let selectedWorldId = 'harbor';\n",
"        let selectedWorldId = 'harbor';\n        const externalModelTemplates = new Map();\n        let externalModelsReady = false;\n        const EXTERNAL_MODEL_SOURCES = {\n            hatchback: 'assets/models/kenney/hatchback-sports.glb',\n            delivery: 'assets/models/kenney/delivery.glb',\n            taxi: 'assets/models/kenney/taxi.glb',\n            buildingA: 'assets/models/kenney/building-type-a.glb',\n            buildingF: 'assets/models/kenney/building-type-f.glb'\n        };\n",
"external model state",
)

replace_once(
"            createCityMap();\n            createSandboxWorld();\n            drawMapBackground();\n",
"            createCityMap();\n            createSandboxWorld();\n            loadExternalModelLibrary();\n            drawMapBackground();\n",
"model loader init",
)

marker = "        function createVehicleModel(type, traffic = false) {\n"
external_code = r'''        function prepareExternalTemplate(root) {
            root.traverse(node => {
                if (!node.isMesh) return;
                node.castShadow = false;
                node.receiveShadow = true;
                if (node.material) {
                    node.material = node.material.clone();
                    node.material.needsUpdate = true;
                }
            });
            return root;
        }

        function normalizeExternalObject(root, targetFootprint, targetHeight = Infinity) {
            root.updateMatrixWorld(true);
            const before = new THREE.Box3().setFromObject(root);
            const size = before.getSize(new THREE.Vector3());
            const horizontal = Math.max(size.x, size.z, 0.001);
            const vertical = Math.max(size.y, 0.001);
            const scale = Math.min(targetFootprint / horizontal, targetHeight / vertical);
            root.scale.setScalar(scale);
            root.updateMatrixWorld(true);
            const after = new THREE.Box3().setFromObject(root);
            root.position.y -= after.min.y;
            return root;
        }

        function vehicleExternalModelKey(type) {
            if (type === 'van') return 'delivery';
            if (type === 'taxi') return 'taxi';
            if (type === 'car' || type === 'sports') return 'hatchback';
            return null;
        }

        function attachExternalVehicleModel(vehicle) {
            const key = vehicleExternalModelKey(vehicle.userData.type);
            const template = key && externalModelTemplates.get(key);
            if (!template || vehicle.userData.externalVisual) return;
            const visual = normalizeExternalObject(template.clone(true), vehicle.userData.type === 'van' ? 4.0 : 3.55, 2.15);
            visual.position.y += 0.08;
            visual.name = `cc0-${key}-visual`;
            visual.traverse(node => { if (node.isMesh) { node.castShadow = !vehicle.userData.traffic; node.receiveShadow = true; } });
            vehicle.add(visual);
            vehicle.userData.proceduralChildren.forEach(child => { child.visible = false; });
            vehicle.userData.externalVisual = visual;
        }

        function applyExternalVehicleModels() {
            [...vehicles, ...trafficVehicles].forEach(attachExternalVehicleModel);
        }

        function hideProceduralBuilding(chunk, index) {
            const visual = chunk.buildingVisuals;
            if (!visual) return;
            const zero = new THREE.Matrix4().makeScale(0, 0, 0);
            [visual.buildingMesh, visual.roofMesh, visual.roofUnits, visual.entryMesh].forEach(mesh => {
                mesh.setMatrixAt(index, zero);
                mesh.instanceMatrix.needsUpdate = true;
            });
            for (let facadeIndex = index * 12; facadeIndex < index * 12 + 12; facadeIndex++) {
                visual.facadeMesh.setMatrixAt(facadeIndex, zero);
            }
            visual.facadeMesh.instanceMatrix.needsUpdate = true;
        }

        function decorateChunkWithExternalBuilding(chunk) {
            if (!externalModelsReady || chunk.externalBuildingAdded || !chunk.specs.length) return;
            const center = new THREE.Vector3(chunk.cx * CHUNK_SIZE + CHUNK_SIZE / 2, 0, chunk.cz * CHUNK_SIZE + CHUNK_SIZE / 2);
            if (center.distanceToSquared(playerGroup.position) > (CHUNK_SIZE * 2.15) ** 2) return;
            const index = Math.floor(hash2D(chunk.cx, chunk.cz, 611) * chunk.specs.length);
            const key = (chunk.cx + chunk.cz) % 2 === 0 ? 'buildingA' : 'buildingF';
            const template = externalModelTemplates.get(key);
            if (!template) return;
            const spec = chunk.specs[index];
            const visual = normalizeExternalObject(template.clone(true), spec.size * 1.02, spec.height * 0.94);
            visual.position.x += spec.x;
            visual.position.z += spec.z;
            visual.name = `cc0-${key}-landmark`;
            visual.traverse(node => { if (node.isMesh) { node.castShadow = qualityMode === 'visual'; node.receiveShadow = true; } });
            hideProceduralBuilding(chunk, index);
            chunk.group.add(visual);
            chunk.externalBuildingAdded = true;
        }

        function decorateExternalBuildings() {
            loadedChunks.forEach(decorateChunkWithExternalBuilding);
        }

        function loadExternalModelLibrary() {
            const loader = new GLTFLoader();
            const entries = Object.entries(EXTERNAL_MODEL_SOURCES);
            Promise.all(entries.map(([key, url]) => new Promise((resolve, reject) => {
                loader.load(url, gltf => {
                    const root = gltf.scene || gltf.scenes?.[0];
                    if (!root) { reject(new Error(`No scene in ${url}`)); return; }
                    externalModelTemplates.set(key, prepareExternalTemplate(root));
                    resolve(key);
                }, undefined, reject);
            }))).then(() => {
                externalModelsReady = true;
                applyExternalVehicleModels();
                decorateExternalBuildings();
                if (gameStarted) setSandboxMessage('CC0外部モデルを読み込み、近傍の車両と建物へ適用しました。');
            }).catch(error => {
                console.warn('CC0モデルは読み込めなかったため、標準モデルを使用します。', error);
            });
        }

'''
replace_once(marker, external_code + marker, "external model functions")

replace_once(
"            const ring = new THREE.Mesh(new THREE.RingGeometry(Math.max(1.35, type==='bus'||type==='tram'?2.1:1.35), Math.max(1.48, type==='bus'||type==='tram'?2.24:1.48), 32), new THREE.MeshBasicMaterial({ color:traffic?0xffd66d:0x86f4ff,transparent:true,opacity:0,side:THREE.DoubleSide }));\n",
"            const proceduralChildren = group.children.slice();\n            const ring = new THREE.Mesh(new THREE.RingGeometry(Math.max(1.35, type==='bus'||type==='tram'?2.1:1.35), Math.max(1.48, type==='bus'||type==='tram'?2.24:1.48), 32), new THREE.MeshBasicMaterial({ color:traffic?0xffd66d:0x86f4ff,transparent:true,opacity:0,side:THREE.DoubleSide }));\n",
"procedural visual marker",
)

replace_once(
"            group.userData={...palette,type,traffic,boardable:traffic && ['bus','tram','taxi'].includes(type),transit:['bus','tram'].includes(type),speed:traffic?palette.cruise*(.84+Math.random()*.18):0,steer:0,ring,active:false,axis:Math.random()>.5?'x':'z',direction:Math.random()>.5?1:-1,wheels,prompt,route:null,routeIndex:0,stopTimer:0,stopIndices:[],rolling:0};\n            return group;\n",
"            group.userData={...palette,type,traffic,boardable:traffic && ['bus','tram','taxi'].includes(type),transit:['bus','tram'].includes(type),speed:traffic?palette.cruise*(.84+Math.random()*.18):0,steer:0,ring,active:false,axis:Math.random()>.5?'x':'z',direction:Math.random()>.5?1:-1,wheels,prompt,route:null,routeIndex:0,stopTimer:0,stopIndices:[],rolling:0,proceduralChildren,externalVisual:null};\n            if (externalModelsReady) attachExternalVehicleModel(group);\n            return group;\n",
"vehicle external attachment",
)

replace_once(
"mapObjects.add(group);loadedChunks.set(chunkKey(cx,cz),{cx,cz,group,ground,specs,entries,colliders,hub});sandboxGround=ground;chunkLoadCount++;",
"mapObjects.add(group);const chunkRecord={cx,cz,group,ground,specs,entries,colliders,hub,buildingVisuals:{buildingMesh,roofMesh,roofUnits,facadeMesh,entryMesh},externalBuildingAdded:false};loadedChunks.set(chunkKey(cx,cz),chunkRecord);if(externalModelsReady)decorateChunkWithExternalBuilding(chunkRecord);sandboxGround=ground;chunkLoadCount++;",
"chunk external building record",
)

path.write_text(text)
print('External CC0 model integration applied.')
