from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()


def replace_between(source, start_marker, end_marker, replacement):
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    return source[:start] + replacement + source[end:]

css = r'''
        /* Phase 5: contextual vehicle and transit prompts. */
        .vehicle-proximity { display:flex; flex-direction:column; align-items:center; gap:2px; min-width:112px; padding:7px 10px; border:2px solid rgba(255,255,255,.9); border-radius:13px; color:#effaff; background:linear-gradient(145deg,rgba(7,42,78,.92),rgba(11,83,139,.9)); box-shadow:0 6px 0 rgba(0,16,36,.26),0 12px 24px rgba(0,0,0,.24); font:800 10px/1.1 system-ui,sans-serif; text-align:center; letter-spacing:.04em; } .vehicle-proximity b { display:inline-flex; min-width:20px; justify-content:center; padding:3px 5px; border-radius:6px; color:#173d64; background:#fff; font-size:11px; } .vehicle-proximity small { color:#aeeeff; font-size:8px; font-weight:800; }
'''
if 'Phase 5: contextual vehicle and transit prompts' not in text:
    text = text.replace('        </style>', css + '\n        </style>', 1)

text = text.replace("let selectedVehicle = null, controlledVehicle = null, nearestVehicle = null;\n        let vehicleSpeed = 0, vehicleSteer = 0, placeMode", "let selectedVehicle = null, controlledVehicle = null, ridingTransit = null, nearestVehicle = null;\n        let vehicleSpeed = 0, vehicleSteer = 0, placeMode", 1)

text = text.replace('<select id="vehicle-type" aria-label="乗り物タイプ"><option value="car">クルーザー</option><option value="sports">スポーツカー</option><option value="bike">ホバーバイク</option></select>', '<select id="vehicle-type" aria-label="乗り物タイプ"><option value="car">クルーザー</option><option value="sports">スポーツカー</option><option value="bike">ホバーバイク</option><option value="van">配達バン</option><option value="bicycle">シティバイク</option><option value="taxi">タクシー</option></select>', 1)
text = text.replace('車両・建物・NPCの近くで <kbd>E</kbd> または「使う」。</p><p>City Atlasで目的地を置き、徒歩または車の自動運転を開始できます。', '車両・建物・NPCの近くで <kbd>E</kbd> または「使う」。バス、路面電車、タクシーにも乗車できます。</p><p>City Atlasで目的地を置き、徒歩または車の自動運転を開始できます。', 1)

