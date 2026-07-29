# Manual EchidnaBlack y EchidnaML — proyecto Zensical

Conversión a Markdown del manual publicado en <https://rea.echidna.es/manual/>.
El contenido se distribuye en páginas independientes, conserva las imágenes y
mantiene la jerarquía del manual original. Los acordeones y demás contenidos
dependientes de JavaScript se han transformado en apartados visibles y lineales.

## Requisitos

- Python 3
- `pip`

## Vista previa local

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
zensical serve
```

En Windows, active el entorno con `.venv\Scripts\activate`.
La terminal mostrará la dirección local de la vista previa.

## Generar el sitio estático

```bash
zensical build --clean
```

El sitio resultante se guarda en `site/`. Puede publicarse con cualquier
servidor web estático.

## Generar el PDF

```bash
python scripts/build_pdf.py
```

Requiere haber ejecutado antes `zensical build --clean`. El script une el
contenido de todas las páginas (en el orden y la jerarquía del `nav` de
`zensical.toml`) en un único documento y lo maqueta con
[WeasyPrint](https://weasyprint.org/) usando `scripts/print.css`: portada,
índice con numeración de página real, cabeceras de capítulo y saltos de
página solo entre capítulos y subsecciones, para que el resultado se lea
como un manual impreso y no como páginas web sueltas pegadas. Genera
`site/manual.pdf`.

En Debian/Ubuntu, WeasyPrint necesita estas bibliotecas del sistema y, si
`pip` no encuentra una rueda precompilada de `lxml` para tu Python, hacen
falta además las cabeceras de desarrollo de `libxml2`/`libxslt` para
compilarlo:

```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0 libxml2-dev libxslt1-dev
```

El flujo de GitHub Actions instala estas dependencias y genera el PDF en
cada publicación, por lo que queda disponible en `<sitio>/manual.pdf`.

## Ajustar el tamaño de las imágenes

El tamaño de cada imagen del manual (en el sitio y en el PDF) se controla
añadiendo `{ width="N" }` tras la imagen en el Markdown correspondiente. Para
decidir esos tamaños a mano existe un flujo de trabajo en dos pasos:

```bash
pip install -r requirements.txt -r scripts/requirements-worksheet.txt
python scripts/build_image_worksheet.py
```

Esto genera `image-worksheet/tamanos-imagenes.docx`, con todas las imágenes
del manual agrupadas por página, cada una seguida de una leyenda gris con su
identificador (`IMGxxx`), su tamaño nativo y su ancho actual. Abra el
documento, redimensione (arrastrando una esquina, para mantener la
proporción) las imágenes que quiera cambiar de tamaño —deje las demás tal
cual— y expórtelo o guárdelo como PDF a tamaño real (sin ajustar a página).
No edite el texto gris de las leyendas: es lo que permite volver a localizar
cada imagen en el PDF exportado.

Con ese PDF, aplique los cambios a `docs/`:

```bash
python scripts/apply_image_sizes.py ruta/al/documento-editado.pdf
```

El script mide el ancho real de cada imagen en el PDF y solo toca los
ficheros Markdown de las imágenes cuyo tamaño cambió de verdad respecto al
que tenían al generar el documento (con un margen del 3 % para redondeos de
Word/LibreOffice). Añada `--dry-run` para ver qué cambiaría sin escribir
nada. `image-worksheet/` no se versiona (está en `.gitignore`): es un
directorio de trabajo, no contenido del manual.

## Publicar en GitHub Pages

1. Suba este proyecto a un repositorio de GitHub.
2. Abra **Settings → Pages**.
3. En **Build and deployment**, seleccione **GitHub Actions**.
4. Haga un `push` a la rama `main`.

El flujo `.github/workflows/docs.yml` compilará y publicará el manual.

## Publicar en GitLab Pages

Suba el proyecto a GitLab. El archivo `.gitlab-ci.yml` compilará el sitio al
actualizar la rama predeterminada y publicará el directorio `site/`.

## Estructura

- `zensical.toml`: configuración y navegación.
- `docs/`: páginas Markdown y recursos.
- `docs/assets/images/`: imágenes originales del manual.
- `docs/assets/stylesheets/extra.css`: ajustes visuales sobrios.
- `scripts/manual_nav.py`: recorrido común del `nav` de `zensical.toml` (usado por los demás scripts).
- `scripts/build_pdf.py`: genera `site/manual.pdf` uniendo todas las páginas del sitio construido.
- `scripts/print.css`: maquetación de impresión (portada, índice, cabeceras, saltos de página) para WeasyPrint.
- `scripts/build_image_worksheet.py` / `scripts/apply_image_sizes.py`: flujo para decidir a mano el tamaño de las imágenes (ver más abajo).
- `.github/workflows/docs.yml`: publicación en GitHub Pages y generación del PDF.
- `.gitlab-ci.yml`: publicación en GitLab Pages.

## Actualización del contenido

Los ficheros Markdown son la fuente editorial. Para actualizar el manual,
edítelos directamente y ejecute `zensical serve` para revisar los cambios.

## Licencia

La obra original, de Echidna Educación, está publicada bajo
[Creative Commons Reconocimiento-CompartirIgual 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Esta adaptación mantiene la misma licencia.
