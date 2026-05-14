# .claude/

Project-level Claude Code configuration for qeetro. Anything in this folder is checked into the repo so future sessions (and future engineers) inherit the same workflows.

## Slash commands

Available in any Claude Code session opened in this repo:

| Command | Purpose |
|---|---|
| `/load-context` | Load planning blueprint + ADRs + live sprint state before answering non-trivial questions. Run first when starting a fresh session. |
| `/sprint-status` | Read-only snapshot of the current sprint: completion, blockers, carryover risk. Safe to run any time. |
| `/plan-next-sprint` | End-to-end planning for the next 2-week sprint — pulls catalog, audits current sprint, creates issues + labels + milestone + project field values + checklist. Run at the end of a sprint. |
| `/sprint-review` | End-of-sprint retro generator. Tallies outcomes, produces `docs/planning/sprint-<N>-retro.md`, closes the milestone, hands off to `/plan-next-sprint`. |
| `/architecture-check` | Audit a branch or working tree against the 8 architectural lock-ins. Read-only. Run before merging anything cross-cutting. |

## Typical sprint loop

```
Day 1  → /load-context            # fresh session
       → /sprint-status           # what should I be working on?
       → … implement issues …
Day 5  → /sprint-status           # mid-sprint health check
       → /architecture-check      # before a tricky merge
Day 14 → /sprint-review           # close out
       → /plan-next-sprint        # tee up the next 14 days
```

## What is NOT here

- **Skills** (`.claude/skills/`) — not used yet. Slash commands cover the current workflow.
- **`settings.json`** — intentionally absent. Permission and hook policy are left to each user's local `~/.claude/settings.json`. If the team wants shared permissions later, add `settings.json` (committed) for read-only operations and `settings.local.json` (gitignored) for individual preferences.

## Editing commands

Each file in `commands/` is a Markdown prompt with optional frontmatter (`description`, `argument-hint`). The body is the instruction set Claude follows when the command is invoked. Update them as the project evolves — every command should age forward with the codebase, not just describe a single sprint.
