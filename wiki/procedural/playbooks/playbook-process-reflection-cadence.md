---
memory_tier: procedural
type: playbook
domains: [methodology, process-improvement, governance]
tags: [playbook, feedback-loop, process-reflection, cadence, audit]
created: 2026-09-16
last_updated: 2026-09-16
---

# Playbook: Dual Feedback Loops & Process Reflection Cadence

> "Two kinds of feedback: the document loop and the process loop... The maintain stage closes a loop per document. That's necessary but not sufficient... Add a second, slower loop — a process reflection, on its own cadence (monthly or quarterly, not per-document)."  
> — *[ai-native-project-playbook.md](../../../ai-native-project-playbook.md)*

---

## 🔄 Dual Feedback Architecture

```
 ┌────────────────────────────────────────────────────────────────────────┐
 │ 1. Fast Document Loop (Per Deliverable)                                │
 │    intent.md -> spec.md -> draft.md -> review.md -> final.md           │
 │       ▲                                                 │              │
 │       └────────────────── feedback.md ◄─────────────────┘              │
 └────────────────────────────────────────────────────────────────────────┘

 ┌────────────────────────────────────────────────────────────────────────┐
 │ 2. Slower Process Loop (Monthly / Quarterly Cadence)                  │
 │    Audits the entire workflow across all projects:                     │
 │    • Stage ROI (did spec.md prevent rewrites or add delay?)            │
 │    • Human attention audit (are you still reading whole drafts?)       │
 │    • Skill drift check (are certified skills out of date?)             │
 │    • Loop shape calibration (is the 6-stage process right-sized?)      │
 │    Output: reflections/<year>-<quarter>-reflection.md                  │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 🔍 The 4 Core Process Audit Questions

During every cadence review (stored in `reflections/`), the study group answers four diagnostic questions:

### 1. Where did stages actually earn their keep?
- Did `spec.md` prevent a messy rewrite, or was it bureaucratic drag for a straightforward document?
- Did `review.md` catch verifiable errors and policy hallucinations, or did reviewers just rubber-stamp it?

### 2. Where is human attention actually going?
- If domain experts are still reading every draft word-by-word from start to finish, the layered-review shift has not materialized.
- Are humans spending their scarce hours on strategic framing, ethics, and political nuance—or on comma-splicing and basic sentence mechanics?

### 3. Are certified skills drifting from active standards?
- Has a government policy changed (e.g., IndiaAI Mission allocation rules or Bhashini API protocols) that makes an approved skill subtly incorrect?
- Do any candidate skills need to be graduated or retired?

### 4. Is the loop shape still right?
- Did a specific project need all 6 stages, or could intent and spec have been collapsed?
- Do we need a new project track based on emerging seminar themes?

---

## 🔗 Cross-References
- Retrospectives Vault: `reflections/`
- Reflection Template: `reflections/reflection-template.md`
- Master Playbook: [ai-native-project-playbook.md](../../../ai-native-project-playbook.md)
