"""Reference ID sets used ONLY to validate that cited control/subcategory numbers exist.

These are identifiers (numbers + titles), not standard text.
  - ISO/IEC 42001:2023 Annex A: identifiers taken from the author's metadata skeleton.
  - ISO/IEC 27001:2022 Annex A: identifiers taken from the author's metadata skeleton.
  - NIST AI RMF 1.0 (NIST AI 100-1, Jan 2023): subcategory identifiers (US government work).
"""

ISO42001_ANNEX_A = {
    "A.2.2", "A.2.3", "A.2.4",
    "A.3.2", "A.3.3",
    "A.4.2", "A.4.3", "A.4.4", "A.4.5", "A.4.6",
    "A.5.2", "A.5.3", "A.5.4", "A.5.5",
    "A.6.1.2", "A.6.1.3",
    "A.6.2.2", "A.6.2.3", "A.6.2.4", "A.6.2.5", "A.6.2.6", "A.6.2.7", "A.6.2.8",
    "A.7.2", "A.7.3", "A.7.4", "A.7.5", "A.7.6",
    "A.8.2", "A.8.3", "A.8.4", "A.8.5",
    "A.9.2", "A.9.3", "A.9.4",
    "A.10.2", "A.10.3", "A.10.4",
}

# Main-body clause numbers are NOT in the skeleton the author supplied; they are cited from
# author knowledge of the standard's structure and are flagged as unverified in the README.
ISO42001_CLAUSES_UNVERIFIED = {
    "4", "5.2", "5.3", "6.1.2", "6.1.3", "6.1.4", "7.2", "7.3", "7.5",
    "8.1", "8.2", "8.3", "8.4", "9.1", "9.2", "9.3", "10.1", "10.2",
}

ISO27001_ANNEX_A = (
    {f"5.{i}" for i in range(1, 38)} |
    {f"6.{i}" for i in range(1, 9)} |
    {f"7.{i}" for i in range(1, 15)} |
    {f"8.{i}" for i in range(1, 35)}
)

NIST_AI_RMF = (
    {f"GOVERN 1.{i}" for i in range(1, 8)} | {f"GOVERN 2.{i}" for i in range(1, 4)} |
    {f"GOVERN 3.{i}" for i in range(1, 3)} | {f"GOVERN 4.{i}" for i in range(1, 4)} |
    {f"GOVERN 5.{i}" for i in range(1, 3)} | {f"GOVERN 6.{i}" for i in range(1, 3)} |
    {f"MAP 1.{i}" for i in range(1, 7)} | {f"MAP 2.{i}" for i in range(1, 4)} |
    {f"MAP 3.{i}" for i in range(1, 6)} | {f"MAP 4.{i}" for i in range(1, 3)} |
    {f"MAP 5.{i}" for i in range(1, 3)} |
    {f"MEASURE 1.{i}" for i in range(1, 4)} | {f"MEASURE 2.{i}" for i in range(1, 14)} |
    {f"MEASURE 3.{i}" for i in range(1, 4)} | {f"MEASURE 4.{i}" for i in range(1, 4)} |
    {f"MANAGE 1.{i}" for i in range(1, 5)} | {f"MANAGE 2.{i}" for i in range(1, 5)} |
    {f"MANAGE 3.{i}" for i in range(1, 3)} | {f"MANAGE 4.{i}" for i in range(1, 4)}
)
assert len(NIST_AI_RMF) == 72, len(NIST_AI_RMF)

VERDICTS = {"Substantially evidences", "Partially evidences", "Adjacent", "No coverage"}
VERDICTS_27001 = VERDICTS | {"Not assessed"}
