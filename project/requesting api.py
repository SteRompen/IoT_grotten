

import urequests as requests
import json
#make a extra file called secrets and specifty your SSID and PASSWORD. 

import network
import secrets
import time
import machine
led = machine.Pin('LED', machine.Pin.OUT) 

# The WLAN class represents the wireless LAN interface and provides methods
# and attributes to interact with the Wi-Fi functionality of the device.
wlan = network.WLAN(network.STA_IF)

# Connect to the Wi-Fi network
try:
    wlan.active(True)
    time.sleep(2)
    wlan.connect(secrets.SSID , secrets.PASSWORD)
    print("Connecting to", secrets.SSID)
    # zas long as its not connected, it stays in the loop
    while not wlan.isconnected():
        pass
    print("Connected to", secrets.SSID)
    led.on()
    print("Connection status:", True)
except Exception as e:
    print("Connection failed:", e)
    print("Connection status:", False)
    
    
# Print the network settings
if wlan.isconnected():
    print("Connected to network:", wlan.config("essid"))
    print("IP address:", wlan.ifconfig()[0])
    print("Subnet mask:", wlan.ifconfig()[1])
    print("Gateway:", wlan.ifconfig()[2])
    print("DNS server:", wlan.ifconfig()[3])
else:
    print("Not connected to any network")

time.sleep(10)

api_url = "http://api.weatherstack.com/current"
api_key = "f9fc9322c6c71f1f511ba6b44b522be3"
query = input("Enter City? ")

response = requests.get(f"{api_url}?access_key={api_key}&query={query}")
print(response)
if response.status_code == 200:
    print("API request successful")
else:
    print("API request failed")
    print(response.json())

json_data_dic = response.json()

temperature = json_data_dic["location"]
location = json_data_dic["location"]

print(f"In {location} is het nu {temperature} graden ")
print("holl")
