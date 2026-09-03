# Report / Báo cáo

Choose one source template:

- [`main-en.tex`](main-en.tex) for English;
- [`main-vi.tex`](main-vi.tex) for Vietnamese.

Open the private group repository in a local editor or GitHub Codespaces. Fill
every required identity and project field, delete unused member rows, and compile
the selected source:

```bash
cd report
latexmk -pdf -halt-on-error main-en.tex   # or main-vi.tex
cp main-en.pdf report.pdf                 # or main-vi.pdf
```

The required final file is:

```text
report/report.pdf
```

The private report must identify every member by official full name, student ID,
and GitHub username. Those official identity fields must not be copied into the
class-visible topic issue.

The report must include **Changes from the submitted proposal** or **Thay đổi so
với đề xuất đã nộp**. Describe every material change and its relevant proposal
commit, or state explicitly that no material change occurred.

Use only real sources actually consulted. Do not leave sample identities,
fabricated authors, titles, venues, URLs, DOI values, datasets, metrics, or
results in the final report.
