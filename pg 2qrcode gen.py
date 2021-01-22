import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "www.youtube.com"
  
# Generate QR code 
url = pyqrcode.create(s) 
url.png('pyqr.png', scale = 6) 