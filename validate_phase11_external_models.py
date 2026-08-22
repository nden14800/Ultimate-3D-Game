from pathlib import Path
import re
import subprocess
import sys

root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
model_root = root / 'assets' / 'models' / 'kenney'
required_assets = [
    model_root / 'car' / 'hatchback-sports.glb',
    model_root / 'car' / 'delivery.glb',
    model_root / 'car' / 'taxi.glb',
    model_root / 'car' / 'Textures' / 'colormap.png',
    model_root / 'city' / 'building-type-a.glb',
    model_root / 'city' / 'building-type-f.glb',
    model_root / 'city' / 'Textures' / 'colormap.png',
    model_root / 'LICENSE-AND-SOURCES.md',
]
checks = {
    'gltf_loader_import': "GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'" in html,
    'model_loader_start': 'loadExternalModelLibrary();' in html,
    'car_model_sources': all(path in html for path in (
        'assets/models/kenney/car/hatchback-sports.glb',
        'assets/models/kenney/car/delivery.glb',
        'assets/models/kenney/car/taxi.glb',
    )),
    'city_model_sources': all(path in html for path in (
        'assets/models/kenney/city/building-type-a.glb',
        'assets/models/kenney/city/building-type-f.glb',
    )),
    'vehicle_visual_attachment': 'function attachExternalVehicleModel(vehicle)' in html and 'if (externalModelsReady) attachExternalVehicleModel(group);' in html,
    'chunk_visual_attachment': 'function decorateChunkWithExternalBuilding(chunk)' in html and 'if(externalModelsReady)decorateChunkWithExternalBuilding(chunkRecord);' in html,
    'asset_license_record': all(path.exists() for path in required_assets),
}
module_match = re.search(r'<script type="module">\s*(.*?)\s*</script>', html, re.S)
if not module_match:
    checks['javascript_syntax'] = False
else:
    module = root / '.phase11_module_check.js'
    module.write_text(module_match.group(1))
    node = subprocess.run(['node', '--check', str(module)], text=True, capture_output=True)
    module.unlink(missing_ok=True)
    checks['javascript_syntax'] = node.returncode == 0
for name, passed in checks.items():
    print(f'{name}={"PASS" if passed else "FAIL"}')
if not all(checks.values()):
    sys.exit(1)
print('PHASE11_EXTERNAL_MODELS_VALIDATION=PASS')
