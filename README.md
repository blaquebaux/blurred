# Blaque Baux Blurred

**Deliberately uncorrelated — names with no relationship, traded as one book.**

Blurred is a member of the Blaque Baux family. The [core repo](https://github.com/Carter-Warrens/blaquebaux)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Blurred points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/Carter-Warrens/blaquebaux-blurred.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Where pairs trading seeks cointegrated (correlated) names, Blurred seeks the opposite: a basket of genuinely UNCORRELATED names for maximum diversification, or spreads between names that shouldn't move together. The base correlation study is the caution — truly uncorrelated equities are rare (most share market beta), so the real work is finding and *verifying* low-correlation structure.

## Research plan (Path A — not yet built)

- Max-diversification basket — assemble low-pairwise-correlation names; measure effective bets.
- Verify, don't assume — correlations are unstable; test out-of-sample (the Bore lesson).
- Uncorrelated spreads — trade divergences between economically unrelated names.

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Scaffold.** Engine wired as a submodule; strategy research not yet conducted.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/Carter-Warrens/blaquebaux) is the
base/blueprint and holds the [full family roster](https://github.com/Carter-Warrens/blaquebaux#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> Carter-Warrens/blaquebaux)
research/   Path-A strategy sketches (to come)
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