new_vehicle_block = r'''        function addVehicleWheel(group, x, z, radius, wheelMat, wheels, width = 0.25) {
            const wheel = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, width, 14), wheelMat);
            wheel.rotation.z = Math.PI / 2;
            wheel.position.set(x, radius + 0.08, z);
            wheel.castShadow = true; wheel.receiveShadow = true;
            group.add(wheel); wheels.push(wheel);
        }

        function addVehicleProximityLabel(group) {
            const div = document.createElement('div');
            div.className = 'vehicle-proximity';
            div.innerHTML = '<b>E</b><span>乗車</span><small>NEARBY VEHICLE</small>';
            const label = new CSS2DObject(div);
            label.position.set(0, 2.8, 0);
            label.visible = false;
            group.add(label);
            return label;
        }

        function createVehicleModel(type, traffic = false) {
            const group = new THREE.Group();
            const specs = {
                car: { body:0x3f9eff, trim:0x071a2b, max:32, accel:6.0, brake:14, coast:0.52, turn:1.82, wheelBase:2.15, label:'クルーザー', cruise:16, kind:'road' },
                sports: { body:0xff4f6d, trim:0x240611, max:52, accel:9.3, brake:20, coast:0.42, turn:2.16, wheelBase:2.2, label:'スポーツカー', cruise:24, kind:'road' },
                bike: { body:0x74edc0, trim:0x09221e, max:27, accel:7.0, brake:15, coast:0.62, turn:2.5, wheelBase:1.9, label:'ホバーバイク', cruise:14, kind:'road' },
                van: { body:0xe6edf4, trim:0x18354c, max:27, accel:4.7, brake:13, coast:0.58, turn:1.55, wheelBase:2.7, label:'配達バン', cruise:14, kind:'road' },
                bicycle: { body:0x43dba4, trim:0x172b34, max:12, accel:3.1, brake:8, coast:0.75, turn:2.9, wheelBase:1.55, label:'シティバイク', cruise:7, kind:'road' },
                taxi: { body:0xffc84b, trim:0x182635, max:30, accel:5.8, brake:14, coast:0.54, turn:1.72, wheelBase:2.15, label:'シティタクシー', cruise:15, kind:'taxi' },
                bus: { body:0x1f86df, trim:0x083050, max:17, accel:2.8, brake:8, coast:0.75, turn:0.88, wheelBase:4.5, label:'シティバス', cruise:11, kind:'bus' },
                tram: { body:0xf2eef2, trim:0x13587b, max:15, accel:2.4, brake:7, coast:0.78, turn:0.72, wheelBase:5.2, label:'路面電車', cruise:9.5, kind:'tram' }
            };
            const palette = specs[type] || specs.car;
            const bodyMat = new THREE.MeshStandardMaterial({ color:palette.body, metalness:0.48, roughness:0.28, emissive:traffic ? 0x000000 : new THREE.Color(palette.body).multiplyScalar(0.055) });
            const trimMat = new THREE.MeshStandardMaterial({ color:palette.trim, metalness:0.72, roughness:0.23 });
            const glassMat = new THREE.MeshStandardMaterial({ color:0x8de9ff, metalness:0.72, roughness:0.09, transparent:true, opacity:0.73, emissive:0x0b2c44, emissiveIntensity:0.3 });
            const wheelMat = new THREE.MeshStandardMaterial({ color:0x101216, roughness:0.78, metalness:0.08 });
            const lampMat = new THREE.MeshBasicMaterial({ color: traffic ? 0xffd676 : 0x93f6ff });
            const wheels = [];
            const box = (size, position, material, parent=group) => { const mesh=new THREE.Mesh(new THREE.BoxGeometry(...size),material); mesh.position.set(...position); mesh.castShadow=!traffic; mesh.receiveShadow=true; parent.add(mesh); return mesh; };

            if (type === 'bike') {
                box([0.72,.22,2.35],[0,.68,0],bodyMat); const nose=new THREE.Mesh(new THREE.ConeGeometry(.43,.85,6),bodyMat);nose.rotation.x=Math.PI/2;nose.position.set(0,.72,1.46);group.add(nose); box([.48,.2,.65],[0,.93,-.24],trimMat); const glow=new THREE.Mesh(new THREE.CylinderGeometry(.12,.34,.65,8),lampMat);glow.rotation.x=Math.PI/2;glow.position.set(0,.68,-1.35);group.add(glow);
            } else if (type === 'bicycle') {
                const frame = new THREE.Mesh(new THREE.TorusGeometry(.46,.055,7,12), bodyMat); frame.rotation.y=Math.PI/2; frame.position.set(0,.63,0); group.add(frame);
                [-.72,.72].forEach(z=>{ const wheel=new THREE.Mesh(new THREE.TorusGeometry(.42,.055,7,14),wheelMat);wheel.rotation.y=Math.PI/2;wheel.position.set(0,.43,z);group.add(wheel);wheels.push(wheel); });
                const fork=box([.07,.78,.07],[0,.78,.68],trimMat);fork.rotation.x=-.38; box([.07,.65,.07],[0,.84,-.38],trimMat); box([.62,.07,.07],[0,1.2,.72],trimMat); box([.42,.08,.24],[0,1.05,-.52],trimMat);
            } else if (type === 'bus') {
                box([2.32,.92,6.15],[0,.77,0],bodyMat); box([2.24,.18,6.02],[0,1.34,0],trimMat); box([2.07,.68,4.55],[0,1.37,-.15],glassMat);
                [[-1.17,-1.86],[-1.17,1.86],[1.17,-1.86],[1.17,1.86]].forEach(([x,z])=>addVehicleWheel(group,x,z,.43,wheelMat,wheels,.28));
                box([1.32,.22,.11],[0,1.37,3.1],lampMat); box([.72,.38,.05],[0,1.63,3.13],new THREE.MeshBasicMaterial({color:0xeafaff}));
                [-.76,.76].forEach(x=>box([.05,.52,1.08],[x,1.34,.6],glassMat));
            } else if (type === 'tram') {
                box([2.28,.82,7.05],[0,.78,0],bodyMat); box([2.2,.16,6.9],[0,1.32,0],trimMat); box([2.05,.64,5.56],[0,1.35,0],glassMat);
                [[-1.14,-2.42],[-1.14,2.42],[1.14,-2.42],[1.14,2.42]].forEach(([x,z])=>addVehicleWheel(group,x,z,.39,wheelMat,wheels,.25));
                box([1.44,.17,.10],[0,1.14,3.56],lampMat); const pantograph=box([.08,.46,.08],[0,2.05,0],trimMat);const arm=box([.1,.08,1.05],[0,2.25,0],trimMat);arm.rotation.x=.42;
                [-.79,.79].forEach(x=>box([.05,.48,1.22],[x,1.32,-.1],glassMat));
            } else if (type === 'van') {
                box([1.86,.62,3.75],[0,.72,0],bodyMat); box([1.73,1.15,1.66],[0,1.28,-.75],bodyMat); box([1.62,.54,.9],[0,1.38,1.08],glassMat); box([1.12,.18,.10],[0,.78,1.92],lampMat);
                [[-.94,-1.24],[-.94,1.24],[.94,-1.24],[.94,1.24]].forEach(([x,z])=>addVehicleWheel(group,x,z,.34,wheelMat,wheels));
            } else {
                box([1.72,.48,3.35],[0,.7,0],bodyMat); box([1.28,.55,1.52],[0,1.12,-.18],glassMat); box([1.62,.23,.9],[0,.97,1.06],bodyMat); box([1.58,.20,.6],[0,.98,-1.42],bodyMat); box([1.8,.18,.25],[0,.52,1.72],trimMat); box([1.8,.18,.25],[0,.52,-1.72],trimMat);
                [-.68,.68].forEach(x=>box([.05,.43,1.18],[x,1.14,-.17],glassMat));
                [[-.88,1.06],[.88,1.06],[-.88,-1.06],[.88,-1.06]].forEach(([x,z])=>addVehicleWheel(group,x,z,.32,wheelMat,wheels));
                box([1.05,.16,.08],[0,.77,1.73],lampMat);
                if(type==='sports') box([1.25,.10,.22],[0,1.32,-1.38],trimMat);
                if(type==='taxi') { box([.86,.2,.42],[0,1.46,-.12],new THREE.MeshBasicMaterial({color:0xf5fbff})); box([.52,.08,.46],[0,1.59,-.12],lampMat); }
            }
            const ring = new THREE.Mesh(new THREE.RingGeometry(Math.max(1.35, type==='bus'||type==='tram'?2.1:1.35), Math.max(1.48, type==='bus'||type==='tram'?2.24:1.48), 32), new THREE.MeshBasicMaterial({ color:traffic?0xffd66d:0x86f4ff,transparent:true,opacity:0,side:THREE.DoubleSide }));
            ring.rotation.x=-Math.PI/2; ring.position.y=.025; group.add(ring);
            const prompt=addVehicleProximityLabel(group); prompt.position.y = (type==='bus'||type==='tram') ? 3.0 : 2.55;
            group.traverse(node=>{ if(node.isMesh){node.castShadow=node.castShadow && !traffic;node.receiveShadow=true;} });
            group.userData={...palette,type,traffic,boardable:traffic && ['bus','tram','taxi'].includes(type),transit:['bus','tram'].includes(type),speed:traffic?palette.cruise*(.84+Math.random()*.18):0,steer:0,ring,active:false,axis:Math.random()>.5?'x':'z',direction:Math.random()>.5?1:-1,wheels,prompt,route:null,routeIndex:0,stopTimer:0,stopIndices:[],rolling:0};
            return group;
        }

        function spawnGarageVehicle(type, position, rotation = 0) {
            const vehicle=createVehicleModel(type);vehicle.position.copy(position);vehicle.rotation.y=rotation;scene.add(vehicle);vehicles.push(vehicle);return vehicle;
        }
        function spawnVehicle() {
            const type=document.getElementById('vehicle-type').value; currentCamera.getWorldDirection(cameraForward);cameraForward.y=0;if(cameraForward.lengthSq()<.0001)cameraForward.set(0,0,-1);const spawnPoint=playerGroup.position.clone().add(cameraForward.normalize().multiplyScalar(4));const vehicle=spawnGarageVehicle(type,spawnPoint,getScreenForwardRotation());selectedVehicle=vehicle;updateChunkStreaming(spawnPoint);setSandboxMessage(vehicle.userData.label+'を近くに出しました。Eキーまたは「乗車」で運転できます。');updateVehicleUi();
        }
        function makeTransitRoute(type,index,center) {
            const cx=nearestRoad(center.x)+(index%2?ROAD_INTERVAL:0), cz=nearestRoad(center.z)+(index%3?ROAD_INTERVAL:0); const span=type==='tram'?ROAD_INTERVAL*2:ROAD_INTERVAL*(type==='taxi'?1.6:3); const lane=type==='tram'?0:(index%2?1:-1)*ROAD_WIDTH*.24;
            return [new THREE.Vector3(cx-span,0,cz-span+lane),new THREE.Vector3(cx+span,0,cz-span+lane),new THREE.Vector3(cx+span+lane,0,cz+span),new THREE.Vector3(cx-span+lane,0,cz+span)];
        }
        function configureTrafficRoute(vehicle,index,center) {
            const data=vehicle.userData; const routeType=data.type==='bus'||data.type==='tram'||data.type==='taxi'?data.type:'car'; data.route=makeTransitRoute(routeType,index,center); data.routeIndex=index%data.route.length; data.stopIndices=data.type==='bus'||data.type==='tram'?[0,2]:[]; data.stopTimer=Math.random()*1.3; vehicle.position.copy(data.route[data.routeIndex]); const target=data.route[(data.routeIndex+1)%data.route.length]; vehicle.rotation.y=Math.atan2(target.x-vehicle.position.x,target.z-vehicle.position.z);
        }
        function createTrafficFleet() {
            const trafficTypes=['bus','tram','taxi','van','car','sports','bike','car','tram','bus','taxi','car'];
            trafficTypes.forEach((type,index)=>{const vehicle=createVehicleModel(type,true);configureTrafficRoute(vehicle,index,playerGroup?playerGroup.position:new THREE.Vector3());scene.add(vehicle);trafficVehicles.push(vehicle);});
        }
        function placeTrafficNear(vehicle,index,center) { configureTrafficRoute(vehicle,index,center); }

'''
text = replace_between(text, '        function createVehicleModel(type, traffic = false) {', '        function getControlledObject() {', new_vehicle_block)

