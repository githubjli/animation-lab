# 《The Michelin Masterpiece》· 可运行 FINAL Prompt（对齐你的资产）

> 基于 `master-prompt-ORIGINAL.md`（el.cine 逐字原稿）改成**匹配你手上素材**的可运行版。原稿保留不动，本文件用于实际生成。
> 生成日期：2026-09-29

## 相对原稿的改动（3 处）
1. **厨师改无胡子**：`full dark beard` → `clean-shaven, swept dark hair, thick eyebrows`（匹配你的 chef 设定图）。
2. **Shot 16 / 17 去胡子**：`His beard begins to tremble` → `chin and lower lip`；`rolls down into his beard` → `rolls down his cheek`。
3. **两道菜都用图**（比原稿更强）：`dish-home-style.png`=奶奶家常菜，占原版 `@image 3` 槽位（第14镜）；`dish.png`=厨师精致菜，新增 `@image 6` 槽位（第2镜）。原稿里厨师菜是纯文字，这里升级成有参考图，反差笑点靠两张真图更稳。

## 资产映射（你的文件 → Prompt 引用名 / Filmera 槽位）
| 你的文件 | Prompt 引用名 | Filmera 槽位 |
|---|---|---|
| `characters/chef.png` | CHARACTER_01_CHEF | image 1 |
| `characters/grandma.png` | CHARACTER_02_GRANDMA | image 2 |
| `props/dish-home-style.png`（奶奶家常菜） | DISH | image 3 |
| `scenes/restaurant.png` | RESTAURANT | image 4 |
| `scenes/kitchen.png` | KITCHEN | image 5 |
| `props/dish.png`（厨师精致菜） | CHEF_DISH | image 6（新增） |
| `storyboard/storyboard.png` | （参考，非必须入槽） | — |
> Duplicate el.cine 工程时 image 1–5 槽位已排好，直接把图**替换成上表你的文件**；额外**新增一个 image 6 槽**放 `dish.png`。`@image 3/4/5` 编号不变即可对上。

## 生成配置
Seedance 2.5 · 720p · 16:9 · 30s · Audio On · 单 Shot / 18 镜一次生成。

---

## FINAL Prompt 全文（可直接粘贴）

