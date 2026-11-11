# RECKLESS ELEMENTS — AIARE Research Harness Blueprint

**Version:** 1.0.0  
**Issued:** 2026-11-11  
**Status:** Implementation-ready specification; **not yet installed, integrated, or locally validated**  
**Owner:** THE RECKLESS ELEMENTS — studio engineering  
**Scope:** Research, binary-analysis interoperability, verification, evidence management, and reuse-first game-prototype handoff  
**Companion files:** [Agent contract](AGENTS_TEMPLATE_v1.0.0.md) · [Acceptance tests](ACCEPTANCE_TEST_PLAN_v1.0.0.md) · [Owned test fixture](fixtures/owned_transform.c) · [Fixture verifier](fixtures/verify_transform.py)

> **Purpose.** Convert an original gameplay concept into a verified behavioral specification and then identify the largest compatible, legitimately reusable gameplay foundation. Analyze binaries only to the depth necessary. Codex performs research/integration work; independent evidence and tests decide what passes. A working Unity greybox—not a quantity of AI output—is the ultimate production outcome.

## 1. Provenance and decision labels

The labels below must appear in research reports and in decisions derived from external material:

- **UPSTREAM-DOCUMENTED (UD):** directly checked against a named primary repository or maintainer document, pinned to a revision; a documented claim is *not* a locally reproduced result.
- **LOCALLY-VERIFIED (LV):** executed against our exact host/tool versions with independently retained output and a passing external check.
- **STUDIO-PROPOSED (SP):** our architecture, policy, thresholds, or workflow design; not claimed as an upstream feature.
- **REPORTED (R):** project author/user anecdote or case-study result not reproduced by us.
- **BLOCKED / UNKNOWN:** insufficient proof or missing prerequisites. Never silently promote to PASS.

### 1.1 Primary source register (consult before installation)

