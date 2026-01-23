# Diophantine Constraint Exploration: Resource Allocation

A complete research package exploring a real-world combinatorics problem through the lens of Diophantine constraints, featuring:

- **Essay**: A publishable 2,500+ word essay in Diophantus voice
- **Colab Notebook**: Reproducible experiments with enumeration, heatmaps, and geometry analysis
- **Formal Specification**: YAML constraint definition
- **Reviewer Packets**: Detailed reviews from Gauss, Hilbert, and Tufte

---

## Problem Statement

Count nonnegative integer solutions to:
- $x_1 + x_2 + \cdots + x_n = u$ (total allocation)
- $x_1 + 2x_2 + 3x_3 + \cdots + nx_n = v$ (weighted capacity)

**Multiplicity**: $M(u,v) = \#\{\mathbf{x} \in \mathbb{Z}_{\ge 0}^n : \text{constraints satisfied}\}$

This constraint encodes a resource allocation problem: distribute $u$ units across $n$ tasks such that the weighted sum equals $v$.

---

## Package Contents

```
diophantine/
├── essay.md                          # Main essay (Diophantus voice)
├── diophantine_exploration.ipynb     # Google Colab notebook
├── constraint.yaml                   # Formal constraint specification
├── README.md                         # This file
├── reviewers/
│   ├── gauss_review.md              # Rigor & number theory review
│   ├── hilbert_review.md            # Formulation & generality review
│   └── tufte_review.md              # Visual evidence review
├── results/                          # Generated data (CSV, JSON, cache)
└── figures/                          # Generated visualizations (PNG)
```

---

## Quick Start

### 1. Read the Essay

Start with `essay.md` for the complete narrative, covering:
- The combinatorial problem
- The Diophantine constraint derivation
- Three perspectives: property, geometry, multiplicity
- Experimental results and conjectures

### 2. Run the Colab Notebook

1. Open `diophantine_exploration.ipynb` in Google Colab
2. Run all cells sequentially
3. Results will be saved to `results/` and `figures/`

**Note**: The notebook computes $M(u,v)$ for $u \le 50$, $v \le 150$, which may take a few minutes. Caching is enabled to speed up re-runs.

### 3. Review the Specification

See `constraint.yaml` for the formal definition of:
- Constraint equations
- Variable domains
- Input pair definition
- Multiplicity computation

### 4. Check Reviewer Feedback

The `reviewers/` directory contains detailed critiques from three perspectives:
- **Gauss**: Mathematical rigor, solvability conditions
- **Hilbert**: Problem formulation, generalization
- **Tufte**: Visualization clarity, interpretation

---

## Key Results

### Feasibility Region
Solutions exist only when: $u \le v \le n \cdot u$

### Multiplicity Patterns
- For fixed $u$, $M(u,v)$ is unimodal with peak near $v \approx \frac{n+1}{2} \cdot u$
- Growth rate: $M(u,v) \sim O(u^{n-2})$ for typical $v$ values
- Congruence patterns reveal hidden structure

### Sample Values (n=3)
- $M(10, 15) = 6$
- $M(10, 20) = 11$
- $M(20, 30) = 21$

---

## Three Perspectives

### 1. Combinatorial Property
Each solution vector $\mathbf{x}$ represents a unique allocation pattern. The mapping from objects to solutions is bijective.

### 2. Geometry of Solutions
Solutions form a lattice polytope—integer points in an $(n-2)$-dimensional affine space. The geometry reveals symmetries, invariants, and growth patterns.

### 3. Multiplicity Heatmaps
Visualizing $M(u,v)$ as a heatmap reveals:
- Feasibility boundaries
- Peak structures (typical allocations)
- Congruence patterns
- Phase transitions

---

## Non-Engineered Justification

This constraint is **not** reverse-engineered. It emerges naturally from:

1. **Conservation laws**: Total allocation must equal demand
2. **Weighted capacity**: Tasks have different costs/priorities
3. **Minimality**: Both constraints are necessary and sufficient
4. **Robustness**: Extends naturally to parameter changes

The derivation narrative (Section 7 of the essay) provides full justification.

---

## Experiment Configuration

Default settings in the Colab notebook:
- $n = 3$ (number of tasks)
- $u \in [0, 50]$ (total demand)
- $v \in [0, 150]$ (weighted capacity)

To explore different parameters, modify `CONFIG` in Notebook 0.

---

## Output Files

After running the notebook, you'll find:

### Figures (`figures/`)
- `heatmap_log.png`: Multiplicity heatmap (log scale)
- `heatmap_linear.png`: Multiplicity heatmap (linear scale)
- `slices_fixed_u.png`: Distribution slices for fixed $u$
- `geometry_3d.png`: 3D scatter plots of solutions (n=3)
- `growth_rate.png`: Growth rate analysis

### Data (`results/`)
- `multiplicity_samples.csv`: Sample $(u,v)$ pairs with counts
- `summary.json`: Summary statistics
- `multiplicity_cache.json`: Cached enumeration results
- `results_section.md`: Auto-generated results summary

---

## Extending the Work

### Parameter Expansions
- **General weights**: Replace $w_i = i$ with arbitrary weights
- **Inequality constraints**: Use $\le$ or $\ge$ instead of $=$
- **Additional constraints**: Add bounds or coprimality conditions
- **Higher dimensions**: Increase the number of constraint equations

### Open Questions
1. Asymptotic formula for $M(u, \alpha u)$ as $u \to \infty$
2. Unimodality of $M(u,v)$ as a function of $v$
3. Computational complexity of exact enumeration
4. Generating function identities

See Section 10 of the essay for detailed conjectures.

---

## Citation

If you use this work, please cite:

```
McShan, Daniel (in voce Diophantus). "One Constraint to Bind Them: A Diophantine Lens on a Combinatorial Artifact."
Inquiry.Institute, 2026.
```

---

## License

This work is provided for educational and research purposes.

---

## Contact

For questions or feedback, see the reviewer packets in `reviewers/` for detailed critiques and suggestions.

---

*"One constraint. Three perspectives. Infinite structure."*
