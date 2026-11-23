# HTML Briefing Report

[中文](README.md) | [English](README.en.md)

一个面向业务汇报、项目复盘、测试报告、技术方案、调研分析、源码审计与数据取证的通用 HTML 报告技能。

它把结论前置、事实核查、来源标注、字段解释、源码对照、GitHub 风格排版、可点击链路图和单文件交付固化为可复用流程。生成结果是单个 `.html`，默认不依赖远程字体、CDN、JavaScript 或图片服务。

## 能力

- 首屏先给完整结论，再展开机制、数据和来源。
- 删除空泛过渡、重复总结、写作过程说明和无法落地的占位话术。
- 数据报告保留原始字段名、通俗含义、来源与数据性质。
- 源码报告按“触发 → 条件/权限 → 采集 → 组织 → 缓存/去重 → 外发”组织完整链路。
- 代码使用可读的 Markdown 式代码块，并带语法高亮与阶段对照。
- 内置链路图规范，图表可点击跳转到对应源码或数据说明。
- 支持 GitHub、简洁、研究、看板、展示型五种视觉风格。
- 最终 HTML 可在桌面、iOS、Android 和 HarmonyOS 浏览器直接打开。

## 五种风格

| `data-style` | 视觉来源 | 适用场景 |
|---|---|---|
| `github` | Primer CSS | 源码审计、工程报告、接口对比、数据报告 |
| `minimal` | Pico CSS | 简洁的业务简报、单页结论 |
| `research` | Tufte CSS | 长文分析、旁注、研究型报告 |
| `dashboard` | Start Bootstrap | 指标、状态、测试与运营摘要 |
| `gallery` | HTML5 UP | 展示型调研成果与对外摘要 |

外部项目仅作为视觉与信息结构参考。最终报告只内嵌实际使用的 CSS，不加载外部框架或 CDN。各项目的许可证与使用边界见 [references/open-source-styles.md](references/open-source-styles.md)。

## 安装

### Codex Skills

将仓库克隆到 Codex 的全局技能目录：

```bash
git clone https://github.com/fbike2985/html-briefing-report.git ~/.codex/skills/html-briefing-report
```

Windows PowerShell：

```powershell
git clone https://github.com/fbike2985/html-briefing-report.git "$HOME/.codex/skills/html-briefing-report"
```

重新打开会话后，技能会自动出现在可用技能列表中。

### Skills CLI

```bash
npx skills add fbike2985/html-briefing-report
```

## 使用

直接提出需要生成的 HTML 汇报，例如：

```text
把这份测试结果整理成 HTML 汇报，结论放最前面，保留失败样本和源码位置。
```

```text
整理这两个 SDK 的蓝牙采集链路，做相同点、不同点和源码阶段对照。
```

```text
把这份业务调研整理成单文件 HTML，使用 github 风格，数据字段要解释清楚。
```

你也可以显式调用：

```text
$html-briefing-report 把下面的材料整理成可直接发送的 HTML 报告……
```

完整教程：

- [中文使用教程](docs/usage.zh-CN.md)
- [English usage guide](docs/usage.en.md)

## 新报告模板

从 [assets/report-starter.html](assets/report-starter.html) 开始，并内嵌 [assets/github-report.css](assets/github-report.css)。

```html
<body data-style="github">
  <main id="main" class="wrap">
    <section id="conclusion">
      <div class="section-head"><h2>结论</h2></div>
      <p class="lead"><strong>先写可执行的完整结论。</strong>接着写数据范围、机制与边界。</p>
    </section>
  </main>
</body>
```

## 目录

```text
html-briefing-report/
├─ SKILL.md
├─ README.md
├─ README.en.md
├─ LICENSE
├─ agents/openai.yaml
├─ assets/
│  ├─ github-report.css
│  └─ report-starter.html
├─ docs/
│  ├─ usage.zh-CN.md
│  └─ usage.en.md
├─ references/
│  ├─ open-source-styles.md
│  ├─ report-spec.md
│  └─ source-comparison.md
└─ scripts/
   └─ check_report.py
```

## 检查

```bash
python scripts/check_report.py path/to/report.html
python ~/.codex/skills/diagram-design/scripts/self_check.py --offline path/to/report.html
```

`check_report.py` 检查：

- 结论是否为第一个实质章节；
- 是否残留占位符、过程性废话或禁用的不确定话术；
- 是否存在远程脚本、字体、图片或 iframe 依赖；
- 内部锚点是否全部可解析；
- 代码块是否存在语法高亮；
- SVG 是否具备可访问描述和可点击目标；
- 是否缺少来源、版本、哈希或源码路径。

## 技能结构

核心入口是 [SKILL.md](SKILL.md)。详细写作规范位于 [references/report-spec.md](references/report-spec.md)，源码链路规范位于 [references/source-comparison.md](references/source-comparison.md)。

## License

本项目使用 MIT License，详见 [LICENSE](LICENSE)。
