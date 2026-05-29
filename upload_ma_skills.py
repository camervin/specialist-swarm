"""
Upload M&A diligence skills (Card B) via the Skills API and attach them to the
right specialist agents.

Uses `files_from_dir` (from anthropic.lib) to package each skill directory.
Each skill bundle must contain a SKILL.md at its root with proper YAML
frontmatter (`name` and `description`).

Usage:
    python upload_ma_skills.py
"""

import json
import os
from pathlib import Path

from anthropic import Anthropic
from anthropic.lib import files_from_dir


# Map skill directory name → specialist key that should get it
SKILL_TO_SPECIALIST = {
    "financial-analysis":  "financial_analyst",
    "legal-diligence":     "legal_diligence",
    "tech-stack-assessment": "tech_stack_assessor",
    "people-culture":      "people_culture",
}


def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("Set ANTHROPIC_API_KEY before running.")

    specialist_ids_path = Path(".ma_specialist_ids.json")
    if not specialist_ids_path.exists():
        raise SystemExit("Run create_ma_specialists.py first.")
    specialist_ids = json.loads(specialist_ids_path.read_text())

    client = Anthropic()

    print("Checking for existing skills...")
    existing_by_title: dict[str, str] = {}
    for page in client.beta.skills.list(source="custom"):
        existing_by_title[page.display_title] = page.id

    uploaded: dict[str, str] = {}

    for skill_name, specialist_key in SKILL_TO_SPECIALIST.items():
        skill_dir = Path("skills") / skill_name
        if not (skill_dir / "SKILL.md").exists():
            print(f"  Skipping {skill_name} — no SKILL.md found")
            continue

        display_title = skill_name.replace("-", " ").title()

        if display_title in existing_by_title:
            skill_id = existing_by_title[display_title]
            print(f"Reusing existing skill: {skill_name} ({skill_id})")
            uploaded[skill_name] = skill_id
        else:
            print(f"Uploading skill: {skill_name}...")
            skill = client.beta.skills.create(
                display_title=display_title,
                files=files_from_dir(str(skill_dir)),
            )
            uploaded[skill_name] = skill.id
            print(f"  -> {skill.id}")

        specialist_id = specialist_ids[specialist_key]
        skill_id = uploaded[skill_name]
        print(f"  attaching to specialist `{specialist_key}` ({specialist_id})...")

        current = client.beta.agents.retrieve(specialist_id)
        already_attached = any(
            s.get("skill_id") == skill_id for s in (current.skills or [])
        )
        if already_attached:
            print(f"  already attached ✓ (skipping)")
            continue

        new_skills = list(current.skills or []) + [
            {"type": "custom", "skill_id": skill_id, "version": "latest"}
        ]
        client.beta.agents.update(
            specialist_id,
            version=current.version,
            skills=new_skills,
        )
        print(f"  attached ✓")

    Path(".ma_skill_ids.json").write_text(json.dumps(uploaded, indent=2))
    print(f"\nUploaded {len(uploaded)} skills and attached them to specialists.")
    print("Next: python create_ma_coordinator.py")


if __name__ == "__main__":
    main()
