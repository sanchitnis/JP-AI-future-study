---
project: <project-slug>
stage: 4-test
artifact: review
reviewer_human: <Domain Expert>
reviewer_agent: Antigravity / Claude
date: YYYY-MM-DD
status: in-review | revisions-requested | certified
tags: [ai-native, review, stage-4]
---

# Review Ledger: <Project Title>

## 🤖 Layer 1: Agent Automated Review Check

| Checkpoint | Status | Notes / Findings |
| :--- | :---: | :--- |
| **Grounding & Sources** | Pass / Flagged | Do all empirical claims link to `wiki/semantic/sources/`? |
| **Spec Adherence** | Pass / Flagged | Does the draft include all sections defined in `spec.md`? |
| **Scope Drift Check** | Pass / Flagged | Did the agent avoid the explicit non-goals in `spec.md`? |
| **Contradiction Check**| Pass / Flagged | Any statements contradicting prior group positions? |

---

## 👤 Layer 2: Human Domain Expert Judgment

| Section / Paragraph | Flagged Issue / Question | Human Expert Decision | Action Taken |
| :--- | :--- | :--- | :--- |
| e.g. §3.2 Compute Pricing | "Is 10,000 GPUs sufficient for 2026 demands?" | Revised: qualify as Phase 1 allocation. | Adjusted draft. |
| | | | |

---

## ✍️ Sign-Off & Promotion Gate
- [ ] Agent checks passed with zero unverified empirical claims.
- [ ] Human domain expert certifies framing, ethical alignment, and strategic impact.
- **Decision**: Promoted to `final.md` on [Date] by [Name].
