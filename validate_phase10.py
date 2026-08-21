from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()

checks = {
    'city_worlds_title': 'CITY WORLDS' in html and 'SELECT A' in html,
    'join_setup': 'id="join-setup"' in html and 'id="join-world-button"' in html,
    'world_cards': all(f'data-world-id="{world}"' in html for world in ('harbor', 'neon', 'green')),
    'camera_pointer_capture': 'activeLookPointerId = event.pointerId' in html and 'setPointerCapture?.(event.pointerId)' in html,
    'free_cam_custom_look': 'function applyFreeCamLook()' in html and "orbitControls.enabled = false;" in html,
    'mobile_interact_parity': "mobile-interact-button').addEventListener('click', handlePrimaryInteract)" in html and "key === 'e') handlePrimaryInteract()" in html,
    'use_prompt_copy': 'E / 使う' in html,
    'atlas_refresh': 'function drawCityAtlas()' in html and 'CITY RADAR · TAP' in html and "ctx.fillText('N'" in html,
    'hud_declutter': '#mobile-action-rail { display:none !important; }' in html and 'Hide gameplay HUD while a title or pre-join layer is active.' in html,
    'premium_materials': 'urban-facade-atlas.png' in html and 'toneMappingExposure = qualityMode' in html,
    'no_legacy_title_start': 'start-game-button' not in html,
}

module = root / '.phase10_module_check.js'
module.write_text(re.search(r'<script type="module">\s*(.*?)\s*</script>', html, re.S).group(1))
node = subprocess.run(['node', '--check', str(module)], text=True, capture_output=True)
module.unlink(missing_ok=True)
checks['javascript_syntax'] = node.returncode == 0

for name, passed in checks.items():
    print(f'{name}={"PASS" if passed else "FAIL"}')

if not all(checks.values()):
    sys.exit(1)

print('PHASE10_VALIDATION=PASS')
