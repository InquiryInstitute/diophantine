# Math Rendering Setup

This site uses **MathJax 3** for beautiful mathematical notation rendering.

## Features

- ✅ Inline math: `$x^2 + y^2 = r^2$` → $x^2 + y^2 = r^2$
- ✅ Display math: `$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$`
- ✅ Automatic equation numbering
- ✅ Right-click context menu for zooming and copying
- ✅ Works with all LaTeX math commands

## Usage in Markdown

### Inline Math
Use single dollar signs:
```markdown
The equation $E = mc^2$ is famous.
```

### Display Math
Use double dollar signs:
```markdown
$$
\sum_{i=1}^{n} x_i = u
$$
```

### Numbered Equations
Use `\begin{equation}`:
```markdown
\begin{equation}
M(u,v) = \#\{\mathbf{x} \in \mathbb{Z}_{\ge 0}^n : \text{constraints satisfied}\}
\end{equation}
```

## Pages with Math Enabled

The following pages have math rendering enabled:
- `/essay/` - Main essay with extensive mathematical notation
- `/analysis/` - Analysis results page
- `/` - Home page

## Configuration

Math rendering is configured in:
- `_includes/head-custom.html` - MathJax setup
- `_config.yml` - Kramdown math engine configuration
- Page front matter - `math: true` enables MathJax on specific pages

## Testing

To test math rendering locally:
1. Install Jekyll: `bundle install`
2. Run server: `bundle exec jekyll serve`
3. Visit: http://localhost:4000/diophantine/

Math should render automatically!
