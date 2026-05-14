---
description: Analyze current sprint progress, then prepare the next 2-week sprint by creating issues, labels, milestone, and project field values from the catalog.
argument-hint: "[sprint-number]   # optional override; otherwise auto-detected from today's date"
---

You are helping plan the next sprint of qeetro. Sprint cadence is **2 weeks starting Monday, May 18, 2026** (Sprint 1). Sprints 2..10 follow at 14-day intervals. The full plan lives in [docs/planning/04-issue-catalog.md §14](docs/planning/04-issue-catalog.md).

## Step 1 — Determine which sprint is being planned

1. Get today's date.
2. Compute the **current sprint number** from the cadence:
   - Sprint 0: 2026-05-14 to 2026-05-17 (planning window only — not a real iteration)
   - Sprint 1: 2026-05-18 to 2026-05-31
   - Sprint 2: 2026-06-01 to 2026-06-14
   - ...continues every 14 days through Sprint 10 (ends 2026-10-04)
3. **Next sprint = current + 1**, unless the user passed an explicit number in `$ARGUMENTS`.
4. State the inferred current and next sprint numbers + their date windows so the user can correct you before any GitHub mutation runs.

## Step 2 — Audit what is actually done

Pull the live state from GitHub:

```bash
gh issue list --repo qeetgroup/qeetro --milestone "M<N> - <title>" --state all \
  --json number,title,state,labels,closedAt,milestone --limit 200
```

Then for each issue in the current milestone:

1. **Done**: `state == "closed"` and no `won't-do` label.
2. **Carryover candidate**: open issues that were targeted for current sprint and have not finished.
3. **Won't do**: closed with that explicit reason.

Cross-check against the project field state:

```bash
./scripts/configure_project.py --phase 4   # only safe if Sprint 1 issues; for general queries, use the GraphQL query below
```

Or directly:

```bash
cat <<'EOF' | gh api graphql --input -
{"query":"query{organization(login:\"qeetgroup\"){projectV2(number:23){items(first:100){nodes{id content{__typename ... on Issue{number title state}} fieldValues(first:30){nodes{... on ProjectV2ItemFieldSingleSelectValue{field{... on ProjectV2SingleSelectField{name}} name} ... on ProjectV2ItemFieldIterationValue{field{... on ProjectV2IterationField{name}} title}}}}}}}}"}
EOF
```

Summarize: completed count, carryover count, total scope vs catalog plan. Show the user before proceeding.

## Step 3 — Read the catalog for the next sprint

Look in [docs/planning/04-issue-catalog.md §13](docs/planning/04-issue-catalog.md) for every catalog row tagged `Sprint: <next-sprint-number>`. Examples:

- Sprint 2 → ID-001, AUTH-001..004, ORG-001..002, MEM-001..002, PERM-001..003, UI-AUTH-001, UI-ORG-001
- Sprint 3 → TEAM-001..002, PROJ-001..002, UI-PROJ-001, ISS-001..005, UI-ISS-001
- Sprint 4 → BACKLOG-001..002, BOARD-001..002, UI-BACKLOG-001, UI-BOARD-001, FILTER-001
- Sprint 5 → CMT-*, EVT-001, ACT-001, UI-ACT-001, RT-001..003, UI-RT-001, NOTIF-001..002, UI-NOTIF-001, AUD-001
- Sprint 6 → EPIC-*, SPR-*, UI-EPIC/SPR/ROAD, ROAD-001..002
- Sprint 7 → ANA-*, SEARCH-*, FILE-001, AI-001..005, UI-AI-001
- Sprint 8 → GH-*, SLACK-*, AUTO-*, UI-AUTO-001, QUEUE-001
- Sprint 9 → SEC-*, DATA-001, PERF-001, OBS-*, UX-001, QA-001, REL-001
- Sprint 10 → API-001..002, WEBHOOK-001, IMP-*, DOCS-001, REL-002

Use the catalog row's metadata (Type, Domain, Priority, Size, Dependencies, full description) as the source of truth.

## Step 4 — Add carryover from the current sprint

For every incomplete issue from the current sprint:

1. Confirm it should carry forward (vs descope to backlog vs split). Ask the user only for items that look genuinely stuck — apply the **carry-forward by default** rule for everything else.
2. Update its `Sprint` iteration field to the next iteration.
3. Update its Start/End/Due dates to fall inside the next sprint window.

## Step 5 — Generate issue body files

Mirror the established pattern from [scripts/sprint1-issues/](scripts/sprint1-issues/):

