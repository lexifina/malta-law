# Maltese law, change by change

The laws of Malta as a git repository: 562 Chapters and 4514 pieces of subsidiary legislation from [legislation.mt](https://legislation.mt), the official source published by the Legislation Unit. There is one file per article, regulation or schedule. Each change is a commit credited to the Act or Legal Notice that made it, dated the day the changed text took effect, at noon Malta time. The English text is used throughout.

The record runs from 1834-06-28 to 2026-10-06 in 7255 commits, built from 8187 consolidated versions.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did article 57 of the Code of Organization and Civil Procedure say on 1 June 2022? | `python tools/in_force_on.py 2022-06-01 cap/12 57` |
| The whole of a law on a date | `python tools/in_force_on.py 2022-06-01 cap/12` |
| Which law last changed each line of an article? | `git blame cap/12/57.md` |
| Every change to an article, with the law behind it | `git log -p cap/12/57.md` |
| Everything one Act changed, across every law | `git log --author='Act XXV of 2026' --stat` |
| Every law that changed a Chapter, in order | `git log --format='%(trailers:key=In-force,valueonly,separator=) %an' -- cap/12` |
| What no law is credited with | `git log --grep='Kind: unexplained'` |
| The list of laws, with their versions | [`laws.csv`](laws.csv) |

Each article file starts with its number and margin heading (`# 57. Duties of Director General (Courts).`), with any Book, Title or Part headings above it as `##` lines. Then comes one line per sub-article, paragraph or proviso. At the end, the history the consolidation prints in the margin, copied as it is: `- Amended by: VI.1880.6; XV.1913.22.` Here `VI.1880.6` means Act (before 1921, Ordinance) VI of 1880, section 6.

## The dates, and which one we use

legislation.mt publishes each law as a series of consolidated versions, each for a "point in time": the day from which that text applies. **Commits are dated by that day.** That is the date that decides which text governs a case, and it is also the day the amendments in that version came into force. Each amendment commit also carries the amending law's publication date, where legislation.mt gives one (`Published:`).

The record starts at each law's earliest version on legislation.mt, mostly from December 2020, when the current site began keeping versions; some laws have earlier versions. That first version is a commit labelled `Kind: consolidated`, by the Legislation Unit. It has the whole text as it stood then, with each article's margin history, so the history before that date is recorded but not as separate commits.

**Git cannot store dates before 1970.** A law whose earliest version is older is committed on 1970-01-01, one second apart and in order. Its real date is in the `Consolidated:` or `In-force:` trailer, which `tools/in_force_on.py` reads.

## What "author" means

The author of a commit is the law that made the change, at an address that cannot exist: `Act XXV of 2026 <act-2026-25@legislation-mt.invalid>`, `L.N. 218 of 2026 <ln-2026-218@legislation-mt.invalid>`. So `git blame` names, for each line, the law that last wrote it. One commit holds everything one law changed on one day, across every Chapter and piece of subsidiary legislation it touched (`Affecting:` trailers).

A change is credited by the evidence in the consolidation itself, strongest first (`Evidence:` trailer):
1. **margin note**: the changed article's margin history gains a new citation (`Amended by: XXV.2026.3`) — 6888 units;
2. **law**: the law's new version cites exactly one new law anywhere — 9431 units;
3. **date**: exactly one related Act or Legal Notice was published between the two versions — 3103 units.
4. **commencement**: exactly one related law is marked "partly in force" on legislation.mt, so its deferred part is what took effect — 175 units;
5. **cited earlier**: the unit's margin history already cites exactly one recent enough law, which was printed before and takes effect now — 56 units.

A law made before the previous version is never taken as the cause of a change since it: if its citation appears newly beside a unit, it has only moved between margin notes in a new typesetting. Where legislation.mt has no version for years, a change is credited to the law the margin names but dated by the first version that shows it.

A change with none of these (0 units) is by the Legislation Unit and labelled `Kind: unexplained`; it is never credited to a law. Where an article's margin gains more than one citation at once, the commit is credited to the latest and the others are listed as `Also-cited:`.

In total there are 5045 consolidated versions, 1965 amendment commits by 1817 amending laws, and 244 unexplained ones.

## What it does not show

- Text before each law's earliest version on legislation.mt, except as the margin histories list it.
- The Maltese text. Where the two differ, the Maltese text prevails for most laws; see article 74 of the Constitution of Malta.
- Footnotes, and the arrangement tables at the start of each Chapter.
- Versions whose PDF could not be read (43), listed in [`data/unreadable.csv`](data/unreadable.csv).
- Commencement that comes later than the consolidated version's date, and savings or transitional rules. These are in the amending laws themselves, at the `Source:` link of each commit.
- Who wrote words that a later version reproduces unchanged under a new number.

This is a research aid. Only the Government Gazette is authoritative, and the consolidated texts on legislation.mt, and so this repository, are not.

## How it is checked

`tools/build/` holds the build as it was run. Every PDF's sha256 is in [`data/pdf-sha256.tsv`](data/pdf-sha256.tsv), and the build is deterministic: from the same PDFs it gives the same commit hashes. See [`REPRODUCE.md`](REPRODUCE.md).

## How it is built

`fetch_catalogue.py` reads the ELI sitemap and each law's page on legislation.mt, which lists its consolidated versions and the laws related to it. `fetch_pdfs.py` downloads each English version's PDF. `parse_pdf.py` reads each PDF into units by their typography: bold article numbers, the margin column, centred headings and schedules. `build.py` compares consecutive versions unit by unit, credits each change as above, and writes the history with `git fast-import`. No AI model takes part in building or checking it.

## Licence

Source: legislation.mt, the Legislation Unit, Government of Malta. The texts were converted to one file per unit and arranged as commits, and the wording was not changed. The Copyright Act (Cap. 415) excludes "any written law" from literary works, subject to article 12 of the Statute Law Revision Act, 1980. **Check that article before this repository is made public.** Lexifina's own contributions (the tools, the arrangement and the commit messages) are CC0. See [`LICENSE`](LICENSE).
