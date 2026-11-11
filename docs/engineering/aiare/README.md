# AIARE — AI-Assisted Reverse Engineering Research Harness

**RECKLESS ELEMENTS Studio · Version 1.0.0 · 2026-11-11**

**Status:** Published implementation specification and studio-owned test fixture. **No claim is made that the Codex–REA–Ghidra harness has been installed or fully validated on the studio's computer.**

## Documents

1. **[AIARE Research Harness Blueprint v1.0.0](AIARE_RESEARCH_HARNESS_BLUEPRINT_v1.0.0.md)** — architecture, scope, primary-source register, installation runbook, research case format, resource controls, evidence gates, and Unity reuse-first handoff.
2. **[Agent Contract / AGENTS.md Template v1.0.0](AGENTS_TEMPLATE_v1.0.0.md)** — a restrictive contract to install in a future private operational workspace; public template only, not an active agent.
3. **[Installation and Acceptance Test Plan v1.0.0](ACCEPTANCE_TEST_PLAN_v1.0.0.md)** — objective gate matrix (A00–A12), evidence requirements, practical test commands, positive/negative controls, and promotion rules.
4. **[Original C test fixture](fixtures/owned_transform.c)** and **[independent Python verifier](fixtures/verify_transform.py)** — an intentionally tiny self-owned sample for a future blind binary-analysis trial. Do not hand the fixture source or oracle to the investigating agent.

## Version and evidence policy

- **UPSTREAM-DOCUMENTED:** linked evidence was checked in source documentation; does **not** mean tested on our machine.
- **LOCALLY-VERIFIED:** independently exercised against our host and recorded with a check.
- **STUDIO-PROPOSED:** studio design; not an upstream claim or an observed production result.
- **REPORTED:** external project/case-study result not replicated in our environment.
- **BLOCKED / UNKNOWN:** missing proof; never treat as PASS.

## Starting point

1. Preserve any existing local/uncommitted game work and back up Codex configuration.
2. Follow the Blueprint's pinned-source acquisition and the Acceptance Plan's **A00–A04** provider and live-MCP checks.
3. Run the **owned binary pilot** with the hidden verifier in an isolated private workspace, then approve more advanced targets only if independently tested.

Keep original game binaries, asset extractions, commercial code, local evidence stores, credentials, and private IP outside this public repository. This documentation describes authorized research and legitimate reusable systems; it does not license third-party content.

## Research basis

- [awesome-rea](https://github.com/yibie/awesome-rea) — curation, source checking and verification discipline.
- [REA by morluto](https://github.com/morluto/rea) — analysis/MCP interface, provider constraints and structured evidence.
- [DecompPipeline](https://github.com/GeneralAtrox/DecompPipeline) — translator-first, verifier-first, oracle/coverage/mutation architecture.
- [Ghidra](https://github.com/NationalSecurityAgency/ghidra) and [Codex documentation](https://learn.chatgpt.com/docs/developer-commands?surface=cli) — local analysis and MCP integration.

See the Blueprint for pinned revisions, scope limits, compatibility warnings, and distinctions between verified documentation and proposed studio process.
