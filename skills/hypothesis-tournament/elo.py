"""Elo ratings from a match log.

Usage: python elo.py matches.jsonl > ratings.md
Each line of the log: {"a": "C1", "b": "C4", "winner": "C4"}   (winner may be "draw")
Matches are processed in file order, so the order of the log affects the result.
"""
import json
import sys

START, K = 1200.0, 32.0


def expected(ra, rb):
    return 1.0 / (1.0 + 10 ** ((rb - ra) / 400.0))


def ratings(matches):
    r, played = {}, {}
    for m in matches:
        a, b, w = m["a"], m["b"], m["winner"]
        assert w in (a, b, "draw"), f"winner must be a, b or 'draw': {m}"
        ra, rb = r.setdefault(a, START), r.setdefault(b, START)
        sa = 0.5 if w == "draw" else float(w == a)
        r[a] = ra + K * (sa - expected(ra, rb))
        r[b] = rb + K * ((1 - sa) - expected(rb, ra))
        played[a] = played.get(a, 0) + 1
        played[b] = played.get(b, 0) + 1
    return r, played


def table(r, played):
    rows = ["| Rank | ID | Elo | Matches |", "|---|---|---|---|"]
    for i, (c, v) in enumerate(sorted(r.items(), key=lambda kv: -kv[1]), 1):
        rows.append(f"| {i} | {c} | {v:.0f} | {played[c]} |")
    return "\n".join(rows)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as f:
        log = [json.loads(line) for line in f if line.strip()]
    print("# Elo ratings\n\nPreference among generated ideas, not evidence of truth.\n")
    print(table(*ratings(log)))
