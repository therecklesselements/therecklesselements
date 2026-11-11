# Owned AIARE Fixture — Local QA Receipt

**Date:** 2026-11-11  
**Scope:** Only the two original studio-authored fixture files published in this directory.  
**Outcome:** Fixture compiler and oracle tests behaved as designed. **This is not an installation test of the studio's computer, Codex, REA, Ghidra, or a game binary.**

## Provenance

The files were reconstructed byte-for-byte from the published source and validated using the Git blob identity algorithm. Their local SHA-1 Git blob IDs matched the GitHub repository's read-back blobs exactly:

| File | Git blob SHA-1 (published = tested) |
| --- | --- |
| `owned_transform.c` | `110ede42ba5b9badcc50641a6f98f3778cd279f5` |
| `verify_transform.py` | `e29fae9be2145bd4eaaf8cb67ef878f5f773c1f0` |

Execution environment: ephemeral isolated Linux x86_64 tool container, Linux kernel 6.18.57; GCC 14.2.0 (Debian 14.2.0-19), Python 3.13.5. **Not the user's local machine.**

## Executed checks

1. `python3 -m py_compile verify_transform.py` → exit **0**.
2. `cc -O0 -g owned_transform.c -o owned_transform_exact` → exit **0**.
3. `python3 verify_transform.py --binary ./owned_transform_exact --report ./positive_exact.json` → exit **0**; status **PASS**, 9/9 vectors.
4. `python3 verify_transform.py --binary ./owned_transform_exact --negative-control --report ./negative_exact.json` → exit **1**; status **FAIL**, 8/9 vectors, intentionally wrong expectation at input 3 (expected 8 vs actual 7).

The temporary compiled sample's SHA-256 was:

```text
5fa4a8f3d8edaf6b7c781ef128b208685997b392ff9c1487f70be62494b55039
```

That binary hash is **specific to this compiler/environment** and must not be used to approve a different local build. No game data or compiled binary was committed.

## Limits

- The isolated execution checks verify fixture syntax, compiling, a positive oracle result, and that an intentionally incorrect expectation is rejected.
- No live Codex MCP request occurred. No native function/pseudocode was extracted through REA/Ghidra. No blind investigator submitted a rule to the checker.
- Therefore installation gates A00–A06 and A09–A12 remain **NOT_RUN** in the studio environment; the genuine blind-investigation A07 is also **NOT_RUN**.
- The fixture's *local test tool behavior* has a positive/negative receipt, but the AIARE **research harness has not passed the end-to-end acceptance plan**.

**Next step:** Execute [Acceptance Test Plan v1.0.0](../ACCEPTANCE_TEST_PLAN_v1.0.0.md) on the actual target computer with isolated investigator and verifier permissions.
