# qeetro Planning: Competitor Analysis, Strategy, and Philosophy

## Source Notes

Current public product and documentation references used while preparing this plan:

- Atlassian: [Jira Software features](https://www.atlassian.com/software/jira/features), [Jira automation](https://support.atlassian.com/cloud-automation/docs/jira-automation/), [Atlassian Intelligence/Rovo](https://www.atlassian.com/software/rovo), [Jira Data Center](https://www.atlassian.com/enterprise/data-center/jira)
- Linear: [Linear product](https://linear.app/), [Linear docs](https://linear.app/docs), [Linear API](https://linear.app/developers), [Linear integrations](https://linear.app/integrations)
- Asana: [Asana work management](https://asana.com/product), [rules and automation](https://help.asana.com/s/article/rules), [Asana AI](https://asana.com/product/ai), [enterprise](https://asana.com/enterprise)
- monday.com: [work management](https://monday.com/work-management), [automations](https://monday.com/features/automations), [AI](https://monday.com/features/ai), [enterprise](https://monday.com/enterprise)
- GitHub: [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects), [Projects workflows](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project), [sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues), [issue types](https://docs.github.com/en/issues/tracking-your-work-with-issues/configuring-issues/managing-issue-types-in-an-organization), [project insights](https://docs.github.com/en/issues/planning-and-tracking-with-projects/viewing-insights-from-your-project)
- ClickUp: [product](https://clickup.com/features), [ClickUp Brain](https://clickup.com/ai), [automations](https://clickup.com/features/automations), [API and webhooks](https://clickup.com/api)
- Plane: [Plane](https://plane.so/), [Plane docs](https://docs.plane.so/), [work items](https://docs.plane.so/work-items), [cycles](https://docs.plane.so/cycles), [modules](https://docs.plane.so/modules)
- Notion: [projects](https://www.notion.com/product/projects), [Notion AI](https://www.notion.com/product/ai), [automations](https://www.notion.com/help/database-automations), [enterprise](https://www.notion.com/enterprise)
- Trello: [features](https://trello.com/features), [automation](https://trello.com/guide/automate-anything), [Power-Ups](https://trello.com/power-ups), [enterprise](https://trello.com/enterprise)

2026 deltas to account for in qeetro planning:

- Jira is positioning [Rovo in Jira](https://www.atlassian.com/software/jira/ai) agents inside Jira workflows for work creation, work breakdown, status drafting, and Teamwork Graph-backed context.
- Linear introduced [Linear Agent](https://linear.app/changelog/2026-03-24-introducing-linear-agent) in March 2026 and is explicitly moving toward agent-native product development workflows.
- Asana launched [AI Teammates](https://asana.com/resources/ai-teammates-overview) as workflow-embedded agents with shared context, governance, and permission-aware execution.
- monday.com [Sidekick](https://support.monday.com/hc/en-us/articles/26701503726610-Get-started-with-monday-sidekick) now emphasizes account/board/item-level action, MCP/API connectivity, permissions, usage limits, and human confirmation for impactful changes.
- GitHub Projects [hierarchy view](https://github.blog/changelog/2026-03-19-hierarchy-view-in-github-projects-is-now-generally-available/) became generally available in March 2026, reinforcing parent/child issue planning as a first-class workflow.
- ClickUp Brain now includes [Super Agents and Autopilot Agents](https://help.clickup.com/hc/en-us/articles/20658787666071-Use-AI-from-anywhere-in-ClickUp) as workspace-level AI surfaces.
- Plane is adding [AI-assisted cycle planning](https://plane.so/cycles), at-risk item detection, cycle summaries, and agent mentions.
- Notion's [April 2026 releases](https://www.notion.com/releases/2026-04-14) expanded AI connectors, MCP/n8n integrations, database enrichment, and performance claims.
- Trello exposes [Atlassian Intelligence activation](https://support.atlassian.com/trello/docs/activate-atlassian-intelligence-for-your-trello-workspace/) for Standard, Premium, and Enterprise workspaces, but its model remains board/list/card first.

User pain themes also reflect recurring public review and community patterns through 2026: Jira complexity and administration overhead, ClickUp performance and reliability complaints, Notion project-management gaps at scale, Trello reporting/dependency limits, monday.com governance sprawl, and Linear customization/reporting constraints.

# 1. Competitor Analysis

### Jira

Product philosophy: highly configurable enterprise issue and workflow management. Jira optimizes for breadth, governance, auditability, and process fit across many team types.

UX philosophy: admin-configured structure first, user speed second. The UI exposes schemes, workflows, issue types, screens, permissions, reports, and JQL. This makes Jira powerful but cognitively expensive.

Information architecture:

- Site -> projects -> issue types -> issues -> subtasks.
- Boards are views over issues, not the source of truth.
- Workflows, fields, permissions, screens, notifications, and automations are separate configurable systems.

Collaboration model: comments, mentions, watchers, links, attachments, Confluence integration, Slack/Teams integrations, and activity history.

Workflows: extremely flexible. Custom issue types, statuses, transitions, validators, post-functions, automation rules, and cross-project boards are strengths.

Performance characteristics: acceptable for normal cloud use, but large instances often suffer from slow navigation, indexing delays, expensive JQL, plugin overhead, and admin complexity.

AI capabilities: Atlassian Intelligence/Rovo focuses on summarization, search, answers, agents, writing assistance, and cross-Atlassian knowledge discovery.

Extensibility: Marketplace, Forge, REST APIs, webhooks, OAuth apps, automation, and Atlassian ecosystem integrations.

Customization: best-in-class, but the configuration model can become a liability. Schemes and workflows often drift into undocumented process debt.

Scalability: enterprise-ready with cloud and Data Center options, but operational complexity rises sharply with custom fields, apps, workflows, and data volume.

Developer experience: strong when paired with GitHub/GitLab/Bitbucket and CI tools, but less joyful than Linear/GitHub due to navigation weight and admin ceremony.

Onboarding: hard for new users and administrators. Non-admin users can usually learn a board, but project configuration is a specialist skill.

User pain points:

- Too many concepts before value is visible.
- Slow or visually dense UI.
- Admin-only configuration bottlenecks.
- Process can dominate execution.
- Hard to keep workflows clean over time.

Enterprise readiness: very high. SSO, audit logs, compliance posture, access controls, marketplace governance, and enterprise support are mature.

Realtime: collaborative enough for comments and updates, but not perceived as truly realtime-first like a modern multiplayer workspace.

Reporting/analytics: deep agile reporting, dashboards, JQL, burnup/burndown, velocity, cumulative flow, advanced roadmaps.

Notifications: mature but noisy. Watchers, mentions, email, in-app, Slack/Teams, and automation can create overload.

Automation: powerful rule-based automation, but rules become hard to govern at scale.

What users love:

- Can model almost any enterprise process.
- Strong reporting and governance.
- Integrates with the broader software delivery ecosystem.
- Mature permissions, auditability, and workflow customization.

What users hate:

- Complexity tax.
- Slow perceived performance.
- Admin bottlenecks.
- Configuration sprawl.

Technical and architectural limitations:

- Generalized custom-field architecture creates query/index/performance pressure.
- Plugin ecosystems add operational risk.
- Workflow flexibility increases migration and consistency costs.
- Deep configurability makes AI automation harder because semantics vary per instance.

Qeetro differentiation opportunity: provide Jira-level execution depth with Linear-level speed and opinionated defaults. Make customization constrained, observable, and reversible instead of unlimited.

### Linear

Product philosophy: fast, opinionated execution for software teams. Linear optimizes for momentum, low friction, keyboard-driven issue flow, and clean product-development primitives.

UX philosophy: speed, focus, and consistency. Linear deliberately limits admin sprawl and prefers defaults over endless configuration.

Information architecture:

- Workspace -> teams -> issues.
- Projects, initiatives, cycles, views, documents, and roadmaps organize work.
- Triage and inbox patterns make incoming work manageable.

Collaboration model: comments, mentions, documents, project updates, GitHub/GitLab links, Slack integration, notifications, and review workflows.

Workflows: team workflows, statuses, cycles, labels, projects, initiatives, triage, estimates, and views. Strong for product engineering, less flexible for arbitrary operations.

Performance characteristics: market-leading perceived speed. Keyboard navigation, optimistic updates, and simple IA reduce friction.

AI capabilities: Linear has been moving into AI-assisted product development and agent-compatible workflows, including issue creation, summarization, and context handoff patterns.

Extensibility: strong APIs, webhooks, OAuth, GraphQL, GitHub/GitLab, Slack, Sentry, Figma, Zapier, and other integrations.

Customization: intentionally limited compared with Jira/monday/ClickUp. This is a strength for coherence and a weakness for broad enterprise process modeling.

Scalability: scales well for modern software teams, but very complex enterprise hierarchies, compliance workflows, and cross-functional process customization can stretch the model.

Developer experience: excellent. Fast keyboard flow, GitHub/GitLab integration, API quality, and low ceremony make it developer-friendly.

Onboarding: strong for software teams. Users understand issues quickly; admins do not need to learn a large configuration model.

User pain points:

- Less suitable for non-software workflows.
- Reporting and portfolio controls are not as deep as Jira.
- Limited customization can block enterprises with established processes.
- Some knowledge and product context still lives in external docs/tools.

Enterprise readiness: improving, with SSO, SCIM, audit logs, and admin controls, but Jira still has a broader enterprise-governance legacy.

Realtime: strong perceived immediacy across issue and collaboration surfaces.

Reporting/analytics: useful but intentionally focused. Less broad than Jira/ClickUp/monday dashboards.

Notifications: clean inbox model and integrations, less noisy than Jira when configured well.

Automation: integration-driven and workflow-driven rather than no-code-platform heavy.

What users love:

- Speed.
- Tasteful UX.
- Developer-first workflow.
- Low admin overhead.
- High signal-to-noise.

What users hate:

- Customization ceilings.
- Reporting ceilings.
- Less flexible for non-engineering teams.

Technical and architectural limitations:

- Opinionated model can become a product constraint for enterprises.
- Cross-domain collaboration/documentation is not as flexible as Notion.
- Less suited to arbitrary work graph modeling.

Qeetro differentiation opportunity: keep Linear's speed and product taste, but add controlled enterprise extensibility, richer context, and AI-native execution support.

### Asana

Product philosophy: work graph for cross-functional work. Asana optimizes for visibility, accountability, goals, portfolios, and coordination across departments.

UX philosophy: approachable task management with multiple views. It is less developer-native and more operations/product/marketing friendly.

Information architecture:

- Organizations/workspaces -> teams -> projects -> tasks/subtasks.
- Portfolios, goals, timelines, forms, rules, and workload layers support cross-team planning.

Collaboration model: task comments, mentions, assignees, dependencies, approvals, forms, project updates, goals, and team pages.

Workflows: lists, boards, timelines, calendars, approvals, rules, forms, templates, portfolios, goals, dependencies, and workload.

Performance characteristics: generally usable, but large workspaces and heavily automated projects can feel busy and slower than focused tools.

AI capabilities: Asana AI and AI teammates are positioned around work graph reasoning, status summaries, smart goals, risk detection, and workflow assistance.

Extensibility: integrations, API, rules, forms, templates, and app ecosystem.

Customization: stronger than Linear, less schema-heavy than Jira/monday. Good for business workflows; less precise for software engineering workflow semantics.

Scalability: strong for multi-team coordination, portfolio visibility, and executive reporting, but can create "work about work" if process is over-modeled.

Developer experience: acceptable, but not developer-native. GitHub integration exists, but Asana is not centered on code workflow.

Onboarding: friendly for task-level users; portfolio/goals/rules require more maturity.

User pain points:

- Too many notification/activity surfaces.
- Subtask visibility and reporting can confuse teams.
- Engineering workflows often feel less natural than Jira/Linear/GitHub.
- Work can become duplicated across projects.

Enterprise readiness: strong SSO, admin controls, data governance, security, portfolios, and goals.

Realtime: collaboration is responsive, but not designed as a deep realtime multiplayer planning canvas.

Reporting/analytics: dashboards, portfolios, goals, workload, and project status are strong for management visibility.

Notifications: broad email/inbox/mentions/activity model; noise can become a problem.

Automation: rules and workflow builder are mature for business-process automation.

What users love:

- Cross-functional visibility.
- Portfolios and goals.
- Friendly UI.
- Flexible project views.

What users hate:

- Notification noise.
- Less developer-native execution.
- Subtask/reporting ambiguity.
- Duplicate work structures.

Technical and architectural limitations:

- Work graph abstraction is broad, so engineering-specific semantics require conventions.
- Multi-homing tasks across projects can create ownership ambiguity.
- AI value depends heavily on clean structured work data.

Qeetro differentiation opportunity: combine Asana's executive visibility with software-native primitives and stronger work semantics.

### monday.com

Product philosophy: configurable Work OS. monday.com optimizes for no-code work management across many business domains.

UX philosophy: colorful, board-centric, template-first, no-code customization.

Information architecture:

- Workspaces -> folders -> boards -> groups -> items/subitems -> columns.
- Views, dashboards, forms, automations, integrations, docs, and apps extend boards.

Collaboration model: item updates, mentions, owners, docs, forms, notifications, dashboards, and integrations.

Workflows: board columns, custom statuses, automations, views, forms, dashboards, dependencies, workload, and integrations.

Performance characteristics: works well for many teams, but complex boards with many columns, formulas, dependencies, automations, and dashboards can become heavy.

AI capabilities: monday AI and Sidekick patterns focus on content generation, summaries, classification, formula/help tasks, and workflow assistance.

Extensibility: marketplace apps, API, webhooks, automations, integrations, and no-code configuration.

Customization: very high. Users can model many workflows without engineering support.

Scalability: organizationally broad but governance-sensitive. Board proliferation and inconsistent schemas become a long-term issue.

Developer experience: decent API and integrations, but product is not engineering-first.

Onboarding: fast with templates; deeper governance requires admin discipline.

User pain points:

- Customization sprawl.
- Boards can become inconsistent databases.
- Enterprise governance and reporting can require careful setup.
- Pricing/plan feature boundaries can surprise growing teams.

Enterprise readiness: strong enterprise offering with security, admin, governance, integrations, and compliance posture.

Realtime: collaborative updates and notifications are solid, but not perceived as a developer-grade realtime execution tool.

Reporting/analytics: dashboards are broad and approachable; advanced engineering analytics need custom modeling.

Notifications: flexible but can become noisy with automation-heavy boards.

Automation: one of monday's strengths. Recipes are approachable but can accumulate hidden logic.

What users love:

- Flexibility.
- Visual boards.
- Templates.
- Easy automation.
- Cross-department applicability.

What users hate:

- Sprawl.
- Performance on complex boards.
- Governance overhead.
- Less native developer workflow.

Technical and architectural limitations:

- Generic board/item/column model can lose domain semantics.
- Automation recipes can become implicit business logic without versioning.
- Reporting depends on schema discipline.

Qeetro differentiation opportunity: deliver flexible boards with explicit software-project semantics, versioned automations, and guardrails against schema drift.

### GitHub Projects

Product philosophy: planning close to code. GitHub Projects optimizes for developer-native planning inside the same ecosystem as repos, issues, pull requests, and code review.

UX philosophy: flexible project views that feel like a spreadsheet/board/table layer over GitHub issues and PRs.

Information architecture:

- Organizations/users -> repositories -> issues/PRs.
- Projects aggregate items across repositories.
- Custom fields, iterations, roadmaps, views, sub-issues, and issue types add planning structure.

Collaboration model: issue discussions, assignees, labels, milestones, PR links, code review, mentions, notifications, and project views.

Workflows: issue tracking, PR lifecycle, milestones, labels, custom fields, iteration fields, built-in project workflows, issue forms, sub-issues, and issue types.

Performance characteristics: generally good within GitHub's scale, but complex planning experiences can feel less specialized than Linear/Jira.

AI capabilities: GitHub Copilot supports code and some issue/PR workflows, but GitHub Projects is not yet a full AI-native PM platform.

Extensibility: APIs, GitHub Actions, webhooks, Apps, CLI, issue forms, project automation, and ecosystem integrations.

Customization: moderate. Strong enough for software teams, less configurable than Jira/monday.

Scalability: excellent for code-adjacent work, cross-repo planning, and open-source workflows. Less ideal for rich product/portfolio/enterprise planning.

Developer experience: excellent due to repository proximity, PR linking, Actions, CLI, and issue-native workflows.

Onboarding: easy for developers already in GitHub; less friendly for non-technical stakeholders.

User pain points:

- Product-management depth is limited compared with dedicated tools.
- Reporting and portfolio planning require workarounds.
- Permissions and views can be awkward across repos/orgs.
- Rich docs/context usually lives in another tool.

Enterprise readiness: strong in security and code governance; planning governance is improving but not Jira-class.

Realtime: issue/project updates are responsive, but planning is not deeply collaborative like docs/canvas tools.

Reporting/analytics: project insights and charts exist, but advanced agile/portfolio analytics are limited.

Notifications: powerful GitHub notification model, but issue noise can be high for active repos.

Automation: GitHub Actions plus project workflows are powerful, though often engineering-maintained rather than PM-owned.

What users love:

- Close to code.
- Minimal duplication between issue and PR.
- CLI/API/dev workflow.
- Good for open source and engineering teams.

What users hate:

- Not enough PM structure.
- Non-developer UX can be rough.
- Reporting and roadmap limitations.

Technical and architectural limitations:

- Planning model must fit GitHub issue/PR primitives.
- Docs, decisions, and execution context are often fragmented.
- Advanced workflows require Actions/API glue.

Qeetro differentiation opportunity: be as developer-friendly as GitHub Projects while providing first-class product planning, AI context, and execution analytics.

### ClickUp

Product philosophy: one app for everything. ClickUp optimizes for feature breadth across tasks, docs, whiteboards, goals, chat, dashboards, automations, and AI.

UX philosophy: configurable and dense. It tries to serve many personas with many views and tools.

Information architecture:

- Workspace -> spaces -> folders -> lists -> tasks/subtasks.
- Docs, goals, dashboards, whiteboards, chat, custom fields, views, automations, and templates surround tasks.

Collaboration model: comments, docs, chat, mentions, assignments, whiteboards, clips, notifications, and sharing.

Workflows: statuses, custom fields, task types, dependencies, recurring tasks, time tracking, docs, goals, dashboards, automations, forms, approvals, and views.

Performance characteristics: feature breadth can create perceived slowness and complexity. Public complaints often mention reliability, speed, and UI overload.

AI capabilities: ClickUp Brain is positioned as AI across tasks, docs, chat, summaries, writing, answers, and automation support.

Extensibility: API, webhooks, integrations, marketplace, automations, and importers.

Customization: very high. Almost every team can model a workflow, but consistency becomes hard.

Scalability: broad organizational scalability, but information architecture complexity and performance complaints are risks.

Developer experience: useful integrations and API, but less elegant than Linear/GitHub for engineering execution.

Onboarding: templates help; product surface area can overwhelm.

User pain points:

- Too many features.
- UI density.
- Performance/reliability concerns.
- Hard to maintain a clean workspace.

Enterprise readiness: enterprise security, SSO, admin, compliance, and support are available.

Realtime: strong collaboration claims across chat/docs/tasks, but user perception varies with workspace complexity.

Reporting/analytics: broad dashboards and goals. Engineering-specific analytics require configuration.

Notifications: extensive and configurable; noise can be significant.

Automation: broad and approachable, but rule sprawl is possible.

What users love:

- Feature completeness.
- Docs/tasks/whiteboards together.
- Customization.
- Dashboards and automations.

What users hate:

- Complexity.
- Performance issues.
- Product sprawl.
- Constant surface-area expansion.

Technical and architectural limitations:

- All-in-one ambition increases UX and architectural complexity.
- Generic objects and views can weaken domain-specific clarity.
- AI can become broad summarization instead of targeted execution help.

Qeetro differentiation opportunity: offer integrated context without becoming an "everything app." Keep the execution loop intentionally constrained.

### Plane

Product philosophy: open-source, modern project management for software teams. Plane aims to be a lightweight, self-hostable alternative to heavier PM suites.

UX philosophy: clean, software-team focused, with projects, work items, cycles, modules, views, and pages.

Information architecture:

- Workspace -> projects -> work items.
- Cycles, modules, views, pages, intake, and analytics organize execution.

Collaboration model: comments, pages, mentions, issue activity, assignments, and integrations.

Workflows: work items, states, cycles, modules, intake, views, estimates, labels, and pages.

Performance characteristics: generally leaner than large enterprise tools, but maturity and hosted/self-hosted deployment quality matter.

AI capabilities: Plane has been adding AI-facing capabilities and modern dev integrations, but it is not yet the market's strongest AI-native execution system.

Extensibility: open-source codebase, APIs, webhooks/integrations depending on edition, and self-hosting.

Customization: moderate. More opinionated than monday/ClickUp, less mature than Jira.

Scalability: promising for startups and self-hosting, but large-enterprise maturity is still behind Atlassian/GitHub/Asana.

Developer experience: strong for teams that value open-source, self-hosting, and code-level extensibility.

Onboarding: approachable for software teams.

User pain points:

- Maturity compared with incumbents.
- Enterprise and integration depth may lag.
- Open-core boundaries can matter for self-hosting teams.

Enterprise readiness: improving, but not Jira/GitHub-class in broad enterprise trust.

Realtime: expected collaborative updates, but not a primary differentiated perception.

Reporting/analytics: basic to moderate project analytics; less mature than Jira/Asana/monday.

Notifications: standard product notifications; ecosystem depth is smaller.

Automation: less extensive than Jira/monday/ClickUp.

What users love:

- Open-source orientation.
- Clean software-team primitives.
- Self-hosting path.
- Simpler than Jira.

What users hate:

- Missing mature enterprise features.
- Fewer integrations.
- Less battle-tested at very large scale.

Technical and architectural limitations:

- Smaller ecosystem.
- Product maturity risk.
- Enterprise governance and analytics need depth.

Qeetro differentiation opportunity: take the open, developer-friendly spirit, but plan enterprise-grade architecture and AI workflows from day one.

### Notion

Product philosophy: flexible connected workspace for knowledge, docs, databases, and lightweight project management.

UX philosophy: everything is a block. Users compose pages, databases, views, relations, templates, and now AI into custom workspaces.

Information architecture:

- Workspace -> pages -> blocks.
- Databases with properties, relations, rollups, views, templates, and automations.
- Projects/tasks are templates over databases rather than rigid product primitives.

Collaboration model: realtime docs, comments, mentions, page sharing, wikis, databases, and AI knowledge retrieval.

Workflows: docs, tasks, projects, timelines, calendars, databases, dependencies through relations, automations, and templates.

Performance characteristics: excellent for docs and moderate databases; heavy databases and complex relation/rollup systems can feel slow.

AI capabilities: Notion AI, AI connectors, enterprise search, writing assistance, Q&A, summarization, and emerging agent workflows.

Extensibility: API, database automations, integrations, webhooks via ecosystem tools, templates.

Customization: extremely high at the workspace/template level, but often user-built rather than product-enforced.

Scalability: strong for knowledge management; weaker for strict enterprise project execution unless heavily curated.

Developer experience: good API and docs, but not developer-native issue/PR flow.

Onboarding: easy for docs; hard for well-modeled project systems because users must understand databases, relations, and templates.

User pain points:

- Project management can become DIY.
- Permissions at scale can be confusing.
- Heavy databases and offline/mobile limitations are common complaints.
- Lack of strict workflow semantics.

Enterprise readiness: strong enterprise features around admin, security, SSO, audit, compliance, and knowledge governance.

Realtime: excellent collaborative docs experience.

Reporting/analytics: flexible database views, but weak native agile analytics.

Notifications: comments, mentions, reminders, page updates; less execution-oriented than Jira/Linear.

Automation: database automations and integrations; less robust than Jira/monday for complex workflows.

What users love:

- Docs and structured data together.
- Flexibility.
- Collaborative knowledge base.
- AI over workspace context.

What users hate:

- DIY project-system tax.
- Performance at database scale.
- Permission complexity.
- Weak agile/reporting semantics.

Technical and architectural limitations:

- Block/database abstraction is flexible but not execution-specific.
- Rich context can lack normalized domain semantics for AI planning.
- Reporting depends on user-built data quality.

Qeetro differentiation opportunity: make execution structured by default while allowing Notion-like context capture where it improves decisions.

### Trello

Product philosophy: simple visual Kanban. Trello optimizes for immediate comprehension and lightweight collaboration.

UX philosophy: board/list/card simplicity. Users should understand it in minutes.

Information architecture:

- Workspace -> boards -> lists -> cards -> checklists/attachments/custom fields.
- Power-Ups and Butler automation extend the core.

Collaboration model: card comments, members, mentions, checklists, attachments, due dates, labels, and notifications.

Workflows: list-based Kanban, checklists, card movement, labels, due dates, custom fields, Butler automation, Power-Ups.

Performance characteristics: fast and simple for small boards; large boards become hard to navigate and reason about.

AI capabilities: Atlassian ecosystem AI can assist adjacent workflows, but Trello is not perceived as an AI-native planning product.

Extensibility: Power-Ups, Butler, API, and Atlassian integrations.

Customization: lightweight. Good enough for simple workflows, insufficient for complex agile/portfolio needs.

Scalability: excellent for individuals/small teams; weak for enterprise project execution without external tooling.

Developer experience: usable API and GitHub Power-Ups, but not developer-first.

Onboarding: excellent. This remains Trello's enduring strength.

User pain points:

- Weak dependencies, reporting, and hierarchy.
- Large boards become cluttered.
- Hard to scale from team board to portfolio planning.
- Limited structured workflow semantics.

Enterprise readiness: enterprise offering exists, but product model is less enterprise-execution focused than Jira/Asana.

Realtime: simple collaborative board updates.

Reporting/analytics: limited without Power-Ups.

Notifications: card/watch/mention/date-driven notifications; can be noisy but easy to understand.

Automation: Butler is approachable for card/list automation, but limited compared with Jira/monday.

What users love:

- Simplicity.
- Visual boards.
- Fast onboarding.
- Low ceremony.

What users hate:

- Outgrowing it quickly.
- Weak reporting.
- Weak hierarchy and dependencies.
- Board clutter.

Technical and architectural limitations:

- Board/list/card model is too shallow for complex software delivery.
- Reporting and roadmapping depend on add-ons.
- AI has limited structured context to operate on.

Qeetro differentiation opportunity: preserve Trello's immediate visual clarity while supporting serious hierarchy, reporting, permissions, and AI execution.

## Market Gaps

1. Jira power without Jira ceremony.
2. Linear speed without Linear customization ceilings.
3. Notion context without DIY project-management templates.
4. GitHub proximity without PM feature gaps.
5. monday/ClickUp flexibility without workspace sprawl.
6. Trello simplicity that graduates into enterprise execution.
7. AI that does execution reasoning, not just summarization.
8. Configurable workflows that remain typed, versioned, auditable, and analyzable.
9. Project management that treats developer workflow, product context, and delivery analytics as one loop.
10. Self-host or data-control optionality without sacrificing SaaS polish later.

# 2. Product Strategy

### Vision

qeetro is the AI-native execution system where software teams turn product intent into shipped work with speed, context, and operational clarity.

### Mission

Help modern engineering and product organizations plan, coordinate, execute, learn, and automate work without drowning in process.

### Target Audience

- Seed to growth-stage software startups.
- Product engineering teams at SaaS companies.
- Agile teams that need more structure than Trello/GitHub Projects but less ceremony than Jira.
- Developer-led product teams that value speed and context.
- Engineering organizations that want AI assistance but still need human control, auditability, and predictable delivery.

### Ideal Customer Profile

- 10 to 250 employees.
- 5 to 100 engineers.
- Uses GitHub/GitLab, Slack/Teams, cloud CI, and modern SaaS tooling.
- Has outgrown Trello/Notion/GitHub Projects or is frustrated with Jira/ClickUp overhead.
- Needs projects, issues, sprints/cycles, epics, roadmaps, dependencies, notifications, reporting, and integrations.
- Wants AI help for triage, planning, summarization, risk detection, and backlog hygiene.

### Primary Use Cases

- Product backlog management.
- Engineering issue tracking.
- Sprint/cycle planning.
- Project and epic planning.
- Roadmap visibility.
- Cross-functional collaboration.
- AI-assisted issue creation, grooming, triage, and risk detection.
- Developer workflow integration with GitHub/GitLab.
- Delivery reporting and health analytics.
- Notifications and stakeholder updates.

### Positioning

`qeetro` is the fast, AI-native project execution platform for software teams that want Jira's structure, Linear's speed, Notion's context, and GitHub's developer friendliness without inheriting their worst tradeoffs.

# 3. Product Philosophy

## Product Philosophy

- Opinionated core, configurable edges.
- Fast by default.
- Every workflow object should have clear ownership.
- Context should be close to work, but work should remain structured.
- AI should accelerate judgment, not replace accountability.
- Enterprise readiness starts with auditability and permission boundaries, not a premature microservice platform.

## UX Philosophy

- First screen should be the execution workspace, not marketing-style chrome.
- Navigation should be stable: workspace, project, team, issue, board, roadmap, inbox.
- Common actions should be keyboard-friendly and optimistic.
- Complex configuration should be progressive, not front-loaded.
- UI density should support repeated daily work.
- Realtime collaboration should feel natural but not visually noisy.
- Dashboards should explain delivery health, not just display charts.

## Engineering Philosophy

- Modular monolith first.
- Domain events from day one.
- Strong boundaries inside one deployable before service extraction.
- Typed contracts shared through packages.
- Database schema should model business reality, not UI accidents.
- Make eventual extraction cheap by isolating domain logic, event contracts, and data ownership.
- Prefer boring infrastructure until usage proves a need.

## Scalability Philosophy

- Scale the product model before scaling the infrastructure.
- Use PostgreSQL well: indexing, partitioning when needed, query review, and tenant-aware data access.
- Use Redis for cache, ephemeral coordination, rate limiting, BullMQ, and websocket fanout.
- Add search infrastructure only after Postgres full-text search becomes limiting.
- Add Kubernetes only after deployment complexity requires it.

## AI Philosophy

- AI is a domain module, not a feature sprinkle.
- AI must have explicit tools, permissions, audit trails, and human confirmation for destructive actions.
- AI context should come from typed project data, comments, docs, activity, integrations, and search.
- AI outputs should be explainable: source-linked, confidence-aware, and reversible.
- Start with assistive workflows: summarize, triage, refine, split, estimate, detect duplicates, identify blockers, draft updates.
- Defer autonomous agents until the platform has high-quality events, permissions, and audit logs.

## Modular Architecture Philosophy

- Every domain owns its entities, commands, queries, policies, and emitted events.
- Cross-domain reads are allowed through query services; cross-domain writes happen through application services or events.
- Shared packages contain types, utilities, UI primitives, and event contracts, not hidden business logic.
- Future service extraction candidates must have stable APIs, stable events, and minimal synchronous dependencies.

## What qeetro Should Be

- Fast enough for daily developer use.
- Structured enough for serious engineering delivery.
- Collaborative enough for product, design, engineering, and leadership.
- AI-native enough to reduce planning and grooming work.
- Opinionated enough to prevent chaos.
- Flexible enough to support real organizations.
- Observable, auditable, and secure from the beginning.
- Built as a modular monolith that can evolve into services selectively.

## What qeetro Should Not Be

- A Jira clone with a prettier skin.
- A generic no-code database.
- A docs app pretending to be a PM system.
- An "everything app" with chat, docs, whiteboards, CRM, HR, and finance mixed together.
- A premature Kubernetes/microservices showcase.
- A tool that hides critical project decisions inside opaque AI.
- A tool that requires administrators to become schema engineers before teams can work.

## Core Principles

1. Speed is a feature.
2. Structure beats sprawl.
3. Configuration must be typed, versioned, and reversible.
4. AI needs permissions, provenance, and auditability.
5. Work should flow from intent to issue to code to release to learning.
6. Defaults should serve software teams first.
7. Enterprise needs begin with identity, authorization, audit logs, and observability.
8. Realtime is for confidence, not animation.
9. Reporting should be derived from events, not manually maintained.
10. Service extraction should follow domain pressure, not architectural fashion.

## Constraints

Product constraints:

- MVP must focus on software project execution, not every work-management category.
- Workflow customization should be constrained until core issue/project semantics are strong.
- AI should not block core platform usefulness.
- The first release should be excellent for a focused team before serving complex enterprises.

Technical constraints:

- PostgreSQL is the source of truth.
- Redis is non-durable support infrastructure, not primary storage.
- BullMQ handles background work, event projection, notification dispatch, integration sync, and AI jobs.
- WebSockets are scoped to live workspace/project/issue collaboration.
- Outbox pattern is required before serious integrations and analytics.

Scalability constraints:

- Every tenant-scoped table must include `organization_id` or a clear parent path to it.
- High-cardinality activity/event data needs retention and archival strategy.
- Search and analytics should not overload transactional queries.
- File handling must use object storage abstractions, not local disk.
- AI context retrieval must have token, latency, and permission budgets.
