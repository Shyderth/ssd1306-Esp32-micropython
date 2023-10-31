# ssd1306-Esp32-micropython
En este ejemplo se utilizan algunas de las funciones basicas de la libreria ssd1306 para controlar una pantalla oled, de dimensiones 128x64 px, por comunicacion I2C. Para este caso, hacemos uso de la funcion ``oled.text()`` y ``oled.show()`` para indicar y mostrar el texto deseado. A su vez se hace uso de la funcion ``oled.rect()`` para crear un rectangulo sin relleno el cual puede desplazarse hacia la derecha o izquierda utilizando dos pulsadores.
## Consideraciones:
* Es necesario corroborar que la pantalla Oled cuente con el controlador adecuado (ssd1306), si no es el caso el codigo no funcionará.
* Los pulsadores utilizados estan en configuración Pull-Down, por tanto el microcontrolador lee un '1' lógico cuando el pulsador es presionado.
* La funcion ``oled.rect()`` recibe como parametros las coordenadas X, Y, además del alto y el ancho en pixeles del rectangulo que se desea dibujar.
