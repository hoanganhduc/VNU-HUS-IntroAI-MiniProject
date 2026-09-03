#!/usr/bin/env python3
"""Optional structural self-check for the manually graded final project.

This program is deliberately offline and awards no points. It checks observable
file structure, required fields, and starter placeholders. It does not contact
GitHub, execute project code, judge project quality, or approve a topic.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable, Sequence


PLACEHOLDER_PATTERNS = (
    "REPLACE_THIS_TEXT",
    "REPLACE_PROJECT_TITLE",
    "REPLACE_GROUP_NAME",
    "REPLACE_WITH_GITHUB_USERNAME",
    "REPLACE_WITH_OFFICIAL_FULL_NAME",
    "REPLACE_WITH_STUDENT_ID",
    "REPLACE_WITH_MAT1206E_OR_MAT3508",
    "REPLACE PROJECT TITLE",
    "REPLACE GROUP NAME",
    "REPLACE GITHUB USERNAME",
    "REPLACE SUBMISSION DATE",
    "REPLACE_WITH_PRIVATE_REPOSITORY_URL",
    "THAY TÊN DỰ ÁN",
    "THAY TÊN NHÓM",
    "THAY TÊN GITHUB",
    "THAY NGÀY NỘP",
    "THAY_BẰNG_LIÊN_KẾT_KHO_RIÊNG_TƯ",
    "TODO",
)

PROPOSAL_FIELDS = (
    "PROJECT_TITLE",
    "TOPIC_SOURCE",
    "PUBLIC_SUMMARY",
    "SELECTED_PROBLEM",
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

TEAM_KEYS = {"course", "group_name", "founder", "members"}
MEMBER_KEYS = {"full_name", "student_id", "github_username"}
USERNAME_PATTERN = re.compile(
    r"(?=.{1,39}\Z)(?!-)[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\Z"
)

EXACT_FORBIDDEN_PATHS = (
    Path(".classroom50.yaml"),
    Path(".classroom50.yml"),
    Path("classroom50-tests.json"),
    Path("autograder.py"),
)

PROPOSAL_CHECKLIST_HEADING = "## Group self-check / Nhóm tự kiểm tra"
PROPOSAL_CHECKLIST_ITEM_COUNT = 10
CHECKBOX_PATTERN = re.compile(r"^- \[([ xX])\] ", re.MULTILINE)


def is_regular_file(path: Path) -> bool:
    return path.is_file() and not path.is_symlink()


def contains_placeholder(text: str) -> bool:
    folded = text.casefold()
    return any(token.casefold() in folded for token in PLACEHOLDER_PATTERNS)


def marked_value(text: str, name: str) -> tuple[str | None, list[str]]:
    begin = f"<!-- BEGIN:{name} -->"
    end = f"<!-- END:{name} -->"
    errors: list[str] = []
    begin_count = text.count(begin)
    end_count = text.count(end)
    if begin_count != 1:
        errors.append(f"{begin} must occur exactly once (found {begin_count})")
    if end_count != 1:
        errors.append(f"{end} must occur exactly once (found {end_count})")
    if errors:
        return None, errors
    start = text.index(begin) + len(begin)
    stop = text.find(end, start)
    if stop < start:
        return None, [f"{end} must occur after {begin}"]
    return text[start:stop].strip(), []


def check_marked_file(
    path: Path,
    field_names: Iterable[str],
    passes: list[str],
    failures: list[str],
) -> None:
    if not is_regular_file(path):
        failures.append(f"required file {path} must be a regular non-symlink file")
        return
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        failures.append(f"{path} is not valid UTF-8: {error}")
        return
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


def filled_string(
    value: Any, label: str, passes: list[str], failures: list[str]
) -> str | None:
    if not isinstance(value, str):
        failures.append(f"{label} must be a string")
        return None
    stripped = value.strip()
    if not stripped or contains_placeholder(stripped):
        failures.append(f"{label} must be filled")
        return None
    passes.append(f"{label} is filled")
    return stripped


def load_team(
    passes: list[str], failures: list[str]
) -> tuple[dict[str, Any] | None, list[dict[str, str]]]:
    path = Path("team.json")
    if not is_regular_file(path):
        failures.append("required file team.json must be a regular non-symlink file")
        return None, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        failures.append(f"team.json is invalid UTF-8 JSON: {error}")
        return None, []
    if not isinstance(data, dict):
        failures.append("team.json must contain a JSON object")
        return None, []

    keys = set(data)
    if keys != TEAM_KEYS:
        missing = sorted(TEAM_KEYS - keys)
        extra = sorted(keys - TEAM_KEYS)
        if missing:
            failures.append("team.json missing key(s): " + ", ".join(missing))
        if extra:
            failures.append("team.json has unexpected key(s): " + ", ".join(extra))
    else:
        passes.append("team.json has the exact top-level schema")

    course = data.get("course")
    if course not in {"MAT1206E", "MAT3508"}:
        failures.append("team.json.course must be MAT1206E or MAT3508")
    else:
        passes.append(f"team.json.course is {course}")

    filled_string(data.get("group_name"), "team.json.group_name", passes, failures)

    founder_raw = data.get("founder")
    founder = filled_string(founder_raw, "team.json.founder", passes, failures)
    if founder is not None and USERNAME_PATTERN.fullmatch(founder) is None:
        failures.append("team.json.founder must be a valid GitHub username")

    raw_members = data.get("members")
    if not isinstance(raw_members, list) or not 1 <= len(raw_members) <= 5:
        failures.append("team.json.members must contain one to five member objects")
        return data, []

    members: list[dict[str, str]] = []
    usernames: list[str] = []
    student_ids: list[str] = []
    for index, raw_member in enumerate(raw_members, start=1):
        label = f"team.json.members[{index - 1}]"
        if not isinstance(raw_member, dict):
            failures.append(f"{label} must be an object")
            continue
        keys = set(raw_member)
        if keys != MEMBER_KEYS:
            missing = sorted(MEMBER_KEYS - keys)
            extra = sorted(keys - MEMBER_KEYS)
            if missing:
                failures.append(f"{label} missing key(s): " + ", ".join(missing))
            if extra:
                failures.append(f"{label} has unexpected key(s): " + ", ".join(extra))

        full_name = filled_string(
            raw_member.get("full_name"), f"{label}.full_name", passes, failures
        )
        student_id = filled_string(
            raw_member.get("student_id"), f"{label}.student_id", passes, failures
        )
        username = filled_string(
            raw_member.get("github_username"),
            f"{label}.github_username",
            passes,
            failures,
        )
        if username is not None and USERNAME_PATTERN.fullmatch(username) is None:
            failures.append(f"{label}.github_username is not a valid GitHub username")

        if full_name is not None and student_id is not None and username is not None:
            members.append(
                {
                    "full_name": full_name,
                    "student_id": student_id,
                    "github_username": username,
                }
            )
            usernames.append(username)
            student_ids.append(student_id)

    folded_usernames = [value.casefold() for value in usernames]
    if len(folded_usernames) != len(set(folded_usernames)):
        failures.append("team.json.members contains duplicate GitHub usernames")
    elif len(usernames) == len(raw_members):
        passes.append(f"team.json lists {len(usernames)} distinct member(s)")

    folded_ids = [value.casefold() for value in student_ids]
    if len(folded_ids) != len(set(folded_ids)):
        failures.append("team.json.members contains duplicate student IDs")
    elif len(student_ids) == len(raw_members):
        passes.append("team.json student IDs are distinct")

    if founder is not None and USERNAME_PATTERN.fullmatch(founder):
        if founder.casefold() not in set(folded_usernames):
            failures.append("team.json.founder must appear among member GitHub usernames")
        else:
            passes.append("team.json founder is one of the listed members")

    return data, members


def check_forbidden_controls(passes: list[str], failures: list[str]) -> None:
    found: list[str] = []
    for path in EXACT_FORBIDDEN_PATHS:
        if path.exists() or path.is_symlink():
            found.append(str(path))
    autograder_dir = Path("autograder")
    if autograder_dir.exists() or autograder_dir.is_symlink():
        found.append(str(autograder_dir))
    workflows = Path(".github/workflows")
    if workflows.is_symlink():
        found.append(str(workflows))
    elif workflows.is_dir():
        for path in sorted(workflows.iterdir()):
            folded_name = path.name.casefold()
            if "autograd" in folded_name or "classroom50" in folded_name:
                found.append(str(path))
    if found:
        failures.append(
            "manual final project must not contain Classroom50/autograding control(s): "
            + ", ".join(found)
        )
    else:
        passes.append("no Classroom50/autograding control file was found")


def check_proposal_checklist(
    path: Path, passes: list[str], failures: list[str]
) -> None:
    if not is_regular_file(path):
        return
    text = path.read_text(encoding="utf-8")
    if text.count(PROPOSAL_CHECKLIST_HEADING) != 1:
        failures.append(
            f"{path}: {PROPOSAL_CHECKLIST_HEADING!r} must occur exactly once"
        )
        return
    section = text.split(PROPOSAL_CHECKLIST_HEADING, 1)[1]
    next_heading = re.search(r"^## ", section, flags=re.MULTILINE)
    if next_heading:
        section = section[: next_heading.start()]
    states = CHECKBOX_PATTERN.findall(section)
    if len(states) != PROPOSAL_CHECKLIST_ITEM_COUNT:
        failures.append(
            f"{path}: group self-check must contain exactly "
            f"{PROPOSAL_CHECKLIST_ITEM_COUNT} checkbox items (found {len(states)})"
        )
        return
    unchecked = sum(state == " " for state in states)
    if unchecked:
        failures.append(
            f"{path}: group self-check has {unchecked} unchecked item(s)"
        )
    else:
        passes.append("proposal group self-check is complete")


def check_proposal(
    passes: list[str], failures: list[str]
) -> tuple[dict[str, Any] | None, list[dict[str, str]]]:
    team, members = load_team(passes, failures)
    proposal_path = Path("proposal/proposal.md")
    check_marked_file(proposal_path, PROPOSAL_FIELDS, passes, failures)
    check_proposal_checklist(proposal_path, passes, failures)
    check_forbidden_controls(passes, failures)
    return team, members


def check_plain_file(path: Path, passes: list[str], failures: list[str]) -> str | None:
    if not is_regular_file(path):
        failures.append(f"required file {path} must be a regular non-symlink file")
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        failures.append(f"{path} is not valid UTF-8: {error}")
        return None
    if not text.strip():
        failures.append(f"required file {path} is empty")
    elif contains_placeholder(text):
        failures.append(f"required file {path} still contains a starter placeholder")
    else:
        passes.append(f"required file {path} is filled")
    return text


def check_pdf(path: Path, passes: list[str], failures: list[str]) -> None:
    if not is_regular_file(path):
        failures.append(f"required PDF {path} must be a regular non-symlink file")
        return
    data = path.read_bytes()
    if len(data) < 100 or not data.startswith(b"%PDF-"):
        failures.append(f"{path} is not a nonempty PDF file")
    else:
        passes.append(f"{path} has a PDF signature")


def check_identity_in_readme(
    readme: str, members: Sequence[dict[str, str]], passes: list[str], failures: list[str]
) -> None:
    for member in members:
        missing = [
            value
            for value in (
                member["full_name"],
                member["student_id"],
                member["github_username"],
            )
            if value not in readme
        ]
        if missing:
            failures.append(
                "README.md does not contain every private identity value for "
                + member["github_username"]
            )
        else:
            passes.append(
                "README.md contains the private identity triplet for "
                + member["github_username"]
            )


def check_final(passes: list[str], failures: list[str]) -> None:
    team, members = check_proposal(passes, failures)

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
        check_identity_in_readme(root_text, members, passes, failures)
        if isinstance(team, dict):
            group_name = team.get("group_name")
            if isinstance(group_name, str) and group_name.strip():
                if group_name.strip() not in root_text:
                    failures.append("README.md must contain team.json.group_name")
                else:
                    passes.append("README.md contains team.json.group_name")

    check_pdf(Path("report/report.pdf"), passes, failures)
    check_pdf(Path("slides/slides.pdf"), passes, failures)
    check_marked_file(Path("project/README.md"), PROJECT_FIELDS, passes, failures)
    check_marked_file(Path("docs/AI_USAGE.md"), AI_FIELDS, passes, failures)
    check_marked_file(
        Path("docs/EXTERNAL_RESOURCES.md"), EXTERNAL_FIELDS, passes, failures
    )

    contributions = check_plain_file(Path("docs/CONTRIBUTIONS.md"), passes, failures)
    if contributions is not None:
        missing = [
            member["github_username"]
            for member in members
            if member["github_username"] not in contributions
        ]
        if missing:
            failures.append(
                "docs/CONTRIBUTIONS.md does not name member(s): " + ", ".join(missing)
            )
        elif members:
            passes.append("docs/CONTRIBUTIONS.md names every team member")


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
