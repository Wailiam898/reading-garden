from pathlib import Path
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parents[1]
for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png'), (180, 'apple-touch-icon.png')]:
    image = Image.new('RGB', (size, size), '#f6e9ce')
    d = ImageDraw.Draw(image)
    def box(coords): return tuple(round(n*size) for n in coords)
    d.ellipse(box((.20,.62,.80,.94)), fill='#bdd6ae')
    d.ellipse(box((.29,.18,.44,.62)), fill='#fffdf6')
    d.ellipse(box((.55,.18,.70,.62)), fill='#fffdf6')
    d.ellipse(box((.33,.25,.40,.52)), fill='#e9b2b6')
    d.ellipse(box((.59,.25,.66,.52)), fill='#e9b2b6')
    d.ellipse(box((.22,.40,.78,.85)), fill='#fffdf6')
    d.ellipse(box((.36,.56,.40,.61)), fill='#344b45')
    d.ellipse(box((.60,.56,.64,.61)), fill='#344b45')
    d.ellipse(box((.30,.64,.41,.70)), fill='#edc3bd')
    d.ellipse(box((.59,.64,.70,.70)), fill='#edc3bd')
    d.polygon([(.46*size,.66*size),(.54*size,.66*size),(.5*size,.71*size)], fill='#d79399')
    target = ROOT/'icons'/name
    target.parent.mkdir(exist_ok=True)
    image.save(target)
    print(target.name, image.size)
