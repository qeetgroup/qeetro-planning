# 9. GitHub Project Structure

Create a GitHub Project named:

```text
qeetro roadmap
```

## Recommended Project Fields

| Field | Type | Values / Notes |
| --- | --- | --- |
| Status | Single select | Triage, Ready, In Progress, In Review, Blocked, Done, Won't Do |
| Issue Type | Single select | Epic, Feature, Story, Task, Bug, Spike, Enhancement |
| Domain | Single select | Auth, Identity, Organizations, Permissions, Workspaces, Teams, Projects, Issues, Boards, Backlog, Sprints, Epics, Comments, Activity, Notifications, Realtime, Search, Files, Analytics, Automation, Integrations, AI, Audit, Infrastructure, Frontend, Backend, Database, DevOps |
| Priority | Single select | Critical, High, Medium, Low |
| Complexity | Single select | XS, S, M, L, XL |
| Sprint | Iteration | 2-week iterations, starting Monday, May 18, 2026 if implementation begins immediately |
| Release | Single select | Phase 0, MVP, Beta, v1, v2, Future |
| Milestone | GitHub milestone | Mirror the milestones below |
| Owner | Assignee | Person accountable |
| Team | Single select | Platform, Product Core, Frontend, AI/Automation, Integrations |
| Start Date | Date | Planned start |
| Target Date | Date | Planned completion |
| Blocked By | Text | Issue numbers or external dependency |
| Risk | Single select | None, Low, Medium, High |

## Project Views

1. `00 Triage`
   - Filter: `status:Triage`
   - Purpose: new ideas, spikes, unclassified issues.

2. `01 Roadmap`
   - Layout: roadmap/timeline.
   - Group by: Release or Milestone.
   - Shows: epics/features only.

3. `02 Product Backlog`
   - Layout: table.
   - Filter: `status:Ready,Blocked` and `type:feature,story,task`.
   - Sort: Priority, Sprint, Domain.

4. `03 Current Sprint`
   - Layout: board.
   - Group by: Status.
   - Filter: current iteration.

5. `04 Engineering Board`
   - Layout: board.
   - Group by: Domain.
   - Filter: not Done.

6. `05 Release MVP`
   - Layout: table.
   - Filter: `release:MVP`.

7. `06 Architecture and Platform`
   - Filter: `domain:infrastructure,database,backend,devops` or `type:spike`.

8. `07 Risks and Blockers`
   - Filter: `status:Blocked` or `risk:High`.

9. `08 Done`
   - Filter: `status:Done`.

## Workflow States

| State | Meaning | Entry Criteria | Exit Criteria |
| --- | --- | --- | --- |
| Triage | Needs shaping | Issue created | Metadata, priority, and owner assigned |
| Ready | Ready for implementation | Scope clear, dependencies identified | Work starts |
| In Progress | Actively being worked | Assignee committed | PR opened or review needed |
| In Review | PR/design review/test review | Implementation complete | Approved and merged |
| Blocked | Cannot proceed | Blocker documented | Blocker removed or issue descoped |
| Done | Completed | Acceptance criteria met | Closed |
| Won't Do | Explicitly rejected/deferred | Reason documented | Closed |

## Status Transitions

- Triage -> Ready after refinement.
- Ready -> In Progress when pulled into sprint.
- In Progress -> Blocked if dependency prevents progress.
- Blocked -> Ready or In Progress after unblock.
- In Progress -> In Review when implementation/testing is ready for review.
- In Review -> Done after merge and verification.
- Any state -> Won't Do only with a comment explaining reason.

## Automation Recommendations

- Add new issues to `qeetro roadmap` automatically.
- Set Status to Triage for new issues without Status.
- When issue is assigned to current iteration, set Status to Ready.
- When linked PR opens, set Status to In Review only if issue was In Progress.
- When linked PR merges and all sub-issues are done, set Status to Done.
- When `blocked` label is applied, set Status to Blocked.
- When issue is closed as not planned, set Status to Won't Do.
- Auto-archive Done items after 30 days, but not epics until release retrospective.

## Sprint Lifecycle

1. Backlog refinement: classify, split, estimate, dependency-check.
2. Sprint planning: select issues with clear acceptance criteria and capacity fit.
3. Daily execution: update Status, blockers, and PR links.
4. Mid-sprint risk review: inspect Blocked, scope changes, and carryover risk.
5. Sprint review: demo merged work only.
6. Retrospective: capture process improvements as issues/spikes.
7. Close sprint: move incomplete issues back to Ready or next Sprint with notes.

# 10. Label Taxonomy

GitHub labels are flat, so prefixes keep the system clean.

## Type Labels

- `type:epic`
- `type:feature`
- `type:story`
- `type:task`
- `type:bug`
- `type:spike`
- `type:enhancement`

## Domain Labels

