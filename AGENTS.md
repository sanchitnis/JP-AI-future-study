# AGENTS.md — JP AI Future Study Group (Project & Knowledge Hub)

This repository is the central operating hub for the **JP AI Future Study Group** (Jnana Prabodhini — 176 members, 13 recorded seminars across technology, governance, labor, neuroscience, cyber, and geopolitics).

It operates on a **dual-engine architecture** combining:
1. **The Collective Memory Engine (Wiki)**: A persistent 5-tier Cognitive Memory architecture (Episodic, Semantic, Reflective, Working, Procedural) inspired by Andrej Karpathy's LLM wiki paradigm.
2. **The AI-Native Project Engine**: An active deliverable production system (policy briefs, curricula, whitepapers, concept notes) governed by the 6-stage loop of committed artifacts from [ai-native-project-playbook.md](file:///d:/sanjay/JP-AI-future-study/ai-native-project-playbook.md).

**Read `index.md` before doing anything else in a session.** It is the living dashboard linking active projects, collective memory, playbooks, and reflections.

---

## 🏛️ The Dual-Engine Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           JP AI FUTURE STUDY GROUP HUB                                  │
└────────────────────────────────────────────┬────────────────────────────────────────────┘
                                             │
               ┌─────────────────────────────┴─────────────────────────────┐
               ▼                                                           ▼
┌──────────────────────────────┐                            ┌──────────────────────────────┐
│  COLLECTIVE MEMORY (wiki/)   │                            │   PROJECT TRACKS (projects/) │
├──────────────────────────────┤                            ├──────────────────────────────┤
│ 1. Episodic (Seminars/Logs)  │ ◄────── Grounding ───────► │ • intent.md (Stage 1: Plan)  │
│ 2. Semantic (Concepts/Facts) │                            │ • spec.md (Stage 2: Design)  │
│ 3. Reflective (Perspectives) │                            │ • draft.md (Stage 3: Build)  │
│ 4. Working (Primers/Notebook)│                            │ • review.md (Stage 4: Test)  │
│ 5. Procedural (SOPs/Playbooks│                            │ • final.md (Stage 5: Deploy) │
└──────────────────────────────┘                            │ • feedback.md (Stage 6: Loop)│
               │                                            └──────────────────────────────┘
               │                                                           │
               └─────────────────────────────┬─────────────────────────────┘
                                             │
                              ┌──────────────┴──────────────┐
                              ▼                             ▼
               ┌─────────────────────────────┐ ┌─────────────────────────────┐
               │   GOVERNED SKILLS PIPELINE  │ │     PROCESS REFLECTIONS     │
               │      (.agents/skills/)      │ │        (reflections/)       │
               │  Human-in-the-Loop Gate for │ │  Quarterly Slow-Loop Audits │
               │  Repeated Rule Corrections  │ │  of Stage ROI & Attention   │
               └─────────────────────────────┘ └─────────────────────────────┘
```

---

## 📜 Standing Operational Principles

### 1. Wiki Grounding & Immutability (`wiki/`, `raw/`)
- `raw/` is immutable: never edit raw source documents, transcripts, or gazette PDFs.
- Every factual claim, statistic, or quote in a project or wiki node must link back to atomic evidence in `wiki/semantic/sources/`.
- Maintain all 5 cognitive tiers (`memory_tier: episodic | semantic | reflective | working | procedural`).

### 2. AI-Native Project Discipline (`projects/`)
- Knowledge work runs on **committed artifacts**, not ephemeral chats or meeting memory.
- Every stage ends by writing a durable markdown file; the next stage begins by reading it cold.
- **The Spec Rule**: High-stakes deliverables must lock `spec.md` (structure, scope, non-goals, audience tone) before drafting begins.
- **Human Attention is Scarce**: The agent supplies drafting speed, structure, and atomic citations; human domain experts supply architectural direction, political nuance, and critical review.

### 3. Governed Skills Pipeline
- **Rule of Two**: If a reviewer corrects the same convention or concept twice, turn it into a candidate skill (`rule + concrete example`).
- **Expert Review Gate**: No skill runs unsupervised until certified by the corresponding domain expert lead. Unverified skills are never committed.

### 4. Dual Feedback Loops
- **Fast Document Loop**: Stakeholder reception in `feedback.md` immediately triggers the next cycle's `intent.md`.
- **Slow Process Loop**: Quarterly audits in `reflections/` review stage ROI, human attention allocation, and skill freshness.

### 5. Living Dashboard & Audit Trail
- Always update [index.md](file:///d:/sanjay/JP-AI-future-study/index.md) when adding or modifying projects, wiki nodes, or playbooks.
- Append every significant operation to [log.md](file:///d:/sanjay/JP-AI-future-study/log.md).

---

## 📝 Activity Log Format

Each `log.md` entry follows:
```markdown
## [YYYY-MM-DD] project|ingest|perspective|tutor|learning|skill|reflection|lint | <Short Title>
- Summary of action taken, component affected, files modified/created, and relevant expert leads.
```

---

## ⚙️ Git Workflow

- Conventional commits: `project(<slug>): ...`, `wiki(<tier>): ...`, `skill: ...`, `reflection: ...`.
- All final deliverables require peer review in `review.md` before promotion to `final.md`.
