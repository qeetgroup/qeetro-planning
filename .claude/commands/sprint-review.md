---
description: End-of-sprint helper — tally outcomes, close the milestone, generate retro notes, and tee up the next sprint.
argument-hint: "[sprint-number]   # optional; defaults to the sprint that just ended"
---

Run an end-of-sprint review for qeetro. Use this on or after the sprint end date.

## Step 1 — Confirm the sprint being reviewed

Default to the most recently ended sprint (whose end date is in the past). If `$ARGUMENTS` is provided, use that. State the sprint number, milestone, and date window. Wait for confirmation if today's date is more than 2 days before the sprint end (avoid prematurely closing an active sprint).

## Step 2 — Pull final state

Same data sources as `/sprint-status`. Report:

- Issues planned at sprint start (from `docs/planning/sprint-<N>-checklist.md` or the catalog's Sprint N entries).
- Issues actually completed (closed not-as-not-planned).
- Issues carried over (still open, still in this milestone).
- Issues descoped (closed as won't-do or moved out of the milestone).
- Unplanned issues that landed (closed within the sprint window but not in the original plan).
- Merged PRs in the window with their linked issues.

## Step 3 — Update the planning checklist

In `docs/planning/sprint-<N>-checklist.md`, tick every completed item and add notes for carryovers/descopes. If the checklist doesn't exist (early sprints didn't all have one), generate one retroactively from the catalog before annotating.

## Step 4 — Generate retro notes

Create or append to `docs/planning/sprint-<N>-retro.md` using this skeleton (do **not** invent feelings — write only what you can derive from the data):

```md
# Sprint <N> Retro — M<N> <title>

Window: <start> to <end>
Working days: 10

## Delivery facts
- Planned: <n>
- Completed: <n>
- Carryover: <n>
- Descoped: <n>
- Unplanned landed: <n>
- Completion rate: <%>

## Velocity by Size
- XS:  planned <p>  done <d>
- S:   planned <p>  done <d>
- M:   planned <p>  done <d>
- L:   planned <p>  done <d>
- XL:  planned <p>  done <d>

## Observations from the data
- <e.g. "All Database-domain work shipped on time; Frontend slipped 2 days">
- <e.g. "Outbox (EVT-001) blocked 3 downstream issues for 4 days">

## Carryover plan
| ID | Title | Why it slipped (best inference from PRs/comments) | Action |
|---|---|---|---|

## Decisions captured this sprint
- Link to any ADRs added or amended during the sprint.

## Open questions for the next planning session
- <items the data doesn't answer that the user should think about>
```

## Step 5 — Close the milestone (with confirmation)

If completion looks reasonable and the user agrees:

```bash
gh api repos/qeetgroup/qeetro/milestones/<id> --method PATCH -f state=closed
```

Otherwise leave it open and note in the retro why.

## Step 6 — Archive completed items in the project

For items with Status = Done in this milestone older than 30 days, archive them via the project Workflows UI (the planning doc's automation rule already handles this if enabled).

## Step 7 — Hand off to `/plan-next-sprint`

End by telling the user:

> "Sprint <N> retro is at `docs/planning/sprint-<N>-retro.md`. Carryover items: <n>. To plan Sprint <N+1>, run `/plan-next-sprint`."

## Guardrails

- Do not close the milestone if any open issue inside it is not explicitly decided (carry forward, descope, or finish).
- Do not delete or rename completed issue branches.
- Velocity numbers are descriptive only — never use them to silently rescope the catalog. Adjustments to scope require an ADR.
