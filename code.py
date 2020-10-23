
from PIL import Image

def encode(im,text=""):
    width = im.size[0] 
    height = im.size[1]
    for x in range(width):
        for y in range(height):
            [r,g,b]=im.getpixel((x, y))
            r = r - r//240
            g = g - g//240
            b = b - b//240
            value = (r,g,b)
            im.putpixel((x, y), value)
    im.show(im)


comb = [chr(x) for x in range(97,123)] + [str(i) for i in range(10)]    # [a:z] + [0:9]
numbers = [i for i in range(1,37)]                                      # [1:37]
ecode = dict(zip(numbers,comb))                                         # {"1":"a", "2":"b",     }
dcode = dict(zip(comb,numbers))                                         # {"a":"1", "b":"2",     }

text="abcz0129"
r,g,b=0,0,0
for i in text:
    val = dcode.get(i)
    if (val>15) and (val<=30):
        r+=15
        val-=15
    elif (val>30):
        r+=15
        g+=15
        b+=(val-30)
print(r,g,b)

