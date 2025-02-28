import network
import socket
from machine import Pin

LED_PIN = 1  # Change to your LED pin
led = Pin(LED_PIN, Pin.OUT)

# Connect to Wi-Fi
SSID = "Connected_Wifi_name"
PASSWORD = "Connected_Wifi_password"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(SSID, PASSWORD)

while not wifi.isconnected():
    pass  # Wait for connection

print("Connected to Wi-Fi:", wifi.ifconfig())

# HTML Web Page
def webpage():
    state = "ON" if led.value() == 0 else "OFF"
    return f"""<!DOCTYPE html>
<html>
<head>
<title>ESP32 LED Control</title>
</head>
<body>
<h2>ESP32 Web LED Control</h2>
<p>LED is currently: <b>{state}</b></p>
<a href="/on"><button>Turn ON</button></a>
<a href="/off"><button>Turn OFF</button></a>
</body>
</html>"""

# Create Web Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 80))
server.listen(5)

while True:
    conn, addr = server.accept()
    request = conn.recv(1024).decode()
    
    if "/on" in request:
        led.value(0)
    elif "/off" in request:
        led.value(1)
    
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n" + webpage())
    conn.close()
