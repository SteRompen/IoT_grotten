from bme680 import *
from machine import I2C, Pin
import time

# I2C Interface, genuine Micropython
I2C0_SDA_PIN = 14
I2C0_SCL_PIN = 15

i2c0=machine.I2C(1,sda=machine.Pin(I2C0_SDA_PIN), scl=machine.Pin(I2C0_SCL_PIN), freq=400000)





bme = BME680_I2C(i2c0)
time.sleep(1)


for _ in range(3):
    print(bme.temperature, bme.humidity, bme.pressure, bme.gas)
    time.sleep(1)
