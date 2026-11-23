<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoraġġ: x’jinqara u x’ħareġ minnu

[English](README.en.md)

Kif global-law jimmonitorja kull pajjiż: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Din il-paġna hija l-istess għal Malta biss: kull darba li jinqara sors uffiċjali, meta, u x’ħareġ minnu (liġijiet miżjuda, mibdula u mneħħija). Il-forma li tinqara mill-magni hija [data/checks/](../data/checks/) (JSON Lines, skema `lexifina-check/1`), f’`git log` bħala commits `Kind: check`, u xahar b’xahar f’[checks/](checks/).

**L-aħħar verifika:** 2026-11-23 09:54 UTC, Gazzetta tal-Gvern: Atti u Avviżi Legali (kif elenkati fuq legislation.mt): indirizzi moqrija: 84; 0 miżjuda, 0 mibdula, 0 imneħħija; l-ebda bidla; mhux ippubblikati: 70, minnhom mingħajr raġuni: 0. Twissijiet: `publish-lag`.

## Sorsi

| Sors | Folders | Kemm-il darba | L-aħħar verifika li rnexxiet | L-aħħar riżultat | Stat |
| --- | --- | --- | --- | --- | --- |
| [legislation.mt: Liġijiet ta’ Malta (Kapitli u leġiżlazzjoni sussidjarja)](https://legislation.mt/Legislation) | `cap/`, `sl/`, `laws.csv` | kuljum | 2026-11-23 02:35 UTC | l-ebda bidla | taħt osservazzjoni: jitqabblu l-verżjonijiet konsolidati bl-Ingliż, għax dan ir-repożitorju għandu t-test Ingliż |
| [Gazzetta tal-Gvern: Atti u Avviżi Legali (kif elenkati fuq legislation.mt)](https://legislation.mt/eli/eli-update-feed.atom) | `cap/`, `sl/` | kuljum | 2026-11-23 09:54 UTC | l-ebda bidla | taħt osservazzjoni: is-sit tal-Gazzetta stess (gov.mt) iwieġeb lill-qarrejja awtomatiċi bi sfida tal-browser, għalhekk l-Atti u l-Avviżi Legali tagħha jinqraw fuq legislation.mt; il-bidliet tagħhom jaslu f’dan ir-repożitorju permezz tal-verżjonijiet konsolidati ta’ legislation.mt |

## L-aħħar 30 jum

| Bdiet (UTC) | Sors | Moqrija | Miżjuda | Mibdula | Imneħħija | Mhux ippubblikati (mingħajr raġuni) | Riżultat | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-23 09:52](checks/2026-11.md#mt-gazette-20261123t095225z) | gazette | 84 | 0 | 0 | 0 | 70 (0) | l-ebda bidla `publish-lag` | — |
| [2026-11-23 02:33](checks/2026-11.md#mt-legislation-mt-20261123t023312z) | legislation-mt | 84 | 0 | 0 | 0 | 93 (0) | l-ebda bidla `publish-lag` | — |

## Ivverifika int stess

```
python tools/checktrail.py                      # l-aħħar verifika ta’ kull sors
python tools/checktrail.py --day 2026-11-23     # kull verifika ta’ jum
python tools/checktrail.py --act <id>           # meta liġi dehret u ġiet ippubblikata
git log --grep='^Kind: check' --format='%ci %s'  # il-verifiki fl-istorja
```

Il-pubblikazzjoni uffiċjali biss għandha saħħa legali; it-testi hawn huma kopji biex jinqraw u jitfittxu.
