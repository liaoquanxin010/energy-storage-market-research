# Foreign Trade Industry Research Source Policy

> 目标：允许自由检索，但不允许自由下结论。不要写死具体网站；要写死每个文件的最低证据门槛、失败记录和 source-log 追溯，适用于外贸产品、国家市场和客户开发前调研。

## 1. Core Rule

```text
自由检索：允许
自由选择来源：允许
自由下结论：不允许
跳过来源验证：不允许
找不到信息：允许
装作找到了：不允许
```

Every important claim must trace to `_sources/source-log.md`. If a source type is unavailable, record the attempted path and the substitute source used.

## 2. Source Type Codes

Use these source categories in notes and source-log:

| Code | Source type | Examples | Can support hard claims? |
| --- | --- | --- | --- |
| TRADE | Trade / customs data | WITS, UN Comtrade, Eurostat, national customs, paid bill-of-lading data | Yes, with HS-code caveats |
| GOV | Government / regulator | statistics offices, ministries, customs portals, tariff portals | Yes |
| ASSOC | Industry association | construction associations, chamber reports, official sector reports | Yes, if methodology is clear |
| BRAND | Brand / manufacturer official | company page, product page, catalog | Product facts yes; market share no unless independently verified |
| TECH | Technical files | TDS, SDS, DoP, CE/EN documents, test reports | Yes for specs/compliance |
| PLATFORM | Ecommerce / marketplace / retailer | local marketplace, building-material retailer, distributor SKU page | Price/channel signal only |
| REVIEW | Reviews / Q&A / comments | ecommerce reviews, forum posts, public video comments, Reddit | Pain-point signal only |
| SOCIAL | Public social/video content | YouTube, TikTok, Instagram, Facebook public pages | Content/pain signal only |
| DIRECTORY | B2B directory / yellow pages | supplier directories, Google Maps, trade fair lists | Lead signal only |
| MEDIA | Reputable media / research report | trade media, commercial market reports | Directional unless methodology is visible |
| INTERVIEW | Customer or channel interview | distributor call, seller reply, broker answer | Strong signal; record date and role |

## 3. Minimum Evidence Gates By File

These are minimums for `quick_scan`. For `deep_research`, double the sample counts where practical. If the market is small or public data is sparse, the file may use fewer sources only after recording failed search paths.

| File | Required source mix | Minimum sample gate | Must not do |
| --- | --- | --- | --- |
| `00-行业总览与开发结论.md` | TRADE or GOV; macro demand source; competitor/channel signals | 1 trade/stat source + 1 demand source + 3 competitor/channel sources | Do not use a brand claim as market size or market share |
| `01-行业地图与需求结构.md` | GOV/ASSOC/MEDIA demand sources; local industry/channel sources | 2 demand/industry sources + 2 application/channel sources | Do not infer demand only from product listings |
| `02-产品类型与规格.md` | BRAND/TECH/product pages; PLATFORM SKU examples | 3 brand/technical sources + 5 SKU/spec examples | Do not invent specs or standards |
| `03-应用场景与用户痛点.md` | Local REVIEW/Q&A; SOCIAL/forum/video; overseas category reviews as backup | 5 local feedback signals + 3 local public social/forum/tutorial signals + 3 overseas category pain signals | Do not write generic pain points without public signals |
| `04-品牌与竞品数据库.md` | BRAND, TECH, PLATFORM, distributor pages, packaging/label clues | At least 8 brands when visible; each core brand needs 3 evidence types when available | Do not label a brand OEM/self-produced without evidence |
| `05-进口贸易与供应链.md` | TRADE, HS/tariff, importer/distributor/supply-chain signals | 1 trade source + 1 HS/tariff source + 3 supply-chain/channel signals | Do not treat HS6 data as pure product volume |
| `06-价格带与销售渠道.md` | Local PLATFORM/retailer/distributor prices; channel pages | 10 price/SKU samples + 2 channel types | Do not treat promo retail price as wholesale price |
| `07-关键词与买家搜索习惯.md` | Local-language search titles, ecommerce titles, brand/category terms, B2B terms | 10 local-language terms + 10 product/title signals + 5 B2B/export terms | Do not translate English keywords mechanically |
| `08-内容生态与流量渠道.md` | Product/SKU titles; tutorial/video/social titles; competitor content | 20 SKU/product titles + 8 tutorial/social titles | Do not leave title collection for “next step” |
| `09-商业模式与客户类型.md` | Distributor pages, directories, ecommerce sellers, brand channel pages, interviews if available | 5 customer/channel sources + at least 4 customer types | Do not invent margins or monthly volumes |
| `10-认证关税合规.md` | GOV/regulator/tariff portals; TECH/SDS/TDS competitor docs; broker confirmation if available | 2 official/regulatory sources + 2 competitor technical docs | Do not give final tariff/legal advice without broker verification |
| `11-进入风险.md` | Evidence from price, pain points, compliance, competitor, channel files | At least 5 risks traced to source files or source-log entries | Do not list generic risks unrelated to evidence |
| `12-机会地图与开发策略.md` | Synthesis from files 00-11 plus direct customer/channel evidence when available | Every priority opportunity must cite its evidence base | Do not recommend a strategy that contradicts evidence gaps |
| `13-信息源清单.md` | `_sources/source-log.md` plus source quality notes | Quick scan target: 15+ source-log entries; deep research target: 40+ | Do not output a plain link list |
| `14-后续验证任务.md` | All uncertainty sections and failed source paths | Convert every major uncertainty into a validation task | Do not add vague “continue research” tasks without owner/action/output |

## 4. Failed Source Protocol

When a required source type cannot be accessed, write a failed-source record in the relevant file:

```markdown
| Required source | Search path / keywords tried | Result | Substitute source used | Remaining risk |
| --- | --- | --- | --- | --- |
```

Examples:

- If local ecommerce reviews are inaccessible, record the marketplaces searched, the product keywords, and whether login/dynamic pages blocked review access.
- If tariff data cannot be confirmed, record the official portals checked and require customs-broker verification.
- If a brand's TDS/SDS is unavailable, record the official site/product pages checked and use distributor/product pages only as weaker evidence.

## 5. Source-Log Requirements

Every source-log entry should answer:

```text
Date | Claim / Topic | Source | Source Type | Confidence | Notes
```

Rules:

- Record sources as they are used, not after the report is finished.
- Each important conclusion in `00`, `04`, `05`, `10`, and `12` should trace to source-log.
- Source-log may include “failed source attempts” when the attempted path matters.
- Do not cite search-result snippets as final evidence unless the page itself is inaccessible and the limitation is stated.

## 6. Anti-Laziness Self-Check

Before final response, verify:

- Each正文 file has `结论摘要`, `证据来源`, `不确定信息`, and `下一步`.
- Each正文 file meets its minimum source gate or records failed-source paths.
- `03`, `04`, and `08` include sample tables, not only summary prose.
- `13` turns the source-log into a reusable database, not a bullet list.
- Hard claims use hard sources; soft sources are only used for pain points, channel signals, and content angles.
- Unknowns are written as `待验证` with next verification action.
