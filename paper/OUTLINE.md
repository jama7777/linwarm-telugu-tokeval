# Paper Outline — Telugu-First TokEval

**Target:** arXiv preprint now → COLM 2027 / ACL 2027 Findings (Indic/Dravidian track) + workshop MeLLM

## Title options
1. **Telugu-First TokEval: Small Dedicated Tokenizers Beat Massive Multilingual Vocabularies on Fertility and Parity (1.55 vs 13.57 on Telugu)**
2. Parity-Aware Tokenization for Phone-Scale LLMs: A Telugu Case Study with TokEval
3. 64MB vs 2.1GB: Efficient Telugu Tokenization for Edge LLMs

**Authors:** You + me (AI collaborator) — decide ordering. Affiliation: Hyderabad (independent / Azure?)

## Abstract (150 words)
We show Telugu fertility gap is still 11.9x with tiktoken cl100k. Dedicated 16K/32K Unigram/BPE trained on 80K Telugu wiki lines achieves 1.55 tokens/word — 8.8x longer effective context than tiktoken, 37% better than Sarvam 262K and 5% better than Saiteja 50K despite 5-16x smaller vocab. Unigram preserves morphology better (ते split). Joint bilingual 16K balances parity 1.34. All via TokEval intrinsic metrics without pretraining. Embedding cost 64MB (16K) fits phones vs 2.1GB for 262K. We release tokenizers + code.

## Contributions
- First TokEval replication on Telugu with large wiki (80K) vs flores 997
- Systematic BPE vs Unigram vs joint vs normalization at 16K/32K
- Baselines: tiktoken 100K, Sarvam 262K, Saiteja 50K
- Phone-fit analysis + digit boundary failure diagnosis

## Paper Structure (4-8 pages + appendix)
1. Intro: Telugu low-resource, phone LLM dream, tokenizer bottleneck
2. Related: TokEval (Meister COLM 2026), Brahma ACL 2026 Indic 17 langs, Parity-aware BPE (Foroutan), Sarvam tokenizer
3. Data: 80K te wiki + 20K en wiki, flores 997 parallel, norm
4. Method: SentencePiece BPE/Unigram, joint vs dedicated, evaluation: fertility, compression, bytes/token, parity, digit/UTF-8
5. Results: Table sorted by TE fertility (report_large.md), 8.8x, Unigram morphology, vocab scaling, joint tradeoff
6. Analysis: Embedding size vs phone RAM, TokEval prediction to downstream bits-per-byte, digit failure case
7. Limitations & Future: Need Tamil/Kannada cluster, byte_fallback, pretraining validation (bits-per-byte), human eval for translationese
8. Release: HF hub link, GitHub, reproduction

## Venue fit
- **arXiv cs.CL now** (no review, gets priority)
- **COLM 2027** (TokEval was COLM 2026, good fit) — deadline ~May 2027
- **ACL 2027 Findings / MeLLM workshop** — Indic focus, accepts 4-page
- **TinyML/Mobile AI workshop** — phone angle

## What we have vs need for camera-ready
Have: 80K corpus, 8 tokenizers, full metrics, repro scripts (run.py, train_large.py)
Need before journal submission (optional 1 week extra):
- Tamil/Kannada 20K each for true Dravidian cluster (vs sim)
- joint 32K + byte_fallback + split_by_number fix
- Tiny LM 350M bits-per-byte proxy (1B tokens) to validate TokEval correlation

But for arXiv preprint, current is already publishable as short paper / technical report.

## Citations to include (all verified)
- TokEval https://arxiv.org/abs/2608.18062
- Brahma et al. Findings ACL 2026 https://aclanthology.org/2026.findings-acl.1632/
- Parity-aware BPE Foroutan ACL 2026, Kanjirangat MeLLM 2026 https://aclanthology.org/2026.mellm-1.21/
- Sarvam 30B/105B https://huggingface.co/sarvamai/sarvam-105b
- Saiteja/telugu-bpe https://huggingface.co/Saiteja/telugu-bpe
- tiktoken https://github.com/openai/tiktoken

## Repro bundle
- /data corpus lists + HF wikimedia/wikipedia 20231101.te
- tokenizers/*.model + .vocab
- metrics_large.csv, report_large.md
- run.py, train_large.py
- LICENSE MIT
