# 4. Domain Architecture

qeetro should start as a modular monolith with domain-driven module boundaries. The goal is not to split services early, but to make future extraction possible by respecting ownership boundaries now.

## Domain Catalog

| Domain | Purpose and Business Capabilities | Core Entities / Aggregates | APIs and Events | Dependencies | Priority | Complexity | Risks, Scaling, Extraction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Auth | Login, session, token lifecycle, password auth, refresh rotation, invite acceptance | AccountCredential, Session, RefreshToken, PasswordReset, EmailVerification | `POST /auth/login`, `POST /auth/refresh`; events: `auth.session.created`, `auth.token.revoked` | Identity, Notifications | P0 | M | Security-sensitive. Keep provider abstraction for future SSO. Extractable only with Identity contract. |
| Identity | User profile, account identity, preferences, avatars, notification preferences | User, UserProfile, UserPreference | `GET /me`, `PATCH /me`; events: `identity.user.created`, `identity.user.updated` | Auth | P0 | M | Global user vs tenant membership must stay clean. Extraction feasible. |
| Organizations | Tenant root, billing placeholder, org settings, slug, owner | Organization, OrganizationSettings | `POST /orgs`, `GET /orgs/:id`; events: `org.created`, `org.updated` | Identity | P0 | M | Tenant boundary. Hard to extract because all domains reference org. |
| Memberships | Org membership, roles, invitations, seat state | Membership, Invitation, RoleAssignment | `POST /orgs/:id/invites`; events: `membership.added`, `membership.role.changed` | Organizations, Identity, Permissions, Notifications | P0 | M | Invitations and access revocation must be reliable. |
| Permissions | RBAC/ABAC policies, role definitions, resource permissions | Role, Permission, Policy, ResourceGrant | Policy checks, admin APIs; events: `permission.changed` | Memberships, Teams, Projects | P0 | L | Central risk. Avoid scattering authorization logic. Extraction unlikely early. |
| Workspaces | High-level grouping inside an org, product areas, departments | Workspace, WorkspaceSettings | CRUD; events: `workspace.created` | Organizations, Memberships | P1 | S | Important for scale and future multi-team orgs. |
| Teams | Execution teams, team membership, workflows, triage ownership | Team, TeamMember, TeamWorkflow | CRUD; events: `team.created`, `team.member.added` | Workspaces, Memberships, Permissions | P1 | M | Team-level workflow config drives issues/cycles. |
| Projects | Time-bound/product outcomes, project metadata, status, owner, health | Project, ProjectMember, ProjectStatusUpdate | CRUD, status update APIs; events: `project.created`, `project.health.changed` | Teams, Permissions, Activity | P1 | M | Core aggregate. Future extraction feasible with Issue references. |
| Issues | Work item system: stories, tasks, bugs, features, sub-issues, labels, custom fields | Issue, IssueRelation, IssueLabel, IssueFieldValue, IssueStatus | CRUD, bulk update, relations; events: `issue.created`, `issue.updated`, `issue.status.changed` | Projects, Teams, Permissions, Activity, Search | P0 | XL | Hot path. Needs indexing, ordering, history, idempotent event model. Extraction candidate later. |
| Epics | Parent work packages across projects/teams, progress rollups | Epic, EpicIssue, EpicStatus | CRUD, rollup APIs; events: `epic.progress.changed` | Issues, Projects | P1 | M | Could be issue type or separate aggregate. Keep separate semantic layer. |
| Boards | Visual Kanban boards, columns, swimlanes, filters, saved views | Board, BoardColumn, BoardView, BoardFilter | Board query/move APIs; events: `board.item.moved` | Issues, Teams, Projects, Realtime | P1 | L | Ordering and concurrent moves are tricky. Keep rank algorithm isolated. |
| Backlog | Ordered project/team backlog, prioritization, triage queues | Backlog, BacklogItem, Rank | Rank APIs; events: `backlog.rank.changed` | Issues, Teams | P1 | L | Rank conflicts need deterministic handling. |
| Sprints/Cycles | Sprint/cycle planning, capacity, commitment, scope change tracking | Sprint, SprintIssue, SprintGoal, CapacitySnapshot | CRUD, planning APIs; events: `sprint.started`, `sprint.scope.changed`, `sprint.completed` | Teams, Issues, Analytics | P2 | L | Scope history matters for analytics. |
| Roadmaps | Timeline planning, milestones, releases, dependencies | Roadmap, RoadmapItem, Milestone, Release | Timeline APIs; events: `roadmap.item.changed`, `release.created` | Projects, Epics, Issues | P2 | M | Avoid building heavy Gantt early. |
| Comments | Threaded discussions on issues/projects/docs | Comment, CommentReaction, Mention | CRUD; events: `comment.created`, `mention.created` | Identity, Issues, Notifications, Activity | P1 | M | Mentions drive notifications. |
| Activity Feed | Immutable audit-style activity stream for domain changes | ActivityEvent | Query APIs; consumes all domain events | All domains | P1 | M | Must be append-only, filterable, tenant-scoped. |
| Notifications | In-app notifications, email queue, digest, preferences | Notification, NotificationDelivery, NotificationPreference | Query/update; events: `notification.created`, `notification.sent` | Identity, Comments, Activity, Queue | P2 | L | Fanout, dedupe, preferences, digest scheduling. |
| Realtime | WebSocket subscriptions, presence, event broadcast, optimistic update confirmation | Connection, Presence, ChannelSubscription | Socket events; consumes domain events | Auth, Permissions, Redis, Activity | P1 | L | Must authorization-filter events; scale with Redis adapter. |
| Search | Full-text and structured search over issues/projects/comments/docs | SearchDocument, SearchIndexJob | Search APIs; consumes index events | Issues, Projects, Comments, Files | P2 | L | Start with Postgres FTS, abstract for OpenSearch/Meilisearch later. |
| Files | Attachments, avatars, file metadata, object storage adapters | FileAsset, FileLink, UploadSession | Upload/download APIs; events: `file.uploaded` | Auth, Permissions, Issues, Comments | P2 | M | Virus scanning and signed URLs later. |
| Analytics | Agile reports, throughput, cycle time, burndown, health metrics | MetricSnapshot, ReportView, AnalyticsQuery | Report APIs; consumes events | Issues, Sprints, Projects, Activity | P2 | L | Use event-derived snapshots to avoid expensive live aggregation. |
| Automation | Rule definitions, triggers, conditions, actions, run history | AutomationRule, AutomationRun, AutomationTrigger, AutomationAction | Rule CRUD; events: `automation.run.completed` | Events, Queue, Permissions, Notifications | P3 | XL | Needs dry-run, ownership, rate limits, action audit, kill switches. |
| Integrations | GitHub/Slack first, later Figma/Calendar/Email | IntegrationInstallation, ExternalAccount, WebhookEndpoint, SyncCursor | OAuth, webhook endpoints; events: `integration.installed`, `external.issue.synced` | Auth, Issues, Queue, Activity | P3 | XL | External idempotency and rate limits. Service extraction candidate. |
| AI Assistant | AI chat, issue drafting, summarization, risk detection, natural-language query | AiConversation, AiRun, AiToolCall, AiMemory, AiPolicy | Assistant APIs; events: `ai.suggestion.created`, `ai.action.executed` | Search, Permissions, Issues, Projects, Activity | P3 | XL | Permission-aware retrieval, cost controls, audit, prompt/version governance. |
| Audit Logs | Enterprise audit of security and admin actions | AuditLogEntry | Query/export; consumes admin/security events | Auth, Memberships, Permissions, Integrations | P2 | M | Required before serious enterprise use. Immutable append-only storage. |
| Settings | Org/workspace/team/project settings and feature flags | SettingsProfile, FeatureFlag, ConfigVersion | Settings APIs; events: `settings.changed` | All domains | P1 | M | Config drift risk. Version important settings. |
| Public API | External REST/GraphQL API, tokens, rate limits, webhooks | ApiToken, WebhookSubscription, RateLimitBucket | API and webhook APIs; events: `api.token.created`, `webhook.delivery.failed` | Auth, Permissions, Integrations | P4 | L | Build after internal contracts stabilize. |

