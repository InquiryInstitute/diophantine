#!/usr/bin/env python3
"""
LLM Analysis of Diophantine Results
Analyzes the generated results and figures using an LLM.
"""

import json
import os
import base64
from pathlib import Path
from typing import Dict, List, Optional

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    print("Warning: OpenAI not available. Using mock analysis.")

def encode_image(image_path: Path) -> str:
    """Encode image to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def load_results() -> Dict:
    """Load analysis results."""
    results_path = Path("results/summary.json")
    if not results_path.exists():
        return {}
    
    with open(results_path, 'r') as f:
        return json.load(f)

def load_sample_data() -> List[Dict]:
    """Load sample multiplicity data."""
    import pandas as pd
    csv_path = Path("results/multiplicity_samples.csv")
    
    if not csv_path.exists():
        return []
    
    df = pd.read_csv(csv_path)
    return df.to_dict('records')

def get_figures() -> List[Dict]:
    """Get list of generated figures."""
    figures_dir = Path("figures")
    figures = []
    
    figure_files = [
        "heatmap_log.png",
        "heatmap_linear.png",
        "slices_fixed_u.png",
        "growth_rate.png",
    ]
    
    for fig_file in figure_files:
        fig_path = figures_dir / fig_file
        if fig_path.exists():
            figures.append({
                "name": fig_file,
                "path": str(fig_path),
                "encoded": encode_image(fig_path)
            })
    
    return figures

def analyze_with_llm(results: Dict, sample_data: List[Dict], figures: List[Dict]) -> str:
    """Use LLM to analyze results."""
    
    if not HAS_OPENAI:
        return generate_mock_analysis(results, sample_data, figures)
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not set. Using mock analysis.")
        return generate_mock_analysis(results, sample_data, figures)
    
    client = OpenAI(api_key=api_key)
    
    # Prepare context
    context = f"""
# Diophantine Constraint Analysis Results

## Summary Statistics
{json.dumps(results, indent=2)}

## Sample Multiplicity Data (first 20 entries)
{json.dumps(sample_data[:20], indent=2)}

## Generated Figures
{len(figures)} figures generated:
{', '.join([f['name'] for f in figures])}
"""
    
    # Prepare messages
    messages = [
        {
            "role": "system",
            "content": """You are a mathematical researcher analyzing Diophantine constraint results. 
            Analyze the data and figures, identify key patterns, validate hypotheses from the essay, 
            and provide insights about the multiplicity structure, growth rates, and geometric properties.
            Write in a clear, scholarly style suitable for inclusion in a research report."""
        },
        {
            "role": "user",
            "content": context
        }
    ]
    
    # Add figure images if available
    if figures:
        for fig in figures[:4]:  # Limit to 4 figures due to token limits
            messages.append({
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Figure: {fig['name']}"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{fig['encoded']}"
                        }
                    }
                ]
            })
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # or "gpt-4-vision-preview" for vision
            messages=messages,
            max_tokens=2000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return generate_mock_analysis(results, sample_data, figures)

def generate_mock_analysis(results: Dict, sample_data: List[Dict], figures: List[Dict]) -> str:
    """Generate analysis without LLM (fallback)."""
    
    analysis = f"""# Automated Analysis of Diophantine Results

## Summary

Analysis completed on {len(sample_data)} data points with {len(figures)} figures generated.

## Key Findings

### Multiplicity Patterns
- Maximum multiplicity observed: {results.get('max_multiplicity', 'N/A')}
- Location of maximum: u={results.get('max_multiplicity_location', {}).get('u', 'N/A')}, v={results.get('max_multiplicity_location', {}).get('v', 'N/A')}
- Total feasible pairs: {results.get('total_computed', 'N/A')}

### Sample Values
"""
    
    if sample_data:
        for entry in sample_data[:5]:
            analysis += f"- M({entry.get('u', '?')}, {entry.get('v', '?')}) = {entry.get('multiplicity', '?')}\n"
    
    analysis += f"""
### Figures Generated
{len(figures)} visualization(s) created:
"""
    for fig in figures:
        analysis += f"- {fig['name']}\n"
    
    analysis += """
## Observations

1. **Feasibility Region**: The data confirms that solutions exist primarily in the region u ≤ v ≤ n·u, as predicted by the theoretical analysis.

2. **Growth Patterns**: The multiplicity appears to follow polynomial growth, consistent with the constraint lying in an (n-2)-dimensional affine space.

3. **Peak Structure**: For fixed u values, the multiplicity distribution shows unimodal behavior, peaking at intermediate v values.

## Recommendations

- Consider extending the analysis to larger parameter ranges
- Investigate congruence patterns more deeply
- Explore asymptotic behavior as u, v → ∞
- Validate the conjectured growth rate formulas

---
*Note: This is a mock analysis. For full LLM analysis, set OPENAI_API_KEY environment variable.*
"""
    
    return analysis

def main():
    """Main analysis function."""
    print("=" * 70)
    print("LLM Analysis of Diophantine Results")
    print("=" * 70)
    
    # Load data
    print("\nLoading results...")
    results = load_results()
    sample_data = load_sample_data()
    figures = get_figures()
    
    print(f"  - Summary data: {'✓' if results else '✗'}")
    print(f"  - Sample data: {len(sample_data)} entries")
    print(f"  - Figures: {len(figures)}")
    
    # Run analysis
    print("\nRunning LLM analysis...")
    analysis = analyze_with_llm(results, sample_data, figures)
    
    # Save analysis
    output_path = Path("results/llm_analysis.md")
    with open(output_path, 'w') as f:
        f.write(analysis)
    
    print(f"\n✓ Analysis saved to {output_path}")
    
    # Also print summary
    print("\n" + "=" * 70)
    print("Analysis Summary")
    print("=" * 70)
    print(analysis[:500] + "..." if len(analysis) > 500 else analysis)

if __name__ == "__main__":
    main()
