# Class project-topic board

This private repository is visible to one course and is not a second Classroom50
assignment. It records class-visible proposal summaries, exact-duplicate status,
proposal updates, administrative requests, presentation information, and final
commit URLs. It assigns no score.

## Student workflow

1. Complete and commit `team.json` and `proposal/proposal.md` in the group's
   private Classroom50 repository.
2. Ensure every listed member agrees to that exact commit.
3. Search this board for the exact group-repository URL and founder username.
4. If a valid issue already exists, continue in it; do not create another.
5. Otherwise, the founder as default issue custodian chooses
   **Issues -> New issue -> Project topic proposal**, completes every field, and
   links the exact proposal commit.
6. Keep every proposal update, membership request, issue-custodian handover,
   schedule notice, and final submission in that one issue.

The founder is an administrative representative, not the unilateral project
decision-maker. The issue is opened only after all members agree. Another agreed
member may become issue custodian through a recorded handover in the existing
issue, never by opening a replacement issue.

## Privacy

The issue is class-visible. Use GitHub usernames only. Do not post official full
names, student IDs, email addresses, phone numbers, credentials, private keys, or
other unnecessary personal information.

The linked commit in the private group repository is the authoritative full
proposal. The issue is its class-visible summary and discussion record.

## One canonical issue per group repository

The exact Classroom50 group-repository URL is the stable identifier. The earliest
**valid** issue by GitHub creation time for that repository is canonical. A valid
issue:

- is on the correct course board;
- contains every required Issue Form field;
- names the actual final-project repository; and
- links a proposal commit from that repository.

Validity is evaluated when staff first process competing issues. Once staff
identifies the canonical issue, that choice is stable. An earlier incomplete
issue repaired later does not displace an issue already selected as canonical.

If a later issue is opened for the same repository, staff comment:

```text
Duplicate of #<canonical-issue-number>

Continue all proposal updates, scheduling, and final submission in the original issue.
```

Staff then close the later issue. Only the canonical issue carries topic status,
updates, administrative requests, scheduling, and `FINAL SUBMISSION`.

A duplicate issue is not the same as two different repositories selecting the
same exact problem.

## Exact-duplicate check

Canonical issues use only the labels in [`labels.md`](labels.md):

```text
status: submitted
status: recorded
status: duplicate-problem
```

Staff compare the exact selected problem with earlier `status: recorded` issues.
A common area, method, dataset family, or application domain is not by itself an
exact duplicate.

When no earlier exact duplicate is found, staff use `status: recorded`. This
means only that the exact-duplicate check passed at that time; it does not certify
quality, feasibility, scope, method, correctness, resources, or expected results.

When a different group already recorded the same exact problem, the later issue
receives `status: duplicate-problem`. The group updates its private proposal and
the same canonical issue. The issue is not closed for this reason.

## Later updates

Use the formats documented in the student Submission Guide:

- `PROPOSAL UPDATE` for a new proposal commit;
- `MEMBERSHIP CHANGE REQUEST` for a proposed membership change;
- `ISSUE CUSTODIAN HANDOVER` when another agreed member takes over issue upkeep;
- `FINAL SUBMISSION` for the exact final commit.

When the selected problem changes, staff temporarily return the issue to
`status: submitted` and repeat only the exact-duplicate check. Other academic or
technical changes need no new status and do not extend the final deadline.
