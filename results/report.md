# Telugu TokEval Report — 997 sents

Generated: 2026-08-23T23:18:37.704543

**Parity ratio = Telugu fertility / English fertility. 1.0 = perfect fairness. Lower te_fert better.**

## All tokenizers sorted by parity (best first)

| Rank | Name | Vocab | TE fert | EN fert | Parity | TE compression | Digit pieces |
|---|---|---|---|---|---|---|---|
| 1 | Saiteja__telugu-bpe | 50000 | 1.64 | 1.28 | 1.28 | 4.68 |  |
| 2 | sarvamai__sarvam-30b | 262144 | 2.48 | 1.19 | 2.08 | 3.09 |  |
| 3 | tiktoken_cl100k | 100000 | 13.57 | 1.14 | 11.90 | 0.56 |  |

## Key Findings (TokEval lens)

- **Best parity:** `Saiteja__telugu-bpe` parity 1.28 (TE 1.64 vs EN 1.28)
- **Worst parity:** `tiktoken_cl100k` parity 11.90
- **tiktoken gap:** Best Telugu model saves 87.9% tokens vs tiktoken cl100k on Telugu (TE fert 13.57 -> 1.64) = 8.3x longer effective context for free.

## Recommendation for phone model

Pick lowest parity + lowest TE fertility with vocab <=32K (fits 1.7B embedding table: 32K*2048*2bytes=128MB). 16K Unigram norm is often sweet spot for 1B phone (64MB embedding).

## Next steps

- Add Tamil/Kannada corpora to make Dravidian cluster real (now simulated).
- Expand to 100K wiki lines for stable 32K training (now 997 lines, vocab capped to 8K — note in logs).
- Run TokEval's digit/UTF-8 checks via https://github.com/cimeister/tokenizer-intrinsic-evals for full suite.
