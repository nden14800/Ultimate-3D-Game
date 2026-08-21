from pathlib import Path

path = Path('/home/ubuntu/Ultimate-3D-Game/index.html')
text = path.read_text()

def replace_between(source, start_marker, end_marker, replacement):
    start = source.index(start_marker)
    end = source.index(end_marker, start)
    return source[:start] + replacement + source[end:]

css = r'''
        /* Phase 7: focused NPC dialogue and local model control. */
        #npc-dialog-modal { position:fixed; z-index:140; inset:0; display:grid; place-items:center; padding:clamp(16px,4vw,46px); color:#183f71; background:radial-gradient(circle at 50% 12%,rgba(89,184,255,.33),transparent 42%),rgba(5,23,49,.75); backdrop-filter:blur(14px); } #npc-dialog-modal.hidden { display:none; } .npc-dialog-shell { position:relative; display:grid; grid-template-columns:minmax(0,.72fr) minmax(340px,1.28fr); width:min(980px,100%); min-height:min(620px,calc(100dvh - 72px)); overflow:hidden; border:2px solid rgba(255,255,255,.83); border-radius:28px; background:linear-gradient(145deg,rgba(251,254,255,.98),rgba(222,242,255,.96)); box-shadow:0 24px 0 rgba(0,18,48,.22),0 38px 100px rgba(0,0,0,.38); } .npc-dialog-profile { display:flex; flex-direction:column; justify-content:space-between; gap:18px; padding:34px; color:#e9f7ff; background:linear-gradient(155deg,#0a315d,#157da5); } .npc-dialog-kicker { color:#9eeeff; font-size:10px; font-weight:900; letter-spacing:.16em; } .npc-dialog-profile h2 { margin:8px 0 8px; color:#fff; font-size:clamp(32px,5vw,55px); line-height:.92; } .npc-dialog-profile p { margin:0; color:#c7ecff; font-size:13px; line-height:1.65; } .npc-dialog-chips { display:flex; flex-wrap:wrap; gap:7px; } .npc-dialog-chips span { padding:6px 8px; border:1px solid rgba(203,244,255,.35); border-radius:999px; background:rgba(0,22,54,.22); color:#dbf6ff; font-size:9px; font-weight:900; } .npc-dialog-conversation { display:flex; min-width:0; flex-direction:column; padding:24px; } .npc-dialog-close { position:absolute; z-index:2; top:14px; right:15px; display:grid; width:36px; height:36px; place-items:center; border:1px solid #cfdfef; border-radius:11px; color:#3970a6; background:#f8fcff; font-size:22px; } .npc-dialog-heading { padding:2px 46px 15px 0; border-bottom:1px solid #d7e6f4; color:#285a8d; font-size:11px; font-weight:900; letter-spacing:.12em; } #npc-dialog-log { flex:1; min-height:275px; max-height:48dvh; margin:14px 0; overflow:auto; padding:3px 8px 3px 0; color:#31597f; font-size:14px; line-height:1.6; } .npc-dialog-line { max-width:88%; margin:9px 0; padding:10px 12px; border:1px solid #d5e8f7; border-radius:14px 14px 14px 4px; background:#fff; } .npc-dialog-line.player { margin-left:auto; border-color:#77bdf4; border-radius:14px 14px 4px 14px; color:#114f86; background:#daf0ff; } .npc-dialog-line small { display:block; margin-bottom:3px; color:#5d88af; font-size:9px; font-weight:900; letter-spacing:.08em; } #npc-dialog-form { display:flex; gap:8px; padding-top:14px; border-top:1px solid #d7e6f4; } #npc-dialog-input { flex:1; min-width:0; min-height:46px; padding:0 12px; border:1px solid #c8dfef; border-radius:13px; color:#204d79; background:#fff; font:inherit; } #npc-dialog-send { min-width:82px; border:0; border-radius:13px; color:#fff; background:linear-gradient(180deg,#55a8ff,#2579e8); font-weight:900; } .ai-model-status { margin:10px 0 0; color:#6a91b6; font-size:10px; line-height:1.5; } @media (max-width:700px) { #npc-dialog-modal { padding:10px; align-items:end; } .npc-dialog-shell { grid-template-columns:1fr; min-height:min(740px,calc(100dvh - 20px)); border-radius:24px; } .npc-dialog-profile { min-height:180px; padding:24px; } .npc-dialog-profile h2 { font-size:38px; } .npc-dialog-conversation { min-height:0; padding:18px; } #npc-dialog-log { min-height:210px; max-height:35dvh; } }
'''
if 'Phase 7: focused NPC dialogue' not in text:
    text = text.replace('        </style>', css + '\n        </style>', 1)

