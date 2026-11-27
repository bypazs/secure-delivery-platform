# Dual-platform runbook: GitHub (primary) → GitLab (mirror)


## GitHub → GitLab one-way sync (new)
**Source of truth:** GitHub `main`. **Destination:** empty GitLab project. Never commit directly to GitLab `main` or enable GitLab→GitHub mirroring; GitHub is authoritative. Each provider runs its *own* CI workflow (`.github/workflows/ci.yml` and `.gitlab-ci.yml`).

1. Create an **empty private** GitHub repository and an **empty private** GitLab project, without auto-generated README/license; use matching project names if convenient.
2. In GitLab, create a short-lived **Project Access Token** with `write_repository` if the project/plan permits; otherwise a narrowly scoped personal access token (`write_repository`). Its user must have permission to push to main. If main is protected, configure a dedicated allowed-to-push bot or adjust protection intentionally; never disable protection casually.
3. In GitHub → repository **Settings → Secrets and variables → Actions**, add repository **Secret** `GITLAB_TOKEN` (token value) and repository **Variable** `GITLAB_REPO_URL` (`https://gitlab.com/YOUR_NAMESPACE/YOUR_PROJECT.git`; this is not secret).
4. From the project folder, after checking `.gitignore` and `git status`, do `git init`, `git add .`, `git commit -m "Initial portfolio"`, `git branch -M main`, `git remote add origin https://github.com/YOUR_USERNAME/YOUR_PROJECT.git`, then `git push -u origin main` (replace placeholders first).
5. In GitHub **Actions**, check both `CI — Tests and Security` and `Sync main to GitLab (one-way)`; then in GitLab **Build → Pipelines**, inspect test/security jobs. If one provider fails, debug it separately; do not claim both passed.
6. Verify commit identity via `git ls-remote https://github.com/YOUR_USERNAME/YOUR_PROJECT.git refs/heads/main` and `git ls-remote https://gitlab.com/YOUR_NAMESPACE/YOUR_PROJECT.git refs/heads/main` and compare the **40-character hashes**. If the repos are private, authenticate through your approved Git credential manager or compare each site's main commit UI.
7. Use Pull Requests on GitHub. The sync only runs for pushes to `main`; PRs must pass CI before merge. When a commit is pushed to GitLab, normal GitLab CI may run according to project settings and runner availability. A failed GitLab job is not proof mirroring failed; inspect the commit SHA separately.

**Security:** never paste tokens into prompts/logs/README; use a token with the narrowest scope and expiration, and rotate it if exposed. GitHub secret is not available to untrusted fork PR workflows. The mirror workflow deliberately uses a **fast-forward-only push** (no `--force`, no `--mirror`), so it fails safely if the GitLab branch diverges; investigate before fixing history. No real accounts or CI runs are set up by the ZIP alone.

Docs: https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets , https://docs.gitlab.com/security/tokens/access_token_scopes/ , https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax , https://docs.gitlab.com/ci/quick_start/ .

## Interview talking points
- Why one-way? A single source of truth prevents divergent edits and accidental conflicts.
- What is mirrored? Git commits on `main`; not issues, CI logs, PRs, permissions or secrets.
- What if GitHub CI passes, GitLab CI fails? Same SHA but different runners and CI definitions; check failed job logs and reproduce the environment.
- What if push is rejected (non-fast-forward)? Stop; inspect both commits, avoid force pushing or deleting history.
- What evidence? Screenshot GH Actions CI, sync, GitLab CI, same SHA, and explain one red/green test on a safe branch.
