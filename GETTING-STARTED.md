# Getting Started with the JP AI Future Study Group Hub

Welcome to the **JP AI Future Study Group Project Hub**. This guide helps members, domain experts, policy fellows, and research collaborators get up to speed quickly with both our **Active Project Engine** and our **Collective Memory Wiki**.

---

## 🛠️ 1. Recommended Setup: Obsidian Desktop

While all files are standard version-controlled Markdown and can be edited in VS Code or any text editor, the hub is optimized for **[Obsidian](https://obsidian.md/)**.

1. **Open as Vault**:
   - In Obsidian, select **"Open folder as vault"** and point to your local repository directory (`d:\sanjay\JP-AI-future-study`).
2. **Recommended Plugins**:
   - **Dataview**: Enables dynamic querying across project stages and frontmatter tags.
   - **Graph View**: Interactive visual map connecting seminar episodes, concepts, entities, and perspectives.
   - **Omnisearch / Quick Switcher++**: Fast fuzzy search across all atomic claims and project files.

---

## 🚀 2. How to Run an AI-Native Project (The 6 Stages)

If you are drafting a policy memo, curriculum framework, or concept note:

### Stage 1: Plan → Create `intent.md`
- Copy `projects/_template-project/` to `projects/<your-project-slug>/`.
- Define the problem, target audience, constraints, and explicit definition of "done".
- Anchor your intent to existing wiki concepts (`[[compute-capacity-and-energy]]`) and sources.

### Stage 2: Design → Lock `spec.md`
- Work with your agent to compress section headings, tone, and evidence requirements into `spec.md`.
- Agree on explicit non-goals to prevent the agent from generating off-target text.

### Stage 3: Build → Agent Drafts in `draft.md`
- Direct the agent to produce the draft adhering strictly to `context.md` and `spec.md`.
- You supply judgment, direction, and sources; the agent supplies structure and drafting velocity.

### Stage 4: Test → Layered Review in `review.md`
- Run Layer 1: Agent checks citations against `wiki/semantic/sources/` and verifies outline completeness.
- Run Layer 2: Human domain expert evaluates strategic nuance, political sensitivity, and ethics.

### Stage 5: Deploy → Promote to `final.md`
- Once review sign-offs are complete, commit the deliverable to `final.md` for circulation.

### Stage 6: Maintain → Capture Feedback in `feedback.md`
- Log real-world reception, challenges, and new policy questions.
- Formulate the follow-up intent prompt that restarts the loop for the next cycle.

---

## 🧠 3. How to Use the Collective Memory Wiki

- **Seminar Recordings**: Find notes and Google Drive links for all 13 study group meetings in [[ai-meetings-overview]].
- **Grounded Concepts & Facts**: Search `wiki/semantic/concepts/` and `wiki/semantic/sources/` before doing research from scratch.
- **Dialectic Perspectives**: Review opposing arguments in `wiki/reflective/perspectives/` (e.g. [[india-frontier-models-vs-applications]]).
- **Socratic Tutoring**: Prompt your agent:
  > *"Act as an AI Socratic Tutor. Walk me through the implications of algorithmic bias in Indian multilingual datasets at a policy practitioner level."*

---

## 🔁 4. The Governed Skills Pipeline & Reflections

- **Rule of Two**: If you correct an agent on the same convention twice, run the `skill-certification-pipeline` to draft a candidate rule. Route it to your domain lead before merging.
- **Quarterly Retrospective**: Every 3 months, the group reviews `reflections/` to assess stage ROI, check skill freshness, and calibrate our AI-native workflows.
