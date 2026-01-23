---
layout: page
title: "Automated Analysis"
permalink: /analysis/
math: true
---

# Automated Analysis Results

This page displays the results of automated analysis performed by GitHub Actions, including:

1. **Notebook Execution**: The Colab notebook is run programmatically to generate results and figures
2. **LLM Analysis**: An AI analyzes the generated data and visualizations to provide insights

---

{% include analysis.html %}

---

## How It Works

1. **GitHub Actions Workflow** (`.github/workflows/analysis.yml`) runs on every push to main
2. The workflow:
   - Executes the Jupyter notebook (`diophantine_exploration.ipynb`)
   - Generates results in `results/` and figures in `figures/`
   - Runs LLM analysis on the results using OpenAI API
   - Commits the results back to the repository
3. **Pages Deployment** automatically updates when new results are available

## Configuration

To enable LLM analysis, add your OpenAI API key as a GitHub secret:
- Go to Settings → Secrets and variables → Actions
- Add a new secret: `OPENAI_API_KEY`

If the API key is not set, the analysis will use a mock/fallback analysis.

---

[← Back to Home]({{ site.baseurl }}/)
