#!/usr/bin/env bash
# Create labels needed for Sprint 1 of qeetro.
# Re-runnable: existing labels are skipped (gh prints an error line and we move on).
set -u

REPO="qeetgroup/qeetro"

create_label() {
  local name="$1"
  local color="$2"
  local desc="$3"
  if gh label create "$name" --color "$color" --description "$desc" --repo "$REPO" >/dev/null 2>&1; then
    echo "created  $name"
  else
    # try update if exists
    if gh label edit "$name" --color "$color" --description "$desc" --repo "$REPO" >/dev/null 2>&1; then
      echo "updated  $name"
    else
      echo "skipped  $name"
    fi
  fi
}

# Type
create_label "type:epic"          "6f42c1" "Top-level epic spanning multiple features"
create_label "type:feature"       "1d76db" "Feature group inside an epic"
create_label "type:story"         "0e8a16" "User-visible behavior unit"
create_label "type:task"          "c5def5" "Technical task"
create_label "type:bug"           "b60205" "Defect or regression"
create_label "type:spike"         "fbca04" "Time-boxed investigation"
create_label "type:enhancement"   "a2eeef" "Incremental improvement"

# Priority
create_label "priority:critical"  "b60205" "Must complete this sprint, blocks downstream work"
create_label "priority:high"      "d93f0b" "Should complete this sprint"
create_label "priority:medium"    "fbca04" "Plan but can slip"
create_label "priority:low"       "0e8a16" "Nice to have"

# Complexity
create_label "size:XS"            "ededed" "Hours"
create_label "size:S"             "d4d4d4" "Up to a day"
create_label "size:M"             "a0a0a0" "Few days"
create_label "size:L"             "606060" "About a week"
create_label "size:XL"            "303030" "Multi-week, consider splitting"

# Domain labels needed for Sprint 1
create_label "domain:infrastructure" "5319e7" "Monorepo, tooling, runtime infra"
create_label "domain:devops"         "5319e7" "CI/CD, deployment, automation"
create_label "domain:frontend"       "1d76db" "Next.js web app"
create_label "domain:backend"        "0052cc" "NestJS API"
create_label "domain:database"       "c2e0c6" "Prisma, Postgres schema and migrations"
create_label "domain:testing"        "bfdadc" "Test harness, fixtures, coverage"
create_label "domain:observability"  "f9d0c4" "Logging, tracing, metrics"

# Sprint
create_label "sprint:01"          "0052cc" "Sprint 1 (May 18 to May 31, 2026)"

# Release
create_label "release:mvp"        "e99695" "MVP release scope"

echo "Done."
