---
name: jp-ai-study-group-hub
description: Maintain and operate the JP AI Future Study Group Project Hub, orchestrating both the 5-tier Cognitive Memory Wiki and the 6-stage AI-Native Project lifecycle (Plan -> Design -> Build -> Test -> Deploy -> Maintain). Use whenever the user wants to ingest a source, explore seminar notes, develop a policy brief or curriculum, certify a skill, or conduct a process reflection.
---

# JP AI Future Study Group Hub (Dual-Engine Edition)

You operate a living **AI-Native Study Group Project Hub** that pairs an active knowledge work production engine with a persistent 5-tier Collective Memory Wiki.

---

## 🏛️ Repository Layout

```text
AGENTS.md             Standing constitutional instructions
index.md              Master Dashboard linking Projects, Memory, Playbooks & Reflections
log.md                Append-only chronological activity log
projects/             Active & delivered knowledge deliverables (intent -> spec -> draft -> review -> final -> feedback)
  policy-brief-...    Sovereign AI Compute Policy Brief
  curriculum-...      Vernacular Voice AI FLN Curriculum
  concept-note-...    IT/BPO Centaur Workforce Resilience
  _template-project/  Reusable 6-stage project scaffold
reflections/          Quarterly process reflection audits (stage ROI, attention allocation, skill drift)
raw/                  Immutable raw source artifacts (never edit directly)
wiki/                 Collective Memory Engine
  episodic/           Dated seminar sessions (13 study group meetings), interviews, events
  semantic/           Grounded concepts, entities, atomic sources, and comparisons
  reflective/         Dialectic perspective matrices and consensus whitepapers
  working/            Primers, syllabi, and Google NotebookLM bridge packs
  procedural/         AI-native operational playbooks and Obsidian templates
```

---

## 🔁 Core Operations

### 1. Project Operations (6-Stage AI-Native Loop)
- **Plan**: Create `intent.md` defining problem, audience, definition of done, and constraints.
- **Design**: Lock `spec.md` with section outline, non-goals, and reading level.
- **Build**: Generate `draft.md` anchoring to `context.md` and grounded sources.
- **Test**: Run Layer 1 agent checks and Layer 2 human domain expert sign-off in `review.md`.
- **Deploy**: Promote verified deliverable to `final.md`.
- **Maintain**: Capture reception in `feedback.md` and seed the next cycle's `intent.md`.

### 2. Governed Skills Pipeline
- If a correction occurs twice, draft a candidate skill (`rule + concrete example`).
- Route to the domain expert lead for formal certification before graduation into `.agents/skills/`.

### 3. Collective Memory Ingestion & Query
- Ingest episodic seminars into `wiki/episodic/meetings/` and papers into `wiki/semantic/sources/`.
- Answer questions by citing specific atomic nodes (`[[filename|Title]]`).

### 4. Process Reflections
- On quarterly cadence, audit stage ROI, human attention, and skill drift in `reflections/`.
