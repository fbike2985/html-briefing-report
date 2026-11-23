#!/usr/bin/env python3
"""Validate a standalone HTML briefing report without third-party packages."""
from __future__ import annotations
import argparse
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
META_PHRASES = [
    r'本报告由', r'本页由', r'由\s*AI\s*生成', r'AI\s*生成报告', r'AI\s*工具',
    r'作为(?:一个|一名)?\s*(?:AI|人工智能|助手|模型)', r'自动化分析报告',
    r'待验证', r'待进一步验证', r'需进一步验证', r'验证中',
    r'先解释后面对照', r'内部名称', r'领导', r'管理层',
    r'\bReqable\b', r'\bXposed\b', r'\bFrida\b', r'\bhook\s*工具\b',
]

class Audit(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = {}
        self.links = []
        self.h1 = []
        self.h2 = []
        self.tags = {}
        self.stack = []
        self.title_depth = 0
        self.desc_depth = 0
        self.svg_depth = 0
        self.svg_has_title = []
        self.svg_has_desc = []
        self.svg_has_link = []
        self.current_text = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags[tag] = self.tags.get(tag, 0) + 1
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f'duplicate id: {attrs["id"]}')
            self.ids[attrs['id']] = True
        if tag == 'a' and attrs.get('href', '').startswith('#'):
            self.links.append(attrs['href'][1:])
        if tag == 'h1':
            self.h1.append('')
            self.current_text.append('h1')
        if tag == 'h2':
            self.h2.append('')
            self.current_text.append('h2')
        if tag == 'title':
            self.title_depth += 1
        if tag == 'desc':
            self.desc_depth += 1
        if tag == 'svg':
            self.svg_depth += 1
            self.svg_has_title.append(False)
            self.svg_has_desc.append(False)
            self.svg_has_link.append(False)
        if tag == 'a' and self.svg_depth and attrs.get('href', '').startswith('#'):
            self.svg_has_link[-1] = True
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in VOID:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()
            elif tag in self.stack:
                self.errors.append(f'misnested tag: {tag}')
                while self.stack and self.stack[-1] != tag:
                    self.stack.pop()
                if self.stack:
                    self.stack.pop()
            else:
                self.errors.append(f'unmatched closing tag: {tag}')
        if tag == 'title':
            self.title_depth = max(0, self.title_depth - 1)
            if self.svg_depth:
                self.svg_has_title[-1] = True
        if tag == 'desc':
            self.desc_depth = max(0, self.desc_depth - 1)
            if self.svg_depth:
                self.svg_has_desc[-1] = True
        if tag == 'svg':
            self.svg_depth = max(0, self.svg_depth - 1)

    def handle_data(self, data):
        if not self.current_text:
            return
        if self.current_text[-1] == 'h1':
            self.h1[-1] += data.strip()
        elif self.current_text[-1] == 'h2':
            self.h2[-1] += data.strip()

    def reset_heading(self, tag):
        if self.current_text and self.current_text[-1] == tag:
            self.current_text.pop()


