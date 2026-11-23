# Usage Guide

This guide covers installation, invocation, style selection, report structure, validation, and common issues.

## 1. Install

Clone the repository into the global skills directory:

```bash
git clone https://github.com/fbike2985/html-briefing-report.git ~/.codex/skills/html-briefing-report
```

Windows PowerShell:

```powershell
git clone https://github.com/fbike2985/html-briefing-report.git "$HOME/.codex/skills/html-briefing-report"
```

Open a new session and confirm that `html-briefing-report` appears in the available skills.

## 2. Invoke

The skill is selected for HTML briefings, operating reviews, monthly and quarterly reports, sales and budget analyses, project and test reviews, research reports, audits, technical proposals, and source comparisons.

Explicit invocation also works:

```text
$html-briefing-report Turn the following materials into a send-ready HTML report...
```

When the request already includes sources, data, screenshots, and the intended result, work can start immediately.

## 3. Recommended input

Provide the task in one block:

```text
Goal: create a self-contained HTML test report.
Content: conclusion, scope, passed and failed cases, failure logs, reproduction conditions, release decision.
Sources: tests/result.xml and logs/failure.txt.
Style: dashboard.
Constraints: English copy, highlighted code, mobile-friendly tables, no process narration.
```

The skill first resolves facts from the supplied files and context.

## 3A. Office data input

Provide the period, entity, metrics, units, target or comparison baseline, data source, and decision. Example:

```text
Period: October 2026; compare with September 2026 and the full-year target.
Entities: East, South, and North regions.
Metrics: revenue, orders, average order value, and target attainment.
Sources: sales_2026_10.xlsx.
Output: conclusion, target gap, region/product contribution, exceptions, and actions.
```

If a workbook contains multiple sheets or competing definitions, name the primary sheet before analysis. More prompts are in [examples/prompts.en.md](../examples/prompts.en.md).

## 4. Choose a visual system

| Style | Best for | Character |
|---|---|---|
| `github` | Technical reports, source audits, API and data comparisons | High information density and strong technical reading rhythm |
| `minimal` | Short decision documents and one-page summaries | Semantic, restrained, generous spacing |
| `research` | Long-form analysis and annotated evidence | Editorial typography and source-oriented reading |
| `dashboard` | Monthly or quarterly operations, sales, budget, project status, tests, and operational metrics | Clear groups and scan-friendly tables |
| `gallery` | Public-facing research summaries | More expressive presentation for visual material |

`github` is the default. Use `github` for source and dense tabular work, `minimal` for short business briefs, and `research` for long explanatory documents.

## 5. Report structure

Use this order when the supplied facts support it:

1. Conclusion: what happened, what data or behavior is in scope, the mechanism, and the boundary.
2. Key evidence: data, screenshots, request or response objects, and test records.
3. Comparison or mechanism: similarities, differences, flow, and stages.
4. Source and fields: class, method, raw field name, meaning, and source.
5. Scenario assessment: conditions, permissions, field combinations, and processing boundaries.
6. Provenance: versions, hashes, files, endpoints, revisions, or screenshot IDs.

Remove any section that does not carry new facts.

### Office data reports

Use this order:

1. Conclusion: actual, target gap, period movement, main drivers, and decisions needed.
2. KPI snapshot: actual, target, prior period, year-over-year, unit, and source.
3. Trend and target: time series, target line, breakpoints, and definition changes.
4. Driver breakdown: product, region, channel, customer, team, or cost contribution.
5. Exceptions: decline, concentration, one-off items, and missing coverage.
6. Actions: owner, deadline, and expected result only when supplied.
7. Data notes: period, unit, currency, formula, source, and refresh time.

See [references/office-data-reports.md](../references/office-data-reports.md) for detailed metric and chart rules.

## 6. Code comparison

Align systems by the same stages:

```text
01 trigger → 02 gate → 03 collection → 04 normalization → 05 queue/dedupe → 06 outbound
```

Every system uses the same stage names. Put the source path, class, and method above each excerpt. Keep only the behavior that proves the claim.

Recommended structure:

```html
<div class="code-path">Source.java · Class.method()</div>
<pre class="code"><code data-lang="java"><span class="tok-k">if</span> (...) { ... }</code></pre>
```

The checker validates the code-block structure and syntax-highlighting tokens.

## 7. Diagrams

Use the `diagram-design` skill to select an appropriate process, swimlane, data-flow, or architecture grammar.

- Use Chinese labels for Chinese reports.
- Link each node or stage to its supporting section with `<a href="#section-id">`.
- Put the SVG in an `overflow-x:auto` wrapper.
- Give the SVG `role="img"`, a non-empty `title`, and a non-empty `desc`.
- Remove decoration that does not carry information.

## 7A. Start from a template

Use [assets/report-starter.html](../assets/report-starter.html) for general reports and [assets/office-report-starter.html](../assets/office-report-starter.html) for office data reports.

## 8. Validate and preview

```bash
python scripts/check_report.py report.html
python scripts/check_report.py office-report.html --profile data
python ~/.codex/skills/diagram-design/scripts/self_check.py --offline report.html
```

Fix the report when a check fails. Do not weaken the validator to pass a defective page.

Open the HTML directly in a browser. Before delivery, verify:

- tables and code blocks scroll inside their own containers on mobile;
- the page remains complete with network access disabled;
- navigation and diagram links resolve;
- the conclusion, field meanings, and provenance are present;
- no draft copy, empty section, repeated paragraph, or placeholder remains.

## 9. Customize

Visual tokens live in [assets/github-report.css](../assets/github-report.css). Keep customization in semantic variables instead of scattering hard-coded colors through the page.

Switch the report style on the root element:

```html
<body data-style="github">
```

Supported values: `github`, `minimal`, `research`, `dashboard`, and `gallery`.

## 10. Troubleshooting

**The result looks like a generic webpage.**  
Specify the conclusion, data scope, mechanism, and boundary, and require the conclusion before supporting detail.

**Code appears as an uncolored block.**  
Use `pre.code > code` and add `tok-*` classes for comments, keywords, strings, and numbers.

**Tables break on phones.**  
Add `data-label` attributes and use the mobile stacked-table CSS.

**Images or fonts disappear offline.**  
Embed required assets as data URIs or use local/system fonts. The final report must not depend on remote resources.

**The report contains process narration.**  
Remove language about the document, model, writing method, or investigation tool. Keep only facts tied to the conclusion, mechanism, data, and provenance.