new_control_block = r'''        function getControlledObject() { return controlledVehicle || ridingTransit || playerGroup; }
        function getNearestVehicle() {
            const candidates=[...vehicles,...trafficVehicles.filter(vehicle=>vehicle.userData.boardable)];
            return candidates.reduce((nearest,vehicle)=>{const distance=vehicle.position.distanceToSquared(playerGroup.position);return(!nearest||distance<nearest.distance)?{vehicle,distance}:nearest;},null);
        }
        function attemptTransitExit() {
            if(!ridingTransit)return false; const transit=ridingTransit; const exitOffset=new THREE.Vector3(2.15,0,0).applyQuaternion(transit.quaternion); const exitPosition=resolveCollisionMove(transit.position,transit.position.clone().add(exitOffset),PLAYER_COLLISION_RADIUS,transit); if(exitPosition.distanceToSquared(transit.position)<1){setSandboxMessage('ここでは安全に降車できません。次の停留所付近で試してください。');return true;} playerGroup.position.copy(exitPosition);playerGroup.rotation.y=transit.rotation.y;playerGroup.visible=true;ridingTransit=null;setSandboxMessage('公共交通を降りました。街の探索を続けられます。');updateVehicleUi();return true;
        }
        function toggleVehicleControl() {
            if(ridingTransit){attemptTransitExit();return;}
            if(controlledVehicle){const exitOffset=new THREE.Vector3(1.8,0,0).applyQuaternion(controlledVehicle.quaternion);const exitPosition=resolveCollisionMove(controlledVehicle.position,controlledVehicle.position.clone().add(exitOffset),PLAYER_COLLISION_RADIUS,controlledVehicle);if(exitPosition.distanceToSquared(controlledVehicle.position)<1){setSandboxMessage('ここでは安全に降車できません。少し広い場所へ移動してください。');return;}playerGroup.position.copy(exitPosition);playerGroup.rotation.y=controlledVehicle.rotation.y;playerGroup.visible=true;controlledVehicle.userData.active=false;controlledVehicle=null;vehicleSpeed=0;vehicleSteer=0;stopAutoDrive();setSandboxMessage('徒歩に戻りました。自由に探索を続けられます。');updateVehicleUi();return;}
            const nearest=getNearestVehicle();if(!nearest||nearest.distance>5.5*5.5){setSandboxMessage('近くに乗れる車両がありません。「乗り物を出す」で出現させてください。');return;}
            if(nearest.vehicle.userData.boardable){ridingTransit=nearest.vehicle;playerGroup.position.copy(ridingTransit.position);playerGroup.visible=false;stopAutoDrive();setSandboxMessage(`${ridingTransit.userData.label}に乗車しました。Eまたは「使う」で降車できます。`);updateVehicleUi();return;}
            controlledVehicle=nearest.vehicle;selectedVehicle=nearest.vehicle;controlledVehicle.userData.active=true;playerGroup.position.copy(controlledVehicle.position);playerGroup.visible=false;stopAutoDrive();setSandboxMessage(`${controlledVehicle.userData.label}に乗車しました。画面の上方向と同じ進行方向へ、なめらかに操舵します。Eで降車します。`);updateVehicleUi();
        }
        function updateVehicleProximityPrompt(vehicle, show, mode) {
            const prompt=vehicle.userData.prompt;if(!prompt)return;prompt.visible=show;if(!show)return;const key=mode==='ride'?'降車':vehicle.userData.boardable?'乗車':'運転';prompt.element.innerHTML=`<b>E</b><span>${vehicle.userData.label} ${key}</span><small>${vehicle.userData.boardable?'CITY TRANSIT':'DRIVE READY'}</small>`;
        }
        function updateVehicleUi() {
            nearestVehicle=(controlledVehicle||ridingTransit)?(controlledVehicle||ridingTransit):(getNearestVehicle()?.vehicle||null);const nearby=getNearestVehicle();const isNear=!controlledVehicle&&!ridingTransit&&nearby&&nearby.distance<5.5*5.5;
            [...vehicles,...trafficVehicles].forEach(vehicle=>{const focus=vehicle===controlledVehicle||vehicle===ridingTransit||(!controlledVehicle&&!ridingTransit&&vehicle===nearestVehicle);vehicle.userData.ring.material.opacity=focus?.78:0;vehicle.userData.ring.scale.setScalar(focus?1+Math.sin(performance.now()*.006)*.05:1);updateVehicleProximityPrompt(vehicle,(vehicle===nearestVehicle&&(isNear||controlledVehicle||ridingTransit)),(controlledVehicle||ridingTransit)?'ride':'enter');});
            if(isNear||controlledVehicle||ridingTransit)labelRenderUntil=Math.max(labelRenderUntil,performance.now()+240);
            const nextKey=controlledVehicle?`driving:${controlledVehicle.uuid}`:ridingTransit?`transit:${ridingTransit.uuid}`:isNear?`near:${nearestVehicle.uuid}`:'walking';if(nextKey===vehicleUiKey)return;vehicleUiKey=nextKey;const action=document.getElementById('vehicle-action-btn'),status=document.getElementById('vehicle-status'),hint=document.getElementById('vehicle-hint');
            if(controlledVehicle){action.disabled=false;action.innerHTML='<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-right"></use></svg>降車';status.textContent=`${controlledVehicle.userData.label}を運転中`;hint.textContent='Eで降車 · City Atlasで車両自動運転';}
            else if(ridingTransit){action.disabled=false;action.innerHTML='<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-right"></use></svg>降車';status.textContent=`${ridingTransit.userData.label}に乗車中`;hint.textContent='Eで降車 · 路線を自動走行中';}
            else if(isNear){action.disabled=false;action.innerHTML='<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-in-right"></use></svg>乗車';status.textContent=`${nearestVehicle.userData.label}が近くにあります`;hint.textContent=nearestVehicle.userData.boardable?'Eで公共交通に乗車':'Eで乗車';}
            else {action.disabled=true;action.innerHTML='<svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-arrow-in-right"></use></svg>乗車';status.textContent='徒歩で探索中';hint.textContent='近くの乗り物に E';}
        }
        function updateVehicleVisuals(vehicle, delta, speed) { const data=vehicle.userData;data.rolling=(data.rolling||0)+speed*delta/Math.max(.2,data.type==='bus'||data.type==='tram'?.43:.32);(data.wheels||[]).forEach(wheel=>wheel.rotation.x=data.rolling); }
        function updateControlledVehicle(delta) {
            if(ridingTransit){playerGroup.position.copy(ridingTransit.position);playerGroup.rotation.y=ridingTransit.rotation.y;currentSpeedMs=ridingTransit.userData.speed||0;updateChunkStreaming(ridingTransit.position);updateVehicleUi();return true;}
            if(!controlledVehicle)return false;const data=controlledVehicle.userData;
            let desired=new THREE.Vector3();let hasCommand=false;
            if(isAutoDriving){if(autoDriveTargetIndex>=path.length){stopAutoDrive();}else{const target=path[autoDriveTargetIndex];if(controlledVehicle.position.distanceToSquared(target)<2.6*2.6)autoDriveTargetIndex++;if(autoDriveTargetIndex<path.length){desired.subVectors(path[autoDriveTargetIndex],controlledVehicle.position);hasCommand=desired.lengthSq()>.01;}}}
            else {const inputX=((keys.d||keys.ArrowRight)?1:0)-((keys.a||keys.ArrowLeft)?1:0)+mobileInput.x;const inputZ=((keys.s||keys.ArrowDown)?1:0)-((keys.w||keys.ArrowUp)?1:0)+mobileInput.z;desired.copy(getCameraRelativeMove(inputX,inputZ));hasCommand=desired.lengthSq()>.002;}
            const forward=new THREE.Vector3(Math.sin(controlledVehicle.rotation.y),0,Math.cos(controlledVehicle.rotation.y));let alignment=0;
            if(hasCommand){desired.normalize();const targetAngle=Math.atan2(desired.x,desired.z);const angleDelta=THREE.MathUtils.euclideanModulo(targetAngle-controlledVehicle.rotation.y+Math.PI,Math.PI*2)-Math.PI;const steerTarget=THREE.MathUtils.clamp(angleDelta/.68,-1,1);vehicleSteer=THREE.MathUtils.damp(vehicleSteer,steerTarget,10,delta);const turning=(data.turn*(.32+.68*Math.min(1,vehicleSpeed/8)))*vehicleSteer*delta;controlledVehicle.rotation.y+=turning;forward.set(Math.sin(controlledVehicle.rotation.y),0,Math.cos(controlledVehicle.rotation.y));alignment=Math.max(-1,forward.dot(desired));if(alignment>.18)vehicleSpeed+=data.accel*Math.max(.28,alignment)*delta;else vehicleSpeed=Math.max(0,vehicleSpeed-data.brake*delta);}
            else {vehicleSteer=THREE.MathUtils.damp(vehicleSteer,0,7,delta);}
            vehicleSpeed=Math.max(0,vehicleSpeed-data.coast*vehicleSpeed*delta);vehicleSpeed=Math.min(data.max,vehicleSpeed);const desiredPosition=controlledVehicle.position.clone().addScaledVector(forward,vehicleSpeed*delta);const next=resolveCollisionMove(controlledVehicle.position,desiredPosition,VEHICLE_COLLISION_RADIUS,controlledVehicle);if(next.distanceToSquared(desiredPosition)>.001)vehicleSpeed*=.12;controlledVehicle.position.copy(next);playerGroup.position.copy(next);playerGroup.rotation.y=controlledVehicle.rotation.y;currentSpeedMs=vehicleSpeed;updateVehicleVisuals(controlledVehicle,delta,vehicleSpeed);updateChunkStreaming(next);updateVehicleUi();return true;
        }
        function updateTraffic(delta) {
            if(!trafficEnabled)return;const center=getControlledObject().position;const respawnDistanceSq=Math.pow((getActiveChunkRadius()+2)*CHUNK_SIZE,2);
            trafficVehicles.forEach((vehicle,index)=>{const data=vehicle.userData;if(vehicle.position.distanceToSquared(center)>respawnDistanceSq)configureTrafficRoute(vehicle,index,center);if(data.stopTimer>0){data.stopTimer-=delta;updateVehicleVisuals(vehicle,delta,0);return;}const route=data.route||makeTransitRoute(data.type,index,center);data.route=route;const target=route[(data.routeIndex+1)%route.length];const deltaToTarget=new THREE.Vector3().subVectors(target,vehicle.position);const distance=deltaToTarget.length();const step=data.speed*delta;if(distance<=step){vehicle.position.copy(target);data.routeIndex=(data.routeIndex+1)%route.length;if(data.stopIndices.includes(data.routeIndex))data.stopTimer=data.type==='tram'?2.4:1.8;}else{deltaToTarget.multiplyScalar(step/Math.max(distance,.001));vehicle.position.add(deltaToTarget);}const nextTarget=route[(data.routeIndex+1)%route.length];vehicle.rotation.y=Math.atan2(nextTarget.x-vehicle.position.x,nextTarget.z-vehicle.position.z);updateVehicleVisuals(vehicle,delta,data.speed);});
            if(ridingTransit){playerGroup.position.copy(ridingTransit.position);playerGroup.rotation.y=ridingTransit.rotation.y;}
        }

'''
text = replace_between(text, '        function getControlledObject() {', '        function createBuildModule(', new_control_block)