def check(path: Path, allow_scripts: bool, allow_remote: bool, allowed_phrases: list[str]):
    errors, warnings = [], []
    try:
        source = path.read_text(encoding='utf-8')
    except Exception as exc:
        return [f'cannot read UTF-8 HTML: {exc}'], []

    parser = Audit()
    # Track heading text by a tiny second parser pass with explicit data roles.
    parser.feed(source)
    if parser.stack:
        errors.append(f'unclosed tags: {", ".join(parser.stack[-8:])}')
    errors.extend(parser.errors)

    if not re.search(r'<meta\b[^>]*name=["\']viewport["\']', source, re.I):
        errors.append('missing viewport meta tag')
    if '<html' not in source.lower() or '</html>' not in source.lower():
        errors.append('missing complete html document')
    if re.search(r'(?:\[TODO|TODO:|\{\{[A-Z0-9_]+\}\})', source):
        errors.append('unfinished placeholder remains')
    if not re.search(r'<section\b[^>]*id=["\']conclusion["\']', source, re.I):
        errors.append('missing section id="conclusion"')

    h1s = re.findall(r'<h1\b[^>]*>(.*?)</h1>', source, re.I | re.S)
    h2s = re.findall(r'<h2\b[^>]*>(.*?)</h2>', source, re.I | re.S)
    clean = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s)).strip()
    h2text = [clean(x) for x in h2s]
    if len(h1s) != 1:
        errors.append(f'expected exactly one h1, found {len(h1s)}')
    if not h2text or h2text[0] != '结论':
        errors.append('the first h2 must be 结论')

    # Heading parser above intentionally remains structural; text extraction is simpler here.
    if not re.search(r'<p\b[^>]*class=["\'][^"\']*lead[^"\']*["\']', source, re.I):
        errors.append('missing conclusion lead paragraph (.lead)')

    if not allow_scripts and re.search(r'<script\b', source, re.I):
        errors.append('script tag found; standalone briefing reports default to no JavaScript')
    if re.search(r'<(iframe|object|embed)\b', source, re.I):
        errors.append('embedded iframe/object/embed found; keep the report self-contained')

    resource_re = re.compile(r'<(?:script|link|img|source)\b[^>]*(?:src|href)=["\']https?://', re.I)
    if not allow_remote and resource_re.search(source):
        errors.append('remote resource dependency found')

    for missing in sorted(set(parser.links) - set(parser.ids)):
        errors.append(f'internal link target missing: #{missing}')

    pre_blocks = re.findall(r'<pre\b[^>]*>', source, re.I)
    code_blocks = re.findall(r'<pre\b[^>]*class=["\'][^"\']*\bcode\b[^"\']*["\'][^>]*>\s*<code\b', source, re.I)
    if len(pre_blocks) != len(code_blocks):
        errors.append('every code block must be <pre class="code"><code>...</code></pre>')
    if pre_blocks:
        for token in ('tok-k', 'tok-s', 'tok-c', 'tok-n'):
            if f'.{token}' not in source:
                errors.append(f'missing syntax token style: .{token}')
        if 'class="tok-' not in source:
            errors.append('code blocks contain no syntax-highlighted tokens')

    svg_count = source.lower().count('<svg')
    if svg_count:
        svg_blocks = re.findall(r'<svg\b.*?</svg>', source, re.I | re.S)
        if len(svg_blocks) != svg_count:
            errors.append('unbalanced SVG blocks')
        for i, block in enumerate(svg_blocks, 1):
            if not re.search(r'<svg\b[^>]*role=["\']img["\']', block, re.I):
                errors.append(f'SVG {i} missing role="img"')
            if not re.search(r'<svg\b[^>]*aria-labelledby=', block, re.I):
                errors.append(f'SVG {i} missing aria-labelledby')
            if not re.search(r'<title\b[^>]*>\s*[^<\s].*?</title>', block, re.I | re.S):
                errors.append(f'SVG {i} missing non-empty title')
            if not re.search(r'<desc\b[^>]*>\s*[^<\s].*?</desc>', block, re.I | re.S):
                errors.append(f'SVG {i} missing non-empty desc')
            if not re.search(r'<a\b[^>]*href=["\']#', block, re.I):
                warnings.append(f'SVG {i} has no clickable evidence target')
        if 'overflow-x' not in source:
            warnings.append('diagram scroll wrapper does not declare overflow-x')
        if 'min-width' not in source:
            warnings.append('diagram SVG does not pin a readable min-width')

    empty_patterns = [r'<p[^>]*>\s*</p>', r'<tr[^>]*>\s*</tr>', r'<section[^>]*>\s*</section>']
    if any(re.search(p, source, re.I) for p in empty_patterns):
        errors.append('empty paragraph, table row, or section found')

    visible = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', ' ', source, flags=re.I | re.S)
    visible = re.sub(r'<[^>]+>', ' ', visible)
    visible = re.sub(r'\s+', ' ', visible)
    for pattern in META_PHRASES:
        if re.search(pattern, visible, re.I) and pattern not in allowed_phrases:
            errors.append(f'filler or process wording found: {pattern}')

    # Rough provenance test: reports should expose either a hash, source path, version, or endpoint.
    if not re.search(r'\b(?:sha-?256|[0-9a-f]{32,64}|\.java\b|\.kt\b|\.dex\b|https?://|/v\d+|commit|branch|版本)', source, re.I):
        warnings.append('no source path, hash, version, endpoint, or revision marker found')

    if not re.search(r'@media\s+print', source, re.I):
        warnings.append('no print stylesheet found')
    if 'font-size' in source and re.search(r'font-size\s*:\s*(?:[0-9]|1[01])px', source, re.I):
        warnings.append('font-size below 12px found; verify diagram or metadata context')

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description='Validate a standalone HTML briefing report.')
    ap.add_argument('html_file')
    ap.add_argument('--allow-scripts', action='store_true')
    ap.add_argument('--allow-remote-assets', action='store_true')
    ap.add_argument('--allow-phrase', action='append', default=[], help='literal banned phrase to allow for this report')
    args = ap.parse_args()
    path = Path(args.html_file)
    errors, warnings = check(path, args.allow_scripts, args.allow_remote_assets, args.allow_phrase)
    for warning in warnings:
        print(f'WARN {warning}')
    for error in errors:
        print(f'FAIL {error}')
    if errors:
        print(f'FAILED {path} with {len(errors)} error(s)')
        return 1
    print(f'OK {path}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
