---
name: foreign-trade-industry-researcher
description: Research foreign-trade product and target-country markets with source-backed industry landscape folders. Use when Codex needs to judge whether a product is suitable for a country or region, map demand, competitors, prices, channels, keywords, customers, compliance, risks, and development actions. Trigger for 外贸行业调研, 外贸市场调查, 产品出海市场调查, 某产品适不适合某国家, 客户开发前调研, 竞品数据库, product-market research, export market research, country market landscape, and industry landscape. Do not use for individual customer due diligence, viral content ecosystem research, or ongoing monitoring.
---

# Foreign Trade Industry Researcher

## Goal

Turn a foreign-trade industry, product, country, or product-country request into one source-backed `Industry-Landscape` research folder.

There is only one output mode: `industry_landscape`. When the request contains a product plus a country or region, treat it as that country's product industry landscape and include the development judgment inside the same folder.

## Routing

Use this skill for:

- `德国防霉硅酮胶市场`
- `硅酮密封胶适不适合希腊市场`
- `建筑密封胶在沙特市场怎么样`
- `美国宠物清洁用品市场`
- `kitchen sinks in Saudi Arabia`
- `export market research for bathroom cabinets in the UK`

Normalize the research subject as:

- Broad industry: `<industry>`
- Product plus country/region: `<market><product>行业`

Example: `硅酮密封胶适不适合希腊市场` becomes `希腊硅酮密封胶行业`.

Do not run company authenticity or customer identity due diligence in this skill. Keep the work focused on industry structure, product-market demand, channels, competition, compliance, opportunity, and development actions.

Do not use this skill for batch content ecosystem research, viral-topic databases, creator/account databases, or ongoing intelligence monitoring.

## Quick Workflow

1. Normalize inputs:
   - `mode`: always `industry_landscape`
   - `subject`: industry or normalized product-country industry
   - `market`: country/region if present, otherwise `全球`
   - `research_date`: today's date
   - `depth`: `quick_scan` or `deep_research`, default `quick_scan`
   - `output_root`: `./<subject>-Industry-Landscape`
2. Locate this skill's folder from the current `SKILL.md` path. Use the bundled scaffold script when writing local outputs:
   ```bash
   python3 "<skill-folder>/scripts/scaffold_industry_os.py" "<subject>" --market "<market>" --root "/absolute/output/folder"
   ```
3. Read `references/source-policy.md` before writing local outputs. Use web research for current or factual claims and prefer primary or high-trust sources.
4. Fill one unified output structure:
   - market overview and development conclusion
   - industry map and demand structure
   - products, specs, application scenarios, and local-language user pain points
   - brands, competitors, imports, prices, and channels
   - keywords, basic traffic channels, business models
   - customer types, certification, tariffs, risks
   - opportunity map, development strategy, validation tasks
5. End with only:
   - saved path
   - 3 most important findings
   - 3 most important follow-up questions
   - data confidence risks

## Research Rules

- Allow free searching, but enforce the minimum evidence gates in `references/source-policy.md`. Do not write hard conclusions until the required source types are found or failed-source paths are recorded.
- Separate facts, estimates, guesses, and unknowns.
- Every important claim needs a source link, date or year, and confidence level.
- Mark unsourced or single-source claims as `待验证` or `推测`.
- Do not invent rankings, market sizes, growth rates, or Top lists.
- When the user asks for latest, current, fastest-growing, biggest, or Top results, browse and cite current sources.
- Prefer official websites, filings, regulators, industry associations, platform pages, public marketplaces, trade data, and reputable research/media.
- Use Reddit, reviews, comments, forums, and social content for pain points, not for hard market-size claims.
- For `03-应用场景与用户痛点.md`, actively search local-language ecommerce reviews, overseas ecommerce reviews, forum posts, Reddit, X/Twitter, YouTube/video comments, TikTok, Instagram, public Facebook posts/groups, and Q&A pages. Do not leave pain points as a generic “待验证” note unless no public sources are accessible.
- For `04-品牌与竞品数据库.md`, run a first-pass competitor verification before writing conclusions. For every core brand, look for at least three evidence types when available: official product/company page, TDS/SDS/DoP/CE/EN documents, local ecommerce or distributor SKU pages, packaging/label/EAN/importer clues, visible prices, review counts, and channel coverage.
- Treat true sales share as usually unavailable from public pages. Use proxy signals instead: SKU count, number of visible channels, distributor pages, review volume, price-band coverage, Google visibility, and whether the brand appears on mainstream retail/building-material platforms.
- For `08-内容生态与流量渠道.md`, collect product-page titles/SKU titles, tutorial/video/social titles, and competitor content angles during the first pass. Quick-scan minimums: 20 product/SKU titles and 8 tutorial/social titles. Deep-research targets: 50 product/SKU titles and 20 tutorial/social titles.
- For `13-信息源清单.md`, build a reusable source database from `_sources/source-log.md`: categorize sources by use case, link them to the files they support, mark confidence and limitations, and define refresh cadence plus next crawl actions.

## When To Read The Full SOP

Read `references/execution-sop.md` and `references/source-policy.md` when:

- the user explicitly says “按 SOP 执行”;
- the output must be written to local files;
- the user wants repeatable industry research, not a short answer;
- the request contains a product in a target country/region;
- you need exact phase prompts, templates, validation checks, or deep-research extensions.

## File Creation

Use the scaffold script whenever possible. It creates the stable folder structure and frontmatter templates.

```bash
python3 "<skill-folder>/scripts/scaffold_industry_os.py" "德国防霉硅酮胶行业" --market "德国" --root "/absolute/output/folder"
python3 "<skill-folder>/scripts/scaffold_industry_os.py" "沙特建筑密封胶行业" --market "沙特" --root "/absolute/output/folder"
```

If the script is unavailable, create the same structure manually from `references/execution-sop.md`.

