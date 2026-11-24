"""Scan tracked repository content for suspicious non-placeholder data.
Words such as token/password are allowed in policy text; only suspicious values are flagged.
"""
from pathlib import Path
import re, sys, tempfile, subprocess
root=Path(__file__).resolve().parents[1]
tracked=subprocess.run(["git","ls-files"],cwd=root,text=True,capture_output=True,check=True).stdout.splitlines()
email=re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
phone=re.compile(r"(?<![A-Za-z0-9])\+?[0-9][0-9 ()-]{7,}[0-9](?![A-Za-z0-9])")
handle=re.compile(r"(?<![A-Za-z0-9])@[A-Za-z0-9_]{3,}(?![A-Za-z0-9])")
url=re.compile(r'''https?://[^\s)>'"]+''')
secret_value=re.compile(r"(?im)^[ \t]*(?:GITHUB_TOKEN|GOOGLE_ACCESS_TOKEN|OPENAI_API_KEY|PASSWORD|TOKEN)[ \t]*=[ \t]*(?!$|<[^>]+>|YOUR_|EXAMPLE_|__)[^\s#]+")

def scan(path):
 text=path.read_text(encoding='utf-8',errors='ignore')
 hits=[]
 for name,pat in [('email',email),('phone',phone),('handle',handle),('secret_value',secret_value)]:
  hits += [(name,m.group(0)) for m in pat.finditer(text)]
 for m in url.finditer(text):
  u=m.group(0).rstrip('.,')
  if 'example.invalid' not in u and '<' not in u and 'localhost' not in u:
   hits.append(('real_url',u))
 hits=[h for h in hits if not (h[0]=='handle' and h[1] in ('@placeholder','@example'))]
 return hits

def run_scan(base):
 out=[]
 for rel in tracked:
  p=base/rel
  if p.exists(): out.extend((rel,)+h for h in scan(p))
 return out
if __name__=='__main__':
 hits=run_scan(root)
 if hits:
  print('Suspicious patterns requiring review:')
  for h in hits: print(h)
  sys.exit(1)
 print(f'Repository scan passed: {len(tracked)} tracked files reviewed; no suspicious non-placeholder values found.')
 with tempfile.TemporaryDirectory(prefix='outreach-validator-') as td:
  t=Path(td)
  email_value='person'+'@'+'example.com'
  phone_value='+'+''.join(['2012','3456','7890'])
  handle_value='@'+'real_handle'
  url_value='https://'+'real.example.com'
  (t/'positive.txt').write_text('contact '+email_value+' '+phone_value+' '+handle_value+' '+url_value+chr(10)+'TOKEN='+'abc123',encoding='utf-8')
  assert scan(t/'positive.txt'), 'positive fixture was not detected'
  (t/'negative.txt').write_text('password=\nTOKEN=\nhttps://example.invalid/demo <LOCAL_ONLY> @placeholder\n',encoding='utf-8')
  assert not scan(t/'negative.txt'), 'negative fixture was flagged'
 print('Fixture tests passed: positive suspicious patterns detected; negative placeholders accepted.')
