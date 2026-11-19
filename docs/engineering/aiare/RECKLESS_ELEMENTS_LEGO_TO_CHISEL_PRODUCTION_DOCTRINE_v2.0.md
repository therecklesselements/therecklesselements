# RECKLESS ELEMENTS
# AIARE LEGO-TO-CHISEL PRODUCTION DOCTRINE
## Version 2.0

**Issued:** November 19, 2026  
**Status:** Current production-method specification; controlled field validation pending  
**Authority:** RECKLESS ELEMENTS Studio  
**Governing philosophy:** HYPEROP v1.2  
**Supporting research method:** AIARE v1.0.0

---

## 1. Mission

Achieve the fastest practical production of original, commercially viable games by assembling, connecting, configuring, and customizing existing proven gameplay technology, with AI agents performing the technical implementation that would otherwise require a larger programming team.

**Primary objective:** Maximum functional reuse. Minimum original engineering. Earliest possible playable game.

The creator operates as creative director, game designer, and product authority. Codex performs the technical research, programming, editor operations, integration, adaptation, debugging, testing, and build work wherever reliable automation is available.

The creator should not be expected to write gameplay code or perform repetitive technical editor operations that Codex or a validated engine integration can reliably perform. Human creative judgment, direction, approvals, and final experience evaluation remain essential.

## 2. Fundamental principle

**The original creative vision comes first. Existing technology supplies the structure. Original development supplies only what the structure cannot.**

We do not invent a game around available assets.

We identify the intended game, translate its defining experience into functional requirements, locate the closest existing playable foundations, and assemble them into a recognizable approximation of the original vision.

We then refine that assembled structure until it realizes the intended game.

The game's identity determines which components we assemble — never the other way around.

The objective is not to achieve a particular percentage of visual scripting, reused code, or AI-generated code. The objective is to remove programming and technical setup as bottlenecks to creative production.

## 3. The distinction that governs the method

Visual scripting and prebuilt gameplay functionality are different things.

- **Visual scripting** lets a creator construct logic through graphs, nodes, events, and state machines. It can reduce conventional coding, but the logic still has to be designed and assembled.
- **A gameplay framework or complete template** already supplies functioning systems such as movement, combat, targeting, enemy behavior, inventory, saving, or progression.
- **Configuration and data authoring** change the behavior or content of existing systems without rewriting their underlying mechanics.
- **Codex integration work** connects systems, adapts existing functionality, repairs incompatibilities, and writes the smallest necessary bridge or missing component.

For this production model, finding a suitable complete gameplay foundation is generally more valuable than merely finding a visual scripting system.

Use visual scripting where it materially improves designer autonomy, event authoring, encounters, and content iteration. Do not force every system into graphs. Stable, performance-sensitive, state-critical, or heavily tested logic may remain in C# or the selected engine's native programming language, with Codex responsible for its implementation and maintenance.

## 4. AIARE functional discovery

AIARE identifies what the intended experience requires before implementation begins.

For each concept or major feature:

1. Examine the original creative brief and approved design material.
2. Study reference games to identify the behaviors and interactions that create the intended experience.
3. Convert those observations into functional requirements: inputs, outputs, state transitions, timing, dependencies, edge cases, and failure behavior.
4. Search the studio's existing work, engine-native features, complete templates, sample projects, source-available implementations, marketplace frameworks, plugins, visual graphs, scripts, and prefabs.
5. Compare actual functionality rather than marketing descriptions or asset thumbnails.
6. Stop investigating when a suitable, licensed working foundation or defensible specification answers the production need.

Research is decision-oriented, not endless. Every investigated requirement must end in one of these decisions:

- **REUSE** — an existing compatible implementation satisfies the requirement.
- **CONFIGURE** — existing functionality satisfies it after data or editor configuration.
- **ADAPT** — a suitable system needs bounded modification.
- **BUILD LIMITED BRIDGE** — existing systems need a small integration component.
- **INVESTIGATE FURTHER** — a specific unresolved question prevents a decision.
- **STOP / RIGHTS BLOCKED** — licensing, access, compatibility, or provenance prevents use.

AIARE must not become a reason to reverse-engineer unnecessarily. Prefer primary documentation, legitimate source-available code, observable behavior, and licensed implementations. Targeted technical analysis is justified only when it resolves a real production question. Decompiled proprietary code or extracted third-party assets are not automatically licensed for commercial use.

