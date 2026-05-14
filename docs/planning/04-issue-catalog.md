# 13. Parent/Child Issue Tree

This catalog is designed to be copied into GitHub Issues and attached to the GitHub Project named `qeetro roadmap`. Use GitHub sub-issues for hierarchy and the Project fields from [GitHub Project Setup](03-github-project-setup.md).

## Issue Body Standard

Every issue should use this structure:

```md
## Metadata
- Issue Type:
- Parent Issue:
- Domain:
- Priority:
- Complexity:
- Suggested Sprint:
- Dependencies:

## Content
- Description:
- Business Context:
- Problem Statement:
- Scope:
- Technical Notes:
- UX Notes:
- API Notes:
- Database Notes:
- Security Considerations:
- Performance Considerations:
- Edge Cases:

## Delivery
- Acceptance Criteria:
- Testing Requirements:
- Definition of Done:
```

The catalog below compresses those fields into implementation-ready entries. When creating GitHub issues, expand each row using the body standard above.

## Epic Tree

```text
E00 Planning, Program, and Delivery System
  -> F00.1 GitHub project operations
      -> PL-001 Create qeetro roadmap project
      -> PL-002 Create labels, milestones, iterations, and project views
      -> PL-003 Create issue and PR templates
      -> PL-004 Establish ADR and architecture review process

E01 Platform Foundation
  -> F01.1 Monorepo and tooling
      -> PF-001 Scaffold pnpm monorepo
      -> PF-002 Configure TypeScript build boundaries
      -> PF-003 Configure linting, formatting, and commit hygiene
  -> F01.2 App skeletons
      -> PF-004 Create Next.js web shell
      -> PF-005 Create NestJS API shell
      -> PF-006 Create shared UI, config, types, and event contract packages
  -> F01.3 Local infrastructure and CI
      -> PF-007 Add Docker Compose for Postgres and Redis
      -> PF-008 Add Prisma migration foundation
      -> PF-009 Add GitHub Actions CI
      -> PF-010 Add test harness and seed data strategy
      -> PF-011 Add environment and secrets validation
  -> F01.4 Observability foundation
      -> PF-012 Add request IDs, structured logs, health checks, and baseline metrics

E02 Identity, Tenancy, and Permissions
  -> F02.1 Identity and authentication
      -> ID-001 Design user and credential schema
      -> AUTH-001 Implement signup, login, logout, and password hashing
      -> AUTH-002 Implement JWT access and refresh token lifecycle
      -> AUTH-003 Implement session revocation and refresh rotation
      -> AUTH-004 Implement password reset and email verification flow
  -> F02.2 Organization tenancy
      -> ORG-001 Design organization and settings schema
      -> ORG-002 Implement organization create/read/update APIs
      -> MEM-001 Design membership and invitation schema
      -> MEM-002 Implement invitation acceptance and member management
  -> F02.3 Authorization
      -> PERM-001 Define RBAC policy model and role matrix
      -> PERM-002 Implement NestJS guards, decorators, and policy checks
      -> PERM-003 Add authorization test matrix
  -> F02.4 Auth UI
      -> UI-AUTH-001 Build auth screens and form validation
      -> UI-ORG-001 Build org switcher, member list, and invite UI

E03 Work Core
  -> F03.1 Workspace and team model
      -> TEAM-001 Design workspaces, teams, and team membership schema
      -> TEAM-002 Implement workspace and team APIs
  -> F03.2 Projects
      -> PROJ-001 Design project schema, project keys, owners, and health fields
      -> PROJ-002 Implement project CRUD and status update APIs
      -> UI-PROJ-001 Build project list, create flow, and project overview
  -> F03.3 Issues
      -> ISS-001 Design issue core schema, issue keys, statuses, priorities, and relations
      -> ISS-002 Implement issue CRUD APIs
      -> ISS-003 Implement issue workflow state transitions
      -> ISS-004 Implement assignee, labels, estimates, due dates, and relations
      -> ISS-005 Implement issue activity event model
      -> UI-ISS-001 Build issue list and issue detail page
  -> F03.4 Backlog, ranking, and boards
      -> BACKLOG-001 Design deterministic ranking algorithm
      -> BACKLOG-002 Implement backlog ordering APIs
      -> BOARD-001 Design board, column, filter, and saved view schema
      -> BOARD-002 Implement board query and move APIs
      -> UI-BACKLOG-001 Build backlog triage UI
      -> UI-BOARD-001 Build Kanban board with optimistic movement
  -> F03.5 Querying and filters
      -> FILTER-001 Implement saved filters, issue query DTOs, and pagination

E04 Collaboration, Activity, and Realtime
  -> F04.1 Comments and mentions
      -> CMT-001 Design comments, reactions, and mentions schema
      -> CMT-002 Implement comments API and mention extraction
      -> UI-CMT-001 Build comment composer, thread, reactions, and mentions UI
  -> F04.2 Event outbox and activity
      -> EVT-001 Implement transactional outbox pattern
      -> ACT-001 Implement activity feed projection
      -> UI-ACT-001 Build issue/project activity timeline
  -> F04.3 Realtime
      -> RT-001 Implement websocket gateway and auth handshake
      -> RT-002 Implement channel subscription authorization
      -> RT-003 Implement Redis fanout for realtime events
      -> UI-RT-001 Implement frontend realtime reconciliation and optimistic confirmation
  -> F04.4 Notifications and audit
      -> NOTIF-001 Design notification schema and inbox APIs
      -> NOTIF-002 Implement BullMQ notification delivery and dedupe
      -> UI-NOTIF-001 Build notification inbox
      -> AUD-001 Implement audit log baseline for security/admin events

E05 Agile Planning and Roadmaps
  -> F05.1 Epics
      -> EPIC-001 Design epic schema and issue rollups
      -> EPIC-002 Implement epic CRUD and progress APIs
      -> UI-EPIC-001 Build epic detail and progress UI
  -> F05.2 Sprints and cycles
      -> SPR-001 Design sprint/cycle schema, capacity, and scope history
      -> SPR-002 Implement sprint planning and lifecycle APIs
      -> UI-SPR-001 Build sprint planning UI
  -> F05.3 Roadmaps and releases
      -> ROAD-001 Design milestones, releases, and roadmap item schema
      -> ROAD-002 Implement roadmap query and dependency APIs
      -> UI-ROAD-001 Build roadmap timeline MVP
  -> F05.4 Agile analytics
      -> ANA-001 Design event-derived metrics model
      -> ANA-002 Implement burndown, throughput, cycle time, and project health APIs
      -> UI-ANA-001 Build analytics dashboard MVP

E06 Discovery and AI Assistance
  -> F06.1 Search and files
      -> SEARCH-001 Design search document projection and permission metadata
      -> SEARCH-002 Implement PostgreSQL full-text search APIs
      -> UI-SEARCH-001 Build global search and command palette search
      -> FILE-001 Implement file metadata and upload abstraction
  -> F06.2 AI foundation
      -> AI-001 Design AI run, policy, tool call, and cost logging schema
      -> AI-002 Implement permission-aware context builder
      -> AI-003 Implement issue drafting and refinement endpoint
      -> AI-004 Implement activity and project summarization jobs
      -> AI-005 Implement duplicate, blocker, and sprint risk suggestions
      -> UI-AI-001 Build AI assistant panel with preview/confirm workflow

E07 Integrations and Automation
  -> F07.1 GitHub integration
      -> GH-001 Design integration installation, external account, and sync cursor schema
      -> GH-002 Implement GitHub App/OAuth installation flow
      -> GH-003 Implement inbound webhook processing and idempotency
      -> GH-004 Implement PR/status sync to issues
  -> F07.2 Slack integration
      -> SLACK-001 Implement Slack OAuth and workspace mapping
      -> SLACK-002 Implement Slack notifications and action callbacks
  -> F07.3 Automation
      -> AUTO-001 Design automation rule, trigger, condition, action, and run history schema
      -> AUTO-002 Implement trigger/condition/action engine
      -> AUTO-003 Implement dry-run, audit trail, and kill switch
      -> UI-AUTO-001 Build automation rule list and run history UI
  -> F07.4 Queue reliability
      -> QUEUE-001 Add queue retry, backoff, dead-letter, and rate-limit policy

E08 Hardening, Observability, and Beta Readiness
  -> F08.1 Security and reliability
      -> SEC-001 Complete security threat model
      -> SEC-002 Implement rate limits, CORS, CSRF posture, and secure headers
      -> SEC-003 Add tenant isolation test suite
      -> DATA-001 Create backup, restore, retention, and archival plan
  -> F08.2 Performance and observability
      -> PERF-001 Define and test board/search/realtime performance budgets
      -> OBS-001 Add dashboards, alerts, and queue metrics
      -> OBS-002 Add frontend and backend error reporting
  -> F08.3 UX and QA hardening
      -> UX-001 Add onboarding, empty states, and error states
      -> QA-001 Complete accessibility and keyboard navigation pass
      -> REL-001 Complete beta release checklist

E09 Public API, Imports, and v1 Launch
  -> F09.1 Public API and webhooks
      -> API-001 Implement API tokens and rate limits
      -> API-002 Implement public REST API v1 for core work objects
      -> WEBHOOK-001 Implement outbound webhooks and delivery logs
  -> F09.2 Imports and migration
      -> IMP-001 Build CSV import framework
      -> IMP-002 Build GitHub Issues importer
      -> IMP-003 Build Jira/Linear basic importer
  -> F09.3 Launch readiness
      -> DOCS-001 Write user, admin, and developer docs
      -> REL-002 Complete v1 launch checklist

E10 v2 and Future Expansion
  -> F10.1 Enterprise scale
      -> ENT-001 Spike SAML/SCIM and enterprise identity
      -> ENT-002 Spike portfolio planning and capacity model
      -> ENT-003 Spike workflow versioning and custom field analytics
  -> F10.2 Platform expansion
      -> FUT-001 Spike marketplace/app framework
      -> FUT-002 Spike self-hosted edition packaging
      -> FUT-003 Spike service extraction candidates
      -> FUT-004 Spike Kubernetes migration readiness
```

