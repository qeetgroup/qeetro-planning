#!/usr/bin/env bash
# Create the 12 Sprint 1 issues (PF-001..PF-012) in qeetgroup/qeetro
# with proper titles, bodies, labels, and the M1 milestone.
# Re-runnable: skips any title that already exists.
set -euo pipefail

REPO="qeetgroup/qeetro"
MILESTONE="M1 - Platform Skeleton"
BODY_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/sprint1-issues"
COMMON_LABELS=("type:task" "sprint:01" "release:mvp")

create_issue() {
  local id="$1" title="$2"; shift 2
  local extra_labels=("$@")
  local body_file="${BODY_DIR}/${id}.md"

  if [ ! -f "$body_file" ]; then
    echo "MISSING body file: $body_file" >&2
    return 1
  fi

  local full_title="[${id}] ${title}"

  # Skip if an issue with this exact title already exists (open or closed).
  if gh issue list --repo "$REPO" --state all --search "\"${full_title}\" in:title" --json title -q '.[].title' \
      | grep -Fxq "$full_title"; then
    echo "exists  $full_title"
    return 0
  fi

  local label_args=()
  for l in "${COMMON_LABELS[@]}" "${extra_labels[@]}"; do
    label_args+=("--label" "$l")
  done

  gh issue create \
    --repo "$REPO" \
    --title "$full_title" \
    --body-file "$body_file" \
    --milestone "$MILESTONE" \
    "${label_args[@]}" \
    | tail -1
}

create_issue PF-001 "Scaffold pnpm monorepo"                                            domain:infrastructure priority:critical size:M
create_issue PF-002 "Configure TypeScript build boundaries"                             domain:infrastructure priority:critical size:M
create_issue PF-003 "Configure linting, formatting, and commit hygiene"                 domain:devops         priority:high     size:S
create_issue PF-004 "Create Next.js web shell"                                          domain:frontend       priority:critical size:M
create_issue PF-005 "Create NestJS API shell"                                           domain:backend        priority:critical size:M
create_issue PF-006 "Create shared UI, config, types, and event contract packages"      domain:infrastructure priority:high     size:S
create_issue PF-007 "Add Docker Compose for Postgres and Redis"                         domain:infrastructure priority:critical size:S
create_issue PF-008 "Add Prisma migration foundation"                                   domain:database       priority:critical size:M
create_issue PF-009 "Add GitHub Actions CI"                                             domain:devops         priority:critical size:M
create_issue PF-010 "Add test harness and seed data strategy"                           domain:testing        priority:high     size:M
create_issue PF-011 "Add environment and secrets validation"                            domain:infrastructure priority:high     size:S
create_issue PF-012 "Add request IDs, structured logs, health checks, and baseline metrics" domain:observability priority:high  size:M

echo "Done."
