# GitHub Project Board UI Setup Playbook

This document describes the **two configuration steps that GitHub's public GraphQL API does not support** and must be completed in the web UI for the [@qeetro roadmap](https://github.com/orgs/qeetgroup/projects/23) project.

Everything else (fields, options, labels, milestones, issue field values) has already been set by [`scripts/configure_project.py`](../../scripts/configure_project.py) and is idempotent — re-run any phase with `--phase 1..5` if needed.

## What is already configured (automated)

- **14 enterprise fields** present: `Title`, `Assignees`, `Status`, `Labels`, `Linked pull requests`, `Milestone`, `Repository`, `Reviewers`, `Parent issue`, `Sub-issues progress`, `Team`, `Priority`, `Size`, `Estimate`, `Iteration`, `Start date`, `End date`, `Due Date`, `Blocked By`, `Issue Type`, `Domain`, `Release`, `Risk`.
- **Status** options: Triage, Ready, In Progress, In Review, Blocked, Done, Won't Do.
- **Priority** options: Critical, High, Medium, Low.
- **Team** options: Platform, Product Core, Frontend, AI/Automation, Integrations.
- **Issue Type** options: Epic, Feature, Story, Task, Bug, Spike, Enhancement.
- **Domain** options: 30 values covering every architectural domain plus Testing/Observability.
- **Release** options: Phase 0, MVP, Beta, v1, v2, Future.
- **Risk** options: None, Low, Medium, High.
- **Sprint 1 issues (#118–#129)** added to the project with: Status=Ready, Issue Type=Task, Domain=correct, Priority=correct, Size=correct, Release=MVP, Team=Platform, Risk=Low, Iteration=Sprint 1.

## Step 1 — Fix the `Iteration` field dates (required before Sprint 1 starts)

The current `Iteration` field has Sprint 1 starting **2026-05-28**, but the planning doc requires **Sprint 1 = 2026-05-18 to 2026-05-31**. GitHub does not allow rewriting iteration `startDate` via API.

### Fix (UI, 2 minutes)

1. Open https://github.com/orgs/qeetgroup/projects/23.
2. Click the `…` menu (top right) → **Settings**.
3. Scroll to the **Fields** section, click the **Iteration** field.
4. Delete every existing iteration (Sprint 0 through Sprint 8).
5. Click **Add iteration** with these settings, in order:

   | # | Title | Start date | Duration |
   |---|---|---|---|
   | 1 | Sprint 1 | 2026-05-18 | 14 days |
   | 2 | Sprint 2 | 2026-06-01 | 14 days |
   | 3 | Sprint 3 | 2026-06-15 | 14 days |
   | 4 | Sprint 4 | 2026-06-29 | 14 days |
   | 5 | Sprint 5 | 2026-07-13 | 14 days |
   | 6 | Sprint 6 | 2026-07-27 | 14 days |
   | 7 | Sprint 7 | 2026-08-10 | 14 days |
   | 8 | Sprint 8 | 2026-08-24 | 14 days |
   | 9 | Sprint 9 | 2026-09-07 | 14 days |
   | 10 | Sprint 10 | 2026-09-21 | 14 days |

6. After saving, re-run phase 4 to re-bind issues to the new Sprint 1 iteration:

   ```bash
   ./scripts/configure_project.py --phase 4
   ```

Sprint 0 (May 14–17) is intentionally a milestone-only planning window, not an iteration — track those tasks under milestone **M0 - Planning Complete**.

## Step 2 — Configure the 9 enterprise views

The GitHub public GraphQL API does not expose `createProjectV2View` / `updateProjectV2View`. The 6 default views must be reshaped manually in the UI:

- Current: `Prioritized backlog`, `Status board`, `Current iteration`, `Roadmap`, `Bugs 🐛`, `My items`.
- Target: 9 enterprise views per [03-github-project-setup.md §9](03-github-project-setup.md#L29-L66).

### Renaming (existing views)

| Current name | Rename to | Why |
|---|---|---|
| `Prioritized backlog` | `02 Product Backlog` | Aligns with planning doc naming |
| `Status board` | (delete) | Replaced by `03 Current Sprint` |
| `Current iteration` | `03 Current Sprint` | Sprint-scoped board |
| `Roadmap` | `01 Roadmap` | Numbered for sort order |
| `Bugs 🐛` | (keep as utility view) | Optional auxiliary view |
| `My items` | (keep as utility view) | Optional auxiliary view |

To rename: open the view, click the small caret next to the view name in the tab bar → **Rename view**.

### Creating new views

Click the **+ New view** tab and configure each as follows.

#### `00 Triage` — Table

- Layout: **Table**
- Filter: `status:Triage`
- Sort: Priority (descending), Created (ascending)
- Visible fields: Title, Assignees, Issue Type, Domain, Priority, Size, Risk, Created
- Group by: none

#### `01 Roadmap` — Roadmap (rename existing)

- Layout: **Roadmap**
- Date fields: Start date → Target date (or End date)
- Group by: **Release**
- Zoom: Month
- Filter: `type:epic,feature`

#### `02 Product Backlog` — Table (rename existing)

- Layout: **Table**
- Filter: `status:Ready,Blocked -no:iteration`
- Sort: Priority ↓, Domain ↑
- Visible fields: Title, Assignees, Issue Type, Domain, Priority, Size, Sprint, Release, Risk
- Group by: **Domain**

#### `03 Current Sprint` — Board (rename existing)

- Layout: **Board**
- Group by: **Status**
- Filter: `iteration:@current`
- Sort: Priority ↓
- Visible fields on card: Issue Type, Domain, Priority, Size, Assignees

#### `04 Engineering Board` — Board (new)

- Layout: **Board**
- Group by: **Domain**
- Filter: `-status:Done -status:"Won't Do"`
- Sort: Priority ↓

#### `05 Release MVP` — Table (new)

- Layout: **Table**
- Filter: `release:MVP`
- Sort: Sprint ↑, Priority ↓
- Group by: **Iteration**
- Visible fields: Title, Issue Type, Domain, Priority, Size, Status, Assignees

#### `06 Architecture and Platform` — Table (new)

- Layout: **Table**
- Filter: `domain:Infrastructure,Database,Backend,DevOps,Observability,Testing OR type:Spike`
- Group by: **Domain**
- Visible fields: Title, Issue Type, Priority, Size, Status, Risk, Assignees

#### `07 Risks and Blockers` — Table (new)

- Layout: **Table**
- Filter: `status:Blocked OR risk:High`
- Sort: Risk ↓, Priority ↓
- Visible fields: Title, Domain, Priority, Size, Risk, Status, Blocked By, Assignees

#### `08 Done` — Table (new)

- Layout: **Table**
- Filter: `status:Done OR status:"Won't Do"`
- Sort: Closed date ↓
- Group by: **Iteration**
- Visible fields: Title, Issue Type, Domain, Priority, Size, Iteration

### Reorder tabs

Drag the view tabs so they appear in numbered order: `00`, `01`, `02`, `03`, `04`, `05`, `06`, `07`, `08`, then any utility views (`Bugs`, `My items`) at the end.

## Step 3 — Optional but recommended workflows

Inside **Settings → Workflows**, enable:

| Workflow | Trigger | Action |
|---|---|---|
| Auto-add to project | Item added to repo | Add to `qeetro roadmap` |
| Item closed | Issue/PR closed | Set Status → Done |
| Code review approved | PR review approved | Set Status → In Review |
| Pull request merged | PR merged | Set Status → Done |
| Auto-archive items | Item Status = Done for 30 days | Archive |

Plus a custom workflow for the planning doc's automation recommendations ([§9 Automation Recommendations](03-github-project-setup.md#L89-L98)):

| When | Then |
|---|---|
| Issue gets label `blocked` | Set Status → Blocked |
| Issue added to current iteration | Set Status → Ready (if Status was Triage) |
| Issue closed "not planned" | Set Status → Won't Do |

These cannot be configured via the public API either — set them once in the UI and they persist for the lifetime of the project.

## Verification checklist after UI work

- [ ] `Iteration` field shows `Sprint 1` starting **2026-05-18**.
- [ ] All 12 Sprint 1 issues (#118–#129) display in the new `03 Current Sprint` view, grouped by Status, under the Ready column.
- [ ] `00 Triage` is empty (good — nothing is in triage state).
- [ ] `02 Product Backlog` shows all unscheduled future-sprint work once you create more issues.
- [ ] `05 Release MVP` shows the 12 Sprint 1 issues grouped under their Sprint iteration.
- [ ] `06 Architecture and Platform` shows the Infrastructure/Backend/DevOps/Database/Observability/Testing items.
- [ ] `07 Risks and Blockers` is empty (good — nothing is currently blocked or High risk).

Once all checkboxes are ticked, the project is at full enterprise spec and Sprint 1 can start Monday May 18, 2026.
