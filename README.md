# AI & Future of Humanity (India Focus) — Second Brain Wiki

Welcome to the **Second Brain Wiki on AI & The Future of Humanity (India Focus)**.

This repository is an LLM-augmented, Obsidian-native knowledge graph and collaborative think-tank workspace. Built upon the principles of **Andrej Karpathy's LLM Wiki** paradigm, it acts as a collective cognitive infrastructure for an interdisciplinary group of domain experts (technologists, economists, philosophers, legal scholars, sociologists, and policymakers) investigating how the emergence of Artificial Intelligence will shape humanity's future, with an explicit emphasis on India.

---

## 🌟 Core Pillars of this Second Brain

```
                              ┌──────────────────────────────────┐
                              │     HUMAN & AGENT REASONING      │
                              └─────────────────┬────────────────┘
                                                │
         ┌──────────────────┬───────────────────┼───────────────────┬──────────────────┐
         ▼                  ▼                   ▼                   ▼                  ▼
┌─────────────────┐┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│ EPISODIC MEMORY ││ SEMANTIC MEMORY │ │REFLECTIVE MEMORY│ │ WORKING MEMORY  │ │PROCEDURAL MEMORY│
│ (wiki/episodic) ││ (wiki/semantic) │ │(wiki/reflective)│ │ (wiki/working)  │ │(wiki/procedural)│
├─────────────────┤├─────────────────┤ ├─────────────────┤ ├─────────────────┤ ├─────────────────┤
│ • Study Groups  ││ • Concepts      │ │ • Perspectives  │ │ • Primers       │ │ • Playbooks     │
│ • Seminars      ││ • Entities      │ │ • Dialectic Maps│ │ • Curricula     │ │ • Templates     │
│ • Interviews    ││ • Grounded      │ │ • Syntheses     │ │ • Socratic QA   │ │ • Agent Skills  │
│ • Conferences   ││   Sources       │ │ • Consensus     │ │ • NotebookLM    │ │ • Ingestion     │
│ • Timelines     ││ • Comparisons   │ │   Theses        │ │   Packs         │ │   Protocols     │
└─────────────────┘└─────────────────┘ └─────────────────┘ └─────────────────┘ └─────────────────┘
```

1. **Episodic Memory**: Captures dated study group seminars, expert interviews, meeting recordings (such as the 13-session AI Future Study Group), and real-time event logs.
2. **Semantic Memory**: Houses enduring world knowledge, institutions, cross-national comparisons, and atomic factual claims extracted from papers and official policy gazettes.
3. **Reflective Memory**: Catalogs multi-stakeholder dialectic matrices, opposing philosophical/economic stances, and collaborative consensus papers.
4. **Working Memory**: Active retrieval sets, pedagogical primers, Socratic discussion modules, and Google NotebookLM bridge packs.
5. **Procedural Memory**: Standard operating procedures, ingestion playbooks, agent skills, and Obsidian templates for each memory tier.

---

## 📂 Repository Architecture

```text
├── .agents/
│   ├── skills/
│   │   ├── ingest-and-source/                 # Raw ingestion & cognitive tier filing
│   │   ├── collect-and-maintain-perspectives/ # Dialectic matrix & stance tracking
│   │   ├── ai-tutor-and-socratic-dialogue/    # Multi-level tutor & conversational mentor
│   │   ├── generate-learning-materials/       # Primer, curriculum & study guide generator
│   │   ├── notebooklm-sync-and-export/        # Source packs & NotebookLM bridge
│   │   └── lint-and-integrity/                # Wiki health, broken link & freshness checks
│   └── references/
│       └── taxonomy.md                        # Frontmatter schema & cognitive taxonomy
├── raw/                                       # Immutable source store (PDFs, papers, transcripts)
├── wiki/
│   ├── episodic/                              # Time-bound experiences, seminars & meeting logs
│   │   ├── meetings/                          # Study group sessions & series index (ai-meetings-overview)
│   │   ├── interviews/                        # Recorded expert interviews
│   │   └── events/                            # Conferences & roundtables
│   ├── semantic/                              # Grounded world knowledge & facts
│   │   ├── concepts/                          # Cross-cutting themes (compute, labor, DPI)
│   │   ├── entities/                          # Institutions, ministries, schemes (India & Global)
│   │   ├── sources/                           # Atomic summaries & extracted checkable claims
│   │   └── comparisons/                       # Cross-national head-to-head analyses
│   ├── reflective/                            # Dialectic sensemaking & synthesis
│   │   ├── perspectives/                      # Debate spectrums & multi-stakeholder matrices
│   │   └── synthesis/                         # Collaborative theses & consensus whitepapers
│   ├── working/                               # Active engagement & LLM tools
│   │   ├── learning/                          # Socratic modules, course roadmaps & primers
│   │   └── notebooklm/                        # Source packs, podcast notes & NotebookLM mappings
│   └── procedural/                            # Operational workflows & templates
│       ├── playbooks/                         # Human & agent research execution playbooks
│       └── templates/                         # Obsidian markdown blueprints for each tier
├── index.md                                   # Master knowledge catalog & topic index
├── log.md                                     # Append-only chronological activity log
├── AGENTS.md                                  # Repository constitution and agent rules
├── GETTING-STARTED.md                         # Quick-start onboarding guide for users & researchers
└── CONTRIBUTING.md                            # Open collaboration & peer-review guidelines
```

---

## 🚀 Quick Navigation & Use Cases

- **For New Users & Experts**: Read [GETTING-STARTED.md](file:///d:/sanjay/wiki-ai-future/GETTING-STARTED.md) to set up Obsidian, configure prompts, and explore the knowledge graph.
- **For Contributing Research**: Read [CONTRIBUTING.md](file:///d:/sanjay/wiki-ai-future/CONTRIBUTING.md) for citation standards, PR flows, and perspective submission templates.
- **To Explore the Knowledge Catalog**: Open [index.md](file:///d:/sanjay/wiki-ai-future/index.md).
- **To Review Session History**: Check [log.md](file:///d:/sanjay/wiki-ai-future/log.md).

---

## 🤖 Agent Capabilities at a Glance

You can invoke the LLM agent to perform the following operations:

| Task / Intent | Natural Prompt Example |
| :--- | :--- |
| **Ingest Source** | `"Ingest this paper on India's sovereign AI mission and link relevant concepts"` |
| **Map Perspectives** | `"Create a perspective map on the impact of generative AI on India's BPO/IT workforce"` |
| **Socratic Tutoring** | `"Act as a tutor and explain Digital Public Infrastructure (DPI) for AI at a policy practitioner level"` |
| **Generate Learning Primer** | `"Generate a study guide and discussion questions on Compute Governance in the Global South"` |
| **NotebookLM Export** | `"Prepare a NotebookLM source pack on Indic LLMs and generate a podcast audio overview outline"` |
| **Compare Nations** | `"Compare India's AI compute strategy with China's East-Data-West-Compute project"` |
| **Wiki Health Check** | `"Lint the wiki for orphan pages, missing sources, or outdated data"` |

---

## 📄 License & Attribution
Maintained collaboratively by the **India AI & Future of Humanity Expert Group**.
Built with [Obsidian](https://obsidian.md) and inspired by [Andrej Karpathy's LLM Wiki](https://github.com/karpathy).
