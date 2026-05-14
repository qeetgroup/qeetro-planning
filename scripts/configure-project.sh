#!/usr/bin/env bash
# Configure the @qeetro roadmap GitHub Project to the enterprise spec
# defined in docs/planning/03-github-project-setup.md.
#
# Idempotent: re-running adds anything missing without disturbing what is correct.
set -euo pipefail

ORG="qeetgroup"
PROJECT_NUMBER=23
PROJECT_ID="PVT_kwDOC6jnIs4BXqsU"

graphql() {
  gh api graphql -f query="$1" "${@:2}"
}

field_exists() {
  local name="$1"
  gh project field-list "$PROJECT_NUMBER" --owner "$ORG" --limit 100 --format json \
    | python3 -c "import json,sys; print(any(f['name']==sys.argv[1] for f in json.load(sys.stdin)['fields']))" "$name"
}

field_id() {
  local name="$1"
  gh project field-list "$PROJECT_NUMBER" --owner "$ORG" --limit 100 --format json \
    | python3 -c "import json,sys
d=json.load(sys.stdin)['fields']
m=[f for f in d if f['name']==sys.argv[1]]
print(m[0]['id'] if m else '')" "$name"
}

create_single_select() {
  local name="$1"; shift
  local opts_json="$1"; shift   # JSON array of {"name":"...","color":"...","description":"..."}

  if [ "$(field_exists "$name")" = "True" ]; then
    echo "field-exists  $name"
    return 0
  fi

  graphql 'mutation($projectId:ID!, $name:String!, $opts:[ProjectV2SingleSelectFieldOptionInput!]!) {
    createProjectV2Field(input:{
      projectId:$projectId,
      dataType: SINGLE_SELECT,
      name:$name,
      singleSelectOptions:$opts
    }) { projectV2Field { ... on ProjectV2SingleSelectField { id name } } }
  }' \
    -f projectId="$PROJECT_ID" \
    -f name="$name" \
    -f opts="$opts_json" \
    --jq '.data.createProjectV2Field.projectV2Field.name' >/dev/null \
    && echo "created       $name" \
    || echo "FAILED        $name"
}

create_text_field() {
  local name="$1"
  if [ "$(field_exists "$name")" = "True" ]; then
    echo "field-exists  $name"
    return 0
  fi
  graphql 'mutation($projectId:ID!, $name:String!) {
    createProjectV2Field(input:{projectId:$projectId, dataType: TEXT, name:$name}) {
      projectV2Field { ... on ProjectV2Field { id name } }
    }
  }' -f projectId="$PROJECT_ID" -f name="$name" \
    --jq '.data.createProjectV2Field.projectV2Field.name' >/dev/null \
    && echo "created       $name" \
    || echo "FAILED        $name"
}

echo "=== Phase 1: missing fields ==="

# Issue Type
create_single_select "Issue Type" '[
  {"name":"Epic","color":"PURPLE","description":"Top-level epic"},
  {"name":"Feature","color":"BLUE","description":"Feature group inside an epic"},
  {"name":"Story","color":"GREEN","description":"User-visible behavior unit"},
  {"name":"Task","color":"GRAY","description":"Technical task"},
  {"name":"Bug","color":"RED","description":"Defect or regression"},
  {"name":"Spike","color":"YELLOW","description":"Time-boxed investigation"},
  {"name":"Enhancement","color":"PINK","description":"Incremental improvement"}
]'

# Domain (28 values from planning doc §9)
create_single_select "Domain" '[
  {"name":"Auth","color":"GRAY","description":""},
  {"name":"Identity","color":"GRAY","description":""},
  {"name":"Organizations","color":"GRAY","description":""},
  {"name":"Permissions","color":"GRAY","description":""},
  {"name":"Workspaces","color":"GRAY","description":""},
  {"name":"Teams","color":"GRAY","description":""},
  {"name":"Projects","color":"GRAY","description":""},
  {"name":"Issues","color":"GRAY","description":""},
  {"name":"Boards","color":"GRAY","description":""},
  {"name":"Backlog","color":"GRAY","description":""},
  {"name":"Sprints","color":"GRAY","description":""},
  {"name":"Epics","color":"GRAY","description":""},
  {"name":"Comments","color":"GRAY","description":""},
  {"name":"Activity","color":"GRAY","description":""},
  {"name":"Notifications","color":"GRAY","description":""},
  {"name":"Realtime","color":"GRAY","description":""},
  {"name":"Search","color":"GRAY","description":""},
  {"name":"Files","color":"GRAY","description":""},
  {"name":"Analytics","color":"GRAY","description":""},
  {"name":"Automation","color":"GRAY","description":""},
  {"name":"Integrations","color":"GRAY","description":""},
  {"name":"AI","color":"PURPLE","description":""},
  {"name":"Audit","color":"GRAY","description":""},
  {"name":"Infrastructure","color":"BLUE","description":""},
  {"name":"Frontend","color":"BLUE","description":""},
  {"name":"Backend","color":"BLUE","description":""},
  {"name":"Database","color":"GREEN","description":""},
  {"name":"DevOps","color":"ORANGE","description":""},
  {"name":"Testing","color":"YELLOW","description":""},
  {"name":"Observability","color":"PINK","description":""}
]'

