#!/usr/bin/env python3
import csv
import sys


def route(row):
    required = [
        "company",
        "source_url",
        "operator_name",
        "operator_linkedin",
        "signal",
        "unverified_hypothesis",
    ]

    if any(not row.get(field, "").strip() for field in required):
        return "REJECT", "missing provenance/operator/hypothesis"

    evidence = row["public_evidence"].lower()
    density_terms = [
        "global",
        "offices",
        "placements",
        "countries",
        "multiple",
        "ecosystem",
        "nationwide",
    ]
    has_workflow_density = any(term in evidence for term in density_terms)

    if row["size"] in {"51-200", "201-500"} and has_workflow_density:
        return "PRIORITY", "mid-market + publicly visible workflow density"

    if has_workflow_density:
        return "VALIDATE", "strong workflow-density signal; smaller company"

    return "DEFER", "insufficient public workflow-density signal"


def main(path):
    with open(path, encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    counts = {}
    print("MAXX RECRUITMENT WEDGE — VALIDATION QUEUE")
    print("=" * 88)

    for row in rows:
        route_name, reason = route(row)
        counts[route_name] = counts.get(route_name, 0) + 1

        print(f'{row["company"]:<20} {route_name:<9} | {reason}')
        print(f'  operator: {row["operator_name"]} — {row["operator_title"]}')
        print(f'  signal: {row["signal"]}')
        print(f'  probe: {row["unverified_hypothesis"]}')

    print()
    print("COUNTS")
    for name in ["PRIORITY", "VALIDATE", "DEFER", "REJECT"]:
        print(f"{name}={counts.get(name, 0)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python router.py targets.csv")
    main(sys.argv[1])
