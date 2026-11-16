# Malta: l-istorja tal-liġi f’git

**Malti** · **[Or read it in English](README.en.md)**

<picture>
<source media="(prefers-color-scheme: dark)" srcset="data/mt/effort-dark.svg">
<img alt="Il-liġi ta’ Malta f’dan ir-repożitorju: x’fih, il-bidliet skont is-sena tad-dħul fis-seħħ, kemm hu komplut meta mqabbel mas-sorsi uffiċjali u l-korrettezza ta’ dak li fih" src="data/mt/effort-light.svg" width="880">
</picture>

Il-liġi ta’ Malta bħala storja git: fajl wieħed għal kull artikolu, regolament jew skeda, commit wieħed għal kull verżjoni fil-jum li fih daħlet fis-seħħ, u l-Att jew l-Avviż Legali li għamel kull bidla bħala l-awtur tal-commit. `git blame` jsemmi l-liġi wara kull linja; `git log` jelenka kull bidla f’artikolu; jekk tagħżel data, tieħu t-test li kien fis-seħħ dakinhar.

Parti minn [lexifina/global-law](https://github.com/lexifina/global-law), storja git waħda għal-liġi ta’ kull pajjiż: dan huwa d-dritt nazzjonali ta’ Malta, li global-law jaqra f’`malta/national/acts/`.

**X’fih issa:** kull Kapitlu (562) u kull biċċa leġiżlazzjoni sussidjarja (4,522) fuq legislation.mt, 5,084 liġi b’8,195 verżjoni konsolidata sal-punt fiż-żmien tas-6 ta’ Ottubru 2026, f’10,495 commit; 31 minn dawn il-liġijiet m’għandhomx test hawn, għax il-PDFs tagħhom ma setgħux jinqraw. [`laws.csv`](laws.csv) jelenka kull liġi bit-tip tagħha, jekk hijiex fis-seħħ, il-verżjonijiet tagħha u l-folder tagħha.

Kull liġi hija folder, `cap/<numru>/` għal Kapitlu u `sl/<numru>/` għal leġiżlazzjoni sussidjarja (`cap/452/` huwa l-Employment and Industrial Relations Act, l-Att dwar l-Impjiegi u r-Relazzjonijiet Industrijali, Kap. 452; `sl/452.115/` l-Annual Leave National Standard Order), bit-titlu u t-test tal-bidu tagħha f’`title.md`. Kull fajl ta’ artikolu jispiċċa bin-noti li l-konsolidazzjoni tipprintja fil-marġni, bħal `- Amended by: ...; XX.2022.2; ...` (l-Att XX tal-2022, artikolu 2).

It-test huwa bl-Ingliż, mill-verżjonijiet konsolidati Ingliżi ta’ legislation.mt. It-test Malti, li għall-biċċa l-kbira tal-liġijiet jipprevali fejn it-tnejn ikunu differenti (l-artikolu 74 tal-Kostituzzjoni), mhuwiex parti minn dan ir-rekord.

## Mistoqsijiet bħala kmandi git

| Mistoqsija | Kmand |
| --- | --- |
| Kull bidla fl-artikolu 2 tal-Att dwar l-Impjiegi u r-Relazzjonijiet Industrijali | `git log -p --word-diff -- cap/452/2.md` |
| Liema liġi kitbet kull linja tal-artikolu 2? | `git blame cap/452/2.md` |
| Kull verżjoni tal-Att, bil-jum li fih daħlet fis-seħħ kull waħda | `git log --format="%h %(trailers:key=In-force,valueonly,separator=)%(trailers:key=Consolidated,valueonly,separator=) %an" -- cap/452` |
| L-artikolu 2 kif kien fis-seħħ fl-1 ta’ Jannar 2024 | `python tools/in_force_on.py 2024-01-01 cap/452 2` |

**Barra minn git**, dan ir-rekord nospitawh ukoll pubblikament, b’xejn:

- **[Staqsi lil Claude dwar il-liġi Maltija](https://global-law.lexifina.com/v1/try_claude?country=malta)**: jiftaħ Claude bl-ewwel mistoqsija diġà lesta.
- **[Staqsi lil ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=malta)**: l-istess mistoqsija f’ChatGPT.
- **[Fittex fil-liġi Maltija fis-sit tagħna](https://lexifina.com/law?country=malta&q=annual+leave)**: tfittxija għal “annual leave” (leave annwali), bit-test ta’ kull dispożizzjoni u l-verżjonijiet tagħha, mingħajr kont.
- **[REST API għall-iżviluppaturi](https://global-law.lexifina.com/v1/search_law?query=annual+leave&jurisdiction=malta)**: l-istess tfittxija bħala JSON, mingħajr ċavetta. Id-dokumentazzjoni tinsab [hawn](https://lexifina.com/api/global-law).

Iż-żewġ assistenti jaqraw ir-rekord permezz tal-konnettur b’xejn Global law (MCP, `https://global-law.lexifina.com/mcp`); l-ewwel darba, iċ-chat jagħtik il-link li jżidu. Staqsi bl-Ingliż jew bil-Malti.

**Tista’ tħaddmu faċilment int stess.** Ikollok bżonn biss git u Python, u l-għodod jaħdmu fuq il-kompjuter tiegħek:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add malta/national/acts
python3 tools/law.py show 2026-01-01 malta/national/acts/cap/452/2.md
```

Miftuħ f’Claude Code, Cursor, VS Code jew Codex, il-klonu jibda wkoll server MCP lokali bl-istess għodod ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Id-dati

Kull commit huwa datat f’nofsinhar, ħin ta’ Malta (Europe/Malta), fil-punt fiż-żmien tal-verżjoni ta’ legislation.mt li fiha jinsab (il-jum minn meta japplika dak it-test), u jġorr dak il-jum f’trailer:

- bidla: `In-force:`, il-punt fiż-żmien tal-ewwel verżjoni li turiha, bil-jum tal-pubblikazzjoni tal-liġi emendatorja f’`Published:` fejn legislation.mt jagħtih;
- l-ewwel verżjoni ta’ kull liġi fuq legislation.mt: `Consolidated:`. Hija commit wieħed (`Kind: consolidated`) bit-test kollu u bl-istorja marġinali ta’ kull artikolu, għalhekk il-bidliet ta’ qabel huma rreġistrati hemm, mhux bħala commits;
- git ma jistax jaħżen dati ta’ qabel l-1970, għalhekk il-15-il commit ta’ qabel (mit-28 ta’ Ġunju 1834) huma datati mill-1970-01-01, sekonda bejn wieħed u ieħor, bil-jum veru fit-trailer. Biex tistaqsi għal data, uża `tools/in_force_on.py`, mhux `git log --before`;
- commit ippubblikat qatt ma jinkiteb mill-ġdid: il-2,583 liġi li l-ewwel verżjoni tagħhom kienet datata jum tard għandhom commits `Kind: correction` aktar tard (3,222 b’kollox) li jsemmu l-ġranet li jikkoreġu, u `tools/in_force_on.py` japplikahom.

Kull bidla hija attribwita lill-Att jew lill-Avviż Legali li għamilha (`Act XX of 2022`, `L.N. 265 of 2026`), skont l-evidenza fil-konsolidazzjoni, mill-aktar b’saħħitha (`Evidence:`): ċitazzjoni ġdida fil-marġni tal-artikolu, liġi ġdida waħda biss iċċitata fil-verżjoni, liġi relatata waħda biss ippubblikata bejn iż-żewġ verżjonijiet, u żewġ regoli oħra li jintużaw inqas. B’hekk hemm 1,965 commit ta’ emenda minn 1,817 liġi; l-ewwel verżjoni ta’ kull liġi, u l-244 bidla li ma jistgħux jiġu attribwiti lil ebda liġi (`Kind: unexplained`), huma attribwiti lill-Unità tal-Leġiżlazzjoni.

## Kif jiġi vverifikat

- `tools/build/` fih il-build kif tħaddem (`build.py`, `parse_pdf.py`, `docs.py`, bis-sha256 tagħhom f’`REPRODUCE.md`). Mill-istess PDFs, li s-sha256 tagħhom jinsab f’[`data/pdf-sha256.tsv`](data/pdf-sha256.tsv), jagħti l-istess hashes tal-commits.
- L-ispazji, il-virgoletti kurvi, id-dashes u s-soft hyphens jiġu normalizzati, biex it-tipografija waħedha qatt ma toħloq bidla; il-verżjonijiet li l-PDF tagħhom ma setax jinqara jitniżżlu f’lista minflok ma jiġu ndovinati.
- L-istorja tiżdied biss: commit żbaljat jiġi kkoreġut b’ieħor aktar tard (`Corrects:`, `Supersedes:`, `Reason:`) u qatt ma jinkiteb mill-ġdid. Ara [`REPRODUCE.md`](REPRODUCE.md).
- [vulnerabilities/](vulnerabilities/README.md): żbalji possibbli fit-tfassil tal-liġi Maltija, misjuba mid-detetturi ta’ global-law u vverifikati bl-idejn.

## X’ma jurix

- **Il-Kostituzzjoni ta’ Malta**, li legislation.mt jippubblika separatament mill-Kapitli, u **l-ġurisprudenza**.
- **It-test Malti** (ara hawn fuq).
- **It-test ta’ qabel l-ewwel verżjoni ta’ kull liġi fuq legislation.mt**, ħlief kif l-istoriji marġinali tagħha jelenkaw il-liġijiet li biddluha.
- **Verżjonijiet li ma setgħux jinqraw**: 43 (41 minnhom b’test Malti fl-indirizz Ingliż), elenkati f’[`data/unreadable.csv`](data/unreadable.csv); minħabba fihom, 31 liġi m’għandhomx test.
- **Dħul fis-seħħ aktar tard mill-punt fiż-żmien ta’ verżjoni, u regoli ta’ salvagwardja u tranżitorji**: dawn jinsabu fil-liġijiet emendatorji, fil-link `Source:` ta’ kull commit.
- **In-noti f’qiegħ il-paġna**, u t-tabella tal-arranġament fil-bidu ta’ kull Kapitlu.

## Sorsi

| Sors | Tip | Verżjonijiet preċedenti | Noti |
| --- | --- | --- | --- |
| [legislation.mt](https://legislation.mt) (l-Unità tal-Leġiżlazzjoni, Gvern ta’ Malta) | Liġijiet konsolidati uffiċjali: Kapitli u leġiżlazzjoni sussidjarja | iva, verżjoni konsolidata għal kull punt fiż-żmien | Il-PDF Ingliż ta’ kull verżjoni, il-paġna ta’ kull liġi (il-verżjonijiet u l-liġijiet relatati magħha) u s-sitemap ELI; it-test awtorevoli huwa dak tal-Gazzetta tal-Gvern |

## Liċenzja

Ara [`LICENSE`](LICENSE). L-Att dwar id-Drittijiet tal-Awtur (Kap. 415, artikolu 2) jeskludi “any written law” (kull liġi miktuba) mix-xogħlijiet letterarji, ħlief kif provdut fl-artikolu 12 tal-Att tal-1980 dwar ir-Reviżjoni tal-Liġijiet Statutarji (Statute Law Revision Act, 1980); it-testi huma riprodotti mingħajr bidla fil-kliem tagħhom. Il-kontribuzzjonijiet proprji ta’ Lexifina (l-għodod, l-arranġament tal-fajls, il-messaġġi tal-commits u d-dokumentazzjoni) huma CC0 1.0.

Din hija traduzzjoni tal-verżjoni Ingliża ([README.en.md](README.en.md)); jekk ikun hemm differenza, tipprevali l-verżjoni Ingliża.

## Viżwalizzazzjonijiet

- [visualisations/](visualisations/): graffs magħmula minn dan ir-repożitorju. Għadhom ma sarux.

## Aktar

Mir-repożitorju [lexifina/global-law](https://github.com/lexifina/global-law) (bl-Ingliż):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): il-funzjonijiet kollha u x’għandu jappoġġja kull korpus (`git blame`, `law.py`, għodod MCP)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): mistoqsijiet u tweġibiet · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): kif tipproponi bidliet · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): is-server MCP · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): kif inbena · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): kemm hu aġġornat kull korpus · [Monitoraġġ](https://github.com/lexifina/global-law/tree/main/monitoring): jekk l-aġġornamenti humiex jaħdmu · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): kif kull sors uffiċjali jiġi segwit għal bidliet
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): kemm huma veloċi l-għodod, imkejla
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): graffs u konnessjonijiet madwar il-liġi tad-dinja kollha
- [Vulnerabbiltajiet](https://github.com/lexifina/global-law/tree/main/vulnerabilities): żbalji fil-liġijiet kif ġew ippubblikati
