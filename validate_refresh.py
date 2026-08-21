from pathlib import Path
import re
import subprocess
import sys
import urllib.request

root = Path('/home/ubuntu/Ultimate-3D-Game')
html_path = root / 'index.html'
svg_path = root / 'assets' / 'bootstrap-icons.svg'
html = html_path.read_text(encoding='utf-8')
svg = svg_path.read_text(encoding='utf-8')

html_ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', html))
js_ids = set(re.findall(r"document\.getElementById\(['\"]([^'\"]+)['\"]\)", html))
missing_ids = sorted(js_ids - html_ids)

svg_ids = set(re.findall(r'<symbol\b[^>]*\bid="([^"]+)"', svg))
icon_ids = set(re.findall(r'assets/bootstrap-icons\.svg#([^"\']+)', html))
missing_icons = sorted(icon_ids - svg_ids)

module_match = re.search(r"const LOCAL_AI_MODULE_URL = '([^']+)'", html)
module_url = module_match.group(1) if module_match else None
model_match = re.search(r"const LOCAL_AI_MODEL = '([^']+)'", html)
model_id = model_match.group(1) if model_match else None

module_js = Path('/tmp/ultimate3d-module.js')
script_match = re.search(r'<script type="module">\s*(.*?)\s*</script>', html, re.S)
if not script_match:
    raise SystemExit('module script not found')
module_js.write_text(script_match.group(1), encoding='utf-8')
node_result = subprocess.run(['node', '--check', str(module_js)], text=True, capture_output=True)

http_status = None
if module_url:
    try:
        request = urllib.request.Request(module_url, method='HEAD', headers={'User-Agent': 'Ultimate3DGameValidation/1.0'})
        with urllib.request.urlopen(request, timeout=15) as response:
            http_status = response.status
    except Exception as exc:
        http_status = f'error: {type(exc).__name__}'

print('HTML_ID_COUNT=', len(html_ids))
print('JS_ID_REFERENCE_COUNT=', len(js_ids))
print('MISSING_DOM_IDS=', missing_ids)
print('USED_ICON_COUNT=', len(icon_ids))
print('MISSING_SVG_ICON_IDS=', missing_icons)
print('LOCAL_AI_MODEL=', model_id)
print('LOCAL_AI_MODULE_HTTP=', http_status)
print('NODE_CHECK_CODE=', node_result.returncode)
if node_result.stderr:
    print(node_result.stderr)

failed = bool(missing_ids or missing_icons or node_result.returncode != 0 or http_status != 200)
if failed:
    sys.exit(1)
