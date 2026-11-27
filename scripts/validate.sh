#!/usr/bin/env bash
set -euo pipefail
python3 -m compileall -q app tests
python3 -m pytest -q
python3 -m bandit -r app -ll
python3 -m pip_audit -r requirements.txt
printf '\nValidated: compile, pytest, Bandit, pip-audit.\n'
