# Red team: the 11 hardest attacks on this work

Each entry gives the attack, the answer, where in the repository the answer lives, and the **honest weak point** that remains. A defence with no stated weak point is a sales pitch, so every entry has one.

*Position as of 2 October 2026. Re-verify against the Official Journal before operational use.*

---

## Part A - The crosswalk

### 1. "You crosswalked a management standard, a voluntary framework and a binding law as if they were comparable. That is a category error."

**Answer.** The repository does not claim they are comparable. The first paragraph of the README says so. The AI Act obligation is the spine of every row; ISO 42001 and NIST AI RMF are mapped as *evidence an organisation can point to*, with a verdict and a named residual gap. No row is rated "fully covers".
**Where.** README, first paragraph and "Verdict vocabulary"; `residual_gap` column.
**Weak point.** The verdict vocabulary still uses one scale for two very different evidence types (a certifiable control vs an open-ended outcome). That is a simplification. The `residual_gap` text carries the real reasoning, and a reader who looks only at the verdict column will lose nuance.

### 2. "So if I get ISO 42001 certified, I am AI Act compliant, right?"

**Answer.** No. Presumption of conformity flows from harmonised standards whose references are published in the Official Journal (Art. 40), produced through CEN-CENELEC JTC 21. ISO 42001 is outside that programme. Also, most AI Act duties attach to a *system* or a *legal act* (declaration of conformity, CE marking, registration), not to an organisation's management system. In this crosswalk 5 of 46 rows are "No coverage" and 14 more are "Adjacent" for ISO 42001.
**Where.** `docs/HARMONISED_STANDARDS.md`; `docs/GAP_ANALYSIS.md`.
**Weak point.** The pipeline status comes from public trackers (latest entry 15 Sep 2026), not from CEN-CENELEC or the OJ directly. EN 18286 is reported as published but not yet OJ-cited; I could not confirm that nothing was cited between 15 Sep and today. The EN 18286-to-ISO 42001 annex mapping is single-source.

### 3. "Which actor role does this assume?"

**Answer.** Every row carries an explicit actor role and a risk tier; the row key is the triple. No row silently assumes "provider". The README table counts rows per role.
**Where.** README "Actor roles assumed"; `actor_role` and `risk_tier` columns; row IDs begin `PRV-`, `DEP-`, `IMP-`, `DIS-`, `GPP-`.
**Weak point.** Role is not static. Under Art. 25(1) a deployer can become a provider. I handled this with one row (`PRV-HR-A25-CHAIN`), but a real engagement needs a per-system role determination first, which this repository does not do for anyone.

### 4. "The AI Act timeline has moved. Is this current?"

**Answer.** It moved: Regulation (EU) 2026/1744 pushed high-risk obligations to 2 Dec 2027 (Annex III) and 2 Aug 2028 (Annex I). The README and TIMELINE.md carry an "as of 2 October 2026" stamp, say the position is subject to ongoing amendment, and list what I did and did not verify. The 2024 text supplied with the project predates the amendment, so each row has an Omnibus-status column.
**Where.** `docs/TIMELINE.md`; README "Version stamps"; `omnibus_2026_1744_status` column.
**Weak point.** This is the biggest verification gap. I could read the recitals and early articles of the OJ text of 2026/1744 but **not the operative Art. 113 amendment** (the fetch tool cut the document off around Art. 57). Recital 40, the amended-Art.-4 text and several law-firm sources agree on fixed dates and a softened Art. 4. A "conditional" reading appears in some sources; it traces to the Commission's earlier proposal or to the Art. 111(2) legacy-systems rule, not to the adopted dates. Article-level amendments beyond Arts. 4, 4a, 43(3) and 57 are secondary-sourced. Check the OJ text before relying on any of it.

### 5. "NIST AI RMF subcategories are deliberately non-prescriptive. How did you map open-ended outcomes to specific legal obligations?"

**Answer.** By intent alignment, not literal correspondence. This is named as a limitation in the README. "Adjacent" marks topical relatedness that does not evidence conformity.
**Where.** README "Methodology and its limits".
**Weak point.** Intent alignment is a judgement call and was done by one author (me, with no independent review). Two practitioners could land one verdict step apart on many rows. All NIST subcategory IDs were machine-checked for existence, but existence is not the same as appropriateness.

### 6. "This is three public documents in a spreadsheet. What is your contribution?"

