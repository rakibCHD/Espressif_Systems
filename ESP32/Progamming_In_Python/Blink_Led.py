from machine import Pin
import time

LED_PIN = 1  # Built-in LED on ESP32

led = Pin(LED_PIN, Pin.OUT)  # Set GPIO2 as an output

while True:
    led.value(0)  # Turn LED on
    time.sleep(0.5)  # Wait 2 second
    led.value(1)  # Turn LED off
    time.sleep(0.5)  # Wait 0.5 second
