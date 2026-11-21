# Game Finishing Optimization and Polish

[Download the Word master](https://raw.githubusercontent.com/therecklesselements/therecklesselements/main/docs/studio/Game%20Finishing%20Optimization%20and%20Polish.docx)

RECKLESS ELEMENTS Studio · Production master · Edition 1.0 · November 21, 2026

Use this workshop when a playable build already delivers the core loop and the team needs to decide what still stands between that build and players. Start with one promise the player should be able to rely on. Carry it through a packaged build, a difficult play condition, an update from the previous build, and the creator’s review.

For example, “I can recognize the warning, act once, and resume from my checkpoint after a restart” gives engineering, audio, design and release a shared test. A faster build that hides the warning still fails that test.

## Route through the workshop

| Stage | Question to settle | Evidence to carry forward |
| --- | --- | --- |
| 0 · Scope and baseline | What experience, target and build are we closing? | Reference route, package identity and constraints |
| 1 · Stability | Can the player act, traverse and recover reliably? | Input trace, cold run and recovered save |
| 2 · Game feel | Does the defining action respond as intended? | Matched clips and creator’s preference |
| 3 · Clarity | Can a new player understand and complete it? | First-use observation and readable cue |
| 4 · Feedback | Does the added effect communicate the event? | Effects-on and reduced-effects comparison |
| 5 · Optimization | Did the change improve the limiting resource? | Matched traces, patch test and gameplay replay |
| 6 · Release candidate | Which exact package is ready for which decision? | Candidate record, open risks and acceptance |

Begin accessibility, packaging and performance checks as soon as the relevant path exists. Reopen a stage whenever a later change alters its evidence. One person can cover several disciplines. Give each change one writer and name who can accept the result. The receiving game owns its targets and runbook. J. A. Wood retains game feel, milestone and release decisions. FATDOG holds the active production slot through creator-accepted Beta readiness. [Studio operating guide](https://github.com/therecklesselements/therecklesselements/blob/014013275482513a30c81f289ab9e28d09adc2e2/docs/studio/START_HERE.md)

## Scope and baseline

### Gate 0  Agree on the test before tuning

The project lead records the current milestone, source revision, package hash or immutable build ID, target platform, minimum and typical supported configuration, input devices, and display modes. Confirm what the creator wants the action to feel like. Keep a short reference recording and a restorable baseline package.

Choose three routes. Use an ordinary first session, the densest credible encounter or transition, and a recovery route such as quitting during a save and resuming. Write down starting state, camera path, actions, end condition and who can reproduce them. Give cache state, storage, build flags, resolution, quality preset, power mode and frame cap alongside every comparison. Name any unavailable target and leave its result open.

| Decision | How to fill it | Reason it matters |
| --- | --- | --- |
| Player promise | Write the action, perceptible cue and expected result. | A cheaper effect can pass a timing budget and hide that cue. |
| Budget | Choose target, unit, statistic, observation window, allowed excursions and rationale for each supported mode. | An average alone conceals isolated stalls. |
| Resource limits | Measure frame time, RAM, graphics memory where observable, loading and package size. Add voice, overdraw or draw-call limits where they explain a player problem. | A single scene count cannot predict the cost of every scene. |
| Change ownership | Name scope owner, change writer, verifier and decision owner. One person may hold several roles. | A specialist roster would otherwise become a staffing dependency. |

Use scripted headless runs for simulation and state checks. Capture rendering, presentation and interaction on a rendered player. Profile a diagnostic build to locate cost, then repeat the acceptance route in the intended shipping configuration. Qualify crash reporting with a controlled test failure in a disposable build and verify the correct symbols resolve a known location. Keep dumps, symbols and player data in the project’s approved storage. [Unity profiling guide](https://docs.unity3d.com/6000.0/Documentation/Manual/profiler-profiling-applications.html)

**Exit decision.** The lead can replay the baseline and explain what would fail. Freeze scope for this milestone. If a fix changes a frozen mechanic, record the player impact, affected tests, new build and creator decision before treating the old baseline as superseded.

## Simulation and recovery

### Phase 1  Capture the failure where the player sees it

**Input.** Sample through the supported input system. Buffer timestamped action edges when short presses can fall between simulation ticks. Consume each press once, expire stale actions, and clear or reconcile them on pause, focus loss and reconnect. Test taps, holds and rapid reversals at low and high render rates. In physics-driven play, vary zero, one and multiple fixed updates per rendered frame. Record input, simulation acceptance and presentation as separate points. A software timestamp ends at its recorded event. A claimed input-to-photon measurement also needs evidence of physical input and visible display response. [Unity Input System timing](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.13/manual/timing-optimize-fixed-update.html)

**Timing and replay.** A fixed step makes scheduling easier to reason about. For a deterministic replay promise, store the initial state, build, input sequence and relevant seeds, then compare state hashes at agreed ticks. Record the first divergence. Add cross-machine checks only where the game promises them. Choose presentation queue settings for the measured API, device and latency/throughput tradeoff. [Deterministic lockstep](https://gafferongames.com/post/deterministic_lockstep/) · [DXGI presentation latency](https://learn.microsoft.com/en-us/windows/uwp/gaming/reduce-latency-with-dxgi-1-3-swap-chains)

**Memory and streaming.** Profile allocation bursts against hitches. Pool frequently reused, expensive objects only when an A/B run improves the route. Cap retained objects, reset state on reuse, and compare peak and post-unload memory across repeated cycles. For first-visit stalls, compare cold and warm traversal. Separate disk reads, decompression, main-thread activation and shader pipeline creation. Warm representative render states for the target API and measure the added startup cost. [Unity shader loading](https://docs.unity3d.com/2022.3/Documentation/Manual/shader-loading.html)

**Saves.** Keep a known-good generation while writing the next one. Validate format version, integrity and gameplay invariants before promoting a migration. On disposable copies, interrupt the write, truncate the newest save, exhaust available storage, and open an older supported save. Restart twice. Verify the expected checkpoint, inventory and progress survive both restarts. Preserve original data when recovery fails or the save comes from a newer, unsupported build. Platform persistence and flush semantics determine what survives a power loss. [Windows buffered writes](https://learn.microsoft.com/en-us/windows/win32/fileio/flushing-system-buffered-i-o-data-to-disk)

**Exit decision.** Submit the observed response, worst traversal event, post-cycle memory trend and recovered checkpoint. An unresolved loss of progress or an unexplained recurring stall returns to the owning subsystem.

## The defining action

### Phase 2  Tune character controls and camera together

Select one interaction the creator considers central. For a traversal game it might be a turn on a narrow ledge. For a management game it might be selecting and confirming a time-sensitive order. Record the intended start, commit, feedback, recovery and next allowed action. Choose forgiveness windows only where they serve that intent.

Capture the same route before and after one change. Try a short tap, held input, opposite input during recovery and a camera obstruction. Check the deadzone at rest, target visibility in tight spaces and prompt accuracy with remapped controls. At each supported cadence, compare the first visible response, gameplay state change, animation contact and audio cue. Check the event fires exactly once across blends, cancellation and skipped frames. Reserve voice priority or an alternate cue for essential information when the mix is crowded.

**Exit decision.** The designer identifies which action changed. The creator plays the strongest alternative and records the preferred response, reference build and reason. Keep an observable cue in the reference clip so another tester can repeat the comparison.

### Phase 4  Add feedback after the action is legible

Use the accepted timing from Phase 2 and the cue hierarchy from Phase 3. Start with the smallest change that helps the player distinguish anticipation, contact or recovery. Compare visual effect alone, audio alone and the combined result. Add camera impulse, hit-stop, decals, reverb or ducking only when the comparison earns the cost.

| Under stress | What to observe | Adjustment to try |
| --- | --- | --- |
| A hit lands during pause or slow motion | The intended actors pause, menus still work and the next action occurs once. | Name the clock for simulation, animation, UI and audio. Choose local or global pause to fit the design. |
| Several events overlap | The warning stays visible and audible, including at the voice limit. | Reduce decorative layers before changing the critical cue. |
| Shake or effects are reduced | Timing and meaning remain clear with motion disabled and audio muted. | Retain a stable icon, pose or caption and replay the encounter. |

**Exit decision.** Keep the effect when it improves recognition on the same build route, fits measured budgets and preserves the reduced-effects experience. Reopen Phase 2 for altered timing or Phase 3 for a lost cue.

## First use and accessibility

### Phase 3  Verify the task from a fresh profile

Give a first-time player a goal such as “change controls, start a session, recognize the first warning, and resume after a pause.” Avoid giving the button sequence. Note the first hesitation, wrong action or point where help is needed. Keep that observation with the route and build. Make the smallest change, then repeat with a fresh profile and, where available, a new player.

| Path | Stress condition | Observable pass |
| --- | --- | --- |
| Find and change settings | Keyboard only or supported controller, remapped action, disconnect while a modal is open | Focus remains visible, cancel works, the prompt names the bound action, and settings survive restart. |
| Understand a warning | Audio muted, color cues removed, busy backgrounds and overlapping dialogue | The player can identify the event and required response through a second channel. Caption important non-speech sounds as needed. |
| Read and navigate | Largest supported text, narrowest supported view, long translation, missing glyph, diacritics and bidirectional text where relevant | Focus, text and buttons remain reachable. Wrapping, font fallback and reading order preserve meaning. |
| Play with reduced motion | Shake disabled, low-effects mode, rapid overlapping flashes and a scene transition | Critical cues survive. Review the composited sequence against the applicable photosensitivity guidance. |
| Complete onboarding | Skip a prompt, reload mid-tutorial, switch input, revisit with a completed save | Instructions recover, replay or dismiss as intended and progression remains possible. |

Use pseudo-localization early to expose layout defects. Include the longest real strings, translated builds and actual UI scale before accepting a locale. Review controller glyphs only for supported devices. If suitable player feedback or a required assessment is unavailable, record the coverage gap. Keep visual flash assessment separate from comfort preferences and storefront acceptance. [Microsoft localization testing](https://learn.microsoft.com/en-us/globalization/testing/how-to-perform-localization-testing) · [Xbox Accessibility Guidelines](https://learn.microsoft.com/en-us/xbox/accessibility/guidelines) · [Photosensitivity guidance](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/118)

**Exit decision.** Record the completed task, configuration, locale and residual barriers. A player who cannot dismiss a blocking prompt or perceive an essential warning has identified a gameplay defect.

## Performance and package cost

### Phase 5  Diagnose one limiting resource at a time

Use the same route, camera and build settings for baseline and candidate. Repeat the baseline to establish ordinary variation, then interleave baseline and candidate runs. Compare like cache states. A practical starting point is three paired runs per condition. Increase coverage if run-to-run variation could explain the result. Show per-run results and frame counts. Archive the slow trace as well as the typical one.

At 60 frames per second the nominal frame interval is 1000/60 ≈ 16.67 ms. At 120 it is ≈ 8.33 ms. Treat the chosen interval as a design target. Report median, 95th and 99th percentile, worst frame, number of hitches above the project’s threshold, and their positions. Separate presented intervals from CPU and GPU work times, which can overlap. A run with one severe stall can have an excellent 99th percentile.

| Suspected limit | Discriminating check | Candidate change and regression risk |
| --- | --- | --- |
| CPU work or waiting | Separate main/render thread work from frame cap, presentation and synchronization waits. Change one workload. | Reduce measured submission or simulation work. Check AI, collision, animation and warning visibility. |
| GPU cost | Lower render resolution for the same scene. Inspect GPU passes to distinguish shading, geometry, bandwidth or overdraw. | Reduce the costly pass, particles or detail level. Recheck silhouettes, telegraphs and UI at minimum quality. |
| Memory or streaming | Compare peaks and settled memory after identical scene cycles. Correlate stalls with reads, uploads or compilation. | Cap residency or reschedule loads. Reject a fix that trades the hitch for missing assets or an excessive load. |
| Patch or install | Update the previous supported package with one representative content change. Measure download, peak free-space need and install time. | Group assets by change frequency and stable layout. Check the installed build and old save after the update. |

**Exit decision.** Keep the change only if the observed improvement exceeds normal variability, the package still meets its agreed limits, and the original gameplay route passes. If results conflict across configurations, report each one and narrow the change or defer it. SteamPipe can transfer a small delta while rebuilding a large pack locally. [Valve SteamPipe documentation](https://partner.steamgames.com/doc/sdk/uploading)

## Candidate and release decision

### Gate 6  Rehearse delivery and recovery

Freeze the candidate manifest. Record its revision, package identity, build recipe, content and localization versions, and where matching symbols can be retrieved. For any allowed late change, name the defect, affected systems, new package identity, repeat tests and rollback owner. Classify severity by player consequence and the receiving project’s definitions.

Exercise a clean install and an update from the oldest supported installed version. Launch through the intended storefront or distribution channel. On the exact package, finish the critical progression route, reopen the latest save and an older save, restore settings and repeat the defining action. As applicable, add controller disconnect, user switch, suspend/resume, offline launch, network loss and conflicting cloud/local data. Document unavailable combinations. A private test channel can expose missing content that a development checkout supplies accidentally.

Rehearse withdrawing the candidate or restoring the last known-good build in an authorized test channel. Verify the previous binary can handle a save written by the candidate, or demonstrate a tested recovery path. If the update migrates saves irreversibly, plan a forward fix or protected recovery copy before release. Keep platform partner checklists and restricted evidence in their authorized systems. Use the current checklist for the actual target. For Steam, confirm the build and store page meet the applicable review requirements. [Valve review process](https://partner.steamgames.com/doc/store/review_process) · [Valve update testing](https://partner.steamgames.com/doc/store/updates)

### Decision record to copy into the project

| Field | Entry |
| --- | --- |
| Candidate and scope | Build ID/hash ___ · target and mode ___ · change since last accepted build ___ |
| Result | Route ___ · expected ___ · observed ___ · trace, clip or receipt ___ |
| Coverage | Tested configurations ___ · missing target or untested recovery path ___ |
| Risk and recovery | Player impact ___ · workaround or recovery ___ · owner and retest trigger ___ |
| Decision | Technical result ___ · creator decision and date ___ · distribution approval if applicable ___ |

**Disposition.** Record pass, hold, or an explicitly accepted exception. An absent required result stays open. A failed save recovery, blocked progression or unmatched package goes back to its owner. After an authorized release, route crash clusters and support reports by build ID, confirm the first player-visible symptom, and rerun the affected gate on the hotfix. Studio publication of this guide carries no game milestone decision.

## Workshop stress test results

Five bounded counterexamples were executed on November 21, 2026. Each paired an ordinary case with a change that could defeat a plausible acceptance rule. These results test the reasoning in the workshop. The release evidence for any game still comes from its target builds.

| Test and setup | Observed result | Change to the workshop |
| --- | --- | --- |
| Frame pacing. Use 1,000 intervals of 16 ms. Replace one with 120 ms. | Mean rose from 16 to 16.104 ms. Nearest-rank p99 stayed at 16 ms. Exactly one frame exceeded 50 ms. | Gate 5 retains maximum, hitch count and event location. A percentile alone would clear both traces. |
| Short tap. Sample held state at 0, 16 and 32 ms. Press at 4 ms and release at 22 or 8 ms. Also consume a recorded press edge once. | Held-state sampling recognized the long tap once and the short tap zero times. Buffered edge consumption recognized each once. | Gate 1 tests missed and duplicate input under different tick alignments. |
| Text fit. Use Arial at 20 px and a 230 px label area. Pad “View current mission” from 20 to 27 characters with periods. | The base label measured 184 px and the 35% expansion 226 px. “Aktuellen Missionsauftrag anzeigen” measured 313 px. | Gate 3 includes pixel width, real strings and the game’s actual font at supported scales. |
| Save recovery. Replace a disposable save with progress 60, a truncated copy, or a checksummed value of 160 on a 0–100 scale. Keep a valid backup at 40. | Validation loaded 60 for the intact case and recovered 40 in both failure cases. The impossible value had a valid checksum. | Gate 1 checks gameplay meaning and recoverable generations. The fixture models file errors. Hardware power loss needs target-specific evidence. |
| Patch layout. Start with 16 distinct 1 KiB blocks. Compare SHA-256 block identities after a one-byte replacement or insertion at the front. | Replacement changed 1 of 16 blocks. Insertion produced 17 of 17 blocks absent from the original set. | Gate 5 measures the delivered delta and local install work. The fixed-block model illustrates alignment sensitivity, not a store download forecast. |

**Tabletop challenge.** Suppose lowering animation update frequency saves CPU time but delays the warning pose. The performance result remains useful. Hold the change, restore the warning actor’s update path and repeat both traces. If the cue returns and the saving disappears, retain the baseline and investigate the next measured cost.

## Review of the original workshop

The concept workshop’s most useful decision was to stabilize the player’s action before decorating it. The master retains the seven stages and the profile–fix–verify loop. Three changes affect how a lead should use the original recommendations.

**Treat the sequence as a set of dependencies.** The introductory claim of one industry-standard closing structure was unsupported. The source’s role table works as a division of responsibilities. Its job titles and staffing levels are optional. Profiling, accessibility and packaging start early because each can reveal expensive rework before a formal freeze. The original execution summary now has explicit conditions for reopening an earlier stage.

**Replace universal implementation prescriptions with experiments.** Source sections 2–4 proposed deterministic reproduction, maximum input polling, a fixed queue-depth limit, pooling all recurring objects, and shader warmup as a route to eliminating hitches. The revised procedure measures the specific symptom and checks for side effects. Fixed timesteps and recorded seeds can still diverge. Queue depth trades latency for parallelism on some presentation paths. Pooled objects retain memory. An uncovered render state can still compile on first use. The simulation and recovery chapter identifies tests for each.

**Separate coverage from acceptance.** Sections 5–9 used a fixed expansion percentage, a named flash test, sample frame rates and an all-platform certification exit. These provide starting points with different scopes. The five experiments and primary references identify where additional evidence is needed. A measured improvement, a creator’s judgment of feel and a platform’s approval each answer a different question. The candidate record preserves all three.

### Run the next workshop on a real milestone

Choose the first open player-facing failure. Predict which measurement will change if the suspected cause is correct and which behavior must survive the fix. Capture the baseline once under recorded conditions. Apply the smallest reversible change and compare the same route. If it fails, retain the failed capture and revise the hypothesis. If it succeeds, try one adverse condition that would expose a false pass. Capture the conclusion with build identity and retest trigger in the receiving project.

For example, a late door-opening hitch might coincide with a new effect. Compare cold and warm entry, inspect the slow frame, and remove just the effect in a diagnostic candidate. If both cold runs still hitch, investigate activation or streaming before changing the effect budget. Carry forward a scoped finding only after the shipping configuration reproduces it.

**Source record.** Adapted from the supplied *Commercial Game Production: Master Finishing, Optimization, and Polish Pipeline*, sections 1–9. Links throughout this master identify the primary references used to check technical claims. The production choices and illustrative fixtures are Studio workshop recommendations. Recheck engine-version behavior, platform requirements and project authority when adopting them.