1. Create `scripts/sprint<N>-issues/` directory.
2. For each catalog ID, generate `<ID>.md` with the standard body sections:
   - Metadata (Type, Parent Issue, Domain, Priority, Complexity, Sprint, Dependencies, Catalog ID)
   - Content (Description, Business Context, Problem Statement, Scope, Technical Notes, UX Notes, API Notes, Database Notes, Security Considerations, Performance Considerations, Edge Cases)
   - Delivery (Acceptance Criteria, Testing Requirements, Definition of Done)
3. Expand the terse catalog row into full implementation-ready prose. Do NOT invent scope beyond what the catalog row implies; pull surrounding context from [02-architecture-blueprint.md](docs/planning/02-architecture-blueprint.md) when domain semantics are needed.
4. Pause and let the user review one or two body files before generating all of them.

## Step 6 — Create labels, milestone, GitHub issues, project linkage, field values

Reuse the established script patterns:

1. **Labels** — extend `scripts/create-labels-sprint1.sh` into `scripts/create-labels-sprint<N>.sh` adding only the new sprint label (`sprint:NN`) and any domain labels not yet created. Run it.

2. **Milestone** — create with:
   ```bash
   gh api repos/qeetgroup/qeetro/milestones \
     -f title="M<N> - <title from §11>" \
     -f state=open \
     -f description="Sprint <N> window..." \
     -f due_on="<sprint-end>T23:59:59Z"
   ```
   Title and dates come from [03-github-project-setup.md §11](docs/planning/03-github-project-setup.md).

3. **Issues** — write `scripts/create-sprint<N>-issues.sh` (modeled on `create-sprint1-issues.sh`) with one `create_issue` line per catalog ID. Each line passes: `--title "[ID] <human title>"`, `--body-file scripts/sprint<N>-issues/<ID>.md`, `--milestone "M<N> - ..."`, `--label type:<type> --label sprint:<NN> --label release:<rel> --label domain:<domain> --label priority:<prio> --label size:<size>`. Run it.

4. **Add to project** — loop over the new issue numbers and `gh project item-add 23 --owner qeetgroup --url <issue-url>`.

5. **Set project field values** — extend `scripts/configure_project.py` PF_METADATA with the new sprint's tuples, OR add a new function (`phase4_set_values_sprint<N>`) that mirrors the pattern. Run `./scripts/configure_project.py --phase 4`.

## Step 7 — Set Start/End/Due dates by Size + dependency tier

Use the catalog dependency graph to put issues in tiers within the 2-week window. Size→days mapping:
- XS ≈ 0.5d, S = 1d, M = 2–3d, L = 4–5d, XL = split before scheduling.

Schedule:
- Foundational/blocking issues → first half of week 1.
- Dependents → as their predecessors complete.
- Parallel-track issues sharing a tier → identical start dates (or staggered by domain to reduce solo context-switch cost).
- All `Due Date` = sprint end (M<N> milestone due date).

Apply via the same pattern as the Sprint 1 date update script (see prior conversation; can also be written as `scripts/set-sprint<N>-dates.py`).

## Step 8 — Update planning docs

1. Add `docs/planning/sprint-<N>-checklist.md` mirroring [sprint-0-checklist.md](docs/planning/sprint-0-checklist.md): one checkbox per catalog ID + sprint exit criteria.
2. Update [docs/planning/README.md](docs/planning/README.md) index to link the new checklist.
3. If any architectural decision changed during planning, capture it in `docs/adr/NNNN-<slug>.md` using `docs/adr/_template.md`.

## Step 9 — Report

Output a final summary table:

| Metric | Sprint <current> result | Sprint <next> plan |
|---|---|---|
| Issues completed |  |  |
| Issues carried over |  |  |
| New issues scheduled |  | |
| Critical-priority count |  |  |
| Total story points (size sum) |  |  |
| First issue to start |  |  |
| Sprint window |  |  |

Then state: "Sprint <next> is ready. The first issue to start on <date> is [<ID>] <title> (#<number>)."

## Guardrails

- **Do not skip Step 1's date confirmation.** Sprint numbers are derivable but the user may want to plan a sprint other than the chronologically-next one.
- **Do not invent issues that are not in the catalog.** If the user wants new work outside the plan, ask explicitly and add it as a separate spike or feature with its own ADR.
- **Do not modify completed sprint issues.** Past sprints are immutable.
- **All shell scripts must be idempotent.** Use the existing `gh issue list` + title-match pattern to skip existing issues.
- **Reference the planning doc, do not duplicate it.** Issue bodies should link to the architecture sections, not restate them.
