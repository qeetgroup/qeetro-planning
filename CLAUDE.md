# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository state

This repo is **pre-implementation**. There is no application code, no `package.json`, no monorepo workspace yet. Everything under `apps/`, `packages/`, `infra/docker`, `infra/terraform`, and `scripts/` (except the issue-management scripts) is intentionally empty (`.gitkeep`-only) and reserved for Sprint 1 (issues PF-001..PF-012).

Sprint 0 (May 14–17, 2026) is a planning window. Sprint 1 begins **Monday, May 18, 2026** and is when real source code first lands. Until then, the deliverables in this repo are: the planning blueprint, the GitHub Project board configuration, and the issue catalog.

Do **not** scaffold the monorepo, install dependencies, or write app code unprompted. Those actions correspond to specific tracked issues (see below) and the maintainer wants to do them himself or under explicit instruction.

## The planning blueprint is the source of truth

Before answering any architectural, scoping, or sprint-related question, read the relevant section of `docs/planning/`:

- [docs/planning/README.md](docs/planning/README.md) — index.
- [docs/planning/01-competitor-strategy.md](docs/planning/01-competitor-strategy.md) — competitor analysis, product strategy, philosophy.
- [docs/planning/02-architecture-blueprint.md](docs/planning/02-architecture-blueprint.md) — 26-domain catalog, system architecture (FE/BE/DB/realtime/queue/event/search/cache/AI/observability/CI-CD/authz/multi-tenancy), monorepo design, MVP scope, roadmap.
- [docs/planning/03-github-project-setup.md](docs/planning/03-github-project-setup.md) — project fields, views, workflows, labels, milestones M0–M9, epic hierarchy E00–E10.
- [docs/planning/04-issue-catalog.md](docs/planning/04-issue-catalog.md) — ~75 implementation-ready issues with metadata, dependencies, acceptance criteria, sprint plan (Sprint 0–10), implementation order, and risk register.
- [docs/planning/sprint-0-checklist.md](docs/planning/sprint-0-checklist.md) — operational checklist for closing M0.
- [docs/planning/project-board-ui-setup.md](docs/planning/project-board-ui-setup.md) — UI steps for the two project configurations the GitHub API cannot do (view creation + iteration date rewrite).

ADRs live in [docs/adr/](docs/adr/). The first one, [0001-modular-monolith.md](docs/adr/0001-modular-monolith.md), captures the decision to build qeetro as a modular monolith with deferred service extraction — this constrains many later architectural choices.

## Issue ID conventions (used in catalog, branches, PRs, commits)

Every catalog issue has a stable prefix-ID. Branch names, PR titles, and commit messages reference the ID:

`PL-*` planning · `PF-*` platform foundation · `ID-*` identity · `AUTH-*` auth · `ORG-*` organizations · `MEM-*` membership · `PERM-*` permissions · `TEAM-*` teams · `PROJ-*` projects · `ISS-*` issues · `BACKLOG-*` · `BOARD-*` · `FILTER-*` · `CMT-*` comments · `EVT-*` events · `ACT-*` activity · `RT-*` realtime · `NOTIF-*` · `AUD-*` audit · `EPIC-*` · `SPR-*` sprints · `ROAD-*` roadmaps · `ANA-*` analytics · `SEARCH-*` · `FILE-*` · `AI-*` · `GH-*` GitHub integration · `SLACK-*` · `AUTO-*` automation · `QUEUE-*` · `SEC-*` security · `DATA-*` · `PERF-*` · `OBS-*` · `UX-*` · `QA-*` · `REL-*` release · `API-*` public API · `WEBHOOK-*` · `IMP-*` import · `DOCS-*` · `ENT-*` enterprise spike · `FUT-*` future spike · `UI-*` paired frontend issue.

GitHub issue titles use the form `[<ID>] <human title>`. The body files in [scripts/sprint1-issues/](scripts/sprint1-issues/) show the canonical body structure (Metadata → Content → Delivery).

## GitHub Project operations

The board lives at https://github.com/orgs/qeetgroup/projects/23 (`@qeetro roadmap`). Configuration is fully scripted and idempotent.

**Run order if rebuilding from scratch:**

```bash
./scripts/create-labels-sprint1.sh           # 25 labels (type, domain, priority, size, sprint, release)
./scripts/create-sprint1-issues.sh           # 12 PF-001..PF-012 issues with body + labels + milestone
./scripts/configure_project.py --phase all   # 5 phases: fields, options, iterations, item values, views
```

**Common one-offs:**

