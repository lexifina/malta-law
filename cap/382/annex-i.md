## ANNEX I
## A B G
## n1
## 1
## aDestination n1
## b Journey time an3
## cTransport n1
## d ARC an21
## e Date and Time date Time
## G
## n..5
## date Time
## an13 authorised
## an.. 182
## an..65
## an..11
## an..10
## an..50
## a2
## an13
## an8
## 5
## a Tr a d e r an..16
## b Trader Name an.. 182
## c Street Name an..65
## d Street Number an..11
## e Postcode an..10
## f City an..50
## g NAD_LNG a2
## 6
## a Member State a2
## an.. b Serial Number 255
## 7
## an..22
## an..35
## Date
## Time
## an21
## 9X
## aImport an..21
## 10
## a O ff i c e an8
## 11
## a Guarantor Type n..4
## 12 2X
## a Trader Excise an13
## b VAT Number an..35
## c Trader Name an.. 182
## d Street Name an..65
## e Street Number an..11
## f Postcode an..10
## g City an..50
## h NAD_LNG a2
## 13
## a Transport Mode n..2
## 14
## a VAT Number an..35
## 99X
## n..2
## an.. 350
## 999x
## n..3
## an4
## n8
## d Quantity n.. 15,3
## e Gross Weight n.. 15,2
## f Net Weight n.. 15,2
## gAlcoholic n..5,2
## h Degree Plato n..5,2
## i Fiscal Mark an.. 350
## jFiscal a2
## kFiscal n1
## l Designation of an.. 350
## n..15
## n..5,2
## 99x
## aCategory n1
## b Wine-Growing n..2
## c Third Country a2
## dOther an.. 350
## eOther a2
## 17.2 99x .1
## a Wine Operation n..2
## 18 9x
## aShort an.. 350
## bShort a2
## cReference of an.. 350
## dReference of a2
## a ARC an21
## 2
## aCancellation n1
## an3
## N1
## date
## 4
## e S e a l a2
## f Complementary an.. 350
## g Complementary a2
## aNotification n1
## bNotification date Time
## an21 c ARC
## 2 9x
## 9x
## an..16
## an..4
## o Density n..5,2
## pCommercial an.. 350
## qCommercial a2
## r Brand Name of an.. 350
## s Brand Name of a2
## 11 99x
## aKind a2
## bNumber n..15
## cIdentity an..35
## d S e a l an.. 350
## a Date of arrival Date
## bGlobal n..2
## c Complementary an.. 350
## d Complementary a2
## 7 999X
## aBody Record n..3
## bIndicator a1
## cObserved n.. 15,3
## d Excise Product an4
## eRefused n.. 15,3
# annex-i
Table 1
(referred to in Article 3(1) and Article 8(1))
Draft electronic administrative document and electronic administrative document
Table 2
(referred to in Article 4(1))
Cancellation
Table 3
(referred to in Article 5(1) and 8(2))
Change of destination
Table 4
(referred to in the second subparagraph of Article 5(3), Article 5(6) and in point (b)
of Article 6(2))
Notification of change of destination/
Notification of splitting
Table 5
(referred to in Article 6(1) and Article 8(2))
Splitting operation
Table 6
(referred to in Article 7 and Article 8(3))
Report of receipt/Report of export
(referred to in Article 2)
Lists of codes
1. LANGUAGE CODES
These codes are extracted from the standard ISO 639.1 (Alpha-2 codes); in addition, two out-of-standard codes have been added to be used in conjunction with a Latin character version of languages using a non-Latin character set, i.e.:
- bt - Bulgarian (Latin character) - gr - Greek (Latin character) Code Description bg Bulgarian bt Bulgarian (Latin character) cs Czech da Danish nl Dutch en English et Estonian fi Finnish fr French ga Gaelic gr Greek (Latin character) de German el Greek hu Hungarian it Italian lv Latvian lt Lithuanian mt Maltese pl Polish pt Portuguese ro Romanian sk Slovak sl Slovenian (Slovene) es Spanish sv Swedish 2. ADMINISTRATIVE REFERENCE CODE
Field Content Field type Examples
1 Year Numeric 2 05 2 Identifier of the MS where the e-AD Alphabetic 2 ES
was initially submitted
3 Nationally assigned, unique code Alphanumeric 16 7R19YTE17UIC8J45 4 Check digit Numeric 1 9 Field 1 is last two digits of year of formal acceptance of movement. Field 3 must be filled with a unique identifier per EMCS movement. The way this field is used is under the responsibility of the Member States, but each EMCS movement must have a unique number.
Field 4 gives the check digit for the whole ARC that will help detect an error when keying the ARC.
3. MEMBER STATES
Must be identical to the codes of the standard ISO Alpha 2 code (1) (ISO 3166), limited to the Member States, except:
- For Greece, where EL instead of GR must be used. - For the United Kingdom, where GB instead of UK must be used.
4. COUNTRY CODES
Use the codes of the standard ISO Alpha 2 code (ISO 3166). 5. CUSTOMS OFFICE REFERENCE NUMBER (COR)
The COR is composed of an identifier of the Member State (see Code list 3) followed by a 6-digit alphanumeric national number, example IT0830AB.
6. GUARANTOR TYPE CODE Code Description 1 Consignor 2 Transporter 3 Owner of the Excise products 4 Consignee 12 Joint guarantee of the consignor and of the transporter 13 Joint guarantee of the consignor and of the owner of the Excise products 14 Joint guarantee of the consignor and of the consignee 23 Joint guarantee of the transporter and of the owner of the Excise products 24 Joint guarantee of the transporter and of the consignee 34 Joint guarantee of the owner of the Excise products and of the consignee 123 Joint guarantee of the consignor, of the transporter and of the owner of the Excise
products
124 Joint guarantee of the consignor, of the transporter and of the consignee 134 Joint guarantee of the consignor, of the owner of the Excise products and of the
consignee
234 Joint guarantee of the transporter, of the owner of the Excise products and of the
consignee
1234 Joint guarantee of the consignor, of the transporter, of the owner of the Excise
products and of the consignee
7. TRANSPORT MODE CODE Code Description 0 Other Code Description 1 Sea Transport 2 Rail transport 3 Road transport 4 Air transport 5 Postal consignment 7 Fixed transport installations 8 Inland waterway transport 8. TRANSPORT UNIT CODE Code Description 1 Container 2 Vehicle 3 Trailer 4 Tractor 9. PACKAGING CODES
Use the codes of Annex 38, box 31 of Regulation (EEC) No 2454/93 10. CANCELLATION REASON CODE Code Description 0 Other 1 Typing error 2 Commercial transaction interrupted 3 Duplicate e-AD 4 The movement has not begun at the date of dispatch 11. EXCISE PRODUCT EPC CAT UNIT Description A P D T200 T 4 Cigarettes, as defined in Articles 4(1) and 7(2) of N N N
Council Directive 95/59/EC T300 T 4 Cigars and cigarillos, as defined in Articles 3 and 7(1) N N N
of Directive 95/59/EC T400 T 1 Fine-cut tobacco for the rolling of cigarettes, as defined N N N
in Article 6 of Directive 95/59/EC T500 T 1 Other smoking tobacco, as defined in accordance with N N N
Articles 5 and 7(2) of Directive 95/59/EC
B000 B 3 Beer, as defined in Article 2 of Directive 92/83/EEC Y Y N W200 W 3 Still wine and still fermented beverages other than wine Y N N
and beer, as defined in Articles 8(1) and 12(1) of
Directive 92/83/EEC W300 W 3 Sparkling wine and sparkling fermented beverages Y N N
other than wine and beer, as defined in Article 8(2) and
12(2) of Directive 92/83/EEC I000 I 3 Intermediate products, as defined in Article 17 of Y N N
Directive 92/83/EEC S200 S 3 Spirituous beverages, as defined in Article 20, first, Y N N
second and third indent of Directive 92/83/EEC
S300 S 3 Ethyl alcohol, as defined in Article 20, first indent of Y N N
Directive 92/83/EEC, falling within CN codes 2207 and
2208, other than spirituous beverages (S200)
EPC CAT UNIT Description A P D S400 S 3 Partially denatured alcohol, falling within Article 20 of Y N N
Directive 92/83/EEC, being alcohol which has been
denatured but which does not yet fulfil the conditions to
benefit from the exemption foreseen in Article 27(1)(a)
or (b) of that Directive, other than spirituous beverages
(S200) S500 S 3 Products containing ethyl alcohol, as defined in Article Y N N
20, first indent of Directive 92/83/EEC, falling within
CN codes other than 2207 and 2208 E200 E 2 Vegetable and animal oils - Products falling within CN N N Y
codes 1507 to 1518, if these are intended for use as
heating fuel or motor fuel (Article 20(1)(a) of Council
Directive 2003/96/EC) E300 E 2 Mineral oils (energy products) - Products falling within N N Y
CN codes 2707 10, 2707 20, 2707 30, and 2707 50
(Article 20(1)(b) of Directive 2003/96/EC)
E410 E 2 Leaded petrol falling within CN codes 2710 11 31, N N Y
2710 11 51 and 2710 11 59 (Article 20(1)(c) of
Directive 2003/96/EC) E420 E 2 Unleaded petrol falling within CN codes 2710 11 31, N N Y
2710 11 41, 2710 11 45 and 2710 11 49 (Article
20(1)(c) of Directive 2003/96/EC) E430 E 2 Gasoil, unmarked falling within CN codes 2710 19 41 N N Y
to 2710 19 49 (Article 20(1)(c) of Directive 2003/96/
EC) E440 E 2 Gasoil, marked falling within CN codes 2710 19 41 to N N Y
2710 19 49 (Article 20(1)(c) of Directive 2003/96/EC)
E450 E 2 Kerosene, unmarked falling within CN codes 2710 19 N N Y
21 and 2710 19 25 (Article 20(1)(c) of Directive 2003/
96/EC) E460 E 2 Kerosene, marked falling within CN codes 2710 19 21 N N Y
and 2710 19 25 (Article 20(1)(c) of Directive 2003/96/
EC) E470 E 1 Heavy fuel oil falling within CN codes 2710 19 61 to N N N
2710 19 69 (Article 20(1)(c) of Directive 2003/96/EC)
E480 E 2 Products falling within CN codes 2710 11 21, 2710 11 N N Y
25, 2710 19 29 in bulk commercial movements (Article
20(1)(c) of Directive 2003/96/EC) E490 E 2 Products falling within CN codes 2710 11 to 2710 19 N N Y
69, not specified above, except products falling within
CN codes 2710 11 21, 2710 11 25, 2710 19 29 other
than in bulk commercial movements (Article 20(1)(c)
of Directive 2003/96/EC) E500 E 1 Liquefied petroleum gases and other gaseous N N N
hydrocarbons (LPG) of CN codes 2711 12 11 to 2711
19 00 (Article 20(1)(d) of Directive 2003/96/EC)
E600 E 1 Saturated acyclic hydrocarbons falling within CN code N N N
2901 10 (Article 20(1)(e) of Directive 2003/96/EC)
E700 E 2 Cyclic hydrocarbons falling within CN codes 2902 20, N N Y
2902 30, 2902 41, 2902 42, 2902 43 and 2902 44
(Article 20(1)(f) of Directive 2003/96/EC)
E800 E 2 Products falling within CN code 2905 11 00 (methanol N N Y
(methyl alcohol)), which are not of synthetic origin, if
these are intended for use as heating fuel or motor fuel
(Article 20(1)(g) of Directive 2003/96/EC)
EPC CAT UNIT Description A P D E910 E 2 Fatty-acid mono-alkyl esters, containing by volume N N Y
96,5% or more of esters (FAMAE) falling within CN
code 3824 90 99 (Article 20(1)(h) of Directive 2003/96/
EC) E920 E 2 Products falling within CN code 3824 90 99, if these N N Y
are intended for use as heating fuel or motor fuel -
others than Fatty-acid mono-alkyl esters, containing by
volume 96,5% or more of esters (FAMAE) (Article
20(1)(h) of Directive 2003/96/EC)
Note: The CN Codes used in the table for energy products are those of Commission Regulation (EC) No 2031/2001 (OJ L 279, 23.10.2001)
Legend of columns: EPC Excise Product Code CAT Excise product category UNIT Unit of measurement (from the list 12) A: Alcoholic strength must be given (Yes/No) P: Degree Plato may be given (Yes/No) D: Density at 15°C must be given (Yes/No) 12. UNITS OF MEASUREMENT Unit of measurement code Description 1 Kg 2 Litre (temperature of 15°C) 3 Litre (temperature of 20°C) 4 1 000 items
PART I
The additional codes to the Taric Codes for:
(a) alcohol and alcoholic beverages as listed in the Second
Schedule;
(b) energy products as listed in the Fourth Schedule; and
(c) goods listed in the Eighth Schedule,
shall be applicable as the additional codes for these above-mentioned products in their entirety as Part I of the Sixth Schedule to this Act.
- Added by: VII.2022.66.
