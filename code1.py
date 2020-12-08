from PIL import Image
import string
    # 0 1-26 27 28-36
    #   a-z  " "  0-9

comb = [""]+[chr(x) for x in range(97,123)] +[" "]+ [str(i) for i in range(10)]    # [a:z] + [ ] + [0:9]
numbers = [i for i in range(39)]                                      # [1:38]
ecode = dict(zip(numbers,comb))                                         # {"1":"a", "2":"b",     }
dcode = dict(zip(comb,numbers))                                         # {"a":"1", "b":"2",     }


def encode(im,text=""):
    
    text = text.lower()
    width, height = im.size[0], im.size[1]
    dcoded = [dcode.get(i) for i in text]
    #print(dcoded)
    dcoded = iter(dcoded)
    len_text = len(text)

    for y in range(0,height):
        for x in range(0,width,2):
            [r1,g1,b1]=im.getpixel((x,y))
            [r2,g2,b2]=im.getpixel((x+1,y))         #First fill r2,g2 and b2 then r1,g1,b1
            if (len_text):      #To check if there's a character          
                val3 = int(next(dcoded))
                len_text-=1
            else:
                val3 = 0
            if val3>35:
                r1 = (r1>>3<<3) + 7
                g1 = (g1>>3<<3) + 7
                b1 = (b1>>3<<3) + 7
                r2 = (r2>>3<<3) + 7
                g2 = (g2>>3<<3) + 7
                b2 = (b2>>3<<3) + val3 - 35
            elif val3>28:
                r1 = (r1>>3<<3) + 7
                g1 = (g1>>3<<3) + 7
                b1 = (b1>>3<<3) + 7
                r2 = (r2>>3<<3) + 7
                g2 = (g2>>3<<3) + val3 -28
                b2 = (b2>>3<<3) 
            elif val3>21:
                r1 = (r1>>3<<3) + 7
                g1 = (g1>>3<<3) + 7
                b1 = (b1>>3<<3) + 7
                r2 = (r2>>3<<3) + val3 - 21
                g2 = (g2>>3<<3) 
                b2 = (b2>>3<<3) 
            elif val3>14:
                r1 = (r1>>3<<3) 
                g1 = (g1>>3<<3) 
                b1 = (b1>>3<<3) 
                r2 = (r2>>3<<3) + 7
                g2 = (g2>>3<<3) + 7
                b2 = (b2>>3<<3) + val3 - 14
            elif val3>7:
                r1 = (r1>>3<<3) 
                g1 = (g1>>3<<3) 
                b1 = (b1>>3<<3) 
                r2 = (r2>>3<<3) + 7
                g2 = (g2>>3<<3) + val3 - 7
                b2 = (b2>>3<<3)
            elif val3>=0:
                r1 = (r1>>3<<3) 
                g1 = (g1>>3<<3) 
                b1 = (b1>>3<<3) 
                r2 = (r2>>3<<3) + val3
                g2 = (g2>>3<<3) 
                b2 = (b2>>3<<3) 
            value1 = (r1,g1,b1)
            im.putpixel((x, y), value1)
            value2 = (r2,g2,b2)
            im.putpixel((x+1, y), value2)
    #im.show(im)
    im.save("down.png")
    return im


def decode(im):

    width, height = im.size[0], im.size[1]
    text=""

    for y in range(0,height):
        for x in range(0,width,2):
            [r1,g1,b1]=im.getpixel((x, y))
            [r2,g2,b2]=im.getpixel((x+1, y))
            r1,g1,b1 = (r1&7, g1&7, b1&7)
            r2,g2,b2 = (r2&7, g2&7, b2&7)
            char = ecode.get(r1+g1+b1+r2+g2+b2)
            #print(char,end="")
            text+=char
    return text,im
    
