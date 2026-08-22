from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()

def replace_once(old, new, label):
    global text
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f'{label}: expected 1 occurrence, found {count}')
    text = text.replace(old, new, 1)

replace_once(
"        let isRunning = false;\n",
"        let isRunning = false;\n        let touchRunActive = false;\n",
"run state",
)

replace_once(
"            document.addEventListener('keyup', (e) => { keys[normalizedKey(e.key)] = false; });\n            window.addEventListener('blur', clearMovementInput);\n",
"            document.addEventListener('keyup', (e) => {\n                const key = normalizedKey(e.key);\n                keys[key] = false;\n                if (key === 'Shift') isRunning = false;\n            });\n            document.addEventListener('pointerup', () => { touchRunActive = false; isRunning = false; }, { passive: true });\n            document.addEventListener('pointercancel', () => { touchRunActive = false; isRunning = false; }, { passive: true });\n            window.addEventListener('blur', clearMovementInput);\n",
"run key release",
)

replace_once(
"                mobileInput.z = 0;\n                isRunning = false;\n",
"                mobileInput.z = 0;\n                touchRunActive = false;\n                isRunning = false;\n",
"clear run state",
)

replace_once(
"            runButton.addEventListener('touchstart', (e) => { e.preventDefault(); isRunning = true; }, { passive: false });\n            runButton.addEventListener('touchend', (e) => { e.preventDefault(); isRunning = false; }, { passive: false });\n            runButton.addEventListener('touchcancel', () => { isRunning = false; });\n",
"            const releaseRun = () => { touchRunActive = false; isRunning = false; };\n            runButton.addEventListener('pointerdown', (e) => { e.preventDefault(); touchRunActive = true; isRunning = true; runButton.setPointerCapture?.(e.pointerId); });\n            runButton.addEventListener('pointerup', releaseRun);\n            runButton.addEventListener('pointercancel', releaseRun);\n            runButton.addEventListener('lostpointercapture', releaseRun);\n",
"mobile run hold",
)

replace_once(
"                isRunning = keys['Shift'] || isRunning;\n",
"                // キーボードはShiftを押しているフレームだけ、タッチは走るボタンを保持している間だけ加速する。\n                isRunning = Boolean(keys['Shift'] || touchRunActive);\n",
"per-frame run reset",
)

replace_once(
"        function updateInteractionPrompts() { const prompt=ensureBuildingEntryPrompt();if(interiorState||controlledVehicle||ridingTransit){prompt.visible=false;return;}const nearest=getNearestBuildingEntry(playerGroup.position);const hub=getNearestCityHub(playerGroup.position);const target=hub&&(!nearest||hub.distanceSq<nearest.distanceSq)?{position:hub.hub.entrance,label:'CITY HUB',distanceSq:hub.distanceSq}:{position:nearest?.entry.position,label:nearest?.entry.label,distanceSq:nearest?.distanceSq};if(target?.position&&target.distanceSq<7.4*7.4){prompt.position.copy(target.position).add(new THREE.Vector3(0,2.45,0));prompt.visible=true;prompt.element.innerHTML=`<b>E / 使う</b><span>${target.label} に入る</span><small>BUILDING ENTRY</small>`;labelRenderUntil=Math.max(labelRenderUntil,performance.now()+240);}else prompt.visible=false; }\n",
"        function getVehicleInteractionCandidate(position = playerGroup.position) {\n            const nearby = getNearestVehicle();\n            if (!nearby || nearby.distance > 5.5 * 5.5) return null;\n            const toVehicle = nearby.vehicle.position.clone().sub(position); toVehicle.y = 0;\n            const cameraDirection = new THREE.Vector3(); currentCamera.getWorldDirection(cameraDirection); cameraDirection.y = 0;\n            const facing = toVehicle.lengthSq() > .001 && cameraDirection.lengthSq() > .001 ? cameraDirection.normalize().dot(toVehicle.normalize()) : 0;\n            return { ...nearby, facing };\n        }\n        function shouldPrioritizeVehicleInteraction(position = playerGroup.position) {\n            const candidate = getVehicleInteractionCandidate(position);\n            // 車は至近距離、または画面正面寄りにあるとき、建物入口より先に扱う。\n            return Boolean(candidate && (candidate.distance < 3.55 * 3.55 || candidate.facing > -0.12));\n        }\n        function updateInteractionPrompts() {\n            const prompt = ensureBuildingEntryPrompt();\n            if (interiorState || controlledVehicle || ridingTransit || shouldPrioritizeVehicleInteraction()) { prompt.visible = false; return; }\n            const nearest = getNearestBuildingEntry(playerGroup.position);\n            const hub = getNearestCityHub(playerGroup.position);\n            const target = hub && (!nearest || hub.distanceSq < nearest.distanceSq) ? { position:hub.hub.entrance,label:'CITY HUB',distanceSq:hub.distanceSq } : { position:nearest?.entry.position,label:nearest?.entry.label,distanceSq:nearest?.distanceSq };\n            if (target?.position && target.distanceSq < 7.4 * 7.4) {\n                prompt.position.copy(target.position).add(new THREE.Vector3(0,2.45,0)); prompt.visible=true;\n                prompt.element.innerHTML=`<b>E / 使う</b><span>${target.label} に入る</span><small>BUILDING ENTRY</small>`;\n                labelRenderUntil=Math.max(labelRenderUntil,performance.now()+240);\n            } else prompt.visible=false;\n        }\n",
"interaction priority prompt",
)

