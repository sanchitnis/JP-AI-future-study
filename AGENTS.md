# AGENTS.md — AI & The Future of Humanity (India Focus) Second Brain

This repository is a persistent, LLM-augmented **Second Brain Wiki** built on the principles of Andrej Karpathy's LLM wiki paradigm and organized under a **Cognitive Memory Architecture**. It is designed for an interdisciplinary group of domain experts studying the emerging future of humanity in the context of Artificial Intelligence, with a primary focus on India and global comparative dynamics.

**Read `index.md` before doing anything else in a session.** It is the living catalog and knowledge graph of the entire wiki — never re-derive from raw sources what existing wiki pages synthesize.

---

## The Cognitive Memory Framework

All knowledge in this second brain is filed and retrieved across five cognitive memory tiers:

```
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ EPISODIC MEMORY │ │ SEMANTIC MEMORY │ │REFLECTIVE MEMORY│ │ WORKING MEMORY  │ │PROCEDURAL MEMORY│
│ wiki/episodic/  │ │ wiki/semantic/  │ │wiki/reflective/ │ │ wiki/working/   │ │wiki/procedural/ │
├─────────────────┤ ├─────────────────┤ ├─────────────────┤ ├─────────────────┤ ├─────────────────┤
│ • Study Groups  │ │ • Concepts      │ │ • Perspectives  │ │ • Primers       │ │ • Playbooks     │
│ • Seminars      │ │ • Entities      │ │ • Dialectic Maps│ │ • Curricula     │ │ • Templates     │
│ • Interviews    │ │ • Grounded      │ │ • Syntheses     │ │ • Socratic QA   │ │ • Agent Skills  │
│ • Conferences   │ │   Sources       │ │ • Consensus     │ │ • NotebookLM    │ │ • Ingestion     │
│ • Timelines     │ │ • Comparisons   │ │   Horizons      │ │   Bridge Packs  │ │   Workflows     │
└─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘
```

Every markdown entry must declare its cognitive tier in the frontmatter:
```yaml
---
memory_tier: episodic | semantic | reflective | working | procedural
type: meeting | interview | event | concept | entity | source | comparison | perspective | synthesis | learning | notebooklm | playbook
---
```

---

## Standing Principles & Operational Rules

1. **Immutable Raw Ingestion (`raw/`)**:
   - `raw/` contains raw source artifacts (papers, PDFs, reports, interview transcripts, recorded notes).
   - Never edit files inside `raw/`. If a source needs clarification or correction, document it on the corresponding `wiki/semantic/sources/<slug>.md` page.

2. **Episodic Capture (`wiki/episodic/`)**:
   - Capture dated meetings, study group seminars, expert interviews, and conference notes in `wiki/episodic/`.
   - Maintain the overarching series index at `wiki/episodic/meetings/ai-meetings-overview.md`.
   - Every episodic entry must cross-link to relevant semantic concepts, reflective perspectives, and entities.

3. **Atomic Traceability & Grounded Claims (`wiki/semantic/`)**:
   - Every factual assertion, quote, metric, or perspective on a wiki page must link back to an atomic source in `wiki/semantic/sources/`.
   - If an idea is speculative, an open question, or a dialectic thesis, mark it explicitly in the appropriate frontmatter and section headers.

4. **Multi-Perspective Synthesis & Dialectic Mapping (`wiki/reflective/`)**:
   - This wiki is not a monoculture of opinion. On contested issues (e.g. AI automation vs. job creation in India, sovereign compute vs. open cloud, AI safety vs. open source acceleration), capture diverse, well-reasoned viewpoints from domain experts in `wiki/reflective/perspectives/`.
   - Acknowledge counter-arguments, caveats, and domain-specific nuances.

5. **Obsidian-Native Knowledge Graph (`[[wiki-link]]`)**:
   - Use `[[wiki-link]]` syntax (preferably basename format `[[filename|Title]]`) for all cross-references across entities, concepts, comparisons, perspectives, learning materials, and NotebookLM packs.
   - Maintain frontmatter tags and schema metadata (`memory_tier`, `type`, `tags`, `domains`, `created`, `last_updated`, `source_count`) to ensure Obsidian Dataview and Graph View operate seamlessly.

6. **Interactive Tutor & Working Memory (`wiki/working/`)**:
   - Provide Socratic explanations, multi-level educational primers (beginner to advanced researcher), and modular study guides in `wiki/working/learning/`.
   - Maintain grounding links for external LLM tools, including NotebookLM source sets and audio overview scripts in `wiki/working/notebooklm/`.

7. **Living Index & Audit Trail**:
   - Always update `index.md` whenever adding or refactoring pages.
   - Append every ingestion, synthesis, perspective capture, comparison, brief, or lint operation to `log.md`.

---

## Log Format

Each `log.md` entry:
```markdown
## [YYYY-MM-DD] ingest|perspective|tutor|learning|compare|brief|notebooklm|lint|memory | <Short Title>
- Summary of action taken, memory tier affected, pages modified/created, and relevant sources.
```

---

## Git Operations

- Commit after atomic operations or batch ingestion runs using conventional commits (e.g. `memory: ...`, `ingest: ...`, `perspective: ...`, `learning: ...`, `refactor: ...`).
- In open collaboration workflows, adhere to PR reviews and peer-review checklists detailed in `CONTRIBUTING.md`.
