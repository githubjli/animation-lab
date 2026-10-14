from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, subprocess, wave, struct, hashlib, json
ROOT=Path(__file__).resolve().parent
W,H=960,540
font='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
F=ImageFont.truetype(font,23); SMALL=ImageFont.truetype(font,17); BIG=ImageFont.truetype(font,36)
shots=[(0,5,'建立空间：狐狸讲究，熊期待'),(5,10,'第一次合影：熊挡住狐狸'),(10,14,'看失败照片：尴尬，但继续合作'),(14,19,'风遮住脸：狐狸努力保持姿势'),(19,25,'熊帮忙：两人确认与配合'),(25,31,'重新启动计时：30秒启动，40秒快门'),(31,35,'风带走围巾：先看见，再追出数步'),(35,38,'抓住两端：减速，轻轻坐倒'),(38,41,'确认无碍 → 笑起来 → 意外快门'),(41,45,'看照片：狐狸接受自然的合影')]
def lerp(a,b,p): return a+(b-a)*max(0,min(1,p))
def char(d,x,y,kind='fox',mood='neutral',sit=0,phase=0,scale=1,arm=None):
    def pt(a,b):return (x+a*scale,y+b*scale)
    def line(points,fill='#384349',width=5):d.line([pt(a,b) for a,b in points],fill=fill,width=max(1,int(width*scale)))
    def ellipse(box,fill,outline='#384349',width=3):d.ellipse((*pt(box[0],box[1]),*pt(box[2],box[3])),fill=fill,outline=outline,width=max(1,int(width*scale)))
    col='#e8a263' if kind=='fox' else '#b89073'; coat='#647b96' if kind=='fox' else '#829378'
    knee=math.sin(phase)*8*(1-sit)
    line([(-15,-12),(-23-knee,0),(-40-knee,0)],width=7);line([(15,-12),(23+knee,0),(40+knee,0)],width=7)
    ellipse((-29,-100,29,-10),coat)
    if kind=='fox':
        d.polygon([pt(-28,-119),pt(-30,-165),pt(-5,-140)],fill=col,outline='#384349'); d.polygon([pt(28,-119),pt(30,-165),pt(5,-140)],fill=col,outline='#384349')
        ellipse((-58,-47,-13,-12),col)
    else:
        ellipse((-39,-151,-12,-124),col);ellipse((12,-151,39,-124),col)
    ellipse((-33,-145,33,-83),col);ellipse((-22,-115,22,-86),'#f1e2cc')
    if mood=='laugh':
        line([(-19,-119),(-13,-124),(-7,-119)],width=3);line([(7,-119),(13,-124),(19,-119)],width=3)
        ellipse((-10,-106,10,-92),'#544039')
    else:
        eye=4 if mood!='surprise' else 6
        ellipse((-17-eye,-124-eye,-17+eye,-124+eye),'#384349',width=1);ellipse((11-eye,-124-eye,11+eye,-124+eye),'#384349',width=1)
        if mood=='surprise':ellipse((-4,-103,4,-95),'#544039',width=1)
        else:line([(-9,-100),(0,-97 if mood=='happy' else -101),(9,-100)],width=2)
        if mood=='awkward':line([(-24,-134),(-9,-129)],width=3)
    line([(-27,-79),(-43,-57),(-35,-37)])
    line([(27,-79),(42,-60),(35,-38)] if arm is None else [(27,-79),arm])
def camera(d):
    d.line([(112,306),(81,415)],fill='#384349',width=5);d.line([(112,306),(143,415)],fill='#384349',width=5)
    d.rounded_rectangle((74,270,151,312),radius=5,fill='#52616b',outline='#283741',width=3);d.ellipse((118,281,142,302),fill='#c5e0df',outline='#283741',width=3)
