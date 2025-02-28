import network
import usocket
import uos

# Wi-Fi Credentials
STA_SSID = "Connected_Wifi_name"
STA_PASSWORD = "Connected_Wifi_password"

# Set up ESP32 as a Wi-Fi Station (Client)
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(STA_SSID, STA_PASSWORD)

while not wifi.isconnected():
    pass  # Wait for connection

print("Connected to:", wifi.ifconfig())

# Set up ESP32 as an Access Point (Repeater)
AP_SSID = "ESP32_Extender"
AP_PASSWORD = "12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=AP_SSID, password=AP_PASSWORD)

print("Repeater active:", ap.ifconfig())

# Basic NAT Function - Forward packets from AP to STA (Experimental)
def forward_packets():
    addr = usocket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = usocket.socket()
    s.bind(addr)
    s.listen(5)

    while True:
        conn, client_addr = s.accept()
        request = conn.recv(1024)
        print("Packet:", request)
        conn.send("HTTP/1.1 200 OK\nContent-Type: text/plain\n\nRepeater is Working!")
        conn.close()

# Start packet forwarding (Experimental)
forward_packets()
