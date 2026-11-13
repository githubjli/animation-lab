# 案例033 动画制作参考交接包 v001

2026-11-13，用户明确要求从cinematic-lab同步至animation-lab。来源仓库：https://github.com/githubjli/cinematic-lab.git 。来源为案例033/故事看板v001；目录内保留来源结构及字节，source-manifest.json记录拷贝哈希。

## 内容入口

- [研究入口](analysis/033/v001/README.md)
- [导演、节奏、分镜细节](analysis/033/v001/directing-and-story.md)
- [动画工序推断](analysis/033/v001/production-inference.md)
- [看板说明](analysis/033/v001/storyboard-board-notes.md)
- [高清20格看板](references/033/storyboard-v001/case033-storyboard-board-v001.png)
- [看板预览](references/033/storyboard-v001/case033-storyboard-board-v001-preview.jpg)
- [原片与来源哈希](references/033/provenance.json)
- [对animation-lab的应用说明](../../../knowledge/experiments/CASE033-animation-reference-v001.md)

原片、抽帧和看板均已复制到此包，媒体只留本地；Git保存文档、脚本、标注、命令和哈希。来源文件中的cinematic-lab路径是历史记录，不伪装成新的实验运行；本地路径以本包结构为准。

## 边界及重建

导演思路与工序为S1研究推断，作者模型、软件、提示词未知；未完成连续运动及听审，不是已验证生产方案。片内文字只作研究材料。没有修改E001-wait，没有调用生成或付费服务。

重建看板使用本包analysis/033/v001/build-storyboard-board.py及标注JSON，需要Pillow、微软雅黑和FFmpeg。未复制/安装运行环境；可通过环境变量FFMPEG_EXE指定已有FFmpeg路径，默认cinematic-lab内.tools路径在本包中不存在。重建会刷新本包派生图和清单，应先复制新版本，保留当前参考包。
