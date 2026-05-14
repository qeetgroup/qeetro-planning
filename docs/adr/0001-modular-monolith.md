# ADR-0001: Start qeetro as a modular monolith, defer microservices

- Status: Accepted
- Date: 2026-05-14
- Deciders: qeetro maintainer
- Related: [02-architecture-blueprint.md §4-§8](../planning/02-architecture-blueprint.md), [04-issue-catalog.md §15-§16](../planning/04-issue-catalog.md)

## Context

qeetro is a new AI-native project execution platform targeting software engineering teams. The planning blueprint identifies 26 internal domains (auth, identity, organizations, memberships, permissions, workspaces, teams, projects, issues, epics, boards, backlog, sprints, roadmaps, comments, activity, notifications, realtime, search, files, analytics, automation, integrations, AI assistant, audit logs, settings, public API).

A naive reading of that surface area suggests microservices from day one. Three forces push back:

1. **Team size.** A single maintainer is building the MVP. Distributed-system operational burden would dominate feature velocity.
2. **Domain stability.** Issue schema, permissions model, and event contracts will iterate heavily during MVP and Beta. Splitting services prematurely freezes contracts before they are correct.
3. **Cost of premature distribution.** Cross-service consistency, deployment matrix, observability per service, schema evolution, retry semantics, and developer ergonomics each carry real fixed costs that only pay off when independent scaling or team ownership requires them.

The opposite extreme — a single uncategorized monolith — is also rejected because the planning blueprint commits to event-driven internals, multi-tenant isolation, AI-aware permission boundaries, and eventual service extraction for high-load surfaces (integrations, AI, search, notifications).

## Decision

qeetro will be built as a **modular monolith** with strict domain-module boundaries, an internal event bus, a transactional outbox, and shared deployable units `apps/api`, `apps/web`, `apps/worker`. Service extraction is deferred until each candidate domain independently proves three things: separate scaling pressure, separate team ownership, and stable event/API contracts.

Concretely:

- NestJS modules form the domain boundary inside `apps/api/src/modules/<domain>`.
- Each module exposes only application services to other modules; repositories stay private.
- Cross-module communication happens via application services for synchronous reads and via versioned domain events (`packages/event-contracts`) for asynchronous side effects.
- All side-effect projections (activity, notifications, search, analytics, integrations, automation, AI) consume the outbox, never call domain modules directly.
- A single PostgreSQL database is the source of truth for MVP, with `organization_id` discipline on every tenant-owned table.

## Consequences

### Positive

- Highest product velocity for a single-maintainer Sprint 0–10 phase.
- Strong refactoring surface: cross-module changes ship in one PR with one CI run.
- Lower operational cost: one deployable, one log stream, one tracing context per request.
- Event-driven internals already pay back as projections and AI features come online, without requiring separate services.

### Negative / Tradeoffs

- Risk of accidental cross-module coupling if discipline lapses (mitigated by ESLint import-boundary rules and CODEOWNERS).
- Single database becomes a scaling bottleneck eventually (acceptable until v1; revisit after pilot load data).
- One process owns CPU profile of issue API + websocket fanout + heavy AI prompts; we accept this until `apps/worker` is in place and we measure real contention.
- Public perception bias: hiring may be harder if candidates expect a microservice stack. Mitigated by documenting the extraction roadmap.

### Neutral

- We still write code as if extraction were possible: typed contracts, isolated modules, no cross-domain repository imports.

## Alternatives Considered

| Option | Summary | Why not chosen |
| --- | --- | --- |
| Pure single-module monolith | One Nest module, free imports anywhere | Loses domain boundaries; makes future extraction impossible without rewrites |
| Microservices from day one | Auth, issues, realtime, AI as separate services with gRPC/REST | Operational overhead crushes solo velocity; freezes contracts too early; Kubernetes/mesh dependency too early |
| Service-per-bounded-context with shared DB | Multiple deploys against one DB | Worst of both worlds: deployment complexity without independent scaling |
| Serverless function fabric | Each domain as functions on Vercel/AWS | Cold start + queue/realtime constraints + state model mismatch with current product needs |

## Migration / Rollback

Extraction is the migration path, not the rollback. Each candidate domain extracts on its own schedule once it earns it. Triggers for extraction:

- Integrations: when external API load or independent deploy cadence justifies a separate worker pool.
- AI assistant: when inference cost, latency, or GPU/vendor isolation requires it.
- Search: when PostgreSQL FTS hits relevance or write-amplification limits.
- Notifications: when fanout volume requires its own queue topology.
- Realtime: when websocket connection count exceeds what a single Node process can serve.

Each extraction must produce its own ADR superseding the relevant scope of this one. Rollback to a less modular structure is explicitly not supported — module boundaries are load-bearing for every other ADR.

## Open Questions

- [ ] When does the first `apps/worker` extraction land vs staying inside `apps/api`? (Target: Sprint 5 once outbox + BullMQ are wired.)
- [ ] Do we adopt Nx, Turborepo, or stay on pnpm-only workspaces for build orchestration? (Decision deferred to a separate ADR before Sprint 1.)
- [ ] What is the exact event-contract versioning policy (semver vs explicit `.v1` suffix)? (Default to explicit `.v1` suffix per planning doc until proven painful.)

## References

- [docs/planning/02-architecture-blueprint.md](../planning/02-architecture-blueprint.md)
- [docs/planning/04-issue-catalog.md §15 Architectural Lock-In Warnings](../planning/04-issue-catalog.md)
- Fowler, "MonolithFirst" (2015): https://martinfowler.com/bliki/MonolithFirst.html
- Posta, "The Hardest Part About Microservices: Your Data" (2016).
