#!/usr/bin/env python3
"""
build.py — Genera presentacion-build.html con el contenido de slides.md incrustado.
El fichero resultante se puede abrir directamente en el navegador sin servidor local.

Uso: python3 build.py
"""

import re

with open("slides.md", encoding="utf-8") as f:
    slides = f.read()

with open("presentacion.html", encoding="utf-8") as f:
    html = f.read()

inline = (
    '<section data-markdown data-separator="^---$" '
    'data-separator-notes="^Note:" data-charset="utf-8">\n'
    '  <textarea data-template>\n'
    + slides +
    '\n  </textarea>\n'
    '</section>'
)

result = re.sub(
    r'<section\s+data-markdown="slides\.md"[^>]*>\s*</section>',
    inline,
    html
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(result)

print("OK → index.html")
