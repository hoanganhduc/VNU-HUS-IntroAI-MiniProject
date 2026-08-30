#!/usr/bin/env python3
"""Optional structural self-check for the manually graded final project.

This program awards no points and makes no claim about project correctness or
quality. It checks only observable file structure and starter placeholders.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable


PLACEHOLDER_PATTERNS = (
    "REPLACE_THIS_TEXT",
    "REPLACE_PROJECT_TITLE",
    "REPLACE_GROUP_NAME",
    "REPLACE_WITH_GITHUB_USERNAME",
    "REPLACE_WITH_MAT1206E_OR_MAT3508",
    "TODO",
)

PROPOSAL_FIELDS = (
    "PROJECT_TITLE",
    "TOPIC_SOURCE",
    "PUBLIC_SUMMARY",
    "PROBLEM_AND_MOTIVATION",
    "SCOPE_AND_FEASIBILITY",
    "PLANNED_METHOD",
    "DATA_TOOLS_AND_SOURCES",
    "EXPECTED_OUTPUT",
    "MILESTONES",
    "REFERENCES",
    "CONSIDERATIONS",
)

PROJECT_FIELDS = (
    "PROJECT_STRUCTURE",
    "SETUP",
    "INPUTS_AND_OUTPUTS",
    "REPRODUCTION",
    "LIMITATIONS",
)

AI_FIELDS = (
    "AI_TOOLS_AND_PURPOSES",
    "AI_VERIFICATION",
)

EXTERNAL_FIELDS = (
    "RESOURCES_AND_PROVENANCE",
    "LICENSE_AND_ACCESS",
    "SETUP_AND_PREPROCESSING",
    "REPRODUCIBILITY_LIMITS",
)

USERNAME_PATTERN = re.compile(
    r"(?=.{1,39}\Z)(?!-)[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\Z"
)


def marked_value(text: str, name: str) -> tuple[str | None, list[str]]:
    begin = f"<!-- BEGIN:{name} -->"
    end = f"<!-- END:{name} -->"
    errors: list[str] = []
    begin_count = text.count(begin)
    end_count = text.count(end)
    if begin_count != 1:
        errors.append(f'{begin} must occur exactly once (found {begin_count})')
    if end_count != 1:
        errors.append(f'{end} must occur exactly once (found {end_count})')
    if errors:
        return None, errors
    start = text.index(begin) + len(begin)
    stop = text.index(end, start)
    return text[start:stop].strip(), []


def contains_placeholder(text: str) -> bool:
    return any(token in text for token in PLACEHOLDER_PATTERNS)


def check_marked_file(
    path: Path,
    field_names: Iterable[str],
    passes: list[str],
    failures: list[str],
) -> None:
    if not path.is_file():
        failures.append(f"required file {path} does not exist")
        return
    text = path.read_text(encoding="utf-8")
    for name in field_names:
        value, errors = marked_value(text, name)
        failures.extend(f"{path}: {error}" for error in errors)
        if value is None:
            continue
        if not value:
            failures.append(f"{path}: field {name} is empty")
        elif contains_placeholder(value):
            failures.append(f"{path}: field {name} still contains a placeholder")
        else:
            passes.append(f"{path}: field {name} is filled")


def load_team(
    passes: list[str], failures: list[str]
) -> tuple[dict[str, Any] | None, list[str]]:
    path = Path("team.json")
    if not path.is_file():
        failures.append("required file team.json does not exist")
        return None, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        failures.append(f"team.json is invalid JSON: {error}")
        return None, []
    if not isinstance(data, dict):
        failures.append("team.json must contain a JSON object")
        return None, []

    course = data.get("course")
    if course not in {"MAT1206E", "MAT3508"}:
        failures.append("team.json.course must be MAT1206E or MAT3508")
    else:
        passes.append(f"team.json.course is {course}")

    group_name = data.get("group_name")
    if not isinstance(group_name, str) or not group_name.strip() or contains_placeholder(
        group_name
    ):
        failures.append("team.json.group_name must be filled")
    else:
        passes.append("team.json.group_name is filled")

    founder = data.get("founder")
    if not isinstance(founder, str) or USERNAME_PATTERN.fullmatch(founder) is None:
        failures.append("team.json.founder must be one valid GitHub username")

    members = data.get("members")
    if not isinstance(members, list) or not 1 <= len(members) <= 5:
        failures.append("team.json.members must contain one to five usernames")
        return data, []
    if not all(isinstance(value, str) for value in members):
        failures.append("every team.json member must be a string")
        return data, []

    invalid = [value for value in members if USERNAME_PATTERN.fullmatch(value) is None]
    if invalid:
        failures.append(f"invalid GitHub username(s) in team.json: {', '.join(invalid)}")

    folded = [value.casefold() for value in members]
    if len(folded) != len(set(folded)):
        failures.append("team.json.members contains duplicate usernames")
    else:
        passes.append(f"team.json lists {len(members)} distinct member(s)")

    if isinstance(founder, str) and founder.casefold() not in set(folded):
        failures.append("team.json.founder must also appear in team.json.members")
    elif isinstance(founder, str) and USERNAME_PATTERN.fullmatch(founder):
        passes.append("team.json founder is one of the listed members")

    return data, members


def check_proposal(
    passes: list[str], failures: list[str]
) -> tuple[dict[str, Any] | None, list[str]]:
    team, members = load_team(passes, failures)
    check_marked_file(
        Path("proposal/proposal.md"), PROPOSAL_FIELDS, passes, failures
    )
    return team, members


def check_plain_file(path: Path, passes: list[str], failures: list[str]) -> str | None:
    if not path.is_file():
        failures.append(f"required file {path} does not exist")
        return None
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        failures.append(f"required file {path} is empty")
        return text
    if contains_placeholder(text):
        failures.append(f"required file {path} still contains a starter placeholder")
    else:
        passes.append(f"required file {path} is filled")
    return text


def check_pdf(path: Path, passes: list[str], failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"required PDF {path} does not exist")
        return
    data = path.read_bytes()
    if len(data) < 100 or not data.startswith(b"%PDF-"):
        failures.append(f"{path} is not a nonempty PDF file")
    else:
        passes.append(f"{path} has a PDF signature")


def check_final(passes: list[str], failures: list[str]) -> None:
    _, members = check_proposal(passes, failures)

    root_text = check_plain_file(Path("README.md"), passes, failures)
    if root_text is not None:
        for required_path in (
            "report/report.pdf",
            "slides/slides.pdf",
            "project/README.md",
            "docs/CONTRIBUTIONS.md",
            "docs/AI_USAGE.md",
            "docs/EXTERNAL_RESOURCES.md",
        ):
            if required_path not in root_text:
                failures.append(f"README.md must mention {required_path}")

    check_pdf(Path("report/report.pdf"), passes, failures)
    check_pdf(Path("slides/slides.pdf"), passes, failures)
    check_marked_file(Path("project/README.md"), PROJECT_FIELDS, passes, failures)
    check_marked_file(Path("docs/AI_USAGE.md"), AI_FIELDS, passes, failures)
    check_marked_file(
        Path("docs/EXTERNAL_RESOURCES.md"), EXTERNAL_FIELDS, passes, failures
    )

    contributions = check_plain_file(
        Path("docs/CONTRIBUTIONS.md"), passes, failures
    )
    if contributions is not None:
        missing = [member for member in members if member not in contributions]
        if missing:
            failures.append(
                "docs/CONTRIBUTIONS.md does not name member(s): "
                + ", ".join(missing)
            )
        elif members:
            passes.append("docs/CONTRIBUTIONS.md names every team member")

    for forbidden in (
        Path(".classroom50.yaml"),
        Path(".github/workflows/autograde.yaml"),
    ):
        if forbidden.exists():
            failures.append(f"manual final project must not contain {forbidden}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Optional no-score structural self-check for the final project."
    )
    parser.add_argument("mode", choices=("proposal", "final"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    passes: list[str] = []
    failures: list[str] = []

    if args.mode == "proposal":
        check_proposal(passes, failures)
    else:
        check_final(passes, failures)

    print(f"STRUCTURAL SELF-CHECK — {args.mode.upper()} MODE")
    print("No score is assigned. Project correctness and quality are not evaluated.\n")
    for message in passes:
        print(f"PASS {message}")
    for message in failures:
        print(f"FAIL {message}")

    if failures:
        print("\nSELF-CHECK INCOMPLETE — no score is assigned")
        return 1

    print("\nSELF-CHECK COMPLETE — no score is assigned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
