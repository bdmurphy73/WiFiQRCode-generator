#!/usr/bin/env python3

# The module to create the QR code can be found: https://pypi.org/project/wifi-qrcode-generator/

#install with: pip install wifi_qrcode_generator.generator
import wifi_qrcode_generator.generator

# You need pillow module for image processing
# https://pypi.org/project/pillow/
# Install with: pip install pillow

#import image processing modules
from PIL import Image, ImageDraw, ImageFont

#Set your variables. They are all in one spot to make it easier
myssid = 'BDMurphyGuestWiFi'
mypasswd = 'bdM#WiFi$Password%'
imagefile = 'bdmguestwifiQrCode.png'

#Generate the QRCode of the WiFi login
qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
    ssid=myssid, hidden=False, authentication_type='WPA', password=mypasswd
)

#qr_code.print_ascii()
qr_code.make_image().save("Tmpimg.png")

#Now we need to adjust the QRCode image

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

# Load a custom font (replace 'FreeMono.ttf' with the path to your font file)
# Using basic courier font for the text under the QRCode
myFont = ImageFont.truetype('\windows\fonts\cour.ttf', 35)

# Add text with the defined font style
# Put the text at 90 pixels from the bottom of the image. Color is black.
draw.text((30, (new_img.height - 90)), myssid, font=myFont, fill=(0,0,0))

# Save the modified image
new_img.save(imagefile)

# Optionally, display the modified image
new_img.show()
