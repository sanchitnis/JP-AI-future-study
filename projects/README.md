# Study Group Project Tracks (`projects/`)

Welcome to the **Project Delivery Tracks** of the JP AI Future Study Group. While the **Wiki** (`wiki/`) serves as our persistent, collective memory, the `projects/` directory houses our **active deliverables, policy briefs, curricula, whitepapers, and concept notes**.

Every project in this directory is executed using the 6-stage **AI-Native Project Lifecycle** from [ai-native-project-playbook.md](../ai-native-project-playbook.md).

---

## 🚦 Active Project Registry

| Project Slug | Domain / Theme | Primary Deliverable | Current Stage | Lead / Experts |
| :--- | :--- | :--- | :---: | :--- |
| [`policy-brief-sovereign-ai-compute`](./policy-brief-sovereign-ai-compute/) | Compute, Governance | Policy Brief on IndiaAI GPU Cloud & National Compute Access | **Stage 5 (Deployed / Final)** | Saurabh Bodas, Parag |
| [`curriculum-foundational-ai-literacy`](./curriculum-foundational-ai-literacy/) | Talent, Education, DPI | 4-Week Teacher Workshop & Voice-AI Numeracy Framework | **Stage 5 (Deployed / Final)** | Rohan Katepallewar |
| [`teacher-training-high-school-ai-pedagogy`](./teacher-training-high-school-ai-pedagogy/) | Talent, Education, Cognition | High School Teacher AI Literacy & Socratic Pedagogy Framework | **Stage 5 (Deployed / Final)** | Rohan Katepallewar, Deepak Gupte, Gaurav Marathe |
| [`concept-note-ai-workforce-resilience`](./concept-note-ai-workforce-resilience/) | Economy, Labor, IT | Strategic Memo on IT/BPO Centaur Reskilling | **Stage 5 (Deployed / Final)** | Abhishek Suryawanshi, Swanand Joshi |
| [`research-ai-in-india`](./research-ai-in-india/) | Governance, Compute, Economics, Geopolitics, Defense, Education, Inclusion | Comprehensive Research Study: AI in India (2024–2026) | **Stage 5 (Deployed / Final)** | Saurabh Bodas, Mihir Shete, Abhishek Suryawanshi, Rohan Katepallewar |

---

## 🔄 The 6 Committed Artifacts in Every Project

Each project directory forms a self-contained, cold-readable artifact chain:

```text
projects/<project-slug>/
├── context.md     # Standing project context, constraints, and decisions
├── intent.md      # Stage 1: Problem statement, audience, done criteria
├── spec.md        # Stage 2: Locked structure, requirements, non-goals
├── draft.md       # Stage 3: Agent-drafted content with human guidance
├── review.md      # Stage 4: Layered review check (agent checks + human sign-off)
├── final.md       # Stage 5: Published, committed deliverable
└── feedback.md    # Stage 6: Post-launch impact & next cycle intent trigger
```

---

## 🚀 How to Launch a New Project

1. Copy [`_template-project/`](./_template-project/) to `projects/<new-project-slug>/`.
2. Fill out `intent.md` and initial `context.md`.
3. Work with the agent using the `ai-native-project-engine` skill to lock `spec.md`, generate `draft.md`, perform layered review in `review.md`, and deploy to `final.md`.
4. Log the project in this `README.md` and update `index.md` and `log.md`.
