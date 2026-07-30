# 8.1 GNU/Linux

**EchidnaML** funciona en distribuciones **GNU/Linux** de **64 bits** basadas en **Debian**, como Ubuntu, Linux Mint o MAX.

**Descargas disponibles:**

- [echidnaml_1.6.0_amd64.deb](https://github.com/EchidnaEducacion/echidnaml-releases/releases/download/v1.6.0/echidnaml_1.6.0_amd64.deb)
- [echidnaml_1.6.0-ubuntu-24.04_amd64.deb](https://github.com/EchidnaEducacion/echidnaml-releases/releases/download/v1.6.0/echidnaml_1.6.0-ubuntu-24.04_amd64.deb)
- [EchidnaML-1.6.0.AppImage](https://github.com/EchidnaEducacion/echidnaml-releases/releases/download/v1.6.0/EchidnaML-1.6.0.AppImage)

**¿Qué archivo debo descargar?**

- Si utilizas Ubuntu (20.04, 22.04), MAX o Linux Mint, usa `echidnaml_1.6.0_amd64.deb`.
- Si tu sistema operativo es Ubuntu 24.04, usa `echidnaml_1.6.0-ubuntu-24.04_amd64.deb`.
- Si utilizas otra distribución o prefieres una versión portátil, la mejor opción es `EchidnaML-1.6.0.AppImage`.

## Instrucciones de instalación

### A- Instalación mediante paquete .deb

**Opción gráfica:**

1. Haz doble clic sobre el archivo descargado.
2. Pulsa «Instalar».
3. Introduce tu contraseña cuando se solicite.

**Opción mediante terminal de comandos:**

Abre una terminal de comandos y colócate en el directorio donde esté el archivo .deb. La instalación se hace así:

```
sudo apt install ./echidnaml_1.6.0_amd64.deb
```

### B- Ejecución de la versión AppImage

1. Descarga el archivo.
2. Activa el permiso de ejecución (esto solo tienes que hacerlo la primera vez).
3. Haz doble clic para iniciar la aplicación.

Puedes activar el permiso de ejecución de dos maneras:

**Opción gráfica:**

- Haz clic derecho sobre el archivo y selecciona Propiedades.
- Dirígete a la pestaña Permisos y marca la casilla "Permitir ejecutar el archivo como un programa" (o similar, dependiendo de tu distribución).
- Cierra la ventana y haz doble clic sobre el icono para iniciar EchidnaML.

**Opción mediante terminal de comandos:**

Abre una terminal de comandos y colócate en el directorio donde esté el archivo AppImage. Ejecuta la siguiente instrucción:

```
sudo chmod +x EchidnaML-1.6.0.AppImage
```
