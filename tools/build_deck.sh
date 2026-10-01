#!/bin/sh
# Rebuild the C716 deck from the WSQ source: convert_deck.py, then fix_deck.py.
set -e
cd "$(dirname "$0")/.."
OUT="courseware/Semiconductor Process Fundamentals Masterclass (C716)-v1.0.pptx"
python3 ~/.claude/skills/wsq-to-non-wsq/scripts/convert_deck.py \
  --src "source-wsq/courseware/WSQ - Master Trainer Slides - Mastering Semiconductor Key Modules for Enhanced CMOS Process Integration and Device Performance - v9.0.pptx" --out "$OUT" \
  --old-title "Mastering Semiconductor Key Modules for Enhanced CMOS Process Integration and Device Performance" --new-title "Semiconductor Process Fundamentals Masterclass" \
  --old-code TGS-2024051248 --new-code C716 --tsc "ELE-SIS-4002-1.1" \
  --old-version v9.0 --new-version v1.0 \
  --sub "Version v9.0 · 20 August 2026=>Version v1.0 · 1 October 2026" \
  --sub "CMOS Process Integration · TGS-2024051248=>Semiconductor Process Fundamentals · C716" \
  --sub "TGS-2024051248-Mastering-Semiconductor-Key-Modules-for-Enhanced-CMOS-Process-Integration-and-Device=>C716-Semiconductor-Process-Fundamentals-Masterclass" \
  --wsq-slides 1,7,8,9,12,13,14,16,131,134,135,136 --feedback-slide 137
python3 tools/fix_deck.py
