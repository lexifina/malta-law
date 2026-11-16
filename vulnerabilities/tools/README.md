# Tools

The scripts behind this Malta-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/malta-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only malta-law, its commit, its language
(`en`, the language of the texts held) and its code (`MT`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`,
`late_ext_rebut.py` and `config.json` sit three folders up, next to the copy of global-law (`gl/vulnerabilities/scripts/`).

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds this repository's history rows, and runs the detectors (`bash run.sh <shards>`; run here with 6) |
| `add_root.py` | Builds the history rows from this repository's own commits (global-law replays it only up to an earlier commit), so the history detectors read every change; changed for this repository (below) |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category: those whose old and new dates open the same sentence (here none), and, below 40, the shortest of the rest (here all 24) |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in Maltese and English, light and dark |
| `config.json` | The repository, the Maltese category names, the files and folders that are not law, and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_en.py`, `patch_en_et.py` | The same for English text in the search for references to repealed placeholders (found by the Bhutan and Ethiopia runs): "vacated" only as a marker, not "vacation" or "null and void", "shall be deleted" not as the mark of a deleted provision, and a provision that repeals another section or a whole earlier law not as a placeholder |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_de.py`, `patch_co.py`, `patch_sv.py`, `patch_pt.py`, `patch_ru.py`, `patch_r18.py`, `patch_xk.py`, `patch_mo.py` | The same for Vietnamese, Spanish, Catalan, German, Colombian and Salvadoran Spanish, Brazilian Portuguese, Russian, Albanian (Kosovo) and Macau Portuguese text (found by other runs); they change nothing in English text, but `redo.py` runs them on every repository |
| `patch_lu.py`, `patch_li.py` | The same for Luxembourg (the franc as "fr." and "LUF", for code `LU` only; paths with non-ASCII characters) and Liechtenstein (German text only); written after this run and not applied here. Neither changes anything for this repository, whose paths are ASCII and whose texts are English |
| `patch_mt.py` | Written for this run (below): the Maltese lira as "Lm" and "liri", and two words taken for currencies |
| `apply_patches.py` | Runs the patches above once each, in a fixed order (`patch_mt.py` last), and records them in the scripts folder (`.kit_patches.json`) |
| `map_moved.py` | For a repository that moved its act folders (`data/paths.json`), rewrites the paths in the history table to each act's folder since the move; this repository has not moved its folders, so it does nothing here |
| `redo.py` | Runs the patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--keep-reviews` keeps every review already made and reviews only new strong flags; `--full` runs every step again through `run.sh`, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
It was run as `bash run_triage.sh '^(data|tools|vulnerabilities)/|^[^/]+$'` (the root files, `data/` and `tools/` are not
law; every flag turned out to be in `cap/` or `sl/`); the 40 strongest lapsed time limits in law texts are the 40 strongest
of all. One repeal gap (article 198 of the Criminal Code, rape) was refused by the model service's content filter, also on
a second attempt, so 39 repeal gaps were reviewed; it was read by hand.

The detectors carried `patch_detectors.py` and the fourteen patches before `patch_lu.py` when they were run. Changes made
for this repository:

- `add_root.py`: each law's earliest version on legislation.mt is a commit `Kind: consolidated` with its day in
  `Consolidated:` and no `In-force:`, so the kit's `add_root.py` left all 5,053 out of the history table, and the reference
  scan, which reads the provisions that ever existed from that table, would not have known a provision that was in a first
  version and later deleted. They now count as `baseline` (an act's starting text, as the detectors already read it), dated
  by `Consolidated:`. The 244 commits `Kind: unexplained` (changes between two versions of legislation.mt that no law is
  credited with) count as law, beside the 1,965 amendments: 2,209 commits of kind `law`. The 3,222 corrections (`Kind:
  correction`, later commits that move a first version's date by a day) keep their own kind and are left out.
- `patch_mt.py`, in `detectors/currency_scan.py` (in the copy of global-law's scripts):
  - the Maltese lira, replaced by the euro on 1 January 2008, was read only as "lira" next to a figure, which Maltese law
    hardly writes; it writes "Lm15", "Lm 1,000" or "100 liri". "Lm" right before a figure (capital L, small m, not inside a
    word) and "liri" are now read, for Malta only (pins.json code `MT`). "Lm" after a figure is left out, as in the
    measuring instruments regulations it is a length ("not less than 0,02 Lm"), and so is "Lm" before a figure with one
    decimal place, the minimum landing size in the fisheries management plans ("Lm 11.1 cm", "Lm 16.0");
  - for every language, "Cabernet Franc" (a grape variety, in the wine regulations) is no longer the franc and "Dinaric"
    (the Dinaric dolomite Scots pine forests, a habitat type) no longer the dinar.

  The currency scan was run again: dead currencies went from 5 (3 francs of the Warsaw Convention, "Cabernet Franc",
  "Dinaric") to 129 (126 amounts in liri and the 3 francs).

Not changed, and stated in the READMEs: the history detectors take each version's date from the commits, and 877 first
versions hold text from a later year than their date (found by reading their margin notes), so a flag that turns on such a
date may be early; none of the flags that survived the review turns on one.