## Detailed Issue Catalog

Legend: `AC/Test/DoD` means acceptance criteria, testing requirements, and definition of done. Every issue also inherits tenant isolation, structured logging, typed errors, and no unrelated refactor requirements.

### Phase 0 and Sprint 1: Planning and Platform Foundation

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| PL-001 | Type: Task; Parent: F00.1; Domain: DevOps; Priority: Critical; Size: XS; Sprint: 0; Depends: none | Title: Create `qeetro roadmap` GitHub Project. Context: project needs one delivery system before implementation. Scope: create project, add README/docs links, add initial views. Notes: no product code. AC/Test/DoD: project exists with fields, visible views, and planning docs linked. |
| PL-002 | Type: Task; Parent: F00.1; Domain: DevOps; Priority: Critical; Size: S; Sprint: 0; Depends: PL-001 | Title: Create labels, milestones, iterations, and release fields. Context: enables sprint planning and issue triage. Scope: apply taxonomy from section 10 and milestones from section 11. Edge: GitHub labels are flat, use prefixes. AC/Test/DoD: labels/milestones/iterations match docs and one sample issue validates workflow. |
| PL-003 | Type: Task; Parent: F00.1; Domain: DevOps; Priority: High; Size: S; Sprint: 0; Depends: PL-001 | Title: Create issue and PR templates. Context: future work must remain implementation-ready. Scope: issue template with metadata/content/delivery sections, bug template, spike template, PR checklist. Security: require auth/data/access notes where relevant. AC/Test/DoD: templates render in GitHub and support parent/child links. |
| PL-004 | Type: Task; Parent: F00.1; Domain: Infrastructure; Priority: Medium; Size: S; Sprint: 0; Depends: PL-001 | Title: Establish ADR and architecture review process. Context: modular monolith needs conscious boundary decisions. Scope: ADR template, review rubric, decision log location. Edge: avoid bureaucracy for small changes. AC/Test/DoD: first ADR records monorepo/modular-monolith decision. |
| PF-001 | Type: Task; Parent: F01.1; Domain: Infrastructure; Priority: Critical; Size: M; Sprint: 1; Depends: PL-004 | Title: Scaffold pnpm monorepo. Context: all apps/packages need predictable boundaries. Scope: `apps/web`, `apps/api`, `apps/worker`, `packages/*`, `infra`, `docs`. Technical: use pnpm workspaces. AC/Test/DoD: install succeeds, workspace scripts run, empty packages build. |
| PF-002 | Type: Task; Parent: F01.1; Domain: Infrastructure; Priority: Critical; Size: M; Sprint: 1; Depends: PF-001 | Title: Configure TypeScript build boundaries. Context: shared types reduce drift but can create circular dependencies. Scope: base tsconfig, package tsconfigs, path rules. Technical: no domain package imports from apps. AC/Test/DoD: typecheck detects invalid imports and all packages compile. |
| PF-003 | Type: Task; Parent: F01.1; Domain: DevOps; Priority: High; Size: S; Sprint: 1; Depends: PF-001 | Title: Configure linting, formatting, and commit hygiene. Context: early consistency lowers future review cost. Scope: ESLint, Prettier, import order, optional lint-staged. Edge: do not block prototypes on overly strict style. AC/Test/DoD: lint and format scripts pass on clean repo. |
| PF-004 | Type: Task; Parent: F01.2; Domain: Frontend; Priority: Critical; Size: M; Sprint: 1; Depends: PF-001, PF-002 | Title: Create Next.js web shell. Context: frontend needs routing, auth boundary, and app layout before features. Scope: App Router, Tailwind, shadcn/ui setup, route groups. UX: execution workspace first, no landing-page detour. AC/Test/DoD: app boots, layout renders, smoke test passes. |
| PF-005 | Type: Task; Parent: F01.2; Domain: Backend; Priority: Critical; Size: M; Sprint: 1; Depends: PF-001, PF-002 | Title: Create NestJS API shell. Context: backend modules need a consistent module pattern. Scope: bootstrap, config module, health endpoint, validation pipe, exception filter. API: version under `/api/v1`. AC/Test/DoD: health endpoint works and e2e smoke test passes. |
| PF-006 | Type: Task; Parent: F01.2; Domain: Infrastructure; Priority: High; Size: S; Sprint: 1; Depends: PF-001 | Title: Create shared UI, config, types, and event contract packages. Context: cross-app contracts need one home. Scope: `packages/ui`, `config`, `types`, `event-contracts`, `api-client`. Edge: no business logic in shared packages. AC/Test/DoD: imports work and dependency rules are documented. |
| PF-007 | Type: Task; Parent: F01.3; Domain: Infrastructure; Priority: Critical; Size: S; Sprint: 1; Depends: PF-005 | Title: Add Docker Compose for Postgres and Redis. Context: local dev must be reproducible. Scope: compose file, env examples, health checks. Security: no real secrets committed. AC/Test/DoD: services boot cleanly and API can connect locally. |
| PF-008 | Type: Task; Parent: F01.3; Domain: Database; Priority: Critical; Size: M; Sprint: 1; Depends: PF-005, PF-007 | Title: Add Prisma migration foundation. Context: database design is central to tenancy and work objects. Scope: Prisma client, migrations folder, seed conventions. DB: include base audit columns and ID convention. AC/Test/DoD: migration runs on empty DB and seed command works. |
| PF-009 | Type: Task; Parent: F01.3; Domain: DevOps; Priority: Critical; Size: M; Sprint: 1; Depends: PF-001, PF-003 | Title: Add GitHub Actions CI. Context: main branch must stay releasable. Scope: install/cache pnpm, typecheck, lint, unit tests, build. Performance: cache dependencies. AC/Test/DoD: CI passes on PR and fails on intentional type error. |
| PF-010 | Type: Task; Parent: F01.3; Domain: Testing; Priority: High; Size: M; Sprint: 1; Depends: PF-004, PF-005 | Title: Add test harness and seed data strategy. Context: later domains need cheap verification. Scope: API unit/e2e setup, frontend component smoke, seed fixtures. Edge: fixtures must be tenant-scoped. AC/Test/DoD: sample tests run in CI and local. |
| PF-011 | Type: Task; Parent: F01.3; Domain: Infrastructure; Priority: High; Size: S; Sprint: 1; Depends: PF-005 | Title: Add environment and secrets validation. Context: config mistakes cause runtime failures and leaks. Scope: schema-validated env vars, examples, runtime fail-fast. Security: never log secrets. AC/Test/DoD: missing required env fails boot with clear error. |
| PF-012 | Type: Task; Parent: F01.4; Domain: Observability; Priority: High; Size: M; Sprint: 1; Depends: PF-005 | Title: Add request IDs, structured logs, health checks, and baseline metrics. Context: production-grade work needs visibility from day one. Scope: request/correlation IDs, JSON logs, health/readiness, queue metric placeholder. AC/Test/DoD: logs include request/org/user placeholders without PII leakage. |

