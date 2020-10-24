from PIL import Image

comb = [" "]+[chr(x) for x in range(97,123)] + [str(i) for i in range(10)]    # [a:z] + [0:9]
numbers = [i for i in range(38)]                                      # [1:37]
ecode = dict(zip(numbers,comb))                                         # {"0":" ","1":"a", "2":"b",     }
dcode = dict(zip(comb,numbers))                                         # {" ":"0","a":"1", "b":"2",     }
 

def encode(im,text=""):
    width = im.size[0] 
    height = im.size[1]
    dcoded = [dcode.get(i) for i in text]
    dcoded = iter(dcoded)
    len_text = len(text)

    for x in range(height):
        for y in range(width):
            [r,g,b]=im.getpixel((x, y))
            if (len_text):      #It's this part which is causing some issue
                val3 = int(next(dcoded))
                len_text-=1
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
    im.show(im)