# Settings card and NPC modal.
needle = '''                <section class="world-settings-card"><h3><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#buildings-fill"></use></svg>CITY ACTIVITY</h3><label class="settings-toggle"><input type="checkbox" id="traffic-toggle" checked>交通車両を動かす</label><div class="button-grid" style="margin-top:15px"><button class="action-button warm" id="place-prop-btn" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#box-seam-fill"></use></svg>ブロック配置</button><button class="action-button danger" id="clear-props-btn" type="button"><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#trash3-fill"></use></svg>配置を消す</button></div></section>'''
replacement = needle + '''
                <section class="world-settings-card"><h3><svg class="bi-icon" aria-hidden="true"><use href="assets/bootstrap-icons.svg#cpu-fill"></use></svg>LOCAL AI PROFILE</h3><div class="settings-field"><label for="local-ai-model">会話モデル</label><select id="local-ai-model"><option value="Qwen2.5-0.5B-Instruct-q4f16_1-MLC">省メモリ · Qwen 0.5B</option><option value="Hermes-3-Llama-3.2-3B-q4f16_1-MLC">高品質 · Hermes 3B</option><option value="Llama-3.1-8B-Instruct-q4f16_1-MLC">最高品質 · Llama 8B</option></select></div><p id="local-ai-storage-status" class="ai-model-status">モデルは開始時にのみ読み込みます。選択状態はこの端末に保存されます。</p></section>'''
if needle not in text: raise SystemExit('settings CITY ACTIVITY card not found')
text = text.replace(needle, replacement, 1)

modal = '''
    <section id="npc-dialog-modal" class="hidden" role="dialog" aria-modal="true" aria-label="NPC会話">
        <div class="npc-dialog-shell"><button id="npc-dialog-close" class="npc-dialog-close" type="button" aria-label="会話を閉じる">×</button><aside class="npc-dialog-profile"><div><div class="npc-dialog-kicker">DIRECT CITY CONVERSATION</div><h2 id="npc-dialog-name">CITY RESIDENT</h2><p id="npc-dialog-persona">街の居住者と会話します。</p></div><div class="npc-dialog-chips"><span id="npc-dialog-id">ID</span><span id="npc-dialog-ai">TEMPLATE MODE</span><span>LOCAL ONLY</span></div></aside><div class="npc-dialog-conversation"><div class="npc-dialog-heading">PRIVATE DIALOGUE · LOCAL AI OPTIONAL</div><div id="npc-dialog-log" role="log" aria-live="polite"></div><form id="npc-dialog-form"><input id="npc-dialog-input" type="text" autocomplete="off" placeholder="この居住者に話しかける…"><button id="npc-dialog-send" type="submit">送信</button></form></div></div>
    </section>
'''
text = text.replace('    <section id="chat-ui" class="conversation-dock" aria-label="NPC会話">', modal + '\n    <section id="chat-ui" class="conversation-dock" aria-label="NPC会話">', 1)

# Variables and model catalog.
text = text.replace("let localAiEngine = null, localAiStatus = 'idle', localAiSending = false;", "let localAiEngine = null, localAiStatus = 'idle', localAiSending = false, loadedLocalAiModel = null, activeNpcDialog = null, npcDialogSending = false;", 1)
old_const = """        const LOCAL_AI_MODEL = 'Qwen2.5-0.5B-Instruct-q4f16_1-MLC';
        const LOCAL_AI_MODULE_URL = 'https://esm.run/@mlc-ai/web-llm@0.2.84';"""
new_const = """        const LOCAL_AI_MODEL = 'Qwen2.5-0.5B-Instruct-q4f16_1-MLC';
        const LOCAL_AI_MODULE_URL = 'https://esm.run/@mlc-ai/web-llm@0.2.84';
        const LOCAL_AI_STORAGE_KEY = 'ultimate3d.local-ai.selected-model.v2';
        const LOCAL_AI_CACHE_STATE_KEY = 'ultimate3d.local-ai.cache-state.v2';
        const LOCAL_AI_MODELS = {
            'Qwen2.5-0.5B-Instruct-q4f16_1-MLC': { label:'省メモリ · Qwen 0.5B', memory:'約0.8GB目安', tier:'LIGHT' },
            'Hermes-3-Llama-3.2-3B-q4f16_1-MLC': { label:'高品質 · Hermes 3B', memory:'約2.3GB目安', tier:'QUALITY' },
            'Llama-3.1-8B-Instruct-q4f16_1-MLC': { label:'最高品質 · Llama 8B', memory:'約5.0GB目安', tier:'ULTRA' }
        };
        let selectedLocalAiModel = (() => { try { const saved=localStorage.getItem(LOCAL_AI_STORAGE_KEY); return LOCAL_AI_MODELS[saved] ? saved : LOCAL_AI_MODEL; } catch { return LOCAL_AI_MODEL; } })();"""
