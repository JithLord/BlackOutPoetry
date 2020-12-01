from PIL import Image
import string
    # 0 1-26 " " 27-36
    #   a-z  " "  0-9
comb = [""]+[chr(x) for x in range(97,123)] +[" "]+ [str(i) for i in range(10)]    # [a:z] + [0:9]
numbers = [i for i in range(39)]                                      # [1:37]
ecode = dict(zip(numbers,comb))                                         # {"1":"a", "2":"b",     }
dcode = dict(zip(comb,numbers))                                         # {"a":"1", "b":"2",     }
 

def encode(im,text=""):
    text = text.lower()
    width, height = im.size[0], im.size[1]
    dcoded = [dcode.get(i) for i in text]
    #print(dcoded)
    dcoded = iter(dcoded)
    len_text = len(text)

    for y in range(height):
        for x in range(width):
            [r,g,b]=im.getpixel((x, y))
            if (len_text):      #To check if there's a character
                val3 = int(next(dcoded))
                len_text-=1
            else:
                val3 = 0
            if val3>30:
                r = (r>>4<<4)  + 15
                g = (g>>4<<4)  + 15
                b = (b>>4<<4)  + val3 - 30
            elif val3>15:
                r = (r>>4<<4)  + 15
                g = (g>>4<<4)  + val3 - 15
                b = (b>>4<<4)
            elif val3>=0:
                r = (r>>4<<4)   + val3
                g = (g>>4<<4)
                b = (b>>4<<4)
            value = (r,g,b)
            im.putpixel((x, y), value)
    im.show(im)
    im.save("down.png")
    return im


def decode(im):
    width, height = im.size[0], im.size[1]
    text=""
    for y in range(height):
        for x in range(width):
            [r,g,b]=im.getpixel((x, y))
            r,g,b = (r&15, g&15, b&15)
            char = ecode.get(r+g+b)
            print(char,end="")
            text+=char


