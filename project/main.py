# Imports 
from bme680 import *
from machine import I2C, Pin
from time import sleep
import random


# Initalisatie en declaratie -------------------------------------------------------------------
# Initialisatie van de pins 
I2C1_SDA_PIN = 14
I2C1_SCL_PIN = 15
# Initalisatie en declaratie van BME680-sensor
I2C1=machine.I2C(1,sda=machine.Pin(I2C1_SDA_PIN), scl=machine.Pin(I2C1_SCL_PIN), freq=400000)
bme = BME680_I2C(I2C1)
time.sleep(1)
# Data dict
measurement = {
    "device_id": 1,
    "measurement_id": None,
    "temperature": None,
    "humidity": None,
    "pressure": None,
    "air_quality": None,
    "gas": None,
    "carbon_dioxide": None
}
# Onboard LED initaliseren (enkel voor test, in het echt wordt deze uitgeschakeld om stroom te besparen!
led = Pin("LED", Pin.OUT)


# Bijstellen -----------------------------------------------------------------------------------
# Normale luchtdruk locatie (hPa) op NAP
sea_level_pressure = 1015.2
# Deze variable wordt gebruikt ter correctie vd offset van de temperatuur. 
temperature_offset = -1


# Code -----------------------------------------------------------------------------------------
def measureClimate():
    led.value(1)
    # Reset van de sea_level variabele op basis van eigen variabele
    if 'sealevelpressure' in locals():
        bme.sea_level_pressure = sea_level_pressure
    measurement["measurement_id"] = random.randint(0, 100)
    # Sla de waarde die gemeten is op in de dictonairy
    measurement["air_quality"] = calculateIAQ(bme.gas)
    measurement["temperature"] = bme.temperature
    measurement["humidity"] = bme.humidity
    measurement["pressure"] = bme.pressure
    measurement["gas"] = bme.gas
    led.value(0)


def calculateIAQ(gas):
    # Calculate the air_quality_score using temperature, humidity, and gas_resistance
    air_quality_score = 100 - (gas / 300)
    # Limit the air_quality_score to the range [0, 100]
    air_quality_score = min(max(air_quality_score, 0), 100)
    print(air_quality_score)
    return air_quality_score
    
    
while True:
    measureClimate()  
    print(measurement)
    time.sleep(3)


