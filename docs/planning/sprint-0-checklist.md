# Sprint 0 Checklist (May 14 – May 17, 2026)

Operational checklist for closing out the M0 milestone before Sprint 1 starts on Monday, May 18, 2026. Each task maps to an issue ID from [04-issue-catalog.md §13](04-issue-catalog.md). Check items as the corresponding GitHub issues move to Done.

## PL-001 — Create `qeetro roadmap` GitHub Project

- [ ] Project created at the org/user level and named exactly `qeetro roadmap`.
- [ ] Project linked from this repo's README and from `docs/planning/README.md`.
- [ ] All 14 custom fields configured per [03-github-project-setup.md §9](03-github-project-setup.md):
  - [ ] Status (single select, 7 values)
  - [ ] Issue Type (single select, 7 values)
  - [ ] Domain (single select, 28 values)
  - [ ] Priority (single select, 4 values)
  - [ ] Complexity (single select, 5 values)
  - [ ] Sprint (iteration, 2-week, starts 2026-05-18)
  - [ ] Release (single select, 6 values)
  - [ ] Milestone (links to repo milestones)
  - [ ] Owner (assignee)
  - [ ] Team (single select, 5 values)
  - [ ] Start Date (date)
  - [ ] Target Date (date)
  - [ ] Blocked By (text)
  - [ ] Risk (single select, 4 values)
- [ ] All 9 project views created: `00 Triage`, `01 Roadmap`, `02 Product Backlog`, `03 Current Sprint`, `04 Engineering Board`, `05 Release MVP`, `06 Architecture and Platform`, `07 Risks and Blockers`, `08 Done`.
- [ ] Workflow automation rules configured per §9 (auto-add new issues, status transitions on PR open/merge, blocked-on-label).

## PL-002 — Labels, milestones, iterations

- [ ] All label groups from [§10](03-github-project-setup.md#L110-L225) created in the repo:
  - [ ] Type (7 labels)
  - [ ] Domain (28 labels)
  - [ ] Priority (4 labels)
  - [ ] Complexity (5 labels)
  - [ ] Status (5 labels — optional mirrors of the Status field)
  - [ ] Sprint (14 labels, optional if the Iteration field is used)
  - [ ] Release (6 labels)
  - [ ] Risk (6 labels)
  - [ ] Dependency (5 labels)
- [ ] All 10 milestones created per [§11](03-github-project-setup.md#L227-L242):
  - [ ] M0 - Planning Complete — due 2026-05-17
  - [ ] M1 - Platform Skeleton — due 2026-05-31
  - [ ] M2 - Identity and Tenancy — due 2026-06-14
  - [ ] M3 - Work Core — due 2026-07-12
  - [ ] M4 - Collaboration and Realtime — due 2026-08-09
  - [ ] M5 - Agile Planning — due 2026-09-06
  - [ ] M6 - Intelligence and Discovery — due 2026-10-04
  - [ ] M7 - Integrations and Automation — due 2026-11-01
  - [ ] M8 - Beta Hardening — due 2026-11-29
  - [ ] M9 - v1 Launch — due 2026-12-27
- [ ] Iteration field configured with 2-week cadence starting 2026-05-18.

## PL-003 — Issue and PR templates

- [ ] `.github/ISSUE_TEMPLATE/feature.yml` — covers epic, feature, and story shape, with the body standard from [04-issue-catalog.md §13](04-issue-catalog.md#L5-L36).
- [ ] `.github/ISSUE_TEMPLATE/task.yml` — technical task shape.
- [ ] `.github/ISSUE_TEMPLATE/bug.yml` — repro, expected/actual, severity, scope.
- [ ] `.github/ISSUE_TEMPLATE/spike.yml` — hypothesis, exit criteria, deliverable.
- [ ] `.github/ISSUE_TEMPLATE/config.yml` — disable blank issues; point contact link to docs.
- [ ] `.github/pull_request_template.md` — summary, linked issue, security/data/access checklist, test plan.

## PL-004 — ADR and architecture review process

- [x] `docs/adr/_template.md` exists.
- [x] `docs/adr/0001-modular-monolith.md` recorded.
- [ ] ADR PR review rule added to PR template (require ADR for cross-domain changes).
- [ ] First architecture review meeting scheduled (or async equivalent) for end of Sprint 1.

## Bulk Catalog Import (Day 4)

After PL-001..PL-004 are done, bulk-create the 75 catalog issues:

- [ ] Create 11 top-level epics (E00..E10) from [§12](03-github-project-setup.md#L244-L271) with `type:epic`.
- [ ] Create 75 child issues from [04-issue-catalog.md §13](04-issue-catalog.md#L222-L380) using the body standard.
- [ ] Link every child issue as a sub-issue of its parent epic via the GitHub sub-issues API.
- [ ] Assign each issue to its target Sprint iteration field.
- [ ] Tag each issue with the matching `domain:`, `type:`, `priority:`, `size:`, `release:` labels.
- [ ] Add each issue to the `qeetro roadmap` project.

## Sprint 0 Exit Criteria

- [ ] PL-001..PL-004 issues all marked Done in the project.
- [ ] Sample issue (e.g. PF-001) traverses Triage → Ready → In Progress → In Review → Done to validate automation.
- [ ] Sprint 1 iteration is populated with PF-001..PF-012 ready to start Monday.
- [ ] ADR-0001 merged and tagged.
- [ ] Maintainer can answer: "what is the first issue I open on Monday?" with a single GitHub link.
