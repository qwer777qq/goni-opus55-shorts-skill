#!/usr/bin/env python3
"""Search the bundled Opus 5.5 video prompt catalog without dependencies."""

import argparse
import json
import re
import sys
from pathlib import Path


CATALOG = Path(__file__).resolve().parents[1] / "references" / "videos.json"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Words or phrase to find in prompts and metadata")
    parser.add_argument("--category", choices=("motion", "explainer", "3d", "interactive"))
    parser.add_argument("--tag", help="Technology tag, e.g. threejs or gsap")
    parser.add_argument("--complete-only", action="store_true", help="Hide partial prompts")
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--full", action="store_true", help="Print complete prompt text")
    args = parser.parse_args()

    terms = re.findall(r"[\w-]+", args.query.casefold())
    if not terms:
        parser.error("query needs at least one word")
    records = json.loads(CATALOG.read_text(encoding="utf-8"))
    ranked = []
    for item in records:
        if args.category and item["category"] != args.category:
            continue
        if args.tag and args.tag.casefold() not in item["tech_tags"]:
            continue
        if args.complete_only and item["prompt_partial"]:
            continue
        haystack = " ".join((item["prompt"], item["slug"], " ".join(item["tech_tags"]))).casefold()
        hits = sum(term in haystack for term in terms)
        if not hits:
            continue
        score = hits * 10 + (20 if args.query.casefold() in haystack else 0)
        score += sum(min(haystack.count(term), 3) for term in terms)
        ranked.append((score, item))

    ranked.sort(key=lambda pair: (-pair[0], pair[1]["slug"]))
    for number, (score, item) in enumerate(ranked[: max(args.limit, 0)], 1):
        completeness = "partial" if item["prompt_partial"] else "complete"
        prompt = item["prompt"].strip() if args.full else " ".join(item["prompt"].split())[:360]
        print(f"{number}. {item['slug']} | score {score} | {item['category']} | {','.join(item['tech_tags'])} | {completeness}")
        print(f"   Watch: {item['skillry_url']}")
        print(f"   Original: {item['post_url']}")
        print(f"   Prompt: {prompt}")
        print()


if __name__ == "__main__":
    main()
