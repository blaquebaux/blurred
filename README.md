# Blaque Baux Blurred

**Deliberately uncorrelated — names with no relationship, traded as one book.**

Blurred is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Blurred points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/blurred.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Where pairs trading seeks cointegrated (correlated) names, Blurred seeks the opposite: a basket of genuinely UNCORRELATED names for maximum diversification, or spreads between names that shouldn't move together. The base correlation study is the caution — truly uncorrelated equities are rare (most share market beta), so the real work is finding and *verifying* low-correlation structure.

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard:

| # | Question | Verdict |
|---|----------|---------|
| 1 | Can you build an uncorrelated book from equities? | ❌ no — 40 names → **7.5 bets** (avg corr +0.30); best-10 still +0.17 |
| 1 | Does the low correlation hold out-of-sample / in crises? | ❌ unstable — pairs +0.02→+0.17; crash corr +0.30→**+0.66** |
| 1 | Where does uncorrelation actually live? | ✅ across **asset classes** — 8 classes avg corr −0.00, 60% efficient |
| 2 | Trade uncorrelated names against each other? | ❌ no anchor — the spread is a random walk (−0.33) |

**The synthesis:** you cannot build an uncorrelated book out of equities — they share market beta,
so 40 broad names collapse to ~7.5 effective bets (avg corr +0.30) and even the lowest-correlation 10
still average +0.17 (a floor, not zero). Worse, that thin uncorrelation is **unstable**: the lowest
pairs drift +0.02→+0.17 out-of-sample and the crash-window average jumps +0.30→**+0.66** — it
converges exactly when you need it (Bore's caution). Genuine uncorrelation lives **across asset
classes** (8 classes at ~0.00 avg corr, 60% efficient — 3× the efficiency), which is what the spine
already harvests. And "trade uncorrelated names against each other" has no anchor: a spread needs a
*cointegrated* tie to mean-revert (the opposite of uncorrelated), so the most-uncorrelated pair fades
to −0.33 while only a correlated pair tilts positive (+0.15, and weak — dead pairs, per Bore).

## Status
**Research: first pass complete — a null / re-derivation** (`research/`). Uncorrelation is the right
ingredient for diversification, the wrong one for a spread, and within equities you get neither. The
honest conclusion points back to the spine: **diversify across asset classes, not across names.**
No live driver. Nothing validated to the spine's bar.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   two Path-A sketches (diversification floor + instability, no-spread) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
