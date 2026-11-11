# AIARE Research Harness — Installation and Acceptance Test Plan

**Version:** 1.0.0 · **Date:** 2026-11-11  
**Status:** Test specification published; **no local test results asserted**  
**Design:** STUDIO-PROPOSED acceptance protocol informed by the pinned primary sources in the [Blueprint](AIARE_RESEARCH_HARNESS_BLUEPRINT_v1.0.0.md).

## 0. Rules for reporting

For each gate save `test_id`, UTC date/time, OS/architecture, operator, exact command, relevant stdout/stderr, tool versions, binary SHA-256, reference revision, expected result, actual result, status and an artifact path. Results are **PASS / FAIL / BLOCKED / NOT_RUN / STALE**.

A status is **PASS only when its explicitly named test has been executed and independently compared**. Absence of an error, a correctly generated report, or an agent's narrative is not proof. Missing prerequisites are BLOCKED (not FAIL). A changed binary, oracle, toolchain or fixture invalidates dependent results: mark STALE.

**Test boundary:** G0–G5 validate the research harness. G6 validates a legitimate reuse decision; G7 validates a later Unity playable prototype. G6/G7 do not automatically pass with G5.

## 1. Gate matrix

| ID | Gate | Executor | Exact acceptance condition | Required artifact |
| --- | --- | --- | --- | --- |
| A00 | Existing work preserved | Operator, outside worker sandbox | `git status` on all affected projects recorded before work; required config backups exist; no unrelated files were modified/deleted | `reports/preflight/git-before.txt`, backup receipt |
| A01 | Authentic REA package | Operator | Repository/publisher is `morluto/rea` and package `rea-agents`; exact version, downloaded distribution source and checksum/lock recorded | `toolchain.lock.json` |
| A02 | Toolchain compatibility | Operator | Exact host, CPU, provider, Ghidra/JDK versions meet their **matching** upstream requirements; unsupported combination is BLOCKED | `reports/preflight/toolchain.json` |
| A03 | Client registration | Operator | Scoped `rea doctor --client codex --json` reports a healthy explicit client scope; `codex mcp list --json` contains REA configuration | Raw doctor and MCP list JSON |
| A04 | Live MCP provider | Codex + independent observer | Codex session calls one REA tool; it returns structured, attributable evidence from the owned binary; provider health passes and evidence identifies source | Redacted MCP transcript and REA evidence receipt |
| A05 | Binary identity | Operator | Owned fixture SHA-256 recorded, exact analyzed copy matches identity; unreadable/changed file BLOCKED | `manifest.json`, digest records |
| A06 | Structural research | Investigator, then reviewer | Investigator identifies branches/function relation from actual assembly or supported decompiler evidence, with address/function evidence and explicit limitations | `analysis.md`, evidence references |
| A07 | Held-out behavior | **Independent verifier**, inaccessible to investigator | All positive oracle vectors match the compiled owned binary; researcher hypotheses/predictions are compared separately | Machine-generated `verdict.json` |
| A08 | Negative-control sensitivity | **Independent verifier** | Intentionally wrong expected result is **rejected** (nonzero exit / FAIL); a false hypothesis must not be accepted | Separate negative-control report |
| A09 | Clean reproduction | Operator | Repeat fixture analysis on a fresh copy at the same SHA-256 and rerun independent held-out vectors; no silent dependency drift | Rerun receipts and verdict |
| A10 | Source classification | Reviewer | All research claims labeled UD, LV, SP, R or UNKNOWN; observations separated from inference; source URLs/commits reproducible | Reviewed case report |
| A11 | Rights and reuse | Reviewer | Target rights scope recorded; proposed modules have recorded commercial license, exact version and integration compatibility; unknown rights block reuse | `rights.md`, candidate matrix |
| A12 | Unity acceptance (later) | Codex + test runner | Standalone build produced and launched; complete smallest gameplay loop passes; logs/test outputs saved; no new critical errors | Build location, automated tests, playthrough proof |

**Promotion:** installation/harness-ready = A00–A10 PASS for one studio-owned fixture (A11 required before third-party research). Full production proof requires A11 and A12 on a separate, authorized game-mechanic pilot.

## 2. Non-destructive preflight commands

Run from a trusted directory outside a game project. Capture each command's exact output and exit code. Different shells expose absent programs differently.

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

For `A00`, in **each affected** project:

```sh
git status --porcelain=v1
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
```

