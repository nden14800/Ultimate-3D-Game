import { readFileSync } from 'node:fs';

const file = process.argv[2];
if (!file) throw new Error('GLB path is required');
const data = readFileSync(file);
if (data.toString('utf8', 0, 4) !== 'glTF') throw new Error('Not a GLB file');
const jsonLength = data.readUInt32LE(12);
const jsonType = data.readUInt32LE(16);
if (jsonType !== 0x4E4F534A) throw new Error('GLB has no JSON chunk');
const json = JSON.parse(data.toString('utf8', 20, 20 + jsonLength));
console.log(JSON.stringify({
  asset: json.asset,
  scenes: json.scenes?.length || 0,
  nodes: json.nodes?.length || 0,
  meshes: json.meshes?.length || 0,
  skins: json.skins?.length || 0,
  animations: (json.animations || []).map((clip, index) => ({ index, name: clip.name || `clip-${index}`, channels: clip.channels?.length || 0 })),
  images: (json.images || []).length,
}, null, 2));
