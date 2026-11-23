# Open-source HTML style library

Use these projects as design references or implementation sources after checking the report's destination and license. The delivered report remains one self-contained HTML file; do not link to a CDN in the final artifact.

## Selection matrix

| Style key | Reference | License | Best for | Do not use for |
|---|---|---|---|---|
| `github` | [Primer CSS](https://github.com/primer/css) | MIT | Source audits, engineering briefs, API and data reports, comparisons | Visual campaigns or informal editorial layouts |
| `minimal` | [Pico CSS](https://github.com/picocss/pico) | MIT | Short decision briefs, semantic documents, clean single-page summaries | Dense multi-column dashboards or code-heavy side-by-side reports |
| `research` | [Tufte CSS](https://github.com/edwardtufte/tufte-css) | MIT | Long-form analysis, evidence narratives, scholarly or analytical reports | Highly interactive dashboards |
| `dashboard` | [Start Bootstrap](https://startbootstrap.com/) | MIT for free themes | Metrics, operations, project status, test and monitoring summaries | Long prose or code comparison pages |
| `gallery` | [HTML5 UP](https://html5up.net/) | Creative Commons Attribution 3.0 | Visual research showcases, public-facing summaries, portfolios | Dense technical reports unless the license attribution is included |
| `themeable` | [daisyUI](https://github.com/saadeghi/daisyui) | MIT | Applications needing multiple theme tokens or a theme switcher | Static reports where one restrained visual system is enough |

## Theme capability notes

- **daisyUI** currently documents 35 built-in themes, custom theme generation, and section-level nested themes. Use its semantic token model as inspiration: base, primary, secondary, accent, neutral, info, success, warning, error. Do not import Tailwind or daisyUI into a static report unless the project already uses it.
- **Pico CSS** documents 20 precompiled color themes with more than 100 combinations. It is class-light and semantic. Its repository is archived at v2.1.1, so use the stable ideas or a maintained fork rather than expecting new releases.
- **Primer CSS** is GitHub's implementation. It provides separate core, product, and marketing layers. Its repository is in maintenance mode, which is acceptable for a stable report baseline.
- **Tufte CSS** is a focused, CSS-only editorial system with sidenotes and strong typography. Use a local font fallback for self-contained reports.
- **HTML5 UP** is a collection of complete responsive templates, not one shared theme engine. Attribution is required under CC BY 3.0 unless a separate license is obtained. Keep attribution in the report when its template code is reused.
- **Start Bootstrap** publishes free Bootstrap templates and themes under the MIT license. Prefer its information hierarchy and responsive behaviors rather than copying scripts or vendor assets.

## Recommended defaults

1. Technical or source-based report → `github`.
2. Short general-purpose briefing → `minimal`.
3. Long analytical report with footnotes or evidence annotations → `research`.
4. Operational or test status report → `dashboard`.
5. Public-facing visual summary → `gallery`.
6. User explicitly requests multiple visual themes → define shared semantic tokens first, then offer only the variants that fit the content. Use the daisyUI token model as a reference.

## Implementation rules

- Keep the final output standalone: embed only the CSS actually used, inline SVG, and local images.
- Use CSS variables for semantic colors, spacing, radii, and type. A style change must not require rewriting the content or source sections.
- Do not copy external template HTML wholesale. Recreate the information structure with the report's real content.
- Preserve required attribution when CC BY material is used.
- Do not use a heavy framework merely to obtain a theme. Reproduce the needed tokens and components in compact report CSS.
- Every selected style must still satisfy the conclusion-first structure, responsive behavior, accessibility, code highlighting, and provenance requirements in this skill.

## Local style presets

`assets/github-report.css` exposes token overrides through `data-style`:

```html
<body data-style="github">...</body>
<body data-style="minimal">...</body>
<body data-style="research">...</body>
<body data-style="dashboard">...</body>
<body data-style="gallery">...</body>
```

The default is `github`. Choose one style for the complete report. Do not mix style families section by section.
