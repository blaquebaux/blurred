# Blaque Baux Blurred — research

First-pass Path-A research on the dream of a **deliberately uncorrelated book**. All sketches read
Alpaca SIP daily bars (2016–2026), are read-only, and print their results. Two universes: a broad
40-name cross-sector equity set (to hunt for low correlation) and 8 genuinely distinct asset classes.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/blurred_1_diversification_floor.py   # can you find uncorrelated equities? does it hold?
python research/blurred_2_no_spread.py                # can you trade uncorrelated names against each other?
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Can you build an uncorrelated book from equities? | 40 names → **7.5 bets** (19% eff, avg corr +0.30); best-10 still +0.17 | ❌ no — a floor, not zero |
| 1 | Does the low correlation hold out-of-sample / in crises? | lowest pairs +0.02 → +0.17; crash corr +0.30 → **+0.66** | ❌ unstable — converges when needed |
| 1 | Where does uncorrelation actually live? | 8 asset classes: avg corr **−0.00**, 60% efficient | ✅ across ASSET CLASSES (the spine) |
| 2 | Trade uncorrelated names against each other? | uncorrelated pair fade −0.33; correlated pair +0.15 | ❌ no anchor — the spread is a random walk |

## The synthesis

- **You cannot build an uncorrelated book out of equities.** They share market beta, so 40 broad
  cross-sector names collapse to **~7.5 effective bets** (19% efficient, avg pairwise corr +0.30).
  Even the hand-picked *lowest*-correlation 10 (gold miners + health + telecom + energy + staples)
  still average **+0.17** — a floor, not zero.

- **And the little uncorrelation you find is unstable.** The 20 lowest-correlation pairs drift from
  +0.02 to **+0.17** out-of-sample, and in the 2020 crash the universe's average pairwise correlation
  jumps **+0.30 → +0.66** — diversification evaporates exactly when you need it (Bore's caution:
  *correlations are unstable*, and they converge toward 1 in a crisis).

- **Genuine uncorrelation lives across ASSET CLASSES.** Eight distinct classes (equity / bonds /
  gold / commodities / ags / dollar / vol) sit at **~0.00** average correlation and **60% efficient**
  — 3× the diversification efficiency of 40 equities. This is the base's diversification law verbatim,
  and it is exactly what the validated spine already harvests.

- **"Trade uncorrelated names against each other" has no anchor.** A spread is tradeable only when the
  legs are *tied* (cointegrated) so the gap mean-reverts — the **opposite** of uncorrelated. Z-fading
  the most-uncorrelated pair earns a negative Sharpe (−0.33, a random walk); only a genuinely
  correlated pair has a positive tilt (+0.15), and even that is weak — the dead-pairs result from Bore.

**Verdict:** Blurred is a **null / re-derivation**, and a clarifying one. Uncorrelation is the right
ingredient for *diversification* but the wrong one for a *spread*, and within equities you can get
neither — the correlation floor is positive and it rises in stress. The honest conclusion points
straight back to the family's spine: **diversify across asset classes, not across names.** No live
driver; nothing here clears the spine's bar.

## Files
- `_blurred_common.py` — shared helpers + the two universes (40 equities, 8 asset classes).
- `blurred_1_diversification_floor.py` — the correlation floor + instability; equities vs asset classes.
- `blurred_2_no_spread.py` — uncorrelated names have no tradeable spread (needs a cointegrated tie).
