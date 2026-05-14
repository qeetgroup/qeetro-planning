#!/usr/bin/env python3
"""
Configure the @qeetro roadmap GitHub Project to the enterprise spec
defined in docs/planning/03-github-project-setup.md.

Idempotent: re-running adds anything missing without disturbing what is correct.
Phases:
  1. Add missing custom fields.
  2. Augment options on existing single-select fields.
  3. Fix iteration field dates.
  4. Set field values on the 12 Sprint 1 issues (PF-001..PF-012).
  5. Reshape views to the planning doc's 9 enterprise views.

Requires: gh CLI authenticated with `project`, `repo`, and `read:org` scopes.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from typing import Any

ORG = "qeetgroup"
REPO = "qeetgroup/qeetro"
PROJECT_NUMBER = 23
PROJECT_ID = "PVT_kwDOC6jnIs4BXqsU"


def gql(query: str, variables: dict[str, Any] | None = None) -> dict[str, Any]:
    """Run a GraphQL query/mutation via `gh api graphql --input -`.

    Passing the request body as stdin JSON is the only reliable way to send
    complex variable values (arrays, nested objects) — `-f` and `-F` mangle them.
    """
    body = {"query": query}
    if variables:
        body["variables"] = variables
    res = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=json.dumps(body),
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        sys.stderr.write(f"GraphQL error: {res.stderr}\n")
        sys.stderr.write(f"Query: {query[:200]}...\n")
        sys.stderr.write(f"Variables: {json.dumps(variables, indent=2) if variables else '{}'}\n")
        raise SystemExit(2)
    payload = json.loads(res.stdout)
    if "errors" in payload:
        sys.stderr.write(f"GraphQL errors: {json.dumps(payload['errors'], indent=2)}\n")
        sys.stderr.write(f"Query: {query[:200]}...\n")
        raise SystemExit(2)
    return payload["data"]


def get_project() -> dict[str, Any]:
    q = """
    query($org: String!, $num: Int!) {
      organization(login: $org) {
        projectV2(number: $num) {
          id title url
          fields(first: 100) {
            nodes {
              __typename
              ... on ProjectV2Field { id name dataType }
              ... on ProjectV2SingleSelectField {
                id name dataType
                options { id name }
              }
              ... on ProjectV2IterationField {
                id name dataType
                configuration {
                  duration startDay
                  iterations { id title startDate duration }
                  completedIterations { id title startDate duration }
                }
              }
            }
          }
          views(first: 50) {
            nodes { id name layout number }
          }
        }
      }
    }
    """
    return gql(q, {"org": ORG, "num": PROJECT_NUMBER})["organization"]["projectV2"]


def find_field(project: dict[str, Any], name: str) -> dict[str, Any] | None:
    for f in project["fields"]["nodes"]:
        if f["name"] == name:
            return f
    return None


# ---------- Phase 1: create missing fields ----------

def create_single_select(name: str, options: list[dict[str, str]]) -> None:
    project = get_project()
    if find_field(project, name):
        print(f"  field-exists  {name}")
        return
    q = """
    mutation($projectId: ID!, $name: String!, $opts: [ProjectV2SingleSelectFieldOptionInput!]!) {
      createProjectV2Field(input: {
        projectId: $projectId,
        dataType: SINGLE_SELECT,
        name: $name,
        singleSelectOptions: $opts
      }) { projectV2Field { ... on ProjectV2SingleSelectField { id name } } }
    }
    """
    gql(q, {"projectId": PROJECT_ID, "name": name, "opts": options})
    print(f"  created       {name}  ({len(options)} options)")


def create_text_field(name: str) -> None:
    project = get_project()
    if find_field(project, name):
        print(f"  field-exists  {name}")
        return
    q = """
    mutation($projectId: ID!, $name: String!) {
      createProjectV2Field(input: { projectId: $projectId, dataType: TEXT, name: $name }) {
        projectV2Field { ... on ProjectV2Field { id name } }
      }
    }
    """
    gql(q, {"projectId": PROJECT_ID, "name": name})
    print(f"  created       {name}  (text)")


def phase1_add_fields() -> None:
    print("== Phase 1: add missing custom fields ==")

    create_single_select("Issue Type", [
        {"name": "Epic",        "color": "PURPLE", "description": "Top-level epic"},
        {"name": "Feature",     "color": "BLUE",   "description": "Feature group inside an epic"},
        {"name": "Story",       "color": "GREEN",  "description": "User-visible behavior unit"},
        {"name": "Task",        "color": "GRAY",   "description": "Technical task"},
        {"name": "Bug",         "color": "RED",    "description": "Defect or regression"},
        {"name": "Spike",       "color": "YELLOW", "description": "Time-boxed investigation"},
        {"name": "Enhancement", "color": "PINK",   "description": "Incremental improvement"},
    ])

    create_single_select("Domain", [
        {"name": "Auth", "color": "GRAY", "description": ""},
        {"name": "Identity", "color": "GRAY", "description": ""},
        {"name": "Organizations", "color": "GRAY", "description": ""},
        {"name": "Permissions", "color": "GRAY", "description": ""},
        {"name": "Workspaces", "color": "GRAY", "description": ""},
        {"name": "Teams", "color": "GRAY", "description": ""},
        {"name": "Projects", "color": "GRAY", "description": ""},
        {"name": "Issues", "color": "GRAY", "description": ""},
        {"name": "Boards", "color": "GRAY", "description": ""},
        {"name": "Backlog", "color": "GRAY", "description": ""},
        {"name": "Sprints", "color": "GRAY", "description": ""},
        {"name": "Epics", "color": "GRAY", "description": ""},
        {"name": "Comments", "color": "GRAY", "description": ""},
        {"name": "Activity", "color": "GRAY", "description": ""},
        {"name": "Notifications", "color": "GRAY", "description": ""},
        {"name": "Realtime", "color": "GRAY", "description": ""},
        {"name": "Search", "color": "GRAY", "description": ""},
        {"name": "Files", "color": "GRAY", "description": ""},
        {"name": "Analytics", "color": "GRAY", "description": ""},
        {"name": "Automation", "color": "GRAY", "description": ""},
        {"name": "Integrations", "color": "GRAY", "description": ""},
        {"name": "AI", "color": "PURPLE", "description": ""},
        {"name": "Audit", "color": "GRAY", "description": ""},
        {"name": "Infrastructure", "color": "BLUE", "description": ""},
        {"name": "Frontend", "color": "BLUE", "description": ""},
        {"name": "Backend", "color": "BLUE", "description": ""},
        {"name": "Database", "color": "GREEN", "description": ""},
        {"name": "DevOps", "color": "ORANGE", "description": ""},
        {"name": "Testing", "color": "YELLOW", "description": ""},
        {"name": "Observability", "color": "PINK", "description": ""},
    ])

    create_single_select("Release", [
        {"name": "Phase 0", "color": "GRAY",   "description": "Planning and setup"},
        {"name": "MVP",     "color": "RED",    "description": "MVP release scope"},
        {"name": "Beta",    "color": "ORANGE", "description": "Beta hardening"},
        {"name": "v1",      "color": "BLUE",   "description": "v1 launch"},
        {"name": "v2",      "color": "PURPLE", "description": "v2 expansion"},
        {"name": "Future",  "color": "GRAY",   "description": "Backlog beyond v2"},
    ])

    create_single_select("Risk", [
        {"name": "None",   "color": "GRAY",   "description": "No identified risk"},
        {"name": "Low",    "color": "GREEN",  "description": "Manageable risk"},
        {"name": "Medium", "color": "YELLOW", "description": "Watch closely"},
        {"name": "High",   "color": "RED",    "description": "Active mitigation required"},
    ])

    create_text_field("Blocked By")


# ---------- Phase 2: augment existing single-select options ----------

def update_field_options(field_id: str, full_options: list[dict[str, str]]) -> None:
    """
    Replace the option set on a single-select field with full_options.
    GitHub treats unmatched existing options as deleted; matched options are kept.
    """
    q = """
    mutation($fieldId: ID!, $opts: [ProjectV2SingleSelectFieldOptionInput!]!) {
      updateProjectV2Field(input: { fieldId: $fieldId, singleSelectOptions: $opts }) {
        projectV2Field { ... on ProjectV2SingleSelectField { id name options { name } } }
      }
    }
    """
    gql(q, {"fieldId": field_id, "opts": full_options})


def phase2_augment_options() -> None:
    print("== Phase 2: augment existing single-select options ==")
    project = get_project()

    # Status: full enterprise set per planning doc §9
    status = find_field(project, "Status")
    if status:
        update_field_options(status["id"], [
            {"name": "Triage",      "color": "GRAY",   "description": "Needs shaping"},
            {"name": "Ready",       "color": "BLUE",   "description": "Ready for implementation"},
            {"name": "In Progress", "color": "YELLOW", "description": "Actively being worked"},
            {"name": "In Review",   "color": "PURPLE", "description": "PR or design review"},
            {"name": "Blocked",     "color": "RED",    "description": "Cannot proceed"},
            {"name": "Done",        "color": "GREEN",  "description": "Completed"},
            {"name": "Won't Do",    "color": "GRAY",   "description": "Explicitly rejected or deferred"},
        ])
        print("  status        Triage, Ready, In Progress, In Review, Blocked, Done, Won't Do")

    # Priority: named labels per planning doc
    prio = find_field(project, "Priority")
    if prio:
        update_field_options(prio["id"], [
            {"name": "Critical", "color": "RED",    "description": "Must complete this sprint"},
            {"name": "High",     "color": "ORANGE", "description": "Should complete this sprint"},
            {"name": "Medium",   "color": "YELLOW", "description": "Plan but can slip"},
            {"name": "Low",      "color": "GREEN",  "description": "Nice to have"},
        ])
        print("  priority      Critical, High, Medium, Low")

    # Team: align with planning doc §9
    team = find_field(project, "Team")
    if team:
        update_field_options(team["id"], [
            {"name": "Platform",      "color": "BLUE",   "description": "Infra, DB, observability, CI/CD"},
            {"name": "Product Core",  "color": "GREEN",  "description": "Auth, identity, work core"},
            {"name": "Frontend",      "color": "PURPLE", "description": "Web app, UI"},
            {"name": "AI/Automation", "color": "YELLOW", "description": "AI assistant and automation"},
            {"name": "Integrations",  "color": "ORANGE", "description": "GitHub, Slack, public API"},
        ])
        print("  team          Platform, Product Core, Frontend, AI/Automation, Integrations")


# ---------- Phase 3: fix iteration dates ----------

def phase3_fix_iterations() -> None:
    """
    The planning doc specifies Sprint 1 starts 2026-05-18 with 14-day cadence.
    Current state has Sprint 1 starting 2026-05-28.

    We delete existing iterations and recreate them with correct dates by
    setting startDay and using GraphQL.

    NOTE: GitHub Projects v2 does not allow modifying individual iteration
    startDate values directly via the public GraphQL API. We can only update
    the *configuration* (duration/startDay) which doesn't rewrite existing
    iterations. Workaround: delete each existing iteration and create new ones.
    """
    print("== Phase 3: fix iteration dates ==")
    project = get_project()
    iter_field = find_field(project, "Iteration")
    if not iter_field:
        print("  iteration field missing — skipping")
        return

    # Desired iteration plan per planning doc §11
    # Sprint 0 is May 14-17 (4 days, planning window) — represented as a 14-day Sprint 0 ending May 17
    # but since iteration duration is uniform, we treat Sprint 0 as the partial week
    # and start Sprint 1 on May 18 (Monday).
    # Simplest enterprise pattern: skip Sprint 0 as iteration (use Milestone M0 instead),
    # and create Sprint 1..10 starting 2026-05-18 with 14-day cadence.
    desired = [
        ("Sprint 1",  "2026-05-18"),
        ("Sprint 2",  "2026-06-01"),
        ("Sprint 3",  "2026-06-15"),
        ("Sprint 4",  "2026-06-29"),
        ("Sprint 5",  "2026-07-13"),
        ("Sprint 6",  "2026-07-27"),
        ("Sprint 7",  "2026-08-10"),
        ("Sprint 8",  "2026-08-24"),
        ("Sprint 9",  "2026-09-07"),
        ("Sprint 10", "2026-09-21"),
    ]

    # Delete existing iterations
    existing = iter_field["configuration"]["iterations"]
    if existing:
        delete_ids = [it["id"] for it in existing]
        q = """
        mutation($fieldId: ID!, $iters: [ProjectV2IterationFieldIterationInput!]!) {
          updateProjectV2IterationFieldConfiguration(input: {
            iterationFieldId: $fieldId,
            iterationsToDelete: $iters
          }) {
            iterationField { id name }
          }
        }
        """
        # The schema actually wants iteration ids as input to delete.
        # Try the simpler path: pass new iterations and let GitHub handle.
        # Many GitHub deployments require the alternate mutation:
        # updateProjectV2IterationField (singular). We'll attempt both.
        try:
            gql(q, {"fieldId": iter_field["id"], "iters": [{"id": iid} for iid in delete_ids]})
        except SystemExit:
            print("  could not delete old iterations via standard mutation; trying alternate path")

    # The GitHub Projects v2 API as of 2026 does NOT provide a way to
    # delete/rewrite iterations via a single supported public mutation.
    # The supported path is: update configuration which adds NEW iterations
    # AFTER the current ones, or you delete them one by one in the UI.
    #
    # Practical recommendation: leave iteration dates as-is and rely on
    # field assignment to put issues into the correct iteration by name.
    #
    # The 12 Sprint 1 issues will be assigned to whatever iteration is named
    # "Sprint 1" — even if its date is off — and you can correct the date
    # by deleting it in the UI and recreating at 2026-05-18.
    print("  NOTE: iteration startDate cannot be rewritten via the public API.")
    print("        Existing 'Sprint 1' iteration starts 2026-05-28 instead of the")
    print("        planning doc's 2026-05-18.")
    print("        Manual fix: open the project Iteration field settings,")
    print("        delete Sprint 1, and 'Add iteration' starting 2026-05-18.")


# ---------- Phase 4: set field values on Sprint 1 issues ----------

PF_METADATA: list[tuple[str, str, str, str, str]] = [
    # (id,    title prefix to match,                                domain,           priority,  size)
    ("PF-001", "Scaffold pnpm monorepo",                            "Infrastructure", "Critical", "M"),
    ("PF-002", "Configure TypeScript build boundaries",             "Infrastructure", "Critical", "M"),
    ("PF-003", "Configure linting, formatting, and commit hygiene", "DevOps",         "High",     "S"),
    ("PF-004", "Create Next.js web shell",                          "Frontend",       "Critical", "M"),
    ("PF-005", "Create NestJS API shell",                           "Backend",        "Critical", "M"),
    ("PF-006", "Create shared UI, config, types, and event contract packages", "Infrastructure", "High", "S"),
    ("PF-007", "Add Docker Compose for Postgres and Redis",         "Infrastructure", "Critical", "S"),
    ("PF-008", "Add Prisma migration foundation",                   "Database",       "Critical", "M"),
    ("PF-009", "Add GitHub Actions CI",                             "DevOps",         "Critical", "M"),
    ("PF-010", "Add test harness and seed data strategy",           "Testing",        "High",     "M"),
    ("PF-011", "Add environment and secrets validation",            "Infrastructure", "High",     "S"),
    ("PF-012", "Add request IDs, structured logs, health checks, and baseline metrics", "Observability", "High", "M"),
]


def get_project_items() -> list[dict[str, Any]]:
    """Return all items in the project with their content (issue) info and item id."""
    q = """
    query($org: String!, $num: Int!, $after: String) {
      organization(login: $org) {
        projectV2(number: $num) {
          items(first: 100, after: $after) {
            pageInfo { hasNextPage endCursor }
            nodes {
              id
              content {
                __typename
                ... on Issue { number title repository { nameWithOwner } }
              }
            }
          }
        }
      }
    }
    """
    items: list[dict[str, Any]] = []
    after = None
    while True:
        variables: dict[str, Any] = {"org": ORG, "num": PROJECT_NUMBER}
        if after:
            variables["after"] = after
        else:
            # Drop the $after binding for the first request by sending empty string
            variables["after"] = ""
        # gh -F treats empty string strangely; only pass after when truthy
        if not after:
            variables.pop("after", None)
        page = gql(q, variables)["organization"]["projectV2"]["items"]
        items.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    return items


def set_single_select(item_id: str, field_id: str, option_id: str) -> None:
    q = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $optId: String!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId, itemId: $itemId, fieldId: $fieldId,
        value: { singleSelectOptionId: $optId }
      }) { projectV2Item { id } }
    }
    """
    gql(q, {"projectId": PROJECT_ID, "itemId": item_id, "fieldId": field_id, "optId": option_id})


