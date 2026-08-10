#!/usr/bin/python3
# =============================================================================
# _blurred_common.py — shared helpers for the BLAQUE BAUX BLURRED sketches.
#
# Blurred hunts for the OPPOSITE of pairs trading: genuinely uncorrelated names,
# for maximum diversification. Two universes:
#   EQ — a broad cross-sector equity set, to hunt for the lowest correlation.
#   AC — genuinely distinct ASSET CLASSES (equity / bonds / gold / commodities /
#        ags / dollar / vol), the real diversifier the base's law points to.
# All sketches read Alpaca SIP daily bars, are read-only, print their results.
# Keys come from env only (ALPACA_KEY_ID / ALPACA_SECRET_KEY) — never hardcoded.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

_H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"],
      "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}

# broad cross-sector equity universe (tech, fin, energy, health, staples,
# discretionary, industrial, utilities, REIT, materials, gold miners, telecom)
EQ = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","TSLA","JPM","BAC","GS","XOM","CVX","COP",
      "JNJ","PFE","MRK","LLY","PG","KO","WMT","COST","HD","MCD","CAT","BA","GE","LMT",
      "NEE","DUK","SO","AMT","FCX","NEM","GOLD","T","VZ","DIS","UNH","V","MA"]
# genuinely distinct asset classes
AC = ["SPY","TLT","IEF","GLD","DBC","DBA","UUP","VIXY"]


def _closes(sym, start="2016-01-01", end="2026-08-01"):
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={sym}&timeframe=1Day"
         f"&start={start}&end={end}&adjustment=all&feed=sip&limit=10000")
    b = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=_H), timeout=40)
                  ).get("bars", {}).get(sym, [])
    return {x["t"][:10]: x["c"] for x in b}


def panel(syms, start="2016-01-01", end="2026-08-01"):
    """Aligned (dates, price-matrix) over the symbols with >500 shared days."""
    D = {s: _closes(s, start, end) for s in syms}
    D = {s: v for s, v in D.items() if len(v) > 500}
    u = list(D)
    ds = sorted(set.intersection(*[set(v) for v in D.values()]))
    return u, ds, np.array([[D[s][d] for s in u] for d in ds], float)


def eff_bets(C):
    """Participation ratio of the correlation eigenvalues = effective # of bets."""
    lam = np.linalg.eigvalsh(C)
    return (lam.sum() ** 2) / (lam ** 2).sum()


def avg_corr(C):
    return float(C[np.triu_indices(len(C), 1)].mean())


def sharpe(pnl, ann=252):
    pnl = pnl[np.isfinite(pnl)]
    s = pnl.std()
    return float(pnl.mean() / s * math.sqrt(ann)) if s > 0 else float("nan")