# 5. System Architecture

## Frontend Architecture

**Decision:** Next.js App Router with React, TypeScript, TailwindCSS, shadcn/ui, TanStack Query, and Zustand.

**Why:** Next.js gives routing, server rendering where useful, API edge options later, and strong ecosystem fit. TanStack Query owns server cache and invalidation. Zustand owns ephemeral UI state such as selected board filters, command palette state, split panes, and local drafts.

**Structure:**

- Route groups by product area: `(auth)`, `(app)`, `(marketing-later)`.
- Feature modules under `apps/web/src/features/<domain>`.
- Shared UI primitives in `packages/ui`.
- API client generated or typed in `packages/api-client`.
- Server state in TanStack Query hooks per domain.
- Optimistic updates for issue status, board rank, comments, assignments.
- Zustand only for local UI state, never as source of truth for server data.

**Tradeoffs:** Next.js can tempt mixing business logic into server components. Keep domain logic in API/backend packages and keep frontend domain services thin.

**Scaling implications:** Use virtualized lists for backlogs/boards, route-level code splitting, and normalized query keys. Board columns and issue lists must paginate.

## Backend Architecture

**Decision:** NestJS modular monolith with strict domain modules.

**Why:** NestJS gives module boundaries, DI, guards, interceptors, pipes, gateways, and background worker reuse. A modular monolith avoids distributed-system cost while allowing future service extraction.

