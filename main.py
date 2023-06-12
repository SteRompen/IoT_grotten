# Imports 
from bme680 import *
from machine import I2C, Pin
from time import sleep


# Initalisatie en declaratie -------------------------------------------------------------------
# Initialisatie van de pins 
I2C1_SDA_PIN = 14
I2C1_SCL_PIN = 15
# Initalisatie en declaratie van BME680-sensor
i2c1=machine.I2C(1,sda=machine.Pin(I2C1_SDA_PIN), scl=machine.Pin(I2C1_SCL_PIN), freq=400000)
bme = BME680_I2C(i2c1)
time.sleep(1)
# Data dict
measurement = {
  "temperature": None,
  "humidity": None,
  "pressure": None,
  "air_quality": None,
  "gas": None
}
# Onboard LED initaliseren (enkel voor test, in het echt wordt deze uitgeschakeld om stroom te besparen!
led = Pin("LED", Pin.OUT)

# Bijstellen -----------------------------------------------------------------------------------
# Normale luchtdruk locatie (hPa) op NAP
sealevelpressure = 1013.25
# Deze variable wordt gebruikt ter correctie vd offset van de temperatuur. 
temperature_offset = -2

# Code -----------------------------------------------------------------------------------------
def measureClimate():
    led.value(1)
    # Reset van de sea_level variabele op basis van eigen variabele
    if 'sealevelpressure' in locals():
        bme.sea_level_pressure = sealevelpressure
    # Sla de waarde die gemeten is op in de dictonairy
    measurement["temperature"] = bme.temperature
    measurement["humidity"] = bme.humidity
    measurement["pressure"] = bme.pressure
    # measurement["air_quality"] = bme.air
    measurement["gas"] = bme.gas
    led.value(0)


while True:
    measureClimate()  
    print(measurement)
    time.sleep(3)

