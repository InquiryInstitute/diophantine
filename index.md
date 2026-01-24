---
layout: default
title: "One Constraint to Bind Them"
subtitle: "A Diophantine Lens on a Combinatorial Artifact"
math: true
---

# One Constraint to Bind Them

**A Diophantine Lens on a Combinatorial Artifact**

*By Daniel McShan, in voce Diophantus*  
*Inquiry.Institute*

---

## About This Project

This research package explores a real-world combinatorics problem through the lens of Diophantine constraints, featuring:

- **Essay**: A publishable 2,500+ word essay in Diophantus voice
- **Colab Notebook**: Reproducible experiments with enumeration, heatmaps, and geometry analysis
- **Formal Specification**: YAML constraint definition
- **Reviewer Packets**: Detailed reviews from Gauss, Hilbert, and Tufte

## Problem Statement

Count nonnegative integer solutions to:

$$x_1 + x_2 + \cdots + x_n = u \quad \text{(total allocation)}$$

$$x_1 + 2x_2 + 3x_3 + \cdots + nx_n = v \quad \text{(weighted capacity)}$$

**Multiplicity**: 

$$M(u,v) = \#\{\mathbf{x} \in \mathbb{Z}_{\ge 0}^n : \text{constraints satisfied}\}$$

<div class="quick-links">

## Quick Navigation

- [📄 Read the Essay]({{ site.baseurl }}/essay)
- [📓 Open Colab Notebook](https://colab.research.google.com/github/InquiryInstitute/diophantine/blob/main/diophantine_exploration.ipynb) - Interactive notebook
- [📊 View Results & Data]({{ site.baseurl }}/results/) - Generated data and figures
- [🤖 Automated Analysis]({{ site.baseurl }}/analysis) - LLM-powered results analysis
- [📋 Constraint Specification]({{ site.baseurl }}/constraint.yaml)
- [👥 Reviewer Feedback]({{ site.baseurl }}/reviewers/)

</div>

## Key Results

### Feasibility Region
Solutions exist only when:

$$u \le v \le n \cdot u$$

### Multiplicity Patterns
- For fixed $u$, $M(u,v)$ is unimodal with peak near $v \approx \frac{n+1}{2} \cdot u$
- Growth rate: $M(u,v) \sim O(u^{n-2})$ for typical $v$ values  
- Congruence patterns reveal hidden structure

## Repository Structure

```
diophantine/
├── essay.md                          # Main essay
├── diophantine_exploration.ipynb     # Google Colab notebook
├── constraint.yaml                   # Formal specification
├── reviewers/                        # Reviewer packets
│   ├── gauss_review.md
│   ├── hilbert_review.md
│   └── tufte_review.md
├── results/                          # Generated data
│   ├── multiplicity_samples.csv
│   ├── summary.json
│   └── llm_analysis.md
└── figures/                          # Generated visualizations
    ├── heatmap_log.png
    ├── heatmap_linear.png
    ├── slices_fixed_u.png
    └── growth_rate.png
```

## Direct Links

- **📓 [Open in Google Colab](https://colab.research.google.com/github/InquiryInstitute/diophantine/blob/main/diophantine_exploration.ipynb)** - Run the notebook interactively
- **📊 [View Results & Figures]({{ site.baseurl }}/results/)** - Browse generated data files and visualizations
- **🖼️ [View Figures on GitHub](https://github.com/InquiryInstitute/diophantine/tree/main/figures)** - Browse generated visualizations
- **📓 [Notebook Source](https://github.com/InquiryInstitute/diophantine/blob/main/diophantine_exploration.ipynb)** - View raw notebook file

## Three Perspectives

### 1. Combinatorial Property
Each solution vector $\mathbf{x}$ represents a unique allocation pattern. The mapping from objects to solutions is bijective.

### 2. Geometry of Solutions
Solutions form a lattice polytope—integer points in an $(n-2)$-dimensional affine space.

### 3. Multiplicity Heatmaps
Visualizing $M(u,v)$ reveals feasibility boundaries, peak structures, and phase transitions.

---

*"One constraint. Three perspectives. Infinite structure."*
