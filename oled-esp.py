from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c)

bt1 = Pin(12, Pin.IN)
bt2 = Pin(13, Pin.IN)
bt3 = Pin(34, Pin.IN)
bt4 = Pin(35, Pin.IN)

oled.text('Hola Mundo!', 10, 10)
oled.show()
time.sleep(1)
oled.text('Ejemplo Basico', 6, 25)
oled.show()
time.sleep(1)
oled.text("Oled ssd-1306", 10, 45)
oled.show()
time.sleep(1)

oled.fill(0)

x = 28
y = 16
w = 40
h = 30


while True :
    if bt1.value() :
        x-=4
        if(x<-w):
            x=oled_width-1
        
    if bt2.value():
        x+=4
        if(x>oled_width-1):
            x=-w
            
    if bt3.value():
        y+=2
        
    if bt4.value():
        y-=2
    
    oled.rect(x ,y ,w ,h ,1)
    oled.show()
    oled.fill(0)


