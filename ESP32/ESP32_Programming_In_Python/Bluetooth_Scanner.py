import bluetooth
import time
from micropython import const

# Define IRQ constants manually
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_COMPLETE = const(6)

# Initialize Bluetooth
ble = bluetooth.BLE()
ble.active(True)

# Store found devices to avoid duplicates
found_devices = set()

def bt_callback(event, data):
    if event == _IRQ_SCAN_RESULT:  # Device found
        addr_type, addr, adv_type, rssi, adv_data = data
        mac = ":".join("{:02x}".format(b) for b in addr)
        
        # Print only if the device is new
        if mac not in found_devices:
            found_devices.add(mac)
            print(f"📡 Found Device - MAC: {mac}, RSSI: {rssi} dBm")

    elif event == _IRQ_SCAN_COMPLETE:  # Scan finished
        print("✅ Bluetooth Scan Complete!")
        ble.gap_scan(None)  # Ensure scanning is stopped

def scan_ble(duration=20):  # Scan for 20 seconds
    print("\n🔍 Scanning for Bluetooth devices...")
    ble.gap_scan(duration * 1000, 30000, 30000)  # Scan for 'duration' seconds
    ble.irq(bt_callback)
    time.sleep(duration)  # Wait for scanning to complete
    ble.gap_scan(None)  # Stop scanning explicitly

# Start Bluetooth scanning (only once)
scan_ble()
