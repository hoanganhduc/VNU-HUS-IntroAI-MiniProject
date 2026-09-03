# Final-project submission guide / Hướng dẫn nộp dự án cuối kỳ

[English](#english) | [Tiếng Việt](#tiếng-việt)

This guide covers the complete manually graded group-project workflow. Classroom50
creates one empty private repository per group. GitHub stores the work and the
class-visible topic record. Classroom50 does not grade this assignment.

## English

### 1. Understand the workflow

The group uses three connected records:

1. one private Classroom50 project repository for identities, proposal, code,
   report, slides, and declarations;
2. one exact proposal commit in that repository; and
3. one canonical issue in the correct course topic board for the class-visible
   summary, exact-duplicate status, updates, scheduling, and final commit URL.

The proposal is required but ungraded. The optional local checker assigns no
points and does not certify feasibility, correctness, or quality. Final marks are
assigned manually using [`Rubrics.md`](Rubrics.md).

### 2. Record the calendar

| Milestone | Date and time (ICT, UTC+7) |
|---|---|
| Project materials released | 2026-09-04 13:00 |
| Classroom50 acceptance opens | 2026-09-11 13:00 |
| Recommended group-formation target | 2026-09-13 23:59 |
| Initial proposal commit and canonical issue due | 2026-09-20 23:59 |
| Exact-duplicate check completed | 2026-09-25 |
| Exact-duplicate correction due | 2026-09-27 23:59 |
| Final commit and `FINAL SUBMISSION` comment due | 2026-11-04 23:59 |
| Presentations begin | 2026-11-06 |

The final deadline is common to all groups and is not extended by presentation
order, proposal updates, or a change of selected problem.

### 3. Form the group and choose roles

Before anyone accepts the assignment:

1. agree on one to five members from the same course;
2. verify every member's GitHub username;
3. choose exactly one founder;
4. agree that the founder will perform the initial Classroom50 acceptance and
   serve as the default topic-issue custodian; and
5. review existing topics on the correct course board.

Only the founder accepts. Other members must not accept separately, because each
acceptance can create a different repository.

The founder is an administrative representative. The founder cannot
unilaterally choose or change the group, selected problem, scope, proposal, or
submitted commit. Every listed member must agree to those decisions.

### 4. Accept and bootstrap the empty repository

#### Classroom50 graphical path

1. Open the course's final-project acceptance link.
2. Sign in to Classroom50 with GitHub.
3. Open the VNU-HUS organization marked **Student**.
4. Open `final-project` and choose **Accept**.
5. Follow the resulting link to the private GitHub repository.

#### CLI alternative

```bash
gh student accept VNU-HUS <classroom> final-project
```

Use one acceptance route, not both.

The accepted repository is intentionally empty. Clone the reviewed public
starter, rename its original remote to `starter`, and add the empty assignment
repository as `origin`:

```bash
git clone https://github.com/VNU-HUS/introai-final-project-template.git final-project
cd final-project

git remote rename origin starter
git remote add origin <CLASSROOM50_ASSIGNMENT_REPOSITORY_URL>

git remote -v
git ls-remote --heads origin
git push -u origin HEAD:main
```

Before the first push, verify:

```text
starter -> VNU-HUS/introai-final-project-template
origin  -> this group's empty private Classroom50 repository
```

`git ls-remote --heads origin` should show no unexpected branch. Never push to
`starter`, never use the canonical source repository as `origin`, and never reuse
a repository from the other course.

### 5. Add members and record private identity

In Classroom50, open the accepted assignment, use the edit pencil, choose
**Manage collaborators**, and add the other zero to four agreed members. A
one-person group adds nobody.

CLI alternative for one member:

```bash
gh student invite VNU-HUS/<assignment-repository> <github-username>
```

An empty repository has no `.classroom50.yaml`, so CLI or direct GitHub
invitations may not enforce the configured maximum. The group and staff must
compare the actual collaborators with `team.json`; the total must remain one to
five, including the founder.

Fill the private `team.json` with:

- `MAT1206E` or `MAT3508`;
- group name;
- founder's GitHub username; and
- one to five member objects, each containing official full name, student ID,
  and GitHub username.

Put the same identity triplets in the private root README and final report. The
class-visible topic issue uses GitHub usernames only.

### 6. Study the worked example

Open [`examples/topic-proposal/README.md`](examples/topic-proposal/README.md)
with the whole group before editing the real files. It links:

- a filled private membership record;
- a complete proposal covering every required field; and
- the corresponding class-visible issue.

Every identity, identifier, repository, commit, and result in the example is
fictional. The example is not prior approval, a reserved topic, a guaranteed
passing proposal, a minimum-quality benchmark, or text that may be submitted
verbatim.

Students edit the real root `team.json` and `proposal/proposal.md`; the example
files remain unchanged as reference material.

### 7. Prepare the private proposal

Edit:

```text
team.json
proposal/proposal.md
```

The proposal must state:

- project title and topic source;
- class-visible summary;
- one exact selected problem;
- problem and motivation;
- student-defined scope, explicit non-goals, and feasibility;
- planned method;
- data, tools, papers, software, and existing projects;
- expected output or demonstration;
- milestones;
- references actually consulted; and
- relevant integrity, privacy, safety, and licensing considerations.

`Mini-Project Ideas.md` is optional inspiration. It does not define a minimum
project and does not remove the group's responsibility to choose a precise,
feasible problem.

Complete the checklist at the end of `proposal/proposal.md`. The exact proposal
commit must represent what every listed member agreed to.

### 8. Self-check, commit, and identify the proposal version

Run the optional structural check:

```bash
python3 check_project_files.py proposal
```

The command checks schema, required fields, placeholders, and prohibited
Classroom50 grading controls. It does not contact GitHub, run project code, judge
the topic, or assign a score.

After all members review the files:

```bash
git status
git add team.json proposal/proposal.md README.md
git diff --cached
git commit -m "Submit topic proposal"
git push
git rev-parse HEAD
```

Copy the permanent GitHub commit URL or complete 40-character SHA. A branch URL,
file URL without a commit, screenshot, or latest-branch link does not identify an
immutable proposal version.

### 9. Find or open the canonical topic issue

Before creating anything, search the correct course topic board for:

1. the exact Classroom50 group-repository URL; and
2. the founder's GitHub username.

If a valid issue for the repository already exists, it is the canonical issue.
Continue there and do not create another issue.

Otherwise, after every member agrees to the proposal commit, the founder as
default issue custodian:

1. opens **Issues -> New issue -> Project topic proposal**;
2. uses `[Proposal] <group name> — <project title>` as the title;
3. completes every required field;
4. lists GitHub usernames only;
5. pastes the exact group-repository URL and proposal commit URL or SHA; and
6. submits the issue.

The earliest valid issue by GitHub creation time for the exact group-repository
URL is canonical. A valid issue is on the correct course board, supplies every
required field, names the actual project repository, and links a proposal commit
from that repository. Validity is evaluated when staff first process competing
issues. Once staff records which issue is canonical, that choice is stable; an
earlier incomplete issue repaired later does not displace it.

If a later duplicate issue is opened for the same repository, stop using it.
Staff comment:

```text
Duplicate of #<canonical-issue-number>

Continue all proposal updates, scheduling, and final submission in the original issue.
```

The later issue is then closed. A duplicate issue is different from a duplicated
selected problem across two different groups.

### 10. Understand the exact-duplicate status

Canonical issues use only:

```text
status: submitted
status: recorded
status: duplicate-problem
```

- `status: submitted`: the selected problem awaits comparison with earlier
  recorded problems.
- `status: recorded`: staff found no earlier exact duplicate at the time of
  review. This does not certify scope, feasibility, method, correctness, or
  expected results.
- `status: duplicate-problem`: a different group repository already recorded the
  same exact problem. The group must revise the selected problem in the existing
  proposal and canonical issue.

A shared broad area, method, dataset family, or application domain is not by
itself an exact duplicate. When two groups select exactly the same problem, the
earlier complete canonical issue normally keeps it. The later group posts a
corrected proposal by 2026-09-27 at 23:59 ICT in the same issue.

### 11. Update the proposal

The proposal is a living plan. The group may change scope, method, data, tools,
implementation, expected output, or ambition without seeking academic
certification. Explain material changes in the final report.

Commit every proposal revision and comment in the canonical issue:

```text
PROPOSAL UPDATE

Previous proposal commit:
<old commit URL or SHA>

New proposal commit:
<new commit URL or SHA>

Selected problem changed: yes/no

Summary of changes:
- ...

Reason for the changes:
- ...
```

When the exact selected problem changes, staff temporarily return the issue to
`status: submitted` and repeat only the exact-duplicate check. Other proposal
changes need no new status. No update extends the common final deadline.

### 12. Change membership or issue custodian

Membership changes are administrative exceptions. Update `team.json`, commit the
change, and post in the canonical issue:

```text
MEMBERSHIP CHANGE REQUEST

Current members:
- ...

Proposed members:
- ...

Reason:
- ...

Commit updating team.json:
<commit URL or SHA>
```

The membership change takes effect only after explicit instructor confirmation.
Keep all members in one course and keep the group size between one and five.

When the founder cannot continue as issue custodian, the group may record one
handover without opening another issue:

```text
ISSUE CUSTODIAN HANDOVER

Previous custodian: @...
New custodian: @...
All listed members agree: yes
Reason: ...
```

A custodian handover does not alter the founder recorded as the student who
accepted the assignment, and it gives no member unilateral authority over the
project.

### 13. Develop the project

Use ordinary Git and GitHub collaboration:

```bash
git switch -c <short-purpose-branch>
git add <paths>
git commit -m "Describe the project change"
git push -u origin <short-purpose-branch>
```

Pull requests and peer review are recommended for multi-person groups. Commit
counts, pull-request counts, and lines changed are evidence, not point formulas.

Maintain throughout the project:

```text
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

Do not commit credentials, unnecessary personal data, unlawfully redistributed
material, or unexplained large dependencies. Record external resources, licenses,
access conditions, preprocessing, and reproducibility limitations.

### 14. Prepare the final repository and report

The final commit must include:

```text
README.md
team.json
proposal/proposal.md
report/report.pdf
slides/slides.pdf
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

The private README and report must identify every member by official full name,
student ID, and GitHub username. Remove unused placeholder rows. The report must
include **Changes from the submitted proposal** and describe material changes,
or state that none occurred.

Compile the chosen report template and place the result at
`report/report.pdf`. Place the final presentation at `slides/slides.pdf`.

Run:

```bash
python3 check_project_files.py final
```

This remains a no-score structural check. Passing it is not a grade or quality
judgment.

### 15. Record the final submission and present

After every member agrees to the exact final commit:

```bash
git status
git push
git rev-parse HEAD
```

Post in the canonical issue by 2026-11-04 at 23:59 ICT:

```text
FINAL SUBMISSION

Final commit:
<permanent commit URL or complete SHA>

Report:
report/report.pdf at the final commit

Slides:
slides/slides.pdf at the final commit

All listed members agree to this submitted version: yes
```

Do not create a new issue and do not use a Classroom50 grading or submission
trigger. The issue comment and exact Git commit identify the submitted version.

Presentations begin on 2026-11-06. Report and Slides include shared components;
Oral presentation/time management and Q&A are graded individually as specified in
the rubric.

### 16. Troubleshoot safely

- **Several students accepted separately:** stop using the duplicate repositories
  and contact staff before deleting or moving work. Do not merge identities or
  history without instructions.
- **Wrong remote:** do not push. Inspect `git remote -v` and correct the remote
  only after identifying the intended private group repository.
- **A canonical issue already exists:** continue in it. Do not open another.
- **A duplicate-problem status appears:** revise the exact selected problem and
  proposal, then update the same issue by the correction deadline.
- **A member changes:** use `MEMBERSHIP CHANGE REQUEST`; do not silently edit the
  roster.
- **The founder is unavailable:** record an issue-custodian handover in the same
  issue.
- **A large file is unsuitable for Git:** store it lawfully elsewhere and record
  source, license, retrieval, preprocessing, and reproduction details.
- **A secret was committed:** revoke it immediately, notify staff when exposure
  matters, and remove it using an appropriate history-cleanup procedure. A later
  deletion commit alone does not erase a secret from history.

## Tiếng Việt

### 1. Hiểu quy trình

Nhóm sử dụng ba hồ sơ liên kết với nhau:

1. một kho dự án riêng tư do Classroom50 tạo để lưu danh tính, đề xuất, mã nguồn,
   báo cáo, slide và các bản khai;
2. một commit đề xuất chính xác trong kho đó; và
3. một issue chính thức trong kho chủ đề của đúng học phần để lưu tóm tắt mà lớp
   có thể xem, trạng thái kiểm tra trùng, cập nhật, lịch và URL commit cuối.

Đề xuất là bắt buộc nhưng không có điểm. Công cụ tự kiểm tra cục bộ không cho
điểm và không chứng nhận tính khả thi, đúng đắn hay chất lượng. Điểm cuối được
chấm thủ công theo [`Rubrics.md`](Rubrics.md).

### 2. Ghi lại lịch

| Mốc | Thời gian (ICT, UTC+7) |
|---|---|
| Công bố tài liệu dự án | 2026-09-04 13:00 |
| Mở nhận bài trên Classroom50 | 2026-09-11 13:00 |
| Mốc khuyến nghị hoàn thành lập nhóm | 2026-09-13 23:59 |
| Hạn commit đề xuất và issue chính thức | 2026-09-20 23:59 |
| Hoàn thành kiểm tra trùng chính xác | 2026-09-25 |
| Hạn sửa khi trùng chính xác bài toán | 2026-09-27 23:59 |
| Hạn commit cuối và bình luận `FINAL SUBMISSION` | 2026-11-04 23:59 |
| Bắt đầu trình bày | 2026-11-06 |

Hạn cuối chung áp dụng cho mọi nhóm và không thay đổi theo thứ tự trình bày, lần
cập nhật đề xuất hoặc việc đổi bài toán cụ thể.

### 3. Lập nhóm và chọn vai trò

Trước khi nhận bài:

1. thống nhất một đến năm thành viên thuộc cùng học phần;
2. kiểm tra tên GitHub của từng thành viên;
3. chọn đúng một thành viên đại diện;
4. thống nhất rằng người này nhận bài lần đầu và mặc định quản lý issue chủ đề;
5. xem các chủ đề đã có trong kho chủ đề của đúng học phần.

Chỉ người đại diện nhận bài. Các thành viên khác không nhận riêng vì mỗi lần nhận
có thể tạo một kho khác.

Người đại diện chỉ thực hiện vai trò hành chính. Người này không được tự ý quyết
định hoặc thay đổi nhóm, bài toán, phạm vi, đề xuất hay commit nộp thay cả nhóm.
Mọi thành viên được liệt kê phải đồng ý với các quyết định đó.

### 4. Nhận bài và khởi tạo kho trống

#### Thao tác trên Classroom50

1. Mở liên kết nhận dự án của học phần.
2. Đăng nhập Classroom50 bằng GitHub.
3. Mở tổ chức VNU-HUS có nhãn **Student**.
4. Mở `final-project` và chọn **Accept**.
5. Theo liên kết tới kho GitHub riêng tư vừa tạo.

#### Lựa chọn CLI

```bash
gh student accept VNU-HUS <classroom> final-project
```

Chỉ dùng một cách nhận bài.

Kho vừa nhận được cố ý để trống. Sao chép starter công khai đã kiểm tra, đổi remote
ban đầu thành `starter`, rồi thêm kho bài tập trống thành `origin`:

```bash
git clone https://github.com/VNU-HUS/introai-final-project-template.git final-project
cd final-project

git remote rename origin starter
git remote add origin <CLASSROOM50_ASSIGNMENT_REPOSITORY_URL>

git remote -v
git ls-remote --heads origin
git push -u origin HEAD:main
```

Trước lần push đầu, kiểm tra:

```text
starter -> VNU-HUS/introai-final-project-template
origin  -> kho Classroom50 riêng tư và trống của đúng nhóm
```

`git ls-remote --heads origin` không được có nhánh bất ngờ. Không push vào
`starter`, không dùng kho nguồn chuẩn làm `origin`, và không dùng lại kho của học
phần khác.

### 5. Thêm thành viên và ghi danh tính riêng tư

Trong Classroom50, mở bài đã nhận, dùng biểu tượng bút chì, chọn **Manage
collaborators**, rồi thêm từ không đến bốn thành viên còn lại. Nhóm một người
không thêm ai.

Lựa chọn CLI cho một thành viên:

```bash
gh student invite VNU-HUS/<assignment-repository> <github-username>
```

Kho trống không có `.classroom50.yaml`, vì vậy lời mời bằng CLI hoặc trực tiếp
trên GitHub có thể không thực thi giới hạn số lượng. Nhóm và giảng viên phải so
sánh collaborator thực tế với `team.json`; tổng số phải từ một đến năm, kể cả
người đại diện.

Điền `team.json` riêng tư với:

- `MAT1206E` hoặc `MAT3508`;
- tên nhóm;
- tên GitHub của người đại diện; và
- một đến năm đối tượng thành viên, mỗi đối tượng có họ tên chính thức, mã sinh
  viên và tên GitHub.

Ghi cùng bộ ba danh tính trong README riêng tư và báo cáo cuối. Issue mà lớp có
thể xem chỉ dùng tên GitHub.

### 6. Xem ví dụ hoàn chỉnh

Cả nhóm mở [`examples/topic-proposal/README.md`](examples/topic-proposal/README.md)
trước khi sửa tệp thật. Ví dụ liên kết tới:

- hồ sơ thành viên riêng tư đã điền;
- đề xuất đầy đủ mọi trường bắt buộc; và
- issue tương ứng mà lớp có thể xem.

Mọi danh tính, mã, kho, commit và kết quả trong ví dụ đều hư cấu. Ví dụ không
phải là sự chấp thuận trước, chủ đề được giữ chỗ, đề xuất chắc chắn đạt, chuẩn
chất lượng tối thiểu hoặc văn bản được phép nộp nguyên xi.

Sinh viên sửa `team.json` và `proposal/proposal.md` thật ở gốc kho; các tệp ví dụ
được giữ nguyên làm tài liệu tham khảo.

### 7. Chuẩn bị đề xuất riêng tư

Sửa:

```text
team.json
proposal/proposal.md
```

Đề xuất phải nêu:

- tên dự án và nguồn chủ đề;
- tóm tắt công khai trong lớp;
- một bài toán cụ thể;
- bài toán và động lực;
- phạm vi do nhóm xác định, mục tiêu không cam kết và tính khả thi;
- phương pháp dự kiến;
- dữ liệu, công cụ, bài báo, phần mềm và dự án có sẵn;
- đầu ra hoặc phần minh họa dự kiến;
- các mốc thực hiện;
- tài liệu đã thực sự tham khảo; và
- các vấn đề liên quan đến liêm chính, riêng tư, an toàn và giấy phép.

`Mini-Project Ideas.md` chỉ là nguồn gợi ý. Tệp này không quy định dự án tối thiểu
và không thay trách nhiệm của nhóm trong việc chọn bài toán rõ ràng, khả thi.

Hoàn thành danh sách tự kiểm tra cuối `proposal/proposal.md`. Commit đề xuất phải
là đúng phiên bản mà mọi thành viên đã thống nhất.

### 8. Tự kiểm tra, tạo commit và xác định phiên bản

Chạy kiểm tra cấu trúc tùy chọn:

```bash
python3 check_project_files.py proposal
```

Lệnh kiểm tra schema, trường bắt buộc, chỗ giữ nội dung và tệp điều khiển chấm tự
động bị cấm. Lệnh không kết nối GitHub, không chạy mã dự án, không đánh giá chủ
đề và không cho điểm.

Sau khi mọi thành viên xem lại:

```bash
git status
git add team.json proposal/proposal.md README.md
git diff --cached
git commit -m "Submit topic proposal"
git push
git rev-parse HEAD
```

Sao chép URL commit cố định hoặc SHA đủ 40 ký tự. URL nhánh, URL tệp không gắn
commit, ảnh chụp hoặc liên kết tới nhánh mới nhất không xác định phiên bản bất
biến.

### 9. Tìm hoặc mở issue chính thức

Trước khi tạo issue, tìm trong kho chủ đề của đúng học phần theo:

1. URL chính xác của kho Classroom50 của nhóm; và
2. tên GitHub của người đại diện.

Nếu đã có issue hợp lệ cho kho đó, đây là issue chính thức. Tiếp tục tại đó và
không tạo issue khác.

Nếu chưa có, sau khi mọi thành viên đồng ý với commit đề xuất, người đại diện với
vai trò quản lý issue mặc định:

1. chọn **Issues -> New issue -> Project topic proposal**;
2. dùng tiêu đề `[Proposal] <tên nhóm> — <tên dự án>`;
3. điền mọi trường bắt buộc;
4. chỉ liệt kê tên GitHub;
5. dán URL kho nhóm và URL hoặc SHA commit đề xuất chính xác;
6. gửi issue.

Issue hợp lệ được tạo sớm nhất theo thời gian GitHub cho đúng URL kho nhóm trở
thành issue chính thức. Issue hợp lệ phải ở đúng kho học phần, có đủ trường, nêu
đúng kho dự án và liên kết commit đề xuất thuộc kho đó. Tính hợp lệ được xác định
khi giảng viên lần đầu xử lý các issue cạnh tranh. Sau khi issue chính thức đã
được ghi nhận, lựa chọn đó được giữ ổn định; một issue cũ nhưng thiếu thông tin
không thể thay thế issue đã chọn chỉ vì được sửa hoàn chỉnh về sau.

Nếu sau đó có issue trùng cho cùng kho, ngừng dùng issue mới. Giảng viên bình
luận:

```text
Duplicate of #<canonical-issue-number>

Continue all proposal updates, scheduling, and final submission in the original issue.
```

Issue mới được đóng. Issue trùng không giống trường hợp hai nhóm khác nhau chọn
trùng chính xác một bài toán.

### 10. Hiểu trạng thái kiểm tra trùng chính xác

Issue chính thức chỉ dùng:

```text
status: submitted
status: recorded
status: duplicate-problem
```

- `status: submitted`: bài toán đang chờ so sánh với các bài toán đã ghi nhận.
- `status: recorded`: tại thời điểm kiểm tra không tìm thấy bài toán trùng chính
  xác trước đó. Trạng thái này không chứng nhận phạm vi, tính khả thi, phương
  pháp, độ đúng hoặc kết quả dự kiến.
- `status: duplicate-problem`: một kho nhóm khác đã ghi nhận cùng bài toán chính
  xác. Nhóm phải sửa bài toán trong đề xuất và issue hiện có.

Cùng lĩnh vực rộng, phương pháp, họ dữ liệu hoặc miền ứng dụng chưa đủ để coi là
trùng chính xác. Khi hai nhóm chọn đúng cùng bài toán, issue đầy đủ được tạo sớm
hơn thường được giữ. Nhóm còn lại đăng đề xuất sửa trước 23:59 ngày 2026-09-27
trong cùng issue.

### 11. Cập nhật đề xuất

Đề xuất là kế hoạch có thể thay đổi. Nhóm có thể đổi phạm vi, phương pháp, dữ
liệu, công cụ, cách triển khai, đầu ra hoặc mức độ tham vọng. Báo cáo cuối phải
giải thích thay đổi quan trọng.

Tạo commit cho mỗi lần sửa và bình luận trong issue chính thức:

```text
PROPOSAL UPDATE

Previous proposal commit:
<old commit URL or SHA>

New proposal commit:
<new commit URL or SHA>

Selected problem changed: yes/no

Summary of changes:
- ...

Reason for the changes:
- ...
```

Khi bài toán cụ thể thay đổi, giảng viên tạm đặt lại `status: submitted` và chỉ
lặp lại kiểm tra trùng chính xác. Các thay đổi khác không cần trạng thái mới. Mọi
cập nhật đều không gia hạn hạn cuối chung.

### 12. Thay đổi thành viên hoặc người quản lý issue

Thay đổi thành viên là ngoại lệ hành chính. Sửa `team.json`, tạo commit và đăng
trong issue chính thức:

```text
MEMBERSHIP CHANGE REQUEST

Current members:
- ...

Proposed members:
- ...

Reason:
- ...

Commit updating team.json:
<commit URL or SHA>
```

Thay đổi chỉ có hiệu lực sau xác nhận rõ ràng của giảng viên. Mọi thành viên vẫn
phải cùng học phần và tổng số vẫn từ một đến năm.

Nếu người đại diện không thể tiếp tục quản lý issue, nhóm ghi một lần bàn giao
trong chính issue đó, không mở issue khác:

```text
ISSUE CUSTODIAN HANDOVER

Previous custodian: @...
New custodian: @...
All listed members agree: yes
Reason: ...
```

Bàn giao không thay đổi người đã nhận bài ban đầu và không trao quyền tự quyết dự
án cho bất kỳ thành viên nào.

### 13. Phát triển dự án

Dùng Git và GitHub thông thường:

```bash
git switch -c <short-purpose-branch>
git add <paths>
git commit -m "Describe the project change"
git push -u origin <short-purpose-branch>
```

Nên dùng pull request và đánh giá chéo trong nhóm nhiều người. Số commit, số pull
request và số dòng thay đổi chỉ là minh chứng, không phải công thức điểm.

Duy trì trong suốt dự án:

```text
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

Không commit khóa bí mật, dữ liệu cá nhân không cần thiết, tài liệu phân phối trái
phép hoặc phụ thuộc lớn không được giải thích. Ghi rõ nguồn bên ngoài, giấy phép,
điều kiện truy cập, tiền xử lý và giới hạn tái tạo.

### 14. Chuẩn bị kho và báo cáo cuối

Commit cuối phải có:

```text
README.md
team.json
proposal/proposal.md
report/report.pdf
slides/slides.pdf
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

README riêng tư và báo cáo phải nêu họ tên chính thức, mã sinh viên và tên GitHub
của từng thành viên. Xóa các dòng giữ chỗ không dùng. Báo cáo phải có mục **Thay
đổi so với đề xuất đã nộp**, mô tả thay đổi quan trọng hoặc ghi rõ không có thay
đổi.

Biên dịch mẫu báo cáo đã chọn thành `report/report.pdf`. Đặt slide cuối tại
`slides/slides.pdf`.

Chạy:

```bash
python3 check_project_files.py final
```

Đây vẫn là kiểm tra cấu trúc không có điểm. Vượt qua kiểm tra không đồng nghĩa với
điểm số hoặc đánh giá chất lượng.

### 15. Ghi nhận phiên bản nộp cuối và trình bày

Sau khi mọi thành viên đồng ý với đúng commit cuối:

```bash
git status
git push
git rev-parse HEAD
```

Đăng trong issue chính thức trước 23:59 ngày 2026-11-04:

```text
FINAL SUBMISSION

Final commit:
<permanent commit URL or complete SHA>

Report:
report/report.pdf at the final commit

Slides:
slides/slides.pdf at the final commit

All listed members agree to this submitted version: yes
```

Không tạo issue mới và không dùng cơ chế chấm hay kích hoạt nộp của Classroom50.
Bình luận trong issue và commit Git chính xác xác định phiên bản nộp.

Bắt đầu trình bày từ ngày 2026-11-06. Báo cáo và Slide có phần điểm chung; phần
trình bày miệng/quản lý thời gian và hỏi đáp được chấm riêng theo rubric.

### 16. Xử lý sự cố an toàn

- **Nhiều sinh viên đã nhận bài riêng:** ngừng dùng các kho trùng và liên hệ giảng
  viên trước khi xóa hoặc chuyển công việc. Không tự gộp danh tính hoặc lịch sử.
- **Sai remote:** không push. Kiểm tra `git remote -v` và chỉ sửa sau khi xác định
  đúng kho riêng tư của nhóm.
- **Đã có issue chính thức:** tiếp tục trong issue đó, không mở issue khác.
- **Có `status: duplicate-problem`:** sửa bài toán cụ thể và đề xuất, rồi cập nhật
  cùng issue trước hạn sửa.
- **Thay đổi thành viên:** dùng `MEMBERSHIP CHANGE REQUEST`, không âm thầm sửa
  danh sách.
- **Người đại diện vắng:** ghi bàn giao quản lý trong cùng issue.
- **Tệp quá lớn không phù hợp với Git:** lưu hợp pháp ở nơi khác và ghi nguồn,
  giấy phép, cách lấy, tiền xử lý và tái tạo.
- **Đã commit bí mật:** thu hồi bí mật ngay, báo giảng viên khi cần và dùng quy
  trình làm sạch lịch sử phù hợp. Một commit xóa sau đó không xóa bí mật khỏi
  lịch sử cũ.
