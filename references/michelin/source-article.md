# 源文章存档

- 标题：美国导演 el.cine，手把手教AI动画电影2：The Michelin Masterpiece
- 作者：Neal / 公众号「路过AI」
- 发布：2026-09-15 17:00（荷兰）
- URL：https://mp.weixin.qq.com/s/xqq7mkj1LM1sAshU1sRcwg
- 抓取方式：app 内置浏览器（WebFetch 被微信验证墙拦截）
- 抓取日期：2026-09-29

> 下为正文要点转录（非逐字全文；仅供本子项目学习流程用）。

## 项目
el.cine（旧金山电影导演 + AI 顾问，14 年好莱坞导演/剪辑经验）在线发起"开源分享 AI 动画视频制作案例"活动。本片《The Michelin Masterpiece》连同制作过程一起公开：角色图、场景图、Storyboard、完整 Prompt、Seedance 2.5 参数，以及可直接复制的 Filmera 工程。

故事：一个厨师给奶奶做菜；奶奶尝后接过厨师帽亲自下厨；最后轮到厨师尝奶奶手艺。成片 30 秒。

## 五步流程（原文）
1. **先做 Storyboard**：用 GPT Image（原文"GPT Image 2.5"）把餐厅/厨房/两人动作排成一张分镜，定死人物/场景/每镜内容/顺序/情绪。镜头数不先写死。
   - 原文给的可复用指令：「把下面的故事整理成一张完整的动画 Storyboard。按剧情顺序设计连续镜头，标明镜头编号、景别、人物动作、情绪变化和场景关系，同时保持角色、服装、道具和画风一致。」
2. **单独准备参考图**：共 6 张——厨师、奶奶、Storyboard、最终菜品、餐厅、厨房。奶奶的眼镜/手袋、厨师的高帽固定下来。
3. **复制 Filmera 工程**：点 "Duplicate to try this" 复制，再换成自己的角色/场景/Storyboard。最终 Prompt 公开，长 8,981 字符，像导演执行单：前6镜慢/7–13加速/14停住/15–18放慢；规定各自表演、餐厅↔厨房切换、厨师帽第6→18镜去向、无 BGM 时的现场声。做法：复制原工程→保留 Prompt 结构→改人物/场景/剧情，再核对图片引用。
4. **交给 Seedance 2.5**：720p / 16:9 / 30s / Audio On。工程仅 1 个 Shot，一次生成按顺序完成 18 镜。原文特别说明：可拆成几段分别生成再剪辑拼接。
5. **多生成几个版本**：项目概览 1 Shot / 12 Takes，多跑几个 Take 挑选。一次只改一样（人物问题改人物图；顺序问题改 Storyboard/Prompt）。Takes ≠ 成片数（当前视频节点只显示 T1）。

## 工具（均为商业产品，非开源代码）
- GPT Image — Storyboard/参考图
- Filmera（filmera.ai）— 工程编排 + 公开可复制模板
- Seedance 2.5（字节/BytePlus）— 视频生成底座

## 素材图 URL（文章内共 16 张，未提供外部直链；以下为图片 CDN 地址，供查阅）
- Storyboard（第1/2页，已复原镜头表见 ../PIPELINE.md）：
  https://mmbiz.qpic.cn/sz_mmbiz_png/s06WuNnDVzrOcGKZ6VDcMKTiaicwFtsor1tJ8M7J7zWic7SBC1lGQXa8PtSqgbV9tT1AAMgz6IUTtiaHX0TW688qSUDRkrhSEwxkcMLUk2P4Zhs/640?wx_fmt=png&from=appmsg
- 其余角色/场景/工程截图共 15 张，前缀同为 `s06WuNnDVz...`，imgIndex 0–15；如需逐张查阅在文章页按顺序点开。

## 关联
- 同作者/同流程的另一片《The Last Bond》(13 镜)：
  https://www.aiposthub.com/el-cine-the-last-bond-filmera-seedance-tutorial-2026/
- el.cine：X @EHuanglu、IG @el.cine.h
- Filmera：X @filmera_ai、filmera.ai