## 5. The reuse hierarchy

Search and evaluate in this order:

1. **Single largest usable licensed gameplay chassis** — a complete template, starter project, or coherent framework that already resembles the intended game.
2. **Matching complete samples** — official samples or demonstrators that supply missing portions of the core loop.
3. **Compatible modules** — combat, inventory, AI, interaction, traversal, dialogue, quests, progression, networking, or other required systems.
4. **Engine-native configuration and events** — prefabs, data assets, visual scripting, animation systems, timelines, editor tools, and built-in functionality.
5. **Small Codex integration bridges** — the minimum code or editor automation needed to connect compatible components.
6. **Adaptation of existing systems** — only where configuration and a small bridge are insufficient.
7. **Original engineering** — last resort, or when the defining IP experience genuinely requires it.

Prefer one coherent foundation plus the fewest compatible supporting modules. Do not assemble a large collection of unrelated plugins before determining whether a complete chassis already provides most of the intended experience.

A pile of assets is not a gameplay foundation. A compiling project is not a playable game.

## 6. Engine selection is per IP

THE RECKLESS ELEMENTS does not require every project to use the same engine.

Choose the engine and foundation that minimize the total remaining work for that specific IP. Evaluate:

- Availability and completeness of suitable gameplay chassis.
- Coverage of the game's defining mechanics.
- Quality and maturity of relevant frameworks and modules.
- Native visual scripting and designer-facing configuration.
- How easily Codex can inspect, create, modify, and test project content.
- Reliability of editor automation and command-line tooling.
- Compatibility with the target platform and the actual development computer.
- Runtime performance and iteration speed.
- Version compatibility and dependency burden.
- Maintenance status, support, documentation, and community evidence.
- Commercial licensing, redistribution rights, and total cost.
- The amount of original programming and manual editor work still required.

### Initial engine assessment from the source workshop

These are starting hypotheses from the November 2026 workshop, not permanent studio-wide rankings. Recheck current versions, product availability, pricing, licensing, and integration maturity before committing to a project.

| Engine | Potential advantage for this method | Important limitation to test |
|---|---|---|
| Unreal Engine | Native Blueprints and substantial built-in 3D gameplay, animation, AI, and cinematic tooling | Blueprint asset editing requires a reliable editor-connected workflow; do not assume Codex can safely edit binary assets as ordinary text |
| Unity | Existing studio experience, C# accessibility to Codex, text-serialized project assets, and third-party gameplay frameworks such as Game Creator 2 | Unity Visual Scripting is not itself a complete gameplay framework; validate the selected framework and its module compatibility |
| Godot | GDScript and text-based scenes are accessible to coding agents; Orchestrator is a visual-graph candidate | Confirm that a suitable complete gameplay chassis and compatible modules exist for the intended project |

The workshop's initial comparison identifies Unreal as the strongest native visual-scripting candidate, Unity with a suitable gameplay framework as a strong prefabricated-development candidate, and Godot as a lightweight code-agent-oriented alternative. These assessments require project-specific testing.

FATDOG remains in Unity. Its working prototype is not to be migrated or disrupted merely to test another engine.

## 7. Designer autonomy and the Sandfall lesson

The useful lesson from Sandfall Interactive is not a numerical target for how much code must be written visually.

It is the production structure:

- A small technical foundation exposes reliable building blocks.
- Designers and artists can configure and combine those building blocks independently.
- Native engine functionality is used before proprietary tooling is invented.
- Content, events, encounters, and presentation can be changed without repeatedly rewriting core mechanics.

For Unity, a practical hybrid may use:

| Responsibility | Candidate Unity capability |
|---|---|
| Stable underlying rules and systems | Small, tested C# foundation |
| Content definitions and tuning | ScriptableObjects and data assets |
| Events and interactions | Unity Visual Scripting, events, and existing framework actions |
| Presentation and sequencing | Timeline and Cinemachine |
| AI authoring | Unity Behavior or a compatible existing behavior system |
| Visual effects | VFX Graph and Particle System |
| Materials | Shader Graph |
| Environment assembly | Prefabs, ProBuilder, URP, and native editor tools |
| Quality | Unity Test Framework, Profiler, and reproducible builds |

This is a menu of candidate capabilities, not a mandatory package list. Select only what the project needs.

The underlying architecture should make common content variations possible through data and configuration. For example, once a consumption system exists, a new food item should ideally be definable through an asset containing its mass, growth multiplier, score, reaction type, and presentation events — without rewriting the consumption rules.

