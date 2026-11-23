# Office and business data reports

Use this reference for monthly and quarterly reviews, sales analysis, budget and expense reports, operations, project status, staffing, customer service, quality, and other office data reports.

## 1. Start with the business question

State the decision the report supports before choosing charts or sections. Common questions:

- What changed against the previous period or target?
- Which products, regions, teams, customers, or channels explain the change?
- Which exceptions need action?
- Is the result driven by volume, price, mix, conversion, cost, retention, or timing?
- What is the outlook if the current run rate continues?
- What action is required, by whom, and by when?

The visible conclusion should answer the main question with the key numbers and the reason they moved.

## 2. Data contract

Every metric shown in the conclusion needs a compact definition. Record:

- reporting period and time zone;
- entity and aggregation level;
- numerator and denominator;
- unit and currency;
- precision and rounding;
- comparison baseline: prior period, same period last year, target, budget, or forecast;
- inclusion and exclusion rules;
- source file, query, system, and refresh time;
- known changes in definition or scope.

Use the same definition across the report. Do not compare numbers that use different scopes, currencies, tax treatments, or time ranges.

## 3. Calculation rules

Show the common formulas near the relevant table or chart:

```text
环比 = (本期 - 上期) / 上期
同比 = (本期 - 去年同期) / 去年同期
目标达成率 = 实际值 / 目标值
贡献度 = 分项变化 / 总体变化
客单价 = 收入 / 订单数
转化率 = 完成目标人数 / 进入流程人数
```

- Show the denominator when it changes the meaning.
- Keep percentage and percentage-point changes separate.
- Use absolute values with direction labels when growth is near zero or signed.
- Explain an index, score, or synthetic metric before using it.
- Do not average percentages across groups without stating the weighting rule.
- Use “无记录” for a missing category and explain the data coverage; do not replace missing data with zero.

## 4. Recommended structure

### Periodic operating report

1. Conclusion: actual result, target gap, period movement, main drivers, action.
2. KPI snapshot: actual, target, prior period, same period last year, unit.
3. Trend and target: time series, target line, notable breaks.
4. Driver decomposition: product, region, channel, customer, cost, or team.
5. Exceptions: top misses, abnormal concentration, data gaps.
6. Action table: owner, action, deadline, expected effect.
7. Data notes: scope, definitions, source, refresh time.

### Sales report

1. Revenue, volume, price, mix, new and returning customers.
2. Target attainment by region, product, channel, and salesperson when available.
3. Top growth and decline contributors.
4. Conversion, retention, receivables, or inventory where relevant.
5. Pipeline and next-period risk.

### Budget and expense report

1. Actual versus budget and forecast.
2. Variance by category and business owner.
3. Fixed versus variable cost and one-off items.
4. Forecast impact and corrective action.
5. Accounting scope and currency notes.

### Project or operating review

1. Outcome versus milestone and commitment.
2. Schedule, scope, cost, quality, and risk.
3. Blocked items and dependency.
4. Recovery action, owner, due date.
5. Change log and source.

### Customer, quality, or service report

1. Satisfaction, failure, SLA, complaint, or turnaround result.
2. Segment and cause distribution.
3. High-impact cases and repetition pattern.
4. Remediation, prevention, owner, deadline.
5. Data coverage and excluded cases.

## 5. Chart selection

| Story | Chart | Avoid |
|---|---|---|
| Change over time | Line chart | Decorative sparkline without axis or period |
| Compare categories | Horizontal bar | Pie chart with many slices |
| Show target versus actual | Bar with target marker or bullet chart | Two unrelated scales |
| Explain a total change | Waterfall | Stacked bar without the bridge logic |
| Show composition | Stacked bar or treemap | Rainbow legend with more than five unnamed groups |
| Show distribution | Histogram or beeswarm/box plot | Average-only claim for a skewed population |
| Show relationship | Scatter plot | Correlation without units and sample size |
| Show process drop-off | Funnel | Equal-width boxes implying no conversion loss |

Every chart includes period, unit, comparison baseline, source, and one readable takeaway. Use tabular numerals and direct labels when the value is the point.

## 6. Tables

A summary table should show:

- metric;
- current period;
- comparison period or target;
- change and unit;
- source or owner.

A detail table should support sorting conceptually through grouping and alignment. Keep counts and money right-aligned, use consistent decimals, and include totals that reconcile with the visible rows. If the total does not reconcile because of exclusions or unallocated amounts, label the residual explicitly.

## 7. Insight quality

An insight needs a measured change, a driver, and a consequence. “Revenue increased” is incomplete. Use:

```text
Revenue was 12.4m, 8.6% above target and 5.1% above last month.
The increase came mainly from the East region (+1.1m) and product A (+0.7m).
Product B declined 9.2%; the decline offset 0.3 percentage points of the total growth.
```

Distinguish:

- fact: measured value;
- explanation: supported driver or decomposition;
- recommendation: action based on the result.

Do not present a recommendation as the cause of a movement.

## 8. Office report visual system

- Use `dashboard` for routine operating, sales, budget, and project reports.
- Use `minimal` for a short executive brief.
- Use `research` for a long analytical explanation with notes.
- Use `github` when the report contains dense source, query, API, or system detail.
- Keep the conclusion on the first screen with one main trend or target chart nearby.
- Use one primary accent for target and one semantic warning color for exceptions.

## 9. Quality checks

- The conclusion can be understood without reading the tables.
- Every metric has a period, unit, definition, and source.
- Every comparison uses a stated baseline.
- Percentages, percentage points, counts, money, and ratios are not mixed.
- Totals reconcile with details or the residual is explained.
- Top drivers include both positive and negative effects.
- Recommendations name an owner and a deadline when the prompt provides them.
- Missing data is not replaced with invented values.
- Source notes identify the file, system, query, or export date.