replace_once(
"if(controlledVehicle||ridingTransit){setSandboxMessage('建物へ入る前に乗り物を降りてください。');return true;}const hub=getNearestCityHub(playerGroup.position);",
"if(controlledVehicle||ridingTransit){setSandboxMessage('建物へ入る前に乗り物を降りてください。');return true;}if(shouldPrioritizeVehicleInteraction()){return false;}const hub=getNearestCityHub(playerGroup.position);",
"building guard",
)

replace_once(
"        function handlePrimaryInteract() {\n            if(tryEnterOrExitInterior?.())return;\n            if(!controlledVehicle&&!ridingTransit){const npc=getConversationNpc();if(npc&&npc.position.distanceToSquared(playerGroup.position)<5.5*5.5){openNpcDialog(npc);return;}}\n            toggleVehicleControl();\n        }\n",
"        function handlePrimaryInteract() {\n            // 室内の出口は常に最優先。街では、近くの車両を入口より先に選択する。\n            if (interiorState && tryEnterOrExitInterior?.()) return;\n            if (controlledVehicle || ridingTransit || shouldPrioritizeVehicleInteraction()) { toggleVehicleControl(); return; }\n            const npc = getConversationNpc();\n            if (npc && npc.position.distanceToSquared(playerGroup.position) < 5.5 * 5.5) { openNpcDialog(npc); return; }\n            if (tryEnterOrExitInterior?.()) return;\n            toggleVehicleControl();\n        }\n",
"primary interaction priority",
)

css = r'''

        /* Phase 12: stable input, explicit interaction priority, and mobile-first overlays. */
        html, body { width:100%; height:100%; min-height:100%; overflow:hidden; overscroll-behavior:none; background:#071323; }
        body { position:fixed; inset:0; touch-action:manipulation; }
        input, textarea, select, #chat-log, .scroll-surface, .ui-container, #field-pack, .atlas-toolbar { overscroll-behavior:contain; }
        #chat-ui.conversation-dock { left:18px; bottom:112px; z-index:44; }
        #pause-screen { position:fixed; inset:0; z-index:150; width:100vw; height:100dvh; background:linear-gradient(130deg,rgba(3,12,28,.98),rgba(10,56,101,.92)); backdrop-filter:blur(18px); }
        #pause-screen .pause-hub { min-height:100dvh; box-sizing:border-box; }
        #city-atlas-screen { position:fixed; inset:0; z-index:170; width:100vw; height:100dvh; overflow:hidden; background:linear-gradient(140deg,#061a35,#0b3b68); }
        #city-atlas-screen .atlas-shell { display:grid; grid-template-columns:1fr; grid-template-rows:minmax(0,1fr); width:min(1440px,100%); height:100%; min-height:0; max-width:none; margin:0 auto; padding:72px 26px 24px; box-sizing:border-box; gap:0; }
        #city-atlas-screen .atlas-intro { display:none; }
        #city-atlas-screen .atlas-workbench { display:grid; grid-template-rows:auto minmax(0,1fr) auto; min-height:0; height:100%; gap:11px; }
        #city-atlas-screen .atlas-toolbar { flex-wrap:nowrap; overflow-x:auto; overflow-y:hidden; padding:2px 1px 7px; scrollbar-width:thin; }
        #city-atlas-screen .atlas-tool, #city-atlas-screen .atlas-chip { flex:0 0 auto; }
        #city-atlas-screen .atlas-map-frame { min-height:0; height:100%; border-radius:20px; }
        #city-atlas-screen #city-atlas-canvas { width:100%; height:100%; min-height:0; }
        #city-atlas-screen .atlas-footer { justify-content:space-between; min-height:48px; }
        @media (pointer:coarse),(max-width:760px) {
            #chat-ui.conversation-dock { left:calc(9px + env(safe-area-inset-left)); bottom:calc(88px + env(safe-area-inset-bottom)); width:min(360px,calc(100vw - 150px)); max-height:min(250px,calc(100dvh - 164px)); }
            #chat-ui.conversation-dock.collapsed { bottom:calc(80px + env(safe-area-inset-bottom)); }
            #city-atlas-screen .atlas-shell { padding:60px 10px 10px; }
            #city-atlas-screen .atlas-workbench { gap:8px; }
            #city-atlas-screen .atlas-toolbar { gap:6px; min-height:43px; }
            #city-atlas-screen .atlas-map-frame { border-width:2px; border-radius:16px; }
            #city-atlas-screen .atlas-footer { display:grid; grid-template-columns:1fr auto; gap:7px; }
            #city-atlas-screen #atlas-destination-readout { grid-column:1/-1; width:auto; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
            #city-atlas-screen #atlas-back { display:none; }
            #pause-screen .pause-hub { min-height:100dvh; padding-top:calc(70px + env(safe-area-inset-top)); }
        }
'''
replace_once("\n        </style>\n", css + "\n        </style>\n", "phase12 css")

path.write_text(text)
print('Phase 12 input and UI fixes applied.')
