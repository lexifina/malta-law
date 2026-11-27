<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoraġġ: x’jinqara u x’ħareġ minnu

[English](README.en.md)

Kif global-law jimmonitorja kull pajjiż: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). Din il-paġna hija l-istess għal Malta biss: kull darba li jinqara sors uffiċjali, meta, u x’ħareġ minnu (liġijiet miżjuda, mibdula u mneħħija). Il-forma li tinqara mill-magni hija [data/checks/](../data/checks/) (JSON Lines, skema `lexifina-check/1`), f’`git log` bħala commits `Kind: check`, u xahar b’xahar f’[checks/](checks/).

**L-aħħar verifika:** 2026-11-27 05:24 UTC, Gazzetta tal-Gvern: Atti u Avviżi Legali (kif elenkati fuq legislation.mt): indirizzi moqrija: 6; 0 miżjuda, 2 mibdula, 0 imneħħija; instabu bidliet; mhux ippubblikati: 21, minnhom mingħajr raġuni: 0.

## Sorsi

| Sors | Folders | Kemm-il darba | L-aħħar verifika li rnexxiet | L-aħħar riżultat | Stat |
| --- | --- | --- | --- | --- | --- |
| [legislation.mt: Liġijiet ta’ Malta (Kapitli u leġiżlazzjoni sussidjarja)](https://legislation.mt/Legislation) | `cap/`, `sl/`, `laws.csv` | kuljum | 2026-11-27 05:24 UTC | instabu bidliet | taħt osservazzjoni: jitqabblu l-verżjonijiet konsolidati bl-Ingliż, għax dan ir-repożitorju għandu t-test Ingliż |
| [Gazzetta tal-Gvern: Atti u Avviżi Legali (kif elenkati fuq legislation.mt)](https://legislation.mt/eli/eli-update-feed.atom) | `cap/`, `sl/` | kuljum | 2026-11-27 05:24 UTC | instabu bidliet | taħt osservazzjoni: is-sit tal-Gazzetta stess (gov.mt) iwieġeb lill-qarrejja awtomatiċi bi sfida tal-browser, għalhekk l-Atti u l-Avviżi Legali tagħha jinqraw fuq legislation.mt; il-bidliet tagħhom jaslu f’dan ir-repożitorju permezz tal-verżjonijiet konsolidati ta’ legislation.mt |

## L-aħħar 30 jum

| Bdiet (UTC) | Sors | Moqrija | Miżjuda | Mibdula | Imneħħija | Mhux ippubblikati (mingħajr raġuni) | Riżultat | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-27 05:24](checks/2026-11.md#mt-gazette-20261127t052425z) | gazette | 6 | 0 | 2 | 0 | 21 (0) | instabu bidliet | — |
| [2026-11-27 05:04](checks/2026-11.md#mt-legislation-mt-20261127t050436z) | legislation-mt | 736 | 0 | 2 | 0 | 39 (0) | instabu bidliet `audit-disagrees` | [3](https://github.com/lexifina/malta-law/compare/66cdde84d4d3...4e697d58c954) |
| [2026-11-26 05:30](checks/2026-11.md#mt-gazette-20261126t053054z) | gazette | 9 | 0 | 3 | 0 | 23 (0) | instabu bidliet `audit-disagrees` | — |
| [2026-11-26 05:10](checks/2026-11.md#mt-legislation-mt-20261126t051013z) | legislation-mt | 743 | 0 | 4 | 0 | 39 (0) | instabu bidliet `audit-disagrees` | [4](https://github.com/lexifina/malta-law/compare/e13476ca3660...8af0d6bd6cc1) |
| [2026-11-25 05:27](checks/2026-11.md#mt-gazette-20261125t052755z) | gazette | 5 | 0 | 0 | 0 | 26 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-25 05:08](checks/2026-11.md#mt-legislation-mt-20261125t050821z) | legislation-mt | 729 | 0 | 0 | 0 | 39 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-24 00:25](checks/2026-11.md#mt-gazette-20261124t002526z) | gazette | 6 | 0 | 0 | 0 | 26 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-24 00:04](checks/2026-11.md#mt-legislation-mt-20261124t000443z) | legislation-mt | 739 | 0 | 0 | 0 | 41 (0) | instabu bidliet `audit-disagrees` | [3](https://github.com/lexifina/malta-law/compare/08a837235d8b...f910a6a07ddd) |
| [2026-11-24 00:04](checks/2026-11.md#mt-gazette-20261124t000420z) | gazette | 2 | 0 | 0 | 0 | 26 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-23 21:43](checks/2026-11.md#mt-legislation-mt-20261123t214330z) | legislation-mt | 5068 | 0 | 0 | 0 | 39 (0) | l-ebda bidla `verify-differ` `audit-disagrees` | — |
| [2026-11-23 21:42](checks/2026-11.md#mt-gazette-20261123t214212z) | gazette | 6 | 0 | 0 | 0 | 26 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-23 21:35](checks/2026-11.md#mt-legislation-mt-20261123t213542z) | legislation-mt | 233 | 0 | 0 | 0 | 39 (0) | il-verifika falliet | — |
| [2026-11-23 21:32](checks/2026-11.md#mt-gazette-20261123t213228z) | gazette | 9 | 0 | 0 | 0 | 26 (0) | l-ebda bidla `audit-disagrees` | — |
| [2026-11-23 21:21](checks/2026-11.md#mt-legislation-mt-20261123t212128z) | legislation-mt | 393 | 0 | 0 | 0 | 39 (0) | l-ebda bidla | [41](https://github.com/lexifina/malta-law/compare/5b4cb29d6cc1...ecedd7b51065) |
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
