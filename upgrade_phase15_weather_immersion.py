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


replace_once(
    "        let weatherParticles, cloudLayer = null, directionalLight, ambientLight, hemisphereLight, sandboxGround;\n",
    "        let weatherParticles, cloudLayer = null, directionalLight, ambientLight, hemisphereLight, sandboxGround;\n        let activeWeather = 'sunny';\n",
    'active weather state'
)

cloud_update = r'''        function updateCloudLayer(time, focus) {
            if (!cloudLayer) return;
            cloudLayer.position.set(Math.floor(focus.x / 96) * 96, 0, Math.floor(focus.z / 96) * 96);
            const weather = activeWeather || document.getElementById('weather-select')?.value || 'sunny';
            const profile = { sunny:{ opacity:.30, drift:.008 }, cloudy:{ opacity:.68, drift:.016 }, rainy:{ opacity:.84, drift:.043 }, snowy:{ opacity:.78, drift:.034 } }[weather];
            cloudLayer.visible = qualityMode !== 'performance' || weather !== 'sunny';
            cloudLayer.children.forEach((cloud, index) => {
                const phase = cloud.userData.phase || index;
                cloud.position.x += Math.sin(time * .000018 + phase) * profile.drift;
                cloud.position.z += Math.cos(time * .000014 + phase) * profile.drift * .62;
                cloud.traverse(node => {
                    if (!node.isMesh || !node.material) return;
                    node.material.transparent = true;
                    node.material.opacity = profile.opacity * (qualityMode === 'visual' ? 1 : .78);
                    node.material.needsUpdate = true;
                });
            });
        }

'''
replace_between('        function updateCloudLayer(time, focus) {', '        function setupEventListeners() {', cloud_update, 'cloud weather update')

weather_function = r'''        function applyWeatherSurfaceProfile(weather) {
            if (!chunkAssets) return;
            const profiles = {
                sunny: { turf:0x5e8b6d, road:0x202c35, groundRoughness:.86, roadRoughness:.49, roadMetalness:.24, fog:0xbde9ff, near:58 },
                cloudy: { turf:0x557c68, road:0x26343f, groundRoughness:.82, roadRoughness:.42, roadMetalness:.32, fog:0xaebdca, near:48 },
                rainy: { turf:0x355d55, road:0x162733, groundRoughness:.48, roadRoughness:.17, roadMetalness:.64, fog:0x829bb2, near:31 },
                snowy: { turf:0xb8cbd2, road:0x72808b, groundRoughness:.72, roadRoughness:.52, roadMetalness:.20, fog:0xdcecf6, near:38 }
            };
            const profile = profiles[weather] || profiles.sunny;
            chunkAssets.groundMaterial.color.setHex(profile.turf); chunkAssets.groundMaterial.roughness = profile.groundRoughness;
            chunkAssets.roadMaterial.color.setHex(profile.road); chunkAssets.roadMaterial.roughness = profile.roadRoughness; chunkAssets.roadMaterial.metalness = profile.roadMetalness;
            chunkAssets.groundMaterial.needsUpdate = true; chunkAssets.roadMaterial.needsUpdate = true;
            if (scene.fog) { scene.fog.color.setHex(profile.fog); scene.fog.near = profile.near; }
        }

        function changeWeather(weather) {
            activeWeather = weather;
            if (weatherParticles) { scene.remove(weatherParticles); weatherParticles.geometry.dispose(); weatherParticles.material.dispose(); weatherParticles = null; }
            updateTime(parseFloat(document.getElementById('time-slider').value));
            const profiles = {
                sunny:{ turbidity:7.5, rayleigh:1.85, mie:.005, light:1, ambient:1, hemi:1, cloud:false },
                cloudy:{ turbidity:13.5, rayleigh:.86, mie:.010, light:.74, ambient:.92, hemi:.91, cloud:true },
                rainy:{ turbidity:18.5, rayleigh:.36, mie:.018, light:.58, ambient:.78, hemi:.78, cloud:true },
                snowy:{ turbidity:15.5, rayleigh:.72, mie:.014, light:.76, ambient:1.10, hemi:1.06, cloud:true }
            };
            const profile = profiles[weather] || profiles.sunny;
            const uniforms = sky.material.uniforms;
            uniforms['turbidity'].value = profile.turbidity; uniforms['rayleigh'].value = profile.rayleigh; uniforms['mieCoefficient'].value = profile.mie;
            const hour = parseFloat(document.getElementById('time-slider').value); const isNight = hour >= 17 || hour < 6;
            if (!isNight) { directionalLight.intensity *= profile.light; ambientLight.intensity *= profile.ambient; hemisphereLight.intensity *= profile.hemi; }
            applyWeatherSurfaceProfile(weather);
            if (weather === 'rainy' || weather === 'snowy') {
                const count = weather === 'rainy' ? qualityConfig().weatherCount : Math.floor(qualityConfig().weatherCount * .68);
                const positions = new Float32Array(count * 3), velocities = new Float32Array(count * 3), geometry = new THREE.BufferGeometry();
                const lateral = weather === 'rainy' ? .24 : .075;
                for (let i = 0; i < count * 3; i += 3) {
                    positions[i] = (Math.random() - .5) * 112; positions[i + 1] = Math.random() * 52; positions[i + 2] = (Math.random() - .5) * 112;
                    velocities[i] = (Math.random() - .5) * lateral; velocities[i + 1] = weather === 'rainy' ? -(.82 + Math.random() * .62) : -(.045 + Math.random() * .055); velocities[i + 2] = weather === 'rainy' ? .14 : (Math.random() - .5) * .035;
                }
                geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3)); geometry.setAttribute('velocity', new THREE.BufferAttribute(velocities, 3));
                const material = new THREE.PointsMaterial({ color:weather === 'rainy' ? 0xb8d7ef : 0xffffff, size:weather === 'rainy' ? .075 : .17, transparent:true, opacity:weather === 'rainy' ? .74 : .86, depthWrite:false, sizeAttenuation:true });
                weatherParticles = new THREE.Points(geometry, material); weatherParticles.name = `weather-${weather}-particles`; weatherParticles.renderOrder = 2; scene.add(weatherParticles);
            }
            if (cloudLayer) cloudLayer.visible = profile.cloud || qualityMode === 'visual';
            syncWeatherAudio(weather); updateCityPhoneUi();
        }
'''
replace_between('        function changeWeather(weather) {', '        function drawMapBackground() {', weather_function + '\n\n        ', 'weather function')

replace_once(
    "                if (wanted[kind] && gameStarted && !gamePaused && !cityPhoneOpen) audio.play().catch(() => {});\n",
    "                if (wanted[kind] && gameStarted && !gamePaused) audio.play().catch(() => {});\n",
    'weather sound when phone open'
)

path.write_text(text)
print('Phase 15 weather immersion applied.')