```
[GLOBAL] A complete comedic short in ONE generation, told in 18 numbered shots in order — real time runs continuously from shot to shot, each shot beginning where the last ended. Stylized 3D feature-animation look: appealing cartoon character shapes, rich warm lighting, glossy exaggerated food rendering, strong squash-and-stretch, smear frames and cartoony motion blur on the fast beats, smooth 24fps. RHYTHM: shots 1–6 are unhurried and polite; shots 7–13 are a rapid-fire escalating burst; shot 14 is a long, completely still, silent hold; shots 15–18 are slow again. GRANDMA (match CHARACTER_02_GRANDMA exactly): tiny, round, very short elderly woman, fluffy light-blue bun, enormous round gold glasses, pearls, white cardigan, small handbag on her forearm — she barely reaches the chef's waist. CHEF (match CHARACTER_01_CHEF exactly): very tall, broad, clean-shaven with swept dark hair and thick eyebrows, immaculate white jacket, a very tall white toque. THE CHEF'S DISH (match @image 6 exactly): a precious fine-dining plate — a seared filet on a swirl of purée, a few baby vegetables, dots of sauce, micro-herbs and a delicate tuile, lots of empty white plate. GRANDMA'S DISH (match DISH / @image 3 exactly): the generous home-style plate that appears in shots 14–17 — thick hand-cut steak slices, a hearty heap of glossy roasted carrots and potatoes, dark rich pan sauce spilling off the edge, one sprig of rosemary, thick steam. RESTAURANT (match RESTAURANT) for shots 1–6 and 15–18; KITCHEN (match KITCHEN) for shots 7–14; the two rooms connect through the swinging porthole door. THE HAT: the chef's tall toque is taken by Grandma in shot 6, worn by her through shots 7–15 (far too big — it slides down over her glasses and she keeps shoving it back up), and returned to his head in shot 18. ACTING: HIGHLY EXPRESSIVE cartoon performance, never flat — Grandma is small, calm and unhurried, and does her acting with her eyebrows, her chewing and her tiny hands; the chef does his with his whole enormous body (chest deflating, hands flying to his head, knees buckling). Emotion shown only through visible physical behaviour, never named. Nobody is ever completely still except where a hold is specified. No on-screen text of any kind, no logos, no signage. NO background music — diegetic sound only, cued exactly on the action: the cloche lifting with a soft ring, cutlery on china, a slow chew, the tiny rattle of a salt shaker, a chair scraping, the hat's soft whump landing on her head, the swinging door creaking, gas igniting with a whoomp, knife chops accelerating, a slap on the back of a hand, a fan flapping, a ladle tap, then TOTAL SILENCE on the plating hold, then the cloche ring again, a fork through crust, chewing, a sniff, a wet sob, knees hitting the floor, two pats on a cheek.

Shot 1: wide establishing shot, eye-level, slow push-in, the small round table centred in the elegant restaurant (match @image 4): the CHEF towers beside the table, chest out, and lifts the silver cloche off the plate with a flourish and a soft ring, beaming down at GRANDMA, who sits tiny in her chair with her handbag in her lap and looks up at him with a polite closed-mouth smile.

Shot 2: tight close-up, high angle, static, on the chef's dish (match @image 6): the precious fine-dining plate — a seared filet on a swirl of purée, a few baby vegetables, dots of sauce, micro-herbs and a delicate tuile, a great deal of empty white plate — the chef's white torso soft in the background, his hands folding proudly behind his back.

Shot 3: extreme close-up on Grandma's face, eye-level, her huge glasses magnifying her eyes: she cuts a small piece, lifts it in, and chews SLOWLY — very slowly — her eyes drifting sideways toward the chef, one eyebrow creeping up a millimetre at a time. She swallows. Her mouth makes a small, polite "hm."

Shot 4: medium shot from across the table, Grandma centred, the chef's beaming face visible at the top of frame: without breaking eye contact with him, she opens her handbag, takes out a TINY SILVER SALT SHAKER, and gives his dish two crisp little shakes — rattle, rattle — puts it away, takes a second bite, and gives one small satisfied nod: better.

Shot 5: close-up on the chef's face, eye-level, slight push-in: his beaming smile freezes, then slides off his face in stages — the corners of the mouth dropping, the eyes widening, the nostrils flaring — until his mouth is open and his eyebrows are up in his hairline. His chest visibly deflates.

Shot 6: wide two-shot, eye-level, the height difference filling the frame: Grandma dabs her mouth with the napkin, folds it, sets it down, and stands — her head barely reaching his waist. She goes up onto her tiptoes, reaches straight up with both arms, and lifts the tall white toque clean off his head. She lowers it onto her own bun — WHUMP — where it slides down over her glasses; she shoves it back up with one hand, then walks straight past him toward the swinging porthole door, leaving him frozen with both hands on top of his bare head.

Shot 7: wide shot, low angle, in the kitchen (match @image 5), checkered floor stretching to camera: the swinging door CREAKS open and Grandma marches in wearing the huge toque, drags the step stool out from under the counter with one hand, climbs up onto it in front of the range, plants both fists on her hips, and every burner IGNITES at once with a row of whoomps. Behind her, the chef appears in the porthole window, face pressed to the glass.

Shot 8: close-up, low angle, Grandma's face lit from below by blue flame, the toque brim just above her glasses: she picks up the chef's knife, tests the edge with her thumb, purses her lips, unimpressed, and sharpens it in two fast strokes on the rim of a copper pan — SHING, SHING — then looks straight into the lens with narrowed eyes, glasses flashing.

Shot 9: extreme close-up on the wooden board, blade and tiny hands only: the knife machine-guns down through a thick steak in a blur of smear frames, her pinky raised the whole time, thick slices fanning out; the tempo of chops accelerates past what a hand could do.

Shot 10: medium shot on the range, low angle: the slices hit the copper pan with a violent sizzle and a wall of orange flame ROARS up past the lens; she leans right into it, toque brim smoking slightly, and flaps a little folding fan from her handbag at the flames to make them bigger.

Shot 11: medium shot at the counter, eye-level: the CHEF pushes through the door, reaches a huge hand toward the pan to help — and without looking she SLAPS the back of his hand with a wooden spoon, a sharp crack. He snatches it back, cradling it. She points the spoon at the door. He backs out through it, rubbing his hand.

Shot 12: wide shot, Grandma centred on her stool: she is now running three pans at once — tossing one so high the slices flip near the hanging pots, stirring a second with her elbow, catching a bottle knocked off the shelf with the back of her hand without looking — the toque sliding over her eyes every few seconds and getting shoved back up with the heel of her hand.

Shot 13: close-up, eye-level: she dips a ladle into the sauce, blows on it once, tastes it with her pinky raised, and pauses — then wipes her hands on the front of the chef's giant apron she has tied around herself twice, and gives one tiny nod.

Shot 14: THE PLATING — tight overhead macro on a plain white plate, and the pace drops right down: thick slices are laid on with a spoon, generous and honest, a heap of glossy carrots and potatoes is pushed against them, dark pan sauce is spooned over so it spills off the edge of the meat, a sprig of rosemary is dropped on by hand — then her hands withdraw and the shot HOLDS completely still on the finished generous home-style dish (match DISH / @image 3), thick steam curling up, ALL SOUND CUTTING TO SILENCE.

Shot 15: wide shot, eye-level, the same framing as Shot 1 but reversed, back in the restaurant (match @image 4): the CHEF now sits in her chair, bareheaded, too big for it, knees up near the tabletop. Grandma, still wearing his toque, stands beside the table and lifts a silver cloche off the plate with exactly his flourish and the same soft ring, and looks down at him with the same polite closed-mouth smile.

Shot 16: close-up on the chef's face, eye-level, slight push-in: he looks at the plate, then up at her, then back at the plate, and picks up a fork with a hand that is not quite steady. He takes one big bite — and stops chewing. His eyes bulge. His eyebrows climb. His chin and lower lip begin to tremble.

Shot 17: close-up two-shot: Grandma leans in from the side, chin resting on her tiny hand, and raises one eyebrow at him — see? — and one enormous glossy cartoon tear wells up in the chef's eye and rolls down his cheek, then another, and his whole face crumples as he presses both hands over it.

Shot 18: final wide shot, eye-level, slow pull-back, the two of them centred: the chef slides off the chair onto both knees on the carpet, head bowed, shoulders shaking. Grandma reaches up, takes the tall toque off her own bun, and sets it back on his bowed head, straightening it once. She pats his cheek twice — pat, pat — sits back down in her chair, picks up her fork, and calmly takes another bite of her own dish. Hold one beat. End.
```

---

## 跑之前的最终检查清单
- [ ] Filmera：Duplicate el.cine 工程，并新增第 6 个 image 槽。
- [ ] 6 张图入槽：chef→1、grandma→2、**dish-home-style→3**、restaurant→4、kitchen→5、**dish→6**。
- [ ] 粘贴本 FINAL Prompt，确认 `@image 3`(奶奶菜)、`@image 6`(厨师菜)、`@image 4/5`(餐厅/厨房)指向正确。
- [ ] Seedance 2.5：720p / 16:9 / 30s / Audio On。
- [ ] 跑 3–5 个 Take，一次只改一处再迭代。