### Sprint 2: Identity, Tenancy, and Permissions

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| ID-001 | Type: Task; Parent: F02.1; Domain: Identity; Priority: Critical; Size: M; Sprint: 2; Depends: PF-008 | Title: Design user and credential schema. Context: separate global identity from tenant membership. Scope: User, UserProfile, AccountCredential, Session. DB: unique email normalization and audit fields. AC/Test/DoD: migration reviewed with indexes and lifecycle states. |
| AUTH-001 | Type: Story; Parent: F02.1; Domain: Auth; Priority: Critical; Size: M; Sprint: 2; Depends: ID-001 | Title: Implement signup, login, logout, and password hashing. Context: users need secure entry. Scope: endpoints, DTOs, password policy, bcrypt/argon2. Security: timing-safe failure behavior. AC/Test/DoD: happy path, invalid credentials, lockout/rate-limit hooks tested. |
| AUTH-002 | Type: Story; Parent: F02.1; Domain: Auth; Priority: Critical; Size: L; Sprint: 2; Depends: AUTH-001 | Title: Implement JWT access and refresh token lifecycle. Context: web/API sessions need predictable auth. Scope: short-lived access token, refresh rotation, cookie strategy, token claims. Edge: concurrent refresh. AC/Test/DoD: refresh reuse is detected and revoked. |
| AUTH-003 | Type: Task; Parent: F02.1; Domain: Auth; Priority: High; Size: M; Sprint: 2; Depends: AUTH-002, PF-007 | Title: Implement session revocation and refresh rotation storage. Context: users/admins need logout everywhere. Scope: session table, token family, Redis denylist where needed. Security: revoke compromised family. AC/Test/DoD: revoked sessions cannot refresh or access protected endpoints. |
| AUTH-004 | Type: Story; Parent: F02.1; Domain: Auth; Priority: Medium; Size: M; Sprint: 2; Depends: AUTH-001, PF-008 | Title: Implement password reset and email verification flow. Context: account lifecycle needs recovery. Scope: tokens, expiry, one-time use, email delivery adapter stub until notification queues exist. Edge: enumeration resistance. AC/Test/DoD: token expiry/reuse/invalid states tested. |
| ORG-001 | Type: Task; Parent: F02.2; Domain: Organizations; Priority: Critical; Size: M; Sprint: 2; Depends: ID-001, PF-008 | Title: Design organization and settings schema. Context: org is tenant root. Scope: Organization, OrganizationSettings, slug, owner, plan placeholder. DB: unique `(slug)`, future billing fields. AC/Test/DoD: migration enforces tenant root constraints. |
| ORG-002 | Type: Story; Parent: F02.2; Domain: Organizations; Priority: Critical; Size: M; Sprint: 2; Depends: ORG-001, AUTH-002 | Title: Implement organization create/read/update APIs. Context: all product work lives inside an org. Scope: create org after signup, update settings, list orgs for user. API: tenant-aware routes. AC/Test/DoD: user cannot read/update unrelated orgs. |
| MEM-001 | Type: Task; Parent: F02.2; Domain: Organizations; Priority: Critical; Size: M; Sprint: 2; Depends: ORG-001, ID-001 | Title: Design membership and invitation schema. Context: collaboration starts with membership. Scope: Membership, Invitation, RoleAssignment. DB: unique active membership per org/user. AC/Test/DoD: migration covers invite expiry, accepted/revoked states. |
| MEM-002 | Type: Story; Parent: F02.2; Domain: Organizations; Priority: Critical; Size: L; Sprint: 2; Depends: MEM-001, ORG-002 | Title: Implement invitation acceptance and member management. Context: teams need secure onboarding. Scope: invite, accept, revoke, change role, remove member. Security: inviter must have permission. AC/Test/DoD: expired/revoked/duplicate invites tested. |
| PERM-001 | Type: Task; Parent: F02.3; Domain: Permissions; Priority: Critical; Size: L; Sprint: 2; Depends: MEM-001 | Title: Define RBAC policy model and role matrix. Context: authorization cannot be scattered. Scope: org owner/admin/member/viewer, project roles, policy decisions. Edge: future ABAC. AC/Test/DoD: matrix documents every protected action. |
| PERM-002 | Type: Task; Parent: F02.3; Domain: Permissions; Priority: Critical; Size: L; Sprint: 2; Depends: PERM-001, AUTH-002 | Title: Implement NestJS guards, decorators, and policy checks. Context: endpoints need consistent authorization. Scope: current user context, org scope, resource policy guard. Performance: avoid expensive joins per check. AC/Test/DoD: protected endpoint tests cover allow/deny. |
| PERM-003 | Type: Task; Parent: F02.3; Domain: Permissions; Priority: High; Size: M; Sprint: 2; Depends: PERM-002 | Title: Add authorization test matrix. Context: auth regressions are high-risk. Scope: table-driven tests for roles/resources. Security: include cross-tenant denial. AC/Test/DoD: CI fails on missing coverage for new protected route category. |
| UI-AUTH-001 | Type: Story; Parent: F02.4; Domain: Frontend; Priority: High; Size: M; Sprint: 2; Depends: AUTH-001, AUTH-002, PF-004 | Title: Build auth screens and form validation. Context: first user journey must be smooth. Scope: login, signup, logout, validation, error states. UX: fast, minimal, accessible forms. AC/Test/DoD: keyboard/a11y smoke and API error handling verified. |
| UI-ORG-001 | Type: Story; Parent: F02.4; Domain: Frontend; Priority: High; Size: M; Sprint: 2; Depends: ORG-002, MEM-002 | Title: Build org switcher, member list, and invite UI. Context: multi-tenant navigation needs clarity. Scope: org selector, invite modal, member table, role changes. Edge: user with no org. AC/Test/DoD: user can create org, invite member, switch org without stale data. |

