# 2.4 Pines de entrada- salida

![Pines entrada-salida](../assets/images/Pines_I-O.jpg "Pines entrada-salida")

Los **pines** de **entrada/salida** (I/O) son **conexiones** que nos permiten conectar dispositivos adicionales a la placa, actuando como entradas (sensores) o salidas (actuadores).

- Cuando funcionan como **entrada** reciben información de sensores externos.
- Cuando funcionan como **salida**, envían señales desde la placa para controlar actuadores externos.

La placa cuenta con **tres pines digitales** de entrada/salida  (D4, D7, D8) y **uno analógico** (A2), a los que podemos conectar una gran variedad de componentes, como servomotores, sensores de distancia infrarrojos, sensores de humedad de suelo, etc.

Cada pin de entrada/salida cuenta con una conexión a 0 V (G), 5 V (+), y el pin de señal (I/O).

#### **Selector de alimentación**

Cerca de estos pines de entrada/salida se encuentra un selector de alimentación que permite elegir de dónde reciben energía estos pines moviendo un jumper entre dos posiciones:

**Posición 5v**

En la posición de salida 5V, la corriente proviene del regulador de tensión interno de la placa, proporcionando un voltaje estable para componentes que no requieran mucha potencia.

**Limitación de Corriente:** Esta salida está destinada únicamente a la alimentación de componentes que no requieran mucha potencia. No se recomienda su uso si los componentes externos superan un consumo total de 300 mA, ya que hacerlo podría sobrecargar el regulador interno de la placa, con el riesgo de dañarlo.

**Posición Vin**

En la posición Vin, la alimentación llega desde una fuente externa conectada al jack, lo que resulta más seguro cuando se utilizan actuadores que requieren mayor potencia.
