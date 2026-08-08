# AGENTS.md

本仓库是 `blader/humanizer` 的简体中文本地化版本。运行时真源是 `SKILL.md`。

## 维护约定

- 保留上游作者 Siqi Chen（blader）的署名、`LICENSE` 和上游链接。
- `SKILL.md`、README 模式表、`.claude-plugin/plugin.json` 必须使用同一版本。
- 技能保持 33 个编号模式。新增、删除或改号时，同步 README 和校验脚本。
- 英语上游变化必须做中文功能等价本地化，不能直接用机器翻译覆盖现有规则。
- 不得在示例中新增“改前”没有的事实，以免教会技能用编造细节换取真人感。
- 安装和使用说明保持跨 Agent 兼容；Claude Code、Codex 等只是示例。
- 非显而易见的规则变化写入 README 版本记录，并在 `LOCALIZATION.md` 说明映射。

## 发布前校验

```bash
python3 scripts/validate-package.py
npx skills add . --list
claude plugin validate .
```
