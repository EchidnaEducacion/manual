# 6.1 ¿Qué es Firmata?

Para trabajar con **EchidnaML** en la placa **EchidnaBlack** tenemos que tener **instalado** un **programa** denominado **Firmata** que permite la comunicación entre la placa y el ordenador. 

**Firmata** es un **protocolo** que facilita la **comunicación** entre **microcontroladores** y **ordenadores** de forma sencilla. Permite que el programa ejecutado en EchidnaML interactúe con la placa en tiempo real a través del puerto serie. De este modo, se establece un flujo bidireccional: la placa reporta constantemente las lecturas de sus sensores y el programa, tras procesarlas, envía las instrucciones necesarias para controlar los actuadores

![StandardFirmata](../assets/images/StandarFirmata-EchidnaBlocks.png "StandardFirmata"){ width="1000" }

En EchidnaBlack trabajamos con **StandardFirmata**, que viene **instalado** de **serie** por lo que lo normal es que no necesites hacer nada. Si necesitas volver a instalar el programa StandardFirmata en el siguiente apartado te explicamos cómo hacerlo.
