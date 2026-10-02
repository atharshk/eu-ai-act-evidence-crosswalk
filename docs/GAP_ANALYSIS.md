# Gap analysis: "We are ISO/IEC 42001 certified. What EU AI Act obligations are we still exposed on?"

*Generated from `crosswalk/crosswalk.csv` by `scripts/build_docs.py`. Position as of 2 Oct 2026; the Act's timeline is still subject to legislative amendment. Verdicts are the author's professional judgement, not a measurement - re-verify before operational use.*

## Short answer

Certification does **not** make you AI Act compliant, and in this crosswalk it does not even come close on most rows. Of **46** obligation rows (high-risk systems and general-purpose AI models):

| ISO 42001 evidences the obligation... | Rows | Share |
|---|---|---|
| Substantially (most of the way, with a named gap) | 6 | 13% |
| Partially (helps, leaves a named gap) | 21 | 46% |
| Adjacent only (related subject, not evidence) | 14 | 30% |
| No coverage (nothing in the standard speaks to it) | 5 | 11% |

**19 of 46 rows (41%) are fully exposed**: the certificate gives you nothing to point at. **No row is rated "fully covered"** - even the six best matches carry a named residual gap. Percentages are descriptive of this crosswalk's row selection; they are not a compliance score and should not be quoted as one.

## Why the certificate cannot be a shortcut (the mechanism)

1. **Presumption of conformity flows from harmonised standards, not from management-system certificates.** Under Art. 40, a high-risk system or GPAI model conforming to a harmonised standard whose reference is published in the Official Journal is presumed to meet the corresponding requirements. ISO/IEC 42001 is an international standard outside the CEN-CENELEC JTC 21 harmonisation programme; its certificate is not an Art. 40 instrument.
2. **As of the latest source I could find (15 Sep 2026), no AI Act harmonised standard is cited in the OJ.** EN 18286 (quality management for Art. 17) has been published by CEN-CENELEC but its citation is outstanding; the other JTC 21 deliverables are in enquiry or drafting, and three of them (prEN 18228 risk management, prEN 18282 cybersecurity and prEN 18229-1 logging) were rejected at their first enquiry votes. So today **nobody** has a harmonised-standard presumption of conformity. See [HARMONISED_STANDARDS.md](HARMONISED_STANDARDS.md).
3. **Different objects.** An ISO 42001 certificate attests that an *organisation's management system* meets the standard. Most AI Act duties attach to a *specific system* (Arts. 9-15), to *legal acts* (declaration of conformity, CE marking, registration) or to a *person in a role* (provider, deployer, importer...). The certificate speaks to none of those directly.

## Rows where the certificate gives you nothing (No coverage / Adjacent)