**Answer.** Six things: law-anchored architecture with a residual-gap column; actor role and tier in the row key; the harmonised-standards finding with live pipeline status; the ISO-certified gap view; a rights-aware register wired to the crosswalk by ID; and post-Omnibus awareness with machine-validated identifiers.
**Where.** README last section.
**Weak point.** None of these is secret knowledge. The value is in the judgement per row, and that judgement has not been peer reviewed. Treat this as a well-structured first draft by a practitioner, not an authoritative reference.

### 7. "Did you reproduce ISO standard text?"

**Answer.** No. Controls are cited by number with author-written intent summaries. The README says so in the copyright statement. A validator rejects cells containing quotation marks or longer than 420 characters, and checks every cited number against the identifier list.
**Where.** README "Copyright statement (ISO)"; `scripts/build_crosswalk.py`.
**Weak point.** A script cannot detect a paraphrase that is too close to the source. The intent summaries were written from my knowledge and the author-supplied metadata skeleton, not by copying, but **the author, as a Lead Implementer holding a licensed copy, should read them against the standard before publishing.** Separately, the Annex A identifier list is not verified against a licensed copy; its provenance and limits are stated in the README and `docs/AUDIT_LOG.md`. Main-body clause numbers were removed on 2 Oct 2026 because they could not be verified.

---

## Part B - The risk register

### 8. "Your 1-5 scale is arbitrary."

**Answer.** Partly true of all risk scoring. Each scale point for likelihood, rights impact and organisational impact is defined in words, and the ordinal-not-cardinal limitation is named in the methodology sheet.
**Where.** `register/SCORING_METHODOLOGY.md`; the "Scoring Methodology" sheet.
**Weak point.** The anchors are my construction. The organisational-impact top anchor references Art. 99/101 fine ceilings, which I took from the 2024 text; amendments may have changed thresholds for some actors. Multiplying ordinals is methodologically imperfect, and the register's MAX-of-two-scores rule is a design choice, not a theorem.

### 9. "Risk to whom?"

**Answer.** Two impact scales, scored separately: harm to persons (the Act's sense) and harm to the organisation (enterprise sense). The inherent score is the maximum of the two, never an average, and a driver column shows which dimension won. A rights floor prevents severe harm to individuals from sitting under a Medium rating.
**Where.** README "The risk register"; register "Scoring Methodology" sheet.
**Weak point.** The Act's "risk" is about health, safety and fundamental rights across the population affected; a single 1-5 rights-impact number for one risk row compresses a lot. It does not replace a proper fundamental-rights impact assessment (Art. 27).

### 10. "Who owns these risks?"

**Answer.** Owners are roles, not names (for example "Head of AI Product (accountable); Chief Data Officer (responsible); DPO (consulted)" and "General Counsel (accountable); Head of Data Acquisition (responsible)"). Treatment, target and review dates are columns.
**Where.** `register/risk_register.xlsx`, Register sheet, worked examples.
**Weak point.** The two worked rows are **fictional and illustrative**, and their evidence references (`EV-A10-BIAS-001`, `EV-A53-COPY-001`) are placeholders, not real evidence. A register with invented evidence refs would be fabrication; they are labelled as placeholders for that reason.

### 11. "How does this connect to your crosswalk?"

**Answer.** Every risk row must cite a Linked Crosswalk Obligation ID. Actor role, tier and the ISO verdict are looked up from the crosswalk by formula, and the control-effectiveness rating is capped by that verdict so an ISO certificate cannot be over-credited.
**Where.** Register sheet formulas; `register/SCORING_METHODOLOGY.md` "Cap derived from the crosswalk verdict".
**Weak point.** The lookup reads a snapshot of the crosswalk IDs held in the workbook ("Crosswalk IDs" sheet). If the crosswalk is rebuilt and obligation IDs change, the register's snapshot must be regenerated with `scripts/build_register.py`. The link is live inside the workbook, not across files.

---

## Things nobody has attacked yet but should

- **Row selection bias.** The percentages in the gap analysis describe *my 46 rows*, chosen to represent high-risk and GPAI duties. A different row split would change the percentages. They are not a compliance score.
- **Verdicts are single-author.** No second reviewer, no client validation. The author's own Lead Implementer review is the minimum step before publishing.
- **Scope exclusions matter.** Art. 5 prohibitions, Art. 50 transparency (which applies from 2 Aug 2026) and sector-specific Annex I rules are out of scope. A client with a chatbot or emotion-recognition use case may be exposed under provisions this repository does not cover.
- **Not legal advice.** Said in the README; repeated here because it is the line most likely to matter if someone relies on a verdict.
