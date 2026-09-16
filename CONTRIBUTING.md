# Contributing to the JP AI Future Study Group Hub

Thank you for contributing to the **JP AI Future Study Group Project Hub**. This repository unites our **Active Project Delivery Tracks** with our persistent **Collective Memory Wiki**.

To maintain analytical rigor, traceability, and high operational velocity across both streams, all human contributors and AI agents adhere to the following standards.

---

## 🏛️ Contribution Tracks

Contributors can participate across two interconnected engines:

### Track 1: Active Knowledge Work Projects (`projects/`)
When authoring a policy brief, curriculum, whitepaper, or concept note:
1. Follow the 6-stage lifecycle (`intent.md` → `spec.md` → `draft.md` → `review.md` → `final.md` → `feedback.md`).
2. Adhere to the **Committed Artifacts Standard**: all decisions, constraints, and scope boundaries must be committed to repository markdown files, not left in oral or chat memory.
3. Lock `spec.md` before drafting begins.
4. Ensure Layer 1 automated checks and Layer 2 human domain expert sign-offs are documented in `review.md` before promoting to `final.md`.

### Track 2: Collective Memory Wiki (`wiki/`)
When adding or refining knowledge nodes:
1. **Grounded Factual Claims**: Every empirical assertion or metric must link to an atomic claim in `wiki/semantic/sources/`.
2. **Cognitive Tier Frontmatter**: Every note must declare `memory_tier: episodic | semantic | reflective | working | procedural`.
3. **Dialectic Balance**: Present opposing viewpoints fairly in `wiki/reflective/perspectives/`.
4. **Preserve Raw Immutability**: Never modify or overwrite files in `raw/`.

---

## 🔁 The Governed Skills Pipeline
If you find yourself repeatedly correcting the agent on a specific convention, style rule, or domain concept:
1. Apply the **Rule of Two**: Draft a candidate skill containing the core rule, one positive example, and one negative example.
2. Route the candidate skill to the corresponding study group domain lead for formal certification before committing.
3. Unverified skills must not be merged.

---

## 🔄 Collaboration & PR Workflow

1. **Branching**: Branch from `main` using standard prefixes:
   - `project/<slug>` (e.g. `project/policy-brief-gpu-allocation`)
   - `wiki/<tier>/<slug>` (e.g. `wiki/semantic/source-bhashini-update`)
   - `skill/<slug>` (e.g. `skill/indian-patent-rubric`)
2. **Update Index & Log**:
   - Update `index.md` to reflect new deliverables or wiki nodes.
   - Append an entry to `log.md` detailing the change and domain leads involved.
3. **Peer Review**: Submit a Pull Request for review by the appropriate domain lead (e.g. Saurabh Bodas, Rohan Katepallewar, Abhishek Suryawanshi, Swanand Joshi, Dr. Abhishek Dedhe, Mihir Shete).
