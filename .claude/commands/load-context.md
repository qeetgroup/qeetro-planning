---
description: Load qeetro's planning blueprint, ADRs, current sprint state, and architectural lock-ins into context.
---

Read the qeetro project context before answering any non-trivial question. Run all of these in parallel:

1. **CLAUDE.md** — repository conventions, sprint cadence, architectural lock-ins, issue ID prefixes.
2. **README.md** — high-level repo intent.
3. **docs/planning/README.md** — index to the blueprint.
4. **docs/adr/** — every accepted ADR (start with `0001-modular-monolith.md`).
5. **docs/planning/sprint-<current>-checklist.md** — if it exists for the sprint covering today's date.

Then quick-look live state:

```bash
# Current open milestones
gh api repos/qeetgroup/qeetro/milestones --jq '.[] | {title, due_on, open_issues, closed_issues}'

# Project field summary
cat <<'EOF' | gh api graphql --input -
{"query":"query{organization(login:\"qeetgroup\"){projectV2(number:23){title url fields(first:100){nodes{... on ProjectV2SingleSelectField{name options{name}} ... on ProjectV2IterationField{name configuration{iterations{title startDate}}}}}}}}"}
EOF

# Recent commits and branches
git log --oneline -20
git branch -a --sort=-committerdate | head -20
```

After loading, output a one-paragraph summary:

> "Loaded qeetro context. Current sprint: Sprint <N> (<window>). Milestone: M<N> <title>. Project: @qeetro roadmap. Branch: <current>. Recently merged: <list>. Open architectural concerns: <count of open Risk:High items>. Ready to answer."

Then wait for the next instruction. Do not begin work.
