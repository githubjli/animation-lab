# 角色、场景与道具出图提示词 v0.1

2026-10-10。依据CHARACTER-STORY-v0.1与当前30秒故事方向。仅准备，未提交。所有视觉资产仍planned。以下英文块为拟用原文，实际提交时须保存最终原文、输入文件SHA256与顺序、已知参数、原始输出和审查；模型、尺寸、seed、成本当前未知。16:9是构图目标，不是实际输出参数。

## 使用顺序与参考槽位

先运行01候选，评审后以选定文件作为STYLE_MASTER。02/03引用它制作身份候选，评审后成为FOX_ID/RABBIT_ID。04引用STYLE_MASTER；05引用评审后的场景图；06引用FOX_ID及道具图。槽位名不是已存在图片，提交前必须替换为真实附件，并记录上传顺序。不要无参考分别出图后宣称一致。候选均另存不覆盖。

## 01 双角色风格探索

```text
Create one landscape 16:9 visual development image for an original warm animated short. Two adult anthropomorphic animals stand side by side, full bodies and feet visible, fox on the left, rabbit on the right, on a quiet warm-gray studio background. Cohesive stylized 3D animation design, sculpted grouped fur, matte woven clothes, appealing clear silhouettes, restrained expressive faces, animal muzzles, believable joints and weight. Warm upper rear-left key light with cool soft frontal sky fill, readable eyes and gentle contact shadows.
FOX: taller and slender, rust-red fur, cream muzzle and tail tip, pointed ears, elongated face, dark brown nose and brows; blue-gray short coat with a usable pocket on the character's own right side, beige trousers, dark brown flat shoes. One bushy tail emerges below the back of the coat. Relaxed hands, subtly impatient but kind expression.
RABBIT: shorter and compact, warm cream fur, long ears with muted gray-pink interiors, dark brown eyes and nose; moss-green vest over a plain ivory shirt, warm light-gray trousers, dark brown flat shoes. One plain canvas satchel at the character's own left hip, strap from the character's right shoulder to left hip. Calm attentive expression.
Both have consistent simplified four-digit hands including the thumb. Adult proportions, moderate eye size, no baby heads. No hats, jewelry, logos, text, extra characters, food, or scene props. Keep hands and satchel strap clearly visible. This is a design exploration, not a story scene.
```

兔子内搭象牙白衬衫为本包新增候选细节，供背心结构完整；采纳后同步角色身份卡、人物设计提案和执行稿。

## 02 狐狸身份图（引用选定STYLE_MASTER）

```text
Using the attached approved style exploration as the visual reference, create a clean fox character model sheet. Preserve the fox's face, adult proportions, fur colors, coat, trousers, shoes and hand anatomy exactly. Top row: full-body front, left profile, and rear views of the same fox, neutral standing pose, matched scale and ground line, feet uncropped. Show the single tail emerging naturally below the coat; the rear view must show its root. The coat pocket is on the character's own right side. Bottom row: four close face studies, neutral, mildly puzzled, small surprised realization, and a relaxed grateful smile. Keep the animal muzzle and identity stable in every view. Empty hands, no paper bag or handkerchief. Warm-gray background, soft readable studio lighting in the same visual style. No text, labels, logos or additional clothing.
```

## 03 兔子身份图（引用选定STYLE_MASTER）

```text
Using the attached approved style exploration as the visual reference, create a clean rabbit character model sheet. Preserve the rabbit's face, adult proportions, fur colors, long ears, vest, shirt, trousers, shoes and hand anatomy exactly. Top row: full-body front, left profile, and rear views of the same rabbit, neutral standing pose, matched scale and ground line, feet uncropped. Preserve one canvas satchel at the character's own left hip and its strap from right shoulder to left hip; do not mirror the strap between views. Bottom row: four close face studies, neutral attentive, concerned warning, patient explanation, and a gentle relieved smile. Ear poses support subtle expression without changing ear length. Warm-gray background, soft readable studio lighting in the same visual style. No handkerchief in the hands, text, labels, logos or additional accessories.
```