# Release
create_single_select "Release" '[
  {"name":"Phase 0","color":"GRAY","description":"Planning and setup"},
  {"name":"MVP","color":"RED","description":"MVP release scope"},
  {"name":"Beta","color":"ORANGE","description":"Beta hardening"},
  {"name":"v1","color":"BLUE","description":"v1 launch"},
  {"name":"v2","color":"PURPLE","description":"v2 expansion"},
  {"name":"Future","color":"GRAY","description":"Backlog beyond v2"}
]'

# Risk
create_single_select "Risk" '[
  {"name":"None","color":"GRAY","description":""},
  {"name":"Low","color":"GREEN","description":""},
  {"name":"Medium","color":"YELLOW","description":""},
  {"name":"High","color":"RED","description":""}
]'

# Blocked By (text)
create_text_field "Blocked By"

echo
echo "=== Phase 2: augment existing single-select options ==="

add_options() {
  local field_id="$1"; shift
  local opts_json="$1"; shift
  graphql 'mutation($fieldId:ID!, $options:[ProjectV2SingleSelectFieldOptionInput!]!) {
    updateProjectV2Field(input:{fieldId:$fieldId, singleSelectOptions:$options}) {
      projectV2Field { ... on ProjectV2SingleSelectField { id name } }
    }
  }' -f fieldId="$field_id" -f options="$opts_json" \
    --jq '.data.updateProjectV2Field.projectV2Field.name' >/dev/null \
    && echo "options-updated  $(graphql_field_name "$field_id")" \
    || echo "FAILED options for fieldId=$field_id"
}

graphql_field_name() {
  local fid="$1"
  graphql 'query($id:ID!) { node(id:$id) { ... on ProjectV2SingleSelectField { name } } }' -f id="$fid" --jq '.data.node.name'
}

STATUS_FID="$(field_id 'Status')"
PRIORITY_FID="$(field_id 'Priority')"
TEAM_FID="$(field_id 'Team')"

# Status: ensure Triage, Ready, In Progress, In Review, Blocked, Done, Won't Do exist
add_options "$STATUS_FID" '[
  {"name":"Triage","color":"GRAY","description":"Needs shaping"},
  {"name":"Ready","color":"BLUE","description":"Ready for implementation"},
  {"name":"In Progress","color":"YELLOW","description":"Actively being worked"},
  {"name":"In Review","color":"PURPLE","description":"PR or design review"},
  {"name":"Blocked","color":"RED","description":"Cannot proceed"},
  {"name":"Done","color":"GREEN","description":"Completed"},
  {"name":"Won'\''t Do","color":"GRAY","description":"Explicitly rejected or deferred"}
]'

# Priority: replace P0/P1/P2 with named labels per planning doc
add_options "$PRIORITY_FID" '[
  {"name":"Critical","color":"RED","description":"Must complete this sprint"},
  {"name":"High","color":"ORANGE","description":"Should complete this sprint"},
  {"name":"Medium","color":"YELLOW","description":"Plan but can slip"},
  {"name":"Low","color":"GREEN","description":"Nice to have"}
]'

# Team: align with planning doc §9 (Platform, Product Core, Frontend, AI/Automation, Integrations)
add_options "$TEAM_FID" '[
  {"name":"Platform","color":"BLUE","description":"Infra, DB, observability, CI/CD"},
  {"name":"Product Core","color":"GREEN","description":"Auth, identity, work core"},
  {"name":"Frontend","color":"PURPLE","description":"Web app, UI"},
  {"name":"AI/Automation","color":"YELLOW","description":"AI assistant and automation"},
  {"name":"Integrations","color":"ORANGE","description":"GitHub, Slack, public API"}
]'

echo
echo "Phase 1-2 complete."
echo "Run phase 3 (iteration dates) and phase 4 (set values) separately to keep operations reviewable."
