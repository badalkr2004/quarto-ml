# Learn ML — Quarto notes site

Extensible multi-course notes for machine learning / deep learning.

## Preview locally

```powershell
.\preview.ps1
```

## Publish (Posit Connect Cloud)

Free hosted static sites: [docs](https://quarto.org/docs/publishing/posit-connect-cloud.html)

1. Sign in at [connect.posit.cloud](https://connect.posit.cloud) (keep that browser session open)
2. From this folder run:

```powershell
.\publish.ps1
```

3. Press **Y** when asked to authorize, approve in the browser  
4. Your public URL is saved in `_publish.yml` after the first publish  

## Current course

- **MFML** — Mathematical Foundations of Machine Learning (Prof. Prathosh A.P.)
  - Notes + beginner notebook under `courses/mfml/`

## Add the next lecture series

See `docs/adding-a-course.qmd` or the in-site page after preview.

## Layout

```
courses/<series-id>/     # one folder per lecture series
templates/new-course/    # copy this when starting a new series
references/              # shared bibliography-style links
docs/                    # how to extend the site
_quarto.yml              # navbar + per-course sidebars
```
