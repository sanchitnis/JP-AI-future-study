# JP AI Future Study Group — AI-Native Knowledge & Research Hub

Welcome to the **JP AI Future Study Group Project Hub** (Jnana Prabodhini — 176 members, 13 expert seminars from August 2025 to August 2026).

This repository operates as an **AI-Native Knowledge Laboratory** adapted from Anthropic's AI-Native SDLC and the [AI-Native Project Playbook](./ai-native-project-playbook.md). It combines an active **Project Production Engine** with a persistent 5-tier **Collective Memory Wiki**.

---

## 🏛️ System Architecture

```
                                  ┌──────────────────────────────────┐
                                  │   JP AI FUTURE STUDY GROUP HUB   │
                                  │  (176 Members • 13 Seminars)     │
                                  └─────────────────┬────────────────┘
                                                    │
                   ┌────────────────────────────────┴────────────────────────────────┐
                   ▼                                                                 ▼
    ┌──────────────────────────────┐                                  ┌──────────────────────────────┐
    │  COLLECTIVE MEMORY (wiki/)   │                                  │   PROJECT TRACKS (projects/) │
    ├──────────────────────────────┤                                  ├──────────────────────────────┤
    │ • Episodic (Seminars & Logs) │ ◄────── Grounded Evidence ─────► │ • intent.md (Stage 1: Plan)  │
    │ • Semantic (Concepts/Sources)│                                  │ • spec.md (Stage 2: Design)  │
    │ • Reflective (Debate Maps)   │                                  │ • draft.md (Stage 3: Build)  │
    │ • Working (Primers/Notebook) │                                  │ • review.md (Stage 4: Test)  │
    │ • Procedural (Playbooks/SOPs)│                                  │ • final.md (Stage 5: Deploy) │
    └──────────────────────────────┘                                  │ • feedback.md (Stage 6: Loop)│
                   │                                                  └──────────────────────────────┘
                   │                                                                 │
                   └────────────────────────────────┬────────────────────────────────┘
                                                    │
                                   ┌────────────────┴────────────────┐
                                   ▼                                 ▼
                    ┌──────────────────────────────┐  ┌──────────────────────────────┐
                    │   GOVERNED SKILLS PIPELINE   │  │     PROCESS REFLECTIONS      │
                    │      (.agents/skills/)       │  │        (reflections/)        │
                    │   Human Expert Review Gate   │  │ Quarterly Slow-Loop Retros   │
                    │   for Certified Standards    │  │ on Stage ROI & Attention     │
                    └──────────────────────────────┘  └──────────────────────────────┘
```

---

## 🌟 The Core Components

### 1. Active Project Tracks (`projects/`)
Delivers high-stakes knowledge artifacts through the 6-stage committed artifact loop:
- [`policy-brief-sovereign-ai-compute`](./projects/policy-brief-sovereign-ai-compute/): Sovereign compute vouchers, GPU cloud infrastructure, and green power tariffs.
- [`curriculum-foundational-ai-literacy`](./projects/curriculum-foundational-ai-literacy/): 4-week vernacular voice AI educator workshop for NIPUN Bharat.
- [`concept-note-ai-workforce-resilience`](./projects/concept-note-ai-workforce-resilience/): Navigating the Centaur shift and billing-hour collapse in Indian IT/BPO services.
- [`_template-project`](./projects/_template-project/): Standard 6-stage starter scaffold.

### 2. Collective Memory Wiki (`wiki/`)
Persistent knowledge engine across 5 Cognitive Memory tiers:
- **Episodic**: 13 seminar session notes and verified recordings ([[ai-meetings-overview]]).
- **Semantic**: Factual world knowledge, institutions ([[bharatgen]], [[indiaai-mission]]), concepts, and atomic claim sheets.
- **Reflective**: Multi-stakeholder dialectic debate matrices ([[india-frontier-models-vs-applications]], [[ai-impact-on-indian-it-jobs]]).
- **Working**: Socratic primers, syllabi, and Google NotebookLM bridge packs ([[pack-india-sovereign-ai]]).
- **Procedural**: Operational playbooks and reusable Obsidian blueprints.