The same principle applies to abilities, enemies, weapons, loot, encounters, dialogue, and environmental interactions.

## 8. Integration discipline — prevent the incompatible-module problem

Every prototype needs one primary framework responsible for shared core state wherever practical.

Establish clear ownership of:

- Input.
- Player and character state.
- Movement and physics.
- Combat state and damage resolution.
- Targeting and interaction.
- Inventory and equipment.
- Progression and game state.
- Saving and loading.

Supporting modules must connect through small, documented interfaces. They must not compete to own the same state or independently replace core systems without an explicit architecture decision.

Before integration, Codex must inspect:

- Exact engine and editor version.
- Package and module versions.
- Dependency graph.
- Shared state ownership.
- Input and event conventions.
- Data and save formats.
- Required editor or runtime hooks.
- Known bugs and maintenance status.
- Licensing and commercial redistribution rights.
- Installation reproducibility and rollback path.

Pin dependencies during prototype development. Preserve a known working baseline. Test each major integration before adding another.

The goal is not to avoid all integration work. It is to prevent the cost of connecting incompatible systems from exceeding the work saved by reusing them.

## 9. Automation mandate and division of labor

### Creator — creative director and product authority

The creator supplies and approves:

- Original IP and product vision.
- Desired player experience.
- Creative and gameplay decisions.
- Visual identity and art direction.
- Priorities and acceptance criteria.
- Final judgment of game feel and presentation.

The creator should not be required to write gameplay code or manually repeat technical editor operations that a validated agent integration can perform.

### Codex — technical implementation team

Codex is responsible for:

- Researching candidate foundations and documentation.
- Inspecting project structure and dependencies.
- Installing and configuring approved components.
- Importing and assembling systems.
- Creating and configuring scenes, prefabs, assets, graphs, and data.
- Connecting events and gameplay systems.
- Writing limited integration code or missing functionality.
- Debugging, testing, profiling, and building.
- Recording decisions, dependencies, and reproducible instructions.

Use direct engine/editor automation wherever supported. If a required editor operation cannot be automated reliably, identify the exact limitation and reduce the manual task to the smallest necessary action. Never claim an editor action occurred without evidence.

## 10. The production sequence

### Stage 1 — Original vision

Define the intended game before selecting technology:

- IP identity and player fantasy.
- Core activity and gameplay loop.
- Defining mechanic or interaction.
- Required systems and content.
- Visual and presentation direction.
- Reference games and relevant behaviors.
- Non-negotiable creative requirements.

### Stage 2 — AIARE functional analysis

Translate the vision into a functional requirements inventory. Identify system dependencies and the minimum playable experience that must be proven.

### Stage 3 — Chassis discovery and feasibility

Search for the largest coherent foundation first. Produce an Assembly Feasibility Report identifying:

- Exact candidate projects, frameworks, templates, and versions.
- Which required systems already work.
- Which requirements need configuration, modules, bridges, adaptation, or original code.
- Compatibility and state ownership.
- Editor automation requirements.
- Licensing and commercial-use status.
- Maintenance and support risks.
- Costs and expected manual work.
- Evidence from actual demos, tests, and builds.

Do not purchase a framework or commit to an engine until the feasibility report supports the decision and any required approval has been obtained.

### Stage 4 — LEGO assembly

Use Codex to import, configure, connect, and adapt the chosen foundation. Prefer existing systems and editor-native tools. Keep new engineering small and explicitly tied to a missing requirement.

Preserve working milestones. Use isolated worktrees or project copies for experiments. Do not make simultaneous uncontrolled changes to the same project or editor state.

### Stage 5 — First playable greybox / alpha

The first major milestone is a standalone, playable approximation of the intended game.

It must:

- Start from a clean launch.
- Demonstrate the defining interaction in simplified form.
- Connect the required core systems.
- Complete the smallest intended prototype objective.
- Preserve the original game's defining experience rather than merely resembling its genre.
- Produce reproducible test evidence and a standalone build.

Placeholder visuals are acceptable. Missing core behavior is not.

This milestone must satisfy the relevant HYPEROP Minimum Fun Proof and Complete Loop Proof gates. Technical completion does not establish player enjoyment or creative success.

### Stage 6 — Chisel and sculpt

Once the macro gameplay works, progressively realize the original IP:

