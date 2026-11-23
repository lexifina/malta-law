<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Malti](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Malta only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-23 09:54 UTC, Government Gazette: Acts and Legal Notices (as listed on legislation.mt): 84 addresses read; 0 added, 0 changed, 0 removed; no change; 70 not published, 0 of them with no reason. Flags: `publish-lag`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [legislation.mt: Laws of Malta (Chapters and subsidiary legislation)](https://legislation.mt/Legislation) | `cap/`, `sl/`, `laws.csv` | daily | 2026-11-23 02:35 UTC | no change | watched: the English consolidated versions are compared, as this repository holds the English text |
| [Government Gazette: Acts and Legal Notices (as listed on legislation.mt)](https://legislation.mt/eli/eli-update-feed.atom) | `cap/`, `sl/` | daily | 2026-11-23 09:54 UTC | no change | watched: the Gazette's own site (gov.mt) answers automated readers with a browser challenge, so its Acts and Legal Notices are read on legislation.mt; their changes reach this repository through legislation.mt's consolidated versions |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
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
