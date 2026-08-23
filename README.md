# Linwarm: Telugu-First TokEval — 8.8x Context Win for Phone-Scale LLMs

**Author:** Gottipati Jamadagni — Software Engineer, **Unnanu** (Model: **Linwarm**) — Hyderabad — jama.gottipati7@gmail.com  
**With:** AI collaborator Muse Spark  
**Date:** 2026-08-23  
**Format:** IEEE Conference (4 pages + references) — `paper/paper_ieee.pdf`

> Small dedicated Telugu tokenizers (16K/32K, 64-128 MB) beat massive multilingual vocabularies (Sarvam 262K, 2.1 GB) and tiktoken 100K on Telugu fertility: **1.55 vs 13.57 (8.8x win)** — TokEval replication on 80K Wikipedia + FLORES-200.

## Results (sorted by Telugu FLORES fertility)

| Rank | Tokenizer | Vocab | TE | EN | Parity | TE wiki | Embed |
|---|---|---|---|---|---|---|---|
| 1 | **te_bpe_32k_large** | 32K | **1.55** | 2.47 | 0.62 | 1.85 | 128 MB |
| 2 | te_unigram_32k_large | 32K | 1.55 | 2.51 | 0.62 | 1.85 | 128 MB |
| 3 | Saiteja/telugu-bpe | 50K | 1.64 | 1.28 | 1.28 | 1.47 | 200 MB |
| 4 | te_unigram_16k_large | 16K | 1.68 | 2.96 | 0.57 | 2.07 | **64 MB** |
| 9 | joint_bpe_16k_large (bilingual) | 16K | 1.91 | 1.42 | **1.34** | 2.29 | 64 MB |
| 10 | Sarvam 262K | 262K | 2.48 | 1.19 | 2.08 | 2.79 | 2147 MB |
| 11 | tiktoken cl100k | 100K | 13.57 | 1.14 | 11.90 | 13.89 | 400 MB |

**Takeaway:** Dedicated 16K Unigram gives 64 MB embedding (fits phone) vs Sarvam 2.1 GB, 8% within 32K. Joint 16K best for Telugu+English.

## Repo
- `paper/draft.md` — full paper, `paper/paper.tex` — arXiv LaTeX (Overleaf-ready)
- `paper/arxiv_metadata.txt` — title/abstract for submission
- `train_large.py` — train 8 tokenizers on wikimedia/wikipedia 20231101.te (80K)
- `run.py` + `results/report_large.md` — TokEval metrics
- `data/corpus_te_wiki_full.txt` (36 MB), `tokenizers/*large.model`
- Weekly digest source: `../weekly_llm_digest_2026-08-23.md`

## Reproduce
```bash
pip install sentencepiece tiktoken transformers datasets --break-system-packages
python3 train_large.py   # trains 8 tokenizers, ~5 min on laptop
python3 run.py          # FLORES eval vs baselines
cat results/report_large.md
```

## Cite
```
@misc{jamadagni2026telugutokeval,
  title={Telugu-First TokEval: Small Dedicated Tokenizers Beat Massive Multilingual Vocabularies},
  author={Gottipati Jamadagni and Muse Spark},
  year={2026},
  howpublished={\\url{https://arxiv.org/abs/XXXX.XXXXX}},
  note={80K Wikipedia Telugu, TokEval replication}
}
```
References: TokEval https://arxiv.org/abs/2608.18062, Brahma et al. https://aclanthology.org/2026.findings-acl.1632/

## Next: Publish
See `paper/README_PUBLISH.md` — arXiv (cs.CL) now, then COLM/ACL.

## License
MIT — tokenizers CC BY 4.0
Contact: jama.gottipati7@gmail.com
