# Final-project submission guide / Hướng dẫn nộp dự án cuối kỳ

[English](#english) | [Tiếng Việt](#tiếng-việt)

The browser path is shown first. The CLI commands are equivalent or provide the
required fallback when Classroom50 has no browser action. Classroom50 creates
and displays assignments; GitHub hosts repositories, Issues, Pull Requests,
Codespaces, and commits; Git records file history.

Screenshots are added only after pilot verification. Until then, use the exact
button labels and text paths below. See the
[screenshot checklist](docs/images/classroom50/README.md).

## English

## 1. Purpose and authoritative rules

- One founder accepts one Classroom50 group assignment.
- The group contains one to five students from the same course.
- The same private repository is used for proposal, development, report, slides,
  and final submission.
- The proposal is required but ungraded.
- The final project has no autograder, automatic score, Feedback PR, scored
  Release, or `gh student submit` step.
- An exact Git commit URL plus the GitHub issue or comment timestamp identifies
  each submitted milestone.
- The final score is assigned manually using the published 5+3 rubric. Slides
  is a shared group score; Oral presentation and Q&A are individual scores.
- When multiple teachers grade, each teacher provides one complete score out of
  100 for each student, and the final score is the arithmetic mean of those
  complete scores. No rubric component or subtotal is averaged separately.

## 2. Calendar

| Milestone | Date and time (ICT, UTC+7) |
|---|---|
| Project materials released | 2026-09-04 13:00 |
| Classroom50 acceptance opens | 2026-09-11 13:00 |
| Recommended group-formation target | 2026-09-13 23:59 |
| Initial proposal issue due | 2026-09-20 23:59 |
| Exact-duplicate correction due | 2026-09-27 23:59 |
| Final commit and issue comment due | 2026-11-04 23:59 |
| Presentations begin | 2026-11-06 |

The final deadline is common to every group and does not depend on presentation
order.

## 3. Before accepting the assignment

1. Agree on the final group membership and one founder.
2. Confirm that every member belongs to the same course.
3. Review existing proposals on the class topic-board Issues page.
4. Decide which single student will accept.

> **Only the founder accepts.** Other members must not accept separately, because
> that may create duplicate project repositories.

## 4. Accept and bootstrap the empty repository

### Classroom50 graphical path

1. Open the final-project assignment link supplied for the course.
2. Choose **Sign in with GitHub** at <https://classroom50.org>.
3. Open the VNU-HUS organization marked **Student**.
4. Open `final-project` and choose **Accept**.
5. Follow the repository link displayed after acceptance.

### CLI alternative

```bash
gh student accept VNU-HUS <classroom> final-project
```

Use one acceptance route, not both.

The Classroom50 repository is intentionally empty. It has no template files or
autograding configuration. The founder copies the reviewed public starter into
the accepted repository.

### Graphical development environment

On the accepted GitHub repository, choose **Code → Codespaces**. A terminal is
still needed for the initial remote setup below.

### Reproducible terminal bootstrap

```bash
git clone https://github.com/VNU-HUS/introai-final-project-template.git final-project
cd final-project

git remote rename origin starter
git remote add origin <CLASSROOM50_ASSIGNMENT_REPOSITORY_URL>

git remote -v
git push -u origin HEAD:main
```

Before pushing, verify that:

```text
starter → VNU-HUS/introai-final-project-template
origin  → the group's private Classroom50 repository
```

After this push, the other members open or clone the Classroom50 repository.

## 5. Record and verify the group

### Classroom50 graphical path

1. Open the accepted assignment.
2. Use the edit pencil near the top-right.
3. Choose **Manage collaborators**.
4. Add the other enrolled GitHub usernames. A one-person group adds nobody.

### CLI alternative

```bash
gh student invite \
  VNU-HUS/<assignment-repository> \
  <github-username>
```

Complete `team.json` with:

- `MAT1206E` or `MAT3508`;
- the group name;
- the founder's GitHub username;
- one to five distinct GitHub usernames.

Compare `team.json` with the collaborators shown by Classroom50 or GitHub. Do
not place student IDs, email addresses, phone numbers, credentials, or private
keys in the class-visible topic issue.

## 6. Prepare the initial proposal

### GitHub graphical path

Open the repository and choose **Code → Codespaces**, or use the GitHub web
editor, to edit:

```text
team.json
proposal/proposal.md
```

Students choose and justify their own scope. `Mini-Project Ideas.md` is only an
optional catalogue; it does not prescribe a minimum project.

### Optional structural self-check

```bash
python3 check_project_files.py proposal
```

This command produces no score, does not judge correctness, and does not approve
the topic.

### Commit the proposal

```bash
git add team.json proposal/proposal.md
git commit -m "Submit topic proposal"
git push
git rev-parse HEAD
```

Copy the complete 40-character SHA or permanent GitHub commit URL.

## 7. Open the one class-visible topic issue

### GitHub graphical path

1. Open the topic-board repository for the correct course.
2. Choose **Issues → New issue → Project topic proposal**.
3. Use the title:

   ```text
   [Proposal] <group name> — <project title>
   ```

4. Complete the Issue Form and paste the exact proposal commit URL.
5. Submit the issue.

### CLI alternative

The graphical Issue Form is preferred because it enforces the required fields.
When a tested Markdown fallback form is supplied, `gh issue create` may be used
with that exact body template.

The issue body is a class-visible summary and discussion record. The linked
private commit is the authoritative full proposal. Use one issue for the entire
project; do not open a second proposal issue for a revision.

## 8. Read and respond to proposal review

Staff use these labels:

```text
status: pending
status: revision-required
status: approved
status: rejected
```

Silence is not approval. Approval exists only when an instructor comment names
the approved commit SHA.

When revision is required:

1. edit the same proposal file;
2. create and push a new commit;
3. comment on the same issue with the new commit URL.

Beginning substantial implementation before approval is at the group's risk.

## 9. Update an approved proposal

Minor implementation refinements normally require no formal update, such as:

- changing a library or programming language;
- adjusting parameters or internal implementation details;
- improving visualizations;
- adding experiments;
- adjusting internal milestones.

Material changes require instructor approval, including changes to the main
problem, domain, principal dataset, principal method, expected output,
substantial scope, important privacy/licensing/safety assumptions, or group
membership.

For a material change:

```bash
git add proposal/proposal.md team.json
git commit -m "Update project proposal"
git push
git rev-parse HEAD
```

Comment on the existing topic issue:

```text
PROPOSAL UPDATE REQUEST

Previous approved commit:
<old commit URL or SHA>

Proposed new commit:
<new commit URL or SHA>

Summary of changes:
- ...

Reason for the changes:
- ...
```

When membership changes, list the usernames to add or remove. Staff apply
`status: update-pending`. The previous approved commit remains authoritative
until the instructor posts:

```text
APPROVED UPDATE

This proposal supersedes:
<old commit SHA>

Approved proposal commit:
<new commit SHA>
```

There is no separate topic-change cutoff. When the selected problem changes,
the group updates the same proposal issue immediately. A topic change does not
extend the common final deadline.

## 10. Develop the project

Recommended graphical workflow:

```text
GitHub Issue
→ feature branch
→ commit and push
→ Pull Request
→ review
→ merge
```

Equivalent terminal work may use ordinary `git` and `gh` commands. Commit count,
Pull Request count, lines changed, and GitHub activity volume do not directly
produce points.

Maintain during development:

```text
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

Do not commit passwords, tokens, private keys, private personal data, pirated
datasets, or unnecessary large binaries. Document external data, models,
services, licenses, access instructions, preprocessing, and reproduction limits
in `docs/EXTERNAL_RESOURCES.md`.

## 11. Prepare the final repository

The final repository contains at least:

```text
README.md
team.json
proposal/proposal.md
report/report.pdf
slides/slides.pdf
project/README.md and project materials
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

The root README links to the report, slides, project materials, and declarations.
The final report contains **Changes from the approved proposal**. When no
material change occurred, state that explicitly.

Check every link and reproduction instruction before the final commit.

## 12. Submit the final snapshot

### Optional structural self-check

```bash
python3 check_project_files.py final
```

This produces no score and does not evaluate project quality.

### Create the final commit

```bash
git add .
git commit -m "Submit final project"
git push
git rev-parse HEAD
```

### GitHub graphical path to the permanent commit URL

Open the repository, choose **Commits**, open the `Submit final project` commit,
and copy its permanent URL.

Comment on the existing topic issue no later than 2026-11-04 23:59 ICT:

```text
FINAL SUBMISSION

Commit:
<complete commit URL or 40-character SHA>
```

Do not force-push away, delete, or otherwise make the submitted commit
unreachable before grading is complete.

### Important Classroom50 limitation

Because `final-project` is empty and non-autograded, Classroom50 has no meaningful
project **View grade** workflow and no browser **Submit** button. The exact GitHub
commit URL posted in the topic issue is the submission record.

## 13. After the deadline

- Later pushes do not replace the submitted SHA.
- An exceptionally accepted replacement requires an instructor comment naming
  the replacement SHA.
- Late work, extensions, acceptance, rejection, and penalties are manual
  instructor decisions.
- The instructor grades the exact linked commit from the repository snapshot.

## 14. Troubleshooting and recovery

### Duplicate repositories or wrong founder

Stop work and contact the instructor. Do not open additional repositories or
issues while trying to repair the mistake independently.

### Invitation or access failure

Verify the GitHub username, enrollment in the correct organization/classroom,
and the **Manage collaborators** list. The founder may retry the tested CLI
invite command.

### Incorrect `origin`

Run:

```bash
git remote -v
```

Do not push until `origin` is the group's private Classroom50 repository.

### Secret committed accidentally

Revoke or rotate the credential immediately, then contact the instructor. Merely
deleting the visible line does not invalidate a leaked secret.

### Oversized file

Remove the unnecessary binary from the pending commit. Store a lawful,
accessible resource externally and document it in `EXTERNAL_RESOURCES.md`.

### Sixth collaborator or cross-course member

The project group is invalid until staff resolve it. Do not assume that a name
in `team.json` overrides the actual collaborator list.

### Issue in the wrong course board or wrong SHA

Comment with the correction and notify staff. Do not erase the history unless
staff explicitly instructs you to do so.

### Pending or rejected proposal near a milestone

Respond in the existing issue and submit the required revision. Silence or an
unlabelled issue is not approval.

## 15. What is and is not assessed

See [`Rubrics.md`](Rubrics.md).

```text
Proposal:      required, ungraded
Report:        60 points, five shared group components
Presentation:  40 points = shared Slides 12 + individual Oral 12 + individual Q&A 16
Teacher score: one complete total out of 100 for each student
Final score:   average of complete teacher totals when multiple teachers grade
```

Repository presence alone is not correctness. The optional self-check, issue
labels, commit count, lines changed, and GitHub activity do not directly produce
points. The instructor manually reviews the exact submitted repository, report,
slides, presentation or demonstration, Q&A, and demonstrated understanding.

---

## Tiếng Việt

## 1. Mục đích và quy tắc chính thức

- Một thành viên đại diện nhận một bài tập nhóm trên Classroom50.
- Nhóm có từ một đến năm sinh viên thuộc cùng một học phần.
- Cùng một kho riêng tư được dùng cho đề xuất, phát triển, báo cáo, slide và nộp
  cuối kỳ.
- Đề xuất là bắt buộc nhưng không có điểm riêng.
- Dự án không có chấm tự động, điểm tự động, Feedback PR, scored Release hoặc
  bước `gh student submit`.
- Liên kết commit Git chính xác cùng thời gian của issue hoặc bình luận xác định
  phiên bản đã nộp.
- Điểm được chấm thủ công theo thang 5+3 đã công bố. Điểm Slide là điểm
  chung của nhóm; điểm Trình bày miệng và Hỏi đáp là điểm cá nhân.
- Khi có nhiều giảng viên chấm, mỗi giảng viên cho một tổng điểm đầy đủ trên 100
  đối với từng sinh viên; điểm cuối cùng là trung bình cộng của các tổng điểm
  đầy đủ đó. Không tính trung bình riêng cho thành phần hoặc tổng phần nào.

## 2. Lịch

| Mốc | Thời gian (ICT, UTC+7) |
|---|---|
| Công bố tài liệu dự án | 2026-09-04 13:00 |
| Mở liên kết nhận bài Classroom50 | 2026-09-11 13:00 |
| Mốc khuyến nghị hoàn thành lập nhóm | 2026-09-13 23:59 |
| Hạn đăng đề xuất ban đầu | 2026-09-20 23:59 |
| Hạn sửa khi trùng chính xác bài toán | 2026-09-27 23:59 |
| Hạn commit cuối và bình luận nộp bài | 2026-11-04 23:59 |
| Bắt đầu trình bày | 2026-11-06 |

Hạn cuối giống nhau cho mọi nhóm và không phụ thuộc thứ tự trình bày.

## 3. Trước khi nhận bài

1. Thống nhất danh sách nhóm và một thành viên đại diện.
2. Xác nhận mọi thành viên thuộc cùng học phần.
3. Xem các đề xuất hiện có trong trang Issues của kho chủ đề lớp.
4. Chọn đúng một sinh viên thực hiện thao tác nhận bài.

> **Chỉ thành viên đại diện chọn Accept.** Các thành viên khác không nhận bài
> riêng, vì có thể tạo các kho trùng lặp.

## 4. Nhận bài và đưa mẫu vào kho trống

### Giao diện Classroom50

1. Mở liên kết bài tập dự án của học phần.
2. Chọn **Sign in with GitHub** tại <https://classroom50.org>.
3. Mở tổ chức VNU-HUS có nhãn **Student**.
4. Mở `final-project` và chọn **Accept**.
5. Theo liên kết tới kho được hiển thị sau khi nhận bài.

### Lựa chọn CLI

```bash
gh student accept VNU-HUS <classroom> final-project
```

Chỉ dùng một cách nhận bài.

Kho Classroom50 được tạo trống có chủ ý. Thành viên đại diện sao chép mẫu công
khai đã được kiểm tra vào kho đó.

### Môi trường phát triển đồ họa

Trong kho GitHub, chọn **Code → Codespaces**. Vẫn cần terminal để thiết lập
remote lần đầu.

### Các lệnh thiết lập có thể tái tạo

```bash
git clone https://github.com/VNU-HUS/introai-final-project-template.git final-project
cd final-project

git remote rename origin starter
git remote add origin <CLASSROOM50_ASSIGNMENT_REPOSITORY_URL>

git remote -v
git push -u origin HEAD:main
```

Trước khi push, kiểm tra:

```text
starter → VNU-HUS/introai-final-project-template
origin  → kho Classroom50 riêng tư của nhóm
```

Sau lần push đầu, các thành viên khác mở hoặc clone kho Classroom50.

## 5. Ghi và kiểm tra thành viên nhóm

### Giao diện Classroom50

1. Mở bài tập đã nhận.
2. Dùng biểu tượng bút chì ở phía trên bên phải.
3. Chọn **Manage collaborators**.
4. Thêm các tên GitHub còn lại. Nhóm một người không thêm ai.

### Lựa chọn CLI

```bash
gh student invite \
  VNU-HUS/<assignment-repository> \
  <github-username>
```

Điền `team.json` với mã học phần, tên nhóm, thành viên đại diện và từ một đến năm
tên GitHub khác nhau. So sánh với danh sách collaborator trên Classroom50 hoặc
GitHub. Không đưa mã sinh viên, email, số điện thoại hoặc thông tin bí mật vào
issue công khai trong lớp.

## 6. Chuẩn bị đề xuất ban đầu

### Giao diện GitHub

Chọn **Code → Codespaces** hoặc dùng trình sửa web để chỉnh:

```text
team.json
proposal/proposal.md
```

Sinh viên tự chọn và giải thích phạm vi. `Mini-Project Ideas.md` chỉ là danh sách
gợi ý, không quy định một dự án tối thiểu.

### Tự kiểm tra cấu trúc, không có điểm

```bash
python3 check_project_files.py proposal
```

Lệnh này không chấm đúng sai và không phê duyệt chủ đề.

### Tạo commit đề xuất

```bash
git add team.json proposal/proposal.md
git commit -m "Submit topic proposal"
git push
git rev-parse HEAD
```

Sao chép SHA đủ 40 ký tự hoặc liên kết commit cố định.

## 7. Mở issue chủ đề duy nhất của nhóm

### Giao diện GitHub

1. Mở kho chủ đề của đúng học phần.
2. Chọn **Issues → New issue → Project topic proposal**.
3. Dùng tiêu đề:

   ```text
   [Proposal] <tên nhóm> — <tên dự án>
   ```

4. Điền Issue Form và dán liên kết commit đề xuất.
5. Gửi issue.

Issue là bản tóm tắt và lịch sử trao đổi mà lớp có thể xem. Commit riêng tư được
liên kết là đề xuất đầy đủ chính thức. Mỗi nhóm chỉ dùng một issue trong suốt dự
án.

## 8. Đọc và phản hồi đánh giá đề xuất

Giảng viên dùng các nhãn:

```text
status: pending
status: revision-required
status: approved
status: rejected
```

Không có phản hồi không có nghĩa là đã phê duyệt. Chỉ bình luận của giảng viên
nêu đúng SHA mới xác lập phiên bản được phê duyệt.

Khi cần sửa, nhóm chỉnh cùng tệp đề xuất, tạo commit mới và bình luận trong cùng
issue bằng liên kết commit mới.

## 9. Cập nhật đề xuất đã được phê duyệt

Các điều chỉnh triển khai nhỏ thường không cần phê duyệt lại. Thay đổi quan trọng
về bài toán, miền ứng dụng, dữ liệu chính, phương pháp chính, đầu ra, phạm vi lớn,
giả định quan trọng hoặc thành viên nhóm cần được phê duyệt.

```bash
git add proposal/proposal.md team.json
git commit -m "Update project proposal"
git push
git rev-parse HEAD
```

Bình luận trong issue hiện có theo mẫu `PROPOSAL UPDATE REQUEST` ở phần tiếng
Anh. Khi thay đổi thành viên, nêu rõ tên cần thêm hoặc bỏ. Phiên bản cũ vẫn chính
thức cho đến khi có bình luận `APPROVED UPDATE` nêu SHA mới.

Không có hạn riêng cho việc đổi chủ đề. Khi bài toán đã chọn thay đổi, nhóm
phải cập nhật ngay trong cùng issue đề xuất. Việc đổi chủ đề không gia hạn hạn
nộp cuối chung.

## 10. Phát triển dự án

Quy trình đồ họa được khuyến nghị:

```text
GitHub Issue → nhánh → commit/push → Pull Request → review → merge
```

Số commit, Pull Request, dòng thay đổi hoặc mức hoạt động GitHub không trực tiếp
tạo điểm.

Duy trì các tệp:

```text
project/README.md
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

Không commit mật khẩu, token, khóa riêng, dữ liệu cá nhân riêng tư, dữ liệu vi
phạm bản quyền hoặc tệp nhị phân lớn không cần thiết.

## 11. Chuẩn bị kho cuối cùng

Kho cuối cùng có ít nhất:

```text
README.md
team.json
proposal/proposal.md
report/report.pdf
slides/slides.pdf
project/README.md và tài liệu dự án
docs/CONTRIBUTIONS.md
docs/AI_USAGE.md
docs/EXTERNAL_RESOURCES.md
```

Báo cáo phải có mục **Thay đổi so với đề xuất đã được phê duyệt**. Nếu không có
thay đổi quan trọng, ghi rõ điều đó.

## 12. Nộp phiên bản cuối

### Tự kiểm tra cấu trúc, không có điểm

```bash
python3 check_project_files.py final
```

### Tạo commit cuối

```bash
git add .
git commit -m "Submit final project"
git push
git rev-parse HEAD
```

### Sao chép liên kết commit bằng giao diện GitHub

Mở **Commits**, mở commit `Submit final project` và sao chép liên kết cố định.

Trước 2026-11-04 23:59 ICT, bình luận trong issue hiện có:

```text
FINAL SUBMISSION

Commit:
<liên kết commit đầy đủ hoặc SHA 40 ký tự>
```

Không force-push làm mất commit, xóa commit hoặc làm SHA đã nộp không còn truy
cập được trước khi chấm xong.

### Giới hạn của giao diện Classroom50

Vì `final-project` là bài tập kho trống và không chấm tự động, Classroom50 không
có **View grade** có ý nghĩa hoặc nút **Submit** trên trình duyệt. Liên kết commit
được đăng trong issue là bản ghi nộp bài.

## 13. Sau hạn nộp

- Push sau hạn không thay thế SHA đã nộp.
- SHA thay thế chỉ được chấp nhận khi giảng viên bình luận rõ.
- Nộp muộn, gia hạn và hình thức xử lý là quyết định thủ công của giảng viên.
- Giảng viên chấm đúng commit đã được liên kết trong bản chụp kho.

## 14. Xử lý lỗi

- **Kho trùng hoặc sai thành viên đại diện:** dừng và báo giảng viên; không tự
  tạo thêm kho hoặc issue.
- **Không mời được hoặc không truy cập được:** kiểm tra tên GitHub, lớp và
  **Manage collaborators**.
- **Sai `origin`:** chạy `git remote -v`; không push khi chưa đúng kho riêng tư.
- **Lộ thông tin bí mật:** thu hồi hoặc thay khóa ngay và báo giảng viên.
- **Tệp quá lớn:** bỏ khỏi commit, lưu ở nguồn hợp pháp và mô tả trong
  `EXTERNAL_RESOURCES.md`.
- **Thành viên thứ sáu hoặc khác học phần:** nhóm chưa hợp lệ cho đến khi được
  xử lý.
- **Sai kho chủ đề hoặc sai SHA:** bình luận sửa và báo giảng viên; không xóa
  lịch sử nếu chưa được yêu cầu.
- **Đề xuất còn pending hoặc bị từ chối:** phản hồi và sửa trong issue hiện có.

## 15. Nội dung được chấm và không được chấm

Xem [`Rubrics.md`](Rubrics.md).

```text
Đề xuất:       bắt buộc, không có điểm
Báo cáo:       60 điểm, năm thành phần chung của nhóm
Trình bày:     40 điểm = Slide chung 12 + Trình bày miệng cá nhân 12 + Hỏi đáp cá nhân 16
Điểm giảng viên: một tổng điểm đầy đủ trên 100 cho mỗi sinh viên
Điểm cuối:     trung bình cộng các tổng điểm đầy đủ khi có nhiều giảng viên chấm
```

Việc có đủ tệp không tự chứng minh tính đúng đắn. Tự kiểm tra, nhãn issue, số
commit, số dòng thay đổi và mức hoạt động GitHub không trực tiếp tạo điểm. Giảng
viên chấm thủ công kho và báo cáo đã nộp, slide, phần trình bày hoặc minh họa,
hỏi đáp và mức độ hiểu công việc.