def frame(t):
    i=next(k for k,(a,b,_) in enumerate(shots) if a<=t<b);a,b,label=shots[i];p=(t-a)/(b-a)
    im=Image.new('RGB',(W,H),'#edf0e8');d=ImageDraw.Draw(im)
    d.rectangle((0,65,W,460),fill='#e4e9e5');d.polygon([(0,350),(230,320),(600,340),(960,307),(960,460),(0,460)],fill='#d2ddbd')
    d.ellipse((706,285,902,371),fill='#aab89a');d.ellipse((762,277,842,337),fill='#b8c5a2')
    for k in range(9):
        x=200+k*82; sway=math.sin(t*2+k)*5;d.line([(x,412),(x+sway,393)],fill='#829378',width=2);d.ellipse((x+sway-3,389,x+sway+3,395),fill='#e5bd88')
    camera(d)
    d.line([(156,299),(850,246)],fill='#b5c0b8',width=1);d.line([(156,299),(850,434)],fill='#b5c0b8',width=1)
    x1,y1,x2,y2=410,382,555,382;m1,m2='neutral','happy';s=0;phase=0
    if i==0:x1=lerp(155,410,p);m1='neutral'
    if i==1:x1=lerp(155,490,min(p*2,1));x2=lerp(555,485,p);m1='awkward'
    if i==2:m1='awkward';m2='awkward'
    if i==3:m1='awkward';m2='surprise';x2=lerp(555,510,max(0,(p-.5)*2))
    if i==4:x2=510;m1='awkward' if p<.6 else 'happy';m2='neutral'
    if i==5:x1=lerp(410,155,p*1.5) if t<30 else lerp(155,410,t-30);m2='neutral'
    if i==6:
        q=max(0,(p-.2)/.8);x1=lerp(410,590,q);x2=lerp(555,720,q);phase=t*12;m1=m2='surprise'
    if i==7:
        x1=590;x2=720;s=max(0,(p-.35)/.65);y1=y2=lerp(382,431,s);m1=m2='surprise'
    if i==8:
        x1=590;x2=720;y1=y2=431;s=1;m1='surprise' if p<.45 else 'laugh';m2='surprise' if p<.6 else 'laugh'
    if i==9:x1=245;x2=345;m1=m2='happy'
    char(d,x1,y1,'fox',m1,s,phase,arm=(60,-50) if i in (4,7,8) else None)
    char(d,x2,y2,'bear',m2,s,phase+.6,arm=(-60,-50) if i in (4,7,8) else None)
    if i not in (6,7,8,9):
        sy=y1-83;ex=x1+85;ey=sy+math.sin(t*4)*12
        if i==3:ey=y1-126;ex=x1+15
        if i==4:ex=lerp(x1+15,x1+65,p);ey=lerp(y1-126,sy+10,p)
        d.line([(x1-20,sy),(x1+18,sy),(ex,ey)],fill='#b75753',width=12)
    if i==6:
        sx=lerp(455,760,p);sy=lerp(275,320,p);d.line([(sx-65,sy+12),(sx,sy),(sx+35,sy+8)],fill='#b75753',width=12)
    if i in (7,8):d.line([(x1+60,y1-50),(650,lerp(345,419,s)),(x2-60,y2-50)],fill='#b75753',width=12)
    if i==2 and p<.45:
        d.rounded_rectangle((290,130,670,390),radius=12,fill='#52616b');d.rectangle((306,145,654,374),fill='#d2ddbd')
        char(d,455,360,'fox','awkward',scale=1.15);char(d,480,360,'bear','happy',scale=1.65)
        d.text((314,151),'第一次照片',font=SMALL,fill='white')
    if i==9 and p>.35:
        d.rounded_rectangle((430,145,873,405),radius=12,fill='#52616b');d.rectangle((446,160,857,389),fill='#d2ddbd')
        char(d,557,375,'fox','laugh',sit=1,scale=.9);char(d,726,375,'bear','laugh',sit=1,scale=.9)
        d.line([(611,330),(650,366),(672,330)],fill='#b75753',width=10)
        d.text((457,169),'留下这一张',font=SMALL,fill='#384349')
    if 5<=t<10 or 30<=t<40:
        n=math.ceil((10 if t<10 else 40)-t);d.text((95,230),str(n),font=BIG,fill='#b75753')
    if abs(t-10)<.1 or abs(t-40)<.1:d.rectangle((0,65,W,460),fill='#fff8e9')
    d.rectangle((0,0,W,65),fill='#293e47');d.text((22,10),'风中的合影  /  粗动态分镜 v0.1',font=F,fill='white');d.text((22,40),'简化姿态预演 · 非最终美术 / 动画 · 临时声音',font=SMALL,fill='#cad6d6')
    d.rectangle((0,460,W,H),fill='#293e47');d.text((22,470),f'S{i+1:02d}  {a:02d}—{b:02d}s  |  {label}',font=F,fill='white');d.text((22,510),f'{t:05.1f} / 45.0 秒   ·   先看事件与反应，再评估节奏',font=SMALL,fill='#cad6d6')
    d.rectangle((0,536,int(W*t/45),539),fill='#e2ba81')
    return im
