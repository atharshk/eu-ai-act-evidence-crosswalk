#!/usr/bin/env bash
# Rebuild everything and refresh cached formula values in the register workbook via LibreOffice.
# openpyxl writes formulas without cached values; Excel recalculates on open, but viewers/previewers may not.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
python3 scripts/build_crosswalk.py
python3 scripts/build_register.py
python3 scripts/build_docs.py
TMP="$(mktemp -d)"
soffice --headless --calc --convert-to xlsx --outdir "$TMP" register/risk_register.xlsx >/dev/null 2>&1
cp "$TMP/risk_register.xlsx" register/risk_register.xlsx
rm -rf "$TMP"
echo "rebuilt and recalculated"
