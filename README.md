# Foreign Trade Industry Researcher

一个给 Codex 使用的外贸行业调研 Skill。它适合用来做产品出海前的国家市场判断，例如：

- 某个产品适不适合某个国家或地区
- 目标市场的需求、应用场景和用户痛点
- 本地品牌、进口品牌、竞品、价格带和渠道
- 关键词、内容生态、客户类型、合规风险和开发策略

这个仓库面向外贸业务员、工厂老板、创业者和正在用 Codex 做市场调研的人。

## Install

复制下面这句话，发给 Codex：

```text
$skill-installer install https://github.com/Haoteng948/foreign-trade-industry-researcher/tree/main/foreign-trade-industry-researcher
```

安装完成后，重启 Codex。

## Test Prompt

安装后，可以用这些话测试：

```text
用外贸行业调研 skill，帮我研究德国防霉硅酮胶市场。
```

```text
Use foreign-trade-industry-researcher to research whether kitchen sinks are suitable for the Saudi market.
```

```text
帮我做一个美国宠物清洁用品市场的外贸开发前调研。
```

## What It Produces

这个 Skill 会尽量把调研结果整理成一个 `Industry-Landscape` 文件夹，包括：

- 行业总览与开发结论
- 行业地图与需求结构
- 产品类型与规格
- 应用场景与用户痛点
- 品牌与竞品数据库
- 进口贸易与供应链
- 价格带与销售渠道
- 关键词与买家搜索习惯
- 内容生态与流量渠道
- 商业模式与客户类型
- 认证、关税、合规
- 进入风险
- 机会地图与开发策略
- 信息源清单
- 后续验证任务

## Important Notes

- 这个 Skill 不是普通文档，要安装到 Codex 里使用。
- 它会要求 Codex 做联网检索，所以调研质量取决于公开信息是否充足。
- 市场规模、进口数据、认证、关税等结论必须标注来源和可信度；无法确认的内容要写成“待验证”。
- 它不替代律师、报关行、认证机构或当地渠道访谈。

## Repository Structure

```text
foreign-trade-industry-researcher/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── execution-sop.md
│   └── source-policy.md
└── scripts/
    └── scaffold_industry_os.py
```

