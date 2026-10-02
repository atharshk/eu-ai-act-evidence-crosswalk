# Harmonised standards and the "ISO 42001 is not a shortcut" finding

> **Version stamp.** Status below is as reported by public trackers up to **15 September 2026** (the newest entry I could retrieve). The area is moving quickly; I would re-verify before relying on it.

## The mechanism (plain language)

1. The Act sets **requirements** for high-risk AI systems (Chapter III, Section 2: Arts. 8-15) and **obligations** for GPAI providers (Chapter V).
2. Art. 40(1): a system or model that conforms to a **harmonised standard whose reference has been published in the Official Journal** is **presumed** to meet the requirements that standard covers. That presumption is the only "shortcut" the Act builds in (alongside common specifications under Art. 41, and the narrow presumptions in Art. 42).
3. Harmonised standards are produced by **CEN-CENELEC JTC 21** in response to a Commission standardisation request (M/613). A standard becomes "harmonised" only after the Commission assesses it and cites it in the OJ. Publishing a European Standard (EN) does **not** by itself create the presumption.
4. **ISO/IEC 42001** is an international management-system standard developed in ISO/IEC JTC 1/SC 42. It is not part of the EU harmonisation programme. Certification to it attests that an organisation's management system meets the standard - it is **not** an Art. 40 instrument and confers **no** presumption of conformity.
5. For GPAI, the Act names three routes (Art. 53(4), 55(2)): an approved code of practice, a harmonised standard, or "alternative adequate means" assessed by the Commission. An ISO certificate is not one of them.

## JTC 21 pipeline (as reported by the 15 Sep 2026 tracker edition, plus a June 2026 snapshot)

| Standard | Covers | Status reported |
|---|---|---|
| **EN 18286** | Quality management system (Art. 17) | **Published by CEN-CENELEC in July 2026** (sources give 22 and 30 Jul). **OJ citation outstanding** as of 15 Sep 2026 -> no presumption yet. Reported to include an annex mapping to ISO/IEC 42001 controls (single secondary source). |
| prEN 18228 | Risk management (Art. 9) | Enquiry closed 30 Jul 2026; **rejected by a majority of national standards bodies**; comment resolution scheduled first week of November. |
| prEN 18229-1 | Logging (Art. 12) | Enquiry closed 20 Aug 2026; **rejected on the weighted-population threshold**; 443 comments; reconsideration requests due 25 Sep 2026. |
| prEN 18282 | Cybersecurity (Art. 15) | Enquiry closed 30 Jul 2026; **rejected**; revised, closer-to-the-Act scope at ballot until 16 Sep 2026. |
| prEN 18229-2 | Accuracy and robustness (Art. 15) | Drafting (June 2026 snapshot) |
| prEN 18229-3 | Transparency and human oversight (Arts. 13-14) | Drafting (June 2026 snapshot) |
| prEN 18284 | Dataset quality and governance (Art. 10) | Drafting; Commission comments under review Aug 2026; target: public enquiry before October plenary |
| prEN 18283 | Bias management (Art. 10) | Drafting; same target |
| prEN 18285 | Conformity assessment framework (Art. 43) | Mature draft 4 Sep 2026; going to the Commission |
| M/613 | Standardisation request | Expires **28 Feb 2027** |

## Consequences for the crosswalk

- Every "Substantially evidences" or "Partially evidences" verdict is a statement about **evidence**, never about **presumption**.
- When a reference is published in the OJ, the relevant row's "Residual gap" should be revisited: the presumption route will then be real for the requirements that standard covers, and the right question becomes "does our ISO 42001 AIMS plus the harmonised standard's annex mapping close the gap?"
- If harmonised standards are not available when high-risk obligations apply (2 Dec 2027), the Act has a fallback (common specifications, Art. 41); I have **not** assessed whether the Commission intends to use it.

## Honest limits of this page

All status information comes from three public trackers and law-firm/standards-community notes, not from CEN-CENELEC or the OJ directly. The EN 18286 publication date differs between sources. The "Annex D maps to ISO 42001" statement comes from a single secondary source and should be checked against the published EN.
