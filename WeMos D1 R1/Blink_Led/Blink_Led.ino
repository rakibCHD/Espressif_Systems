/*
-->Board Manager Url:http://arduino.esp8266.com/stable/package_esp8266com_index.json
-->Board: "WeMos D1 R1"
-->Upload Speed: "921600"
-->CPU Frequency: "80 MHz"
-->Flash Size: "4M (no SPIFFS)"
-->Debug port: "Disabled"
-->Debug Level: "None"
-->lwIP Variant: "v2 Lower Memory"
-->VTables: "Flash"
-->Exceptions: "Disabled"
-->Erase Flash: "Only Sketch"
-->Programmer:esptool(deafult)
-->On board Blue led connected with GPIO2(D4);
*/ 

int led = D4;

void setup() 
{
  pinMode(led, OUTPUT);       
}

void loop()
{              
  digitalWrite(led, HIGH);                           
} 
