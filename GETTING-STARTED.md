# Getting Started with the AI & Future of Humanity Second Brain

This guide helps researchers, domain experts, policy analysts, and contributors get up and running with the **Second Brain Wiki** quickly.

---

## 🛠️ 1. Recommended Setup: Obsidian Desktop

While the repository is standard Git markdown and works in any editor, it is optimized for **[Obsidian](https://obsidian.md/)**.

1. **Clone or Open Folder**:
   - In Obsidian, select **"Open folder as vault"** and point to `d:\sanjay\wiki-ai-future` (or your local clone path).
2. **Recommended Obsidian Plugins**:
   - **Dataview**: Enables dynamic querying of frontmatter tags, last updated dates, and source counts.
   - **Graph View**: Built-in visual map of interconnections between concepts, entities, and perspectives.
   - **Omnisearch / Quick Switcher++**: Fast fuzzy search across all atomic claims.
   - **Canvas**: Built-in tool for visual mind-mapping and whiteboarding arguments.

---

## 🧭 2. How to Use the Second Brain

### A. Exploring Knowledge via `index.md` and Graph View
- Always start at [index.md](file:///d:/sanjay/wiki-ai-future/index.md). It organizes all entities, concepts, perspectives, learning materials, and sources by domain.
- In Obsidian, press `Ctrl + G` (or `Cmd + G`) to open the **Interactive Graph View**. Notice how concepts cluster around domains like *Governance*, *Labor*, *Compute*, and *Ethics*.

### B. Ingesting New Seminars, Papers, Reports, or Links
Whenever you have a new seminar recording, whitepaper, podcast transcript, or government gazette:
1. Put the raw PDF/file in `raw/` (if applicable) or note the recording link.
2. Prompt your LLM agent:
   - For a seminar/meeting: *"Ingest this study group seminar recording into Episodic Memory, create a session note, and connect related concepts."*
   - For a paper/report: *"Ingest this document into Semantic Memory. Extract key atomic claims, create a source page in `wiki/semantic/sources/`, and update related concepts and perspectives."*
3. The agent will parse claims, build backlinks across cognitive tiers, and update [index.md](file:///d:/sanjay/wiki-ai-future/index.md) and [log.md](file:///d:/sanjay/wiki-ai-future/log.md).

### C. Exploring and Contributing Dialectic Perspectives (Reflective Memory)
AI's impact on humanity is multifaceted. To explore or build debates:
1. Browse `wiki/reflective/perspectives/` to see existing spectrums of thought.
2. Prompt your agent:
   > *"Collect and map out the debate on whether India should focus on training frontier foundation models vs fine-tuning open-source models for local applications. Include arguments from industry, academia, and government."*

### D. Interactive Socratic Tutor Sessions (Working Memory)
Need to understand a complex concept or prepare for a panel discussion?
- Prompt your agent:
   > *"Act as an AI Socratic Tutor. Walk me through the implications of algorithmic bias in Indian multilingual datasets. Test my assumptions and explain at a Policy Practitioner level."*

### E. Generating Learning Primers & Study Materials
To create a pedagogical module for a working group or workshop:
- Prompt your agent:
   > *"Generate a learning primer on 'Compute Sovereignty in India: Opportunities & Bottlenecks', with discussion prompts, case studies, and reading lists."*
- The generated guide will be saved under `wiki/working/learning/`.

### F. Linking and Syncing with Google NotebookLM
To use Google NotebookLM alongside this Second Brain:
1. Run the `notebooklm-sync-and-export` workflow to bundle markdown files and raw sources into a single export pack in `wiki/working/notebooklm/`.
2. Upload the pack to your [NotebookLM](https://notebooklm.google.com) notebook.
3. Generate NotebookLM **Audio Overviews (Deep Dive Podcasts)** or grounded Q&As.
4. Save the generated podcast transcript notes or query digests back to `wiki/working/notebooklm/`.

---

## 🔍 3. Daily Workflow Cheat Sheet (Cognitive Memory Model)

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Start Day: Check index.md across the 5 Cognitive Tiers   │
│ 2. Episodic: File seminar notes & recordings in episodic/   │
│ 3. Semantic: Ingest papers to sources/ -> concepts/         │
│ 4. Reflective: Map dialectic debates in perspectives/       │
│ 5. Working: Study primers in learning/ & NotebookLM packs   │
│ 6. End Day: Run Lint health check & verify log.md           │
└─────────────────────────────────────────────────────────────┘
```

