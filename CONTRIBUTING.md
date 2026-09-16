# Contributing to the AI & Future of Humanity Second Brain

Thank you for contributing to the **AI & Future of Humanity (India Focus) Second Brain Wiki**. This repository serves as a shared, multidisciplinary think-tank knowledge base.

To maintain high analytical rigor, traceability, and neutrality across controversial debates, all contributors and LLM agents adhere to the following standards.

---

## 🏛️ Contribution Principles

1. **No Unsupported Factual Claims**:
   - Every empirical data point, policy quote, or timeline event must cite an atomic source in `wiki/semantic/sources/` or an episode in `wiki/episodic/`.
2. **Cognitive Tier Categorization**:
   - Every note must be filed into its appropriate cognitive memory tier (`wiki/episodic/`, `wiki/semantic/`, `wiki/reflective/`, `wiki/working/`, or `wiki/procedural/`) and declare `memory_tier` in its frontmatter.
3. **Neutrality in Debate Representation**:
   - When discussing contested topics (e.g. AI safety vs. acceleration, IP rights in training data, labor automation), present the strongest arguments for all credible perspectives without editorial bias in `wiki/reflective/perspectives/`.
4. **Obsidian-Native Formatting**:
   - Use `[[wiki-link]]` format (basename preferred) for cross-referencing files.
   - Include valid YAML frontmatter compliant with [taxonomy.md](file:///d:/sanjay/wiki-ai-future/.agents/references/taxonomy.md).
5. **Preserve Raw Immutability**:
   - Never modify or overwrite files in `raw/`.
6. **Update Index & Log**:
   - Every PR that adds or alters knowledge pages must update [index.md](file:///d:/sanjay/wiki-ai-future/index.md) and append to [log.md](file:///d:/sanjay/wiki-ai-future/log.md).

---

## 🔄 Pull Request & Collaboration Flow

We follow an **Open Collaboration with Peer Review** model:

```
1. Fork or create feature branch (e.g., `episodic/study-group-session-2` or `source/indiaai-cabinet-note`)
2. File into raw/ and appropriate cognitive tier (wiki/episodic, wiki/semantic, wiki/reflective)
3. Cross-link nodes across memory tiers
4. Update index.md and append one entry to log.md
5. Run lint health check
6. Submit Pull Request with the Contribution Template below
7. Domain Expert Peer Review -> Merge
```

---

## 📋 Pull Request Submission Template

When opening a Pull Request, use this checklist in the PR description:

```markdown
### Summary of Changes
- [ ] Added new episodic session/event or semantic source: [[node-slug]]
- [ ] Created / Updated Concept or Perspective: [[concept-or-perspective-slug]]
- [ ] Updated `index.md` and appended to `log.md`

### Cognitive Memory Tier
- [ ] Episodic Memory (`wiki/episodic/`)
- [ ] Semantic Memory (`wiki/semantic/`)
- [ ] Reflective Memory (`wiki/reflective/`)
- [ ] Working Memory (`wiki/working/`)
- [ ] Procedural Memory (`wiki/procedural/`)

### Domain Coverage
- [ ] Governance & Policy
- [ ] Economy, Labor & Future of Work
- [ ] Ethics, Philosophy & Culture
- [ ] Infrastructure, Compute & Sovereign AI
- [ ] Education, Talent & Human Capital
- [ ] Geopolitics & Global Comparison
- [ ] Sectoral (Healthcare / Agriculture / Public Services)

### Quality & Integrity Checklist
- [ ] All factual claims cite a source in `wiki/semantic/sources/` or episode in `wiki/episodic/`
- [ ] Frontmatter matches `references/taxonomy.md` schema (including `memory_tier`)
- [ ] No broken `[[wiki-links]]`
- [ ] Opposing perspectives acknowledged where applicable
```

---

## ✍️ Frontmatter Guidelines for Contributors

Every markdown file added to `wiki/` must start with structured frontmatter:

```yaml
---
memory_tier: episodic | semantic | reflective | working | procedural
type: meeting | interview | event | concept | entity | source | comparison | perspective | synthesis | learning | notebooklm | playbook
domains: [economy-work, governance]
countries: [india, us]
tags: [automation, bpo, talent]
created: 2026-09-16
last_updated: 2026-09-16
source_count: 4
expert_contributors: ["@your_handle"]
---
```
---

## 🧪 Peer Review & Dispute Resolution

- If a contributor disagrees with the framing of a perspective or thesis:
  - **Do not delete the existing perspective.**
  - Add the counter-perspective, cite supporting sources, and document the unresolved tension under `## Synthesis & Consensus Horizons` on that perspective page.
  - Open a discussion issue for domain expert working group review.

