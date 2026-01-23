# GitHub Actions Setup

This repository includes automated analysis workflows that:

1. **Run the Colab notebook** programmatically
2. **Generate results and figures**
3. **Use an LLM to analyze** the results and provide insights

## Workflows

### `analysis.yml` - Run Analysis and LLM Review

This workflow:
- Executes `diophantine_exploration.ipynb` using `run_analysis.py`
- Generates results in `results/` and figures in `figures/`
- Runs LLM analysis using `analyze_results.py`
- Commits results back to the repository
- Uploads artifacts for the Pages workflow

**Triggers:**
- Push to `main` branch
- Manual workflow dispatch
- Daily at 2 AM UTC (scheduled)

### `pages.yml` - Deploy GitHub Pages

This workflow:
- Downloads analysis results from the analysis workflow
- Builds the Jekyll site
- Deploys to GitHub Pages

**Triggers:**
- Push to `main` branch
- Manual workflow dispatch
- After analysis workflow completes

## Setup

### 1. Enable LLM Analysis (Optional)

To enable full LLM analysis with OpenRouter (recommended):

1. Go to repository **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Name: `OPENROUTER_API_KEY`
4. Value: Your OpenRouter API key
5. Click **Add secret**
6. (Optional) Add `OPENROUTER_MODEL` secret (defaults to `openai/gpt-4o`)

Alternatively, you can use `OPENAI_API_KEY` for direct OpenAI access.

**Note:** If no API key is set, the analysis will use a mock/fallback analysis that still provides useful insights.

### 2. Enable GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Under "Source", select **GitHub Actions**
3. The site will deploy automatically

## How It Works

```
┌─────────────────┐
│  Push to main   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  analysis.yml   │
│  - Run notebook │
│  - Generate     │
│    results      │
│  - LLM analysis │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  pages.yml      │
│  - Download     │
│    results      │
│  - Build Jekyll │
│  - Deploy       │
└─────────────────┘
```

## Files

- `run_analysis.py` - Executes the Jupyter notebook
- `analyze_results.py` - Runs LLM analysis on results
- `requirements.txt` - Python dependencies
- `.github/workflows/analysis.yml` - Analysis workflow
- `.github/workflows/pages.yml` - Pages deployment workflow

## Viewing Results

- **Analysis page**: https://inquiryinstitute.github.io/diophantine/analysis/
- **Actions logs**: https://github.com/InquiryInstitute/diophantine/actions
- **Results directory**: `results/llm_analysis.md` (committed after each run)

## Troubleshooting

### Analysis fails to run

- Check Python dependencies in `requirements.txt`
- Verify notebook syntax is correct
- Check Actions logs for specific errors

### LLM analysis not working

- Verify `OPENROUTER_API_KEY` (or `OPENAI_API_KEY`) secret is set correctly
- Check API key has sufficient credits
- Verify model name is correct (if using custom `OPENROUTER_MODEL`)
- Fallback analysis will run if API is unavailable

### Results not appearing on site

- Ensure `results/llm_analysis.md` is committed
- Check Jekyll build logs
- Verify file is in `results/` directory (not excluded)

## Manual Trigger

You can manually trigger the analysis workflow:

1. Go to **Actions** tab
2. Select **Run Analysis and LLM Review**
3. Click **Run workflow**
4. Select branch (usually `main`)
5. Click **Run workflow**

The analysis will run and results will be committed automatically.
