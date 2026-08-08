# Humanizer 中文版：中文 AI 写作去痕与自然改写 Skill

[![Validate package](https://github.com/holygeek00/humanizer-zh-cn/actions/workflows/validate.yml/badge.svg)](https://github.com/holygeek00/humanizer-zh-cn/actions/workflows/validate.yml)
[![Sync upstream](https://github.com/holygeek00/humanizer-zh-cn/actions/workflows/sync-upstream.yml/badge.svg)](https://github.com/holygeek00/humanizer-zh-cn/actions/workflows/sync-upstream.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent_Skill-Codex%20%7C%20Claude_Code-blue)](#支持的-agent)

把 ChatGPT、GPT 等模型生成的中文初稿改得自然、具体，清理“赋能、打造、闭环、未来可期”等 AI 味、黑话和套话，同时保留事实、原意与作者声线。

`humanizer-zh` 是一个简体中文 Agent Skill，适合 Codex、Claude Code 和其他支持 Markdown Skills 的 Agent。它不靠禁词表机械替换，而是检查黑话有没有吞掉“谁做了什么、作用于谁、结果如何、证据在哪”，再从原文中把信息放回句子。

> Chinese-first AI writing humanizer skill for Codex and Claude Code. Removes formulaic AI tone and business jargon without changing facts.

[看改写效果](#改写效果) · [30 秒安装](#30-秒安装) · [支持的 Agent](#支持的-agent) · [33 类模式](#33-类中文-ai-写作模式) · [常见问题](#常见问题)

## 改写效果

**改写前**

> 本次功能升级以用户体验为核心抓手，通过上线订单页自助退款入口，进一步赋能售后服务提质增效。上线后，每天需要人工处理的退款工单从 120 件降到 45 件，充分彰显了团队持续创新的卓越能力。

**改写后**

> 订单页上线自助退款入口后，每天需要人工处理的退款工单从 120 件降到 45 件。

改写保留了入口位置、工单类型和数字，只删掉没有增加信息的姿态层。原文没有具体信息时，技能不会为了“更像真人”编造数字、流程、案例或来源。

## 30 秒安装

```bash
npx skills add holygeek00/humanizer-zh-cn --global
```

安装后新开会话或重新加载 Skills，然后直接说：

```text
用 $humanizer-zh 去掉下面这段中文的 AI 味，保留事实、原意和语气：

[粘贴文本]
```

## 它解决什么

- 文案、文章、报告、邮件和社交媒体内容去 AI 味
- 清理“赋能、打造、深度、全方位、未来可期”等套话，找回被抽象词遮住的动作和责任主体
- 减少机械排比、强凑三点、标题口号化和聊天机器人残留
- 按用户样稿校准声线，保留方言、网络用语和个人表达习惯
- 审校时保护事实、数字、引用、代码和真正的不确定性

## 为什么不是同义词替换器

“AI 赋能业务增长”不能只改成“AI 助力业务增长”。两句话都没有信息。技能会检查：

1. 谁在使用 AI？
2. AI 具体做了什么？
3. 作用于哪个流程或对象？
4. 结果是什么？
5. 有什么数据或事实支持？

原文有答案，就把动作和结果写出来；没有答案，就删除无依据的效果，或在审校意见中指出缺失。详见 [SKILL.md](SKILL.md#先找回被黑话吃掉的信息)。

## 支持的 Agent

| Agent / 工具 | 安装方式 | 验证状态 |
|---|---|---|
| Codex | Skills CLI | 已验证 |
| Claude Code | 插件或手动安装 | 已验证插件清单 |
| 其他支持 Markdown Skills 的 Agent | Skills CLI 或复制 `SKILL.md` | 取决于宿主实现 |

运行时核心只有一份 Markdown 文件，不依赖模型 API 或外部服务。

## 其他安装方式

### Skills CLI

安装到所有受支持的 Agent：

```bash
npx skills add holygeek00/humanizer-zh-cn --global --agent '*'
```

更新已安装版本：

```bash
npx skills update humanizer-zh --global
```

### Claude Code 插件

```text
/plugin marketplace add holygeek00/humanizer-zh-cn
/plugin install humanizer-zh@humanizer-zh-cn
```

### 手动安装

`SKILL.md` 是运行时文件。把仓库克隆到你的技能目录，或只复制 `SKILL.md`：

```bash
git clone https://github.com/holygeek00/humanizer-zh-cn.git /path/to/skills/humanizer-zh
```

安装后请新开会话或重新加载技能。

## 使用方法

直接粘贴文本：

```text
用 $humanizer-zh 去掉下面这段话的 AI 味，保留事实和原意：

[粘贴文本]
```

提供自己的样稿来校准声线：

```text
用 $humanizer-zh 改写。先参考下面两段我以前写的文字，保留我的句长、语气和用词习惯：

[本人样稿]

[待改文本]
```

也可以指定文件。技能会保留代码块、frontmatter、数据和链接目标，只改自然语言正文。

## 33 类中文 AI 写作模式

| # | 模式 | 典型表现 |
|---|---|---|
| 1 | 空泛拔高意义 | “开启新篇章”“具有里程碑意义” |
| 2 | 用名气代替信息 | “多家权威媒体广泛关注” |
| 3 | 句尾伪分析 | “从而提升……进一步赋能……” |
| 4 | 宣传广告腔 | “匠心打造”“震撼来袭” |
| 5 | 模糊归因 | “有专家表示”“研究表明”却无来源 |
| 6 | 挑战与展望模板 | “尽管面临挑战，未来仍可期” |
| 7 | 抽象动词吞掉动作 | 赋能、聚焦、生态、闭环、抓手 |
| 8 | 回避简单判断句 | “定位于”“作为……载体” |
| 9 | 先否后肯滥用 | “不仅是……更是……” |
| 10 | 强凑三点和排比 | 无论内容都分成三项 |
| 11 | 同义词轮换 | 同一对象不断换称呼 |
| 12 | 虚假范围 | “从一杯咖啡到一座城市” |
| 13 | 主体消失 | “已完成”“得到有效提升” |
| 14 | 破折号和括号过密 | 用标点制造戏剧停顿 |
| 15 | 重点标记过多 | 每段机械加粗关键词 |
| 16 | 小标题式清单 | “体验：……性能：……安全：……” |
| 17 | 标题对仗口号化 | “洞察趋势：解码未来” |
| 18 | 表情装饰结构 | 用 🚀💡✅ 代替层级 |
| 19 | 标点混用 | 全角半角混杂、概念滥加引号 |
| 20 | 聊天机器人残留 | “当然可以”“希望对你有帮助” |
| 21 | 免责声明和猜测补洞 | “公开资料有限，因此她可能……” |
| 22 | 讨好和附和 | “你说得太对了” |
| 23 | 冗余套话 | “值得注意的是”“在此基础之上” |
| 24 | 过度限定 | “在某种程度上可能会产生一定影响” |
| 25 | 万能正能量结尾 | “让我们拭目以待”“再创辉煌” |
| 26 | 四字词连用 | “凝心聚力、锐意进取、攻坚克难” |
| 27 | 本质论和权威口吻 | “底层逻辑是”“归根结底” |
| 28 | 预告式开场 | “接下来从三个维度深入探讨” |
| 29 | 标题后重复标题 | 标题下一句只复述标题 |
| 30 | 以修改过程为中心 | 非更新日志反复说新增、优化、调整 |
| 31 | 人造金句和短句连击 | “时代变了。规则变了。” |
| 32 | 空洞比喻 | “数据是灯塔，信任是底色” |
| 33 | 假坦诚反问 | “说实话？答案可能出乎意料” |

完整说明、误伤保护和改写流程见 [SKILL.md](SKILL.md)。

## 与上游相比做了什么

本项目 fork 并改编自 Siqi Chen（GitHub 用户 [blader](https://github.com/blader)）的 [blader/humanizer](https://github.com/blader/humanizer)，不是原作者维护的官方中文版，也不是逐句翻译。主要改动包括：

- 保留上游 33 类框架、声线校准、事实不增补和“初稿 → 审校 → 终稿”流程。
- 将英语特有触发词和例句替换为中文互联网、职场、公文、营销、自媒体常见表达。
- 把英语的 copula、Title Case、连字符等规则改写为中文等价问题，如“定位于”、口号式标题、四字词堆叠和全半角标点混用。
- 增加中文误伤保护，不因一个破折号、正式词汇、列表或正确语法就判定为 AI。
- 不把“赋能”之类的词当作简单禁词，而是检查主体、动作、对象、结果与证据；禁止用同义黑话替换黑话。
- 修正会凭空补充日期、人数、流程或效果的示例；原文缺少细节时明确指出缺失，不伪造“具体感”。
- 使用独立技能名 `humanizer-zh`，避免与原版安装冲突。

详细映射和维护约定见 [LOCALIZATION.md](LOCALIZATION.md)。

## 常见问题

### 这是中文 AI 检测器吗？

不是。它是中文文本改写和审校 Skill，用来处理可观察的写作问题，不判断一段文字究竟由人还是 AI 创作。

### 能降低 AI 检测率或 AIGC 检测率吗？

不承诺。不同检测器的结果不稳定，本项目也不以规避学校、期刊或公司的 AI 使用规定为目标。它解决的是套话、黑话、机械结构和事实漂移。

### 可以处理论文、报告和技术文档吗？

可以审校表达，但会保留术语、数字、引文、代码和真正的不确定性。它不会编造实验结果、参考文献或数据，也不能替代领域审稿。

### ChatGPT、Codex 和 Claude Code 都能用吗？

仓库已验证 Codex 的 Skills CLI 发现和 Claude Code 插件清单。`SKILL.md` 是纯 Markdown，也可以作为指令交给其他支持 Skills 或自定义提示词的 Agent；具体加载方式取决于宿主。

### 支持繁体中文吗？

当前规则和例句主要面向简体中文。繁体文本可以尝试使用，但尚未针对台湾、香港等地区的词汇和语感做系统验证。

## 上游同步

`.github/workflows/sync-upstream.yml` 每周运行一次，也支持手动触发：

1. 拉取 `blader/humanizer` 的 `main` 分支。
2. 如果上游没有新提交，直接结束。
3. 尝试把上游提交合并到本仓库；只有无冲突且本地校验全部通过时，才自动推送到 `main`。
4. 如果发生冲突或校验失败，回滚临时合并并创建带上游提交号、冲突文件和比较链接的 GitHub issue，交由维护者审查。
5. 同一上游提交只创建一个 issue，避免定时任务重复刷屏。

这种策略不会用机器翻译覆盖中文规则，也不会在冲突时强推。详见 [LOCALIZATION.md](LOCALIZATION.md)。

## 版本记录

- **2.9.1-zh.2**：加入“黑话吞掉信息”的诊断框架；按主体、动作、对象、结果和证据还原句子；禁止同义黑话替换；修复首版示例中为追求具体而新增原文事实的问题。
- **2.9.1-zh.1**：基于上游 2.9.1 完成首个简体中文本地化版本；重写 33 类规则与例句；加入中文 README、来源与许可证说明、包校验和每周安全同步。

上游英文版历史见 [blader/humanizer README](https://github.com/blader/humanizer#version-history)。

## 许可证与署名

本项目遵循 [MIT License](LICENSE)。原始版权声明 `Copyright (c) 2025 Siqi Chen` 保持不变。任何复制或重要部分的再分发都应附带该版权与许可声明。

- 原项目：https://github.com/blader/humanizer
- 本地化维护：https://github.com/holygeek00/humanizer-zh-cn

## 反馈与贡献

发现误伤、漏判或新的中文 AI 写作套路，可以[提交 issue](https://github.com/holygeek00/humanizer-zh-cn/issues)。如果这个 Skill 对你有用，欢迎给仓库一个 Star，方便以后找到，也能帮助更多中文写作者发现它。