### Sprints 3-4: Work Core, Backlog, and Boards

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| TEAM-001 | Type: Task; Parent: F03.1; Domain: Teams; Priority: High; Size: M; Sprint: 3; Depends: ORG-001, MEM-001 | Title: Design workspaces, teams, and team membership schema. Context: organizations need structure beyond one project. Scope: Workspace, Team, TeamMember, TeamWorkflow. DB: tenant-scoped slugs. AC/Test/DoD: migration supports one default workspace/team. |
| TEAM-002 | Type: Story; Parent: F03.1; Domain: Teams; Priority: High; Size: M; Sprint: 3; Depends: TEAM-001, PERM-002 | Title: Implement workspace and team APIs. Context: projects/issues attach to teams. Scope: CRUD, membership assignment, default team. API: pagination and permissions. AC/Test/DoD: role-limited CRUD tests pass. |
| PROJ-001 | Type: Task; Parent: F03.2; Domain: Projects; Priority: Critical; Size: M; Sprint: 3; Depends: TEAM-001 | Title: Design project schema, project keys, owners, and health fields. Context: projects are outcome containers. Scope: Project, ProjectMember, status, health, target dates. DB: unique project key per org. AC/Test/DoD: schema supports archived and active states. |
| PROJ-002 | Type: Story; Parent: F03.2; Domain: Projects; Priority: Critical; Size: L; Sprint: 3; Depends: PROJ-001, PERM-002 | Title: Implement project CRUD and status update APIs. Context: users need to create and manage work containers. Scope: create, update, archive, status update. API: permission-filtered list. AC/Test/DoD: project member and org role behavior tested. |
| UI-PROJ-001 | Type: Story; Parent: F03.2; Domain: Frontend; Priority: High; Size: M; Sprint: 3; Depends: PROJ-002 | Title: Build project list, create flow, and project overview. Context: first product workspace starts here. Scope: list, empty state, create form, overview cards. UX: dense, utilitarian, no marketing hero. AC/Test/DoD: create project and navigate to overview works. |
| ISS-001 | Type: Task; Parent: F03.3; Domain: Issues; Priority: Critical; Size: XL; Sprint: 3; Depends: PROJ-001, TEAM-001 | Title: Design issue core schema, issue keys, statuses, priorities, and relations. Context: issues are the hot path. Scope: Issue, IssueStatus, IssueRelation, IssueLabel, IssueFieldValue. DB: tenant/project keys, indexes for lists. AC/Test/DoD: schema handles sub-issues, duplicates, blockers, archived issues. |
| ISS-002 | Type: Story; Parent: F03.3; Domain: Issues; Priority: Critical; Size: L; Sprint: 3; Depends: ISS-001, PERM-002 | Title: Implement issue CRUD APIs. Context: teams need create/read/update/delete/archive work. Scope: create, update, list, detail, archive. API: cursor pagination, filters by project/team/status/assignee. AC/Test/DoD: tenant isolation, validation, pagination tests pass. |
| ISS-003 | Type: Story; Parent: F03.3; Domain: Issues; Priority: Critical; Size: M; Sprint: 3; Depends: ISS-002 | Title: Implement issue workflow state transitions. Context: state changes drive boards, analytics, and notifications. Scope: allowed transitions, status config, transition events. Edge: invalid or stale transition. AC/Test/DoD: transition rules and event emission tested. |
| ISS-004 | Type: Story; Parent: F03.3; Domain: Issues; Priority: High; Size: M; Sprint: 3; Depends: ISS-002 | Title: Implement assignee, labels, estimates, due dates, and relations. Context: issue planning needs basic metadata. Scope: update fields, relation CRUD, label attach/detach. DB: indexed label/status/assignee combos. AC/Test/DoD: relation cycles and cross-project relation rules tested. |
| ISS-005 | Type: Task; Parent: F03.3; Domain: Activity; Priority: High; Size: M; Sprint: 3; Depends: ISS-002 | Title: Implement issue activity event model. Context: every meaningful change needs history. Scope: domain event payloads for create/update/status/assignment/relation. Technical: versioned event contracts. AC/Test/DoD: events include actor, org, resource, before/after where safe. |
| UI-ISS-001 | Type: Story; Parent: F03.3; Domain: Frontend; Priority: Critical; Size: L; Sprint: 3; Depends: ISS-002, ISS-003, ISS-004 | Title: Build issue list and issue detail page. Context: daily execution requires fast issue access. Scope: list, detail drawer/page, edit fields, status changes. UX: keyboard-friendly, optimistic safe fields. AC/Test/DoD: create/edit/status flow works with validation and loading states. |
| BACKLOG-001 | Type: Task; Parent: F03.4; Domain: Backlog; Priority: Critical; Size: L; Sprint: 4; Depends: ISS-001 | Title: Design deterministic ranking algorithm. Context: backlog/board ordering is concurrency-sensitive. Scope: rank value strategy, move semantics, rebalance policy. Edge: concurrent moves, huge lists. AC/Test/DoD: algorithm documented with collision and rebalance tests. |
| BACKLOG-002 | Type: Story; Parent: F03.4; Domain: Backlog; Priority: Critical; Size: L; Sprint: 4; Depends: BACKLOG-001, ISS-002 | Title: Implement backlog ordering APIs. Context: teams need stable prioritization. Scope: ordered list query, move before/after, bulk reorder. API: idempotency key for moves. AC/Test/DoD: concurrent reorder and pagination tests pass. |
| BOARD-001 | Type: Task; Parent: F03.4; Domain: Boards; Priority: High; Size: L; Sprint: 4; Depends: ISS-003, BACKLOG-001 | Title: Design board, column, filter, and saved view schema. Context: boards are views over issues. Scope: Board, BoardColumn, BoardView, filter definitions. DB: no duplication of issue source of truth. AC/Test/DoD: default Kanban board can be generated per project/team. |
| BOARD-002 | Type: Story; Parent: F03.4; Domain: Boards; Priority: High; Size: L; Sprint: 4; Depends: BOARD-001, BACKLOG-002 | Title: Implement board query and move APIs. Context: visual workflow needs fast moves. Scope: columns, grouped query, move issue to status/rank. Performance: p95 query target under 250ms for normal board. AC/Test/DoD: move emits issue status and rank events. |
| UI-BACKLOG-001 | Type: Story; Parent: F03.4; Domain: Frontend; Priority: High; Size: M; Sprint: 4; Depends: BACKLOG-002 | Title: Build backlog triage UI. Context: grooming must be fast. Scope: backlog list, drag reorder, quick filters, create issue. Edge: empty and huge backlog. AC/Test/DoD: optimistic reorder reconciles server rank and handles failure. |
| UI-BOARD-001 | Type: Story; Parent: F03.4; Domain: Frontend; Priority: High; Size: XL; Sprint: 4; Depends: BOARD-002 | Title: Build Kanban board with optimistic movement. Context: board is core perceived-speed surface. Scope: columns, cards, drag/drop, status/rank updates. UX: stable dimensions, no layout shift. AC/Test/DoD: move across columns updates immediately and rolls back on API failure. |
| FILTER-001 | Type: Story; Parent: F03.5; Domain: Issues; Priority: Medium; Size: M; Sprint: 4; Depends: ISS-002, BOARD-001 | Title: Implement saved filters, issue query DTOs, and pagination. Context: lists/boards need reusable views. Scope: filter parser, saved view CRUD, cursor pagination. Security: filters cannot leak other tenants. AC/Test/DoD: query edge cases and invalid filters tested. |

### Sprint 5: Collaboration, Activity, Realtime, Notifications

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| CMT-001 | Type: Task; Parent: F04.1; Domain: Comments; Priority: High; Size: M; Sprint: 5; Depends: ISS-002, ID-001 | Title: Design comments, reactions, and mentions schema. Context: collaboration belongs close to work. Scope: Comment, Reaction, Mention. DB: polymorphic target with controlled resource types. AC/Test/DoD: schema supports issue comments first and project comments later. |
| CMT-002 | Type: Story; Parent: F04.1; Domain: Comments; Priority: High; Size: M; Sprint: 5; Depends: CMT-001, PERM-002 | Title: Implement comments API and mention extraction. Context: users need discussion and directed attention. Scope: create/update/delete/list, markdown, mentions. Security: sanitize/escape rendered content. AC/Test/DoD: mention parsing and unauthorized target access tested. |
| UI-CMT-001 | Type: Story; Parent: F04.1; Domain: Frontend; Priority: Medium; Size: M; Sprint: 5; Depends: CMT-002 | Title: Build comment composer, thread, reactions, and mentions UI. Context: issue detail should support collaboration. Scope: composer, edit/delete, reactions, mention suggestions. UX: keyboard submit and accessible editor. AC/Test/DoD: comment lifecycle works with optimistic add. |
| EVT-001 | Type: Task; Parent: F04.2; Domain: Backend; Priority: Critical; Size: L; Sprint: 5; Depends: PF-008, ISS-005 | Title: Implement transactional outbox pattern. Context: side effects must be reliable. Scope: outbox table, dispatcher, event status, retry. Performance: batch dispatch. AC/Test/DoD: DB mutation and outbox write are atomic; retries are idempotent. |
| ACT-001 | Type: Story; Parent: F04.2; Domain: Activity; Priority: High; Size: M; Sprint: 5; Depends: EVT-001, ISS-005, CMT-002 | Title: Implement activity feed projection. Context: users need work history and later analytics. Scope: consume events into ActivityEvent. DB: append-only, tenant-scoped indexes. AC/Test/DoD: issue/project activity queries return ordered events. |
| UI-ACT-001 | Type: Story; Parent: F04.2; Domain: Frontend; Priority: Medium; Size: S; Sprint: 5; Depends: ACT-001 | Title: Build issue/project activity timeline. Context: changes should be explainable. Scope: render activity entries with actor/time/resource. UX: concise event copy. AC/Test/DoD: timeline displays create/update/comment/status events. |
| RT-001 | Type: Task; Parent: F04.3; Domain: Realtime; Priority: High; Size: L; Sprint: 5; Depends: AUTH-002, PF-007 | Title: Implement websocket gateway and auth handshake. Context: realtime is core to collaboration and speed perception. Scope: socket auth, disconnect, user context, presence placeholder. Security: reject invalid/expired sessions. AC/Test/DoD: authenticated socket connects and unauthenticated socket fails. |
| RT-002 | Type: Task; Parent: F04.3; Domain: Realtime; Priority: Critical; Size: L; Sprint: 5; Depends: RT-001, PERM-002 | Title: Implement channel subscription authorization. Context: realtime can leak data if raw events are broadcast. Scope: org/project/issue/user channels and policy checks. Edge: permission changes mid-connection. AC/Test/DoD: cross-tenant subscription attempts denied. |
| RT-003 | Type: Story; Parent: F04.3; Domain: Realtime; Priority: High; Size: M; Sprint: 5; Depends: RT-002, EVT-001 | Title: Implement Redis fanout for realtime events. Context: API instances will need horizontal fanout. Scope: Redis adapter, event mapping, presentation event shape. Performance: do not broadcast raw domain event to all clients. AC/Test/DoD: two API instances receive and filter events correctly. |
| UI-RT-001 | Type: Story; Parent: F04.3; Domain: Frontend; Priority: High; Size: M; Sprint: 5; Depends: RT-003, UI-BOARD-001 | Title: Implement frontend realtime reconciliation and optimistic confirmation. Context: clients must resolve optimistic moves/comments with server truth. Scope: socket client, query invalidation, patch reconciliation. Edge: duplicate and out-of-order events. AC/Test/DoD: repeated events do not duplicate UI state. |
| NOTIF-001 | Type: Task; Parent: F04.4; Domain: Notifications; Priority: Medium; Size: L; Sprint: 5; Depends: CMT-002, ACT-001 | Title: Design notification schema and inbox APIs. Context: users need signal without noise. Scope: Notification, NotificationDelivery, preferences placeholder. DB: dedupe keys and unread indexes. AC/Test/DoD: mention notification appears once and can be marked read. |
| NOTIF-002 | Type: Task; Parent: F04.4; Domain: Notifications; Priority: Medium; Size: M; Sprint: 5; Depends: NOTIF-001, PF-007 | Title: Implement BullMQ notification delivery and dedupe. Context: email/digest/slack later require async delivery. Scope: queue processor, dedupe, retry, dead-letter. Edge: duplicate event replay. AC/Test/DoD: duplicate jobs do not create duplicate notification rows. |
| UI-NOTIF-001 | Type: Story; Parent: F04.4; Domain: Frontend; Priority: Medium; Size: S; Sprint: 5; Depends: NOTIF-001 | Title: Build notification inbox. Context: attention should be centralized. Scope: unread count, list, mark read, link target. UX: low-noise inbox. AC/Test/DoD: mention opens target issue and clears unread state. |
| AUD-001 | Type: Task; Parent: F04.4; Domain: Audit; Priority: High; Size: M; Sprint: 5; Depends: EVT-001, PERM-002 | Title: Implement audit log baseline for security/admin events. Context: enterprise readiness begins with auditability. Scope: auth, membership, role, integration, settings events. Security: immutable append-only writes. AC/Test/DoD: admin role changes are queryable with actor/time/IP metadata. |

