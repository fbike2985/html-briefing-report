# 使用教程

本教程覆盖安装、调用、风格选择、报告结构、检查与常见问题。

## 1. 安装技能

将仓库克隆到全局技能目录：

```bash
git clone https://github.com/fbike2985/html-briefing-report.git ~/.codex/skills/html-briefing-report
```

Windows PowerShell：

```powershell
git clone https://github.com/fbike2985/html-briefing-report.git "$HOME/.codex/skills/html-briefing-report"
```

重新打开会话后，确认技能列表出现 `html-briefing-report`。

## 2. 触发方式

技能会根据“HTML 汇报、经营分析、月度/季度报告、销售报表、预算分析、项目复盘、测试报告、调研报告、审计报告、技术方案、源码对比”等描述自动触发。

也可以显式调用：

```text
$html-briefing-report 把下面的数据整理成可直接发送的 HTML 汇报……
```

如果材料清楚，可以直接给结论、原始数据、截图、源码路径和目标读者；不需要提供采集过程。

## 3. 推荐输入格式

一次提供完整输入，减少来回确认：

```text
目标：整理成一份单文件 HTML 测试报告。
内容：结论、测试范围、通过/失败结果、失败日志、复现条件、发布判断。
数据源：tests/result.xml、logs/failure.txt。
风格：dashboard。
约束：中文正文，代码高亮，表格适应手机，不出现过程说明。
```

技能会优先从文件和已有上下文中补全事实。

## 3A. 办公数据报告怎么给材料

办公数据报告至少提供：统计周期、业务对象、指标、单位、目标或比较基准、数据源和期望的决策。例如：

```text
统计周期：2026 年 10 月；对比：2026 年 9 月和全年目标。
业务对象：华东、华南、华北三个区域。
指标：收入、订单数、客单价、目标达成率。
数据源：sales_2026_10.xlsx。
期望内容：结论、目标差距、区域/产品贡献、异常和行动建议。
```

如果原始表包含多个工作表或不同口径，先说明哪张表是主数据；技能会按源数据定义计算，不擅自改变口径。更多提示词见 [examples/prompts.zh-CN.md](../examples/prompts.zh-CN.md)。

## 4. 选择风格

| 风格 | 适用内容 | 特点 |
|---|---|---|
| `github` | 技术报告、源码审计、接口与数据对比 | 信息密度高，边框清晰，技术阅读稳定 |
| `minimal` | 简短决策材料、单页摘要 | 语义化、留白充分、层级克制 |
| `research` | 长文分析、研究结论、带旁注的证据 | 衬线标题、长文阅读、来源说明突出 |
| `dashboard` | 月度/季度经营、销售、预算、项目状态、测试和运营数据 | 数据与状态分组明确，表格可扫描 |
| `gallery` | 对外汇报、调研成果展示 | 视觉表现更强，适合摘要与案例 |

默认使用 `github`。源码、字段与大量表格优先 `github`；纯业务结论优先 `minimal`；长篇解释优先 `research`。

## 5. 报告结构

常见顺序如下，缺少事实的章节直接删除：

1. 结论：发生了什么，数据或行为范围是什么，机制是什么，边界是什么。
2. 关键证据：数据、截图、请求对象、返回对象、测试记录。
3. 对比或机制：相同点、不同点、链路和阶段。
4. 源码与字段：类、方法、字段名、含义和来源。
5. 场景判断：适用条件、权限、组合字段与处理边界。
6. 来源：版本、哈希、文件、端点、提交或截图标识。

不要为了保持模板完整而保留空章节。

### 办公数据报告

办公数据报告通常使用：

1. 结论：实际值、目标差距、环比同比、主要驱动和需要决策的事项。
2. KPI 快照：实际、目标、上期、同比、单位和数据来源。
3. 趋势与目标：时间轴、目标线、明显拐点和口径变化。
4. 驱动拆解：产品、区域、渠道、客户、团队或成本项贡献。
5. 异常项：下降、集中度、一次性项目、缺失覆盖。
6. 行动项：负责人、截止时间、预期结果；源数据未提供时不要编造。
7. 数据说明：统计周期、单位、币种、公式、来源和刷新时间。

完整口径和图表规则见 [references/office-data-reports.md](../references/office-data-reports.md)。

## 6. 代码对照

按阶段对齐不同系统，例如：

```text
01 触发 → 02 条件 → 03 采集 → 04 数据组织 → 05 保存/去重 → 06 外发
```

每个系统使用相同阶段名，代码块上方写出源文件、类和方法。只保留证明行为的代码，不粘贴整份文件。

推荐 HTML 结构：

```html
<div class="code-path">Source.java · Class.method()</div>
<pre class="code"><code data-lang="java"><span class="tok-k">if</span> (...) { ... }</code></pre>
```

检查器会验证代码块是否使用统一结构并包含语法高亮。

## 7. 图表

图表使用 `diagram-design` 技能选择正确的流程、泳道、数据流或架构类型。

要求：

- 中文报告使用中文标签。
- 每个节点或阶段使用 `<a href="#section-id">` 连接到对应说明。
- 图表放在 `overflow-x:auto` 容器内。
- SVG 必须有 `role="img"`、`title` 和 `desc`。
- 图上不放与内容无关的装饰。

## 7A. 从模板开始

通用报告使用 [assets/report-starter.html](../assets/report-starter.html)，办公数据报告使用 [assets/office-report-starter.html](../assets/office-report-starter.html)。

## 8. 检查和预览

```bash
python scripts/check_report.py report.html
python scripts/check_report.py office-report.html --profile data
python ~/.codex/skills/diagram-design/scripts/self_check.py --offline report.html
```

检查失败时优先修正报告，不要修改检查器绕过问题。

浏览器直接打开 HTML 即可预览。最终交付前重点检查：

- 手机宽度下表格和代码块是否独立滚动；
- 关闭网络后页面是否仍完整显示；
- 所有目录链接与图表节点是否能跳转；
- 页面标题、结论、字段解释和来源是否完整；
- 是否残留草稿、空卡片、重复段落或未命名占位。

## 9. 自定义

视觉变量位于 [assets/github-report.css](../assets/github-report.css)。修改颜色、间距和字号时保持语义变量，不要在单个段落中散落硬编码颜色。

风格通过根元素切换：

```html
<body data-style="github">
```

支持值：`github`、`minimal`、`research`、`dashboard`、`gallery`。

## 10. 常见问题

**生成结果像普通网页，不像汇报。**  
把“结论、数据范围、机制、边界”写进任务，并要求先出结论再展开。

**代码块只有纯黑文本。**  
使用 `pre.code > code`，并为关键词、字符串、注释、数字添加 `tok-*` 类。

**表格在手机上看不清。**  
为表头或单元格设置 `data-label`，移动端使用堆叠布局。

**图片或字体离线后消失。**  
将必要资源内嵌为 data URI，或改用本地系统字体；最终报告不得依赖远程资源。

**报告中出现过程性废话。**  
删除对文档、模型、写作方法或采集工具的描述，只保留与结论、机制、数据和来源直接相关的内容。