**Module shape per domain:**

- `domain`: entities, value objects, domain services, policies, events.
- `application`: commands, queries, use cases.
- `infrastructure`: Prisma repositories, queue processors, external adapters.
- `presentation`: REST controllers, WebSocket gateways, DTOs.

**Rules:**

- Controllers call application services only.
- Repositories are private to domain modules.
- Cross-domain writes use application services or domain events.
- Events are versioned contracts in `packages/event-contracts`.
- All mutating use cases emit activity/audit events when user-visible or security-relevant.

## Monorepo Architecture

**Decision:** pnpm workspaces with apps and packages.

**Why:** Shared TypeScript types, event contracts, UI primitives, config, and API clients reduce drift. Keep deployables separated while enabling fast local development.

## Database Architecture

**Decision:** PostgreSQL primary database via Prisma.

**Why:** Project management data is relational and needs strong consistency: tenants, permissions, issue relations, rank ordering, reports, audit trails.

**Core principles:**

- Every tenant-owned table includes `organization_id`.
- Use UUIDs or cuid-style IDs consistently.
- Use composite unique indexes with tenant scope, for example `(organization_id, slug)`.
- Use soft-delete only where required; otherwise prefer archived states with audit history.
- Use event/outbox tables for reliable async processing.
- Use JSONB only for bounded custom fields or provider payloads, not core relational data.
- Add created/updated/deleted metadata consistently.

**Custom fields strategy:**

- Define `custom_field_definition` per org/workspace/project.
- Store typed values in `issue_custom_field_value` with typed columns where possible: `text_value`, `number_value`, `date_value`, `boolean_value`, `json_value`.
- Selectively index field definitions marked `isIndexed`.
- Prevent unbounded reporting complexity with field count and indexed field limits.

## Realtime Architecture

**Decision:** WebSockets in the API initially, Redis adapter for fanout, domain-event driven broadcasts.

**Why:** Realtime board/comment/issue updates are core to perceived speed. Keep it in the monolith first to avoid service complexity.

**Pattern:**

1. Command mutates database.
2. Transaction writes outbox event.
3. Event dispatcher publishes to Redis/BullMQ.
4. Realtime gateway maps event to authorized channels.
5. Client receives event and reconciles optimistic state.

**Channels:**

- `org:<orgId>`
- `workspace:<workspaceId>`
- `team:<teamId>`
- `project:<projectId>`
- `issue:<issueId>`
- `user:<userId>`

**Security:** Do not broadcast raw domain events directly. Build presentation events after permission filtering.

## Queue Architecture

**Decision:** BullMQ over Redis.

**Queues:**

- `events`: outbox dispatch and projections.
- `notifications`: in-app/email digest delivery.
- `search-index`: index updates.
- `integrations`: inbound/outbound sync.
- `ai`: AI summarization, draft creation, risk analysis.
- `analytics`: metric snapshots.

**Rules:** Jobs are idempotent, retryable, tenant-scoped, and carry correlation IDs.

## Event Architecture

**Decision:** Internal event-driven architecture with transactional outbox.

**Why:** Activity, realtime, notifications, search, analytics, automations, integrations, and AI all react to work changes. Direct synchronous calls will couple the system too early.

**Event contract example categories:**

- `issue.created.v1`
- `issue.updated.v1`
- `issue.status_changed.v1`
- `comment.created.v1`
- `sprint.started.v1`
- `project.health_changed.v1`
- `membership.role_changed.v1`

**Tradeoff:** Event systems add complexity. Use them for side effects and projections, not for core command consistency.

## Search Architecture

**MVP:** PostgreSQL full-text search plus trigram indexes for issues/projects/comments.

**Beta/v1:** Dedicated `search_documents` projection table with weighted fields and permission metadata.

**Later:** Meilisearch/OpenSearch if query volume, typo tolerance, ranking, or cross-object search requires it.

**Why:** Avoid external search infrastructure until product semantics settle.

## Caching Architecture

**Use Redis for:**

- Session/token denylist.
- Rate limits.
- Short-lived query caches for expensive dashboards.
- WebSocket presence.
- Pub/sub fanout.
- BullMQ.

