#!/usr/bin/env python3
"""Aplica a docs/*.md los tamaños de imagen decididos en el PDF exportado
desde image-worksheet/tamanos-imagenes.docx.

Uso:
    python scripts/apply_image_sizes.py ruta/al/documento-editado.pdf [--dry-run]

Empareja cada imagen del PDF con su fila del manifiesto localizando el texto
"IMGxxx" de la leyenda (situada justo debajo de cada imagen) y midiendo la
imagen más cercana por encima de esa leyenda. Solo toca docs/*.md cuando el
ancho medido difiere del que tenía el documento al generarse (más de un 3%
de margen, para no reaccionar a redondeos de LibreOffice/Word).
"""

import argparse
import json
import re
import sys
from pathlib import Path

import fitz  # PyMuPDF

from image_inventory import find_usage
from manual_nav import DOCS_DIR

ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT / "image-worksheet" / "manifest.json"

ID_RE = re.compile(r"\bIMG(\d{3})\b")
PT_TO_PX = 96 / 72
TOLERANCE = 0.03


def extract_measurements(pdf_path: Path) -> dict[str, float]:
    """Devuelve {image_id: ancho_medido_en_px} a partir del PDF."""
    doc = fitz.open(pdf_path)
    measurements = {}

    for page in doc:
        images = page.get_image_info(xrefs=True)
        text_dict = page.get_text("dict")

        captions = []
        for block in text_dict["blocks"]:
            for line in block.get("lines", []):
                line_text = "".join(span["text"] for span in line["spans"])
                m = ID_RE.search(line_text)
                if m:
                    x0, y0, x1, y1 = line["bbox"]
                    captions.append((f"IMG{m.group(1)}", x0, y0, x1, y1))

        for image_id, cx0, cy0, cx1, cy1 in captions:
            best = None
            best_gap = None
            for img in images:
                ix0, iy0, ix1, iy1 = img["bbox"]
                overlap = min(ix1, cx1) - max(ix0, cx0)
                if overlap <= 0:
                    continue
                gap = cy0 - iy1
                if gap < -5:
                    continue
                if best_gap is None or gap < best_gap:
                    best_gap = gap
                    best = img
            if best is not None:
                width_pt = best["bbox"][2] - best["bbox"][0]
                measurements[image_id] = width_pt * PT_TO_PX

    return measurements


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf_path", type=Path)
    parser.add_argument("--dry-run", action="store_true", help="Muestra los cambios sin escribirlos")
    args = parser.parse_args()

    if not args.pdf_path.exists():
        sys.exit(f"No existe {args.pdf_path}")
    if not MANIFEST_PATH.exists():
        sys.exit(f"No existe {MANIFEST_PATH}. Ejecuta antes build_image_worksheet.py.")

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    measurements = extract_measurements(args.pdf_path)

    unmatched = [e for e in manifest if e["id"] not in measurements]
    changes = []

    for entry in manifest:
        image_id = entry["id"]
        if image_id not in measurements:
            continue

        measured_px = measurements[image_id]
        # Comparamos contra el tamaño que realmente se mostró en el .docx
        # (initial_width_in), no contra el `current_width` previo de docs/:
        # ese fue el punto de partida real que el usuario pudo o no tocar.
        baseline_px = entry["initial_width_in"] * 96

        if abs(measured_px - baseline_px) / baseline_px <= TOLERANCE:
            continue  # sin cambios significativos

        new_width = round(measured_px)
        changes.append((entry, new_width))

    if not changes:
        print("No hay cambios de tamaño que aplicar.")
    else:
        print(f"{len(changes)} imagen(es) con tamaño nuevo:")
        for entry, new_width in changes:
            print(f"  {entry['id']} {entry['filename']} ({entry['md_path']}): "
                  f"{entry['current_width'] or 'auto'} -> {new_width}px")

    if unmatched:
        print(f"\nAviso: no se pudo medir {len(unmatched)} imagen(es) en el PDF "
              "(¿se borraron sus leyendas o filas?):")
        for entry in unmatched:
            print(f"  {entry['id']} {entry['filename']} ({entry['md_path']})")

    if args.dry_run or not changes:
        return

    by_file = {}
    for entry, new_width in changes:
        by_file.setdefault(entry["md_path"], []).append((entry, new_width))

    for md_path, file_changes in by_file.items():
        abs_md = DOCS_DIR / md_path
        text = abs_md.read_text(encoding="utf-8")

        # de atrás hacia adelante para no invalidar offsets dentro del mismo fichero
        edits = []
        for entry, new_width in file_changes:
            usage = find_usage(md_path, entry["src"], entry["occurrence_index"])
            if usage is None:
                print(f"  ! No se pudo relocalizar {entry['id']} en {md_path}, se omite")
                continue
            edits.append((usage, new_width))
        edits.sort(key=lambda e: e[0].match_start, reverse=True)

        for usage, new_width in edits:
            original = text[usage.match_start:usage.match_end]
            if usage.kind == "md":
                if usage.current_width:
                    updated = re.sub(r'width="\d+"', f'width="{new_width}"', original)
                else:
                    if original.rstrip().endswith("}"):
                        updated = re.sub(r'\}\s*$', f' width="{new_width}" }}', original)
                    else:
                        updated = original + f'{{ width="{new_width}" }}'
            else:  # html
                if usage.current_width:
                    updated = re.sub(r'width="\d+"', f'width="{new_width}"', original)
                else:
                    updated = re.sub(r'/?>\s*$', f' width="{new_width}" />', original)

            text = text[:usage.match_start] + updated + text[usage.match_end:]

        abs_md.write_text(text, encoding="utf-8")
        print(f"Actualizado docs/{md_path}")


if __name__ == "__main__":
    main()
