# Report specification

## 1. Reader outcome

A reader should understand the result from the first screen and find supporting data within one click. Write for a mixed audience: direct language for the result, exact identifiers and source symbols for technical review.

Do not use a template section unless it contains new facts. The page is complete when every claim is traceable and nothing redundant remains.

## 2. Opening block

The opening must contain:

1. A one-sentence conclusion that names the subject, collection or finding, and practical boundary.
2. A compact evidence-backed summary of what data or behavior is covered.
3. The mechanism in plain language.
4. The most important difference or risk boundary.

Avoid a history of the investigation or an explanation of how the page was assembled.

## 3. Deletion rules

Remove copy that does any of the following:

- labels itself as a report, conclusion, next section, or summary before saying the fact;
- says “本文 / 本报告 / 下面 / 接下来 / 需要注意的是 / 综上所述” when the sentence can stand alone;
- explains the writing process, the model, the assistant, the capture setup, or the toolchain instead of the subject;
- introduces a term only to explain it later in a large glossary;
- repeats the same conclusion in the heading, subtitle, lead, card, and callout;
- adds “待验证 / 需验证 / 后续确认 / 可能 / 推测” when supplied evidence establishes the fact;
- uses “领导 / 管理层 / AI / 工具 / 自动化分析” as visible report language;
- uses “证据显示” before a claim that already sits beside its source;
- uses generic praise such as “全面 / 高效 / 深入 / 极大提升” without measured meaning;
- leaves empty rows, cards, accordions, captions, spacers, or decorative section numbers.

When evidence is incomplete, resolve it from the artifacts first. If the missing fact changes the primary conclusion, ask before drafting. Do not publish a report built around uncertainty language.

## 4. Information architecture

Use the smallest amount of structure that supports the request.

- Result report: conclusion → evidence table or chart → mechanism → field/behavior detail → scenarios → provenance.
- Comparison report: conclusion → same dimensions → different dimensions → shared source comparison → unified diagram → fields → provenance.
- Audit report: conclusion → finding → full chain → source/evidence detail → data model → boundary → provenance.
- Research report: conclusion → key facts → comparison matrix → representative examples → limitations that affect interpretation → provenance.
- Business decision report: conclusion → decision inputs → evidence or data → tradeoffs → recommendation → source notes.
- Project review: conclusion → planned versus delivered result → deviations → causes → corrective actions → responsible data or source.
- Test report: conclusion → scope → test matrix → failure evidence → impact → release or remediation decision.
- Product or technical proposal: conclusion → current constraint → proposed mechanism → data/request flow → measurable effect → boundary → source notes.
- Office data report: conclusion → KPI snapshot → trend/target → driver breakdown → exceptions → actions → data notes. For detailed metric, chart, and calculation rules, read `references/office-data-reports.md`.
- Sales report: conclusion → revenue and volume → target attainment → product/region/channel drivers → pipeline or risk → data notes.
- Budget report: conclusion → actual versus budget → category variance → fixed/variable and one-off items → forecast → actions.
- Operations review: conclusion → service or production result → trend → bottleneck → exceptions → owner/action → source notes.

Avoid a table of contents when the page has fewer than six sections. Use a compact sticky navigation only for long reports.

## 5. Terms and identifiers

- Write a plain-language meaning the first time an internal code appears.
- Keep the original code beside the explanation: `BIType=111（环境数据包编号）`.
- For field tables, include raw field, meaning, source/evidence, and data nature.
- Do not translate proper nouns into a different product name.
- Do not leave an unexplained single-letter or numeric type in the visible conclusion.

## 6. Visual language

Use a GitHub-light system unless the user pins another visual identity.

- Page: `#f6f8fa`; surface: `#ffffff`; primary text: `#1f2328`; muted text: `#57606a`; border: `#d0d7de`.
- Blue `#0969da` for the first subject or external calls; green `#1a7f37` for the second subject or confirmed behavior; amber `#9a6700` for the third subject or boundary emphasis.
- Keep one hierarchy: page title, section title, subsection title, body, metadata.
- Body measure 65–75 characters. Tables may be wider but must scroll locally.
- Use borders for hierarchy. Do not use decorative shadows, glass, gradients, colored side stripes, or pill-shaped containers.
- Maximum card radius is 10px for diagram nodes and 8px for report surfaces.
- Use system fonts and a system monospace stack. No remote font dependency.
- Chinese text must not fall below 12px inside diagrams.
- Include print styles. Disable animation or scroll effects under `prefers-reduced-motion`.

