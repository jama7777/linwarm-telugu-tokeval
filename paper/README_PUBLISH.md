# Publish Checklist — Telugu TokEval

## Files ready
- Draft: `paper/draft.md` (full 8-section) + `paper/paper.tex` (arXiv style, needs pdflatex or overleaf)
- Outline: `paper/OUTLINE.md`
- Results: `results/report_large.md` + `results/metrics_large.csv`
- Code: `train_large.py`, `run.py`, `data/` lists, `tokenizers/*large.model`
- Weekly digest source: `weekly_llm_digest_2026-08-23.md`

## Step 1: arXiv now (15 mins)
1. Create https://arxiv.org account if needed. Choose `cs.CL` primary + `cs.LG`
2. Compile PDF: easiest = upload `paper.tex` to https://overleaf.com → Recompile → Download PDF (no local latex needed). Or install MacTeX: `brew install --cask mactex`
3. arXiv submission: Title = "Telugu-First TokEval: Small Dedicated Tokenizers Beat Massive Multilingual Vocabularies" — Abstract from draft.md — Add authors — Upload PDF + source (.tex + .bbl) — License CC BY 4.0
4. After announcement, add arXiv ID back to GitHub README.

## Step 2: Code + Model release (parallel, 30 mins)
```bash
# Create GitHub repo telugu-tokeval
git init
git add train_large.py run.py paper/ results/ README.md
git commit -m "init: telugu tokeval 1.55 fertility, 8.8x over tiktoken"
git push

# HF Hub upload (needs hf_token)
pip install huggingface_hub --break-system-packages
huggingface-cli login
python3 -c "from huggingface_hub import HfApi; api=HfApi(); api.create_repo('telugu-unigram-32k', exist_ok=True); api.upload_folder(folder_path='tokenizers', repo_id='YOUR_HF/telugu-unigram-32k', commit_message='add 32k tokenizers')"
```
Add MIT LICENSE, cite Sarvam/Saiteja.

## Step 3: Venue upgrade (optional, 1-2 weeks extra work)
- To strengthen for **COLM/ACL Findings**, add:
  - Joint 32K with `byte_fallback=true` + `split_by_number=false` (fix digits)
  - Real Dravidian cluster: add ta/kn wiki 20K each
  - Tiny LM proxy: 350M Qwen, 1B tokens, compare bits-per-byte (TokEval ρ test)
  - Human eval 50 Telugu sentences for translationese vs Sarvam
- Page limit 8 + appendix. Deadline COLM ~ May 2027, ACL ~ Feb 2027 — plenty time.

## Step 4: What to do now (we do together)
- [ ] You: Fill `[Your Name]` + email in `draft.md:1` and `paper.tex:8`
- [ ] You: Choose license + HF username
- [ ] Me: I will polish draft → finalize PDF on Overleaf, generate arXiv abstract file
- [ ] Me: Prepare GitHub README with table from `metrics_large.csv`

Say: "fill name X, push to arXiv" and I will generate final submission bundle (paper.pdf + source zip).

## Why this is publishable now
- Novelty: First large-wiki TokEval Telugu replication with phone-fit analysis; beats deployed SoTA despite 8x smaller vocab
- Rigor: 8 tokenizers, controlled parity metrics, public wiki data, repro scripts, baselines with URLs verified Aug 23
- Impact: Directly enables your dream — 1.7B phone LLM with 64MB embedding, 8.8x context win
- Limitations honestly stated — reviewers love that

Next command from you decides journal/venue and I prepare bundle.
