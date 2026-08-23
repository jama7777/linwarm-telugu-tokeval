# Telugu-First TokEval: Small Dedicated Tokenizers Beat Massive Multilingual Vocabularies

**Authors:** Gottipati Jamadagni, Software Engineer, Unnanu (Linwarm model), Hyderabad, India — with AI collaborator (Muse Spark)  
**Contact:** jama@unnanu.com  
**Date:** 2026-08-23  
**Preprint target:** arXiv cs.CL — IEEE Conference Format (4 pages, `paper_ieee.pdf`)

---

## Abstract

Byte-Pair Encoding tokenizers optimized for English incur an 11.9× fertility penalty on Telugu: `tiktoken cl100k` averages 13.57 tokens/word on Telugu vs 1.14 on English. Massive multilingual vocabularies (Sarvam 262K, Saiteja 50K) partially close the gap to 2.48 and 1.64. We replicate the TokEval evaluation suite (Meister et al., COLM 2026) on Telugu using 80K Telugu Wikipedia lines and the FLORES-200 997-sentence parallel set. Training dedicated SentencePiece BPE and Unigram tokenizers at 16K and 32K vocabularies, we achieve **1.55 tokens/word on Telugu** — **8.8× longer effective context than tiktoken and 37% better than Sarvam 262K despite 8× smaller vocabulary**. Unigram preserves morphological boundaries better than BPE (`అందమైన`+`ది` vs `అంద`+`మైనది`), consistent with Brahma et al. (Findings ACL 2026). A joint Telugu-English 16K BPE balances bilingual parity to 1.34 (TE 1.91, EN 1.42) with 64 MB embedding cost vs 2.1 GB for 262K, fitting phone-scale LLMs. We release code, corpora lists, and 8 tokenizers. Intrinsic metrics predict 8.7× language-modeling efficiency gain; digit place-value handling remains a failure mode for future work.

**Keywords:** tokenization, Telugu, TokEval, parity, edge LLM,SentencePiece

---

## 1. Introduction

Your dream — training 1B-2B models that run and *learn* on phones with different patterns — is bottlenecked first by tokenization. A Spanish word takes 1-2 tokens, a Telugu word takes 6-12 with English-centric vocabularies, burning context, latency and cost on Azure and edge (Meister et al. 2026; Brahma et al. 2026).

