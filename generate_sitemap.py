#!/usr/bin/env python3
"""
Sitemap generator for HOUSE, Inc. static website.
Scans for all .html files and outputs sitemap.xml with proper directory-style URLs.
"""
import os
from pathlib import Path

WEBSITE_ROOT = Path(__file__).parent
BASE_URL = "https://houseinc501c3.com"

def html_files():
    """Yield all .html files under website root, excluding .git/ and underscore-prefixed."""
    for root, dirs, files in os.walk(WEBSITE_ROOT):
        dirs[:] = [d for d in dirs if d != '.git' and not d.startswith('_') and d != 'node_modules']
        for fname in files:
            if fname.endswith('.html') and not fname.startswith('_'):
                yield Path(root) / fname

def to_sitemap_url(path):
    rel = path.relative_to(WEBSITE_ROOT)
    if rel == Path('index.html'):
        return '/'
    if rel.name == 'index.html':
        parts = rel.parts[:-1]
        if not parts:
            return '/'
        return '/' + '/'.join(parts) + '/'
    parts = rel.parts[:-1] + (rel.stem,)
    return '/' + '/'.join(parts) + '/'

def priority_for_url(url):
    if url == '/':
        return 1.0
    high = ['/mission/', '/programs/', '/apply/', '/donate/']
    med = ['/stories/', '/transparency/', '/contact/']
    if url in high:
        return 0.9
    if url in med:
        return 0.7
    return 0.6

def generate_sitemap():
    urls = []
    for f in html_files():
        url = to_sitemap_url(f)
        urls.append((url, priority_for_url(url)))

    seen = set()
    unique = []
    for u, p in urls:
        if u not in seen:
            seen.add(u)
            unique.append((u, p))

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, pri in unique:
        lines.append('  <url>')
        lines.append(f'    <loc>{BASE_URL}{url}</loc>')
        lines.append(f'    <priority>{pri}</priority>')
        lines.append('  </url>')
    lines.append('</urlset>')

    out = WEBSITE_ROOT / 'sitemap.xml'
    with open(out, 'w') as fh:
        fh.write('\n'.join(lines) + '\n')

    print(f'Generated {out}')
    print(f'URLs found ({len(unique)}):')
    for url, pri in unique:
        print(f'  {BASE_URL}{url}  [priority={pri}]')

if __name__ == '__main__':
    generate_sitemap()