if old_const not in text: raise SystemExit('AI constants missing')
text = text.replace(old_const, new_const, 1)

# Event listeners additions/replacement.
text = text.replace("document.getElementById('mobile-chat-button').addEventListener('click', () => { document.getElementById('chat-ui').classList.remove('collapsed'); document.getElementById('chat-input').focus(); });", "document.getElementById('mobile-chat-button').addEventListener('click', () => { const npc=getConversationNpc(); if(npc&&npc.position.distanceTo(getControlledObject().position)<9) openNpcDialog(npc); else { document.getElementById('chat-ui').classList.remove('collapsed'); document.getElementById('chat-input').focus(); } });", 1)
text = text.replace("document.getElementById('bgm-volume').addEventListener('input', (e) => setBgmVolume(Number(e.target.value) / 100));", "document.getElementById('bgm-volume').addEventListener('input', (e) => setBgmVolume(Number(e.target.value) / 100));\n            document.getElementById('local-ai-model').value = selectedLocalAiModel;\n            document.getElementById('local-ai-model').addEventListener('change', (e) => changeLocalAiModel(e.target.value));\n            document.getElementById('npc-dialog-close').addEventListener('click', closeNpcDialog);\n            document.getElementById('npc-dialog-form').addEventListener('submit', submitNpcDialog);", 1)

old_start_local = '''        async function startLocalAi() {
            if (localAiStatus === 'loading' || localAiStatus === 'ready') return;
            if (!navigator.gpu) {
                localAiStatus = 'fallback';
                setChatModeStatus('WebGPU非対応・テンプレート会話');
                updateLocalAiButton();
                addChatSystemNote('このブラウザはWebGPUを利用できないため、軽量なテンプレート会話を使用します。');
                return;
            }
            localAiStatus = 'loading';
            setChatModeStatus('LOCAL AIを準備中…');
            updateLocalAiButton();
            addChatSystemNote('LOCAL AIを準備しています。初回のみモデルの取得に時間がかかることがあります。');
            try {
                const webllm = await import(LOCAL_AI_MODULE_URL);
                localAiEngine = await webllm.CreateMLCEngine(LOCAL_AI_MODEL, {
                    initProgressCallback: (report) => {
                        const note = typeof report === 'string' ? report : report?.text || report?.progress || 'モデルを読み込み中';
                        setChatModeStatus(`LOCAL AI: ${String(note).slice(0, 42)}`);
                    }
                });
                localAiStatus = 'ready';
                npcAiHistories.clear();
                localAiQueue = [];
                lastAutonomousAiAt = performance.now() + 2400;
                setChatModeStatus('LOCAL AI: 複数NPCがこの端末で会話中');
                updateLocalAiButton();
                addChatSystemNote('LOCAL AIの準備ができました。複数のNPCが一つの端末内モデルを共有し、人格ごとの会話履歴で自律会話します。APIキーは使用しません。');
            } catch (error) {
                console.warn('LOCAL AI initialization failed', error);
                localAiEngine = null;
                localAiStatus = 'fallback';
                setChatModeStatus('LOCAL AI未接続・テンプレート会話');
                updateLocalAiButton();
                addChatSystemNote('LOCAL AIを開始できなかったため、テンプレート会話へ切り替えました。WebGPU対応や端末メモリを確認してください。');
            }
        }'''
