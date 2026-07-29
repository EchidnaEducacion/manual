"""Inventario de imágenes usadas en docs/*.md, en orden de lectura del manual.

Detecta tanto la sintaxis Markdown `![alt](src "title"){ width="N" }` como
las etiquetas `<img src="..." ...>` embebidas en HTML (usadas en algunas
tablas). Lo usan build_image_worksheet.py (genera el documento de trabajo) y
apply_image_sizes.py (aplica los tamaños que se decidan en ese documento).
"""

import re
from dataclasses import dataclass
from pathlib import Path

from manual_nav import DOCS_DIR, load_nav, ordered_pages

MD_IMAGE = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+"(?P<title>[^"]*)")?\)'
    r'(?:\{(?P<attrs>[^}]*)\})?'
)
HTML_IMAGE = re.compile(r'<img\s+(?P<attrs>[^>]*?)/?>')
ATTR = re.compile(r'(?P<key>[\w-]+)\s*=\s*"(?P<value>[^"]*)"')
WIDTH_IN_ATTRS = re.compile(r'width\s*=\s*"(?P<value>\d+)"')


@dataclass
class ImageUsage:
    image_id: str
    md_path: str            # ruta relativa a docs/, p.ej. "04-.../01-ledes.md"
    src: str                 # tal como aparece en el fichero fuente
    kind: str                 # "md" o "html"
    match_start: int
    match_end: int
    occurrence_index: int     # nº de vez que aparece este mismo src en el fichero (0-based)
    alt: str
    title: str
    current_width: int | None
    file_path: Path           # ruta absoluta al fichero de imagen


def _parse_html_attrs(attrs_str: str) -> dict:
    return {m.group("key"): m.group("value") for m in ATTR.finditer(attrs_str)}


def iter_usages_in_file(md_relpath: str):
    """Genera ImageUsage (sin image_id) en el orden en que aparecen en el fichero."""
    abs_md = DOCS_DIR / md_relpath
    text = abs_md.read_text(encoding="utf-8")

    events = []
    for m in MD_IMAGE.finditer(text):
        width = None
        if m.group("attrs"):
            wm = WIDTH_IN_ATTRS.search(m.group("attrs"))
            if wm:
                width = int(wm.group("value"))
        events.append((
            m.start(), m.end(), "md", m.group("src"),
            m.group("alt") or "", m.group("title") or "", width,
        ))

    for m in HTML_IMAGE.finditer(text):
        attrs = _parse_html_attrs(m.group("attrs"))
        if "src" not in attrs:
            continue
        width = int(attrs["width"]) if "width" in attrs and attrs["width"].isdigit() else None
        events.append((
            m.start(), m.end(), "html", attrs["src"],
            attrs.get("alt", ""), attrs.get("title", ""), width,
        ))

    events.sort(key=lambda e: e[0])

    occurrence_counts = {}
    for start, end, kind, src, alt, title, width in events:
        image_path = (abs_md.parent / src).resolve()
        occurrence_index = occurrence_counts.get(src, 0)
        occurrence_counts[src] = occurrence_index + 1
        yield ImageUsage(
            image_id="",
            md_path=md_relpath,
            src=src,
            kind=kind,
            match_start=start,
            match_end=end,
            occurrence_index=occurrence_index,
            alt=alt,
            title=title,
            current_width=width,
            file_path=image_path,
        )


def find_usage(md_path: str, src: str, occurrence_index: int) -> ImageUsage | None:
    """Vuelve a localizar una aparición concreta releyendo el fichero ahora mismo
    (no reutiliza offsets guardados, por si el fichero cambió mientras tanto)."""
    for usage in iter_usages_in_file(md_path):
        if usage.src == src and usage.occurrence_index == occurrence_index:
            return usage
    return None


def build_inventory() -> list[ImageUsage]:
    nav, _ = load_nav()
    pages = ordered_pages(nav, include_home=True)

    usages = []
    counter = 0
    for _depth, md_path in pages:
        for usage in iter_usages_in_file(md_path):
            counter += 1
            usage.image_id = f"IMG{counter:03d}"
            usages.append(usage)
    return usages
