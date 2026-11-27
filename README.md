# Secure Delivery Platform

**Neutral, beginner-oriented DevSecOps portfolio**. GitHub `main` is the single source of truth; GitHub Actions tests it and syncs it to GitLab. GitLab CI independently tests the mirrored code. The app is a minimal FastAPI service with Docker and Helm deployment examples. **No claim of production readiness or live CI validation is made.**

## Status (as shipped)
| Component | Shipped | Validated in this package |
|---|---|---|
| FastAPI + pytest | Yes | Local test pending validation report |
| GitHub Actions + GitLab CI (pytest, Bandit, pip-audit) | Yes | Configuration only; cloud runs not verified |
| GitHub → GitLab one-way sync | Yes | Configuration only; requires user tokens and repos |
| Dockerfile | Yes | Docker build not verified in this environment |
| Helm chart | Yes | Helm/kind deployment not verified in this environment |
| Gitleaks / Trivy manual exercises | Scripts and docs | Not part of enforced CI; run and record evidence |
| Prometheus/Grafana example | Yes | Not verified end-to-end |
| AWS / Terraform / Ansible / ArgoCD | No | Extension plans only |

## Start here
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
uvicorn app.main:app --reload
# Separate terminal: curl -f http://127.0.0.1:8000/health
```

See `docs/architecture/` for Architecture Decision Records (ADRs) and `docs/dual-platform-runbook.md` for the GitHub-to-GitLab sync runbook. GitLab is a mirror: do not push to its `main` directly. Never store CI tokens in Git, documentation or AI prompts.

## Scope boundaries
Security scanning is indicative, not a proof the system is secure. An intentionally failing test is preferable to adding a live credential or exploitable application. All exercises should run on locally controlled systems or explicitly authorized environments.

## Official docs
- https://docs.github.com/en/actions
- https://docs.gitlab.com/ci/
- https://docs.docker.com/get-started/
- https://kubernetes.io/docs/tutorials/kubernetes-basics/
- https://helm.sh/docs/
- https://trivy.dev/docs/latest/
- https://github.com/gitleaks/gitleaks
