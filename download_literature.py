"""
Literature Downloader for JP AI Future Study Group Projects
=============================================================
Downloads source documents (PDFs, HTML reports, official releases)
for each project's literature survey into:
  - projects/<project_slug>/literature/

Also maintains traceability manifests and links to raw/literature/ summaries.

Usage:
    python download_literature.py
"""

import os
import sys
import json
import time
import subprocess
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Base directory
BASE_DIR = Path(r"d:\sanjay\JP-AI-future-study")
PROJECTS_DIR = BASE_DIR / "projects"
RAW_LIT_DIR = BASE_DIR / "raw" / "literature"

# Common browser headers for curl
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

# ──────────────────────────────────────────────────────────────────────────────
# Project 1: Teacher Training High School AI Pedagogy
# ──────────────────────────────────────────────────────────────────────────────
TEACHER_TRAINING_SOURCES = [
    {
        "slug": "unesco-ai-competency-framework-teachers-2024",
        "title": "UNESCO AI Competency Framework for Teachers (2024)",
        "url": "https://www.unesco.org/en/articles/ai-competency-framework-teachers",
        "filename": "unesco-ai-competency-framework-teachers-2024.html",
        "type": "html",
        "rubric_score": "4.8 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "unesco-ai-competency-framework-teachers-2024.md",
    },
    {
        "slug": "mollick-assigning-ai-socratic-tutor-prompts",
        "title": "Assigning AI: Socratic Tutoring & Seven Approaches (Mollick & Mollick, 2023)",
        "url": "https://ai.wharton.upenn.edu/",
        "filename": "mollick-assigning-ai-wharton-overview.html",
        "type": "html",
        "rubric_score": "4.9 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "mollick-assigning-ai-socratic-tutor-prompts.md",
    },
    {
        "slug": "singapore-moe-ai-in-education-framework-sls",
        "title": "Singapore MOE AI in Education Framework & SLS Platform",
        "url": "https://www.moe.gov.sg/education-in-sg/educational-technology-journey/edtech-masterplan",
        "filename": "singapore-moe-edtech-masterplan.html",
        "type": "html",
        "rubric_score": "4.9 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "singapore-moe-ai-in-education-framework-sls.md",
    },
    {
        "slug": "cbse-nep2020-secondary-ai-curriculum-guidelines",
        "title": "CBSE Secondary AI Curriculum & Skill Education Portal",
        "url": "https://cbseacademic.nic.in/ai.html",
        "filename": "cbse-academic-ai-portal.html",
        "type": "html",
        "rubric_score": "4.7 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "cbse-nep2020-secondary-ai-curriculum-guidelines.md",
    },
    {
        "slug": "china-moe-k12-ai-curriculum-guidelines-2025",
        "title": "China MOE K-12 AI Curriculum & Pedagogy Guidelines (2025)",
        "url": "http://english.moe.gov.cn/",
        "filename": "china-moe-official-portal.html",
        "type": "html",
        "rubric_score": "4.9 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "china-moe-k12-ai-curriculum-guidelines-2025.md",
    },
    {
        "slug": "south-korea-ai-digital-textbooks-policy-2025",
        "title": "South Korea AI Digital Textbooks Policy Case (2024-2025)",
        "url": "https://www.moe.go.kr/eng/main.do",
        "filename": "south-korea-moe-english-portal.html",
        "type": "html",
        "rubric_score": "4.6 / 5.0",
        "tier": "Tier 1 (Foundational)",
        "summary_file": "south-korea-ai-digital-textbooks-policy-2025.md",
    },
]

