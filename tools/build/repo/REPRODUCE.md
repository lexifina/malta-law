# Reproducing this repository

Everything in this history comes from legislation.mt and can be rebuilt from it. The same PDFs give the same commit hashes.

## What this build used

- Built on {{TODAY}} from {{LAWS}} laws ({{CHAPTERS}} Chapters, {{SUBSIDIARY}} subsidiary legislation) and {{VERSIONS}} English consolidated versions.
- {{COMMITS}} commits: {{CONSOLIDATED}} consolidated, {{AMENDMENT}} amendment, {{UNEXPLAINED}} unexplained, and this documentation commit.
- The sha256 of every PDF is in `data/pdf-sha256.tsv`. Unreadable versions ({{UNREADABLE}}) are in `data/unreadable.csv`.
- Build scripts (sha256), copied to `tools/build/`:
  - `build.py` {{SHA_BUILD_PY}}
  - `parse_pdf.py` {{SHA_PARSE_PDF_PY}}
  - `fetch_catalogue.py` {{SHA_FETCH_CATALOGUE_PY}}
  - `fetch_pdfs.py` {{SHA_FETCH_PDFS_PY}}
  - `docs.py` {{SHA_DOCS_PY}}

## Steps

Python 3.11+ with `pymupdf`, and `curl` and `git` on the path.

```sh
cd tools/build
python fetch_catalogue.py --workers 16   # .cache/laws/<kind>-<id>.json: versions and related laws per law
python fetch_pdfs.py --workers 10        # .cache/pdf/<snapshot>.pdf and .cache/pdf-sha256.tsv
python build.py ../../../malta-law-rebuilt --today {{TODAY}}
```

`--today` dates the documentation commit and is required, so a rebuild never depends on the day it is run.

legislation.mt adds versions as laws change, so a later fetch gives a longer history. To rebuild this exact history, use PDFs whose sha256 match `data/pdf-sha256.tsv`.

## Fetch rate

legislation.mt's robots.txt (checked 28 October 2026) disallows only the Sogou crawler and sets no Crawl-delay. The catalogue (5,079 law pages) was fetched with 8 and then 16 parallel requests, and the 8,187 PDFs (2.0 GB) with 10 to 20 parallel requests, over about two hours, with responses cached on disk so each document was fetched once. A rebuild from the cache makes no requests. For a fresh full fetch, consider asking the Legislation Unit for bulk access first.

## Decisions

- **Which text:** the English PDF of each consolidated version (`eli/<cap|sl>/<id>/<YYYYMMDD>/eng`). The Maltese versions are not used.
- **Units:** an article (regulation, rule) starts at a bold number at the start of a line. Inside a schedule, bold numbers are items of the schedule. Centred lines between articles are headings of the next article. The front matter up to the arrangement table is `title.md`.
- **Margin notes** belong to the unit that starts nearest at or above them on the page.
- **Normalised away:** whitespace, curly quotes, dashes and soft hyphens, so typesetting alone never makes a change.
- **Crediting:** margin note, then law, then date, else unexplained (see README).
- **Dates:** noon Malta time (CET, or CEST from the last Sunday of March to the last Sunday of October), on the version's point-in-time date. Dates before 1970 are clamped to 1970-01-01 plus one second per commit, in order.
- **Order:** by date; on one date, consolidated versions first, then amendments by law (Acts before Legal Notices, by year and number), then unexplained changes.
