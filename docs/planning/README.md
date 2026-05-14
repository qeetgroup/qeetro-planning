# qeetro Planning Index

This folder is the pre-implementation blueprint for qeetro. It is intended to let you create the GitHub Project named `qeetro roadmap`, define milestones, create parent epics and child issues, and begin sprint planning without needing to invent architecture as you go.

## Documents

1. [Competitor Analysis, Product Strategy, and Philosophy](01-competitor-strategy.md)
   - Jira, Linear, Asana, monday.com, GitHub Projects, ClickUp, Plane, Notion, and Trello analysis.
   - Sections 1-3: qeetro vision, positioning, product philosophy, constraints, and differentiation.

2. [Architecture Blueprint](02-architecture-blueprint.md)
   - Sections 4-8: domain decomposition, system architecture, monorepo design, MVP scope, and roadmap.
   - Frontend, backend, database, realtime, queue, event, search, caching, AI, observability, deployment, CI/CD, authorization, and multi-tenancy architecture.
   - Monorepo structure and package boundary rules.

3. [GitHub Project Setup](03-github-project-setup.md)
   - Sections 9-12: project fields, views, workflows, labels, milestones, issue states, and epic hierarchy.

4. [Issue Catalog and Sprint Plan](04-issue-catalog.md)
   - Sections 13-16: parent/child issue hierarchy, sprint planning, implementation order, risks, and recommendations.
   - Implementation-ready issue catalog with metadata, dependencies, acceptance criteria, tests, and definition of done.
   - Sprint sequencing and implementation order.

## Planning Assumptions

- Sprint length: 2 weeks.
- Suggested start: Monday, May 18, 2026.
- Initial architecture: pnpm monorepo, modular monolith, event-driven internally, PostgreSQL first, Redis/BullMQ for queues and realtime fanout.
- Explicit non-goal: no Kubernetes and no premature microservices in MVP.
- Product scope: production-grade MVP through v1, with v2 and future roadmap carved as later epics.
