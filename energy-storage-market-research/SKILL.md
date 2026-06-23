---
name: energy-storage-market-research
description: Conduct source-backed country or regional market research for an energy-storage pack manufacturer, covering energy-storage batteries, photovoltaic products, inverters, applications, customer pain points, competitors, channels, certification, logistics, and market-entry actions. Use for 储能国别市场调研, 光伏市场分析, 逆变器市场调研, 储能电池出海, 某国储能市场, country energy-storage market analysis, battery storage market research, PV market landscape, inverter market research, or export-market assessment. Produce a repeatable local research folder when a country or region is specified. Do not use for individual customer due diligence, a live monitoring service, or a generic global overview with no target market.
---

# Energy Storage Market Research

## Goal

Turn a country/region and product request into a decision-ready, source-backed market landscape for an energy-storage pack manufacturer. Cover battery storage, PV, and inverters as one system, then recommend market entry, product configuration, and validation priorities.

## Normalize the Brief

Extract or ask only for information needed to avoid a material error:

- `market`: country or region; default `全球` only for an explicitly global request.
- `focus`: `all` (default), `residential`, `C&I`, `utility`, `off-grid/microgrid`, or a stated product.
- `depth`: `quick_scan` (default) or `deep_research`.
- `report_date`: today.
- `output_root`: `./<market>-Energy-Storage-Market-Landscape` unless the user specifies a path.
- `decision`: market screening, distributor recruitment, project bidding, product localization, or entry plan.

State any assumption in `00-项目说明.md`. Do not assume grid voltage, certification requirements, tariff rates, storage deployment, or prices from another country.

## Create the Deliverable

For a local deliverable, run the bundled scaffold before researching:

```bash
python "<skill-folder>/scripts/scaffold_energy_market.py" "<market>" --focus "<focus>" --depth quick_scan --root "<absolute-output-root>"
```

Use the generated folder as the single source of truth. Keep facts, estimates, hypotheses, and unknowns distinct. Add a source URL, publication date/year, access date, and confidence (`high`/`medium`/`low`) to every material claim.

Read [references/execution-playbook.md](references/execution-playbook.md) for the report structure and acceptance criteria. Read [references/source-policy.md](references/source-policy.md) before web research or writing claims. Read [references/product-fit-matrix.md](references/product-fit-matrix.md) when specifying products or localization.

## Research Workflow

1. Establish the market baseline: macroeconomy, electricity system, renewable build-out, solar resource/climate, grid constraints, prices, and storage policy.
2. Segment demand by residential, C&I, utility, and off-grid/microgrid. Identify the economic trigger and the buyer's operational pain point for each relevant segment.
3. Map the local offer: active battery, inverter, PV, EMS, and integrated-system brands; local distributors; installers/EPCs; developers; utilities; and their visible products, prices, service coverage, and channel evidence.
4. Convert country conditions into a pack-factory product brief: battery voltage/platform, usable capacity, C-rate, enclosure/IP/corrosion/thermal requirements, inverter interoperability, BMS/EMS communications, safety architecture, certifications, documentation, and warranty/service expectations.
5. Assess import, compliance, logistics, after-sales, financing, currency, payment, and project-bankability risks. Separate legal requirements from customer preferences.
6. Score segments and entry routes using the decision matrix. Recommend only actions supported by evidence; otherwise define the smallest validation test.
7. Perform the quality gate in the playbook and update `13-信息源与证据清单.md` plus `_sources/source-log.md`.

## Pack Manufacturer Lens

Prioritize findings that change product, commercial, or channel decisions:

- **System compatibility:** local AC voltage/frequency/phases, grid codes, inverter brands/protocols, PV coupling mode, and backup/off-grid requirements.
- **Battery design:** LFP/NMC preference, low-temperature charging, high-temperature derating, altitude, dust, humidity, salt mist, seismic/fire requirements, indoor/outdoor installation, and transport classification.
- **Commercial fit:** MOQ, container utilization, local stock expectation, target price band, warranty reserve, spare parts, installer training, remote diagnostics, and local-language documents.
- **Route to market:** distributor versus EPC/developer versus direct project sales; procurement cycles; tender/prequalification; credit and payment terms.

Do not present a competitor's claimed specification as independently verified. Do not equate announced projects, pipeline capacity, or import shipments with operational installed capacity.

## Evidence and Research Rules

- Browse for all time-sensitive facts. Prefer regulators, grid operators, customs/trade data, standards bodies, government statistics, utility filings, company product documents, and tender/project documents.
- Use distributor and marketplace pages to validate visible SKU, price, availability, and channel—not market size or share.
- Use local-language reviews, installer forums, service tickets, and public social/video discussions to identify pain points; record sample limitations.
- Verify each core competitor with at least two independent evidence types where available: official product/documentation plus a local channel, project, certification, or tender source.
- Do not invent market size, CAGR, pricing, certification status, rankings, or customer lists. Mark unverified claims `待验证`.
- Cite exact dates and currency basis. For prices, record tax/shipping status, seller, product configuration, and observation date.

## Completion Standard

Finish with only the saved folder path, the market-entry conclusion, the three highest-impact findings, the three principal risks/unknowns, and the next validation actions. Keep the conclusion conditional when evidence is incomplete.
