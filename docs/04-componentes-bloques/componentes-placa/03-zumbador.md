# 4.1.3 Zumbador: Pulsador-sonido

## COMPONENTE:

Disponemos de dos salidas para reproducir audio, el **zumbador** y el **jack** al que podemos conectar auriculares o altavoces autoamplificados. Al conectar una clavija de audio en el jack se desconecta el zumbador.

<div class="img-row" markdown="1">
![zumbador](../../assets/images/zumbador.png "zumbador"){ width="150" }

![jack audio](../../assets/images/jack_audio.png "jack audio"){ width="227" }
</div>

Además, contamos con un potenciómetro que permite ajustar el volumen del sonido.

## BLOQUE DE PROGRAMACIÓN:

Para controlar el **zumbador** podemos usar el siguiente **bloque**:

![bloque zumbador](../../assets/images/bloque_zumbador.png "bloque zumbador"){ width="393" }

En el cual podemos cambiar su estado a encender o apagar.

## EJEMPLO: Timbre

Este ejemplo muestra cómo **controlar** el **zumbador** (actuador de sonido) utilizando un **pulsador** como **entrada**.

![Ejemplo pulsador zumbador](../../assets/images/Ejemplo_pulsador-zumbador.png "Ejemplo pulsador zumbador"){ width="655" }

**Lógica de programación:**

```
Si el pulsador es presionado (o activado):
    ➡ Entonces el zumbador suena.

Si el pulsador es liberado (o soltado):
    ➡ Entonces el zumbador deja de sonar.
```

De esta forma, el zumbador solo se activa mientras el pulsador se mantiene presionado.
