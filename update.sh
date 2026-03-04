#!/bin/bash
# Monthly knowledge base update
# Run manually or schedule via Task Scheduler (Windows) / cron (Mac/Linux)
#
# Windows Task Scheduler:
#   Program: bash
#   Arguments: ~/Documents/Coding/knowledge-base/update.sh
#   Trigger: Monthly
#
# Mac/Linux cron (1st of each month at 8am):
#   0 8 1 * * ~/development/coding/knowledge-base/update.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$SCRIPT_DIR/update.log"

echo "$(date '+%Y-%m-%d %H:%M:%S') — Starting knowledge base update" | tee -a "$LOG"
cd "$SCRIPT_DIR"
python3 fetch.py update 2>&1 | tee -a "$LOG"
echo "$(date '+%Y-%m-%d %H:%M:%S') — Done" | tee -a "$LOG"
