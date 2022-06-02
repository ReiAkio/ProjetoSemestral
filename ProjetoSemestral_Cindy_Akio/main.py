from imu import MPU6050
import time
from machine import Pin, I2C, SPI, PWM
from ssd1306 import SSD1306_SPI
from utime import sleep

#Buzzer
buzzer = PWM(Pin(15))
def playtone(frequency):
    buzzer.duty_u16(1000)
    buzzer.freq(frequency)

def bequiet():
    buzzer.duty_u16(0)

# SPI
spi = SPI(0, 10000, mosi=Pin(19), sck=Pin(18))
oled = SSD1306_SPI(128, 32, spi, Pin(17),Pin(20), Pin(16))

#I2C
i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
imu = MPU6050(i2c)

# MAIN PROJECT
def main_project():
    while True:

        acceleration = imu.accel.magnitude
        print (acceleration)
       
        if abs(acceleration) > 1.1:
            
            print("Houve uma queda")
            oled.text("Houve uma queda", 0, 0)
            oled.show()
            oled.fill(0)
            playtone(500)

        else:
            print("Esta tudo certo")
            oled.text("Esta tudo certo", 0, 0)
            oled.show()
            oled.fill(0)
            bequiet()
        time.sleep(0.2)
            
        buzzer.duty_u16(0)

# Rodando o codigo principal
main_project()