Record dirty paths *without* `git reset`, `git clean`, auto-stash, broad commits, or restoring someone else's work.

## 3. Readiness diagnostics and setup

Use trusted sources from the Blueprint. Before acquisition, identify the supported Ghidra/JDK pair. REA's **Windows Ghidra path is experimental** and presently constrained to specific read-only native-analysis operations on supported local x64 hosts; do not treat a working `java` command as provider proof.

Replace `<PINNED_REA_VERSION>` with the actual reviewed release number and preserve it in the lock record:

```sh
npx -y rea-agents@<PINNED_REA_VERSION> doctor --provider ghidra --json
npx -y rea-agents@<PINNED_REA_VERSION> doctor --client codex --json
npx -y rea-agents@<PINNED_REA_VERSION> setup --client codex --dry-run --json
```

**Expected before changes:** dry run prints a change plan; it must not silently overwrite unrelated configuration. Back up Codex config and tool settings first. After operator approval:

```sh
npx rea-agents@<PINNED_REA_VERSION> setup --client codex
codex mcp list --json
npx -y rea-agents@<PINNED_REA_VERSION> doctor --provider ghidra --client codex --json
```

**A03 PASS:** the relevant `doctor` checks and registered client are healthy. **A04 PASS additionally requires an actual REA tool invocation within a refreshed Codex session**, not merely a registered MCP server. In the Codex terminal interface, use `/mcp verbose` to inspect active servers and available tools. If the provider refuses the host/target, record the exact reason and test a documented alternative platform/provider rather than declaring success.

The official REA installer does **not** automatically install an arbitrary compatible Ghidra/JDK pair. The operator installs compatible prerequisites separately, using the upstream instructions.

## 4. Owned blind fixture and verifier

These files are original studio-authored acceptance fixtures. They are not copies of any game:

- [owned_transform.c](fixtures/owned_transform.c): deterministic tiny native program with multiple branches.
- [verify_transform.py](fixtures/verify_transform.py): independent behavioral comparator and intentional negative control.

### 4.1 Build in an isolated temporary folder

Linux/macOS with a C compiler:

```sh
mkdir -p /tmp/aiare-fixture
cc -O0 -g docs/engineering/aiare/fixtures/owned_transform.c -o /tmp/aiare-fixture/owned_transform
shasum -a 256 /tmp/aiare-fixture/owned_transform    # macOS, when shasum is present
# or: sha256sum /tmp/aiare-fixture/owned_transform   # Linux, when sha256sum is present
```

Windows with MSVC Developer PowerShell (adjust to an existing private folder and verified path):

```powershell
New-Item -ItemType Directory -Force -Path "$env:TEMP\aiare-fixture"
cl /Od /Zi /Fe:"$env:TEMP\aiare-fixture\owned_transform.exe" .\docs\engineering\aiare\fixtures\owned_transform.c
Get-FileHash "$env:TEMP\aiare-fixture\owned_transform.exe" -Algorithm SHA256
```

An absent compiler is a **BLOCKED prerequisite**, not grounds to invent a successful binary build.

### 4.2 Blind investigation

Prepare two **physically separate** working locations:

1. **Investigator:** compiled executable copy, hash, task packet, allowed REA tools, *no original source file and no test oracle*.
2. **Verifier:** source, oracle script, independent reference-output vectors and permission to inspect the investigator's submitted predictions (read-only).

Investigator task:

> Inspect this studio-owned native executable using the registered REA/Ghidra tools. Without seeing its source, identify the primary integer transform's conditional branches. Describe the input/output rule, cite exact function/address/instruction evidence, predict results for the operator-supplied test inputs, and state uncertainty. Do not declare PASS; do not alter any tests.

Capture the REA tool's actual evidence ID and function evidence. Distinguish “tool returned pseudocode” from “this behavior has been verified.”

### 4.3 Independent positive/negative test

Linux/macOS:

```sh
python3 docs/engineering/aiare/fixtures/verify_transform.py --binary /tmp/aiare-fixture/owned_transform --report /tmp/aiare-fixture/positive.json
# Expect exit 0, status PASS, all reference vectors matched.
python3 docs/engineering/aiare/fixtures/verify_transform.py --binary /tmp/aiare-fixture/owned_transform --negative-control --report /tmp/aiare-fixture/negative.json
# Expect NONZERO exit and status FAIL, because one expected result was intentionally corrupted.
```

Windows (use your actual Python command):

