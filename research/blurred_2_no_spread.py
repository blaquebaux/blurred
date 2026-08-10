#!/usr/bin/python3
# =============================================================================
# blurred_2_no_spread.py — BLAQUE BAUX BLURRED #2
#   "Trade uncorrelated names against each other" — there's no anchor to trade.
#
# The thesis' second leg: trade spreads between names that shouldn't move together.
# FINDING: uncorrelated is the wrong ingredient. A tradeable spread needs a MEAN-
# REVERTING (cointegrated) relationship — i.e. the two legs must be TIED together so
# the gap pulls back. Uncorrelated names have no such tie, so their spread is a
# random walk: z-fading the most-uncorrelated pair (TSLA/VZ, corr +0.03) earns a
# NEGATIVE Sharpe (-0.33), while z-fading a genuinely CORRELATED pair (KO/PG, corr
# +0.61) is the only one with a positive tilt (+0.15) — and even that is weak, the
# same dead-pairs result Bore found. The irony: Blurred's own ingredient (low corr)
# is exactly what removes the thing you'd trade.
#
# RESULTS AS TESTED (2016-2026, 60d z-fade of the log-spread, 2bp/side):
#   uncorrelated pair TSLA/VZ (corr +0.03): spread-fade Sharpe -0.33   (random walk, no anchor)
#   correlated   pair KO/PG   (corr +0.61): spread-fade Sharpe +0.15   (weak — dead pairs, per Bore)
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blurred_common import EQ, panel, sharpe

u, ds, M = panel(EQ); R = M[1:] / M[:-1] - 1; idx = {s: u.index(s) for s in u}
print("=" * 76, "\nBLURRED #2 — uncorrelated names have no tradeable spread\n" + "=" * 76)

def fade(a, b, win=60, cost=2.0):
    """z-fade the log-spread; needs a mean-reverting (cointegrated) tie to work."""
    la = np.log(M[:, idx[a]]); lb = np.log(M[:, idx[b]]); sp = la - lb
    z = np.full(len(sp), np.nan)
    for t in range(win, len(sp)):
        seg = sp[t - win:t]
        if seg.std() > 0: z[t] = (sp[t] - seg.mean()) / seg.std()
    sig = -np.tanh(z)[:-1]                                   # fade the deviation
    pnl = sig * (R[:, idx[a]] - R[:, idx[b]]) / 2 - np.abs(np.diff(np.r_[0, sig])) * cost / 1e4
    return sharpe(pnl)

# most-uncorrelated pair in the universe vs a classic correlated pair
Ce = np.corrcoef(R.T); iu = np.triu_indices(len(u), 1)
lo = sorted(zip(Ce[iu], iu[0], iu[1]))[0]; a, b = u[lo[1]], u[lo[2]]
print(f"  uncorrelated pair {a}/{b} (corr {Ce[lo[1],lo[2]]:+.2f}): spread-fade Sharpe {fade(a,b):+.2f}   (random walk, no anchor)")
print(f"  correlated   pair KO/PG (corr {Ce[idx['KO'],idx['PG']]:+.2f}): spread-fade Sharpe {fade('KO','PG'):+.2f}   (weak — dead pairs, per Bore)")

print("\nVERDICT: 'trade uncorrelated names against each other' has no anchor. A spread is tradeable")
print("only when the legs are TIED (cointegrated) so the gap mean-reverts — the opposite of")
print("uncorrelated. Uncorrelation is the right ingredient for DIVERSIFICATION (blurred_1), the")
print("wrong one for a SPREAD. And the correlated pairs that do have an anchor are weak (Bore).")