| ID | Source | Pinned reference (as inspected 2026-11-11) | What it supports | Evidence class |
| --- | --- | --- | --- | --- |
| U01 | [awesome-rea](https://github.com/yibie/awesome-rea) | `fd449e08858456e5aed21f5c1b78ec1af29817f1` | Two-track research curation, acceptance-test discipline, source/evidence scrutiny, failure discussions | UD |
| U02 | [awesome-rea curation skill](https://github.com/yibie/awesome-rea/blob/fd449e08858456e5aed21f5c1b78ec1af29817f1/.agents/skills/rea-curation/SKILL.md) | U01 commit | Source verification, search retries, supply-chain and merge-loss safeguards | UD |
| U03 | [REA (official)](https://github.com/morluto/rea) | `0909d89c966c30955fd0906b622ff25f3700789f` | Agent setup, local evidence, managed/IL2CPP and native inspection, provider limitations | UD |
| U04 | [REA installation](https://github.com/morluto/rea/blob/0909d89c966c30955fd0906b622ff25f3700789f/docs/getting-started/installation.md) | U03 commit | Scoped doctor, dry-run setup, approval, Codex integration | UD |
| U05 | [REA Windows Ghidra](https://github.com/morluto/rea/blob/0909d89c966c30955fd0906b622ff25f3700789f/docs/providers/windows-ghidra-p0.md) | U03 commit | Experimental Windows x64 read-only native provider boundary; precise host/target requirements | UD |
| U06 | [REA IL2CPP](https://github.com/morluto/rea/blob/0909d89c966c30955fd0906b622ff25f3700789f/docs/il2cpp-metadata.md) | U03 commit | Supported metadata versions and explicit partial/unsupported outcomes | UD |
| U07 | [DecompPipeline](https://github.com/GeneralAtrox/DecompPipeline) | `677a880c9fa942dbbc8d0076332cb2e7e0a1e3b5` (`master`) | Translator-first, independent judge, separate per-function workers, oracle freshness, coverage/mutation checks, cost reporting | UD; project performance figures R |
| U08 | [DecompPipeline proof gates](https://github.com/GeneralAtrox/DecompPipeline/blob/677a880c9fa942dbbc8d0076332cb2e7e0a1e3b5/docs/PROOF_GATES.md) | U07 commit | Why vector PASS alone is inadequate; coverage and mutation-based challenge | UD |
| U09 | [Official Hex-Rays IDA MCP](https://github.com/HexRaysSA/ida-mcp) | `391c2f0606a773050fbafcd3ff62942688a0713b` | Optional official IDA/Codex integration; **not** required for phase 1 | UD |
| U10 | [Codex MCP commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | Living documentation; record retrieval date | `codex mcp list --json`, `codex mcp get`, `/mcp` checks | UD |
| U11 | [Ghidra official repository](https://github.com/NationalSecurityAgency/ghidra) and [Getting Started](https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GettingStarted.md) | Living documentation; pin chosen release at setup | Upstream installation and JDK compatibility | UD |

**Important source correction:** U01 contains an older/nonresolving entry for `ReverseEngineer-Anything/REA-Github`. Use U03 (`morluto/rea`) and its official package/install links, not lookalike repositories or unverified ZIPs. The catalog's CC0 license does **not** confer rights to third-party game code, art, music, binaries, or linked tools.

**Compatibility warning:** Ghidra's newest mainline requirements can differ from the specific Ghidra version validated by REA. The REA Windows P0 guide names Ghidra 12.1.x and a 64-bit JDK 21+ for that limited lane; newer upstream Ghidra documentation describes other JDK requirements. **Choose and pin a tested provider/host pair; do not infer compatibility from “latest.”**

## 2. Production objective and stopping rule [SP]

**Original vision → existing research → authorized observation → targeted binary inspection only if necessary → evidence-backed specification → maximum compatible licensed reuse → Codex integration → tested playable greybox → original IP refinement.**

1. First search studio evidence, engine features, source-available implementations, game samples, official docs, and commercially licensed frameworks.
2. Observe/reference mechanics and define measurable inputs, outputs, timing, state changes, dependencies, and failure cases.
3. Inspect structural metadata if observation is insufficient.
4. Conduct targeted function analysis only to resolve an explicit outstanding question.
5. Attempt matching decompilation / static recompilation **only** for an authorized preservation, compatibility, or other justified reconstruction objective; never make full recovery the default.
6. Stop investigating as soon as a licensed working foundation or defensible specification answers the production need.
7. Never use a decompiled proprietary implementation or extracted third-party assets as if they were automatically licensed for commercial reuse.

**Research completion is decision-oriented:** the report must say **REUSE**, **CONFIGURE**, **ADAPT**, **BUILD LIMITED BRIDGE**, **INVESTIGATE FURTHER**, or **STOP / RIGHTS BLOCKED**, with evidence and costs. Do not research indefinitely for its own sake.

## 3. Logical harness architecture [SP]

```text
Creative brief / gameplay question
       |
GPT-6 (research director: criteria, scope, evidence review)
       |
Codex CLI/desktop in local isolated AIARE workspace
       |-- reuse & primary-source discovery
       |-- REA MCP -> Ghidra native analysis (optional other validated provider)
       |-- managed/.NET, Unity IL2CPP or package structure inspection
       |-- bounded behavioral probes for an authorized sample
       |-- immutable evidence artifacts + report drafts
       |
Independent host-side judge (never writable by the worker)
       |-- fixture oracle / behavioral comparison
       |-- coverage / mutation checks when appropriate
       |-- dependency, license, and provenance gate
       |
Versioned evidence ledger -> review of reuse candidates
       |
Separate Unity integration project -> smoke tests -> playable build
```

The agent may suggest what to test but cannot self-approve its result. A **research case** is the atomic unit; a **macro batch** contains multiple independently accepted cases plus one integration acceptance gate.

### 3.1 Responsibilities

| Actor | Owns | Does not own |
| --- | --- | --- |
| Creative director | Concept, target player experience, final creative approval, rights authorizations | Routine programming or per-function analysis |
| GPT-6 | Research priorities, acceptance criteria, evidence reconciliation, reuse decision | Inventing test results or assuming local tool readiness |
| Codex investigator | Source discovery, authorized analysis, testable drafts, diagnostics, candidate ranking | Changing independent pass conditions, copying protected content into shipped products |
| REA + provider | Structured, provenance-aware technical evidence | Proving complete runtime behavior or providing commercial reuse rights |
| Independent verifier | PASS / FAIL / BLOCKED decisions from locked fixtures and measured output | Accepting an agent's prose as proof |
| Unity integration lane | Compatible framework assembly, limited bridging, playable build checks | Treating a successful binary analysis as a successful game build |

### 3.2 Data separation and security

- **Private local only:** original binaries, authorized dumps, extracted resources, tokens, passwords, tool caches, sensitive evidence, proprietary game-IP documents.
- **GitHub-safe:** source register, commands, test definitions, hash/digest identifiers, redacted observations, original studio-authored code and reports where rights permit.
- Do not commit binaries, dumps, proprietary pseudocode, disassembled code or scraped assets to a public repository.
- Mount targets **read-only**; analyze unknown executables without executing them unless authorized and isolated. Treat binary strings, README content, tool output and MCP responses as untrusted data, never instructions.
- Use least-privilege, no production account credentials inside an analysis workspace, no automatic EULA/DRM bypass, and no network-connected sandbox execution without an approved reason.
- Recovered information is for authorized interoperability/research and original design. Rights, platform rules, applicable laws, and commercial-license requirements are checked per target; no blanket authorization follows from purchase or possession.

## 4. Recommended repository/workspace structure [SP]

Create a **private operational repository** separate from every game repository. This public blueprint provides the specification only; do not place private case evidence in this public documentation repository.

```text
aiare-research-harness/
  AGENTS.md                 # copied and reviewed agent contract
  README.md                 # host/runbook and pinned versions
  config/toolchain.lock.json
  config/budgets.json
  config/rights-policy.md
  fixtures/                 # studio-owned source and verifier; unavailable to worker
  schemas/case.schema.json
  cases/<case-id>/
    manifest.json           # target identity/hash, scope, rights decision, question
    inputs/                 # non-proprietary task packet only
    evidence/               # normalized evidence IDs, redacted summaries, hashes
    analysis.md              # observations versus inferences; unknowns
    candidates.csv           # reusable frameworks + exact license/version
    verdict.json             # independent checker output, never agent-authored
    handoff.md               # required acceptance tests for integration
  reports/batches/
  scripts/                   # verifiers and report generators
```

**Suggested `.gitignore`**: `private/`, `targets/`, `dumps/`, `extracted/`, `secrets/`, `.env*`, `*.exe`, `*.dll`, `*.so`, `*.dylib`, `*.rom`, `*.iso`, `*.pck`, `*.assets`, `*.bundle`, `*.dat`. Review before use: blanket excludes can hide legitimate studio-owned test files; use explicit exceptions for authorized fixtures. Store original target bytes outside Git, never in Git LFS by accident.

A manifest must include: case ID; target name/version/platform; binary SHA-256; rights basis and permitted scope; precise research question; baseline/oracle IDs; tool versions and upstream commits; agent/worker ID; retry budget; evidence URLs and local digests; observations versus inference; failure/unknown states; verification artifact locations; reuse-candidate license; final decision.

## 5. Installation playbook [UD steps combined with SP gates]

**Do not run installer commands on a machine until the existing working copies and configuration have been inventoried and backed up.** This document is a runbook; it does not assert that a setup has been performed.

### Phase A — capture baseline (no changes)

Run locally in the shell appropriate to the host:

```sh
git --version
node --version
npm --version
codex --version
java -version
javac -version
python --version
codex mcp list --json
```

Some commands may be absent; record each exact output/error as **PASS**, **BLOCKED** or **NOT INSTALLED**. Do not install automatically to hide a failed preflight. Back up `~/.codex/config.toml` and any tool configuration before changes. Record operating system, architecture, available memory/disk, current Git branch and local dirty state for each development project; **do not reset, clean, overwrite or commit unrelated local work**.

### Phase B — identify trusted distributions

- REA: official `morluto/rea`, package `rea-agents`. Record exact npm version, source and lock/checksum before acquiring. Prefer a pinned reviewed version over an unreviewed `@latest` in unattended production.
- Ghidra: official NSA release archive, **not** a repository mirror or GitHub “Source code” zip. Match its documented JDK requirement to the exact Ghidra version.
- Codex: local CLI/desktop/IDE access supporting MCP, not an assumed capability of this ChatGPT conversation.
- Windows: provider integration in REA is documented as **experimental and read-only with host/format restrictions**; doctor + live function inspection are required before approval. Mac/Linux requirements differ.
- Optional IDA: consider only after the free Ghidra lane fails a defined use case and licensing/cost are approved. Avoid running redundant IDA MCP servers.

### Phase C — scoped diagnostics and reversible registration

Replace `<PINNED_REA_VERSION>` with the reviewed npm package version (do not type brackets literally):

```sh
npx -y rea-agents@<PINNED_REA_VERSION> doctor --provider ghidra --json
npx -y rea-agents@<PINNED_REA_VERSION> doctor --client codex --json
npx -y rea-agents@<PINNED_REA_VERSION> setup --client codex --dry-run --json
```

Review exact paths/settings proposed by the dry run. After explicit operator approval:

```sh
npx rea-agents@<PINNED_REA_VERSION> setup --client codex
codex mcp list --json
npx -y rea-agents@<PINNED_REA_VERSION> doctor --provider ghidra --client codex --json
```

Restart Codex if requested. In an active Codex session, inspect `/mcp` or `/mcp verbose` to verify REA **tools actually load**, not merely that a config entry exists. Preserve the post-setup configuration and its previous backup for rollback. The setup flow supports operator approval; do not use unconditional `--yes` for the initial install.

**Why this is a gate:** a correct package installation does not establish provider compatibility, native decompilation functionality, successful MCP invocation, or permission to inspect a particular target.

### Phase D — first owned/authorized binary

- Build the included [studio-owned fixture](fixtures/owned_transform.c) on the actual host; compile with symbols/unoptimized settings if available. Store the executable **outside the public repository**.
- Let Codex/REA inspect **only the compiled executable and the question**, not fixture source or the private oracle.
- Ask for the input/output rule, branch conditions, approximate data flow, and cited binary evidence. Explicitly report uncertainty.
- Independently run [verify_transform.py](fixtures/verify_transform.py) against the compiled program. Check predicted results, not the agent's claims.
- Require at least one intentionally wrong hypothesis to FAIL the verifier (negative control).
- Retain binary hash, exact commands, MCP evidence IDs, outputs, checker report, and resource cost.

Detailed test IDs and pass/fail conditions: [Acceptance Test Plan](ACCEPTANCE_TEST_PLAN_v1.0.0.md).

## 6. Runtime operating protocol [SP]

### Intake → discovery → execution → judgment → handoff

1. **Intake:** define one narrow question and intended game-system decision. Confirm permitted analysis and record target SHA-256.
2. **Prior-work lookup:** search the studio ledger for matching mechanic, target version, implementation and failed approaches. Existing accepted results must be reused.
3. **Cheapest sufficient method:** source/docs/license search → observable behavior → structural metadata → targeted decompilation → justified high-cost reconstruction.
4. **Task packet:** give Codex a bounded, minimally necessary packet: question, known constraints, specific evidence references, allowed tool actions, expected output schema and budget.
5. **Execution:** separate read-only evidence gathering from proposed changes. For concurrent workers, use isolated worktrees and exclusive task claims; no shared mutable analysis database.
6. **Independent verification:** a host-side checker compares recorded observations and/or candidate behavior with a pinned baseline. Worker never modifies the oracle, expected outputs, gate, or test runner.
7. **Decision:** accept with evidence, retry with a specific new hypothesis, or stop as blocked/unknown. Do not “retry harder” without a changed cause.
8. **Handoff:** write the functional specification, candidate reuse matrix, risks, and Unity acceptance criteria. A successful build or test must be reproducible.

### 6.1 Macro-batch orchestration

- The operator requests a **macro outcome** (for example, a complete movement/interaction specification).
- The controller splits it into independent research cases, claims each exactly once, and queues them.
- Only verified cases are merged. Run a subsystem integration check across their state transitions and shared dependencies.
- Deliver one macro report containing accepted cases, exception IDs, blocker details, measured costs and next decisions.
- Preserve progress after each independently passing case. A stalled case does not invalidate completed sibling work.
- Set concurrency from measured machine/memory/provider limits; start at **one worker**, increase to two only after serial success, and scale further only when throughput/quality improves.

### 6.2 Resource and failure controls

Initial **studio-proposed pilot defaults**, to be calibrated from measured data (not upstream universal settings):

| Knob | Pilot default | Stop/escalation behavior |
| --- | --- | --- |
| Attempts per unchanged research hypothesis | 3 | Require changed evidence, a new hypothesis or human decision |
| Agent wall time per narrow case | 15 minutes | Save artifact/log and mark `TIME_BUDGET`; never claim completion |
| Native tool startup | Follow provider-documented timeouts | On failure record provider error; avoid blind agent retries |
| Parallel research workers | 1 | Increase only after local pass-rate/throughput test |
| Maximum context | Compact selected evidence; full source kept on disk | Fetch specific evidence page as needed, not a complete dump |
| Budget currency | Tokens, cost, tool time, retries and accepted outcomes | Surface cost per **verified** case |

Never present these suggested budgets as calibrated. Failed attempts, timeouts and blocked tasks are included in cost metrics. An infrastructure error is distinct from an incorrect hypothesis; a previously successful case becomes **STALE** if a dependent oracle, binary hash, tool version, or test fixture changes.

### 6.3 Verification strength

- **Level V0 — source-verified:** primary docs/repo confirmed; no local run.
- **Level V1 — environment-verified:** trusted tool + provider + Codex MCP live.
- **Level V2 — behavior-verified:** targeted original/replica comparisons on predetermined input vectors; retain raw outputs and digest.
- **Level V3 — challenge-verified:** coverage measures, untested-path declaration, negative controls / mutation tests appropriate to the target.
- **Level V4 — product-verified:** game-engine integration, a built executable, and complete player-loop smoke tests.

Do not equate V2 with exhaustive equivalence. Byte-exact matching is an appropriate gate only for an explicit matching-decompilation objective using a compatible toolchain; a Unity behavioral analogue should usually use functional acceptance tests, not byte matching.

## 7. Production handoff and reuse matrix [SP]

Search in this order: **single largest usable licensed gameplay chassis**, matching sample projects, compatible modules, engine-native configuration/events, small Codex integration bridges, changes to existing systems, and finally new original systems when necessary.

Evaluate each candidate against: exact supported engine/editor version, complete playable demo, coverage of required mechanic, compatibility with the chosen chassis, ownership of shared state (input/combat/inventory/save), dependency graph, maintenance status, license/commercial redistribution rights, installation reproducibility, cost, and demonstrated build/test outcomes.

**Acceptance for the initial Unity handoff:** the concept-specific mechanic works in an isolated project, its required input/output cases pass, engine Console has no new critical errors, and a standalone build completes the smallest required play loop. A pile of compatible-looking packages, a screenshot or a compiling script is not sufficient.

## 8. Test and readiness gates [SP]

The [acceptance matrix](ACCEPTANCE_TEST_PLAN_v1.0.0.md) is authoritative. Summary:

| Gate | Proof required | A gate cannot pass if… |
| --- | --- | --- |
| G0 baseline | OS/tool inventory, dirty-tree capture, backup receipts | state was not checked or existing work was overwritten |
| G1 provenance | approved upstream URLs, exact versions, recorded digests | downloaded from a lookalike or unsupported source |
| G2 installation | provider/client scoped doctor + running Codex MCP tool | only config registration is demonstrated |
| G3 forensic smoke | owned executable analyzed with verifiable function evidence | reports merely assert analysis occurred |
| G4 behavioral integrity | independent correct/negative control outcomes | oracle is agent-writable, vectors untested or mismatched |
| G5 reproducibility | clean rerun + evidence/manifest checks | expected results cannot be reproduced |
| G6 reuse handoff | documented legal/licensing and Unity acceptance criteria | reused code/assets have unknown commercial rights |
| G7 game integration (later) | working standalone Unity build and complete gameplay smoke test | only compilation or editor screenshots exist |

**Status semantics:** `PASS` requires artifact path + independent verifier output + source/tool revision. `FAIL` means a check was run and contradicted expected results. `BLOCKED` means prerequisite, rights, infrastructure or access failed. `NOT_RUN` means unattempted; it is never a pass. `STALE` means the proof is invalidated by changed dependencies.

**Initial deployment readiness:** G0–G5 PASS on one owned fixture; G6 documented for the first target. G7 is a separate game-integration acceptance, not required to declare the *research harness* installed.

## 9. Operational deliverables and change control

For each accepted case, save:
- `manifest.json` with target SHA-256, toolchain pins, rights basis, question, owner, status and case ID;
- `evidence/index.json` with selected REA evidence IDs, paths, hashes, exact calls, coverage/unknowns;
- `analysis.md` differentiating direct observation, inference, and unverified ideas;
- `verdict.json` emitted by the independent judge with expected/observed values and PASS/FAIL;
- `handoff.md` with reuse candidates, license evidence and executable Unity acceptance cases;
- a commit hash for **original studio-authored** documentation/tests, plus any exceptions.

A batch closes only if every required case has passed or is explicitly recorded as a nonpassing exception, and the macro objective has a passing integration gate. Failed workers must leave their latest outputs and a reason; no silent “completed” placeholders.

**Change protocol:** v1.0.0 is the baseline. Fixes that alter acceptance gates, scope/rights, budgets or toolchain pins require a documented decision and version update. Never rewrite an earlier PASS after changes; mark it STALE and rerun. Build/source tools from a reviewable pinned dependency set; keep portable proof receipts.

## 10. First field experiment and metrics

**Pilot:** one studio-authored native fixture, not a commercial game. Perform a blind REA/Ghidra inspection, identify the branch structure, predict outcomes, run the independent verifier, and rerun on a clean copied binary.

Track:
- doctor/provider/client success (G2);
- binary/fixture identity and evidence links (G1/G3);
- expected output match rate and negative-control detection (G4);
- test-path coverage where available, with untested branches explicitly named (G4);
- time, tokens, model requests, tool calls, retries, cost per accepted case;
- percentage of correctly reused prior evidence;
- number of manual operator actions after initial setup.

**Promotion rule:** only after the owned fixture passes G0–G5 should a second authorized target be admitted. Only after two representative targets pass should optional worker concurrency or additional MCP servers be evaluated. Performance gains are measured in accepted usable findings per unit cost and time, not in generated text or decompiled line count.

## 11. Known limitations and nonclaims

- This document is **a deployable design**, not proof of a deployment. As of publication no local REA/Ghidra/Codex installation, binary inspection, or Unity integration has been performed by this blueprint.
- `awesome-rea` is a curated index, not a decompilation executable or independent lab verification of every included claim.
- REA can parse metadata and inspect many native formats but has explicit version, host, provider and extraction limitations. A parsed metadata table does not establish runtime behavior or return an original editable Unity project.
- DecompPipeline's reported achievements and budgets are target-specific and may not transfer to a modern Unity/Unreal game.
- Agent prompt restrictions alone do not create a secure sandbox. Use OS-level access control, read-only target copies, separate verifier credentials and isolated workspaces.
- Legal/commercial authorization is evaluated per target. No protected assets, decompiled proprietary code, copyrighted audiovisual work or anti-circumvention instructions are imported into the final commercial game without appropriate rights.

## 12. Implementation checklist / checkpoint

- [ ] G0: protect and inventory local state; backup agent configuration.
- [ ] G1: pin REA, Ghidra/JDK and Codex versions from authentic sources.
- [ ] G2: REA doctor + live MCP tool check PASS on the selected host.
- [ ] G3–G5: blind owned-fixture test, independent verifier, negative control and clean rerun PASS.
- [ ] Create private operational repo with AGENTS contract, source register, evidence schema and case ledger.
- [ ] Run one authorized gameplay-mechanic investigation, then one reuse-first Unity integration pilot.
- [ ] Validate macro-batch orchestration only after serial results are reliable.

**Final governing directive:** *Find the closest legitimate working chassis. Investigate only what remains uncertain. Let independent tests decide what is correct. Assemble and prove a playable macro structure before chiseling original detail.*

---
**Source policy:** URLs and pinned commits in §1 are upstream-documentation evidence; all marked SP architecture, gates and thresholds are studio proposals until independently verified. Do not represent the pilot as executed or any experimental compatibility lane as production-supported.
