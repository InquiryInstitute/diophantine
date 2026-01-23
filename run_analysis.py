#!/usr/bin/env python3
"""
Run the Diophantine analysis notebook and generate results.
This script executes the notebook programmatically.
"""

import json
import subprocess
import sys
from pathlib import Path

def run_notebook():
    """Execute the Jupyter notebook and save outputs."""
    notebook_path = Path("diophantine_exploration.ipynb")
    output_path = Path("diophantine_exploration_executed.ipynb")
    
    if not notebook_path.exists():
        print(f"Error: {notebook_path} not found")
        return False
    
    print("Executing notebook...")
    try:
        # Use nbconvert to execute the notebook
        result = subprocess.run(
            [
                "jupyter", "nbconvert",
                "--to", "notebook",
                "--execute",
                "--inplace",
                str(notebook_path)
            ],
            capture_output=True,
            text=True,
            check=True
        )
        print("Notebook executed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing notebook: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: jupyter not found. Installing...")
        # Fallback: try to run as Python script
        return run_as_script()

def run_as_script():
    """Fallback: Extract and run notebook cells as Python script."""
    try:
        import nbformat
        from nbconvert import PythonExporter
    except ImportError:
        print("Error: nbformat/nbconvert not available")
        return False
    
    notebook_path = Path("diophantine_exploration.ipynb")
    
    print("Converting notebook to Python script...")
    try:
        with open(notebook_path, 'r') as f:
            nb = nbformat.read(f, as_version=4)
        
        exporter = PythonExporter()
        (body, resources) = exporter.from_notebook_node(nb)
        
        script_path = Path("run_notebook_script.py")
        with open(script_path, 'w') as f:
            f.write(body)
        
        print("Running Python script...")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=True
        )
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_results():
    """Verify that results were generated."""
    results_dir = Path("results")
    figures_dir = Path("figures")
    
    required_files = [
        results_dir / "summary.json",
        results_dir / "multiplicity_samples.csv",
    ]
    
    optional_figures = [
        figures_dir / "heatmap_log.png",
        figures_dir / "heatmap_linear.png",
        figures_dir / "slices_fixed_u.png",
        figures_dir / "growth_rate.png",
    ]
    
    print("\nChecking generated files...")
    all_good = True
    
    for file in required_files:
        if file.exists():
            print(f"✓ {file}")
        else:
            print(f"✗ {file} (missing)")
            all_good = False
    
    for file in optional_figures:
        if file.exists():
            print(f"✓ {file}")
        else:
            print(f"⚠ {file} (optional, missing)")
    
    return all_good

if __name__ == "__main__":
    print("=" * 70)
    print("Diophantine Analysis Runner")
    print("=" * 70)
    
    success = run_notebook()
    
    if success:
        results_ok = check_results()
        if results_ok:
            print("\n✓ Analysis complete! Results generated successfully.")
            sys.exit(0)
        else:
            print("\n⚠ Analysis ran but some results are missing.")
            sys.exit(1)
    else:
        print("\n✗ Analysis failed!")
        sys.exit(1)
