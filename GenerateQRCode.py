#!/usr/bin/env python3
# Published by B.D. Murphy @ 2024
# This script can be used to create a QR code that users can scan to have their device connect to a WiFi network.
# It requires user intput below for the network SSID, password, and output file name.
# The generated QR code will also have text below so users can type in the information if their device won't scan.
# The module to create the QR code can be found: https://pypi.org/project/wifi-qrcode-generator/

#install with: pip install wifi_qrcode_generator.generator
import wifi_qrcode_generator.generator

# You need pillow module for image processing
# https://pypi.org/project/pillow/
# Install with: pip install pillow
#import image processing modules
from PIL import Image, ImageDraw, ImageFont


####### USER INPUT ###########
#Set your variables. They are all in one spot to make it easier
myssid = 'GuestWi-Fi'
mypasswd = 'LongPassword'
imagefile = 'ExampleWiFiQRCode.png'

######## Processing start
#Generate the QRCode of the WiFi login
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid=myssid, hidden=False, authentication_type='WPA', password=mypasswd
)

#qr_code.print_ascii()
qr_code.make_image().save("Tmpimg.png")

#Now we need to adjust the QRCode image to add the text below

# Open the image 
img = Image.open("Tmpimg.png")

# Define the desired extra space below the QR Code (e.g., 100 pixels)
extra_space_height = 50

# Create a new image with white background
new_height = img.height + extra_space_height
new_img = Image.new('RGB', (img.width, new_height), color='white')

# Paste the original image at the top
new_img.paste(img, (0, 0))

# Create a drawing object
draw = ImageDraw.Draw(new_img)

# Load a custom font (replace 'cour.ttf' with the path to your font file)
# Using basic courier font for the text under the QRCode
myFont = ImageFont.truetype('\windows\fonts\cour.ttf', 35)

# Add text to the image with the defined font style
# Put the SSID at 90 pixels from the bottom of the image. Color is black.
# Put the password at 45 pixels from the bottom
# A guest can read and type in the text if the scan doesn't work.
draw.text((30, (new_img.height - 90)), myssid, font=myFont, fill=(0,0,0))
draw.text((30, (new_img.height - 45)), mypasswd, font=myFont, fill=(0,0,0))

# Save the modified image
new_img.save(imagefile)

# Optionally, display the modified image
new_img.show()
