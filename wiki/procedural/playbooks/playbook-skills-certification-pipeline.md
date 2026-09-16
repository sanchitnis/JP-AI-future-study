---
memory_tier: procedural
type: playbook
domains: [methodology, skills, quality-assurance]
tags: [playbook, skills, certification, expert-review, human-in-the-loop]
created: 2026-09-16
last_updated: 2026-09-16
---

# Playbook: Skills Certification Pipeline (Human-in-the-Loop Gate)

> "A skill that skips the expert-review step is just an unverified assumption with a file extension."  
> — *[ai-native-project-playbook.md](../../../ai-native-project-playbook.md)*

---

## 🎯 Why Skills Need a Human Gate

In software engineering, code has a compiler or runtime test suite: code either runs or breaks. In non-coding knowledge work (policy briefs, pedagogical rubrics, institutional voice, dialectic analyses), **there is no built-in runtime check**.

If an agent mistakenly encodes a subtly flawed rule (e.g. incorrect definition of DPI, outdated GPU subsidy guidelines, or skewed neutral tone), it will replicate that error across dozens of drafts without warning. Therefore, skill-building requires a formal **human expert gate**.

---

## 🔁 The 5-Step Skill Pipeline

```
 [1. Notice Repeated Correction]
               │
               ▼
 [2. Draft Narrow Candidate Skill]  (Rule + 1-2 Concrete Examples)
               │
               ▼
 [3. Domain Expert Review Gate]     (Certifies rule validity & nuance)
               │
      ┌────────┴────────┐
      ▼                 ▼
 [Needs Revision]   [Approved]
      │                 │
      └────────────────►│
                        ▼
 [4. Versioned Skill File]          (.agents/skills/<skill-name>/SKILL.md)
                        │
            ┌───────────┴───────────┐
            ▼                       ▼
   [Used in Build: Drafting]   [Used in Test: Review Rubric]
                        │
                        ▼
 [5. Re-review on Standard Change]  (Prevent silent drift)
```

---

## 📋 The 4 Golden Rules for Knowledge Work Skills

1. **Notice the Pattern (Rule of Two)**: If you correct the agent on the same stylistic, structural, or domain distinction twice, it is a skill candidate—never leave it as an ephemeral chat reminder.
2. **Draft Narrowly**: A rule plus one or two positive/negative examples. Avoid vague essays on "writing well".
3. **Route to the Domain Expert**: Route the draft to the study group expert who owns that topic (e.g., Saurabh Bodas for compute/physical AI, Rohan Katepallewar for voice/foundational literacy, Dr. Abhishek Dedhe for neuroscience, Mihir Shete for geopolitics/China).
4. **Version and Audit**: Tag every skill with `certified_by`, `certified_date`, and `review_cycle`. Audit against standard updates during quarterly process reflections.

---

## 🔗 Cross-References
- Playbook: [[playbook-ai-native-project-lifecycle|AI-Native Project Lifecycle]]
- Agent Skill: `.agents/skills/skill-certification-pipeline/SKILL.md`
- Master Playbook: [ai-native-project-playbook.md](../../../ai-native-project-playbook.md)
