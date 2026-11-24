from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
patterns=[r'\+?[0-9]{7,}',r'@[A-Za-z0-9_]{3,}',r'https?://(?!example\.invalid)',r'(?i)(gmail|outlook|api[_-]?key|token|password)']
found=[]
for p in root.rglob('*'):
    if not p.is_file() or '.git' in p.parts: continue
    text=p.read_text(encoding='utf-8',errors='ignore')
    for pat in patterns:
        if re.search(pat,text): found.append((str(p.relative_to(root)),pat))
if found:
    print('Potential sensitive content:')
    for x in found: print(x)
    sys.exit(1)
print('Repository content scan passed.')