- `./scripts/configure_project.py --phase 4` — re-bind issue field values after fixing iteration dates in the UI.
- `gh project field-list 23 --owner qeetgroup --limit 100` — quickly inspect fields.
- `gh issue list --repo qeetgroup/qeetro --milestone "M1 - Platform Skeleton"` — list Sprint 1 issues.

**GitHub API limitations to remember:**

- The public GraphQL schema does **not** expose `createProjectV2View` / `updateProjectV2View` — view creation must be done in the web UI. The schema has been introspected; do not retry this in code.
- Iteration `startDate` cannot be rewritten via API. To fix sprint dates, delete iterations in the UI and recreate them.
- Both limitations are documented step-by-step in [docs/planning/project-board-ui-setup.md](docs/planning/project-board-ui-setup.md).

## Architectural lock-ins (apply from the first line of code)

These are non-negotiables from [04-issue-catalog.md §15](docs/planning/04-issue-catalog.md):

1. **`organization_id` on every tenant-owned table.** No exceptions. Migrations are reviewed against this rule.
2. **Transactional outbox before any side-effect work.** EVT-001 is a hard prerequisite for activity, realtime, notifications, search, analytics, automation, integrations, and AI.
3. **Permission-filtered presentation events for realtime.** Never broadcast raw domain events to clients (RT-002/RT-003).
4. **Versioned event contracts in `packages/event-contracts`** (`<domain>.<event>.v<N>` naming).
5. **Central `PolicyService` for authorization.** Modules must not invent their own access checks.
6. **No `process.env` reads outside `packages/config`** (PF-011 will add the lint rule).
7. **Apps must not import other apps.** Apps may import packages; packages may not import apps. `packages/domain` must not import Prisma, NestJS, or React.
8. **`apps/api` modules must not import each other's repositories.** Cross-module work goes via application services or domain events.

## Sprint cadence

- 2-week sprints starting 2026-05-18 (Sprint 1).
- M-milestones close at the end of each multi-sprint phase:
  - M0 (May 14–17): planning
  - M1 (May 18–31): platform skeleton — Sprint 1
  - M2 (Jun 1–14): identity + tenancy — Sprint 2
  - M3 (Jun 15–Jul 12): work core — Sprints 3–4
  - … through M9 v1 launch (Dec 27, 2026)
- Status field values: Triage, Ready, In Progress, In Review, Blocked, Done, Won't Do. New issues default to Triage; refinement promotes them to Ready.

## When asked to "implement X" before its sprint

Push back. The catalog ordering is deliberate. Building, say, the AI assistant before the outbox + permission engine exist is one of the documented anti-patterns. Suggest opening the corresponding catalog issue and treating any work as a documented spike if it must happen early.

## Sprint workflow slash commands

The repo ships five project-level slash commands in [.claude/commands/](.claude/commands/). Use them instead of re-deriving sprint state from scratch — they are the canonical mutation/inspection paths for sprint operations.

| Command | Mutates? | Use when |
|---|---|---|
| **`/load-context`** | No | At the start of any non-trivial session. Reads CLAUDE.md, planning blueprint, ADRs, the current sprint checklist, open milestones, and the live project state, then summarises. |
| **`/sprint-status [N]`** | No | Mid-sprint. Reports Done / In Review / In Progress / Blocked / Ready / Triage counts, burndown vs sprint end, at-risk items, blockers. |
| **`/architecture-check [path or branch]`** | No | Before merge, or before opening a PR. Audits a diff/branch/path against the 8 architectural lock-ins and produces PASS / PASS-with-notes / FAIL. |
| **`/sprint-review [N]`** | Yes | On or after sprint end. Tallies completion, generates `docs/planning/sprint-<N>-retro.md`, updates the sprint checklist, closes the milestone (with confirmation). |
| **`/plan-next-sprint [N]`** | Yes | Day before next sprint starts. Auto-detects the next sprint from today's date (or takes an explicit number), pulls the catalog's planned issues, audits the previous sprint for carryover, generates `scripts/sprint<N>-issues/<ID>.md` body files, creates labels/milestone/issues, adds them to the project, sets Status/Type/Domain/Priority/Size/Iteration/Release fields, and computes Start/End/Due dates by dependency-aware tiering. |

Recommended cadence:
1. Session start: `/load-context`
2. Mid-sprint check: `/sprint-status`
3. Before merging a PR with non-trivial change: `/architecture-check`
4. Last day of sprint: `/sprint-review`
5. Day before next sprint starts: `/plan-next-sprint`

All commands are idempotent and read the planning blueprint as the source of truth. They do not invent scope outside what `docs/planning/04-issue-catalog.md` defines for the target sprint.