## 04 公园空间主图（引用STYLE_MASTER）

```text
Create one landscape 16:9 empty park environment reference in the exact visual language of the attached style reference. A small quiet park just after rain, warm sunlight from the upper rear-left and cool sky fill, muted foliage, tactile stylized stone and wood, soft atmospheric depth. Eye-level wide three-quarter view from the path, all key objects fully visible. A freshly painted green wooden bench with a backrest and simple dark metal legs is in the middle-left, front facing the camera. Immediately to the bench's right lies one small wooden warning board, blank back facing upward, illustrated front hidden. At the right foreground is a broad low dry stone step, parallel to the bench, with room for two adults to sit side by side with feet on the path. The step is only one or two walking steps from the bench and beneath a sparse sheltering tree canopy; its sitting surface is matte and dry, with no puddles. The surrounding path has subtle wet patches. Keep the route from bench to step clear. Distinct bench, sign and step silhouettes; no characters, bags, loose cloth, paint cans, brushes, readable lettering, logos or additional benches. Fixed camera, no collage.
```

场景左右为镜头画面方向；身体左右为角色自身方向。此布局为候选，出图通过后再建立俯视空间图、轴线与逐镜构图，不能仅凭提示词认定空间已锁定。

## 05 道具形态与状态图（引用场景图与STYLE_MASTER）

```text
Create a neatly spaced prop design sheet in the attached park scene's exact stylized materials and color palette, on a neutral warm-gray background with consistent soft lighting. Show separate objects clearly, no overlap.
One green wooden park bench matching the scene, three-quarter front view, freshly painted seat and backrest with subtle wet sheen, simple dark metal legs, no exaggerated dripping paint.
The same small wooden warning board in three views: upright illustrated front, upright plain back, and lying flat with plain back up. A stable simple hinged support makes standing and fallen states mechanically plausible. Its front has only a large paintbrush-and-droplet pictogram, dark on pale cream, readable without words. Preserve the same board shape, hinge and support across all views.
One plain folded-top kraft paper bag, no handles, closed, large enough to rest in a forearm and on a seated lap, no visible food.
One simple ivory square cotton handkerchief shown clean and folded, then unfolded with a small muted-green paint smear; identical fabric and size.
One plain canvas satchel matching the rabbit's reference, open enough to show the folded clean handkerchief fitting inside. Use the attached rabbit identity reference if supplied.
No characters, hands, additional objects, text, labels or logos. Show each object's entire silhouette.
```

## 06 接触状态验证图（引用FOX_ID、场景与道具参考）

```text
Create a three-panel continuity study of the approved fox's right hand and the approved green bench backrest, matching all attached references. The same camera angle, lighting, hand anatomy, coat sleeve and bench geometry in every panel. Panel one: clean palm edge hovering just above the freshly painted backrest, no contact and no paint on the hand. Panel two: the palm edge makes gentle visible contact with the top of the backrest, fingers outside the wood, no penetration. Panel three: the hand has withdrawn, palm turned toward camera, with one small green paint mark only along the contacted outer palm edge; a subtle matching contact mark remains on the bench. Four digits including thumb, same hand throughout. No paint on trousers, sleeve or entire palm, no text or labels. These are three successive states, not three hands in one scene.
```

## 评审与依赖

01看成年气质、轮廓反差、统一材质和可读表情；02/03看各视图身份与左右一致；04看干台阶可见、路线短、倒牌不提前揭谜；05看道具唯一、机构可行、手帕可装入包和口袋；06看接触前后因果及手部结构。参考图只能验证静态设计，动作需要动态分镜和连续视频审查。

本包新增衬衫、警示牌支撑机构、手帕颜色及台阶遮雨解释，均待出图评审；采纳后同步CHARACTER-STORY、CONTINUITY、manifest和PROMPT-DRAFT，再推进故事板。SHOT-LOCK v0.1暂保留。没有实际提交，不建立虚构实验结果或输入哈希。
