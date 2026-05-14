---
description: Audit a proposed change or branch against qeetro's architectural lock-ins from the planning blueprint.
argument-hint: "[path or branch]   # optional; defaults to the current working tree"
---

Audit qeetro code (current diff, a branch, or a specific path) against the 8 non-negotiable architectural lock-ins. **Read-only.**

## What to check

For every file in scope, look for violations of these rules (sourced from [04-issue-catalog.md §15](docs/planning/04-issue-catalog.md) and [02-architecture-blueprint.md §6](docs/planning/02-architecture-blueprint.md)):

1. **`organization_id` on every tenant-owned table.**
   - In Prisma schemas: every model that represents tenant data has an `organizationId String` field with a relation or `@@index`.
   - Exceptions allowed only for: `organizations`, `users` (pre-tenant identity), and clearly global tables — document the exception inline.

2. **Outbox precedes side-effect work.**
   - Any code that emits a domain event (`activity.*`, `notification.*`, `realtime.*`, `automation.*`, `ai.*`, `integration.*`) must go through `packages/event-contracts` and the outbox dispatcher. Direct `eventEmitter.emit()` calls inside HTTP handlers or repositories are violations.

3. **Permission-filtered presentation events for realtime.**
   - WebSocket gateways must not forward raw domain events. They subscribe to the outbox, map to presentation event shapes, and check `PolicyService` per recipient.
   - Grep for `socket.broadcast` or `io.emit` calls that pass raw event payloads.

4. **Versioned event contracts.**
   - Event names in `packages/event-contracts` follow `<domain>.<event>.v<N>` and have zod schemas.
   - No unversioned event names anywhere in source.

5. **Central `PolicyService` for authorization.**
   - NestJS modules use the shared guard/decorator from `packages/permissions`. No hand-rolled `if (user.role === ...)` checks inside controllers or services.

6. **No `process.env` reads outside `packages/config`.**
   - Grep for `process.env\.` in any file outside `packages/config/**` (allowed exceptions: `next.config.ts`, `vitest.config.ts`, `playwright.config.ts`).

7. **Apps must not import other apps. Packages must not import apps. `packages/domain` must not import Prisma/Nest/React.**
   - Run the ESLint boundary rule from PF-002. Report any new violations not in the baseline.

8. **`apps/api` domain modules must not import each other's repositories.**
   - Inside `apps/api/src/modules/<domain>`, imports from other modules' `infrastructure/` or `*.repository.ts` are violations. Cross-module work goes via application services or domain events.

## How to run

1. If `$ARGUMENTS` is empty, audit the working tree diff vs `develop`.
2. If `$ARGUMENTS` is a branch name, `git diff develop...<branch>`.
3. If `$ARGUMENTS` is a path, audit files under that path.

Use grep, AST scans (`ts-morph` if available, else regex), and the Prisma schema as data sources.

## Output

Group findings by rule. Each finding:

```
RULE 6: process.env read outside packages/config
  apps/api/src/modules/auth/auth.service.ts:42
  apps/api/src/main.ts:18
  Fix: read via loadConfig() from @qeetro/config (PF-011).
```

End with a verdict:

- **PASS** — no violations of any rule.
- **PASS with notes** — only soft concerns (e.g. acceptable exceptions but worth flagging).
- **FAIL** — at least one hard violation; list the blocking issues that must be fixed before merge.

Do **not** auto-fix. Report only. The maintainer will decide whether to fix in-place, file a follow-up issue, or amend the relevant ADR.
