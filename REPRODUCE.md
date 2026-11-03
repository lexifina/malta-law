# Reproducing this repository

Everything in this history comes from legislation.mt and can be rebuilt from it. The same PDFs give the same commit hashes.

## What this build used

- Built on 2026-10-28 from 5084 laws (562 Chapters, 4522 subsidiary legislation) and 8195 English consolidated versions.
- 7265 commits: 5053 consolidated, 1965 amendment, 244 unexplained, and 3 documentation commits.
- Appended on 2026-11-03, after that build, without rewriting it: S.L. 371.25, S.L. 371.26, S.L. 371.27, S.L. 371.28, S.L. 376.12, S.L. 376.13, S.L. 376.14, S.L. 376.15, as legislation.mt published them that day.
- The sha256 of every PDF is in `data/pdf-sha256.tsv`. Unreadable versions (43) are in `data/unreadable.csv`.
- Build scripts (sha256), copied to `tools/build/`:
  - `build.py` 15a5f34a21ab930f6c780908ae6889a71144c9897a139babb309e346c3e85782
  - `parse_pdf.py` 9cfcc21386b74f35f9730f24b97f26f0c248f01fd89a4367300c08cc7e2edd59
  - `docs.py` 5ea56e2fcf5bd8fc1eca3978075cf59fa5190419023a8b97871183303b530d28

## Steps

Python 3.11+ with `pymupdf`, and `git` on the path.

```sh
cd tools/build
# the retrieved law pages and PDFs (sha256 in data/pdf-sha256.tsv), where build.py reads them
python build.py ../../../malta-law-rebuilt --today 2026-10-28
```

`--today` dates the documentation commit and is required, so a rebuild never depends on the day it is run.

legislation.mt adds versions as laws change, so a later retrieval gives a longer history. To rebuild this exact history, use PDFs whose sha256 match `data/pdf-sha256.tsv`.

## Decisions

- **Which text:** the English PDF of each consolidated version (`eli/<cap|sl>/<id>/<YYYYMMDD>/eng`). The Maltese versions are not used.
- **Units:** an article (regulation, rule) starts at a bold number at the start of a line. Inside a schedule, bold numbers are items of the schedule. Centred lines between articles are headings of the next article. The front matter up to the arrangement table is `title.md`.
- **Margin notes** belong to the unit that starts nearest at or above them on the page.
- **Normalised away:** whitespace, curly quotes, dashes and soft hyphens, so typesetting alone never makes a change.
- **Crediting:** margin note, then law, then date, else unexplained (see README).
- **Dates:** noon Malta time (CET, or CEST from the last Sunday of March to the last Sunday of October), on the version's point-in-time date. Dates before 1970 are clamped to 1970-01-01 plus one second per commit, in order.
- **Order:** by date; on one date, consolidated versions first, then amendments by law (Acts before Legal Notices, by year and number), then unexplained changes.
