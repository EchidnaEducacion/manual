# 9. PREGUNTAS FRECUENTES

En este apartado respondemos algunas preguntas que se dan con cierta frecuencia y que pueden resultar de ayuda.

## 9.1 Qué requisitos técnicos necesito

Para trabajar con EchidnaML se requiere un ordenador de escritorio o portátil con prestaciones básicas. En algunas distribuciones de software libre educativo viene instalada por defecto. Este software no es compatible con Chromebooks, dispositivos móviles ni tablets.

Se recomienda disponer, como mínimo, de un ordenador con las siguientes características: procesador x86_64 o ARM64 de 4 núcleos a 2GHz, 8 GB de memoria RAM y 5 GB de espacio libre en disco para la instalación y ejecución del software.

EchidnaML es compatible con los principales sistemas operativos de escritorio:

- Windows: Windows 10 (64 bits) Windows 11 (64 bits)
- macOS (versiones 14 en adelante)
- Linux (distribuciones basadas en Debian, 64 bits)

Se recomienda mantener el sistema operativo actualizado y disponer de permisos de instalación para garantizar el correcto funcionamiento del programa y la comunicación con la placa EchidnaBlack.

## 9.2 El programa no detecta la placa

Si al abrir EchidnaML el programa no detecta la placa se puede deber a:

**1. EchidnaBlack no tiene instalado el Firmware StandardFirmata:**

Aunque el firmware viene instalado de serie alguien puede haber escrito otro programa. Si es así debemos instalar el programa StandardFirmata tal como se especifica en el apartado 6 de esta guía.

**2. Nuestro ordenador no reconoce el puerto USB al que se conecta EchidnaML:**

Para que EchidnaBlack se pueda comunicar con nuestro PC es necesario que nuestro sistema operativo (SO) le dé permiso de acceso al puerto serie (USB) y que tenga el driver del controlador de comunicación (CH340) instalado.

**2.1 Driver de comunicación:**

