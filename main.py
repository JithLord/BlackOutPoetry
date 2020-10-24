import image
from PIL import Image

im = Image.open('download2.jpg')
im.show(im)
image.encode(im,"qwertyuiopasdfghjklzxcvbnm1234567890")
print('\nDECODE:-----------------')
im2 = Image.open('down.png')
image.decode(im2)