# ──────────────────────────────────────────────────────────────────────────────
# Project 2: Research AI in India
# ──────────────────────────────────────────────────────────────────────────────
RESEARCH_AI_IN_INDIA_SOURCES = [
    {
        "slug": "indiaai-mission-implementation-progress-2024-2026",
        "title": "PIB: Cabinet Approves Comprehensive IndiaAI Mission (₹10,372 Cr)",
        "url": "https://pib.gov.in/PressReleaseIframePage.aspx?PRID=2012011",
        "filename": "pib-indiaai-mission-cabinet-approval-2024.html",
        "type": "html",
        "rubric_score": "4.9 / 5.0",
        "tier": "Tier 1 (Empirical / Strategic)",
        "summary_file": "indiaai-mission-implementation-progress-2024-2026.md",
    },
    {
        "slug": "indiaai-national-portal-overview",
        "title": "IndiaAI National Portal & Compute Ecosystem",
        "url": "https://indiaai.gov.in/",
        "filename": "indiaai-national-portal.html",
        "type": "html",
        "rubric_score": "4.8 / 5.0",
        "tier": "Tier 1 (Empirical / Strategic)",
        "summary_file": "india-ai-governance-guidelines-2025.md",
    },
    {
        "slug": "niti-aayog-responsible-ai-approach",
        "title": "NITI Aayog: Towards Responsible AI for All (2021 Official Strategy)",
        "url": "https://www.niti.gov.in/sites/default/files/2021-02/Responsible-AI-22022021.pdf",
        "filename": "niti-aayog-responsible-ai-approach-2021.pdf",
        "type": "pdf",
        "rubric_score": "4.7 / 5.0",
        "tier": "Tier 1 (Foundational / Policy)",
        "summary_file": "niti-aayog-ai-inclusive-development-shramsestu-2025.md",
    },
    {
        "slug": "niti-aayog-national-strategy-for-ai",
        "title": "NITI Aayog: National Strategy for Artificial Intelligence (#AIforAll)",
        "url": "https://www.niti.gov.in/sites/default/files/2023-03/National-Strategy-for-Artificial-Intelligence.pdf",
        "filename": "niti-aayog-national-strategy-for-ai.pdf",
        "type": "pdf",
        "rubric_score": "4.8 / 5.0",
        "tier": "Tier 1 (Foundational / Policy)",
        "summary_file": "niti-aayog-ai-inclusive-development-shramsestu-2025.md",
    },
    {
        "slug": "india-semiconductor-mission-meity",
        "title": "MeitY / ISM: India Semiconductor Mission Official Framework",
        "url": "https://www.meity.gov.in/esdm/ism",
        "filename": "meity-india-semiconductor-mission.html",
        "type": "html",
        "rubric_score": "4.8 / 5.0",
        "tier": "Tier 1 (Empirical / Strategic)",
        "summary_file": "india-semiconductor-mission-ai-hardware-sovereignty.md",
    },
    {
        "slug": "drdo-national-defense-ai",
        "title": "DRDO: Defence Research and Development Organisation National Portal",
        "url": "https://www.drdo.gov.in/",
        "filename": "drdo-defense-technology-portal.html",
        "type": "html",
        "rubric_score": "4.5 / 5.0",
        "tier": "Tier 1 (Empirical / Strategic)",
        "summary_file": "india-ai-defense-national-security-2025.md",
    },
]


def download_with_curl(url: str, dest_path: Path, timeout: int = 30) -> dict:
    """Download a file using system curl.exe with robust parameters."""
    result = {
        "url": url,
        "dest": str(dest_path),
        "status": "unknown",
        "http_code": 0,
        "size_bytes": 0,
    }

    if dest_path.exists() and dest_path.stat().st_size > 0:
        result["status"] = "skipped (already exists)"
        result["size_bytes"] = dest_path.stat().st_size
        return result

    # Temporary file during download
    temp_dest = dest_path.with_suffix(dest_path.suffix + ".tmp")
    if temp_dest.exists():
        temp_dest.unlink()

    cmd = [
        "curl.exe",
        "-L",  # follow redirects
        "-k",  # allow insecure SSL if government certs expire
        "-s",  # silent
        "-A", USER_AGENT,
        "--max-time", str(timeout),
        "-o", str(temp_dest),
        "-w", "%{http_code}",
        url,
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        http_code_str = proc.stdout.strip()
        http_code = int(http_code_str) if http_code_str.isdigit() else 0
        result["http_code"] = http_code

        if http_code in (200, 206) and temp_dest.exists() and temp_dest.stat().st_size > 0:
            temp_dest.rename(dest_path)
            result["status"] = "downloaded"
            result["size_bytes"] = dest_path.stat().st_size
        else:
            if temp_dest.exists():
                temp_dest.unlink()
            result["status"] = f"HTTP {http_code}" if http_code > 0 else "failed (no response)"
    except subprocess.TimeoutExpired:
        if temp_dest.exists():
            temp_dest.unlink()
        result["status"] = f"timeout (>{timeout}s)"
    except Exception as e:
        if temp_dest.exists():
            temp_dest.unlink()
        result["status"] = f"error: {str(e)}"

    return result


def download_project_literature(project_slug: str, sources: list) -> list:
    """Download all registered literature sources for a project track."""
    lit_dir = PROJECTS_DIR / project_slug / "literature"
    lit_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*75}")
    print(f"  PROJECT LITERATURE SURVEY: {project_slug}")
    print(f"  Destination: {lit_dir}")
    print(f"  Sources to process: {len(sources)}")
    print(f"{'='*75}")

    results = []
    for idx, src in enumerate(sources, 1):
        dest_file = lit_dir / src["filename"]
        print(f"\n  [{idx}/{len(sources)}] {src['title']}")
        print(f"    URL:      {src['url'][:75]}...")
        print(f"    File:     {src['filename']}")
        print(f"    Rubric:   {src['rubric_score']} ({src['tier']})")

        res = download_with_curl(src["url"], dest_file, timeout=25)
        res["title"] = src["title"]
        res["slug"] = src["slug"]
        res["rubric_score"] = src["rubric_score"]
        res["tier"] = src["tier"]
        res["summary_file"] = src["summary_file"]
        res["filename"] = src["filename"]
        results.append(res)

        kb = res["size_bytes"] / 1024.0
        status_tag = (
            "[OK]" if res["status"] == "downloaded" else
            "[EXISTS]" if "skipped" in res["status"] else
            "[FAIL]"
        )
        print(f"    {status_tag} Status: {res['status']} | Size: {kb:,.1f} KB")

        # Small pause between network requests
        if idx < len(sources):
            time.sleep(0.5)

    return results


