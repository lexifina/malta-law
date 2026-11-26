<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Malti](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Malta only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-26 05:31 UTC, Government Gazette: Acts and Legal Notices (as listed on legislation.mt): 9 addresses read; 0 added, 3 changed, 0 removed; changes found; 23 not published, 0 of them with no reason. Flags: `audit-disagrees`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [legislation.mt: Laws of Malta (Chapters and subsidiary legislation)](https://legislation.mt/Legislation) | `cap/`, `sl/`, `laws.csv` | daily | 2026-11-26 05:30 UTC | changes found | watched: the English consolidated versions are compared, as this repository holds the English text |
| [Government Gazette: Acts and Legal Notices (as listed on legislation.mt)](https://legislation.mt/eli/eli-update-feed.atom) | `cap/`, `sl/` | daily | 2026-11-26 05:31 UTC | changes found | watched: the Gazette's own site (gov.mt) answers automated readers with a browser challenge, so its Acts and Legal Notices are read on legislation.mt; their changes reach this repository through legislation.mt's consolidated versions |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-26 05:30](checks/2026-11.md#mt-gazette-20261126t053054z) | gazette | 9 | 0 | 3 | 0 | 23 (0) | changes found `audit-disagrees` | — |
| [2026-11-26 05:10](checks/2026-11.md#mt-legislation-mt-20261126t051013z) | legislation-mt | 743 | 0 | 4 | 0 | 39 (0) | changes found `audit-disagrees` | [4](https://github.com/lexifina/malta-law/compare/e13476ca3660...8af0d6bd6cc1) |
| [2026-11-25 05:27](checks/2026-11.md#mt-gazette-20261125t052755z) | gazette | 5 | 0 | 0 | 0 | 26 (0) | no change `audit-disagrees` | — |
| [2026-11-25 05:08](checks/2026-11.md#mt-legislation-mt-20261125t050821z) | legislation-mt | 729 | 0 | 0 | 0 | 39 (0) | no change `audit-disagrees` | — |
| [2026-11-24 00:25](checks/2026-11.md#mt-gazette-20261124t002526z) | gazette | 6 | 0 | 0 | 0 | 26 (0) | no change `audit-disagrees` | — |
| [2026-11-24 00:04](checks/2026-11.md#mt-legislation-mt-20261124t000443z) | legislation-mt | 739 | 0 | 0 | 0 | 41 (0) | changes found `audit-disagrees` | [3](https://github.com/lexifina/malta-law/compare/08a837235d8b...f910a6a07ddd) |
| [2026-11-24 00:04](checks/2026-11.md#mt-gazette-20261124t000420z) | gazette | 2 | 0 | 0 | 0 | 26 (0) | no change `audit-disagrees` | — |
| [2026-11-23 21:43](checks/2026-11.md#mt-legislation-mt-20261123t214330z) | legislation-mt | 5068 | 0 | 0 | 0 | 39 (0) | no change `verify-differ` `audit-disagrees` | — |
| [2026-11-23 21:42](checks/2026-11.md#mt-gazette-20261123t214212z) | gazette | 6 | 0 | 0 | 0 | 26 (0) | no change `audit-disagrees` | — |
| [2026-11-23 21:35](checks/2026-11.md#mt-legislation-mt-20261123t213542z) | legislation-mt | 233 | 0 | 0 | 0 | 39 (0) | the check failed | — |
| [2026-11-23 21:32](checks/2026-11.md#mt-gazette-20261123t213228z) | gazette | 9 | 0 | 0 | 0 | 26 (0) | no change `audit-disagrees` | — |
| [2026-11-23 21:21](checks/2026-11.md#mt-legislation-mt-20261123t212128z) | legislation-mt | 393 | 0 | 0 | 0 | 39 (0) | no change | [41](https://github.com/lexifina/malta-law/compare/5b4cb29d6cc1...ecedd7b51065) |
| [2026-11-23 09:52](checks/2026-11.md#mt-gazette-20261123t095225z) | gazette | 84 | 0 | 0 | 0 | 70 (0) | no change `publish-lag` | — |
| [2026-11-23 02:33](checks/2026-11.md#mt-legislation-mt-20261123t023312z) | legislation-mt | 84 | 0 | 0 | 0 | 93 (0) | no change `publish-lag` | — |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
