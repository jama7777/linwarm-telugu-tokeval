#!/usr/bin/env python3
import sentencepiece as spm
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"
TOK = ROOT / "tokenizers"
TOK.mkdir(exist_ok=True)

configs = [
    ("bpe", 16000, DATA/"corpus_te_wiki_full.txt", TOK/"te_bpe_16k_large"),
    ("unigram", 16000, DATA/"corpus_te_wiki_full.txt", TOK/"te_unigram_16k_large"),
    ("bpe", 32000, DATA/"corpus_te_wiki_full.txt", TOK/"te_bpe_32k_large"),
    ("unigram", 32000, DATA/"corpus_te_wiki_full.txt", TOK/"te_unigram_32k_large"),
    ("bpe", 16000, DATA/"corpus_te_wiki_norm.txt", TOK/"te_bpe_16k_norm_large"),
    ("unigram", 16000, DATA/"corpus_te_wiki_norm.txt", TOK/"te_unigram_16k_norm_large"),
    ("bpe", 16000, DATA/"corpus_joint_large.txt", TOK/"joint_bpe_16k_large"),
    ("unigram", 16000, DATA/"corpus_dravidian_large.txt", TOK/"dravidian_unigram_16k_large"),
]

for model_type, vocab, corpus, prefix in configs:
    model_file = Path(str(prefix)+".model")
    if model_file.exists():
        print(f"[skip] {prefix.name} exists")
        continue
    cmd = f"--input={corpus} --model_prefix={prefix} --vocab_size={vocab} --model_type={model_type} --character_coverage=0.9995 --input_sentence_size=2000000 --shuffle_input_sentence=true --normalization_rule_name=nmt_nfkc"
    if model_type=="bpe":
        cmd += " --split_by_unicode_script=true --split_by_number=true --allow_whitespace_only_pieces=true"
    print(f"\n[train] {prefix.name} type={model_type} vocab={vocab} corpus={corpus.name} ({corpus.stat().st_size/1e6:.1f} MB)")
    try:
        spm.SentencePieceTrainer.Train(cmd)
        print(f"  -> OK {model_file} ({model_file.stat().st_size/1e3:.0f} KB)")
    except Exception as e:
        print(f"  -> FAIL {e}")

print("\nDone. Listing:")
for p in sorted(TOK.glob("*large.model")):
    print(p, p.stat().st_size)
