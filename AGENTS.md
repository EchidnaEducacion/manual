# AGENTS.md

Instrucciones para agentes de IA (Claude Code y similares) que trabajen en este repositorio.

## Qué es este proyecto

Manual técnico de la placa educativa **EchidnaBlack2** y del entorno de
programación **EchidnaML**, publicado con [Zensical](https://zensical.org/)
(generador de sitios estáticos basado en Markdown). Es una conversión a
Markdown del manual original publicado en <https://rea.echidna.es/manual/>,
creado con eXeLearning por Echidna Educación.

No es un proyecto de software: es contenido editorial. La tarea habitual no
es "programar", sino escribir, corregir o reorganizar documentación técnica
dirigida a docentes y alumnado de secundaria que usan la placa EchidnaBlack.

## Antes de escribir o editar contenido

- Lee al menos dos o tres páginas de `docs/` cercanas al tema que vas a tocar
  para calibrar tono y estructura antes de escribir nada nuevo.
- Respeta la numeración de los apartados (`# 4.1.1 Título`), que debe
  coincidir con la jerarquía definida en `nav` dentro de `zensical.toml`. Si
  añades, eliminas o reordenas una página, actualiza `nav` a la vez.
- Si una sección tiene `index.md`, debe ser el primer elemento de su lista en
  `nav` (así lo espera la característica `navigation.indexes`, activada en
  `zensical.toml`, que evita que el título de la sección aparezca duplicado
  en la barra lateral). `scripts/build_pdf.py` también asume esta convención:
  usa el `<h1>` de ese `index.md` como título del capítulo o subsección en el
  PDF.
- No alteres el contenido técnico o pedagógico del manual original (medidas,
  pines, valores de tensión, pasos de instalación) salvo que el usuario pida
  explícitamente corregir un error o actualizar una versión.

## Convenciones editoriales observadas en `docs/`

- **Idioma**: español, registro neutro-formal. Los términos clave se marcan
  en **negrita** la primera vez que aparecen en una sección.
- **Encabezados**: `#` para el título numerado de la página (coincide con el
  nombre en `nav`); `##`/`####` para subapartados.
- **Marcadores de sección** en las páginas de componentes
  (`docs/04-componentes-bloques/`): `## COMPONENTE:`,
  `## BLOQUE DE PROGRAMACIÓN:`, `## EJEMPLO: <nombre>`. Mantén este patrón
  al añadir un componente o bloque nuevo.
- **Avisos**: se destacan con `**Advertencia: ...**` o `¡ATENCIÓN!` seguidos
  de una frase directa sobre el riesgo (p. ej. quemar un componente, perder
  un proyecto no guardado).
- **Sin emojis**: no se usan en ningún sitio del manual (se quitaron los que
  había en marcadores de sección y avisos porque WeasyPrint no los renderiza
  bien en el PDF). No los reintroduzcas.
- **Imágenes**: viven en `docs/assets/images/` (sin subcarpetas por
  apartado) y se referencian con ruta relativa y el `title` repitiendo el
  `alt`:
  `![Descripción](../../assets/images/Nombre_archivo.png "Descripción")`.
  Si añades una imagen nueva, colócala directamente en esa carpeta.
- **Tamaño de imagen explícito**: cuando una imagen necesita un ancho fijo
  (en vez del automático del tema), se añade con `attr_list`:
  `![Alt](../ruta.png "Alt"){ width="320" }` (sin `:` inicial; así ya
  funciona en este proyecto). El usuario decide estos anchos con el flujo de
  `scripts/build_image_worksheet.py` / `apply_image_sizes.py` (ver
  README.md); no inventes ni cambies estos valores por tu cuenta salvo que
  te lo pida explícitamente.
- Para poner una imagen junto a otra imagen o junto a un párrafo corto de
  texto (en vez de apiladas a todo el ancho), envuélvelas en
  `<div class="img-row" markdown="1">`/`<div class="img-text-row" markdown="1">`
  (clases ya definidas en `extra.css` y `print.css`). Cada imagen o párrafo
  debe quedar en su propio párrafo (línea en blanco entre ellos): si dos
  imágenes comparten un mismo `<p>`, el flex de `.img-row` no las pone en
  fila (aprendido a base de probarlo).
- **Índices de sección** (`index.md` de cada carpeta numerada): listan los
  subapartados con enlaces relativos y numeración, sin más.
- **Tablas complejas** (con colspan, anchos o formato heredado de
  eXeLearning): se dejan en HTML embebido tal cual, gracias a las
  extensiones `attr_list` y `md_in_html` activadas en `zensical.toml`. No
  las reescribas a Markdown salvo que se pida simplificarlas.
- **Pseudocódigo** ("Lógica de programación" con `SI ... / SI NO ...` y
  `-->`): siempre en un bloque de código con ``` ``` ``` (extensión
  `fenced_code`, activada en `zensical.toml`), con 4 espacios por nivel de
  indentación y sin escapar `>` ni comillas dentro del bloque. No uses
  indentación suelta para que "parezca" código: por debajo de 4 espacios no
  se renderiza como bloque en la web, y en el PDF depende de `print.css`
  (que solo estiliza `pre`/`code` reales).

## Estructura del repositorio

- `zensical.toml`: configuración del sitio y navegación (`nav`). Es la
  fuente de verdad del orden y la jerarquía de páginas.
- `docs/`: contenido Markdown, organizado en carpetas numeradas por
  capítulo (`01-introduccion/`, `02-placa/`, etc.).
- `docs/assets/images/`: imágenes originales del manual.
- `docs/assets/stylesheets/extra.css`: ajustes visuales sobrios del tema
  (incluye `.img-row`/`.img-text-row`, ver más arriba).
- `scripts/manual_nav.py`: recorrido común del `nav` (profundidad, orden de
  lectura, rutas), usado por todos los scripts de `scripts/`.
- `scripts/build_pdf.py` + `scripts/print.css`: generan `site/manual.pdf`
  uniendo el contenido de todas las páginas ya construidas (en el orden y la
  jerarquía del `nav`) en un único documento y maquetándolo con WeasyPrint
  (portada, índice con página real, cabeceras de capítulo, saltos de página
  solo entre capítulos/subsecciones). Requiere que `site/` ya exista
  (`zensical build --clean` previo). No reescribas esto para volver a
  "imprimir página por página": esa fue la primera versión y dejaba muchas
  páginas casi en blanco por el salto forzado entre cada fichero .md.
- `.github/workflows/docs.yml`: publicación en GitHub Pages al hacer push a
  `main`; también instala las dependencias de sistema de WeasyPrint y
  ejecuta `scripts/build_pdf.py` para que el PDF quede publicado junto al
  sitio.
- `.gitlab-ci.yml`: publicación en GitLab Pages (no genera el PDF).
- `requirements.txt`: fija las versiones de `zensical`, `weasyprint` y `lxml`.
- `scripts/image_inventory.py`: localiza todas las imágenes usadas en
  `docs/*.md` (Markdown y `<img>` HTML), en orden de lectura del manual.
- `scripts/build_image_worksheet.py`: genera
  `image-worksheet/tamanos-imagenes.docx` (una imagen por fila, con una
  leyenda `IMGxxx` con su tamaño nativo y actual) y
  `image-worksheet/manifest.json`. El usuario redimensiona a mano en Word/
  LibreOffice y exporta a PDF.
- `scripts/apply_image_sizes.py`: dado ese PDF ya editado, mide el ancho
  real de cada imagen (empareja por la leyenda `IMGxxx`, vía PyMuPDF) y
  actualiza el `{ width="N" }` en `docs/*.md`, pero solo de las imágenes
  cuyo tamaño cambió de verdad respecto al que tenían al generar el
  documento (margen del 3 %, para no reaccionar a redondeos). Admite
  `--dry-run`.
- `scripts/requirements-worksheet.txt`: dependencias de ese flujo
  (`python-docx`, `pymupdf`, `pillow`) — no las mezcles con
  `requirements.txt`, que es el que usa la pipeline de publicación y no
  las necesita.
- `image-worksheet/`: directorio de trabajo de ese flujo, no versionado
  (está en `.gitignore`). No es contenido del manual.

## Cómo comprobar los cambios

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
zensical serve
```

Antes de dar por terminado un cambio de contenido, ejecuta `zensical serve`
(o `zensical build --clean` si prefieres una comprobación no interactiva) y
revisa que la página renderiza bien: imágenes visibles, enlaces internos
resueltos y la posición correcta en la navegación lateral.

## Licencia

El contenido original está bajo
[Creative Commons Reconocimiento-CompartirIgual 4.0](https://creativecommons.org/licenses/by-sa/4.0/),
igual que esta adaptación. Cualquier contenido nuevo que se añada debe ser
compatible con esta licencia.