**Avoid caching:**

- Permission decisions without short TTL and invalidation.
- Issue list results before indexes and pagination are proven.

## AI Architecture

**Components:**

- AI Orchestrator application service.
- Context builder that retrieves structured objects first.
- Permission-aware retrieval layer.
- Tool registry for issue/project/comment/search actions.
- Policy engine for allowed AI actions.
- AI run log with prompts, model, input references, output, tool calls, cost, user, org, and approval state.
- Draft layer for AI-proposed issues/status updates/automation rules.

**MVP AI capabilities:**

- Generate issue title/description/acceptance criteria from rough notes.
- Summarize issue and project activity.
- Suggest duplicates/related issues.
- Explain sprint risk from scope and blockers.
- Natural-language issue search.

**Do not build early:**

- Fully autonomous agents.
- Cross-app background agents.
- AI-generated workflow execution without preview.
- Fine-tuning or custom model hosting.

## Observability Architecture

**Stack:**

- OpenTelemetry traces.
- Structured JSON logs.
- Metrics for request latency, queue depth, job failures, DB query duration, realtime fanout count.
- Sentry or equivalent for frontend/backend errors.
- Audit log for security/admin actions.

**Required from Sprint 1:**

- Request ID and correlation ID.
- User/org context in logs, with PII rules.
- Health checks.
- Basic `/metrics` endpoint or metrics adapter.

## Deployment Architecture

**Local:** Docker Compose for Postgres, Redis, API, worker, web.

**MVP hosted:** Containerized web/API/worker deployed to a managed container platform or VPS with managed Postgres/Redis if available.

**Later:** Kubernetes only after one of these is true:

- Multiple teams own independently deployable services.
- Autoscaling patterns diverge materially.
- Enterprise deployment requires it.
- Operational maturity supports it.

## CI/CD Architecture

**GitHub Actions:**

- Install and cache pnpm.
- Typecheck all packages.
- Lint.
- Unit tests.
- Integration tests with Postgres/Redis service containers.
- Prisma migration check.
- Build web/api/worker.
- Security checks: dependency audit, secret scan, basic SAST.
- Preview deployments later.

## Authorization Architecture

**Decision:** RBAC plus ABAC.

**RBAC roles:**

- Org Owner
- Org Admin
- Workspace Admin
- Team Lead
- Project Admin
- Member
- Guest
- Viewer

**ABAC checks:**

- Tenant membership.
- Resource visibility.
- Team/project membership.
- Issue confidentiality.
- External guest restrictions.
- AI action policy.

**Implementation:** Central `PolicyService` with typed resource/action checks. Use Nest guards for route-level checks and application services for object-level checks.

## Multi-Tenancy Architecture

**Decision:** Shared database, tenant-scoped rows.

**Why:** Fastest product velocity and simplest operations. Strong enough for MVP/v1 with careful indexing and permission checks.

**Rules:**

- `organization_id` on tenant tables.
- All repository methods require tenant context.
- No global list endpoint without tenant filter.
- Optional PostgreSQL RLS later for defense in depth.
- Tenant data export/delete should be designed early.

# 6. Monorepo Design

## Proposed Structure

```text
qeetro/
  apps/
    web/
    api/
    worker/
  packages/
    api-client/
    config/
    database/
    domain/
    event-contracts/
    eslint-config/
    logger/
    permissions/
    testing/
    tsconfig/
    ui/
    utils/
  infra/
    docker/
    terraform/
  docs/
    architecture/
    adr/
    api/
    planning/
    runbooks/
  scripts/
  .github/
    ISSUE_TEMPLATE/
    workflows/
```

## Package Boundaries

- `apps/web`: Next.js UI only.
- `apps/api`: HTTP and WebSocket API, NestJS controllers/gateways.
- `apps/worker`: BullMQ processors and scheduled jobs.
- `packages/database`: Prisma schema, migrations, test DB helpers.
- `packages/domain`: shared value objects and pure domain types only. Avoid importing Nest.
- `packages/event-contracts`: versioned event schemas.
- `packages/api-client`: typed client consumed by web and scripts.
- `packages/permissions`: permission constants and shared policy types.
- `packages/config`: environment parsing and typed config.
- `packages/ui`: shadcn/ui-based design system primitives.
- `packages/testing`: factories, fixtures, integration helpers.

## Dependency Rules

- Apps may import packages.
- Packages must not import apps.
- `packages/ui` must not import backend-only packages.
- `packages/domain` must not import Prisma/Nest/React.
- `packages/event-contracts` must be stable and versioned.
- Domain modules inside `apps/api` should not import each other's repositories.

