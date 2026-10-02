#!/usr/bin/env python3
"""Generate docs/GAP_ANALYSIS.md and register/SCORING_METHODOLOGY.md from the data so numbers never drift.
Run after build_crosswalk.py:  python3 scripts/build_docs.py
"""
import csv, sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import scoring as S  # noqa: E402

rows = list(csv.DictReader(open(ROOT / "crosswalk" / "crosswalk.csv", encoding="utf-8-sig")))
N = len(rows)
cnt = Counter(r["iso42001_verdict"] for r in rows)
exposed = [r for r in rows if r["iso42001_verdict"] in ("No coverage", "Adjacent")]
partial = [r for r in rows if r["iso42001_verdict"] == "Partially evidences"]
subst = [r for r in rows if r["iso42001_verdict"] == "Substantially evidences"]


def pct(n):
    return f"{round(100 * n / N)}%"


def short(t, n=230):
    t = " ".join(t.split())
    return t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "..."


def tbl(rs, cols):
    out = ["| " + " | ".join(h for h, _ in cols) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rs:
        out.append("| " + " | ".join(str(f(r)).replace("|", "/") for _, f in cols) + " |")
    return "\n".join(out)


cols_exposed = [("ID", lambda r: f"`{r['obligation_id']}`"), ("Article", lambda r: r["eu_ai_act_article"]),
                ("Role", lambda r: r["actor_role"]), ("ISO 42001", lambda r: r["iso42001_verdict"]),
                ("Why the certificate does not help", lambda r: short(r["residual_gap"]))]
cols_other = [("ID", lambda r: f"`{r['obligation_id']}`"), ("Article", lambda r: r["eu_ai_act_article"]),
              ("Role", lambda r: r["actor_role"]), ("Named gap that remains", lambda r: short(r["residual_gap"]))]

gap = f"""# Gap analysis: "We are ISO/IEC 42001 certified. What EU AI Act obligations are we still exposed on?"

*Generated from `crosswalk/crosswalk.csv` by `scripts/build_docs.py`. Position as of 2 Oct 2026; the Act's timeline is still subject to legislative amendment. Verdicts are the author's professional judgement, not a measurement - re-verify before operational use.*

## Short answer

Certification does **not** make you AI Act compliant, and in this crosswalk it does not even come close on most rows. Of **{N}** obligation rows (high-risk systems and general-purpose AI models):

| ISO 42001 evidences the obligation... | Rows | Share |
|---|---|---|
| Substantially (most of the way, with a named gap) | {cnt['Substantially evidences']} | {pct(cnt['Substantially evidences'])} |
| Partially (helps, leaves a named gap) | {cnt['Partially evidences']} | {pct(cnt['Partially evidences'])} |
| Adjacent only (related subject, not evidence) | {cnt['Adjacent']} | {pct(cnt['Adjacent'])} |
| No coverage (nothing in the standard speaks to it) | {cnt['No coverage']} | {pct(cnt['No coverage'])} |

**{len(exposed)} of {N} rows ({pct(len(exposed))}) are fully exposed**: the certificate gives you nothing to point at. **No row is rated "fully covered"** - even the six best matches carry a named residual gap. Percentages are descriptive of this crosswalk's row selection; they are not a compliance score and should not be quoted as one.

## Why the certificate cannot be a shortcut (the mechanism)

1. **Presumption of conformity flows from harmonised standards, not from management-system certificates.** Under Art. 40, a high-risk system or GPAI model conforming to a harmonised standard whose reference is published in the Official Journal is presumed to meet the corresponding requirements. ISO/IEC 42001 is an international standard outside the CEN-CENELEC JTC 21 harmonisation programme; its certificate is not an Art. 40 instrument.
2. **As of the latest source I could find (15 Sep 2026), no AI Act harmonised standard is cited in the OJ.** EN 18286 (quality management for Art. 17) has been published by CEN-CENELEC but its citation is outstanding; the other JTC 21 deliverables are in enquiry or drafting, and three of them (prEN 18228 risk management, prEN 18282 cybersecurity and prEN 18229-1 logging) were rejected at their first enquiry votes. So today **nobody** has a harmonised-standard presumption of conformity. See [HARMONISED_STANDARDS.md](HARMONISED_STANDARDS.md).
3. **Different objects.** An ISO 42001 certificate attests that an *organisation's management system* meets the standard. Most AI Act duties attach to a *specific system* (Arts. 9-15), to *legal acts* (declaration of conformity, CE marking, registration) or to a *person in a role* (provider, deployer, importer...). The certificate speaks to none of those directly.

## Rows where the certificate gives you nothing (No coverage / Adjacent)

{tbl(exposed, cols_exposed)}

## Rows where ISO 42001 helps but a named gap remains

{tbl(partial, cols_other)}

## The closest matches - and what is still missing

{tbl(subst, cols_other)}

## Plain-language reading of the main exposures

- **The legal "paperwork" is entirely yours.** EU declaration of conformity, CE marking, EU-database registration, authorised-representative appointment and the conformity assessment itself are statutory acts. ISO 42001 has no equivalent. (`PRV-HR-A47-DOC`, `A48-CE`, `A49-REG`, `A22-AR`, `A43-CA`.)
- **Product-design requirements are not management controls.** Human oversight with a working override/stop (Art. 14), logging capability built into the system (Art. 12), declared accuracy (Art. 15) and AI-specific attack resilience (Art. 15(5)) are things the *system* must do. A management system can ask you to think about them; it cannot prove the product has them.
- **"Risk" means something different.** ISO and enterprise risk management measure effect on the organisation's objectives. The Act's risk is harm to the health, safety and fundamental rights of persons. A risk register built only for ISO purposes will under-weight exactly what the regulator cares about. See [/register/](../register/).
- **You can become a provider without meaning to.** Under Art. 25(1), a deployer that puts its name on a high-risk system, substantially modifies it, or re-purposes a general-purpose system for a high-risk use takes on the full provider burden. ISO 42001's supply-chain controls (A.10) do not test for that trigger. (`PRV-HR-A25-CHAIN`.)
- **Incidents have legal definitions and clocks.** An ISO "incident" is not an Act "serious incident"; the 15 / 10 / 2-day reporting clocks (Art. 73) are not in any framework. (`PRV-HR-A73-SI`.)
- **Where you are strongest:** AI literacy (Art. 4, after the 2026 softening), deployer use-governance (Art. 26(1)), impact assessment as the basis for a fundamental-rights impact assessment (Art. 27), the QMS skeleton (Art. 17), data-governance process (Art. 10(2)), and - with a 27001 certificate whose scope covers the model estate - GPAI cybersecurity (Art. 55(1)(d)).

## What a certified organisation should do next (in order)

1. **Classify.** Decide, per system, which role you hold (provider / deployer / importer / distributor) and which tier applies. Document it (`PRV-HR-A06-NONHR` for any "not high-risk" conclusion). Everything else depends on this.
2. **Close the "No coverage" statutory items** relevant to your role - they have lead times (notified bodies, mandates, registration).
3. **Add an "Art. 17 overlay"** to the AIMS for the four missing QMS elements (conformity-assessment strategy; standards-and-specs decision; Art. 73 incident procedure; authority communications).
4. **Re-base risk criteria on harm to persons** and link the register to the crosswalk.
5. **Watch the standards pipeline** (EN 18286 OJ citation; prEN 18228, 18229-1, 18282, 18284, 18283, 18285) and revisit this analysis when a reference is published: from that moment the presumption-of-conformity route becomes real for the covered requirements.

## Timing context (as of 2 Oct 2026)

High-risk obligations are now scheduled for **2 Dec 2027** (Annex III systems) and **2 Aug 2028** (Annex I products) under Regulation (EU) 2026/1744. GPAI obligations have applied since 2 Aug 2025 and Commission fining powers for GPAI providers since 2 Aug 2026. See [TIMELINE.md](TIMELINE.md) for sources and what I did and did not verify against the Official Journal.
"""
(ROOT / "docs").mkdir(exist_ok=True)
(ROOT / "docs" / "GAP_ANALYSIS.md").write_text(gap, encoding="utf-8")


def md_table(head, rs):
    o = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    for r in rs:
        o.append("| " + " | ".join(str(x).replace("|", "/") for x in r) + " |")
    return "\n".join(o)


sm = f"""# Scoring methodology (risk register)

*Generated from `scripts/scoring.py` - the same source feeds the 'Scoring Methodology' sheet in `risk_register.xlsx`.*

## Why two impact scales

In enterprise risk management, "risk" means risk **to the organisation**. In the EU AI Act, "risk" means risk to the **health, safety and fundamental rights of persons**. They can diverge: a system can be commercially low-risk and high-risk to the people it affects, and the Act cares about the latter. This register scores both, in separate columns, and shows which one drives the result.

## Likelihood (next 12 months, in the system's operating context)

{md_table(["Score", "Label", "Definition"], S.LIKELIHOOD)}

## Rights Impact (harm to persons)

{md_table(["Score", "Label", "Definition"], S.RIGHTS_IMPACT)}

## Organisational Impact (harm to the organisation)

{md_table(["Score", "Label", "Definition"], S.ORG_IMPACT)}

## Control effectiveness (rated on evidence of operation)

{md_table(["Rating", "Likelihood reduction", "Definition"], [(n, r, d) for n, r, d in S.EFFECTIVENESS])}

### Cap derived from the crosswalk verdict

{md_table(["Crosswalk ISO 42001 verdict for the linked obligation", "Maximum effectiveness"], list(S.VERDICT_CAP.items()))}

A control that only partially evidences an obligation cannot, on its own, make the obligation-linked risk "largely" controlled. The cap may be exceeded only with a written override that cites a **non-ISO** control (for example a 27001 control or a bespoke technical control) and its evidence. This is what stops a certificate being over-credited.

## Formulae

- Rights score = Likelihood x Rights Impact; Organisational score = Likelihood x Organisational Impact.
- **Inherent score = MAX(Rights score, Organisational score)** - never a sum or average, so a high harm to persons is not diluted by a low business impact. The "Score driver" column says which dimension won.
- Residual likelihood = MAX(1, Likelihood - reduction for the applied effectiveness). Impacts are not reduced by controls in this version.
- Residual score = MAX(residual likelihood x Rights Impact, residual likelihood x Organisational Impact).
- Bands by product: {"; ".join(f"{n} {a}-{b}" for n, a, b in S.BANDS)}.
- {S.RIGHTS_OVERRIDE}

## Limitations (named by the author)

{chr(10).join(f"{i+1}. {t}" for i, t in enumerate(S.LIMITATIONS))}
"""
(ROOT / "register" / "SCORING_METHODOLOGY.md").write_text(sm, encoding="utf-8")
print("docs written")