new_start_local = '''        function selectedAiSpec() { return LOCAL_AI_MODELS[selectedLocalAiModel] || LOCAL_AI_MODELS[LOCAL_AI_MODEL]; }
        function updateLocalAiStorageUi() { const node=document.getElementById('local-ai-storage-status');if(!node)return;const spec=selectedAiSpec();let cache='初回はモデル取得、以降はブラウザキャッシュを優先します。';try{const state=JSON.parse(localStorage.getItem(LOCAL_AI_CACHE_STATE_KEY)||'{}');if(state.model===selectedLocalAiModel)cache='この端末で読込済みの記録があります。ブラウザキャッシュを優先します。';}catch{}node.textContent=`${spec.label} · ${spec.memory}。${cache}`; }
        function changeLocalAiModel(modelId) { if(!LOCAL_AI_MODELS[modelId])return;selectedLocalAiModel=modelId;try{localStorage.setItem(LOCAL_AI_STORAGE_KEY,modelId);}catch{}if(loadedLocalAiModel&&loadedLocalAiModel!==modelId){localAiEngine=null;localAiStatus='idle';setChatModeStatus('モデルを切替済み・開始ボタンで読込');}updateLocalAiButton();updateLocalAiStorageUi(); }
        async function requestLocalAiPersistence() { try { if(navigator.storage?.persist) return await navigator.storage.persist(); } catch {} return false; }
        async function startLocalAi() {
            if(localAiStatus==='loading'||(localAiStatus==='ready'&&loadedLocalAiModel===selectedLocalAiModel))return;
            const spec=selectedAiSpec();if(!navigator.gpu){localAiStatus='fallback';setChatModeStatus('WebGPU非対応・テンプレート会話');updateLocalAiButton();addChatSystemNote('このブラウザはWebGPUを利用できないため、軽量なテンプレート会話を使用します。');return;}
            localAiStatus='loading';setChatModeStatus(`${spec.tier} AIを準備中…`);updateLocalAiButton();addChatSystemNote(`${spec.label}を準備しています。初回だけモデル取得に時間がかかることがあります。`);
            try { const webllm=await import(LOCAL_AI_MODULE_URL);localAiEngine=await webllm.CreateMLCEngine(selectedLocalAiModel,{appConfig:{...webllm.prebuiltAppConfig,cacheBackend:'cache'},initProgressCallback:(report)=>{const note=typeof report==='string'?report:report?.text||report?.progress||'モデルを読み込み中';setChatModeStatus(`${spec.tier}: ${String(note).slice(0,42)}`);}});loadedLocalAiModel=selectedLocalAiModel;localAiStatus='ready';npcAiHistories.clear();localAiQueue=[];lastAutonomousAiAt=performance.now()+2400;const persistent=await requestLocalAiPersistence();try{localStorage.setItem(LOCAL_AI_STORAGE_KEY,selectedLocalAiModel);localStorage.setItem(LOCAL_AI_CACHE_STATE_KEY,JSON.stringify({model:selectedLocalAiModel,loadedAt:Date.now(),persistent}));}catch{}setChatModeStatus(`LOCAL AI: ${spec.tier}・複数NPCが会話中`);updateLocalAiButton();updateLocalAiStorageUi();addChatSystemNote(`LOCAL AIの準備ができました。${spec.label}をこの端末内で共有し、人格ごとの履歴で自律会話します。APIキーは使用しません。`); } catch(error) { console.warn('LOCAL AI initialization failed',error);localAiEngine=null;loadedLocalAiModel=null;localAiStatus='fallback';setChatModeStatus('LOCAL AI未接続・テンプレート会話');updateLocalAiButton();updateLocalAiStorageUi();addChatSystemNote('LOCAL AIを開始できなかったため、テンプレート会話へ切り替えました。端末のWebGPU対応やメモリを確認してください。'); }
        }'''
if old_start_local not in text: raise SystemExit('start local block missing')
text = text.replace(old_start_local, new_start_local, 1)

old_update_button = '''        function updateLocalAiButton() {
            const button = document.getElementById('local-ai-button');
            if (!button) return;
            button.disabled = localAiStatus === 'loading' || localAiStatus === 'ready';
            button.classList.toggle('loading', localAiStatus === 'loading');
            button.classList.toggle('ready', localAiStatus === 'ready');
            const label = button.querySelector('.ai-button-label');
            if (label) label.textContent = localAiStatus === 'ready' ? 'LOCAL AI稼働中' : localAiStatus === 'loading' ? '読込中…' : 'LOCAL AIを開始';
        }'''
new_update_button = '''        function updateLocalAiButton() {
            const button=document.getElementById('local-ai-button');if(!button)return;const isCurrent=localAiStatus==='ready'&&loadedLocalAiModel===selectedLocalAiModel;button.disabled=localAiStatus==='loading'||isCurrent;button.classList.toggle('loading',localAiStatus==='loading');button.classList.toggle('ready',isCurrent);const label=button.querySelector('.ai-button-label');if(label)label.textContent=isCurrent?'LOCAL AI稼働中':localAiStatus==='loading'?'読込中…':'LOCAL AIを開始';const modalChip=document.getElementById('npc-dialog-ai');if(modalChip)modalChip.textContent=isCurrent?`${selectedAiSpec().tier} AI READY`:'TEMPLATE MODE';
        }'''
if old_update_button not in text: raise SystemExit('button block missing')
text = text.replace(old_update_button, new_update_button, 1)