```powershell
python .\docs\engineering\aiare\fixtures\verify_transform.py --binary "$env:TEMP\aiare-fixture\owned_transform.exe" --report "$env:TEMP\aiare-fixture\positive.json"
python .\docs\engineering\aiare\fixtures\verify_transform.py --binary "$env:TEMP\aiare-fixture\owned_transform.exe" --negative-control --report "$env:TEMP\aiare-fixture\negative.json"
```

**A07/A08 require two separate checks:** (1) independent verifier confirms the executable's known input/output behavior, and rejects wrong expectations; (2) investigator's **submitted rule/predictions** independently match the withheld test evidence. If only the verifier passes but the investigator did not provide correct binary-grounded analysis, **A06 and the research portion of A07 remain FAIL/NOT_RUN**. Never conflate testing the fixture with testing the agent.

The verifier writes a JSON report with source binary SHA-256, checks, stdout/stderr snippets, actual versus expected output and overall PASS/FAIL. It is not an exhaustive proof of function equivalence.

## 5. Clean rerun, negative evidence, and release gate

For A09, copy the original executable into a new temporary folder, verify SHA-256 equality, repeat live REA analysis and both positive/negative verification checks. Record whether tool outputs are stable **or explicitly note expected analysis-database/address differences**; compare semantic observations, not unstable local IDs alone.

For A10, the reviewer must check:
- Source citations point to accessible primary sources, correct file/commit versions and actual analysis artifacts.
- `UPSTREAM-DOCUMENTED` is not mislabeled `LOCALLY-VERIFIED`.
- Unsupported metadata versions, unknown symbols, unexercised branches and provider refusal are explicit rather than silently treated as absence.
- Claims of commercial safety cite permissions/licenses for **each** system and asset, not just the catalog.
- A proposed 90% time saving or zero-code result is marked a hypothesis until benchmarked on a real game project.

### Minimal JSON verdict record

```json
{
  "schema_version": "1.0.0",
  "test_id": "A07",
  "case_id": "AIARE-0001",
  "status": "NOT_RUN",
  "checker": "verify_transform.py",
  "checker_revision": "<commit-sha>",
  "binary_sha256": "<actual-sha256>",
  "inputs": [],
  "expected": [],
  "observed": [],
  "evidence_paths": [],
  "notes": "Template only; replace with real machine-generated result."
}
```

Never commit an example `NOT_RUN` template as if it were an executed test.

## 6. Typical failures and correct outcomes

| Symptom | Outcome | Correct response |
| --- | --- | --- |
| Config lists REA but tools absent in active Codex session | A04 BLOCKED | Restart/reconnect and inspect `/mcp verbose`; don't reinstall blindly |
| Ghidra unsupported host or binary format | A02/A04 BLOCKED | Record exact limitation; choose supported documented lane |
| Unexpected executable or lookalike distribution | A01 FAIL | Discard unverified artifact; resolve official provenance before retry |
| No original fixture hash or build identity | A05 BLOCKED | Rebuild/capture hash from owner-controlled input |
| Decompiler reports unknown/partial structure | A06 incomplete | Report unknown; use narrower query or additional independent observation |
| Fixture positive verifier fails | A07 FAIL | Inspect actual stderr/exit code; do not let agent change expected outputs |
| Negative control unexpectedly passes | A08 FAIL | Treat verifier as unsafe and stop all autonomous acceptance |
| Agent rule disagrees with held-out results | A07 FAIL | Preserve evidence and requeue bounded hypothesis with diagnosed mismatch |
| Research matches behavior but reuse license missing | A11 BLOCKED | Stop commercial integration and verify rights |
| Unity project compiles but player cannot complete loop | A12 FAIL | Correct scene/interaction and rerun full runtime smoke test |

## 7. Test report / sign-off

```text
Blueprint version: 1.0.0
Case ID:
Host/OS:
Toolchain pin SHA:
Target SHA-256:
A00:
A01:
A02:
A03:
A04:
A05:
A06:
A07:
A08:
A09:
A10:
A11:
A12:
Total measured time/tokens/cost:
Independent verifier identity and evidence path:
Blocking issues:
Operator decision: PILOT_APPROVED | PILOT_REJECTED | MORE_EVIDENCE_REQUIRED
```

**Do not promote to “ready for automated macro batches” until local G0–G5 evidence is reproducible, an adversarial/negative test fails as intended, and the operator approves the next target's rights/scope.**
