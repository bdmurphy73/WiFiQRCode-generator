This Python script will create a QR Code to provide a simple method to get your phone or tablet onto a Wi-Fi network.

Copyright (c) 2024, Bryan Murphy

license: GNU LGPL


This script can be used to create a QR code allowing someone to shair the WiFi network login. The end user can scan the QR code to have their device connect to a WiFi network.
It requires user input below for:
##### network SSID 
##### password 
##### output file name.

The generated QR code graphic will also have text below so users can type in the information if their device won't scan.
The python module to create the QR code can be found: https://pypi.org/project/wifi-qrcode-generator/
Dependencies are: - wifi_qrcode_generator.generator and pillow <br>
install with: pip install wifi_qrcode_generator.generator<br>
Install with: pip install pillow

You are free to share and use
I use this to generate the QRCode for my guest network. Guests who are visiting can simply scan the QRCode to get WiFi access.

# Why this file instead of an online tool? 
1) You are giving the online system your WiFi password. They keep it and it can be hacked.
2) Some of these online tools only generate a tiny URL. The tiny URL links back to their site so every time someone scans the code the website gets information.



<img alt="Guest WiFi" width="200" height="200" src="https://github.com/bdmurphy73/WiFiQRCode-generator/blob/main/ExampleWiFiQRCode.png">

Enjoy

<h2> 🚀 &nbsp;Some Tools I Have Used and Learned</h2>
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linux/linux-original.svg" alt="Linux" width="45" height="45" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" width="45" height="45" />
</p>

<h2> Social Media and Website</h2>
   <a img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" href=https://www.linkedin.com/in/bryan-murphy>Murphy</a>
   <a href=https://authorbdmurphy.com>Author B.D. Murphy</a>
          

