#!/usr/bin/env python3
"""Genera site/manual.pdf a partir del sitio ya construido por Zensical.

Recorre el sitio en el mismo orden que el `nav` de zensical.toml, imprime
cada página con Chromium (usando el CSS de impresión del tema, que ya
oculta cabecera, pestañas y barras laterales) y une los PDF resultantes en
un único fichero.
"""

import io
import sys
import tomllib
from pathlib import Path

from playwright.sync_api import sync_playwright
from pypdf import PdfWriter

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
CONFIG_PATH = ROOT / "zensical.toml"
OUTPUT_PATH = SITE_DIR / "manual.pdf"


def flatten_nav(nav) -> list[str]:
    """Aplana el `nav` (lista de dicts título -> ruta o sublista) a rutas .md en orden."""
    paths = []
    for item in nav:
        if isinstance(item, str):
            paths.append(item)
        elif isinstance(item, dict):
            for value in item.values():
                if isinstance(value, str):
                    paths.append(value)
                else:
                    paths.extend(flatten_nav(value))
    return paths


def md_to_html(md_path: str) -> Path:
    """Aplica el esquema de URLs limpias que usa Zensical al construir el sitio."""
    relative = Path(md_path)
    if relative.name == "index.md":
        return SITE_DIR / relative.parent / "index.html"
    return SITE_DIR / relative.parent / relative.stem / "index.html"


def main() -> None:
    if not SITE_DIR.exists():
        sys.exit(f"No existe {SITE_DIR}. Ejecuta antes 'zensical build --clean'.")

    config = tomllib.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    pages = flatten_nav(config["project"]["nav"])

    writer = PdfWriter()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.emulate_media(media="print")

        for md_path in pages:
            html_path = md_to_html(md_path)
            if not html_path.exists():
                sys.exit(f"No se encontró la página construida para '{md_path}': {html_path}")

            page.goto(html_path.as_uri())
            page.wait_for_load_state("networkidle")
            pdf_bytes = page.pdf(
                format="A4",
                print_background=True,
                margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"},
            )
            writer.append(fileobj=io.BytesIO(pdf_bytes))

        browser.close()

    with OUTPUT_PATH.open("wb") as f:
        writer.write(f)

    print(f"PDF generado en {OUTPUT_PATH} ({len(pages)} páginas)")


if __name__ == "__main__":
    main()
