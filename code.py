from PIL import Image
import string
    # 0 1-26 " " 27-36
    #   a-z  " "  0-9
comb = [""]+[chr(x) for x in range(97,123)] + [str(i) for i in range(10)]    # [a:z] + [0:9]
numbers = [i for i in range(38)]                                      # [1:37]
ecode = dict(zip(numbers,comb))                                         # {"1":"a", "2":"b",     }
dcode = dict(zip(comb,numbers))                                         # {"a":"1", "b":"2",     }
 

def encode(im,text=""):
    text = text.lower()
    width, height = im.size[0], im.size[1]
    dcoded = [dcode.get(i) for i in text]
    print(dcoded)
    dcoded = iter(dcoded)
    len_text = len(text)

    print('Before:')
    r, g, b = im.getpixel((0, 0))
    print(r, g, b)
    r, g, b = im.getpixel((1, 1))
    print(r, g, b)
    r, g, b = im.getpixel((2, 2))
    print(r, g, b)
    r, g, b = im.getpixel((3, 3))
    print(r, g, b)
    r, g, b = im.getpixel((4, 4))
    print(r, g, b)

    for x in range(height):
        for y in range(width):
            [r,g,b]=im.getpixel((x, y))
            if (len_text):      #To check if there's a character
                val3 = int(next(dcoded))
                len_text-=1
            else:
                val3 = 0
            print('Char', val3, (r,g,b), '->', end="\t")
            if val3>31:
                print('Case 1', end="\t")
                r = (r>>4<<4)  + 15
                g = (g>>4<<4)  + 15
                b = (b>>4<<4)  + val3 - 30
            elif val3>15:
                print('Case 2', end="\t")
                r = (r>>4<<4)  + 15
                g = (g>>4<<4)  + val3 - 15
                b = (b>>4<<4)
            else:
                print('Case 3', end="\t")
                r = (r>>4<<4)   + val3
                g = (g>>4<<4)
                b = (b>>4<<4)
            print((r,g,b))
            value = (r,g,b)
            im.putpixel((x, y), value)
    
    print('After:')
    r, g, b = im.getpixel((0, 0))
    print(r, g, b)
    r, g, b = im.getpixel((1, 1))
    print(r, g, b)
    r, g, b = im.getpixel((2, 2))
    print(r, g, b)
    r, g, b = im.getpixel((3, 3))
    print(r, g, b)
    r, g, b = im.getpixel((4, 4))
    print(r, g, b)

    im.show(im)
    im.save("down.png")


def decode(im):
    width, height = im.size[0], im.size[1]
    text=""

    print('Before:')
    r, g, b = im.getpixel((0, 0))
    print(r, g, b)
    r, g, b = im.getpixel((1, 1))
    print(r, g, b)
    r, g, b = im.getpixel((2, 2))
    print(r, g, b)
    r, g, b = im.getpixel((3, 3))
    print(r, g, b)
    r, g, b = im.getpixel((4, 4))
    print(r, g, b)

    for x in range(height):
        for y in range(width):
            [r,g,b]=im.getpixel((x, y))
            # print((r,g,b), '->', end="\t")
            # r,g,b = r%240,g%240,b%240
            r,g,b = (r&15, g&15, b&15)
            # print((r,g,b),end="\n")
            char = ecode.get(r+g+b)
            print(char,end="")
            text+=char
    # print(text)


im = Image.open('download2.jpg')
im.show(im)
encode(im,"Jithin")
print('\nDECODE:-----------------')
im2 = Image.open('down.png')
decode(im2)
