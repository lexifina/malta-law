<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Watching the sources: what is watched for Malta

[Malti](WATCHING.md)

How global-law watches every country's sources: [global-law WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md). This page is the same for Malta only: every official source this repository takes text from, what is read on it, how often and when it was last read. Every read and what came of it: [monitoring/](monitoring/README.en.md).

| Source | What is read | Folders | How often | Last read | State |
| --- | --- | --- | --- | --- | --- |
| [legislation.mt: Laws of Malta (Chapters and subsidiary legislation)](https://legislation.mt/Legislation) | the ELI sitemap (one request: every Chapter and piece of subsidiary legislation, with the day its entry last changed) and, for each law whose entry changed since it was last read, its page: its consolidated versions and whether it is in force | `cap/`, `sl/`, `laws.csv` | daily | 2026-11-23 21:43 UTC | watched: the English consolidated versions are compared, as this repository holds the English text |
| [Government Gazette: Acts and Legal Notices (as listed on legislation.mt)](https://legislation.mt/eli/eli-update-feed.atom) | legislation.mt's ELI update feed (one request: the latest publications, each with its Gazette issue) and the Acts and Legal Notices of the ELI sitemap; the page of each one published since the day this repository's record runs to, once: its day of publication and the laws it amends, makes or repeals | `cap/`, `sl/` | daily | 2026-11-24 00:04 UTC | watched: the Gazette's own site (gov.mt) answers automated readers with a browser challenge, so its Acts and Legal Notices are read on legislation.mt; their changes reach this repository through legislation.mt's consolidated versions |

Sources are read within their robots.txt and terms, with pauses between requests.
