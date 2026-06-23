#!/usr/bin/env python3
"""Create a stable country-market research folder for this skill."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


FILES = [
    "00-项目说明.md", "01-执行摘要与市场判断.md", "02-国家能源与电力基础.md",
    "03-政策法规与准入.md", "04-需求场景与客户痛点.md", "05-市场规模与项目管线.md",
    "06-产品与技术偏好.md", "07-价格与商业模式.md", "08-品牌竞品与解决方案.md",
    "09-渠道客户与关键参与方.md", "10-区域与物流落地.md", "11-风险与合规清单.md",
    "12-进入策略与验证计划.md", "13-信息源与证据清单.md",
]


def write_if_missing(path: Path, title: str, market: str, focus: str, depth: str) -> None:
    if path.exists():
        return
    path.write_text(
        f"# {title.removesuffix('.md')}\n\n"
        f"- 市场：{market}\n- 焦点：{focus}\n- 深度：{depth}\n- 创建日期：{date.today().isoformat()}\n\n"
        "## 待研究\n\n- 待填充；每项关键事实需附来源、日期和置信度。\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an energy-storage country-market research folder.")
    parser.add_argument("market", help="Country or region")
    parser.add_argument("--focus", default="all")
    parser.add_argument("--depth", choices=("quick_scan", "deep_research"), default="quick_scan")
    parser.add_argument("--root", required=True, help="Absolute or relative output folder")
    args = parser.parse_args()

    root = Path(args.root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    for filename in FILES:
        write_if_missing(root / filename, filename, args.market, args.focus, args.depth)

    source_dir = root / "_sources"
    source_dir.mkdir(exist_ok=True)
    log = source_dir / "source-log.md"
    if not log.exists():
        log.write_text(
            "# Source Log\n\n| 结论/用途 | 来源 | URL | 日期 | 访问日 | 等级 | 置信度 | 局限 |\n|---|---|---|---|---|---|---|---|\n",
            encoding="utf-8",
        )
    print(root)


if __name__ == "__main__":
    main()
