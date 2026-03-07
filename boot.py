"""The code is taken from (https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/)"""


try:
  import usocket as socket    # usocket is MicroPython’s lightweight socket module
except:
  import socket               # If unavailable, it falls back to standard Python’s socket

from machine import Pin       # GPIO module 
import network

import esp                    # Disable ESP debug logs
esp.osdebug(None)    

import gc                     # Garbage collector to save RAM
gc.collect()


# ---- CONNECT TO WIFI ----
ssid = 'REPLACE_WITH_YOUR_SSID'          
password = 'REPLACE_WITH_YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)  # This connects your ESP to your home router

station.active(True)        # active(True) turns Wi‑Fi on

station.connect(ssid, password)  # Connects

while station.isconnected() == False:  # This is a blocking loop, so nothing else runs until Wi‑Fi is ready.
 pass

print('Connection successful')
print(station.ifconfig())  # (IP, subnet mask, gateway, DNS)

led = Pin(2, Pin.OUT)  # GPIO 2 as an output