## Naming Conventions

- Database tables: snake_case singular or plural consistently; recommended plural, for example `issues`, `project_members`.
- TypeScript files: kebab-case.
- Classes: PascalCase.
- DTOs: `CreateIssueDto`, `UpdateIssueStatusDto`.
- Events: `<domain>.<event>.v<version>`.
- Queue names: kebab-case.
- Labels: prefix groups, for example `type:epic`, `domain:issues`.

## Code Ownership

- `apps/web/src/features/issues`: Work Core owner.
- `apps/api/src/modules/issues`: Work Core owner.
- `packages/ui`: Frontend platform owner.
- `packages/database`: Platform/backend owner.
- `packages/event-contracts`: Architecture owner.
- `infra/` and `.github/workflows`: DevOps/platform owner.

## Linting Strategy

- ESLint shared config.
- Strict TypeScript.
- Import boundary checks.
- No circular dependencies.
- No direct `process.env` outside config package.
- No untyped API responses.

## Testing Strategy

- Unit tests for domain rules and pure helpers.
- Integration tests for API use cases with Postgres/Redis.
- Contract tests for event schemas.
- Component tests for complex UI primitives.
- E2E tests for core flows after MVP skeleton.
- Load/performance tests for board moves, issue search, notifications, and realtime fanout before beta.

## Release Strategy

- Trunk-based development with short-lived branches.
- Conventional commits optional, but useful.
- Release milestones in GitHub.
- Feature flags for incomplete product areas.
- Preview deployments for PRs after CI/CD foundation.
- Semantic version only after beta; before that use milestone releases.

# 7. MVP Scope

## Phase 0 - Planning and Foundation

**Goal:** Align architecture, project structure, issue hierarchy, and delivery process.

**Business value:** Prevent chaotic build. Establish clear domain boundaries before code.

**Technical priorities:** Monorepo plan, DB strategy, events, auth/tenancy decisions.

**UX priorities:** Define information architecture and core navigation.

**Infra priorities:** Docker, CI/CD design, environment conventions.

**Success metrics:** GitHub Project ready, epics/child issues created, first sprint startable.

**Risks:** Overplanning. Mitigation: freeze MVP scope and defer speculative enterprise features.

## MVP

**Goal:** A small team can create an org, invite members, create projects, manage issues on list/board/backlog, comment, and see realtime updates.

**Business value:** Core daily execution loop.

**Included:**

- Auth and org membership.
- Teams/workspaces.
- Projects.
- Issues with statuses, priorities, assignees, labels, relations.
- Backlog and Kanban board.
- Comments and activity feed.
- Basic realtime updates.
- In-app notifications.
- Basic search.
- Docker local dev and CI.

**Excluded:**

- Advanced automation.
- Deep AI agents.
- Enterprise SSO.
- Billing.
- Kubernetes.
- Mobile app.

**Success metrics:** Issue create/update under 200ms API p95 locally/staging for normal load, board move under 150ms perceived with optimistic UI, sprint demo can run without manual DB edits.

# 8. Roadmap

## Beta

**Goal:** Teams can plan cycles/sprints, use epics/roadmaps, receive reliable notifications, search effectively, and use AI assistive workflows.

**Included:**

- Sprints/cycles.
- Epics and roadmap timeline.
- Notification digests.
- Search indexing.
- AI issue drafting and summaries.
- GitHub integration MVP.
- Audit logs for admin/security events.
- Observability hardening.

**Success metrics:** Dogfoodable by a real team for 4 weeks; no P0 data-loss bugs; meaningful AI suggestions accepted at least 30 percent of the time.

## v1

**Goal:** Production-grade launch for software teams.

**Included:**

- Automation MVP with visible run history.
- Analytics: cycle time, throughput, burndown/burnup, project health.
- Slack integration.
- Public API basics.
- Import from GitHub/Jira/Linear basic CSV/API importer.
- Security review and performance hardening.

**Success metrics:** 5 pilot teams active weekly; board/search/realtime p95 within targets; onboarding to first project in under 10 minutes.

## v2

**Goal:** Expand from team execution to organization-level planning.

**Included:**

- Portfolio planning.
- Advanced capacity.
- Workflow versioning.
- Custom field reporting.
- Enterprise SSO/SAML/SCIM.
- Advanced AI risk detection and automation builder.

## Future Roadmap

- Self-hosted edition.
- Marketplace/app framework.
- Advanced integrations: Figma, calendar, email, CI/CD providers.
- Mobile app.
- Service extraction for integrations, search, AI, or notifications if load/team topology demands it.
