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

En Debian/Ubuntu, WeasyPrint necesita estas bibliotecas del sistema:

```bash
sudo apt install libpango-1.0-0 libpangoft2-1.0-0 libharfbuzz-subset0
```

El flujo de GitHub Actions instala estas dependencias y genera el PDF en
cada publicación, por lo que queda disponible en `<sitio>/manual.pdf`.

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
- `scripts/build_pdf.py`: genera `site/manual.pdf` uniendo todas las páginas del sitio construido.
- `scripts/print.css`: maquetación de impresión (portada, índice, cabeceras, saltos de página) para WeasyPrint.
- `.github/workflows/docs.yml`: publicación en GitHub Pages y generación del PDF.
- `.gitlab-ci.yml`: publicación en GitLab Pages.

## Actualización del contenido

Los ficheros Markdown son la fuente editorial. Para actualizar el manual,
edítelos directamente y ejecute `zensical serve` para revisar los cambios.

## Licencia

La obra original, de Echidna Educación, está publicada bajo
[Creative Commons Reconocimiento-CompartirIgual 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
Esta adaptación mantiene la misma licencia.