# Direct modal helpers inserted ahead of chat utilities.
modal_helpers = r'''        function renderNpcDialogHistory(npc) { const log=document.getElementById('npc-dialog-log');if(!log||!npc)return;const history=getNpcHistory(npc);log.innerHTML='';if(!history.length){const hello=document.createElement('div');hello.className='npc-dialog-line';hello.innerHTML=`<small>${npc.userData.name}</small>こんにちは。街で見つけたことや、行ってみたい場所を話してみませんか。`;log.appendChild(hello);}history.forEach(entry=>{const line=document.createElement('div');line.className='npc-dialog-line '+(entry.role==='assistant'?'':'player');line.innerHTML=`<small>${entry.role==='assistant'?npc.userData.name:'PLAYER'}</small>${entry.content}`;log.appendChild(line);});log.scrollTop=log.scrollHeight; }
        function openNpcDialog(npc) { const target=npc||getConversationNpc();if(!target)return;activeNpcDialog=target;setPaused(true);document.getElementById('pause-screen').classList.add('hidden');const modal=document.getElementById('npc-dialog-modal');modal.classList.remove('hidden');document.getElementById('npc-dialog-name').textContent=target.userData?.name||'CITY RESIDENT';document.getElementById('npc-dialog-persona').textContent=target.userData?.persona||'親しみやすい都市の居住者です。';document.getElementById('npc-dialog-id').textContent='ID '+(target.userData?.id||'CITY');updateLocalAiButton();renderNpcDialogHistory(target);duckBgm(true);setTimeout(()=>document.getElementById('npc-dialog-input').focus(),60); }
        function closeNpcDialog() { document.getElementById('npc-dialog-modal').classList.add('hidden');activeNpcDialog=null;duckBgm(false);setPaused(false);playBgm(); }
        async function submitNpcDialog(event) { event.preventDefault();const npc=activeNpcDialog,input=document.getElementById('npc-dialog-input');const message=input.value.trim();if(!npc||!message||npcDialogSending)return;npcDialogSending=true;input.value='';appendNpcHistory(npc,'user',message);addChatMessage(playerGroup,message);renderNpcDialogHistory(npc);const log=document.getElementById('npc-dialog-log');const pending=document.createElement('div');pending.className='npc-dialog-line';pending.innerHTML=`<small>${npc.userData.name}</small>考え中…`;log.appendChild(pending);log.scrollTop=log.scrollHeight;let reply='';try{if(localAiStatus==='ready'&&localAiEngine){const persona=npc.userData?.persona||'親しみやすい都市の居住者';const messages=[{role:'system',content:`あなたは創作都市Ultimate 3D CityのNPC「${npc.userData?.name||'居住者'}」です。人物像は「${persona}」。日本語で親しみやすく、最大2文・100文字以内で会話してください。個人情報、外部サービス、現実世界の権限は持たない設定です。`},...getNpcHistory(npc),{role:'user',content:'プレイヤーへ返答してください。'}];const result=await localAiEngine.chat.completions.create({messages,temperature:.72,max_tokens:120});reply=result.choices?.[0]?.message?.content?.trim()||getFallbackReply(message);}else reply=getFallbackReply(message);appendNpcHistory(npc,'assistant',reply);addChatMessage(npc,reply);pending.remove();renderNpcDialogHistory(npc);}catch(error){console.warn('NPC dialog reply failed',error);reply=getFallbackReply(message);appendNpcHistory(npc,'assistant',reply);pending.remove();renderNpcDialogHistory(npc);}finally{npcDialogSending=false;input.focus();} }

'''
text = text.replace('        function addChatMessage(characterObject, message, options = {}) {', modal_helpers + '        function addChatMessage(characterObject, message, options = {}) {', 1)

old_primary = '''        function handlePrimaryInteract() {
            if (tryEnterOrExitInterior?.()) return;
            toggleVehicleControl();
        }'''
new_primary = '''        function handlePrimaryInteract() {
            if(tryEnterOrExitInterior?.())return;
            if(!controlledVehicle&&!ridingTransit){const npc=getConversationNpc();if(npc&&npc.position.distanceToSquared(playerGroup.position)<5.5*5.5){openNpcDialog(npc);return;}}
            toggleVehicleControl();
        }'''
if old_primary not in text: raise SystemExit('primary interaction missing')
text = text.replace(old_primary, new_primary, 1)
text = text.replace("            updateZoomReadout();\n            renderer.setAnimationLoop(animate);", "            updateLocalAiStorageUi();\n            updateZoomReadout();\n            renderer.setAnimationLoop(animate);", 1)

path.write_text(text)
print('Applied phase 7 NPC and local AI refresh')
