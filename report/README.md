# Report / Báo cáo

Choose one source template:

- [`main-en.tex`](main-en.tex) for English;
- [`main-vi.tex`](main-vi.tex) for Vietnamese.

### Graphical path

Open the group repository on GitHub and choose **Code → Codespaces**. Open the
selected `.tex` file, edit it, and use the integrated terminal or a LaTeX editor
to compile it.

### Terminal path

```bash
cd report
latexmk -pdf main-en.tex   # or main-vi.tex
cp main-en.pdf report.pdf  # or main-vi.pdf
```

The final required file is:

```text
report/report.pdf
```

The report must include a section titled **Changes from the approved proposal**
or **Thay đổi so với đề xuất đã được phê duyệt**. When no material change
occurred, state that explicitly.

Official names and student IDs, when included on the private report cover, must
not be copied into the class-visible topic issue.
