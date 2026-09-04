# UXYS — User eXperience Yield System

> **面向 AI Agent 的意图优先 UX 分析方法。**
>
> UXYS 教会 LLM 把界面理解为由用户意图、证据、最短充分路径、摩擦与目标状态组成的网络，而不是输出一套通用的 UX 检查清单。

[![Version](https://img.shields.io/badge/version-0.1.1-2f6feb?style=flat-square)](VERSION)
[![Skill validation](https://github.com/Muredsa/UXYS/actions/workflows/validate.yml/badge.svg)](https://github.com/Muredsa/UXYS/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Codex Skill](https://img.shields.io/badge/Codex-SKILL.md-111827?style=flat-square)](SKILL.md)
<a href="https://www.claudemarket.ai/skills"><img src="https://www.claudemarket.ai/badge-claudemarket.svg" alt="Listed on Claude Market" width="190" height="44" /></a>

[English](README.md) · [Русский](README.ru.md) · **简体中文**

---

## UXYS 改变了什么

常见的 AI UX 审核很容易回到熟悉的建议：让 CTA 更醒目、减少杂乱、改善层级、增加信任元素、简化导航。

UXYS 改变的不是建议列表，而是**分析方式本身**。

```text
INTENT
  ↓
EVIDENCE
  ↓
SHORTEST SUFFICIENT ROUTE
  ↓
FRICTION
  ↓
DESTINATION
```

页面不会被视为只服务一个“理想用户”的单一路径。不同访客在行动之前需要不同程度的解释、证明和风险消除。因此，同一个区块对某个意图可能是必要的，对另一个意图只是辅助，而对已经准备行动的用户则可能形成干扰。

目标不是“删掉所有不必要的内容”。目标是让页面成为一个**由多个短而充分、并且彼此尽量少干扰的用户路径组成的网络**。

## 这个 Skill 会做什么

启用 UXYS 后，Agent 应当：

- 推断多个合理的访客意图，但不虚构这些意图在真实流量中的占比；
- 为每个意图定义明确的 destination；
- 在评价当前页面之前，先推导该意图的最短充分语义路径；
- 将页面真实区块映射到这些路径；
- 区分 necessary / supporting / optional / diversion / harmful / destination / missing；
- 区分注意力转移、语义转移和真实可执行动作；
- 在建议删除区块之前，先评估它对**所有重要意图**的整体价值；
- 对删除、移动、减弱、增强、合并或折叠区块进行反事实推演；
- 输出简单的区块级结论：**KEEP / EMPHASIZE / ADJUST / DE-EMPHASIZE / MOVE / REMOVE / ADD**；
- 始终区分预测行为与真实观测数据，不把模型判断包装成眼动追踪结果。

完整的可执行方法位于 [`SKILL.md`](SKILL.md)，补充规则位于 [`references/`](references/)。

## 在 Codex 中安装

将整个仓库克隆到 Codex 的 skills 目录。

### macOS / Linux

```bash
git clone https://github.com/Muredsa/UXYS.git ~/.codex/skills/uxys
```

### Windows PowerShell

```powershell
git clone https://github.com/Muredsa/UXYS.git "$env:USERPROFILE\.codex\skills\uxys"
```

如果 Skill 没有立即出现，请重启或重新打开 Codex。

## 更新

因为 Skill 本身就是一个 Git 仓库，所以更新只需要 `pull`。

### macOS / Linux

```bash
git -C ~/.codex/skills/uxys pull --ff-only
```

### Windows PowerShell

```powershell
git -C "$env:USERPROFILE\.codex\skills\uxys" pull --ff-only
```

进行重要更新前请先查看 [`CHANGELOG.md`](CHANGELOG.md)。

## 版本规则

UXYS 使用 Semantic Versioning：

- **PATCH** — 不改变方法核心逻辑的修正和澄清；
- **MINOR** — 向后兼容的新分析能力；
- **MAJOR** — 对核心推理模型或 Skill 行为的不兼容修改。

在 `0.x` 阶段，UXYS 仍被视为实验性方法，可能快速演进。当前版本记录在 [`VERSION`](VERSION)。

## 工具增强方法，但不定义方法

UXYS 首先是一套推理方法。当宿主 Agent 具备工具时，它会更强：

- **浏览器** — 检查真实页面、桌面/移动端和交互状态；
- **截图 / Vision** — 判断视觉层级和注意力竞争；
- **DOM / 源码** — 验证真实交互、结构和标签；
- **图像编辑** — 快速制作反事实设计版本；
- **代码编辑** — 实现选中的版本并重新验证；
- **分析数据** — 将 predicted routes 与 observed behavior 分开比较。

如果某项工具不可用，Skill 应降低结论置信度，而不是猜测不存在的数据。

## 这不是 Eye-tracking

UXYS 生成的是**预测性 UX 推理**。没有真实观测数据时，不能声称“73% 的用户会看这里”，也不能虚构转化提升。可以说某个元素“很可能竞争注意力”，但必须说明依据。

## 仓库结构

```text
UXYS/
├── SKILL.md                       # Agent / Codex 入口
├── references/                    # 核心方法与工作协议
├── evals/cases.md                 # 方法回归用例
├── scripts/validate_skill.py      # 无依赖校验器
├── README.md                      # English
├── README.ru.md                   # Русский
├── README.zh-CN.md                # 简体中文
├── VERSION
└── CHANGELOG.md
```

`SKILL.md` 和 `references/` 是唯一的规范实现，统一使用英语维护，以避免三个可执行版本逐渐产生差异。Agent 输出分析时应默认使用用户的语言。

## 参与贡献

UXYS 是一套有明确立场的方法，而不是不断扩张的检查清单。一个改动应该让分析更可靠、更可解释，或者更不容易退化成通用 UX 建议。

请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)。修改核心方法时，应新增或更新对应的 eval case。

## 适用范围

Landing page、SaaS、电子商务、Dashboard、Onboarding、Checkout、表单、内容页面以及其他视觉交互流程。

## License

MIT — [`LICENSE`](LICENSE)。

---

**关键词：** UX、UX analysis、UX audit、user journey、intent modeling、interaction design、conversion、LLM、AI agent、Codex、prompt engineering、vision、web design、HCI、counterfactual UX、design critique。
