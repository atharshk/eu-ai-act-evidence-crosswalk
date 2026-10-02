# Scoring methodology (risk register)

*Generated from `scripts/scoring.py` - the same source feeds the 'Scoring Methodology' sheet in `risk_register.xlsx`.*

## Why two impact scales

In enterprise risk management, "risk" means risk **to the organisation**. In the EU AI Act, "risk" means risk to the **health, safety and fundamental rights of persons**. They can diverge: a system can be commercially low-risk and high-risk to the people it affects, and the Act cares about the latter. This register scores both, in separate columns, and shows which one drives the result.

## Likelihood (next 12 months, in the system's operating context)

| Score | Label | Definition |
|---|---|---|
| 1 | Rare | Not expected in the next 12 months. No comparable incident documented in the sector. Would need several independent control failures. |
| 2 | Unlikely | Could occur. Isolated comparable incidents documented outside the sector or in a materially different use. Preventive controls are strong and tested. |
| 3 | Possible | Plausible under normal operation; comparable incidents documented in the sector. |
| 4 | Likely | Expected at least once in the next 12 months under current operation. Multiple documented comparable incidents, or a known weakness not yet treated. |
| 5 | Almost certain | Occurring now or recurring routinely. Known and unremediated. |

## Rights Impact (harm to persons)

| Score | Label | Definition |
|---|---|---|
| 1 | Negligible | No discernible adverse effect on any person; trivially reversible. |
| 2 | Minor | Transient inconvenience or minor differential treatment that the person can reverse quickly without outside help. |
| 3 | Moderate | Noticeable adverse effect on quality of service or treatment (delay, extra burden) that is reversible through complaint or appeal with effort; limited number of persons. |
| 4 | Major | Material adverse effect on an individual's access to a service, employment, or legal standing, or discrimination on a protected ground; reversal is slow or difficult. |
| 5 | Severe | Death or serious harm to health, loss of liberty, serious infringement of a fundamental right, or discrimination affecting many persons; effectively irreversible. |

## Organisational Impact (harm to the organisation)

| Score | Label | Definition |
|---|---|---|
| 1 | Negligible | Handled inside the team; no external attention; within business-as-usual cost. |
| 2 | Minor | Internal remediation project; no regulator or customer escalation. |
| 3 | Moderate | Regulator information request, customer escalation or contractual remedy; funded remediation programme. |
| 4 | Major | Formal enforcement step (corrective order, withdrawal or recall), loss of a key customer or of a certification, or a fine well below the statutory ceiling. |
| 5 | Severe | Fine at or near the statutory ceiling (Art. 99(4): up to EUR 15m or 3% of worldwide turnover for operator obligations; Art. 99(3): EUR 35m / 7% for Art. 5; Art. 101: up to 3% / EUR 15m for GPAI providers), withdrawal of the product line from the Union market, or existential reputational damage. |

## Control effectiveness (rated on evidence of operation)

| Rating | Likelihood reduction | Definition |
|---|---|---|
| Not effective | 0 | No control, or a documented control with no evidence it operates. |
| Partially effective | 1 | Designed and implemented, but untested, or tested with known material gaps. |
| Largely effective | 2 | Designed, implemented and tested within the last 12 months with only minor gaps. |

### Cap derived from the crosswalk verdict

| Crosswalk ISO 42001 verdict for the linked obligation | Maximum effectiveness |
|---|---|
| Substantially evidences | Largely effective |
| Partially evidences | Partially effective |
| Adjacent | Not effective |
| No coverage | Not effective |

A control that only partially evidences an obligation cannot, on its own, make the obligation-linked risk "largely" controlled. The cap may be exceeded only with a written override that cites a **non-ISO** control (for example a 27001 control or a bespoke technical control) and its evidence. This is what stops a certificate being over-credited.

## Formulae

- Rights score = Likelihood x Rights Impact; Organisational score = Likelihood x Organisational Impact.
- **Inherent score = MAX(Rights score, Organisational score)** - never a sum or average, so a high harm to persons is not diluted by a low business impact. The "Score driver" column says which dimension won.
- Residual likelihood = MAX(1, Likelihood - reduction for the applied effectiveness). Impacts are not reduced by controls in this version.
- Residual score = MAX(residual likelihood x Rights Impact, residual likelihood x Organisational Impact).
- Bands by product: Low 1-4; Medium 5-9; High 10-15; Critical 16-25.
- Rights floor: if Rights Impact = 5, or Rights Impact >= 4 and residual Likelihood >= 2, the band is raised to at least High regardless of the product. This is a deliberate judgement to stop multiplication from burying severe harm to individuals under a Medium score.

## Limitations (named by the author)

1. Ordinal, not cardinal. A 4 is not twice a 2, and a product of 12 is not 'three times' a product of 4. Multiplying ordinals into a composite is standard practice and methodologically imperfect: it creates ties (e.g. 3x4 = 4x3), treats the scales as if they had equal intervals, and hides which dimension drives the score. That is why Rights and Organisational scores are kept in separate columns and the driver is shown.
2. Inherent score = MAX(Rights score, Organisational score), not a sum or average, so a high rights harm is never diluted by a low business impact.
3. Likelihood is a single event-likelihood shared by both impact dimensions. Likelihood of enforcement action is not modelled separately; it is folded into Organisational Impact definitions.
4. Control-effectiveness reductions (0, 1, 2 points of likelihood) are a convention, not a measurement. They are capped by the linked crosswalk verdict so a certificate-backed control cannot be over-credited.
5. Anchored definitions reduce, but do not remove, rater subjectivity. Calibrate by having two raters score the same five risks independently and discussing differences.
6. The register scores risk to persons (Act sense) AND risk to the organisation (ERM sense) because they do not always point the same way. It does not replace the Art. 9 risk management system or the Art. 27 FRIA; it supports them.
