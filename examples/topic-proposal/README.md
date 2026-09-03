# Worked topic-proposal example / Ví dụ hoàn chỉnh về đề xuất chủ đề

> **Fictional and illustrative only.** Do not edit these files as the real
> submission, and do not copy their identities, topic, commit, or prose. The
> example is not prior approval, a guaranteed passing submission, a reserved
> topic, a minimum-quality benchmark, or a rubric model answer.

This directory shows one complete path from group agreement to the class-visible
topic issue:

1. All members agree on one same-course group, one exact problem, and a bounded
   scope.
2. The founder alone accepts the Classroom50 group assignment and adds the other
   agreed members. This is an administrative role, not unilateral authority over
   the project.
3. The group uses [`team.example.json`](team.example.json) as a model for the
   private root `team.json`. Full names and student IDs stay in the private group
   repository.
4. The group collaborates on the private proposal, using
   [`proposal.example.md`](proposal.example.md) only as a structural model.
5. In a temporary copy, the example files can replace the root templates and
   pass `python3 check_project_files.py proposal`; the command assigns no score.
6. The proposal is committed only after every member agrees to that exact
   version.
7. The founder, as default issue custodian, searches the correct board for the
   exact group-repository URL and founder username. If no canonical issue exists,
   the founder opens one issue using the content model in
   [`topic-issue.example.md`](topic-issue.example.md).
8. All later proposal updates, issue-custodian handovers, membership requests,
   scheduling, and final submission remain in that one canonical issue.

A different agreed member may become issue custodian only through a recorded
handover in the existing canonical issue. The group must never open a replacement
issue merely because the custodian changes.

## Privacy boundary

The private membership example contains fictional full names, fictional student
identifiers, and fictional GitHub usernames. The class-visible issue example
contains GitHub usernames only. Real students must apply the same separation.

## Illustrative topic

The example consistently uses:

> Comparing breadth-first search, uniform-cost search, and A* on a synthetic
> campus-routing graph.

The topic is selected because it permits a precise problem, explicit non-goals,
reproducible synthetic data, and meaningful comparisons. It does not prescribe
what another group must build.