# Original synthetic sound only: wind-like bed, timer beeps and shutter cues.
rate=24000
with wave.open(str(ROOT/'temp-sound-v0.1.wav'),'wb') as w:
    w.setparams((1,2,rate,0,'NONE','not compressed'))
    buf=bytearray()
    for n in range(rate*45):
        t=n/rate;v=.008*math.sin(t*2)*math.sin(2*math.pi*127*t)
        for st in list(range(5,10))+list(range(30,40)):
            z=t-st
            if 0<=z<.075:v+=.10*math.sin(2*math.pi*880*z)*math.sin(math.pi*z/.075)
        for st in (10,40):
            z=t-st
            if 0<=z<.12:v+=.18*math.sin(2*math.pi*(900-500*z)*z)*math.exp(-z*35)
        if 31<t<38:v+=.01*math.sin(2*math.pi*173*t)*math.sin(t*9)
        buf.extend(struct.pack('<h',int(max(-1,min(1,v))*32767)))
    w.writeframes(buf)
proc=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','12','-i','pipe:0','-i',str(ROOT/'temp-sound-v0.1.wav'),'-c:v','libx264','-preset','fast','-crf','20','-pix_fmt','yuv420p','-r','24','-c:a','aac','-movflags','+faststart','-t','45',str(ROOT/'animatic-v0.1.mp4')],stdin=subprocess.PIPE)
for n in range(540):proc.stdin.write(frame(n/12).tobytes())
proc.stdin.close();assert proc.wait()==0
sheet=Image.new('RGB',(960,540*5),'white')
for i,(a,b,label) in enumerate(shots):sheet.paste(frame((a+b)/2).resize((480,270)),((i%2)*480,(i//2)*270))
sheet=sheet.crop((0,0,960,1350));sheet.save(ROOT/'contact-sheet-v0.1.jpg')
files=['build_v01.py','temp-sound-v0.1.wav','animatic-v0.1.mp4','contact-sheet-v0.1.jpg']
(ROOT/'record-v0.1.json').write_text(json.dumps({'status':'rough-animatic-unreviewed','duration':45,'output_fps':24,'unique_pose_frames_per_second':12,'resolution':[960,540],'method':'procedural Pillow shapes; original synthetic temporary sound; FFmpeg encoding','model':None,'reference_images_used':[],'source_beats':'../BEATS-v0.1.md','limitations':['not final character assets','no motion or visual quality approval','reference continuous review remains pending','two photo inserts are illustrative reconstruction'],'files':[{'path':f,'sha256':hashlib.sha256((ROOT/f).read_bytes()).hexdigest()} for f in files]},ensure_ascii=False,indent=2),encoding='utf-8')
print(ROOT/'animatic-v0.1.mp4')
