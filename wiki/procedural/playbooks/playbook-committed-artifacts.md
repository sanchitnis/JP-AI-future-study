---
memory_tier: procedural
type: playbook
domains: [methodology, artifacts, knowledge-management]
tags: [playbook, committed-artifacts, versioning, context]
created: 2026-09-16
last_updated: 2026-09-16
---

# Playbook: Committed Artifacts Standard

> "The one habit that makes this work: every stage ends by writing something down, and the next stage starts by reading it. Not a meeting summary — an actual file, kept somewhere durable, that both you and the agent can open cold."  
> — *[ai-native-project-playbook.md](../../../ai-native-project-playbook.md)*

---

## 🎯 The Cold-Open Principle

In traditional knowledge work, project context lives inside human heads, scattered across emails, chat messages, and fleeting calls. In an AI-native study group:
1. **Zero Oral Context**: If a constraint, decision, or source is not written in a versioned repository file, it effectively does not exist for the agent or future collaborators.
2. **Cold-Open Guarantee**: Any contributor (or LLM instance) should be able to open a project directory, read `context.md` and the stage artifacts in sequence, and immediately understand current status, trade-offs, and next actions.

---

## 📂 Standard Project Artifact Chain

Every project inside `projects/<project-slug>/` contains these durable artifacts:

| File | Stage Produced | Purpose & Contract |
| :--- | :--- | :--- |
| `context.md` | Pre-stage / Standing | Project-specific facts, institutional background, standing constraints, and key decisions. |
| `intent.md` | Stage 1: Plan | Raw problem statement, stakeholders, definition of done, constraints. |
| `spec.md` | Stage 2: Design | Locked architecture, section outlines, audience tone, and evidence sources. |
| `draft.md` | Stage 3: Build | Agent-generated full content, iteratively tuned with human direction. |
| `review.md` | Stage 4: Test | Layered verification ledger: fact checks, style compliance, flagged items, and human resolutions. |
| `final.md` | Stage 5: Deploy | Approved, certified final deliverable ready for publication or submission. |
| `feedback.md` | Stage 6: Maintain | Post-publication outcomes, stakeholder responses, and follow-up prompts seeding the next cycle. |

---

## 🛡️ Best Practices for Committed Files

1. **Explicit Frontmatter**: Every artifact should declare its stage, project parent, author, and status in YAML frontmatter.
2. **Atomic References**: Link factual assertions to grounding sources in `wiki/semantic/sources/` using `[[source-slug|Title]]`.
3. **No Phantom Edits**: When moving between stages, do not overwrite previous stage files without saving history; preserve `intent.md`, `spec.md`, and `draft.md` as permanent historical checkpoints.
4. **Clean Commits**: Commit each artifact transition using semantic git conventions (e.g. `project(sovereign-ai): draft spec.md`).

---

## 🔗 Cross-References
- Lifecycle Playbook: [[playbook-ai-native-project-lifecycle|AI-Native Project Lifecycle]]
- Project Templates: `wiki/procedural/templates/template-intent.md`
