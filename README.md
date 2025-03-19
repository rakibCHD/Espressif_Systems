# Espressif_Systems
# Some types of sample ESP Boards with working functionality.
# Supported Boards & Specifications:

# --> ESP32 (Dual-core, WiFi + Bluetooth)

The ESP32 is a powerful microcontroller developed by Espressif Systems, featuring integrated WiFi and Bluetooth capabilities. 
It is widely used in IoT applications due to its high processing power, low energy consumption, and extensive peripheral support.
Key Features:

    Processor: Dual-core Tensilica Xtensa LX6, up to 240 MHz
    RAM: 520 KB SRAM
    Flash Memory: 4 MB (varies by model)
    WiFi: 802.11 b/g/n (2.4 GHz)
    Bluetooth: Bluetooth 4.2 (Classic + BLE)
    I/O Pins: 34-39 GPIO (varies by model)
    ADC: Up to 18x ADC channels (12-bit resolution)
    DAC: 2 DAC channels
    PWM: Up to 16 PWM channels
    UART, SPI, I2C, I2S, CAN Bus: Supported
    Deep Sleep Mode: Power consumption as low as 10 µA.
    
# --> ESP8266 (Single-core, WiFi)

The ESP8266 is an affordable WiFi-enabled microcontroller designed for IoT and wireless communication projects. 
While not as powerful as the ESP32, it is popular due to its low cost and simplicity.
Key Features:

    Processor: Single-core Tensilica L106, up to 80/160 MHz
    RAM: 80 KB (user-accessible)
    Flash Memory: 512 KB to 4 MB
    WiFi: 802.11 b/g/n (2.4 GHz)
    Bluetooth: ❌ (Not supported)
    I/O Pins: 11 GPIO (varies by board)
    ADC: 1 ADC channel (10-bit resolution)
    PWM: Up to 4 PWM channels
    UART, SPI, I2C: Supported
    Deep Sleep Mode: Power consumption as low as 10 µA.

# --> WeMos D1 R1 (ESP8266-based Development Board)

The WeMos D1 R1 is an Arduino Uno-shaped board based on the ESP8266. It is easier to use compared to standalone ESP8266 modules since it comes with a USB-to-Serial converter, voltage regulators, and more accessible GPIO pins.
Key Features:

    Microcontroller: ESP8266 (same as NodeMCU)
    USB Interface: CH340G (for easy programming)
    WiFi: 802.11 b/g/n (2.4 GHz)
    GPIO Pins: 11 Digital I/O (D0 - D10)
    Analog Input: 1 ADC Pin (A0, max 3.3V)
    PWM: Available on most GPIOs
    UART, SPI, I2C: Supported
    Operating Voltage: 3.3V (not 5V tolerant!)
    Power Supply: 5V via USB or Vin.