## 6A. Open-source style families

Choose one style family from `references/open-source-styles.md` and keep it consistent across the report.

- `github`: Primer CSS-inspired, default for source and engineering reports.
- `minimal`: Pico-inspired, semantic and compact.
- `research`: Tufte-inspired, long-form analysis with notes and data.
- `dashboard`: Start Bootstrap-inspired, status and metric reporting.
- `gallery`: HTML5 UP-inspired visual presentation, only when attribution and license are handled.
- `themeable`: daisyUI token model for projects that explicitly need several themes.

Style families change typography, surfaces, borders, and density. They do not change the required conclusion-first information architecture. For a self-contained report, implement only the selected tokens locally; do not link a CDN, framework runtime, or remote font.

## 6B. Office data rules

- Define period, entity, unit, currency, aggregation rule, comparison baseline, source, and refresh time.
- Keep percent, percentage points, counts, money, ratios, and averages distinct.
- Show enough detail to reconcile totals; label a residual when the total does not equal the visible rows.
- Use “无记录” for a missing category and explain the coverage; never invent a value.
- Charts must state the period, unit, baseline, and a one-line takeaway.
- Separate measured fact, supported explanation, and recommended action.
- Detailed formulas, report structures, chart selection, and office scenarios are in `references/office-data-reports.md`.

## 7. Tables and cards

- Tables are for multidimensional comparison, field semantics, permissions, timestamps, and source identity.
- Cards are for a short summary with a distinct role; do not turn every paragraph into a card.
- Three summary cards must have unequal emphasis or widths when possible.
- On phones, convert wide tables to stacked rows with `data-label` visible.
- Every card must answer a different question. Merge cards that repeat the same point.

## 8. Diagrams

Use Diagram Design for architecture, data flow, sequences, state changes, or cross-system comparisons. The report should contain one overview diagram whenever one diagram can carry the relationship.

- Define the four output dials in the Diagram Design skill before drawing: format, size, detail, audience.
- Use `doc-wide` for a multi-system comparison, or `doc-inline` for one chain.
- Keep the chosen type within its complexity budget. Use zones or split into overview/detail when the subject is larger.
- Make clickable node or stage regions navigate to the source section below.
- Give each section target a stable id and `scroll-margin-top`.
- Include keyboard focus styling for SVG anchors.
- Do not put a free-floating legend inside the drawing area.

## 9. Code blocks

Use a fenced-code visual language in HTML without Markdown runtime dependencies.

```html
<pre class="code"><code data-lang="java"><span class="tok-k">if</span> (...) { ... }</code></pre>
```

- Color comments, keywords, strings, numbers, and the decisive method call.
- Keep the exact stage label across compared systems.
- Each code card shows the source location above the block.
- Long code scrolls locally; do not collapse source behind hidden tabs unless the report is exceptionally long.
- Do not cite an entire file. Cite the method or field that establishes the behavior and show the surrounding condition.

## 10. Provenance

At minimum, record the facts that make the artifact identifiable:

- sample name and version;
- package or application identity;
- source repository and revision when supplied;
- source file, class, and method;
- APK, DEX, screenshot, or request/response hash when available;
- endpoint, field names, and report type.

Place provenance near the relevant comparison or in a closing source table. Keep it concise and searchable.

## 11. Responsive and portability checks

- `meta viewport` is present.
- No remote CSS, font, script, image, or iframe is used.
- One file includes all styles and content.
- Wide tables and diagrams have local horizontal scrolling.
- IDs used by anchors are unique and all internal links resolve.
- One `h1`; section headings are ordered.
- Print layout expands hidden projectors and disables sticky navigation.
- The page remains legible with CSS animations disabled and JavaScript absent.

## 12. Automated validation

Run:

```text
python scripts/check_report.py report.html
python "$HOME/.codex/skills/diagram-design/scripts/self_check.py" --offline report.html
```

Fix substantive failures. Do not weaken the checker to pass a report with repeated sections, unresolved anchors, remote resources, or missing source provenance.
