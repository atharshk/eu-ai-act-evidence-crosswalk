# Verification log

*Run on 2 October 2026 against the 46-row crosswalk. One reviewer, no independent second reading. The purpose of this document is to say exactly what was checked, how, what was found, and what was **not** checked.*

## What was checked, against what

| Claim type | Count | Source checked against | Method | Result |
|---|---|---|---|---|
| EU AI Act article citations | 46 rows citing **30 distinct articles** (3, 4, 6, 9-15, 17, 19, 20, 22-27, 42, 43, 47-49, 53-55, 72, 73, 86), plus Art. 4a and Annexes IV, V, XI, XII | Regulation (EU) 2024/1689, OJ L 12.7.2024 (the text supplied with the project) | Script parsed each article / paragraph / point reference and looked it up in the extracted text (all 113 articles located). | All references resolve. 2 flags, both explained: Art. 4a does not exist in the 2024 text (it is inserted by the Omnibus, expected); Art. 3(49) is a definition point, not a paragraph (it is "serious incident", as the row says). |
| Omnibus (2026/1744) status per row | 46 rows: 24 "date moved only", 10 "substantive duties unchanged", 12 "amended or new" | Regulation (EU) 2026/1744 | **Partly read.** Recitals and early articles of the OJ text were readable; the tool cut the text off before the operative Art. 113. Everything else from secondary sources. | See `TIMELINE.md` for item-by-item status. **Not primary-verified at article level.** |
| ISO/IEC 42001 Annex A identifiers | 85 citations of **33 distinct identifiers** (of 38 in the list; not cited: A.2.3, A.2.4, A.3.3, A.4.4, A.6.2.5) | A reference list identical to the author-supplied "metadata skeleton" file (38 = 38, diffed by script); identifiers also compared with two public listings (one from the Singapore AI Verify Foundation, one vendor page): they agree. A third public page listed different, evidently wrong, identifiers, which is why no single public page was trusted. | Validator checks every cited ID exists in the list. A second script compared the short description next to each ID with the skeleton title: 80 of 82 overlap; the other 2 are an abbreviation ("V&V") and a range description. | **Not checked against a licensed copy of the standard.** How the skeleton file itself was originally produced is not recorded in this repository. |
| ISO/IEC 27001:2022 Annex A identifiers | about 63 citations of about 36 distinct identifiers (regex-extracted, so approximate), in 26 rows | List generated from numeric ranges (5.1-5.37, 6.1-6.8, 7.1-7.14, 8.1-8.34 = 93) matching the counts in the author-supplied skeleton | Validator | **Not checked against a licensed copy.** Supplementary column only. |
| NIST AI RMF 1.0 subcategories | 98 citations of **48 distinct subcategories** (of 72), in 40 rows | NIST AI 100-1 (January 2023), full text supplied with the project | The list was reconciled by reading Tables 1-4 (GOVERN 19, MAP 18, MEASURE 22, MANAGE 13 = 72). Validator then checks every citation against the list. In addition, each row's subcategories were re-read against the obligation for subject-matter fit. | All IDs exist. No mapping was found where the subcategory is on a plainly different subject. Weakest link noted: `PRV-HR-A15-CYB` to MANAGE 3.2 (pre-trained model monitoring) bears only indirectly on Art. 15(5). |
| ISO main-body clause numbers | 17 clause-number references across 15 rows | None available | n/a | **All removed on 2 Oct 2026** because they could not be verified. See below. |

## Errors found and corrected

| Where | What was wrong | Correction |
|---|---|---|
| `PRV-HR-A17-QMS` | Cited the heading "A.6.2" as if it were a control; validator flagged it as an unknown identifier. | Replaced with the control range A.6.2.2-A.6.2.8. |
| Crosswalk size | 48 rows, above the 30-45 target. | Two rows deleted (`PRV-HR-A21-COOP`, `PRV-HR-A18-DOCRET`). 46 remain, noted in the README. |
| Gap analysis wording | Described the rejected standards drafts loosely. | Corrected to name the three drafts rejected at their first enquiry votes. |
| TIMELINE (Art. 4 / 4a) | One law-firm note described the Art. 4 amendment as a special-category-data change. | Followed the regulation text: Art. 4 = AI literacy softened; Art. 4a = bias-detection data processing. Recorded in `TIMELINE.md`. |
| README provenance | Said identifiers were "machine-checked" without saying what they were checked against. | Provenance now stated in the version-stamp table and in `scripts/refdata.py`; limit added to Methodology. |
| ISO main-body clauses | 17 clause-number references (for example for risk assessment, competence, internal audit) had been written from memory, not from the skeleton. | Removed. Rows now name the main-body topic without a number; the validator now rejects any `cl. N` or "clause N" in the ISO columns. |
| Omnibus quotation | A fetch returned a "verbatim" quotation of the article amending Art. 113. A later pass showed the text had been truncated before that point. | Quotation discarded as unverified; recorded in `TIMELINE.md`. |

Result of the article check on the 46 rows: no wrong article, paragraph or point numbers found.

## What was NOT verified

- **The operative Art. 113 amendment of Regulation (EU) 2026/1744.** The fixed-dates reading rests on recital 40 plus several law-firm sources; the standards-conditional reading appears to belong to the Commission's earlier proposal. Read the OJ point that replaces Art. 113 before relying on this.
- **Article-level Omnibus changes** other than Art. 4, 4a, 43(3) and 57 (Art. 10(5), 11, 17, 27(4), 42(3), 74/75 and the date of the new Art. 5 prohibitions) are secondary-sourced.
- **ISO/IEC 42001 and 27001 identifiers and titles against the published standards.** Everything depends on the supplied skeleton files and public listings.
- **Whether the intent summaries stay clear of the standards' own wording.** No script can test this; the author holds a licensed copy and should read them against it.
- **Post-15 September 2026 standards pipeline status** (CEN-CENELEC JTC 21), and whether the Commission has adopted the Art. 72(3) template, the Art. 73(7) guidance and the Art. 6 classification guidelines.
- **Legal effect.** Nothing here is legal advice.

## Limitations

- Single reviewer, no independent second reading.
- The checks verify that **citations point to provisions that exist and are on the claimed subject**. They do **not** validate the comparative verdicts in `iso42001_verdict`, `iso27001_verdict` and `nist_verdict`. Those are judgement calls, stated as such in the README, and two practitioners could differ by one step on many rows.
- A web-fetch tool was used to read legal texts and secondary sources. It truncates long documents and summarises rather than copies, so quotations from it are treated as leads, not citations.
