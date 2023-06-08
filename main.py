# -*- coding: utf-8 -*-


# Imports 
from bme680 import *
from machine import I2C, Pin
from time import sleep


# Initialisatie van de pins 
i2c_sda = Pin(20)
i2c_scl = Pin(21)
# Initalisatie van BME680-sensor
bme680 = BME680_I2C(I2C(0, sda=i2c_sda,scl=i2c_scl))
# Declareren van graden Celsius teken
degreecels = '\u00B0' + "C"


# Normale luchtdruk locatie (hPa) op NAP
sealevelpressure = 1013.25
# Deze variable wordt gebruikt ter correctie vd offset van de temperatuur. 
temperature_offset = -2
# Declareren van de dict om de data in op te slaan
measurement = {
  "temperature": None,
  "humidity": None,
  "pressure": None,
  "air_quality": None,
  "gas": None
}


def measureClimate():
    # Reset van de sea_level variabele op basis van eigen variabele
    if 'sealevelpressure' in locals():
        bme680.sea_level_pressure = sealevelpressure
    # Sla de waarde die gemeten is op in de dictonairy
    measurement["temperature"] = bme680.temperature
    measurement["humidity"] = bme680.humidity
    measurement["pressure"] = bme680.pressure
    measurement["air_quality"] = bme680.air
    measurement["gas"] = bme680.gas