Echidna Black utiliza el chip CH340, por lo que dependiendo del SO necesitarás instalar el controlador “[Driver CH341](https://www.wch-ic.com/downloads/ch341ser_exe.html)”

- GNU Linux: En caso de que seas usuario Linux, no debería ser necesario instalar el driver. [Si necesitas el driver para GNU Linux](https://www.wch-ic.com/download/file?id=177).
- macOS: [Aquí tienes acceso al driver para MAC](https://www.wch-ic.com/download/file?id=178).
- Windows: [Aquí tienes acceso al driver para Windows](https://www.wch-ic.com/download/file?id=65).

**2.2 Permiso de acceso al puerto serie:**

Dependiendo del SO es necesario dar o no permisos de acceso al puerto serie. Si ya has instalado el IDE de Arduino, estos permisos deberían estar ya dados.

**GNU Linux:** Si no tuvieras acceso al puerto serie puede que tengas que darle permiso desde una terminal usando el comando: sudo usermod -a -G dialout «usuario». Luego es necesario salir de la sesión y volver a entrar para que los cambios se hagan efectivos.

**macOS**: por defecto ya tenemos acceso al puerto serie.

**Windows**: por defecto ya tenemos acceso al puerto serie.

## 9.3 Puedo conectar la placa una vez abierto programa

Lo más recomendable es conectar la placa EchidnaBlack2 al ordenador antes de abrir el entorno de programación EchidnaML. Esto asegura una detección rápida y que no perdamos el trabajo realizado.

Si ya has abierto el programa EchidnaML y quieres conectar la placa posteriormente:

1.  Conecte la placa al ordenador mediante el cable USB.
2.  Para iniciar la detección, debe hacer clic en el icono USB (o el icono de conexión) dentro de la interfaz.

**Advertencia: Guardar el Trabajo**

Debe tener en cuenta que el proceso de detección y conexión reinicia el entorno de trabajo, provocando la pérdida de cualquier proyecto no guardado. Por esta razón, guarda siempre tu proyecto en el ordenador antes de iniciar el proceso de detección para evitar la pérdida de trabajo y poder recuperarlo.

## 9.4 El joystick registra valores mínimos muy altos y/o máximos muy bajos

En ocasiones el capuchón del joystick viene insertado muy profundamente en el eje, lo que provoca que choque contra la base y no haga todo el recorrido. Prueba a sacarlo un poco hacia arriba.

## 9.5 Que diferencias hay entre EchidnaBlack y EchidnaBlack2

Si tienes una EchidnaBlack debes saber que casi todo lo que se cuenta en este manual es válido para tu placa.

El software EchidnaML detecta que versión de placa estamos usando y ajusta los bloques a las características de la misma.

La principal diferencia entre las placas es la incorporación del acelerómetro por I2C en la nueva placa que ha hecho que algunos pines se reajusten:

<table style="width: 100%;" data-border="1">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<tbody>
<tr class="odd">
<td style="width: 21.7077%"></td>
<td style="width: 37.7667%"><strong>EchidnaBlack</strong></td>
<td style="width: 40.5255%"><strong>EchidnaBlack2</strong></td>
</tr>
<tr class="even">
<td style="width: 21.7077%"><p><strong>Acelerómetro</strong></p></td>
<td style="width: 37.7667%">Conectado a A2, A3<br />
Eje x, y</td>
<td style="width: 40.5255%">Conectado a A4, A5<br />
Comunicación I2C<br />
Eje x, y, z</td>
</tr>
<tr class="odd">
<td style="width: 21.7077%"><strong>LDR</strong></td>
<td style="width: 37.7667%">Conectada a A5</td>
<td style="width: 40.5255%">Conectada a A3</td>
</tr>
<tr class="even">
<td style="width: 21.7077%"><strong>Pines MkMk</strong></td>
<td style="width: 37.7667%">A0, A1, A3, A3, A6, A7, D2, D3</td>
<td style="width: 40.5255%">A0, A1, A3, A3, A6, A7, D2, D3</td>
</tr>
<tr class="odd">
<td style="width: 21.7077%"><strong>Pines I/O</strong></td>
<td style="width: 37.7667%">A4, D4, D7, D8</td>
<td style="width: 40.5255%">A2, D4, D7, D8</td>
</tr>
<tr class="even">
<td style="width: 21.7077%"><strong>Pines I2C</strong></td>
<td style="width: 37.7667%">No tiene</td>
<td style="width: 40.5255%">A4,A5</td>
</tr>
</tbody>
</table>

## 9.6 Qué tensiones soporta la placa

#### Alimentación por USB-C (Recomendada para la mayoría de usos)

Esta es la forma más sencilla, y común de usar la placa, mediante un cable USB-C conectado a un ordenador o a un cargador.

Características:

- La placa recibe una tensión de 5 V y suficiente energía para las funciones básicas.
- Tensión de uso: Toda la placa recibe una tensión regulada y estable de 5V.
- Límite de energía: Es suficiente para las funciones básicas y la mayoría de sensores pequeños (generalmente con un límite de 500 mA).
- Protección: Cuenta con un fusible rearmable que se desconecta si hay un consumo excesivo.

#### Alimentación por Jack (Recomendada para proyectos grandes o autónomos)

La usamos cuando queremos conectar elementos con mucha potencia, como varios servomotores, o para proyectos autónomos.

Características:

- Tensión de uso: La placa recibe una tensión regulada y estable de 5V.
- Límite de energía: Es suficiente para las funciones básicas y la mayoría de sensores (generalmente con un límite de 1000 mA).
- Protección: Cuenta con un fusible rearmable que se desconecta si hay un consumo excesivo.

#### Selector de Alimentación I/O

Este jumper te permite elegir qué tensión quieres enviar a los pines de entrada/salida de la placa (I/O, concretamente A2, D4, D7, D8) que usarán los componentes externos.

**Selector alimentación 5V:**

En el caso de querer alimentar las I/O desde los 5 Volts procedentes del regulador integrado, el selector tiene que estar colocado como indica la imagen de la izquierda. Aconsejado para sensores externos que necesiten una tensión estabilizada.

¡No utilizar la alimentación 5 Volts cuando los dispositivos conectados consuman más de 500 mA!. De lo contrario sobrepasaríamos la capacidad del regulador.

**Selector alimentación Vin (Alimentación externa):**

Aconsejado para alimentar servos u otros dispositivos conectados a I/O que necesiten una tensión mayor de 5 Volts.

¡ATENCIÓN!

Si tu alimentador externo tiene una tensión superior a la que soportan tus componentes conectados a I/O (que a menudo son 5 Volts), ¡puedes quemarlos inmediatamente!
