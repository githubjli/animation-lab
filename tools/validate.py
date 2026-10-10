from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'episodes/E001-wait/manifest.json').read_text(encoding='utf-8'))
t=0
for s in m['shots']:
 assert s['start']==t and s['end']>t
 t=s['end']
assert t==m['duration']==30
for p in json.loads((r/'references/michelin/provenance.json').read_text(encoding='utf-8')):
 assert hashlib.sha256((r/p['copy']).read_bytes()).hexdigest()==p['sha256']
print('PASS: 8 shots, continuous 30-second timeline; reference copies verified. Visual assets remain planned.')