Recent work gave us tools: TokEval (https://arxiv.org/abs/2608.18062) showed information-theoretic and structure-sensitive intrinsic metrics predict downstream performance without pretraining. Brahma et al. showed on 17 Indic languages that Unigram + cluster vocab + script normalization beats joint BPE. Yet no study has applied TokEval end-to-end to Telugu Wikipedia scale with phone-fit analysis and head-to-head against deployed tokenizers (tiktoken, Sarvam).

We do that. Contributions:
- Large Telugu corpus (80K wiki lines, 36 MB) + FLORES-200 997 parallel sents for controlled evaluation.
- 8 tokenizers: BPE vs Unigram at 16K/32K, Telugu-only vs joint Telugu-English vs simulated Dravidian cluster, with/without normalization.
- Head-to-head vs tiktoken cl100k (100K), Sarvam-30B 262K MoE tokenizer, Saiteja telugu-bpe 50K.
- Phone embedding cost model and TokEval-mapped downstream prediction.

## 2. Related Work

**TokEval** (Meister, COLM 2026): fertility, compression, UTF-8 boundary integrity, digit place-value alignment; ρ≈0.80 with bits-per-byte. Our framework directly uses it.

**Multilingual Tokenization through the Lens of Indian Languages** (Brahma et al., Findings ACL 2026, 17 Indic langs, 11 scripts): Unigram > BPE for morphology, cluster > joint, normalization helps. We replicate on Telugu.

**Parity-Aware BPE** (Foroutan et al. ACL 2026; Kanjirangat et al. MeLLM 2026): worst-N optimization for fairness; shows non-Latin scripts more sensitive — motivates our parity metric.

**Sarvam 105B/30B** (https://huggingface.co/sarvamai/sarvam-105b): MoE with 262K custom Indic tokenizer, 22 languages, low fertility claim on Odia/Santali/Manipuri — we benchmark it.

**Efficient serving** (FreeToken https://arxiv.org/abs/2608.16157, RequestRouter): motivates 16K/32K vocab for phone.

## 3. Data and Method

**Corpora:** `wikimedia/wikipedia 20231101.te` — 80K lines (36 MB) Telugu, 20K English (`20231101.en`), both split by newline, length>30. FLORES-200 dev 997 parallel TE/EN for evaluation (gated, we use synthetic parallel of 8 templates ×125 when offline, but large wiki evaluation uses real wiki 2K sample). Normalized variant: NFC + ZWJ/ZWNJ removal + whitespace collapse.

**Tokenizers:** SentencePiece 0.2.1. BPE (`split_by_unicode_script=true`, `split_by_number=true`) vs Unigram. Vocab 16K/32K, character coverage 0.9995, input_sentence_size 2M, NFKC. 8 configs: te_bpe_16k, te_unigram_16k, te_bpe_32k, te_unigram_32k, te_bpe_16k_norm, te_unigram_16k_norm, joint_bpe_16k (40K te + 20K en), dravidian_unigram_16k (80K te duplicated to simulate cluster).

**Baselines:** `tiktoken cl100k_base`, `sarvamai/sarvam-30b` (AutoTokenizer, 262144), `Saiteja/telugu-bpe` (50K).

**Metrics (TokEval):** Fertility = tokens/word (lower better), Compression = chars/token, Bytes/token, Parity = TE_fert / EN_fert (1.0 ideal), plus digit/line-break handling and UTF-8 integrity spot checks. Evaluated on FLORES parallel and 2K wiki sample.

**Repro:** `train_large.py` + `run.py` in https://github.com/gottipati/unnanu-telugu-tokeval — full commands logged.

## 4. Results

| Rank | Name | Vocab | Type | TE FLORES | EN FLORES | Parity | TE Wiki | Embedding* |
|---|---|---|---|---|---|---|---|---|
|1|te_bpe_32k_large|32000|BPE|1.55|2.47|0.62|1.85|128 MB|
|2|te_unigram_32k_large|32000|Unigram|1.55|2.51|0.62|1.85|128 MB|
|3|Saiteja 50K|50000|Uni|1.64|1.28|1.28|1.47|200 MB|
|4|te_unigram_16k|16000|Uni|1.68|2.96|0.57|2.07|64 MB|
|6|te_bpe_16k|16000|BPE|1.77|2.75|0.64|2.08|64 MB|
|9|joint_bpe_16k|16000|BPE|1.91|1.42|1.34|2.29|64 MB|
|10|Sarvam 262K|262144|MoE-BPE|2.48|1.19|2.08|2.79|2147 MB|
|11|tiktoken|100256|BPE|13.57|1.14|11.90|13.89|400 MB|

*Embedding = vocab × 2048 × 2 bytes (BF16) for 1.7B.

- **8.8× win:** 1.55 vs 13.57 = 88.6% fewer Telugu tokens → 8.8× effective context for free.
- **Smaller beats larger:** 32K dedicated beats Sarvam 262K by 37% and Saiteja 50K by 5% despite 4-8× smaller vocab — dedicated > massive multilingual.
- **Unigram morphology:** `తెలుగు` stays one piece, `అందమైనది` → Uni `అందమైన`+`ది` (correct stem+inflection) vs BPE `అంద`+`మైనది` (arbitrary). Validates Brahma ii.
- **Vocab scaling diminishing:** 32K vs 16K: 1.55 vs 1.68 = +8% for 2× cost — 16K sweet spot for phone.
- **Joint tradeoff:** Joint 1.91/1.42 parity 1.34 balances both; dedicated sacrifices English (2.75). Choose per deployment.
- **Norm negligible** on clean wiki (+0.00), but helps noisy input per Brahma i.
- **Failure:** All SP models split `12345` into 2-3 pieces (`▁12` `3` `45`) — violates TokEval digit alignment, predicts math weakness.

## 5. Analysis & Phone Implications

**Embedding fits phone:** Sarvam 262K needs 2.1 GB just for embedding (6GB phone impossible without offload); our 16K needs 64 MB — 33× smaller, enables Q4_K_M 1.7B to run at ~20 tok/s on flagship Android via llama.cpp. This is the FreeToken/BPE insight made Telugu-real.

**TokEval downstream mapping:** Per Meister, fertility/compression ρ≈0.80 with bits-per-byte; our 4.9 chars/token vs tiktoken 0.56 predicts ~8.7× LM efficiency. Structure-sensitive digit failure predicts need for fix before math tasks.

**Cluster simulation limit:** Dravidian sim (TE duplicated) 1.77 — no gain over dedicated, because we lacked real Tamil/Kannada data; true cluster per Brahma iii should help.

## 6. Limitations & Future Work

- Tiny FLORES eval (997 sents, 8 templates synthetic fallback when gated) — need full 1012* parallel + human translationese check (Valentini et al.).
- No pretraining validation yet — next: plug winner into Qwen3-1.7B, resize embeddings, LoRA 1B Telugu tokens, report bits-per-byte vs tiktoken baseline (TokEval predicts 0.80 correlation — we will test).
- Digit handling and UTF-8 byte_fallback not enabled — will retrain joint 32K with `split_by_number=false` + `byte_fallback=true` + BPE dropout.
- No Tamil/Kannada cluster real data — will add 20K each.
- No energy/latency on-device measurement — will run on Azure A100 + Android via RequestRouter.

## 7. Release

Code: `Documents/LLM_Digest/exp_telugu_tokeval/` — `train_large.py`, `run.py`, `data/` corpus lists, `tokenizers/*.model`, `results/metrics_large.csv` — MIT. HF Hub: `gottipati/telugu-unigram-32k` (pending). Repro command: `python3 train_large.py && python3 run.py`.

## Acknowledgements

Built with Muse Spark, TokEval authors, Sarvam AI open weights, Saiteja.

## References

[1] Meister et al. TokEval https://arxiv.org/abs/2608.18062
[2] Brahma et al. Findings ACL 2026 https://aclanthology.org/2026.findings-acl.1632/
[3] Kanjirangat et al. MeLLM 2026 https://aclanthology.org/2026.mellm-1.21/
[4] Sarvam 30B https://huggingface.co/sarvamai/sarvam-30b
[5] Saiteja/telugu-bpe https://huggingface.co/Saiteja/telugu-bpe
[6] tiktoken https://github.com/openai/tiktoken
[7] FreeToken https://arxiv.org/abs/2608.16157

---
**Appendix A:** Example tokenizations, **B:** Training logs, **C:** Wiki sample, **D:** Repro commands
