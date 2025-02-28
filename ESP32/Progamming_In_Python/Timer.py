from machine import Pin
import time

LED_PIN = 1  # Built-in LED on ESP32
led = Pin(LED_PIN, Pin.OUT)  # Set GPIO1 as an output

start_time = time.time()  # Get the start time in second

while time.time() - start_time < 10:  # Run for 10 seconds)
    led.value(0)  # Turn LED on
    time.sleep(0.5)  # Wait 0.5 second
    led.value(1)  # Turn LED off
    time.sleep(0.5)  # Wait 0.5 second

# End of program
led.value(1)  # Ensure LED is off at the end
print("Blinking stopped after {} seconds.".format(time.time() - start_time))

