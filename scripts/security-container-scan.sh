#!/usr/bin/env bash
# Manual verification exercise; requires local installed trivy and gitleaks.
set -euo pipefail
: "${IMAGE_TAG:=secure-delivery-platform:dev}"
command -v trivy >/dev/null || { echo 'Install Trivy from https://trivy.dev/docs/latest/getting-started/installation/'; exit 2; }
command -v gitleaks >/dev/null || { echo 'Install Gitleaks from https://github.com/gitleaks/gitleaks'; exit 2; }
# Working-tree scan; use gitleaks git for history scan as separate exercise.
gitleaks dir . --no-banner --redact --exit-code 1
trivy image --severity HIGH,CRITICAL --exit-code 1 "$IMAGE_TAG"
