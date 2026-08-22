from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()

required_assets = [
    root / 'assets/models/cc0-characters/animated-platformer-character.glb',
    root / 'assets/models/cc0-weather/cloud-cluster.glb',
    root / 'assets/models/cc0-props/smartphone.glb',
    root / 'assets/models/kenney/nature/tree-detailed.glb',
    root / 'assets/models/kenney/nature/tree-oak.glb',
    root / 'assets/models/kenney/nature/tree-pine.glb',
    root / 'assets/models/kenney/nature/bush-detailed.glb',
    root / 'assets/models/kenney/nature/rock-large.glb',
    root / 'assets/models/kenney/roads/streetlight.glb',
    root / 'assets/models/kenney/roads/street-sign.glb',
    root / 'assets/models/kenney/roads/road-barrier.glb',
    root / 'assets/audio/weather/rain-gutter-loop.mp3',
    root / 'assets/audio/weather/strong-wind-blowing.mp3',
    root / 'assets/audio/sfx/ui-tap.ogg',
    root / 'assets/audio/sfx/ui-confirm.ogg',
    root / 'assets/audio/sfx/ui-back.ogg',
    root / 'assets/audio/sfx/ui-error.ogg',
    root / 'assets/audio/sfx/footstep-concrete.ogg',
    root / 'assets/audio/sfx/footstep-grass.ogg',
    root / 'assets/audio/sfx/footstep-snow.ogg',
    root / 'assets/THIRD_PARTY_ASSETS_PHASE13.md',
]

checks = {
    'phase14_assets_present': all(asset.exists() and asset.stat().st_size > 0 for asset in required_assets),
    'character_sources': "character: 'assets/models/cc0-characters/animated-platformer-character.glb'" in html,
    'character_animation': all(token in html for token in ('function installCharacterAnimation', "['Idle', 'Walk', 'Run']", 'function updateCharacterMotion')),
    'external_scenery': all(token in html for token in ('function decorateChunkWithExternalScenery', "addProp('streetlight'", "addProp('streetSign'", "addProp('roadBarrier'")),
    'external_clouds': all(token in html for token in ('function createExternalCloudClusters', "cloudCluster: 'assets/models/cc0-weather/cloud-cluster.glb'")),
    'weather_audio': all(token in html for token in ('function syncWeatherAudio', 'rain-gutter-loop.mp3', 'strong-wind-blowing.mp3')),
    'sfx_and_steps': all(token in html for token in ('function playSfx', 'function updateFootsteps', 'footstep-concrete.ogg', 'footstep-grass.ogg', 'footstep-snow.ogg')),
    'phone_ui': all(token in html for token in ('id="city-phone"', 'CityLink S26', 'function toggleCityPhone', "key === 'f'", 'mobile-phone-button')),
    'non_affiliation_copy': 'ブランド非提携・独自設計のゲーム内端末' in html,
    'wind_credit': 'Strong Wind Blowing — Flixberry Entertainment (CC BY 3.0/4.0)' in html,
    'weather_profiles': all(token in html for token in ('function applyWeatherSurfaceProfile', 'let activeWeather', 'function changeWeather(weather)')),
}

module_match = re.search(r'<script type="module">\s*(.*?)\s*</script>', html, re.S)
if module_match:
    module_path = root / '.phase14_module_check.js'
    module_path.write_text(module_match.group(1))
    result = subprocess.run(['node', '--check', str(module_path)], capture_output=True, text=True)
    module_path.unlink(missing_ok=True)
    checks['javascript_syntax'] = result.returncode == 0
else:
    checks['javascript_syntax'] = False

for name, passed in checks.items():
    print(f'{name}={"PASS" if passed else "FAIL"}')

if not all(checks.values()):
    sys.exit(1)
print('PHASE14_INTEGRATION_VALIDATION=PASS')
