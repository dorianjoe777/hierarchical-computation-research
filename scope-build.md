# Building the scope document

The entry point is `scope-hierarchical-computation-v1.tex`. It is self-contained: no external images, bibliography processor, or private transcript is needed. References are clickable links in the document.

## Tectonic

This edition was built with Tectonic 0.17.0. From the repository root:

```sh
mkdir -p output/pdf
tectonic --outdir output/pdf scope-hierarchical-computation-v1.tex
```

Tectonic retrieves required TeX packages on its first run and reruns LaTeX as needed to resolve the table of contents, equation references, and page count. Use an installed Tectonic executable; the compiler itself is not included in this repository.

## Other TeX installations

The source uses the `article` class and standard packages listed in its preamble. It is intended to work with a full TeX Live installation or Overleaf using pdfLaTeX. An alternative local command is:

```sh
mkdir -p output/pdf
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=output/pdf scope-hierarchical-computation-v1.tex
```

The verified build for this edition uses Tectonic; the alternative engines have not been tested here.

## Edition and evidence

The LaTeX edition follows the founding Markdown plan and adds two labeled appendices: notation/evidence clarifications and potential connections to P versus NP. The original provenance JSON identifies the founding Markdown and private transcript; it is not a hash of the LaTeX or PDF. `scope-provenance.json` records the publication files for this edition.

Compilation and visual review check document structure, mathematics rendering, links, and layout. They do not verify the research hypotheses, simulate the proposed models, or independently audit an external theorem. The SAT summary benchmark is proposed future work.

For subsequent revisions, compile, inspect warnings and all rendered pages, update the publication hashes, and commit the source and PDF together. Preserve existing release tags.
