# EU AI Act Evidence Crosswalk + Rights-Aware Risk Register

**What this is, in one paragraph.** A binding law (EU AI Act, Regulation (EU) 2024/1689), a certifiable management-system standard (ISO/IEC 42001:2023) and a voluntary outcome framework (NIST AI RMF 1.0) are three different kinds of object, so this repository does **not** claim they are equivalent. The **EU AI Act obligation is the spine** of every row. ISO 42001 controls and NIST AI RMF subcategories are mapped as **evidence an organisation can point to** when showing it is working toward that obligation, with an honest verdict on how far each gets you and a named residual gap. The headline output answers the question a client actually asks: **"We are ISO 42001 certified - what AI Act obligations are we still exposed on?"** (See [docs/GAP_ANALYSIS.md](docs/GAP_ANALYSIS.md).)

> **Not legal advice.** This is a professional analysis by the author, not a legal opinion, and not a statement that any organisation is or is not compliant. Verdicts are judgement calls (see Methodology limits). Re-verify against the Official Journal before operational use.

## The three things to know before you read a single row

1. **ISO/IEC 42001 certification does not, by itself, confer presumption of conformity with the AI Act.** Presumption flows from harmonised standards whose references are published in the Official Journal (Art. 40), developed through CEN-CENELEC JTC 21. ISO 42001 sits outside that programme. As of the newest source I could retrieve (15 Sep 2026) **no AI Act harmonised standard is cited in the OJ yet**. Details: [docs/HARMONISED_STANDARDS.md](docs/HARMONISED_STANDARDS.md).
2. **The high-risk timeline has moved.** Regulation (EU) 2026/1744 (the "Digital Omnibus on AI", in force 27 Jul 2026) moved high-risk obligations to **2 Dec 2027** (Annex III) and **2 Aug 2028** (Annex I). Details and what I could not verify: [docs/TIMELINE.md](docs/TIMELINE.md).
3. **Every row has an actor role and a risk tier.** The row key is the triple **(obligation, actor role, risk tier)**. An obligation that binds a provider may not bind a deployer at all.

## Scope

- **In scope:** high-risk AI systems (Chapter III) and general-purpose AI models (Chapter V), plus Art. 4 AI literacy as a horizontal duty because it binds every provider and deployer.
- **Out of scope (deliberately):** prohibited practices (Art. 5), limited-risk transparency (Art. 50), minimal-risk systems, penalties procedure, governance bodies, and sector-specific rules for Annex I products. Covering all four tiers exhaustively would bloat the work without adding value.
- **Rows:** 46 (target was roughly 30-45; the actor-role split is why it is at the top of that range).

## Actor roles assumed

| Role | Rows | Notes |
|---|---|---|
| Provider (high-risk) | 25 | Most requirements (Arts. 9-20, 43-49, 72-73) bind the provider. A deployer, importer or distributor can **become** the provider under Art. 25(1) - see `PRV-HR-A25-CHAIN`. |
| Deployer (high-risk) | 9 | Arts. 4, 26, 27, 86. Row IDs start `DEP-`. |
| Importer / Distributor | 1 / 1 | Arts. 23, 24. |
| GPAI model provider | 10 | Arts. 53-55. Tier is `GPAI` or `GPAI with systemic risk`. |

No row silently assumes "provider". If a row is not labelled `Provider`, it is not a provider obligation.

## Repository layout

```
crosswalk/crosswalk.csv         46-row crosswalk (UTF-8 with BOM, opens cleanly in Excel)
crosswalk/crosswalk.xlsx        same data + summary + "ISO-certified gap view" sheet
crosswalk/_src/                 row sources (r1-r5.py) - edit here, then rebuild
register/risk_register.xlsx     risk register with live formulas, dropdowns, scoring sheet, 2 worked examples
register/risk_register_worked_examples.csv
register/SCORING_METHODOLOGY.md anchored scales, caps, bands, limitations
docs/GAP_ANALYSIS.md            "We are ISO 42001 certified - what are we exposed on?"
docs/TIMELINE.md                phased application timeline, as-of stamp, verification status
docs/HARMONISED_STANDARDS.md    presumption-of-conformity mechanism + JTC 21 pipeline
docs/RED_TEAM.md                the 11 hardest attacks on this work, with answers and honest weak points
docs/SOURCES.md                 sources and how each was used
scripts/                        build + validation (python3 scripts/build_crosswalk.py && ...)
```

## Columns

`obligation_id` | `eu_ai_act_article` | `obligation_plain_words` | `actor_role` | `risk_tier` | `application_date` | `omnibus_2026_1744_status` | `iso42001_clause_or_control` | `iso42001_verdict` | `iso27001_2022_supplementary` | `iso27001_verdict` | `nist_ai_rmf_subcategory` | `nist_verdict` | `residual_gap` | `implementation_note` | `harmonised_standard_pipeline`

Three columns go beyond the original brief, on purpose: the **Omnibus status** (so no reader mistakes the 2024 text for current law), the **ISO/IEC 27001:2022 supplementary** columns (the organisation that holds 42001 usually also holds 27001, and 27001 is the strongest evidence for the cybersecurity, logging and incident rows), and the **harmonised-standard pipeline** (what would turn "evidence" into "presumption").

## Verdict vocabulary