### Sprints 6-7: Agile Planning, Search, Analytics, and AI Assistance

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| EPIC-001 | Type: Task; Parent: F05.1; Domain: Epics; Priority: High; Size: M; Sprint: 6; Depends: ISS-001 | Title: Design epic schema and issue rollups. Context: larger work needs hierarchy beyond sub-issues. Scope: Epic, EpicIssue, status, progress fields. Edge: issue in one epic initially. AC/Test/DoD: schema supports cross-project rollups in same org. |
| EPIC-002 | Type: Story; Parent: F05.1; Domain: Epics; Priority: High; Size: M; Sprint: 6; Depends: EPIC-001, ISS-002 | Title: Implement epic CRUD and progress APIs. Context: teams need track outcome progress. Scope: create/update/archive, attach issues, rollup counts. Performance: cache or projection if rollup grows. AC/Test/DoD: rollup updates after issue status change. |
| UI-EPIC-001 | Type: Story; Parent: F05.1; Domain: Frontend; Priority: Medium; Size: M; Sprint: 6; Depends: EPIC-002 | Title: Build epic detail and progress UI. Context: planning surface needs visibility. Scope: epic header, issue list, progress, status. UX: scan-friendly progress, no decorative cards. AC/Test/DoD: user can attach/detach issues and see progress. |
| SPR-001 | Type: Task; Parent: F05.2; Domain: Sprints; Priority: High; Size: L; Sprint: 6; Depends: TEAM-001, ISS-001 | Title: Design sprint/cycle schema, capacity, and scope history. Context: agile analytics need committed vs added work. Scope: Sprint, SprintIssue, CapacitySnapshot, SprintScopeEvent. DB: preserve scope changes. AC/Test/DoD: schema can calculate committed, added, removed, completed. |
| SPR-002 | Type: Story; Parent: F05.2; Domain: Sprints; Priority: High; Size: L; Sprint: 6; Depends: SPR-001, BACKLOG-002 | Title: Implement sprint planning and lifecycle APIs. Context: teams need plan/start/complete cycles. Scope: create sprint, add/remove issues, start, complete, carryover. Edge: issue in only one active sprint per team. AC/Test/DoD: lifecycle and scope history tests pass. |
| UI-SPR-001 | Type: Story; Parent: F05.2; Domain: Frontend; Priority: Medium; Size: L; Sprint: 6; Depends: SPR-002, UI-BACKLOG-001 | Title: Build sprint planning UI. Context: teams need move backlog into sprint. Scope: planning view, capacity summary, start/complete actions. UX: bulk selection and drag between backlog/sprint. AC/Test/DoD: user can plan and start a sprint. |
| ROAD-001 | Type: Task; Parent: F05.3; Domain: Roadmaps; Priority: Medium; Size: M; Sprint: 6; Depends: PROJ-001, EPIC-001 | Title: Design milestones, releases, and roadmap item schema. Context: roadmap should connect project intent to delivery. Scope: Milestone, Release, RoadmapItem, dependencies. Edge: avoid heavy Gantt in MVP. AC/Test/DoD: schema supports project/epic/release timeline. |
| ROAD-002 | Type: Story; Parent: F05.3; Domain: Roadmaps; Priority: Medium; Size: M; Sprint: 6; Depends: ROAD-001 | Title: Implement roadmap query and dependency APIs. Context: leadership needs timeline visibility. Scope: list items by date, dependency CRUD, release status. Performance: date-range pagination. AC/Test/DoD: dependency cycles are rejected. |
| UI-ROAD-001 | Type: Story; Parent: F05.3; Domain: Frontend; Priority: Medium; Size: M; Sprint: 6; Depends: ROAD-002 | Title: Build roadmap timeline MVP. Context: v1 needs lightweight planning visibility. Scope: timeline list, milestone markers, dependency indicators. UX: responsive table/timeline hybrid. AC/Test/DoD: roadmap renders on desktop/mobile without overlap. |
| ANA-001 | Type: Task; Parent: F05.4; Domain: Analytics; Priority: Medium; Size: L; Sprint: 7; Depends: ACT-001, SPR-001 | Title: Design event-derived metrics model. Context: reports should derive from history, not manual fields. Scope: MetricSnapshot, report queries, event consumers. DB: projection tables and backfill path. AC/Test/DoD: model calculates cycle time from issue events. |
| ANA-002 | Type: Story; Parent: F05.4; Domain: Analytics; Priority: Medium; Size: L; Sprint: 7; Depends: ANA-001, SPR-002 | Title: Implement burndown, throughput, cycle time, and project health APIs. Context: teams need delivery insight. Scope: report endpoints, filters, date ranges. Performance: no expensive live scans on hot issue tables. AC/Test/DoD: fixtures produce known metric outputs. |
| UI-ANA-001 | Type: Story; Parent: F05.4; Domain: Frontend; Priority: Medium; Size: M; Sprint: 7; Depends: ANA-002 | Title: Build analytics dashboard MVP. Context: health should be visible without manual reporting. Scope: cycle time, throughput, burndown, project health cards/charts. UX: compact operational dashboard. AC/Test/DoD: dashboard handles empty and partial data. |
| SEARCH-001 | Type: Task; Parent: F06.1; Domain: Search; Priority: High; Size: L; Sprint: 7; Depends: EVT-001, ISS-002, CMT-002 | Title: Design search document projection and permission metadata. Context: search must respect tenancy and permissions. Scope: SearchDocument projection, weights, resource refs. Security: permission metadata cannot be stale for restricted objects. AC/Test/DoD: projection spec covers issue/project/comment docs. |
| SEARCH-002 | Type: Story; Parent: F06.1; Domain: Search; Priority: High; Size: L; Sprint: 7; Depends: SEARCH-001 | Title: Implement PostgreSQL full-text search APIs. Context: avoid external search until needed. Scope: FTS/trigram indexes, query endpoint, filters. Performance: p95 target under 300ms for seeded beta data. AC/Test/DoD: relevance, typo-ish, tenant isolation, pagination tests. |
| UI-SEARCH-001 | Type: Story; Parent: F06.1; Domain: Frontend; Priority: Medium; Size: M; Sprint: 7; Depends: SEARCH-002 | Title: Build global search and command palette search. Context: fast navigation is a differentiator. Scope: command palette, search results, keyboard shortcuts. UX: no explanatory in-app text beyond necessary labels. AC/Test/DoD: keyboard flow opens results and navigates correctly. |
| FILE-001 | Type: Task; Parent: F06.1; Domain: Files; Priority: Medium; Size: M; Sprint: 7; Depends: PERM-002, PF-008 | Title: Implement file metadata and upload abstraction. Context: comments/issues need attachments eventually. Scope: FileAsset, UploadSession, local/S3 adapter interface. Security: signed URL design, size limits. AC/Test/DoD: metadata lifecycle tested with local adapter. |
| AI-001 | Type: Task; Parent: F06.2; Domain: AI; Priority: High; Size: L; Sprint: 7; Depends: PERM-002, ACT-001 | Title: Design AI run, policy, tool call, and cost logging schema. Context: AI must be auditable and controllable. Scope: AiRun, AiToolCall, AiPolicy, approval state, cost fields. Security: log references, not unnecessary raw secrets. AC/Test/DoD: schema supports replay/debug without leaking private prompts broadly. |
| AI-002 | Type: Task; Parent: F06.2; Domain: AI; Priority: High; Size: L; Sprint: 7; Depends: AI-001, SEARCH-002 | Title: Implement permission-aware context builder. Context: AI value depends on correct scoped context. Scope: retrieve issues/comments/projects/activity with policy checks. Performance: token/latency budgets. AC/Test/DoD: user cannot retrieve AI context for inaccessible resource. |
| AI-003 | Type: Story; Parent: F06.2; Domain: AI; Priority: Medium; Size: M; Sprint: 7; Depends: AI-002 | Title: Implement issue drafting and refinement endpoint. Context: reduce backlog grooming friction. Scope: title, description, acceptance criteria, task split suggestions. UX/API: returns draft only, no auto-create. AC/Test/DoD: generated draft cites input references and requires user confirmation. |
| AI-004 | Type: Story; Parent: F06.2; Domain: AI; Priority: Medium; Size: M; Sprint: 7; Depends: AI-002, ACT-001 | Title: Implement activity and project summarization jobs. Context: status updates are high-value AI use. Scope: summarize issue/project activity, queue job, cache result. Edge: stale summary invalidation. AC/Test/DoD: summary uses only authorized events and logs AI run. |
| AI-005 | Type: Story; Parent: F06.2; Domain: AI; Priority: Medium; Size: M; Sprint: 7; Depends: AI-002, ANA-002 | Title: Implement duplicate, blocker, and sprint risk suggestions. Context: AI should help execution judgment. Scope: candidate related issues, blockers, sprint scope risk. Security: suggestions are non-destructive. AC/Test/DoD: suggestions include confidence and sources; false positives dismissible. |
| UI-AI-001 | Type: Story; Parent: F06.2; Domain: Frontend; Priority: Medium; Size: M; Sprint: 7; Depends: AI-003, AI-004 | Title: Build AI assistant panel with preview/confirm workflow. Context: AI actions need human control. Scope: assistant panel, draft preview, apply buttons, run history link. UX: clear confirm for any write action. AC/Test/DoD: draft creation/edit/apply flow works without hidden writes. |

