# Review by Tufte: Visual Evidence & Interpretation

**Reviewer**: Edward Tufte  
**Focus**: Clarity of visualizations, interpretation discipline, data-ink ratio

---

## Required Fixes

1. **Heatmap Color Scales**: The notebook generates both log-scale and linear-scale heatmaps, but the essay doesn't specify which one to use or when. Log scales can hide important structure (like zeros), while linear scales can saturate.

   **Fix**: In the essay, specify which heatmap is primary and why. Recommend using a diverging colormap for the linear scale to highlight the peak structure. Add a note about the trade-offs.

2. **Axis Labels and Units**: The heatmaps have axes labeled "u" and "v" but don't include units or interpretation. A reader unfamiliar with the problem won't know what these represent.

   **Fix**: Add subtitle or annotation: "u = Total Demand (units)", "v = Weighted Capacity (weighted units)". Consider adding reference lines for $v = u$ and $v = n \cdot u$ (feasibility boundaries).

3. **Figure Captions**: The essay references figures but doesn't provide detailed captions. Each figure should stand alone and tell a story.

   **Fix**: Add comprehensive captions:
   - **Figure 1 (Heatmap)**: "Multiplicity $M(u,v)$ for $n=3$. White regions indicate zero solutions (infeasible). The peak ridge occurs near $v \approx 2u$ (the average weighted allocation)."
   - **Figure 2 (Slices)**: "Slices of $M(u,v)$ for fixed $u$ values, showing unimodal distribution with peak near $v = \frac{n+1}{2} \cdot u$."

4. **Data-Ink Ratio**: The 3D scatter plots for geometry may have too much "non-data ink" (grid lines, axes) relative to the actual solution points.

   **Fix**: Simplify the 3D plots: remove excessive grid lines, use subtle axes, focus on the point cloud. Consider 2D projections if 3D doesn't add insight.

---

## Optional Improvements

5. **Small Multiples**: Instead of separate figures for different $u$ values, use small multiples (Tufte's "small multiples" principle) to show how the distribution changes.

   **Suggestion**: Create a grid of slice plots, one for each $u \in \{5, 10, 15, \ldots, 50\}$, all with the same axes. This reveals the evolution of the distribution.

6. **Contour Lines**: Add contour lines to the heatmap to show level sets of constant multiplicity. This helps identify "ridges" and "valleys" in the landscape.

   **Suggestion**: Overlay contour lines on the heatmap, or create a separate contour plot.

7. **Comparison Visualizations**: The essay mentions "typical" vs "atypical" allocations but doesn't visualize this. What does a "typical" solution vector look like?

   **Suggestion**: For a high-multiplicity $(u,v)$ pair, plot a histogram of $x_1, x_2, x_3$ values across all solutions. This shows the "typical" allocation pattern.

8. **Growth Rate Visualization**: The growth rate plot is good, but it could show confidence intervals or error bars if we're fitting a polynomial.

   **Suggestion**: Add shaded regions for uncertainty, or show multiple fit orders (linear, quadratic, cubic) to assess which is most appropriate.

9. **Interactive Elements**: For a Colab notebook, consider adding interactive sliders to explore the heatmap dynamically.

   **Suggestion**: Use `ipywidgets` to create an interactive heatmap where users can adjust $n$ and see the structure change.

10. **Figure Placement**: The essay should reference figures near the relevant text, not all at the end.

    **Suggestion**: Integrate figures into the text flow. For example, place the heatmap right after Section 6 (Multiplicity Heatmaps), not in an appendix.

---

## Strengths

- The notebook generates a comprehensive set of visualizations.
- The heatmap effectively reveals the feasibility region and peak structure.
- The slice plots clearly show the unimodal distribution.
- The growth rate analysis is well-presented.

---

## Overall Assessment

**Visualization Score**: 7/10

The visualizations are functional but need refinement for clarity and interpretation. The heatmaps are the strongest element, but they need better labeling and context. The 3D geometry plots may not add sufficient value.

**Recommendation**: **Revise and resubmit** after addressing required fixes #1-4. Implementing the optional improvements (especially #5, #6, #7) would make this exemplary.

---

## Specific Suggestions for Colab

- Add a cell that generates a "publication-ready" figure with proper fonts, labels, and styling.
- Include a "Figure Export" cell that saves all figures with consistent naming and high resolution (300 DPI minimum).
- Add annotations to highlight interesting features (peaks, boundaries, symmetries).

---

*Signed, E. Tufte*
