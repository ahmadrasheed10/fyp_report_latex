# AetherFlow FYP Report

LaTeX source, figures, and compiled PDF for the AetherFlow FYP-I Deliverable III report.

## Files

- `main.tex`: main document, front matter, and Chapters 1–6.
- `chapters_7_to_10.tex`: Chapters 7, 9, and 10; Chapter 8 is intentionally omitted for this deliverable.
- `FastFyp.cls`: university report document class.
- `fypbib.bib`: bibliography database.
- `Figures/`: diagrams, screenshots, logos, and other report assets.
- `main.pdf`: compiled report snapshot.
- `evidence/prototype-observations/`: saved preliminary API observations and reproduction scripts.
- `evidence/formal-test-run/`: recorded API responses, assessment script, and the current report case-ID mapping in `report_case_results.json`. The report contains five Passed cases and three Not Executed mode cases; original execution records retain their original IDs.
- `chapters/`: retained earlier chapter source files. The current main document does not import these files; edit `main.tex` and `chapters_7_to_10.tex` for the active report.
- `.vscode/settings.json`: LaTeX Workshop build configuration.

## Build locally

Install a LaTeX distribution such as TeX Live or MiKTeX, including pdfLaTeX and BibTeX. Run these commands from the repository root:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The output is `main.pdf`. In VS Code with LaTeX Workshop installed, open `main.tex` and use the configured build recipe.

## Overleaf

Upload the repository files to an Overleaf project, select `main.tex` as the main document, and use pdfLaTeX.

## Working together

Pull the latest changes before editing. Use a separate branch for larger changes and review the compiled PDF before merging. Commit the updated `main.pdf` with report edits so teammates can view the current version without compiling.

Temporary LaTeX build files, local backups, and scratch files are excluded from version control.
