# Page Schema & Cognitive Memory Taxonomy Guidelines

Every page in this Second Brain Wiki follows Obsidian-compatible markdown with standard YAML frontmatter and `[[wiki-link]]` syntax. The entire knowledge base is structured using the **Cognitive Memory Architecture**.

---

## 1. Cognitive Memory Tiers Overview

| Memory Tier | Purpose | Subdirectories | Primary Note Types |
| :--- | :--- | :--- | :--- |
| **Episodic** | Time-bound experiences, events, seminar sessions, interviews | `wiki/episodic/meetings/`<br>`wiki/episodic/interviews/`<br>`wiki/episodic/events/` | `meeting`, `meeting-index`, `interview`, `event` |
| **Semantic** | Grounded world knowledge, entities, atomic sources, core concepts | `wiki/semantic/concepts/`<br>`wiki/semantic/entities/`<br>`wiki/semantic/sources/`<br>`wiki/semantic/comparisons/` | `concept`, `entity`, `source`, `comparison` |
| **Reflective** | Dialectic sensemaking, multi-stakeholder debate matrices, syntheses | `wiki/reflective/perspectives/`<br>`wiki/reflective/synthesis/` | `perspective`, `synthesis` |
| **Working** | Active retrieval sets, learning primers, Socratic Q&A, NotebookLM packs | `wiki/working/learning/`<br>`wiki/working/notebooklm/` | `learning`, `notebooklm` |
| **Procedural** | Operational SOPs, research workflows, agent skills, templates | `wiki/procedural/playbooks/`<br>`wiki/procedural/templates/` | `playbook`, `template` |

---

## 2. Frontmatter Schema Specification

```yaml
---
memory_tier: episodic | semantic | reflective | working | procedural
type: meeting | interview | event | concept | entity | source | comparison | perspective | synthesis | learning | notebooklm | playbook
domains: [governance, economy-work, ethics-society, compute-infra, talent-education, geopolitics, healthcare, agriculture]
countries: [india, us, china, eu, global-south]
tags: [sovereign-ai, automation, alignment, public-goods]
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
source_count: 1
expert_contributors: ["@expert_handle"]
---
```

---

## 3. Tier-Specific Note Structures

### A. Episodic Memory Pages (`wiki/episodic/...`)
Used for recording dated study group sessions, seminar discussions, interviews, and conferences.
- Template: `[[wiki/procedural/templates/template-episodic-event|template-episodic-event.md]]`
- Session series overview: `[[wiki/episodic/meetings/ai-meetings-overview|ai-meetings-overview.md]]`
- Required Fields: `date`, `speakers` or `participants`, `recording_url` (if available).

### B. Semantic Memory Pages (`wiki/semantic/...`)
- **Sources (`wiki/semantic/sources/<slug>.md`)**: Atomic extracted claims from papers, policy drafts, and reports.
- **Concepts (`wiki/semantic/concepts/<slug>.md`)**: Cross-cutting pillars (sovereign compute, labor automation, DPI for AI).
- **Entities (`wiki/semantic/entities/<country>/<slug>.md`)**: Key institutes, initiatives, and ministries.
- **Comparisons (`wiki/semantic/comparisons/<slug>.md`)**: Cross-national structured analyses.

### C. Reflective Memory Pages (`wiki/reflective/...`)
- **Perspectives (`wiki/reflective/perspectives/<slug>.md`)**: Multi-stakeholder dialectics, contested arguments, and expert spectrum tables.
- **Synthesis (`wiki/reflective/synthesis/<slug>.md`)**: Collaborative whitepapers and consensus horizons.

### D. Working Memory Pages (`wiki/working/...`)
- **Learning & Primers (`wiki/working/learning/<slug>.md`)**: Socratic guides, curricula, and executive flash-briefs.
- **NotebookLM Bridge (`wiki/working/notebooklm/<slug>.md`)**: Grounding bundles, audio overview blueprints, and prompt templates.

### E. Procedural Memory Pages (`wiki/procedural/...`)
- **Playbooks (`wiki/procedural/playbooks/<slug>.md`)**: Step-by-step guides for domain research and episodic ingestions.
- **Templates (`wiki/procedural/templates/<slug>.md`)**: Reusable markdown blueprints for each cognitive tier.
