#!/usr/bin/env python3
"""Create an Obsidian-ready Industry Landscape scaffold."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re


LANDSCAPE_FILES = [
    ("00-行业总览与开发结论.md", "行业总览与开发结论"),
    ("01-行业地图与需求结构.md", "行业地图与需求结构"),
    ("02-产品类型与规格.md", "产品类型与规格"),
    ("03-应用场景与用户痛点.md", "应用场景与用户痛点"),
    ("04-品牌与竞品数据库.md", "品牌与竞品数据库"),
    ("05-进口贸易与供应链.md", "进口贸易与供应链"),
    ("06-价格带与销售渠道.md", "价格带与销售渠道"),
    ("07-关键词与买家搜索习惯.md", "关键词与买家搜索习惯"),
    ("08-内容生态与流量渠道.md", "内容生态与流量渠道"),
    ("09-商业模式与客户类型.md", "商业模式与客户类型"),
    ("10-认证关税合规.md", "认证关税合规"),
    ("11-进入风险.md", "进入风险"),
    ("12-机会地图与开发策略.md", "机会地图与开发策略"),
    ("13-信息源清单.md", "信息源清单"),
    ("14-后续验证任务.md", "后续验证任务"),
]


def safe_name(value: str) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|]+", "-", value.strip())
    cleaned = re.sub(r"\s+", "-", cleaned)
    return cleaned.strip("-") or "Industry"


def frontmatter(subject: str, market: str, research_date: str, depth: str) -> str:
    return (
        "---\n"
        "mode: industry_landscape\n"
        f"industry: {subject}\n"
        f"market: {market}\n"
        f"research_date: {research_date}\n"
        f"depth: {depth}\n"
        "status: draft\n"
        "confidence: low\n"
        "---\n\n"
    )


def landscape_template(title: str, subject: str, market: str, research_date: str, depth: str) -> str:
    if title == "应用场景与用户痛点":
        return (
            frontmatter(subject, market, research_date, depth)
            + f"# {title}\n\n"
            + "## 结论摘要\n\n"
            + "## 数据源门槛\n\n"
            + "- 按 `references/source-policy.md`：5 条本地反馈信号、3 条本地公开社媒/论坛/教程信号、3 条海外通用品类痛点信号；无法访问时记录失败路径。\n\n"
            + "## 应用场景\n\n"
            + "## 本地语言痛点抓取\n\n"
            + "| 平台 | 原始反馈 / 公开信号 | 中文解释 | 场景 | 痛点类型 | 对应产品机会 | 来源 | 可信度 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 海外电商与社媒痛点抓取\n\n"
            + "| 平台 | 原始反馈 / 公开信号 | 中文解释 | 场景 | 痛点类型 | 对应产品机会 | 来源 | 可信度 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 抓取关键词\n\n"
            + "## 证据来源\n\n"
            + "## 不确定信息\n\n"
            + "| Required source | Search path / keywords tried | Result | Substitute source used | Remaining risk |\n"
            + "| --- | --- | --- | --- | --- |\n\n"
            + "## 下一步\n"
        )
    if title == "品牌与竞品数据库":
        return (
            frontmatter(subject, market, research_date, depth)
            + f"# {title}\n\n"
            + "## 结论摘要\n\n"
            + "## 数据源门槛\n\n"
            + "- 按 `references/source-policy.md`：至少 8 个可见品牌；核心品牌尽量验证 3 类证据：官网/产品页、TDS/SDS/技术文件、电商/经销商/价格/包装线索。\n\n"
            + "## 竞品首次验证表\n\n"
            + "| 品牌 | 本土/进口 | 是否疑似自有生产 | 证据 | 渠道覆盖 | SKU/价格/评论信号 | 可信度 | 仍缺什么 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 渠道存在感估算\n\n"
            + "| 品牌 | 可见平台数 | SKU 数 | 评论/评分信号 | 价格带覆盖 | 经销商/门店信号 | 渠道存在感 | 说明 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 中国供应切入判断\n\n"
            + "## 验证关键词\n\n"
            + "## 证据来源\n\n"
            + "## 不确定信息\n\n"
            + "| 问题 | 已查路径 | 结果 | 下一步验证动作 |\n"
            + "| --- | --- | --- | --- |\n\n"
            + "## 下一步\n"
        )
    if title == "内容生态与流量渠道":
        return (
            frontmatter(subject, market, research_date, depth)
            + f"# {title}\n\n"
            + "## 结论摘要\n\n"
            + "## 数据源门槛\n\n"
            + "- 按 `references/source-policy.md`：quick_scan 至少 20 条本地产品页/SKU 标题、8 条施工教程/视频/社媒标题；deep_research 至少 50 条 SKU 标题、20 条教程/社媒标题。\n\n"
            + "## 流量渠道地图\n\n"
            + "| 渠道 | 内容形态 | 用户意图 | 代表来源 | 对外贸开发的意义 | 可信度 |\n"
            + "| --- | --- | --- | --- | --- | --- |\n\n"
            + "## 本地产品页 / SKU 标题样本\n\n"
            + "| 平台 | 原始标题 | 中文解释 | 品牌 | 场景/用途 | 卖点词 | 链接 | 可信度 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 施工教程 / 社媒标题样本\n\n"
            + "| 平台 | 原始标题 | 中文解释 | 场景 | 用户意图 | 可转化内容角度 | 链接 | 可信度 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 高频内容卖点归纳\n\n"
            + "| 高频卖点 | 出现位置 | 买家/用户意图 | 外贸可用表达 | 可做内容/SEO 页面 |\n"
            + "| --- | --- | --- | --- | --- |\n\n"
            + "## 证据来源\n\n"
            + "## 不确定信息\n\n"
            + "| Required source | Search path / keywords tried | Result | Substitute source used | Remaining risk |\n"
            + "| --- | --- | --- | --- | --- |\n\n"
            + "## 下一步\n"
        )
    if title == "信息源清单":
        return (
            frontmatter(subject, market, research_date, depth)
            + f"# {title}\n\n"
            + "## 结论摘要\n\n"
            + "## 数据源门槛\n\n"
            + "- 按 `references/source-policy.md`：从 `_sources/source-log.md` 回收本次实际来源；quick_scan 目标 15+ 条来源记录，deep_research 目标 40+ 条来源记录；不足时解释缺口。\n\n"
            + "## 信息源数据库\n\n"
            + "| 类别 | 信息源 | 链接 | 主要回答什么 | 支撑文件 | 可信度 | 使用限制 | 下一步抓取 |\n"
            + "| --- | --- | --- | --- | --- | --- | --- | --- |\n\n"
            + "## 来源用途矩阵\n\n"
            + "| 研究问题 | 优先来源 | 辅助来源 | 不该用什么来源下结论 |\n"
            + "| --- | --- | --- | --- |\n\n"
            + "## 更新频率\n\n"
            + "| 信息类型 | 更新频率 | 触发条件 | 负责人动作 |\n"
            + "| --- | --- | --- | --- |\n\n"
            + "## 信息缺口\n\n"
            + "| 缺口 | 当前替代来源 | 为什么还不够 | 下一步验证 |\n"
            + "| --- | --- | --- | --- |\n\n"
            + "## 证据来源\n\n"
            + "## 不确定信息\n\n"
            + "## 下一步\n"
        )
    return (
        frontmatter(subject, market, research_date, depth)
        + f"# {title}\n\n"
        + "## 结论摘要\n\n"
        + "## 数据源门槛\n\n"
        + "- 按 `references/source-policy.md` 执行本文件最低来源类型和样本数量；如果无法满足，必须在“不确定信息”记录失败检索路径和替代来源。\n\n"
        + "## 核心信息\n\n"
        + "## 证据来源\n\n"
        + "## 不确定信息\n\n"
        + "| Required source | Search path / keywords tried | Result | Substitute source used | Remaining risk |\n"
        + "| --- | --- | --- | --- | --- |\n\n"
        + "## 下一步\n"
    )


def source_log_template(subject: str, market: str, research_date: str, depth: str) -> str:
    return (
        frontmatter(subject, market, research_date, depth)
        + "# Source Log\n\n"
        + "| Date | Claim / Topic | Source | Source Type | Confidence | Notes |\n"
        + "| --- | --- | --- | --- | --- | --- |\n\n"
        + "## Failed / Unavailable Source Attempts\n\n"
        + "| Date | Required source | Search path / keywords tried | Result | Substitute source used | Remaining risk |\n"
        + "| --- | --- | --- | --- | --- | --- |\n"
    )


def source_quality_template(subject: str, market: str, research_date: str, depth: str) -> str:
    return (
        frontmatter(subject, market, research_date, depth)
        + "# Source Quality\n\n"
        + "## High Confidence\n\n"
        + "- Official websites\n"
        + "- Financial filings\n"
        + "- Government or regulator sources\n"
        + "- Industry associations\n"
        + "- Trade data from official or reputable databases\n"
        + "- Multiple independent sources agreeing\n\n"
        + "## Medium Confidence\n\n"
        + "- Reputable industry media\n"
        + "- Research reports with visible methodology\n"
        + "- Platform public data\n"
        + "- Local ecommerce and distributor listings\n"
        + "- Company interviews\n\n"
        + "## Low Confidence\n\n"
        + "- Single articles\n"
        + "- Social rumors\n"
        + "- Unverified blogs\n"
        + "- AI inference\n\n"
        + "## Required Practice\n\n"
        + "- Separate facts, estimates, guesses, and unknowns.\n"
        + "- Mark unsourced claims as 待验证.\n"
        + "- Include publication year or retrieval date when freshness matters.\n"
        + "- Enforce `references/source-policy.md`: meet each file's source gate or record failed-source paths.\n"
    )


def write(path: Path, content: str, force: bool) -> bool:
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def output_dir(args: argparse.Namespace) -> Path:
    if args.output_root:
        return Path(args.output_root).expanduser().resolve()
    return Path(args.root).expanduser().resolve() / f"{safe_name(args.subject)}-Industry-Landscape"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an industry landscape folder scaffold.")
    parser.add_argument("subject", help="Industry subject, e.g. 美国减肥补充剂行业 or 希腊硅酮密封胶行业")
    parser.add_argument("--market", default="全球", help="Target market or region")
    parser.add_argument("--root", default=".", help="Parent output directory")
    parser.add_argument("--output-root", default=None, help="Exact output directory path")
    parser.add_argument("--date", default=date.today().isoformat(), help="Research date")
    parser.add_argument("--depth", default="quick_scan", choices=["quick_scan", "deep_research"])
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    args = parser.parse_args()

    target = output_dir(args)
    created = 0
    skipped = 0

    for filename, title in LANDSCAPE_FILES:
        did_write = write(
            target / filename,
            landscape_template(title, args.subject, args.market, args.date, args.depth),
            args.force,
        )
        created += int(did_write)
        skipped += int(not did_write)

    source_files = [
        ("source-log.md", source_log_template(args.subject, args.market, args.date, args.depth)),
        ("source-quality.md", source_quality_template(args.subject, args.market, args.date, args.depth)),
    ]
    for filename, content in source_files:
        did_write = write(target / "_sources" / filename, content, args.force)
        created += int(did_write)
        skipped += int(not did_write)

    if args.depth == "deep_research":
        for dirname in ["15-竞品网站拆解", "16-爆款内容拆解"]:
            (target / dirname).mkdir(parents=True, exist_ok=True)

    print(f"Research folder: {target}")
    print(f"Created files: {created}")
    print(f"Skipped existing files: {skipped}")


if __name__ == "__main__":
    main()
