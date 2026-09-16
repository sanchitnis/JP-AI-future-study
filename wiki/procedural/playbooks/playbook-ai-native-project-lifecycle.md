---
memory_tier: procedural
type: playbook
domains: [methodology, research-ops, project-lifecycle]
tags: [playbook, ai-native, knowledge-work, stages, committed-artifacts]
created: 2026-09-16
last_updated: 2026-09-16
---

# Playbook: AI-Native Project Lifecycle (6 Stages for Knowledge Work)

> **Core Insight**: Adapted from Anthropic's AI-Native SDLC and the [AI-Native Project Playbook](../../../ai-native-project-playbook.md). Once drafting runs at agent speed, the traditional bottleneck (writing) vanishes. The scarce resource is **human attention, judgment, and alignment**. Projects move not as a linear conveyor belt, but as a loop of **versioned, committed artifacts**.

---

## 🔄 The 6-Stage Loop

```
 ┌─────────────┐       ┌─────────────┐       ┌─────────────┐
 │ 1. ENVISION │ ----> │ 2. SCOPE    │ ----> │ 3. DRAFT    │
 │ (intent.md) │       │ (spec.md)   │       │ (draft.md)  │
 └─────────────┘       └─────────────┘       └─────────────┘
                                                    │
 ┌─────────────┐       ┌─────────────┐              ▼
 │ 6. ITERATE  │ <---- │ 5. PUBLISH  │ <---- ┌─────────────┐
 │(feedback.md)│       │ (final.*)   │       │ 4. REVIEW   │
 └──────┬──────┘       └─────────────┘       │ (review.md) │
        │                                    └─────────────┘
        └──────────────(Restarts loop as next intent.md)
```

---

## Stage-by-Stage Protocol

### Stage 1: Envision → Capture `intent.md`
- **Objective**: Pin down the raw problem, target audience, affected stakeholders, constraints, and explicit definition of "done".
- **AI-Native Habit**: As soon as an idea or policy challenge surfaces in a study group session, capture it in an `intent.md` rather than trusting human memory or meeting notes.
- **Key Questions**:
  1. What is the core problem or opportunity?
  2. Who is the specific audience (e.g. MeitY policymakers, school administrators, think-tank researchers)?
  3. What does "done" look like (exact format, length, actionable outcome)?
  4. What constraints exist (timeline, word count, non-negotiables, sensitive stances)?
- **Committed Artifact**: `intent.md`

### Stage 2: Scope & Synthesis → Lock Structure in `spec.md`
- **Objective**: Compress requirements, section outlines, tone, and evidence sources into one working session before drafting begins.
- **Synthesis Requirement for Deep Research**: For research studies or whitepapers, this stage MUST include the creation of an Evidence Matrix or a Synthesis document. Agents should cross-reference `wiki/semantic/sources/` to build a grounded factual baseline before any drafting starts.
- **The Split Rule**:
  - *Skip `spec.md`* for quick, low-stakes memos (merge into `intent.md`).
  - *Keep `spec.md`* for high-stakes deliverables (policy briefs, whitepapers, curricula). If a wrong assumption would cost >1 hour to unwind, write the spec.
- **Committed Artifact**: `spec.md` (and optional `evidence-matrix.md` for Deep Track)

### Stage 3: Draft → Agent Drafts; Human Supplies Judgment in `draft.md`
- **Objective**: Generate the full draft at agent speed while anchoring strictly to project `context.md` and relevant certified skills.
- **Rules of Engagement**:
  - The human directs, supplies grounded sources (centrally managed in `raw/literature/` and referenced via `wiki/semantic/sources/`), and evaluates arguments.
  - The agent produces sentences, structures arguments, and embeds citations.
  - Maintain a project `context.md` file so every session can start cold without re-briefing.
- **Committed Artifact**: `draft.md`

### Stage 4: Review → Layered Continuous Verification in `review.md`
- **Objective**: Multi-tiered verification rather than an unguided final read.
- **Verification Layers**:
  1. *Layer 1 (Automated/Agent)*: Grounding audit (does every factual claim link to a wiki source?), structure check against `spec.md`, contradiction check with prior positions.
  2. *Layer 2 (Human Domain Expert)*: Political nuance, ethical implications, strategic framing, and unquantified assumptions.
- **Committed Artifact**: `review.md`

### Stage 5: Publish → Sign-off & Finalize `final.*`
- **Objective**: Formal commitment of the deliverable (policy brief, curriculum module, executive brief).
- **Protocol**: Human domain expert provides final sign-off on flagged items in `review.md`. The draft is promoted to `final.md` (or PDF/presentation).
- **Committed Artifact**: `final.md` (or `final.pdf`, `final.docx`)

### Stage 6: Iterate → Close the Loop in `feedback.md`
- **Objective**: Capture real-world reception, stakeholder reactions, and downstream research questions.
- **Document Loop Trigger**: Feedback is not an archived email thread; it is a committed `feedback.md` that immediately seeds the next project's `intent.md`.
- **Committed Artifact**: `feedback.md`

---

## 🔗 Cross-References
- Playbook: [[playbook-committed-artifacts|Committed Artifacts Standard]]
- Playbook: [[playbook-skills-certification-pipeline|Skills Certification Pipeline]]
- Playbook: [[playbook-process-reflection-cadence|Process Reflection Cadence]]
- Master Playbook Source: [ai-native-project-playbook.md](../../../ai-native-project-playbook.md)