- `domain:auth`
- `domain:identity`
- `domain:organizations`
- `domain:workspaces`
- `domain:teams`
- `domain:projects`
- `domain:issues`
- `domain:epics`
- `domain:boards`
- `domain:backlog`
- `domain:sprints`
- `domain:comments`
- `domain:activity`
- `domain:notifications`
- `domain:realtime`
- `domain:permissions`
- `domain:analytics`
- `domain:automation`
- `domain:integrations`
- `domain:ai`
- `domain:search`
- `domain:files`
- `domain:roadmaps`
- `domain:audit`
- `domain:settings`
- `domain:infrastructure`
- `domain:database`
- `domain:frontend`
- `domain:backend`
- `domain:devops`

## Priority Labels

- `priority:critical`
- `priority:high`
- `priority:medium`
- `priority:low`

## Complexity Labels

- `size:XS`
- `size:S`
- `size:M`
- `size:L`
- `size:XL`

## Status Labels

- `status:blocked`
- `status:in-progress`
- `status:ready`
- `status:review`
- `status:done`

Use Status field as the source of truth. Status labels are optional mirrors for repo issue search.

## Sprint Labels

Prefer the Iteration field. If labels are needed:

- `sprint:01`
- `sprint:02`
- `sprint:03`
- `sprint:04`
- `sprint:05`
- `sprint:06`
- `sprint:07`
- `sprint:08`
- `sprint:09`
- `sprint:10`
- `sprint:11`
- `sprint:12`
- `sprint:13`
- `sprint:14`

## Release Labels

- `release:phase-0`
- `release:mvp`
- `release:beta`
- `release:v1`
- `release:v2`
- `release:future`

## Risk Labels

- `risk:security`
- `risk:performance`
- `risk:data-model`
- `risk:integration`
- `risk:scope`
- `risk:ux`

## Dependency Labels

- `dependency:blocked-by-api`
- `dependency:blocked-by-db`
- `dependency:blocked-by-design`
- `dependency:blocked-by-infra`
- `dependency:external`

# 11. Milestones

Assuming implementation starts Monday, May 18, 2026:

| Milestone | Target Window | Goal |
| --- | --- | --- |
| M0 - Planning Complete | May 14 to May 17, 2026 | Planning docs, GitHub Project, epics, labels, milestones ready |
| M1 - Platform Skeleton | May 18 to May 31, 2026 | Monorepo, apps, CI, Docker, DB foundation |
| M2 - Identity and Tenancy | June 1 to June 14, 2026 | Auth, orgs, members, RBAC baseline |
| M3 - Work Core | June 15 to July 12, 2026 | Projects, issues, statuses, backlog, board MVP |
| M4 - Collaboration and Realtime | July 13 to August 9, 2026 | Comments, activity, realtime, notifications MVP |
| M5 - Agile Planning | August 10 to September 6, 2026 | Epics, sprints/cycles, roadmaps |
| M6 - Intelligence and Discovery | September 7 to October 4, 2026 | Search, analytics, AI assistant MVP |
| M7 - Integrations and Automation | October 5 to November 1, 2026 | GitHub/Slack basics, automation MVP |
| M8 - Beta Hardening | November 2 to November 29, 2026 | Security, observability, performance, imports, beta readiness |
| M9 - v1 Launch | November 30 to December 27, 2026 | Public API basics, enterprise polish, launch docs |

# 12. Epic Hierarchy

Use GitHub sub-issues:

```text
EPIC
  -> FEATURE
      -> STORY
          -> TECHNICAL TASK
```

Recommended top-level epics:

| Epic ID | Epic | Release | Primary Domains |
| --- | --- | --- | --- |
| E00 | Planning, Program, and Delivery System | Phase 0 | Product, TPM, DevOps |
| E01 | Platform Foundation | MVP | Infrastructure, DevOps, Database, Backend, Frontend |
| E02 | Identity, Tenancy, and Permissions | MVP | Auth, Identity, Organizations, Permissions |
| E03 | Work Core | MVP | Workspaces, Teams, Projects, Issues, Backlog, Boards |
| E04 | Collaboration, Activity, and Realtime | MVP/Beta | Comments, Activity, Realtime, Notifications, Audit |
| E05 | Agile Planning and Roadmaps | Beta | Epics, Sprints, Roadmaps, Analytics |
| E06 | Discovery and AI Assistance | Beta | Search, Files, AI, Analytics |
| E07 | Integrations and Automation | v1 | Integrations, Automation, Queues |
| E08 | Hardening, Observability, and Beta Readiness | Beta | Security, Observability, Performance, QA |
| E09 | Public API, Imports, and v1 Launch | v1 | Public API, Webhooks, Imports, Docs |
| E10 | v2 and Future Expansion | v2/Future | Enterprise, Portfolio, Marketplace, Self-hosting |

Create epics first, then attach feature/story/task sub-issues from [Issue Catalog and Sprint Plan](04-issue-catalog.md). Keep epics open until all child issues are complete and the release retrospective confirms the domain is stable enough for the next phase.