- Replace placeholder art and content.
- Refine original mechanics.
- Develop characters and environments.
- Replace or adapt animations.
- Refine combat, encounters, and progression.
- Introduce narrative, sound, and presentation.
- Improve balance, responsiveness, game feel, and interface.
- Replace reused elements when they prevent the intended identity or quality.

Preserve reliable systems unless modification materially improves the result.

Do not defer the defining mechanic until after the greybox. It must be represented from the earliest playable proof; later refinement makes it distinctive and complete.

### Stage 7 — Production Kit extraction

The RECKLESS ELEMENTS Production Kit is an accumulating library of proven reusable components, not a precondition for making the first game.

Extract a component only after it has worked reliably in an actual project and its reusable boundary is understood.

Potential categories:

- Core: events, state conventions, input conventions, common utilities.
- Content: data definitions, prefab conventions, configuration patterns.
- Presentation: timeline sequences, camera reactions, audio/VFX triggers.
- AI: reusable behavior patterns and state transitions.
- Quality: automated tests, profiling, build validation, and regression tools.

A project-specific mechanic may remain unique. Reuse the genuinely common systems around it. Do not build a large proprietary engine or universal framework before actual games prove the need.

### Stage 8 — Commercial production and polish

Complete the HYPEROP vertical-slice, production, performance, and polish gates. Validate functionality, player experience, creative quality, compatibility, performance, content provenance, builds, and release readiness.

## 11. First controlled field experiment

**Preferred test candidate from the workshop:** one SERAPHIN MACHINA infected combat encounter, in a completely isolated project, using the Unreal Engine 5.8 Third Person Combat variant as the first chassis candidate.

This is a test of the production method, not an approved permanent engine choice or a commitment to purchase anything.

### Assembly objective

- Reuse an existing playable character and combat foundation.
- Adapt existing enemy behavior into one basic P.A.R.I.A.H. infected encounter.
- Reuse an existing trigger, pickup, or objective mechanism to complete the encounter and reach an exit.
- Have Codex perform the technical assembly, integration, missing bridges, debugging, and testing.
- Produce a reproducible standalone build.

Before proceeding, verify the actual engine/template version, functionality, licensing, and Codex-compatible editor automation. If the Unreal candidate cannot be operated and validated reliably, compare an equivalent Unity foundation such as the Game Creator 2 candidate identified in the workshop. Godot remains eligible if AIARE discovers a stronger suitable chassis.

Do not modify FATDOG for this experiment. Do not purchase a third-party framework before the free foundation has been inspected and the feasibility report reviewed.

### Measurement

Record:

- Existing gameplay systems reused.
- Required modules and dependencies.
- Original code written by Codex.
- Manual creator actions.
- Editor automation success and failure.
- Integration defects and rework.
- Time to first playable build.
- Time to a complete encounter.
- Whether the defining interaction works.
- Whether the result can be customized without further gameplay code.
- Standalone build and test results.

This is the first evidence for the studio's production model. It is not proof of a universal percentage reduction in development time.

## 12. Acceptance and evidence rules

A major integration is accepted only when the relevant behavior is demonstrated, not merely when packages install or code compiles.

Keep separate acceptance judgments for:

- Functional correctness.
- Complete playable loop.
- Player experience.
- Creative identity.
- Technical performance.
- Compatibility and maintainability.
- Commercial rights and provenance.

Record PASS, FAIL, BLOCKED, NOT_RUN, or STALE. PASS requires reproducible evidence and an independent check appropriate to the risk.

Reported external examples may establish feasibility signals, but they do not prove the studio's own production savings. The workshop identifies commercial AI-assisted releases, advanced AI-directed prototypes, and template/asset assembly demonstrations; it does not establish a fully verified example of a complex polished commercial game produced with virtually no original engineering.

Never promise a 90–95% reduction in development effort before measuring the studio's own representative prototype.

## 13. Governing directive

**Find the complete chassis. Assemble the functional game. Prove the experience. Chisel the original creation.**

Original vision determines the destination. AIARE identifies the requirements. Reuse supplies the largest working foundation. Codex performs the technical work. Independent testing proves the result. The creator directs the experience and its final identity.

This doctrine operates under HYPEROP v1.2 and the AIARE Research Harness Blueprint v1.0.0. It does not override either document, authorize unlicensed reuse, or authorize changes to protected production projects without approval.

**Field-validation status:** Not yet demonstrated by the controlled SERAPHIN MACHINA experiment.
