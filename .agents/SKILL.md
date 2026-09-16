---
name: india-ai-policy-wiki
description: Maintain a persistent, git-backed Obsidian wiki tracking AI policy, research, deployment, infrastructure, and government schemes in India organized under the Cognitive Memory Architecture. Use whenever the user drops in an article, paper, report, or seminar link; whenever a question should be answered from the accumulated wiki; whenever they want a briefing, comparison, or summary; or a wiki health check. Trigger even without the word "wiki" — "file this", "add this to my India AI policy notes", "what do we know about the IndiaAI Mission" all count.
---

# India AI Policy Wiki (Cognitive Memory Edition)

You maintain a living knowledge base — not a chatbot that re-derives answers from scratch each time. Every source you ingest should make the wiki smarter for every future question. The tedious part (cross-referencing, flagging contradictions, keeping summaries current, maintaining cognitive memory tiers) is your job so the user never has to do it.

## Cognitive Memory Layout

```text
AGENTS.md             standing instructions (repository constitution)
index.md              catalog of every wiki page across all 5 cognitive tiers
log.md                append-only record: ## [YYYY-MM-DD] ingest|query|lint|compare|memory | Title
raw/                  immutable source files (articles, PDFs, transcripts) — never edit these
wiki/
  episodic/           time-bound episodes (seminars, study groups, interviews, events)
    meetings/         AI Future Study Group sessions & series index (ai-meetings-overview.md)
    interviews/       expert interviews and recorded dialogues
    events/           summits, workshops, and roundtables
  semantic/           grounded world knowledge, entities, atomic sources, core concepts
    concepts/         cross-cutting themes: compute-capacity-and-energy.md, dpi-for-ai.md, ...
    entities/<c>/     government bodies, agencies, named schemes (e.g. entities/india/indiaai-mission.md)
    sources/          atomic claim sheets extracted from papers and government reports
    comparisons/      head-to-head pages, e.g. india-vs-china-compute-strategy.md
  reflective/         dialectic sensemaking, perspective spectrums & syntheses
    perspectives/     multi-stakeholder debate matrices (e.g. india-frontier-models-vs-applications.md)
    synthesis/        collaborative consensus whitepapers & evolving theses
  working/            active learning primers, Socratic guides & LLM bridges
    learning/         pedagogical primers, curricula, flash-briefs (primer-sovereign-compute-india.md)
    notebooklm/       Google NotebookLM bridge packs & audio blueprints (pack-india-sovereign-ai.md)
  procedural/         operational playbooks, templates, and agent guidelines
    playbooks/        research and episodic ingestion workflows
    templates/        reusable obsidian templates for each memory tier
```

Full frontmatter schema and page-writing conventions are in `.agents/references/taxonomy.md`.

## Operations

### 1. Ingest (Episodic or Semantic)
- Determine if the source is **Episodic** (meeting, seminar, interview transcript) or **Semantic** (paper, government decree, data report).
- File into `wiki/episodic/` or `wiki/semantic/sources/`.
- Cross-link across memory tiers (concepts, perspectives, entities).
- Update `index.md` and append to `log.md`.

### 2. Query
- Search `index.md` and traverse relevant cognitive tiers.
- Answer with explicit citations to specific wiki nodes (`[[filename|Title]]`).

### 3. Compare & Reflect
- Synthesize contested stances in `wiki/reflective/perspectives/`.

### 4. Learning & Working
- Generate primers, discussion questions, and NotebookLM bridge packs in `wiki/working/`.

### 5. Lint
- Check health, orphan nodes, and schema compliance (`memory_tier`) across all 5 tiers.
