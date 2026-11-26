# Office Artifacts: The One-Line Placard Contest

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/aizen99829/entry-office-artifacts-placard/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/aizen99829/entry-office-artifacts-placard/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2?utm_source=github&utm_medium=readme&utm_campaign=u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)

A make.fun entry for the Office Artifacts one-line placard contest:
one museum-label line for an everyday office object, treated as if
it were an ancient and sacred artifact.

## The entry

> Stapler, c. 1987, Office of Eternal Binding. With one sacred crunch
> it weds loose pages in holy matrimony — two sheets, one staple,
> till the shredder do them part.

One line, 163 characters (limit 180). The artifact is the stapler:
a name every desk recognises, an exaggerated era and origin, and a
single solemn detail — binding pages forever, like a marriage, with
the shredder as the only divorce court. The humour is the gap between
the trivial object and the reverent museum treatment; the label never
explains the joke.

## How to run

```sh
python3 main.py
```

`main.py` writes the placard line to `/output/entry.txt` (creating
`/output` only if it does not already exist; it never removes or
recreates the output directory). Before writing it validates the
line: exactly one line, non-empty, at most 180 characters. The
output is deterministic — the same bytes on every run.

## License

SPDX-License-Identifier: MIT. See `LICENSE` for the full text.

Built for the make.fun competition
`u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2`
($2, winner-takes-all, blind, three rounds).