old_start_auto = '''        function startAutoDrive() {
            if (path.length > 0) {
                isAutoDriving = true;
                autoDriveTargetIndex = 1;
                document.getElementById('auto-drive-btn').style.display = 'none';
            }
        }'''
new_start_auto = '''        function startAutoDrive() {
            if (ridingTransit) { setSandboxMessage('公共交通は既定の路線を自動運行中です。目的地には降車後に設定できます。'); return; }
            if (path.length > 0) { isAutoDriving = true; autoDriveTargetIndex = 1; document.getElementById('auto-drive-btn').style.display = 'none'; const mode = controlledVehicle ? `${controlledVehicle.userData.label}での自動運転` : '徒歩自動移動'; setSandboxMessage(`${mode}を開始しました。手動入力または目的地到着で停止します。`); }
        }'''
if old_start_auto not in text:
    raise SystemExit('startAutoDrive block not found')
text = text.replace(old_start_auto, new_start_auto, 1)

old_destination_speed = '''            const isAutoRun = document.getElementById('auto-drive-run').checked;
            const speedKmh = isAutoRun ? RUN_SPEED_KMH : WALK_SPEED_KMH;
            const speedMs = (speedKmh * 1000) / 3600;'''
new_destination_speed = '''            const isAutoRun = document.getElementById('auto-drive-run').checked;
            const speedMs = controlledVehicle ? Math.max(4, controlledVehicle.userData.cruise || 12) : ((isAutoRun ? RUN_SPEED_KMH : WALK_SPEED_KMH) * 1000) / 3600;
            const speedKmh = speedMs * 3.6;'''
if old_destination_speed not in text:
    raise SystemExit('destination speed block not found')
text = text.replace(old_destination_speed, new_destination_speed, 1)

text = text.replace("if (!controlledVehicle) stopAutoDrive();", "if (!controlledVehicle && !ridingTransit) stopAutoDrive();", 1)
text = text.replace("if (isAutoDriving && !controlledVehicle) updateDestinationInfo();", "if (isAutoDriving) updateDestinationInfo();", 1)
text = text.replace("<strong id=\"vehicle-status\">徒歩で探索中</strong><span id=\"vehicle-hint\">近くの乗り物に E</span>", "<strong id=\"vehicle-status\">徒歩で探索中</strong><span id=\"vehicle-hint\">近くの乗り物・公共交通に E</span>", 1)

path.write_text(text)
print('Applied phase 5 transport refresh')
