---
name: html-briefing-report
description: Create or revise self-contained HTML reports for office data analysis, operating reviews, sales and budget reports, project and test reviews, business briefings, audits, research findings, technical proposals, source comparisons, and evidence reviews. Use when the user asks for an HTML 汇报, 经营分析, 月度报告, 季度报告, 销售报表, 预算分析, 项目复盘, 测试报告, 调研报告, 审计报告, 技术方案, 源码对比, or asks to 整理/改写此类页面; require conclusion-first writing, accurate metric definitions, structured visual hierarchy, highlighted code when present, traceable data, concise copy, and clickable Diagram Design visuals.
---

# HTML Briefing Report

Build a single, self-contained HTML file for business readers, analysts, and technical reviewers. Lead with the result, make the data basis and source trail clear, and use the remaining space for facts that support a decision.

## Report modes

Choose one primary mode from the supplied material. A report can include a secondary mode, but keep one information architecture.

- **Office data report**: monthly or quarterly operations, sales, budget, project status, workforce, service, quality, or other business data. Read `references/office-data-reports.md` and normally use `assets/office-report-starter.html`.
- **Technical or source report**: SDK behavior, source chains, request or response inventories, implementation comparisons, logs, and code. Read `references/source-comparison.md` and normally use `assets/report-starter.html`.
- **General business briefing**: decisions, recommendations, research findings, strategy, or project narrative without a dense data or source appendix. Use the report specification and the smallest suitable section set.

## Required context

Read these before implementation:

1. If the report contains a diagram, use the `diagram-design` skill when available. Read its `SKILL.md` and the selected type reference; use the relevant semantic pattern and one readable diagram family.
2. Read [references/report-spec.md](references/report-spec.md) for the writing, layout, evidence, and responsive rules.
3. If the request contains business metrics, spreadsheets, sales, budget, operations, project status, or other office data, read [references/office-data-reports.md](references/office-data-reports.md).
4. If the request includes code, source comparison, audit chains, or field semantics, read [references/source-comparison.md](references/source-comparison.md).
5. When the visual style is not already fixed, read [references/open-source-styles.md](references/open-source-styles.md) and select one style family that matches the report content and destination.

Use [assets/report-starter.html](assets/report-starter.html) for general reports and [assets/office-report-starter.html](assets/office-report-starter.html) for office data reports. Inline [assets/github-report.css](assets/github-report.css) and all report content into the final HTML.

## Visual quality

The default is a production briefing page, not a decorative landing page.

- Use `dashboard` for monthly, quarterly, sales, budget, operations, and project status reports.
- Use `github` for source audits, engineering reports, API comparisons, and dense technical tables.
- Use `minimal` for short executive summaries, `research` for long analytical narratives, and `gallery` for visual research summaries.
- Apply one style family to the entire report. Switch theme tokens through `data-style`; do not mix unrelated visual systems section by section.
- Give each screen one focal fact. Let hierarchy, type size, and layout carry emphasis.
- Let the content choose the form: KPI summary, trend, target comparison, contribution breakdown, exception table, process or source sequence, timeline, code differential, or data graphic. Do not repeat one card layout for every section.
- Use asymmetric grouping and varied section rhythm while preserving a stable grid.
- Keep body text readable, use tabular numerals for data, and avoid faux italics or faux bold on Chinese text.
- Remove decorative template habits: repeated uppercase kickers, mid-dot slogans, gratuitous icons, gradient text, colored side stripes, and identical cards.
- When multiple themes are requested, define semantic tokens first and implement only the variants needed. daisyUI's token model is a reference; it is not a runtime dependency for a standalone report.

## Non-negotiable output contract

- Put a clear, complete conclusion at the top. State the result, the data or behavior covered, the main drivers, and the practical boundary.
- Treat every explicit user requirement as binding: preserve requested comparisons, samples, fields, tone, scope, and emphasis. A template never overrides the brief.
- Preserve all supplied facts exactly: version strings, hashes, names, endpoints, field values, and screenshots. Do not simplify or paraphrase identifiers into different facts.
- Write direct factual prose. Remove assistant meta-commentary, drafting notes, role labels, tool narration, implementation-tool names unrelated to the subject, and statements that merely describe the document.
- Do not add empty transitional copy, repeated explanations, placeholder rows, empty cards, or sections containing only labels.
- Do not write uncertainty scaffolding such as “待验证”, “需进一步确认”, or equivalent. Resolve gaps from the supplied artifacts or omit unsupported claims. If an unknown blocks the core result, ask before producing the report.
- Explain specialized identifiers once, near the fact that needs them. Prefer inline meaning over a separate glossary full of ceremony.
- Preserve source vocabulary for proper nouns and field names. Pair an unexplained identifier with a plain-language meaning.
- State provenance explicitly: reporting period, data source, metric definition, unit, source file or query, version, hash, endpoint, or screenshot identity as applicable.
- Use the selected local style system from `assets/github-report.css`; when no style is specified, use the GitHub-light preset with system fonts, paper `#f6f8fa`, white surfaces, `#d0d7de` rules, blue/green/amber accents, crisp borders, and no decorative shadows.
- Produce one standalone `.html`. Embed CSS, inline SVG, and optional raster assets. Do not depend on remote fonts, scripts, CDNs, or images.
- Keep the page readable on phone, tablet, desktop, iOS, Android, and HarmonyOS browsers. Wide tables and diagrams scroll locally rather than expanding the whole page.
- Use no JavaScript by default. Clickable stages, KPI drill-downs, source references, and navigation must work with ordinary anchors.
- Use semantic HTML: one `h1`, ordered `h2` sections, real tables, real `pre > code` blocks, visible focus states, and print styles.

