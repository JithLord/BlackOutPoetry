efrom code1 import decode, encode
from PIL import Image

im = Image.open('download2.jpg')
im.show(im)
encode(im,"qwertyuiopasdfghjklzxcvbnm1234567890")
print('\nDECODE:-----------------')
im2 = Image.open('down.png')
decode(im2)