### Sprints 8-10: Integrations, Automation, Hardening, and v1

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| GH-001 | Type: Task; Parent: F07.1; Domain: Integrations; Priority: High; Size: M; Sprint: 8; Depends: AUD-001, EVT-001 | Title: Design integration installation, external account, and sync cursor schema. Context: integrations need idempotent external state. Scope: IntegrationInstallation, ExternalAccount, SyncCursor. Security: encrypted tokens. AC/Test/DoD: schema supports GitHub first and generic providers later. |
| GH-002 | Type: Story; Parent: F07.1; Domain: Integrations; Priority: High; Size: L; Sprint: 8; Depends: GH-001, AUTH-002 | Title: Implement GitHub App/OAuth installation flow. Context: qeetro should be developer-friendly. Scope: install callback, token storage, repo selection. Edge: revoked installation. AC/Test/DoD: install/uninstall flow updates state and audit log. |
| GH-003 | Type: Story; Parent: F07.1; Domain: Integrations; Priority: High; Size: L; Sprint: 8; Depends: GH-002, QUEUE-001 | Title: Implement inbound webhook processing and idempotency. Context: external events are noisy/retried. Scope: signature verification, event persistence, idempotency keys, queue handoff. Security: reject bad signatures. AC/Test/DoD: duplicate delivery produces one effect. |
| GH-004 | Type: Story; Parent: F07.1; Domain: Integrations; Priority: Medium; Size: L; Sprint: 8; Depends: GH-003, ISS-004 | Title: Implement PR/status sync to issues. Context: code progress should update work context. Scope: link PRs by issue key, update dev status, activity events. Edge: renamed branches, closed PRs. AC/Test/DoD: PR open/merge/close events appear on issue timeline. |
| SLACK-001 | Type: Story; Parent: F07.2; Domain: Integrations; Priority: Medium; Size: M; Sprint: 8; Depends: GH-001, NOTIF-002 | Title: Implement Slack OAuth and workspace mapping. Context: notifications and issue creation should meet teams in Slack. Scope: OAuth install, channel mapping, token storage. Security: scopes minimal. AC/Test/DoD: install/uninstall and token revoke paths tested. |
| SLACK-002 | Type: Story; Parent: F07.2; Domain: Integrations; Priority: Medium; Size: M; Sprint: 8; Depends: SLACK-001, NOTIF-002 | Title: Implement Slack notifications and action callbacks. Context: mentions/blockers need timely signals. Scope: send mention notifications, button callback to open issue. Edge: missing channel/user mapping. AC/Test/DoD: notification delivery logs success/failure. |
| AUTO-001 | Type: Task; Parent: F07.3; Domain: Automation; Priority: Medium; Size: L; Sprint: 8; Depends: EVT-001, PERM-002 | Title: Design automation rule, trigger, condition, action, and run history schema. Context: automation must be governed, not invisible magic. Scope: AutomationRule, AutomationRun, trigger/action typed config. Security: owner and permission model. AC/Test/DoD: schema supports issue status changed -> notify/update label. |
| AUTO-002 | Type: Story; Parent: F07.3; Domain: Automation; Priority: Medium; Size: XL; Sprint: 8; Depends: AUTO-001, QUEUE-001 | Title: Implement trigger/condition/action engine. Context: reduce repetitive work safely. Scope: event triggers, condition evaluator, action executor. Performance: rate limits and loop prevention. AC/Test/DoD: sample rules execute exactly once with idempotent action. |
| AUTO-003 | Type: Story; Parent: F07.3; Domain: Automation; Priority: Medium; Size: L; Sprint: 8; Depends: AUTO-002, AUD-001 | Title: Implement dry-run, audit trail, and kill switch. Context: admins need trust and recovery. Scope: preview matching events, run logs, disable all/rule-specific. Edge: malformed rule. AC/Test/DoD: dry-run shows planned action and disabled rule never executes. |
| UI-AUTO-001 | Type: Story; Parent: F07.3; Domain: Frontend; Priority: Low; Size: M; Sprint: 8; Depends: AUTO-003 | Title: Build automation rule list and run history UI. Context: automation needs visibility. Scope: list rules, enable/disable, run history, failure reason. UX: no complex builder until later. AC/Test/DoD: admin can inspect and disable failing automation. |
| QUEUE-001 | Type: Task; Parent: F07.4; Domain: Infrastructure; Priority: High; Size: M; Sprint: 8; Depends: PF-007, PF-012 | Title: Add queue retry, backoff, dead-letter, and rate-limit policy. Context: integrations/AI/notifications need reliability. Scope: BullMQ defaults, DLQ, dashboards/metrics hooks. Edge: poison jobs. AC/Test/DoD: retry and dead-letter behavior verified by tests. |
| SEC-001 | Type: Spike; Parent: F08.1; Domain: Security; Priority: Critical; Size: M; Sprint: 9; Depends: E02, E03, E04 | Title: Complete security threat model. Context: beta should not ship unknown auth/tenant risks. Scope: auth, tenancy, realtime, files, integrations, AI. Delivery: documented risks and follow-up issues. AC/Test/DoD: high/critical findings have owners and mitigation plan. |
| SEC-002 | Type: Task; Parent: F08.1; Domain: Security; Priority: Critical; Size: M; Sprint: 9; Depends: SEC-001 | Title: Implement rate limits, CORS, CSRF posture, and secure headers. Context: SaaS surface needs baseline hardening. Scope: request throttling, headers, cookie security, CORS allowlist. AC/Test/DoD: automated security config tests pass. |
| SEC-003 | Type: Task; Parent: F08.1; Domain: Security; Priority: Critical; Size: L; Sprint: 9; Depends: PERM-003, SEARCH-002, RT-002 | Title: Add tenant isolation test suite. Context: multi-tenancy bugs are existential. Scope: API, search, realtime, files, analytics. AC/Test/DoD: cross-tenant access attempts fail for every shared resource category. |
| DATA-001 | Type: Task; Parent: F08.1; Domain: Database; Priority: High; Size: M; Sprint: 9; Depends: PF-008 | Title: Create backup, restore, retention, and archival plan. Context: data-loss recovery is required before beta. Scope: backup schedule, restore runbook, retention for activity/events/logs. AC/Test/DoD: restore drill succeeds in staging-like environment. |
| PERF-001 | Type: Task; Parent: F08.2; Domain: Performance; Priority: High; Size: L; Sprint: 9; Depends: BOARD-002, SEARCH-002, RT-003 | Title: Define and test board/search/realtime performance budgets. Context: speed is a product principle. Scope: seed dataset, load tests, p95 budgets, profiling. AC/Test/DoD: regressions produce measurable follow-up issues. |
| OBS-001 | Type: Task; Parent: F08.2; Domain: Observability; Priority: High; Size: M; Sprint: 9; Depends: PF-012, QUEUE-001 | Title: Add dashboards, alerts, and queue metrics. Context: failures must be visible before users report them. Scope: latency, errors, queue depth, websocket fanout, DB slow queries. AC/Test/DoD: dashboard shows health and sample alert fires. |
| OBS-002 | Type: Task; Parent: F08.2; Domain: Observability; Priority: Medium; Size: M; Sprint: 9; Depends: PF-004, PF-005 | Title: Add frontend and backend error reporting. Context: beta feedback needs actionable traces. Scope: Sentry or equivalent, release tags, source maps, PII scrubbing. AC/Test/DoD: test error appears with correlation ID. |
| UX-001 | Type: Story; Parent: F08.3; Domain: Frontend; Priority: High; Size: M; Sprint: 9; Depends: MVP UI flows | Title: Add onboarding, empty states, and error states. Context: first-run experience determines adoption. Scope: first org/project/issue guidance, empty views, API error states. UX: no feature tutorial walls. AC/Test/DoD: new user reaches first issue in under 10 minutes. |
| QA-001 | Type: Task; Parent: F08.3; Domain: Frontend; Priority: High; Size: M; Sprint: 9; Depends: MVP UI flows | Title: Complete accessibility and keyboard navigation pass. Context: daily tools need ergonomic access. Scope: focus states, ARIA basics, keyboard board/list actions, contrast. AC/Test/DoD: automated a11y checks pass and critical keyboard paths work. |
| REL-001 | Type: Task; Parent: F08.3; Domain: DevOps; Priority: Critical; Size: M; Sprint: 9; Depends: SEC-001, PERF-001, OBS-001 | Title: Complete beta release checklist. Context: beta should be intentionally shippable. Scope: release criteria, known issues, rollback plan, seed demo org. AC/Test/DoD: all critical beta blockers closed or accepted with owner. |
| API-001 | Type: Task; Parent: F09.1; Domain: Public API; Priority: Medium; Size: M; Sprint: 10; Depends: PERM-002, AUD-001 | Title: Implement API tokens and rate limits. Context: external users need controlled API access. Scope: token create/revoke/list, scopes, rate limit buckets. Security: hashed token storage. AC/Test/DoD: token cannot access outside scope/org. |
| API-002 | Type: Story; Parent: F09.1; Domain: Public API; Priority: Medium; Size: L; Sprint: 10; Depends: API-001, ISS-002, PROJ-002 | Title: Implement public REST API v1 for core work objects. Context: developer friendliness requires a documented API. Scope: projects, issues, comments, web pagination, errors. API: stable versioned contract. AC/Test/DoD: OpenAPI docs and contract tests pass. |
| WEBHOOK-001 | Type: Story; Parent: F09.1; Domain: Public API; Priority: Medium; Size: L; Sprint: 10; Depends: API-001, EVT-001 | Title: Implement outbound webhooks and delivery logs. Context: customers will sync qeetro to other tools. Scope: subscriptions, signed delivery, retries, delivery history. Security: secret rotation. AC/Test/DoD: failed delivery retries then dead-letters with visible log. |
| IMP-001 | Type: Task; Parent: F09.2; Domain: Integrations; Priority: Medium; Size: M; Sprint: 10; Depends: ISS-002, PROJ-002 | Title: Build CSV import framework. Context: migration lowers adoption friction. Scope: upload, mapping, validation, dry-run, import job. Edge: malformed rows and duplicates. AC/Test/DoD: sample CSV imports projects/issues with error report. |
| IMP-002 | Type: Story; Parent: F09.2; Domain: Integrations; Priority: Low; Size: M; Sprint: 10; Depends: IMP-001, GH-002 | Title: Build GitHub Issues importer. Context: dev teams often start in GitHub. Scope: repo issue import, labels, assignees best effort. Security: respect repo selection. AC/Test/DoD: importer creates qeetro issues with source links and idempotency. |
| IMP-003 | Type: Story; Parent: F09.2; Domain: Integrations; Priority: Low; Size: L; Sprint: 10; Depends: IMP-001 | Title: Build Jira/Linear basic importer. Context: switching tools needs migration path. Scope: CSV/API minimal fields, mapping UI later. Edge: custom fields unsupported in first pass. AC/Test/DoD: import dry-run reports skipped/unsupported fields. |
| DOCS-001 | Type: Task; Parent: F09.3; Domain: Docs; Priority: High; Size: M; Sprint: 10; Depends: REL-001 | Title: Write user, admin, and developer docs. Context: v1 needs self-serve adoption. Scope: getting started, admin roles, API auth, integrations, troubleshooting. AC/Test/DoD: docs cover first project, invite, issue, board, sprint, GitHub integration. |
| REL-002 | Type: Task; Parent: F09.3; Domain: DevOps; Priority: Critical; Size: M; Sprint: 10; Depends: API-002, DOCS-001, REL-001 | Title: Complete v1 launch checklist. Context: launch requires product, technical, and support readiness. Scope: release notes, rollback, monitoring, support channels, known limitations. AC/Test/DoD: v1 criteria signed off and all P0/P1 issues closed. |

