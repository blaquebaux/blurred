#!/usr/bin/python3
# =============================================================================
# blurred_1_diversification_floor.py — BLAQUE BAUX BLURRED #1
#   Can you find genuinely uncorrelated EQUITIES? And does the low correlation HOLD?
#
# The dream: assemble a max-diversification book of names with no relationship.
# FINDING: within equities, no. They share market beta, so 40 names collapse to
# ~7.5 effective bets (19% efficient, avg corr +0.30). Even the hand-picked
# LOWEST-correlation 10 still average +0.17 corr — a floor, not zero. And the
# little uncorrelation you find is UNSTABLE: the 20 lowest-corr pairs drift from
# +0.02 to +0.17 out-of-sample, and in the 2020 crash average pairwise correlation
# jumps +0.30 -> +0.66 — diversification evaporates exactly when you need it.
# By contrast 8 real ASSET CLASSES sit at ~0.00 avg corr, 60% efficient. That is
# the base's law: genuine uncorrelation lives ACROSS asset classes, not within equities.
#
# RESULTS AS TESTED (2016-2026):
#   40 equities:      avg corr +0.30  eff-bets 7.5/40  (19% efficient)
#   8 asset classes:  avg corr -0.00  eff-bets 4.8/8   (60% efficient)
#   lowest-corr 10 equities: avg corr +0.17  eff-bets 7.5/10  (a floor, not zero)
#   20 lowest-corr pairs: 1st-half +0.02 -> 2nd-half +0.17   (drifts up)
#   avg pairwise corr: normal +0.30 -> 2020 crash +0.66      (converges when needed)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blurred_common import EQ, AC, panel, eff_bets, avg_corr

ue, de, Me = panel(EQ); Re = Me[1:] / Me[:-1] - 1; Ce = np.corrcoef(Re.T)
ua, da, Ma = panel(AC); Ra = Ma[1:] / Ma[:-1] - 1; Ca = np.corrcoef(Ra.T)
print("=" * 76, "\nBLURRED #1 — the limits of diversification via uncorrelation\n" + "=" * 76)

print("\n1. WITHIN EQUITIES vs ACROSS ASSET CLASSES (effective independent bets)")
print(f"  {len(ue)} equities:      avg corr {avg_corr(Ce):+.2f}   eff-bets {eff_bets(Ce):.1f}/{len(ue)}  ({100*eff_bets(Ce)/len(ue):.0f}% efficient)")
print(f"  {len(ua)} asset classes: avg corr {avg_corr(Ca):+.2f}   eff-bets {eff_bets(Ca):.1f}/{len(ua)}  ({100*eff_bets(Ca)/len(ua):.0f}% efficient)")

print("\n2. THE FLOOR — even the lowest-correlation equities aren't uncorrelated")
chosen = [int(np.argmin(np.nanmean(Ce, 1)))]
while len(chosen) < 10:                       # greedy: minimize avg pairwise corr
    best, bv = None, 9.0
    for j in range(len(ue)):
        if j in chosen: continue
        v = float(np.mean([Ce[j, k] for k in chosen]))
        if v < bv: bv, best = v, j
    chosen.append(best)
Csub = Ce[np.ix_(chosen, chosen)]
print(f"  lowest-corr 10: {[ue[j] for j in chosen]}")
print(f"    avg corr {avg_corr(Csub):+.2f}  eff-bets {eff_bets(Csub):.1f}/10   (a floor, not zero)")

print("\n3. INSTABILITY — low correlation drifts up out-of-sample and converges in crises")
h = len(Re) // 2; C1 = np.corrcoef(Re[:h].T); C2 = np.corrcoef(Re[h:].T)
iu = np.triu_indices(len(ue), 1)
pairs = sorted(zip(C1[iu], iu[0], iu[1]))[:20]
c1 = np.mean([p[0] for p in pairs]); c2 = np.mean([C2[a, b] for _, a, b in pairs])
print(f"  20 lowest-corr pairs: 1st-half {c1:+.2f}  ->  2nd-half {c2:+.2f}   (drifts up)")
dwin = [k for k, d in enumerate(de[1:]) if "2020-02-19" <= d <= "2020-03-23"]
Cc = np.corrcoef(Re[dwin].T)
print(f"  avg pairwise corr: normal {avg_corr(Ce):+.2f}  ->  2020 crash {avg_corr(Cc):+.2f}   (converges toward 1)")

print("\nVERDICT: you cannot build an uncorrelated book out of equities — they share market beta,")
print("the residual uncorrelation is a floor (~+0.17), and it drifts up out-of-sample and collapses")
print("in a crisis. Genuine diversification lives ACROSS ASSET CLASSES (avg corr ~0.00, 60% efficient),")
print("which is exactly what the spine already harvests. Blurred re-derives the base's diversification law.")
