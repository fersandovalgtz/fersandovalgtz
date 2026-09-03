#!/usr/bin/env python3
import csv, statistics
from pathlib import Path

p = Path(__file__).resolve().parents[1] / "data" / "fair_care_matrix_main_sample.csv"
with p.open(encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
fair = [float(r["FAIR_D"]) for r in rows]
care = [float(r["CARE_D"]) for r in rows]
delta = [a-b for a,b in zip(fair,care)]

def report(name, xs):
    print(f"{name}: mean={statistics.mean(xs):.2f}; median={statistics.median(xs):.1f}; range={min(xs):.0f}-{max(xs):.0f}")

print(f"n={len(rows)}")
report("FAIR-D", fair)
report("CARE-D", care)
report("Delta", delta)