### v2 and Future Spikes

| ID | Metadata | Issue content and delivery |
| --- | --- | --- |
| ENT-001 | Type: Spike; Parent: F10.1; Domain: Auth; Priority: Medium; Size: L; Sprint: Future; Depends: REL-002 | Title: Spike SAML/SCIM and enterprise identity. Context: larger customers need enterprise identity. Scope: provider requirements, data model deltas, provisioning lifecycle. AC/Test/DoD: recommendation ADR and implementation epic drafted. |
| ENT-002 | Type: Spike; Parent: F10.1; Domain: Roadmaps; Priority: Medium; Size: L; Sprint: Future; Depends: ROAD-002, ANA-002 | Title: Spike portfolio planning and capacity model. Context: organization-level planning should build on projects/epics. Scope: portfolio hierarchy, capacity, dependencies. AC/Test/DoD: avoid breaking issue/project core semantics. |
| ENT-003 | Type: Spike; Parent: F10.1; Domain: Settings; Priority: Medium; Size: L; Sprint: Future; Depends: AUTO-001, ISS-001 | Title: Spike workflow versioning and custom field analytics. Context: configurability needs governance. Scope: config versions, migration, indexed custom fields, reporting limits. AC/Test/DoD: proposal includes constraints and rollback strategy. |
| FUT-001 | Type: Spike; Parent: F10.2; Domain: Platform; Priority: Low; Size: L; Sprint: Future; Depends: API-002, WEBHOOK-001 | Title: Spike marketplace/app framework. Context: extensibility can become a moat after core stability. Scope: app auth, scopes, extension points, review process. AC/Test/DoD: recommendation avoids plugin risk before governance exists. |
| FUT-002 | Type: Spike; Parent: F10.2; Domain: DevOps; Priority: Low; Size: L; Sprint: Future; Depends: REL-002, DATA-001 | Title: Spike self-hosted edition packaging. Context: data-control customers may require self-hosting. Scope: license model, deployment docs, upgrade path, support cost. AC/Test/DoD: decision document names what must be productized first. |
| FUT-003 | Type: Spike; Parent: F10.2; Domain: Architecture; Priority: Low; Size: M; Sprint: Future; Depends: OBS-001, PERF-001 | Title: Spike service extraction candidates. Context: split services only when pressure proves it. Scope: integrations, AI, search, notifications evaluation. AC/Test/DoD: extraction scorecard based on load, team ownership, data coupling. |
| FUT-004 | Type: Spike; Parent: F10.2; Domain: DevOps; Priority: Low; Size: M; Sprint: Future; Depends: FUT-003 | Title: Spike Kubernetes migration readiness. Context: Kubernetes should wait for operational need. Scope: container contracts, config, secrets, workers, migrations. AC/Test/DoD: migration plan exists but no premature cluster work starts. |

# 14. Sprint Planning

Assumption: two-week sprints start Monday, May 18, 2026. Sprint 0 is the current planning/setup window from May 14 to May 17, 2026.

