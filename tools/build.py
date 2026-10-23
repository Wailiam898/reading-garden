"""Assemble the self-contained downloadable HTML (no build tools required at runtime)."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
text=(ROOT/'src/template.html').read_text(encoding='utf-8')
for name in ['core','audio','ui','adult']:
    text=text.replace('/*'+name.upper()+'*/',(ROOT/f'src/{name}.js').read_text(encoding='utf-8'))
assert all('/*'+n.upper()+'*/' not in text for n in ['core','audio','ui','adult'])
(ROOT/'index.html').write_text(text,encoding='utf-8')
print(f'Built index.html: {len(text.encode("utf-8"))} bytes, inline CSS and JS')
