# Build Report — Gottipati Jamadagni, Unnanu — jama@unnanu.com
Generated: 2026-08-23 23:37 IST
All artifacts built and verified.

## Artifacts
- paper/paper.pdf (36 KB) — tectonic compiled, PDF 1.5, 1 page main paper
- paper/proofs.pdf (11 KB, 3 pages) — ReportLab proofs with tables
- paper/paper.tex (3.9 KB) — Overleaf-ready, self-contained (no .bbl needed)
- paper/draft.md (8.8 KB) — full 8-section markdown
- paper/arxiv_metadata.txt — copy-paste for arXiv form
- paper/arxiv_submission.zip (55 KB) — arXiv upload (tex + pdf + proofs + csv + md)
- paper/overleaf_bundle.zip (37 KB) — just tex + pdf for Overleaf
- paper/full_bundle_gottipati_telugu_tokeval.zip (3.7 MB) — everything incl 8 tokenizers (570KB-1.21MB each)

## Verification
- Tectonic build: OK (36.2 KiB), fonts downloaded, no errors
- Proofs: 3 pages, hyperlinks to mailto:jama@unnanu.com, tables rendered
- Metrics: results/metrics_large.csv 11 rows, sorted by TE fertility 1.55 best
- Tokenizers: 8 models, vocab 16K/32K, sizes verified via ls -lh
- Corpus: 80K Telugu wiki 36 MB + 20K English, flores 997

## Proofs Summary
Each claim cross-checked:
1. tiktoken 13.57 parity 11.9 — CSV + log
2. 1.55 8.8x over tiktoken, 37% over Sarvam, 5% over Saiteja — CSV math
3. Unigram morphology split — direct sp.EncodeAsPieces
4. 64 MB vs 2.1 GB — vocab*2048*2
5. Joint parity 1.34 — joint corpus 60K lines
6. Digit failure 2-3 pieces — sp test

