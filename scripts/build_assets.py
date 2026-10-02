#!/usr/bin/env python3
"""Build the orbital identity. Pixel artwork uses a fixed grid; type stays readable."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin
import math
import random

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
BG = '#100f1d'
INK = '#f2edff'
MUTED = '#bfb1d6'
LINE = '#342849'
VIOLET = '#aa80ee'
LILAC = '#d9bcff'
MINT = '#9ccec9'
TAU = math.tau


def font(size, bold=False, pixel=False):
    name = 'Silkscreen.ttf' if pixel else 'SpaceGrotesk.ttf'
    f = ImageFont.truetype(str(ROOT / 'design/fonts' / name), size)
    if not pixel:
        f.set_variation_by_axes([650 if bold else 450])
    return f


def text(draw, xy, value, size, fill=INK, bold=False, pixel=False):
    draw.text(xy, value, font=font(size, bold, pixel), fill=fill, anchor='lt')


def save_png(im, name, origin):
    info = PngImagePlugin.PngInfo()
    info.add_text('Description', origin)
    info.add_text('impeccable:prompt', origin)
    im.save(OUT / name, optimize=True, pnginfo=info)


def sprite():
    # GIF has binary alpha. Quantize alpha and color on the logical pixel grid.
    source = Image.open(ROOT / 'design/source/planet.png').convert('RGBA')
    small = source.resize((96, 64), Image.Resampling.NEAREST)
    alpha = small.getchannel('A').point(lambda a: 255 if a >= 210 else 0)
    colors = small.convert('RGB').quantize(colors=12, method=Image.Quantize.MEDIANCUT,
                                          dither=Image.Dither.NONE).convert('RGBA')
    colors.putalpha(alpha)
    return colors


PLANET = sprite()


def stars(draw, width, height, seed, mobile=False):
    rng = random.Random(seed)
    for i in range(43 if not mobile else 31):
        x = rng.randrange(5, width // 4 - 5) * 4
        y = rng.randrange(5, height // 4 - 5) * 4
        # Leave the lettering field quiet.
        if (x < 595 and 95 < y < 408 and not mobile) or (y < 320 and mobile):
            continue
        color = ['#382b50', '#50406c', '#71618c', '#a899c5'][i % 4]
        draw.rectangle((x, y, x + 3, y + 3), fill=color)
        if i % 13 == 0:
            draw.rectangle((x-4, y+1, x+7, y+2), fill=color)
            draw.rectangle((x+1, y-4, x+2, y+7), fill=color)


def hero(mobile=False):
    width, height = (640, 720) if mobile else (1200, 500)
    canvas = Image.new('RGB', (width, height), BG)
    d = ImageDraw.Draw(canvas)
    stars(d, width, height, 24, mobile)
    if mobile:
        text(d, (42, 50), 'Gustavo', 74, bold=True)
        text(d, (42, 128), 'Maquias.', 74, bold=True)
        text(d, (46, 230), 'Desenvolvimento de software', 26, MUTED)
        text(d, (46, 275), '> java + typescript', 19, LILAC, pixel=True)
        cx, cy = 320, 506
        factor = 6
        orbit_a, orbit_b = 228, 78
    else:
        text(d, (62, 122), 'Gustavo', 91, bold=True)
        text(d, (62, 216), 'Maquias.', 91, bold=True)
        text(d, (68, 338), 'Desenvolvimento de software', 25, MUTED)
        text(d, (68, 407), '> java + typescript', 19, LILAC, pixel=True)
        cx, cy = 897, 243
        factor = 6
        orbit_a, orbit_b = 240, 104
    # A dotted orbital path is intentional diagram geometry on the pixel grid.
    angle = -0.32
    def orbit(t):
        x, y = orbit_a * math.cos(t), orbit_b * math.sin(t)
        return (round((cx+x*math.cos(angle)-y*math.sin(angle))/4)*4,
                round((cy+x*math.sin(angle)+y*math.cos(angle))/4)*4)
    for n in range(104):
        x,y=orbit(n*TAU/104)
        if n%3 != 0:
            d.rectangle((x,y,x+2,y+2),fill=LINE)
    big = PLANET.resize((96*factor,64*factor),Image.Resampling.NEAREST)
    pos=(cx-big.width//2,cy-big.height//2)
    frames=[]
    for n in range(48):
        t=n*TAU/48
        frame=canvas.copy()
        x,y=orbit(t)
        def moon():
            q=ImageDraw.Draw(frame)
            q.rectangle((x-4,y-8,x+3,y+7),fill='#77678d')
            q.rectangle((x-8,y-4,x+7,y+3),fill='#77678d')
            q.rectangle((x-4,y-8,x+3,y-1),fill='#dccbef')
            q.rectangle((x-8,y-4,x-1,y+3),fill='#dccbef')
            q.rectangle((x,y,x+3,y+3),fill='#af9dc8')
        if math.sin(t)<0: moon()
        frame.paste(big,pos,big)
        if math.sin(t)>=0: moon()
        frames.append(frame)
    stem='hero-mobile' if mobile else 'hero'
    save_png(frames[0],stem+'.png','Orbital observatory; generated planet sprite, fixed pixel grid, authored typography and orbit. See design/source/PROMPTS.md.')
    # One shared palette and delta frames prevent palette flicker and keep GIFs light.
    palette=frames[0].quantize(colors=128,method=Image.Quantize.MEDIANCUT)
    indexed=[f.quantize(palette=palette,dither=Image.Dither.NONE) for f in frames]
    indexed[0].save(OUT/(stem+'.gif'),save_all=True,append_images=indexed[1:],
                    duration=250,loop=0,optimize=True,disposal=1,
                    comment=b'Gustavo Maquias / Orbital observatory. Source and provenance: design/source/PROMPTS.md')


def languages(mobile=False):
    w,h=(640,350) if mobile else (1200,236)
    im=Image.new('RGB',(w,h),BG); d=ImageDraw.Draw(im)
    if mobile:
        text(d,(38,32),'Java',54,bold=True)
        text(d,(214,32),'+',40,VIOLET)
        text(d,(270,32),'TypeScript',48,bold=True)
        text(d,(40,107),'Linguagens principais',25,MUTED)
        d.line((40,166,600,166),fill=LINE,width=2)
        text(d,(40,207),'Rust',33,LILAC,bold=True)
        text(d,(40,260),'Em projetos',26,MUTED)
        text(d,(327,207),'Python',33,LILAC,bold=True)
        text(d,(327,260),'Em aprendizado',26,MUTED)
    else:
        text(d,(60,42),'Java',66,bold=True)
        text(d,(244,47),'+',52,VIOLET)
        text(d,(310,42),'TypeScript',66,bold=True)
        text(d,(64,140),'Linguagens principais',24,MUTED)
        d.line((702,46,702,185),fill=LINE,width=2)
        text(d,(762,50),'Rust',30,LILAC,bold=True)
        text(d,(917,55),'Em projetos',26,MUTED)
        text(d,(762,126),'Python',30,LILAC,bold=True)
        text(d,(917,131),'Em aprendizado',26,MUTED)
    save_png(im,'languages-mobile.png' if mobile else 'languages.png','Language hierarchy from the two resumes. No inferred proficiency scores. Authored typography.')


def project_art(kind):
    im=Image.new('RGBA',(120,84),(0,0,0,0)); d=ImageDraw.Draw(im)
    if kind=='nocturne':
        # An isometric archive of three layers with a crescent knowledge core.
        for offset,body,edge in [(17,'#36254f','#6b4c94'),(8,'#503472','#9368c4'),(0,'#72509f','#bfa0e2')]:
            diamond=[(59,22+offset),(91,37+offset),(59,53+offset),(27,37+offset)]
            d.polygon(diamond,fill=body)
            d.line(diamond+[diamond[0]],fill=edge,width=1)
        for x in range(43,69,5):
            d.line((x,35,x+17,43),fill='#bfa0e2')
        # Deliberate block crescent: no monitor silhouette.
        d.ellipse((51,3,70,22),fill='#dbc5f4')
        d.ellipse((59,0,75,16),fill=(0,0,0,0))
        for x,y in [(10,26),(103,18),(98,62)]:
            d.rectangle((x,y,x+5,y+7),fill='#80609f')
            d.rectangle((x+1,y+2,x+3,y+2),fill='#d6b9f4')
        d.line((16,30,27,35),fill='#665079')
        d.line((91,31,103,23),fill='#665079')
        d.line((81,59,98,64),fill='#665079')
    else:
        # A processor with pins, a pulse trace and distinct telemetry endpoints.
        for x in range(42,81,6):
            d.rectangle((x,14,x+2,22),fill='#82739b')
            d.rectangle((x,62,x+2,70),fill='#82739b')
        for y in range(26,60,6):
            d.rectangle((32,y,40,y+2),fill='#82739b')
            d.rectangle((82,y,90,y+2),fill='#82739b')
        d.rectangle((40,22,82,62),fill='#403151',outline='#b49cca',width=2)
        d.rectangle((46,28,76,56),fill='#1d2331',outline='#637686')
        trace=[(8,44),(23,44),(23,40),(32,40),(32,44),(50,44),(50,38),
               (54,38),(54,48),(60,48),(60,34),(64,34),(64,44),(105,44)]
        d.line(trace,fill=MINT,width=2)
        d.rectangle((7,43,10,46),fill='#d8ede6')
        d.rectangle((104,43,107,46),fill='#d8ede6')
        for x,y in [(17,20),(99,17),(18,63),(105,66)]:
            d.rectangle((x,y,x+3,y+3),fill='#806495')
    return im


def project(kind,mobile=False):
    w,h=(640,390) if mobile else (1200,300)
    im=Image.new('RGB',(w,h),BG);d=ImageDraw.Draw(im)
    name='Nocturne Studio' if kind=='nocturne' else 'SysMon'
    caption='Projetos. Contexto. Conhecimento.' if kind=='nocturne' else 'Um olhar sobre o sistema.'
    if mobile:
        text(d,(38,37),name,45,bold=True)
        text(d,(40,100),caption,26,MUTED)
        art=project_art(kind).resize((360,252),Image.Resampling.NEAREST)
        im.paste(art,(140,140),art)
    else:
        text(d,(60,89),name,62,bold=True)
        text(d,(63,178),caption,25,MUTED)
        art=project_art(kind).resize((360,252),Image.Resampling.NEAREST)
        im.paste(art,(786,24),art)
    # One short tracking line connects the visual grammar across the composition.
    d.rectangle((0,0,w-1,3),fill='#5e437d' if kind=='nocturne' else '#536c78')
    save_png(im,f'{kind}'+('-mobile' if mobile else '')+'.png',
             'Authored pixel geometry: knowledge archive' if kind=='nocturne' else 'Authored pixel geometry: processor and signal; illustrative artwork, not a software screenshot.')


if __name__=='__main__':
    for mobile in (False,True):
        hero(mobile)
        languages(mobile)
        for kind in ('nocturne','sysmon'): project(kind,mobile)
    print('Built 10 responsive assets in',OUT)