| ID | Article | Role | ISO 42001 | Why the certificate does not help |
|---|---|---|---|---|
| `PRV-HR-A10-SCD` | Art. 4a (replacing deleted Art. 10(5)) | Provider | Adjacent | Neither AI framework supplies the GDPR Art. 9 analysis. 'Strict necessity' and 'no alternative data' are legal judgements for DPO + counsel. 27001 controls evidence the SECURITY conditions only. |
| `PRV-HR-A14-OVS` | Art. 14(1)-(4) | Provider | Adjacent | Art. 14 is a DESIGN requirement (override, stop, automation-bias awareness). ISO 42001 has no control for it. NIST is stronger than ISO here (MAP 3.5, MANAGE 2.4 'supersede, disengage, or deactivate') but still organisational,... |
| `PRV-HR-A15-CYB` | Art. 15(5), Art. 42(2) | Provider | Adjacent | A generic ISMS does not name the Art. 15(5) AI-specific attack classes (poisoning, evasion, confidentiality attacks, model flaws). NIST AI RMF text (s.3.3) names them but as characteristics, not as a required test. Art. 42(2)... |
| `PRV-HR-A43-CA` | Art. 43 | Provider | Adjacent | Different object, different issuer, different legal effect: an ISO 42001 certificate attests a management system; Art. 43 assesses THE SYSTEM against Section 2. For Annex III point 1 (biometrics) the Annex VII notified-body... |
| `PRV-HR-A47-DOC` | Art. 47, Annex V | Provider | No coverage | A legal act with legal consequences (47(4)). No management-system standard or voluntary framework produces it. |
| `PRV-HR-A48-CE` | Art. 48 | Provider | No coverage | Statutory marking; outside the scope of every voluntary framework. |
| `PRV-HR-A49-REG` | Art. 49(1), 49(5) | Provider | Adjacent | An internal AI-system inventory is a prerequisite for registration but is not registration. |
| `PRV-HR-A06-NONHR` | Art. 6(3)-(4), Art. 49(2) | Provider | Adjacent | Classification is a legal determination. Neither framework has an Act-aligned classification step; a wrong 'not high-risk' conclusion is itself the exposure. |
| `PRV-HR-A22-AR` | Art. 22 | Provider | No coverage | A statutory appointment; no framework contains an equivalent. |
| `DEP-HR-A26-WORK` | Art. 26(7) | Deployer | Adjacent | Collective-information rules sit in national labour law (works councils, consultation). Frameworks do not cover them. |
| `DEP-HR-A86-EXPL` | Art. 86 | Deployer | Adjacent | An individually enforceable right. Needs a request-handling process and explanation capability; NIST MEASURE 2.9 is about explaining the model for governance, not answering an individual. |
| `IMP-HR-A23-VERIFY` | Art. 23 | Importer | Adjacent | Importer verification is a legal gate with named documents, not a supplier-assurance process. |
| `DIS-HR-A24-VERIFY` | Art. 24 | Distributor | Adjacent | As importer: a legal verification gate, not a supplier-management control. |
| `GPP-GP-A53-COPY` | Art. 53(1)(c) | GPAI model provider | Adjacent | Honouring machine-readable opt-outs is a specific technical-legal duty. NIST GOVERN 6.1 / MAP 4.1 mention third-party IP infringement risk, which is related but not the Art. 4(3) mechanism. |
| `GPP-GP-A53-SUMM` | Art. 53(1)(d) | GPAI model provider | Adjacent | A PUBLIC disclosure duty. Internal provenance records are an input, not the deliverable. Check the AI Office template version currently in force before publishing. |
| `GPP-GP-A53-ROUTE` | Art. 53(4), Art. 55(2) | GPAI model provider | No coverage | The GPAI equivalent of the high-risk headline finding: ISO 42001 certification is not one of the three routes the Act names. Without a code or an OJ-cited harmonised standard, the provider carries the burden of showing... |
| `GPP-GP-A54-AR` | Art. 54 | GPAI model provider | No coverage | Statutory appointment; no framework equivalent. |
| `GPP-GPS-A55-EVAL` | Art. 55(1)(a), Annex XI s.2 | GPAI model provider | Adjacent | Documented adversarial testing is not an ISO 42001 control. NIST names security/resilience evaluation and independent assessors but not adversarial testing of frontier-scale models as a requirement. |
| `GPP-GPS-A55-CYB` | Art. 55(1)(d) | GPAI model provider | Adjacent | The ISMS is the strongest evidence here, but only if its SCOPE statement actually includes model weights, training pipelines and the compute estate - scope is chosen by the organisation and is routinely drawn around corporate IT. |

## Rows where ISO 42001 helps but a named gap remains

