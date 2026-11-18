# AetherFlow FYP Report

LaTeX source, figures, and compiled PDF for the AetherFlow FYP-I Deliverable III report.

## Files

- `main.tex`: main document, front matter, and Chapters 1–6.
- `chapters_7_to_10.tex`: Chapters 7–9 (Implementation and Test Cases, Experimental Results and Discussion, and Conclusion). The filename is retained for compatibility; the report chapters are numbered sequentially.
- `FastFyp.cls`: university report document class.
- `fypbib.bib`: bibliography database.
- `Figures/`: diagrams, screenshots, logos, and other report assets.
- `main.pdf`: compiled report snapshot.
- `evidence/preliminary-experiments/`: saved API observations, an evidence index, and the original reproduction script supporting Chapter 8.
- `evidence/prototype-observations/` and `evidence/formal-test-run/`: retained historical records from earlier report revisions. The current report omits the formal test-case and test-metric sections.
- `chapters/`: retained earlier chapter source files. The current main document does not import these files; edit `main.tex` and `chapters_7_to_10.tex` for the active report.
- `.vscode/settings.json`: LaTeX Workshop build configuration.

The current prototype is [AetherFlow](https://aether-flow-gamma.vercel.app/). Preliminary API observations describe recorded prototype behavior; they do not establish measured model accuracy, cost savings, or end-to-end privacy.

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
