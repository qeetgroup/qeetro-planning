---
description: Show qeetro's current sprint status — completed vs in-progress vs blocked vs untouched — without making any changes.
argument-hint: "[sprint-number]   # optional; defaults to the sprint covering today's date"
---

Report the qeetro project's current sprint status. **Read-only.** No issue mutations, no project mutations, no commits.

## Step 1 — Resolve target sprint

Sprint cadence: 2 weeks starting Mon 2026-05-18 (Sprint 1). If `$ARGUMENTS` is a number, use that. Otherwise compute from today's date.

Output the sprint number, milestone name (`M<N> - <title>`), and date window before continuing.

## Step 2 — Pull live data

Run all three in parallel:

```bash
# Issues in the milestone
gh issue list --repo qeetgroup/qeetro \
  --milestone "M<N> - <title>" --state all --limit 200 \
  --json number,title,state,labels,assignees,closedAt,createdAt

# Project field state for those items
cat <<'EOF' | gh api graphql --input -
{"query":"query{organization(login:\"qeetgroup\"){projectV2(number:23){items(first:100){nodes{id content{__typename ... on Issue{number title state}} fieldValues(first:30){nodes{__typename ... on ProjectV2ItemFieldSingleSelectValue{field{... on ProjectV2SingleSelectField{name}} name} ... on ProjectV2ItemFieldDateValue{field{... on ProjectV2Field{name}} date} ... on ProjectV2ItemFieldIterationValue{field{... on ProjectV2IterationField{name}} title startDate}}}}}}}}"}
EOF

# Recent commits and merged PRs touching the sprint
git log --since=<sprint-start> --pretty=format:"%h %ad %s" --date=short
gh pr list --repo qeetgroup/qeetro --state merged --search "merged:>=<sprint-start>" --limit 50 --json number,title,mergedAt
```

## Step 3 — Bucket the issues

Categorize every sprint issue into:

- **Done** — closed not-as-not-planned; or project Status = Done.
- **In Review** — has merged-pending or PR-open links, or project Status = In Review.
- **In Progress** — project Status = In Progress.
- **Blocked** — project Status = Blocked.
- **Ready** — refined, in sprint, not yet started.
- **Triage** — needs grooming before pickup.
- **Won't Do** — explicitly deferred this sprint.

## Step 4 — Output

Render a compact terminal-friendly report:

```
Sprint <N> — M<N> <title> (<start> to <end>)
Today: <date>   Day <X> of 14   Working days remaining: <Y>

Issues:  <total>    Done <a>   In Review <b>   In Progress <c>   Blocked <d>   Ready <e>   Triage <f>

By domain
  Infrastructure  ████░░░░░░  4/10
  Backend         ██████░░░░  6/10
  Frontend        ██░░░░░░░░  2/10

Critical-path risks:
  - [PF-008] Add Prisma migration foundation — Blocked since 2026-05-22 (DB schema review pending)
  - [PF-005] NestJS API shell — In Progress, 60% of allotted days elapsed, no PR yet

Sprint commitment: <a + b + c + d + e>/<total>   completion = <a/total>%

Carryover risk if sprint ends today:
  - <list of issues not Done that are not In Review>

Next actions:
  1. <suggested most-important next move>
  2. ...
```

## Step 5 — Guardrails

- Do not list every issue verbatim unless asked — summarize and surface only the issues that need attention.
- If today's date is **outside** the requested sprint window, state that loudly and ask if the user wants the actual current sprint, the most recently completed sprint, or the future one.
- Treat any catalog ID not yet present as an issue as a "not-yet-created" gap and surface it separately.
- Do not propose changes here — `/plan-next-sprint` and `/sprint-review` are the mutation paths.