| Sprint | Goal | Planned Issues | Dependencies | Risks | Expected Outcome |
| --- | --- | --- | --- | --- | --- |
| Sprint 0 | Make planning actionable in GitHub. | PL-001 to PL-004 | None | Overplanning, duplicate project fields | Project, labels, milestones, templates, and ADR process are ready. |
| Sprint 1 | Establish buildable platform foundation. | PF-001 to PF-012 | Sprint 0 | Tooling churn, CI slowdowns | Monorepo, app shells, DB/Redis, CI, tests, env validation, observability baseline. |
| Sprint 2 | Build secure identity, tenancy, and RBAC foundation. | ID-001, AUTH-001 to AUTH-004, ORG-001 to ORG-002, MEM-001 to MEM-002, PERM-001 to PERM-003, UI-AUTH-001, UI-ORG-001 | Sprint 1 | Auth/security mistakes, tenant model drift | User can sign up, create org, invite members, and protected routes enforce permissions. |
| Sprint 3 | Build project and issue core. | TEAM-001 to TEAM-002, PROJ-001 to PROJ-002, UI-PROJ-001, ISS-001 to ISS-005, UI-ISS-001 | Sprint 2 | Issue schema lock-in, weak event model | Users can create projects and issues with core metadata and activity events. |
| Sprint 4 | Build backlog, board, ranking, and filters. | BACKLOG-001 to BACKLOG-002, BOARD-001 to BOARD-002, UI-BACKLOG-001, UI-BOARD-001, FILTER-001 | Sprint 3 | Concurrent ordering bugs, slow boards | Teams can groom backlog and move issues on a Kanban board with optimistic UI. |
| Sprint 5 | Add collaboration, realtime, notifications, and audit. | CMT-001 to CMT-002, UI-CMT-001, EVT-001, ACT-001, UI-ACT-001, RT-001 to RT-003, UI-RT-001, NOTIF-001 to NOTIF-002, UI-NOTIF-001, AUD-001 | Sprint 4 | Realtime data leaks, event replay bugs | Comments, activity, realtime updates, notification inbox, and audit baseline work. |
| Sprint 6 | Add agile planning and roadmap primitives. | EPIC-001 to EPIC-002, UI-EPIC-001, SPR-001 to SPR-002, UI-SPR-001, ROAD-001 to ROAD-002, UI-ROAD-001 | Sprint 5 | Scope creep into heavy portfolio/Gantt | Epics, cycles/sprints, and lightweight roadmap are usable. |
| Sprint 7 | Add discovery, analytics, and assistive AI. | ANA-001 to ANA-002, UI-ANA-001, SEARCH-001 to SEARCH-002, UI-SEARCH-001, FILE-001, AI-001 to AI-005, UI-AI-001 | Sprints 5-6 | AI permission leaks, expensive queries | Search, metrics, file abstraction, and human-confirmed AI assistance are available. |
| Sprint 8 | Add developer integrations and safe automation. | GH-001 to GH-004, SLACK-001 to SLACK-002, AUTO-001 to AUTO-003, UI-AUTO-001, QUEUE-001 | Sprints 5-7 | External API flakiness, automation loops | GitHub/Slack MVP, automation engine, and queue reliability are ready. |
| Sprint 9 | Harden for beta. | SEC-001 to SEC-003, DATA-001, PERF-001, OBS-001 to OBS-002, UX-001, QA-001, REL-001 | MVP and beta features | Hidden tenant bug, performance surprises | Beta release is monitored, secure enough for pilots, and ergonomically usable. |
| Sprint 10 | Prepare v1 launch surface. | API-001 to API-002, WEBHOOK-001, IMP-001 to IMP-003, DOCS-001, REL-002 | Beta signoff | API contract instability, import edge cases | Public API, webhooks, import path, docs, and v1 readiness checklist are complete. |
| Future | Expand based on adoption pressure. | ENT-001 to ENT-003, FUT-001 to FUT-004 | v1 usage data | Premature enterprise/platform scope | v2 decisions are backed by data, not speculation. |

# 15. Implementation Order

## Best Sequence

1. Planning system: project, labels, milestones, templates, ADRs.
2. Monorepo/tooling: pnpm, TypeScript, lint, CI, app shells.
3. Local infrastructure: Postgres, Redis, Prisma, seed/test harness.
4. Identity and tenancy: users, auth, organizations, membership.
5. Permissions: RBAC matrix, guards, tenant isolation tests.
6. Work core data model: workspaces, teams, projects, issues, statuses, relations.
7. Work core APIs and UI: project overview, issue list/detail.
8. Ordering and boards: backlog ranks, board views, optimistic movement.
9. Event foundation: issue events, transactional outbox, activity projection.
10. Collaboration and realtime: comments, mentions, sockets, Redis fanout.
11. Notifications and audit: inbox, queue delivery, admin/security audit.
12. Agile planning: epics, sprints/cycles, roadmaps.
13. Discovery and insight: search, metrics, analytics dashboards.
14. AI assistance: run logging, permission-aware context, drafts, summaries, risk suggestions.
15. Integrations: GitHub first, Slack second.
16. Automation: after events, permissions, audit, and queue reliability exist.
17. Hardening: security, performance, backup/restore, observability, a11y.
18. Public API, webhooks, imports, docs, launch readiness.

## Do Not Build Early

- Kubernetes, service mesh, or advanced cloud platform engineering.
- Autonomous AI agents that write or mutate work without preview.
- Marketplace/plugin framework.
- Enterprise SSO/SCIM before core tenancy and RBAC prove stable.
- Heavy Gantt/portfolio/capacity planning before epics/sprints/roadmaps are used.
- External search infrastructure before PostgreSQL FTS is proven insufficient.
- Billing until pricing/product packaging decisions are clearer.
- Mobile app before web workflows are stable.

## Parallelization Opportunities

- Frontend shell, API shell, and CI can start together after monorepo scaffold.
- Auth UI can proceed once API contracts are drafted, while backend auth is implemented.
- Project UI and issue UI can split after schema/API DTOs stabilize.
- Search projection, analytics projection, and notification projection can proceed in parallel after outbox exists.
- GitHub and Slack integrations can split once integration installation schema and queue policy are in place.
- Security/performance/a11y hardening can begin before beta completion, but final signoff depends on MVP flows being feature-complete.

## Architectural Lock-In Warnings

- Issue schema is the biggest lock-in point. Keep custom fields typed and bounded, and do not model every UI view as a separate source of truth.
- Permission checks must be centralized. If each module invents access logic, future enterprise features become risky.
- Realtime must broadcast permission-filtered presentation events, not raw domain events.
- AI context retrieval must use the same permission model as the product, or it becomes a hidden data leak.
- Event contracts should be versioned early because analytics, search, notifications, automation, integrations, and AI will all consume them.

# 16. Risks & Recommendations

| Risk | Why It Matters | Mitigation |
| --- | --- | --- |
| Scope sprawl | The competitor set tempts an everything-app roadmap. | Freeze MVP around auth, orgs, projects, issues, backlog, board, comments, activity, realtime, notifications, basic search, and CI. |
| Premature microservices | Distributed systems slow product discovery and increase ops burden. | Keep modular monolith, version events, isolate modules, revisit extraction only after v1 metrics. |
| Weak tenant isolation | Multi-tenant data leaks are existential. | Add `organization_id` discipline, policy guards, tenant test suite, search/realtime/file isolation tests. |
| Issue schema lock-in | Work item model drives every other domain. | Model core fields relationally, custom fields typed/bounded, migrations reviewed by architecture process. |
| Board ordering bugs | Ranking is a high-frequency concurrent path. | Isolate rank algorithm, test concurrent moves, use idempotency keys and rebalance strategy. |
| Event replay side effects | Notifications, search, analytics, integrations, and automation depend on events. | Transactional outbox, idempotent consumers, dedupe keys, dead-letter queues. |
| Realtime data leakage | WebSocket channels bypass normal request/response habits. | Auth handshake, subscription authorization, permission-filtered presentation events. |
| AI trust failure | AI that acts opaquely will reduce confidence. | Run logs, source-linked output, preview/confirm for writes, policy engine, cost and token budgets. |
| Search performance | Search can overload transactional DB if unmanaged. | Search projection table, indexes, query budgets, later external search only if metrics require it. |
| Notification noise | PM tools often become attention spam. | Preferences, dedupe, digest strategy, inbox as source of truth, avoid over-notifying early. |
| Automation loops | Rule engines can create hidden business logic and runaway updates. | Dry-run, run history, loop detection, owner, rate limits, kill switch. |
| Integration brittleness | External APIs fail, retry, and change semantics. | Idempotency, webhook signatures, sync cursors, retries/backoff, visible delivery logs. |
| Reporting inaccuracies | Bad analytics destroy planning trust. | Derive metrics from immutable events and scope history, add fixture-based expected reports. |
| Frontend state drift | Optimistic UI can diverge from server truth. | TanStack Query for server data, clear reconciliation rules, stable query keys, realtime dedupe. |
| Developer experience decay | Monorepos can become tangled. | Dependency rules, code owners, typecheck/lint CI, ADRs for cross-domain changes. |

## CTO Recommendations

1. Build the narrow daily execution loop first: org -> project -> issue -> board -> comment -> realtime update.
2. Treat permissions, events, and activity as platform primitives, not later polish.
3. Delay AI until the system has enough structured work context and auditability to make AI trustworthy.
4. Keep configurability explicit, typed, versioned, and limited until real user pressure proves what must be flexible.
5. Use GitHub as a first-class integration, not a competitor to replace.
6. Make every future service extraction candidate prove three things: separate scaling pressure, separate team ownership, and stable event/API contracts.
7. Review the issue catalog after Sprint 4. That is the first point where product reality will be strong enough to adjust beta scope intelligently.