### 3. AI-Native Operating Playbooks (`wiki/procedural/playbooks/`)
- [[playbook-ai-native-project-lifecycle|AI-Native Project Lifecycle Playbook]]: How non-coding knowledge work runs on committed artifacts.
- [[playbook-committed-artifacts|Committed Artifacts Standard]]: Rules for zero oral context and cold-open readability.
- [[playbook-skills-certification-pipeline|Skills Certification Pipeline]]: Turning repeated human corrections into certified agent skills.
- [[playbook-process-reflection-cadence|Dual Feedback Loops Playbook]]: Document Loop (`feedback.md`) vs Process Loop (`reflections/`).

### 4. Governed Skills Pipeline (`.agents/skills/`)
Ensures that no agent standard runs unsupervised until certified by a human domain expert:
- `ai-native-project-engine`: Orchestrates stages 1 through 6 and manages transitions.
- `skill-certification-pipeline`: Extracts rules and examples from repeated corrections for expert sign-off.
- Domain skills: Ingestion, dialectic mapping, Socratic tutoring, curriculum generation, NotebookLM export, and integrity linting.

### 5. Process Reflections Cadence (`reflections/`)
The second, slower feedback loop auditing stage ROI, reviewer attention, and skill drift:
- [Q1 2026 Process Reflection](./reflections/2026-q1-study-group-reflection.md).

---

## 📂 Repository Layout

```text
├── .agents/
│   ├── skills/                                # Governed Agent Skills (Lifecycle, Ingest, Perspectives, Tutor, etc.)
│   └── references/taxonomy.md                 # Cognitive frontmatter schema & taxonomy
├── projects/                                  # Active & Deployed Knowledge Work Projects
│   ├── _template-project/                     # Reusable 6-stage scaffold (intent, spec, draft, review, final, feedback)
│   ├── policy-brief-sovereign-ai-compute/     # Sovereign compute brief (Stage 5 Deployed)
│   ├── curriculum-foundational-ai-literacy/   # Voice AI FLN curriculum (Stage 5 Deployed)
│   └── concept-note-ai-workforce-resilience/  # IT/BPO Centaur transition memo (Stage 5 Deployed)
├── raw/                                       # Immutable source store (papers, PDFs, transcripts)
├── reflections/                               # Quarterly Process Loop Retrospectives
│   ├── README.md & reflection-template.md     # Process reflection framework
│   └── 2026-q1-study-group-reflection.md      # Inaugural audit
├── wiki/
│   ├── episodic/                              # Seminars, interviews, and session logs (13 meetings)
│   ├── semantic/                              # Grounded concepts, entities, sources, comparisons
│   ├── reflective/                            # Dialectic matrices and consensus papers
│   ├── working/                               # Primers, study guides, and NotebookLM packs
│   └── procedural/                            # Operating playbooks & markdown templates
├── index.md                                   # Master Hub Dashboard linking Projects & Memory
├── log.md                                     # Append-only chronological activity log
├── AGENTS.md                                  # Repository Constitution and operational rules
├── GETTING-STARTED.md                         # Quick-start onboarding guide
└── CONTRIBUTING.md                            # Open collaboration & peer review guidelines
```

---

## 🚀 Quick Navigation

- **Master Hub & Catalog**: [index.md](./index.md)
- **Active Projects Board**: [projects/README.md](./projects/README.md)
- **Process Reflections**: [reflections/README.md](./reflections/README.md)
- **Seminar Series Index**: [ai-meetings-overview](./wiki/episodic/meetings/ai-meetings-overview.md)
- **Activity Log**: [log.md](./log.md)

---

## 📄 Attribution & Community
Maintained by the **Jnana Prabodhini AI & Future of Humanity Study Group**.  
Built on [Obsidian](https://obsidian.md) and inspired by Anthropic's AI-Native SDLC and Andrej Karpathy's LLM Wiki.