## Workflow

1. **Extract the decision.** Identify the result the reader should understand first. Separate supplied facts from explanation or inference.
2. **Build a fact sheet before styling.** For office data, record period, entity, metric definition, unit, comparison baseline, aggregation rule, and source. For technical reports, record fields, source symbols, samples, versions, and boundaries.
3. **Draft the opening conclusion.** Answer the business or technical decision question with the key result, relevant period or baseline, main driver, impact, and practical boundary.
4. **Choose the minimum structure.** Office data reports usually use conclusion → KPI snapshot → trend and target → driver breakdown → exceptions → actions → data notes. Source reports use conclusion → result → mechanism → source detail → boundary → provenance. Remove any section that does not add a fact or decision.
5. **Draw before duplicating prose.** Use Diagram Design for sequences, data flows, trends, comparisons, or relationships. Link each stage or node to the section that carries its supporting detail.
6. **Write code comparisons when code is part of the request.** Keep the same stages across all systems. Use marked-up `pre > code` blocks with syntax colors and focus the statements that prove the behavior.
7. **Run the checks.** Execute `python scripts/check_report.py <file.html>`. Add `--profile data` for office data reports. If an SVG exists, also run Diagram Design's `scripts/self_check.py --offline <file.html>`. Fix every failure before delivery.

## Content decisions

- For office data reports, define reporting period, metric, unit, comparison baseline, calculation rule, data source, and exceptions. Never invent missing values.
- For technical field inventories, pair raw field names with plain-language meaning and data nature.
- For comparisons, align the same periods, entities, units, and definitions before comparing. Give both a compact similarity table and a detailed difference table.
- For source audits, show the full chain in stage order: trigger → gate → collection → normalization → queue/storage → outbound. Use exact class and method names and short code excerpts.
- For screenshots, preserve the image contents and pair them with the precise source or data object they show. Do not add image galleries that do not prove a claim.
- For sensitive identifiers, mask only when the user requests masking. Keep the original source value when the report is intended as direct evidence and no masking request exists.
- For compliance scenarios, tie each statement to observed behavior: trigger, permission, collected fields, combination, storage, retention, and outbound destination. Avoid generic legal lectures.

## Diagram requirements

- Use the Diagram Design selection gate. Pick one primary semantic pattern and visual type.
- Prefer one overview diagram over several decorative diagrams.
- Use Chinese labels for Chinese reports.
- Use clickable `<a href="#section-id">` regions around stages or nodes. Include keyboard focus styles and verifying targets.
- Keep the SVG inside an `overflow-x:auto` wrapper. Its `min-width` must equal the viewBox width.
- Use the selected report style tokens consistently.
- Every SVG needs `role="img"`, a first-child `<title>`, and a non-empty `<desc>`.
- Do not add a diagram when a table or paragraph explains the relationship more clearly.

## Code presentation

Apply this section only when code or implementation excerpts are included.

- Use `<pre class="code"><code data-lang="java">...</code></pre>`.
- Highlight comments, keywords, strings, and numbers with `.tok-c`, `.tok-k`, `.tok-s`, and `.tok-n` spans.
- Group code by stage, not by source file. Place parallel systems in equal columns on desktop and stack them on mobile.
- Keep excerpts short enough to prove the point. Preserve surrounding conditions and the call that carries data to the next stage.
- Never use black code blocks with no syntax differentiation.

## Final pass

Delete any sentence that only explains the document, the model, the toolchain, or the writing process. Then check:

- The first substantive section is the conclusion.
- Every office metric has a period, unit, definition, and source.
- Every technical field in a source report has a meaning.
- Every diagram stage or KPI drill-down reaches supporting detail.
- Every included code block is highlighted and tied to a location.
- No unsupported claim, placeholder, or empty section remains.
- The standalone file opens without network access.
