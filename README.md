# AgentCards
Will presented at MICAI 2025 at CHARAL Workshop
```
agent cards for ai agent
agentcard: 1.0
meta:
  name: TaxBot
  version: 0.7.3
  owner: Tax Operations — Data/AI
  last_updated: 2025-10-10
purpose:
  objective: "Assist with personal and business tax queries, document intake, and filing prep with traceable, policy‑compliant outputs"
  users: [Tax Analyst, Accountant, Taxpayer]
interface:
  inputs: [question, PDF, XML, XLSX]
  outputs: [answer, citation_list, filing_checklist, action_proposal]
tools:
  - name: tax_rules_db
    scope: read-only
    eligibility: requires jurisdiction and tax_year
  - name: parse_tax_pdf
    leakage_guard: no final filing decisions
  - name: sat_portal_client
    scope: read-only
    eligibility: authenticated user session
autonomy:
  allowed_actions: [draft_client_email, create_case_ticket]
  requires_approval_for: [submit_return, modify_client_profile]
memory:
  persistent: session_summaries (TTL: 30d)
  pii: masked_at_ingest; encryption_at_rest: AES256
policies:
  deference_gate: gamma=-3.0 until verify+readiness>=tau
  prohibited_content: [store raw IDs, off‑policy advice]
evaluation:
  kpis: {first_response_time_p50: "<30s", hallucination_rate: "<1%", citation_coverage: ">=95%"}
  red_team: [prompt_injection, refund_scam, identity_theft_vector]
ops:
  envs: [dev, staging, prod]
  logging: structured_traces to s3://agent-logs
  rollback: blue/green with canaries
risks:
  - name: pii_leakage
    mitigation: strict scopes + PII scrubbing + DLP scanners

```
