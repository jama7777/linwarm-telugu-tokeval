# Telugu TokEval — Large Corpus (80K wiki) Report

Corpus: 80K Telugu wiki lines (36 MB), 20K English wiki, 997 FLORES parallel sents for eval. Generated 2026-08-23T23:24:33.881142

**Fertility = tokens per word (lower better). Parity = TE/EN. 1.0 ideal. TE wiki = on natural wiki text (harder than FLORES).**

## Sorted by Telugu FLORES fertility (best first)

| Rank | Name | Vocab | Type | TE FLORES | EN FLORES | Parity | TE Wiki | Note |
|---|---|---|---|---|---|---|---|---|
| 1 | te_bpe_32k_large | 32000 | BPE | 1.55 | 2.47 | 0.62 | 1.85 | te_bpe_32k_large.model |
| 2 | te_unigram_32k_large | 32000 | Unigram | 1.55 | 2.51 | 0.62 | 1.85 | te_unigram_32k_large.model |
| 3 | saiteja_50k | 50000 | Unigram/BPE | 1.64 | 1.28 | 1.28 | 1.47 | Saiteja/telugu-bpe |
| 4 | te_unigram_16k_large | 16000 | Unigram | 1.68 | 2.96 | 0.57 | 2.07 | te_unigram_16k_large.model |
| 5 | te_unigram_16k_norm_large | 16000 | Unigram | 1.68 | 2.74 | 0.61 | 2.08 | te_unigram_16k_norm_large.model |
| 6 | dravidian_unigram_16k_large | 16000 | Unigram | 1.77 | 2.72 | 0.65 | 2.06 | dravidian_unigram_16k_large.model |
| 7 | te_bpe_16k_large | 16000 | BPE | 1.77 | 2.75 | 0.64 | 2.08 | te_bpe_16k_large.model |
| 8 | te_bpe_16k_norm_large | 16000 | BPE | 1.77 | 2.75 | 0.64 | 2.08 | te_bpe_16k_norm_large.model |
| 9 | joint_bpe_16k_large | 16000 | BPE | 1.91 | 1.42 | 1.34 | 2.29 | joint_bpe_16k_large.model |
| 10 | sarvam_262k | 262144 | Moe-BPE | 2.48 | 1.19 | 2.08 | 2.79 | sarvamai/sarvam-30b |
| 11 | tiktoken_cl100k | 100256 | BPE | 13.57 | 1.14 | 11.90 | 13.89 | OpenAI cl100k_base |

## Insights (TokEval lens)

- **Best TE:** `te_bpe_32k_large` TE 1.55 (vocab 32000) — 88.6% fewer tokens than tiktoken (13.57) = **8.8x longer context** on Telugu for free.
- **tiktoken disaster:** TE 13.57 vs EN 1.14 parity 11.9 — Telugu burns 11.9x tokens. Sarvam 262K improves to 2.48 (parity 2.08), Saiteja 50K to 1.64 (parity 1.28). Our dedicated 32K hits **1.55 parity 0.62** — beats both despite 8x smaller vocab.
- **Unigram vs BPE:** On 16K, Unigram TE 1.68 vs BPE 1.77 — Unigram wins, preserves morphology: `తెలుగు` stays `తెలుగు` vs BPE split, `అందమైనది` → U:`అందమైన`+`ది` vs B:`అంద`+`మైనది` (matches Brahma ACL 2026 finding ii).
- **Vocab scaling:** 32K TE 1.55 vs 16K 1.68 = +8% gain for 2x vocab (128MB vs 64MB embedding at 2048 dim). Diminishing returns — 16K is sweet spot for phone.
- **Joint vs Telugu-only:** Joint 16K (TE 1.91 EN 1.42 parity 1.34) balances bilinguality; Telugu-only 16K EN 2.75 (parity 0.64) sacrifices English. For Hyderabad bilingual assistant, joint wins; for Telugu-only ASR/NLP, dedicated wins.
- **Normalization:** No difference on wiki (TE 1.77 both) — NFC/ZWJ removal negligible on clean wiki, but will help noisy user input.
- **Digit boundary (TokEval):** All our SP models split `12345` into 2-3 pieces (e.g., `▁12` `3` `45`) — violates TokEval digit place-value integrity. Need `split_by_number=false` or digit-specific pre-tokenizer to keep `12345` as one piece for math reasoning — next iteration.

## Recommendation for phone 1.7B model

- **If Telugu-first (your dream phone model):** `te_unigram_32k_large` (TE 1.55) or `te_unigram_16k_large` (TE 1.68, 50% smaller embedding). Use Unigram — better morphology, matches Indic paper.
- **If bilingual Telugu+English:** `joint_bpe_16k_large` (TE 1.91 EN 1.42 parity 1.34) or increase to `joint 32K` (not yet trained) expected TE ~1.70.
- **Embedding cost:** 16K×2048×2B = 64 MB, 32K = 128 MB — both fit phone (6GB RAM) easily vs Sarvam 262K×4096×2B = 2.1 GB.

## TokEval mapping to downstream (per Clara Meister paper)

- Information-theoretic (fertility/compression) predicts bits-per-byte language modeling — our 1.55 fertility ≈ 4.9 chars/token vs tiktoken 0.56 = 8.7x better LM efficiency expected.
- Digit/line-break handling correlates with math/code — our current digit split predicts weakness on arithmetic — fix next.
- UTF-8 integrity: SP with `byte_fallback=false` may produce <unk> on rare emojis — enable `byte_fallback=true` for phone robustness.

## Next steps (we do together)

1. Fix digit pre-tokenizer and retrain joint 32K with byte_fallback
2. Build Dravidian cluster for real: add Tamil/Kannada wiki 20K each — expect TE benefit + better Tamil parity
3. Plug winner tokenizer into Qwen3-1.7B fine-tune: replace tokenizer, resize embeddings, LoRA-tune 1B Telugu tokens, measure bits-per-byte vs tiktoken baseline
4. Quantize to Q4_K_M and test on Android via llama.cpp — measure tokens/sec vs memory
