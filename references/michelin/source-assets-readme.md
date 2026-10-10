# Michelin 参考资产

采用内置 image_gen。`chef.png` 复用项目已有厨师设定图；其余资产依据 [reference-image-prompts.md](../reference-image-prompts.md) 生成。

| REF | 资产 |
|---|---|
| chef | [厨师](characters/chef.png) |
| grandma | [奶奶](characters/grandma.png) |
| restaurant | [餐厅](scenes/restaurant.png) |
| kitchen | [厨房](scenes/kitchen.png) |
| dish | [菜品](props/dish.png) |
| storyboard | [18 镜分镜](storyboard/storyboard.png) |

## 提示词与参考图

奶奶、餐厅、厨房、菜品分别使用原提示词文件中的对应描述，并以厨师图作为画风参考。统一使用 cinematic stylized 3D animation, Pixar-like, warm fine-dining lighting, shallow depth of field, soft film grain, 16:9。补充无水印、无文字、完整主体构图；奶奶维持相同衣着和帽型，包含全身、三种表情及戴帽姿势。

分镜已使用内置 image_gen 生成并保存为 storyboard/storyboard.png。带参考图的请求多次遇到网络错误，最终采用纯文字描述生成，包含 18 镜及高帽传递。人物外观与原角色图略有差异，分镜主要作为动作、构图和节奏参考；角色外观以 characters/ 下的设定图为准。精确动作与时序以 master-prompt.md 为准。最终提示词见 [storyboard/prompt.txt](storyboard/prompt.txt)。