| Verdict | Meaning |
|---|---|
| **Substantially evidences** | Implementing the control goes most of the way to demonstrating conformity. A named gap may still remain. |
| **Partially evidences** | Helps, but leaves a named gap. |
| **Adjacent** | Related in subject matter; does **not** evidence conformity. |
| **No coverage** | Nothing in the framework speaks to this obligation. (A row with no coverage cites no reference.) |

No row is rated "fully covers". That is deliberate.

## Version stamps (what each source is and which version I used)

| Source | Version used | Note |
|---|---|---|
| Regulation (EU) 2024/1689 | OJ L, 12.7.2024 text supplied with the project (article numbering) | **Not a consolidated text.** Amendments by Regulation (EU) 2026/1744 were overlaid from secondary sources and are flagged per row. |
| Regulation (EU) 2026/1744 | Published OJ 24 Jul 2026; in force 27 Jul 2026 | Researched via secondary sources; **OJ text not directly retrieved.** |
| ISO/IEC 42001:2023 | Annex A identifiers from the author's metadata skeleton; main-body clause numbers from the author's Lead Implementer knowledge | Clause numbers (`cl. x.y`) are **not verified against the skeleton**; check them against your licensed copy. |
| ISO/IEC 27001:2022 | Annex A identifiers from the author's metadata skeleton | Supplementary column only. |
| NIST AI RMF 1.0 (NIST AI 100-1, Jan 2023) | Full text supplied; subcategory numbers machine-checked | The Playbook is a living web resource with no version number; NIST's page shows "Updated June 10, 2026" and says the Playbook will be updated after the AI RMF is revised. No AI RMF 1.1 was identified. |
| **Timeline** | **As of 2 October 2026** | **Subject to ongoing legislative amendment.** |

## Copyright statement (ISO)

**ISO 42001 control text is not reproduced.** Controls are referenced by number with author-written intent summaries, per ISO copyright terms. The same applies to ISO/IEC 27001. The validator (`scripts/build_crosswalk.py`) rejects cells that contain quotation marks or are unusually long as a heuristic guard, and checks every cited Annex A number against the identifier list. It cannot prove that no paraphrase is too close to the source - the author should read the intent summaries against a licensed copy before publishing. NIST AI RMF is US government work. EU legislation is reproduced/quoted with attribution (Decision 2011/833/EU on reuse of Commission documents; OJ L, 12.7.2024).

## Methodology and its limits

- **Intent alignment, not literal correspondence.** NIST AI RMF subcategories are deliberately non-prescriptive outcomes; I mapped them by intent alignment to the obligation. "Adjacent" exists precisely to mark topical relatedness that is not evidence of conformity.
- **Verdicts are judgement.** They were not produced by any measurement and have not been independently reviewed. Two practitioners could reasonably differ by one step on many rows. The `residual_gap` column states the reasoning so a reader can disagree specifically.
- **The percentages in the gap analysis describe this row selection**, not "how compliant" anyone is.
- **Secondary-source dependency.** The 2026 amendments and the standards pipeline status come from law-firm notes and public trackers. See TIMELINE.md for exactly what was and was not verified.
- **Evidence is not effectiveness.** A control that "partially evidences" an obligation only helps if it operates. The register handles that with an effectiveness cap and an evidence requirement.

## The risk register (`/register/`)

- Every risk row cites a **Linked Crosswalk Obligation ID**; actor role, tier and the ISO verdict are looked up from the crosswalk by formula, so the two cannot drift.
- **Two impact scales, scored separately:** harm to *persons* (the Act's sense of risk) and harm to the *organisation* (enterprise-risk sense). The inherent score is the **max** of the two, never an average, and a "driver" column shows which one won.
- **Anchored scales** (each point defined in words), a stated **ordinal-not-cardinal** caveat, and a **rights floor** so severe harm to individuals cannot hide under a Medium score.
- Control effectiveness is **capped by the crosswalk verdict**, so an ISO certificate cannot be over-credited.
- Two **illustrative** worked rows (fictional systems): one high-risk (recruitment ranking), one GPAI (copyright policy). Owners are roles, not names.

## Rebuild and validate

```bash
pip install openpyxl
python3 scripts/build_crosswalk.py   # validates IDs, verdict vocabulary, copyright heuristics; writes CSV + XLSX
python3 scripts/build_register.py    # writes the register workbook
python3 scripts/build_docs.py        # regenerates GAP_ANALYSIS.md and SCORING_METHODOLOGY.md
```

The register workbook was recalculated in LibreOffice and the formula results matched an independent Python computation for both worked examples.

## What is different from three public documents in a spreadsheet

1. **Law-anchored architecture** - obligations are the spine; frameworks are evidence, with a verdict and a residual gap per row.
2. **Actor role and risk tier as part of the row key** - no silent "provider" assumption.
3. **Harmonised-standards finding with live pipeline status** - why a certificate is not a presumption, and what would change that.
4. **ISO-certified-organisation gap view** - the question clients pay for.
5. **Rights-aware register wired to the crosswalk by ID** - dual scoring, anchored scales, verdict-derived control caps.
6. **Post-Omnibus awareness and machine-checked identifiers** - every ISO Annex A, 27001 Annex A and NIST subcategory cited is validated against an identifier list.

## Licence

See [LICENSE.md](LICENSE.md).