| ID | Article | Role | Named gap that remains |
|---|---|---|---|
| `PRV-HR-A09-RMS` | Art. 9(1)-(5) | Provider | ISO risk = effect of uncertainty on the organisation's objectives; Art. 9 risk = harm to health, safety, fundamental rights. A certificate does not show the risk criteria are rights-anchored. Art. 9(3) scoping, per-hazard AND... |
| `PRV-HR-A09-TEST` | Art. 9(6)-(8) | Provider | ISO asks you to define V&V criteria but does not require pre-defined probabilistic thresholds or a pre-market gate. Nothing in either framework ties test metrics to the intended purpose in Art. 9(8) terms. |
| `PRV-HR-A09-VULN` | Art. 9(9) | Provider | Neither framework names minors or vulnerable groups as a mandatory consideration; ISO A.5.4 is the right place but is generic. |
| `PRV-HR-A10-BIAS` | Art. 10(2)(f)-(g), 10(3)-(4) | Provider | Neither names 'prohibited discrimination under Union law' as the test. NIST MEASURE 2.11 is the most direct outcome in any of the three corpora but is evaluative, not a conformity threshold. Note statutory shortcut: Art. 42(1)... |
| `PRV-HR-A11-DOC` | Art. 11, Annex IV | Provider | ISO does not prescribe Annex IV content. Specific gaps: list of harmonised standards applied (Annex IV pt 7), copy of EU declaration of conformity (pt 8), post-market plan inclusion (pt 9), dated and signed test reports (2(g)).... |
| `PRV-HR-A12-LOG` | Art. 12(1)-(2) (12(3) for Annex III 1(a)) | Provider | ISO A.6.2.8 asks the organisation to define logging; Art. 12 is a PRODUCT-DESIGN requirement (the capability must exist in the system). 27001 logging is built for security events, not AI-functioning traceability. 12(3) adds... |
| `PRV-HR-A13-IFU` | Art. 13(1)-(3) | Provider | A.8.2 does not mandate the Art. 13(3) content list: declared accuracy metrics and circumstances that affect them, group-level performance, pre-determined changes, and deployer log-collection mechanisms are the usual omissions. |
| `PRV-HR-A15-ACC` | Art. 15(1)-(4) | Provider | Neither framework sets levels; both require you to define and monitor them. Feedback-loop mitigation in continual-learning systems (15(4)) is not explicit in either. NIST 'Valid and Reliable' and 'Safe' characteristics are the... |
| `PRV-HR-A19-LOGRET` | Art. 19 | Provider | The six-month floor and the data-protection override are legal parameters; the GDPR storage-limitation tension is for the DPO to resolve, not for a control to evidence. |
| `PRV-HR-A20-CORR` | Art. 20 | Provider | ISO corrective action is raised against the management system; Art. 20 is triggered by non-conformity with the REGULATION and requires a real withdraw/disable/recall capability plus notification of authorities. 'Immediately' has... |
| `PRV-HR-A72-PMM` | Art. 72 | Provider | NIST MANAGE 4.1 is the closest single outcome in any corpus, but neither framework frames monitoring as evaluating continuous compliance with the Section 2 requirements, and neither requires the plan to sit inside the technical... |
| `PRV-HR-A73-SI` | Art. 73(1)-(6); Art. 3(49) | Provider | An ISO 'incident' is not an Act 'serious incident' (death/serious health harm; critical-infrastructure disruption; infringement of fundamental-rights obligations under Union law; serious property/environment harm). The 15/10/2... |
| `PRV-HR-A25-CHAIN` | Art. 25(1)-(4) | Provider | ISO A.10 evidences allocation and supplier management, but does not test the Art. 25(1) trigger: a deployer that rebrands or re-purposes a GPAI system for an Annex III use inherits full provider duties. That is the commonly... |
| `DEP-HR-A26-OVS` | Art. 26(2) | Deployer | 'Authority' (the power to override) is the element usually missing in practice and is not a control requirement in either framework. NIST GOVERN 3.2 (differentiating human-AI configuration roles) is the closer outcome. |
| `DEP-HR-A26-INPUT` | Art. 26(4) | Deployer | ISO Annex A data controls (A.7) are written around development data, not live operational inputs. Representativeness for the intended purpose is not tested. |
| `DEP-HR-A26-MON` | Art. 26(5) | Deployer | The suspend-use duty and the reporting sequence (provider first) are specific legal steps. If the provider cannot be reached, Art. 73 applies mutatis mutandis to the deployer. |
| `DEP-HR-A26-NOTIFY` | Art. 26(11) | Deployer | Content, timing and format of the notice are legal choices; ISO intent is generic. |
| `GPP-GP-A53-DOC` | Art. 53(1)(a), Annex XI s.1 | GPAI model provider | ISO control is system-oriented; Annex XI is MODEL-oriented (training compute in FLOPs, energy consumption, number of data points). Neither framework asks for energy or compute reporting. |
| `GPP-GP-A53-DOWN` | Art. 53(1)(b), Annex XII | GPAI model provider | Annex XII content list (acceptable use policy, context-window size, integration means) is not in ISO A.8.2. This is the information a downstream provider needs for Art. 25 and Art. 13 - gaps here propagate down the chain. |
| `GPP-GPS-A55-SYS` | Art. 55(1)(b) | GPAI model provider | 'Systemic risk' (Art. 3(65)) is specific to high-impact capabilities with Union-level reach. An organisation-scoped risk assessment will not, by default, be scoped to that. |
| `GPP-GPS-A55-INC` | Art. 55(1)(c) | GPAI model provider | No time limit is given in Art. 55(1)(c) ('without undue delay'), unlike the 15/10/2 day clocks in Art. 73 for high-risk providers. The Act's 'serious incident' definition applies (Art. 3(49)). |

## The closest matches - and what is still missing

| ID | Article | Role | Named gap that remains |
|---|---|---|---|
| `PRV-HR-A10-GOV` | Art. 10(1), 10(2)(a)-(e), 10(2)(h) | Provider | 'Substantially' applies to the PROCESS. ISO A.7 sets no quality thresholds and is not tied to one system's intended purpose; Art. 10(2)(h) 'data gaps that prevent compliance with this Regulation' is a legal test ISO does not... |
| `PRV-HR-A17-QMS` | Art. 17(1)-(4) | Provider | The closest thing to an equivalence in the whole crosswalk, and it is still NOT equivalence. Missing from a stock ISO 42001 AIMS: (a) conformity-assessment/modification strategy, (e) which technical specs and standards apply and... |
| `PRV-ALL-A04-LIT` | Art. 4 | Provider | The softened wording makes the ISO competence/awareness clauses a good fit. Residual: Art. 4 also reaches 'other persons dealing with the operation and use of AI systems on their behalf' (contractors), and ISO competence is... |
| `DEP-ALL-A04-LIT` | Art. 4 | Deployer | As provider row. Deployer-specific: literacy must cover how to interpret THIS system's output (ties to Art. 14(4) and Art. 26(2)). |
| `DEP-HR-A26-USE` | Art. 26(1) | Deployer | ISO A.9 is the best organisation-level fit for a deployer. Residual: the benchmark is the PROVIDER'S instructions for use (Art. 13) - a certificate does not show you obtained, read and operationalised them. |
| `DEP-HR-A27-FRIA` | Art. 27 | Deployer | Best conceptual match in the crosswalk (ISO treats impact on individuals as first-class), yet: Art. 27 has a prescribed content list (a)-(f), a scoping rule (who must do it), and a notification-to-authority step with a template.... |

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
