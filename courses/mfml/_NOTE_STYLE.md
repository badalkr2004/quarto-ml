# Note writing style (MFML)

## Hard rules
1. Math: only `$...$` inline and `$$...$$` display. Never `\(...\)` or `\[...\]` (breaks on Quarto/Pandoc).
2. Beginner-first: define every new term in plain English before symbols.
3. If a prerequisite idea is needed (e.g. inverse image, expectation), add a short **Before this clicks** box.
4. Always include: Video link, Learning goals, Main ideas, Worked mini-example, Common confusions, References, Self-check.
5. Keep UTF-8; prefer ASCII arrows as `$\to$` inside math; avoid exotic Windows-unsafe punctuation in paths.

## Front matter template
```yaml
---
title: "Lecture N — Title"
subtitle: "one-line plain English"
sidebar: mfml
toc: true
---
```

## References to reuse
- Course playlist: https://www.youtube.com/playlist?list=PLgMDNELGJ1Cay-Q9Cn8KcpUcC58NDWuiu
- NPTEL: https://nptel.ac.in/courses/106108841
- Blitzstein & Hwang, *Introduction to Probability* (free) — basics
- Cover & Thomas, *Elements of Information Theory* — entropy/KL
- Bishop, *Pattern Recognition and Machine Learning* — classical ML
- Murphy, *Probabilistic Machine Learning* — modern probabilistic view
- Goodfellow et al., *Deep Learning* — NN/CNN/RNN/GAN
- Hastie, Tibshirani, Friedman, *Elements of Statistical Learning* — trees/boosting