def write_project_manifest_and_readme(project_slug: str, results: list):
    """Write _manifest.json and README.md in the project's literature/ folder."""
    lit_dir = PROJECTS_DIR / project_slug / "literature"

    # 1. Manifest JSON
    manifest = {
        "project": project_slug,
        "last_download_run": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "total_sources": len(results),
        "downloaded": sum(1 for r in results if r["status"] == "downloaded"),
        "cached_or_existing": sum(1 for r in results if "skipped" in r["status"]),
        "failed": sum(1 for r in results if r["status"] not in ("downloaded",) and "skipped" not in r["status"]),
        "sources": results,
    }
    manifest_path = lit_dir / "_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Manifest written: {manifest_path.relative_to(BASE_DIR)}")

    # 2. Markdown README
    lines = [
        f"# Literature Survey Source Archive: `{project_slug}`",
        "",
        f"> **Project Track**: [`projects/{project_slug}/`](../)",
        f"> **Survey Methodology**: `literature-survey` skill (4-Factor Standardized Rubric)",
        f"> **Last Updated**: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "This directory stores the primary source files (PDF reports, official gazettes, government announcements, and institutional webpages) evaluated and downloaded for this project track.",
        "Summaries and claim extractions are permanently archived in [`raw/literature/`](../../raw/literature/) and linked to atomic semantic notes in [`wiki/semantic/sources/`](../../wiki/semantic/sources/).",
        "",
        "## Downloaded Literature Registry",
        "",
        "| Source Title | File Name | Size (KB) | Composite Score | Tier | Raw Summary Link |",
        "| :--- | :--- | :---: | :---: | :---: | :--- |",
    ]

    for r in results:
        size_kb = r["size_bytes"] / 1024.0
        status_note = f"{size_kb:,.1f} KB" if r["size_bytes"] > 0 else f"Failed ({r['status']})"
        summary_link = f"[`raw/literature/{r['summary_file']}`](../../raw/literature/{r['summary_file']})"
        lines.append(
            f"| **{r['title']}** | [`{r['filename']}`](./{r['filename']}) | {status_note} | {r['rubric_score']} | {r['tier']} | {summary_link} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## Traceability & Immutability Protocol",
        "1. Primary documents in this folder are read-only reference materials.",
        "2. Analytical syntheses must cite specific section numbers or page coordinates.",
        "3. See [`literature-survey.md`](../literature-survey.md) for full evaluative commentary and cross-source comparative matrices.",
    ])

    readme_path = lit_dir / "README.md"
    readme_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"  README written:   {readme_path.relative_to(BASE_DIR)}")


def main():
    print("=" * 75)
    print("  JP AI FUTURE STUDY GROUP — Automated Literature Downloader")
    print("  Target: projects/<project>/literature/ + raw/literature/ link")
    print("=" * 75)

    # 1. Teacher Training Project
    res_teacher = download_project_literature(
        "teacher-training-high-school-ai-pedagogy",
        TEACHER_TRAINING_SOURCES,
    )
    write_project_manifest_and_readme("teacher-training-high-school-ai-pedagogy", res_teacher)

    # 2. AI in India Research Project
    res_india = download_project_literature(
        "research-ai-in-india",
        RESEARCH_AI_IN_INDIA_SOURCES,
    )
    write_project_manifest_and_readme("research-ai-in-india", res_india)

    # Overall Summary
    total_sources = res_teacher + res_india
    successful = sum(1 for r in total_sources if r["status"] in ("downloaded",) or "skipped" in r["status"])
    failed = len(total_sources) - successful

    print(f"\n{'='*75}")
    print(f"  DOWNLOAD EXECUTION SUMMARY")
    print(f"  Total Sources: {len(total_sources)}")
    print(f"  Available on Disk: {successful} / {len(total_sources)}")
    print(f"  Failed: {failed}")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    main()
