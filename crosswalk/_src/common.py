"""Shared constants for crosswalk row files. Row tuples are positional:

(id, article, obligation, role, tier, applies_from, omnibus_note,
 iso42001_ref, iso42001_verdict, iso27001_ref, iso27001_verdict,
 nist_ref, nist_verdict, residual_gap, impl_note, std_pipeline)
"""

S = "Substantially evidences"
P = "Partially evidences"
A = "Adjacent"
N = "No coverage"
NA = "Not assessed"  # used only for the supplementary ISO 27001 column when irrelevant

HR_DATES = ("2 Dec 2027 (Annex III systems); 2 Aug 2028 (Annex I products). "
            "Originally 2 Aug 2026 / 2 Aug 2027.")
GPAI_DATES = ("Obligations applicable since 2 Aug 2025; Commission fining/enforcement powers "
              "from 2 Aug 2026; models placed before 2 Aug 2025 must comply by 2 Aug 2027.")

PRV = "Provider"
DEP = "Deployer"
IMP = "Importer"
DIS = "Distributor"
GPP = "GPAI model provider"
HR = "High-risk"
GP = "GPAI"
GPS = "GPAI with systemic risk"

FIELDS = [
    "obligation_id", "eu_ai_act_article", "obligation_plain_words", "actor_role", "risk_tier",
    "application_date", "omnibus_2026_1744_status",
    "iso42001_clause_or_control", "iso42001_verdict",
    "iso27001_2022_supplementary", "iso27001_verdict",
    "nist_ai_rmf_subcategory", "nist_verdict",
    "residual_gap", "implementation_note", "harmonised_standard_pipeline",
]
