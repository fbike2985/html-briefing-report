# HTML Briefing Report

[中文](README.md) | [English](README.en.md)

A general-purpose Codex skill for office data analysis, operating reviews, sales and budget reports, project and test reviews, technical proposals, research findings, source audits, and data evidence reports.

It turns conclusion-first writing, metric definitions, target and trend analysis, source provenance, field explanations, source-code comparison, clickable flow diagrams, and single-file delivery into a repeatable workflow. The output is one `.html` file with no default dependency on remote fonts, CDNs, JavaScript, or image services.

## Features

- Lead with a complete conclusion, then explain the mechanism, data, and boundary.
- Remove filler transitions, repeated summaries, drafting notes, and empty placeholders.
- Define reporting period, unit, metric, comparison baseline, aggregation rule, and source for office data.
- Show raw field names beside plain-language meaning, source, and data nature.
- Reconstruct source-backed behavior as `trigger → gate/permission → collection → normalization → queue/dedupe → outbound`.
- Present code in readable fenced-style blocks with syntax colors and stage-by-stage comparison.
- Use clickable diagram stages that jump to their source or data sections.
- Ship five local visual systems: GitHub, minimal, research, dashboard, and gallery.
- Keep the report portable across desktop browsers, iOS, Android, and HarmonyOS.

## Visual systems

| `data-style` | Reference | Best for |
|---|---|---|
| `github` | Primer CSS | Source audits, engineering reports, API comparisons, data reviews |
| `minimal` | Pico CSS | Compact decision briefs and clean one-page summaries |
| `research` | Tufte CSS | Long-form analysis, sidenotes, evidence narratives |
| `dashboard` | Start Bootstrap | Monthly or quarterly operations, sales, budget, status, testing, and operational summaries |
| `gallery` | HTML5 UP | Visual research summaries and public-facing overviews |

External projects are references. A generated report embeds only the CSS it uses and does not load a framework runtime or CDN. See [references/open-source-styles.md](references/open-source-styles.md) for licenses and constraints.

## Install

### Codex Skills

```bash
git clone https://github.com/fbike2985/html-briefing-report.git ~/.codex/skills/html-briefing-report
```

Windows PowerShell:

```powershell
git clone https://github.com/fbike2985/html-briefing-report.git "$HOME/.codex/skills/html-briefing-report"
```

Open a new session after cloning; the skill will appear in the available skill list.

### Skills CLI

```bash
npx skills add fbike2985/html-briefing-report
```

## Usage

Ask for an HTML report directly:

```text
Turn these test results into a single HTML report. Put the conclusion first and keep failure evidence with source locations.
```

```text
Compare the Bluetooth collection chains in these two SDKs, including similarities, differences, and stage-by-stage source code.
```

```text
Create a minimal HTML briefing from this business research and explain every data field.
```

```text
Turn this month's sales detail, targets, regions, and channels into a dashboard-style HTML operating report.
```

```text
Create an HTML budget report from budget, actual, forecast, and department expense data, including variance drivers and actions.
```

Explicit invocation is also supported:

```text
$html-briefing-report Turn the following materials into a send-ready HTML report...
```

Tutorials:

- [Chinese usage guide](docs/usage.zh-CN.md)
- [English usage guide](docs/usage.en.md)
- [Chinese office report prompts](examples/prompts.zh-CN.md)
- [English office report prompts](examples/prompts.en.md)


## Office data reports

Use the skill for monthly operating reviews, quarterly business reviews, sales targets, budgets and expenses, project updates, workforce and organization analysis, customer service, quality, and operations.

Office reports emphasize:

- result: actual, target, period movement, and budget variance;
- drivers: contribution by product, region, channel, customer, team, or cost category;
- exceptions: concentration, declines, missing coverage, and high-impact issues;
- actions: owner, deadline, and expected effect only when supplied;
- data notes: period, unit, currency, computation, source, and refresh time.

See [references/office-data-reports.md](references/office-data-reports.md) for formulas, chart selection, and report structures.

## Office data template

Use [assets/office-report-starter.html](assets/office-report-starter.html) for data reports. It provides conclusion, KPI, target/trend, driver, exception, action, and data-note sections; remove any section not supported by the source data.

## Starter template

Start from [assets/report-starter.html](assets/report-starter.html), then inline [assets/github-report.css](assets/github-report.css).

```html
<body data-style="github">
  <main id="main" class="wrap">
    <section id="conclusion">
      <div class="section-head"><h2>Conclusion</h2></div>
      <p class="lead"><strong>State the complete decision first.</strong>Then add the data scope, mechanism, and boundary.</p>
    </section>
  </main>
</body>
```

## Repository layout

```text
html-briefing-report/
├─ SKILL.md
├─ README.md
├─ README.en.md
├─ LICENSE
├─ agents/openai.yaml
├─ assets/
│  ├─ github-report.css
│  ├─ office-report-starter.html
│  └─ report-starter.html
├─ docs/
│  ├─ usage.zh-CN.md
│  └─ usage.en.md
├─ examples/
│  ├─ prompts.zh-CN.md
│  └─ prompts.en.md
├─ references/
│  ├─ office-data-reports.md
│  ├─ open-source-styles.md
│  ├─ report-spec.md
│  └─ source-comparison.md
└─ scripts/
   └─ check_report.py
```

## Validation

```bash
python scripts/check_report.py path/to/report.html
python scripts/check_report.py path/to/office-report.html --profile data
python ~/.codex/skills/diagram-design/scripts/self_check.py --offline path/to/report.html
```

`check_report.py` validates the conclusion-first structure, placeholder and filler wording, remote resource dependencies, internal anchors, code highlighting, SVG accessibility, and provenance markers.

## Core files

The entrypoint is [SKILL.md](SKILL.md). Office data rules live in [references/office-data-reports.md](references/office-data-reports.md), detailed report rules in [references/report-spec.md](references/report-spec.md), and source-chain rules in [references/source-comparison.md](references/source-comparison.md).

## License

MIT License. See [LICENSE](LICENSE).