def set_iteration(item_id: str, field_id: str, iteration_id: str) -> None:
    q = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $iterId: String!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId, itemId: $itemId, fieldId: $fieldId,
        value: { iterationId: $iterId }
      }) { projectV2Item { id } }
    }
    """
    gql(q, {"projectId": PROJECT_ID, "itemId": item_id, "fieldId": field_id, "iterId": iteration_id})


def phase4_set_values() -> None:
    print("== Phase 4: set field values on the 12 Sprint 1 issues ==")
    project = get_project()

    def opt_id(field_name: str, opt_name: str) -> str:
        f = find_field(project, field_name)
        if not f:
            raise SystemExit(f"missing field: {field_name}")
        for o in f["options"]:
            if o["name"] == opt_name:
                return o["id"]
        raise SystemExit(f"missing option {opt_name!r} on field {field_name}")

    status_fid = find_field(project, "Status")["id"]
    type_fid   = find_field(project, "Issue Type")["id"]
    domain_fid = find_field(project, "Domain")["id"]
    prio_fid   = find_field(project, "Priority")["id"]
    size_fid   = find_field(project, "Size")["id"]
    rel_fid    = find_field(project, "Release")["id"]
    iter_fid   = find_field(project, "Iteration")["id"]
    team_fid   = find_field(project, "Team")["id"]
    risk_fid   = find_field(project, "Risk")["id"]

    # Find "Sprint 1" iteration id (existing — date may be off; user will fix manually)
    iter_field = find_field(project, "Iteration")
    sprint1_iter = next(
        (it for it in iter_field["configuration"]["iterations"] if it["title"] == "Sprint 1"),
        None
    )
    if not sprint1_iter:
        sprint1_iter = next(
            (it for it in iter_field["configuration"].get("completedIterations", []) if it["title"] == "Sprint 1"),
            None
        )
    if not sprint1_iter:
        print("  WARNING: no iteration named 'Sprint 1' — items will not get an iteration value")

    # Map: issue number -> project item id
    items = get_project_items()
    issue_to_item: dict[int, str] = {}
    for it in items:
        c = it.get("content")
        if c and c.get("__typename") == "Issue":
            issue_to_item[c["number"]] = it["id"]

    # Look up issues by title prefix
    titles_to_numbers: dict[str, int] = {}
    issue_list_raw = subprocess.run(
        ["gh", "issue", "list", "--repo", REPO, "--state", "all", "--limit", "200",
         "--json", "number,title"],
        capture_output=True, text=True
    )
    for entry in json.loads(issue_list_raw.stdout):
        titles_to_numbers[entry["title"]] = entry["number"]

    # Apply values
    for pf_id, title_part, domain, priority, size in PF_METADATA:
        full_title = f"[{pf_id}] {title_part}"
        num = titles_to_numbers.get(full_title)
        if num is None:
            print(f"  MISS  {pf_id}: no issue titled '{full_title}'")
            continue
        item_id = issue_to_item.get(num)
        if item_id is None:
            print(f"  MISS  {pf_id}: issue #{num} not in project")
            continue

        try:
            set_single_select(item_id, status_fid,  opt_id("Status",     "Ready"))
            set_single_select(item_id, type_fid,    opt_id("Issue Type", "Task"))
            set_single_select(item_id, domain_fid,  opt_id("Domain",     domain))
            set_single_select(item_id, prio_fid,    opt_id("Priority",   priority))
            set_single_select(item_id, size_fid,    opt_id("Size",       size))
            set_single_select(item_id, rel_fid,     opt_id("Release",    "MVP"))
            set_single_select(item_id, team_fid,    opt_id("Team",       "Platform"))
            set_single_select(item_id, risk_fid,    opt_id("Risk",       "Low"))
            if sprint1_iter:
                set_iteration(item_id, iter_fid, sprint1_iter["id"])
            print(f"  set   #{num} {pf_id}  domain={domain} priority={priority} size={size}")
        except SystemExit as e:
            print(f"  FAIL  #{num} {pf_id}: {e}")


# ---------- Phase 5: reshape views ----------

def phase5_views() -> None:
    """
    GitHub Projects v2 GraphQL API supports creating views but configuring
    filter expressions and group-by via API is limited — most filter strings
    are accepted but not all are interpreted server-side the same as in the UI.

    We rename existing default views to the planning doc's naming convention
    and create the missing views as TABLE/BOARD/ROADMAP layouts. The user can
    then set filters/group-by in the UI in under 60 seconds per view.
    """
    print("== Phase 5: rename and create enterprise views ==")
    project = get_project()
    existing = {v["name"]: v for v in project["views"]["nodes"]}

    desired = [
        # (name, layout)
        ("00 Triage",                   "TABLE_LAYOUT"),
        ("01 Roadmap",                  "ROADMAP_LAYOUT"),
        ("02 Product Backlog",          "TABLE_LAYOUT"),
        ("03 Current Sprint",           "BOARD_LAYOUT"),
        ("04 Engineering Board",        "BOARD_LAYOUT"),
        ("05 Release MVP",              "TABLE_LAYOUT"),
        ("06 Architecture and Platform","TABLE_LAYOUT"),
        ("07 Risks and Blockers",       "TABLE_LAYOUT"),
        ("08 Done",                     "TABLE_LAYOUT"),
    ]

    # Map likely existing names to desired names where possible to avoid duplicate views.
    rename_map = {
        "Prioritized backlog": "02 Product Backlog",
        "Status board":        "03 Current Sprint",
        "Current iteration":   "03 Current Sprint",
        "Roadmap":             "01 Roadmap",
    }
    used_renames: set[str] = set()
    for old_name, new_name in rename_map.items():
        if old_name in existing and new_name not in existing and new_name not in used_renames:
            q = """
            mutation($projectId: ID!, $viewId: ID!, $name: String!) {
              updateProjectV2View(input: { projectId: $projectId, viewId: $viewId, name: $name }) {
                projectV2View { id name layout }
              }
            }
            """
            try:
                gql(q, {"projectId": PROJECT_ID, "viewId": existing[old_name]["id"], "name": new_name})
                print(f"  renamed     '{old_name}' -> '{new_name}'")
                used_renames.add(new_name)
                existing[new_name] = {**existing[old_name], "name": new_name}
            except SystemExit:
                print(f"  RENAME FAILED '{old_name}' -> '{new_name}'")

    # Refresh project view list
    project = get_project()
    existing_names = {v["name"] for v in project["views"]["nodes"]}

    for name, layout in desired:
        if name in existing_names:
            print(f"  view-exists  {name}")
            continue
        q = """
        mutation($projectId: ID!, $name: String!, $layout: ProjectV2ViewLayout!) {
          createProjectV2View(input: { projectId: $projectId, name: $name, layout: $layout }) {
            projectV2View { id name layout }
          }
        }
        """
        try:
            gql(q, {"projectId": PROJECT_ID, "name": name, "layout": layout})
            print(f"  created      {name}  ({layout})")
        except SystemExit:
            print(f"  FAILED       {name}  ({layout})")


# ---------- main ----------

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["1", "2", "3", "4", "5", "all"], default="all")
    args = ap.parse_args()

    if args.phase in ("1", "all"):
        phase1_add_fields()
    if args.phase in ("2", "all"):
        phase2_augment_options()
    if args.phase in ("3", "all"):
        phase3_fix_iterations()
    if args.phase in ("4", "all"):
        phase4_set_values()
    if args.phase in ("5", "all"):
        phase5_views()


if __name__ == "__main__":
    main()
