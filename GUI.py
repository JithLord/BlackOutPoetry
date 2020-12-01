import tkinter 
from tkinter import filedialog
from PIL import ImageTk,Image
from code1 import encode,decode

window = tkinter.Tk()
window.title("Blackout Poetry")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.minsize(w,h)

text = ""
text_label = ""
image = [[]]
img = [[]]
up_image = [[]]

canvas = tkinter.Canvas(window,width=w,height=h,highlightthickness=0)
canvas.place(x=0,y=0)
back=ImageTk.PhotoImage(Image.open('back1.png').resize((w,h), Image.ANTIALIAS))
canvas.create_image(int(w/2),int(h/2), anchor="center", image=back)
canvas.back=back

canvas1 = tkinter.Canvas(window,width=480, height=480,bg="gray50")
canvas1.place(x=300,y=150)
canvas1_label = tkinter.Label(window, text='Original Image', fg='white', bg='black')
canvas1_label.place(x=500,y=120)

canvas2 = tkinter.Canvas(window,width=480, height=480,bg="gray50")
canvas2.place(x=850,y=150)
canvas2_label = tkinter.Label(window, text='Updated Image', fg='white', bg='black')
canvas2_label.place(x=1050,y=120)


#adding image buttons : 
upload_image_button=ImageTk.PhotoImage(Image.open('upload.png').resize((175,40), Image.ANTIALIAS)) #1.2
encode_image_button=ImageTk.PhotoImage(Image.open('encode.png').resize((118,33), Image.ANTIALIAS)) #1.3
decode_image_button=ImageTk.PhotoImage(Image.open('decode.png').resize((118,33), Image.ANTIALIAS)) #1.3
proceed_image_button=ImageTk.PhotoImage(Image.open('proceed.png').resize((128,38), Image.ANTIALIAS)) #1.2
clear_text_image_button=ImageTk.PhotoImage(Image.open('clear_text.png').resize((93,29), Image.ANTIALIAS))
clear_images_image_button=ImageTk.PhotoImage(Image.open('clear_images.png').resize((110,29), Image.ANTIALIAS))
save_image_button=ImageTk.PhotoImage(Image.open('save.png').resize((106,38), Image.ANTIALIAS))
exit_image_button=ImageTk.PhotoImage(Image.open('exit.png').resize((48,23), Image.ANTIALIAS))



#adding upload image box
def upload_image() :
    file = filedialog.askopenfilename(initialdir = "/", 
                    title="Select An Image",
                    filetype=(("JPEG","*.jpg"),("PNG","*.png"),("Bitmap","*.bmp")))
    label = tkinter.Label(window,text=file[:14]+str("...")+file[-12:],font="Helvetica 8 italic")
    label.place(x=30,y=200)
    disp_image(file)

uploadcolor = '#%02x%02x%02x' % (50, 39, 35)
upload = tkinter.Button(window,
                image=upload_image_button,
                command=upload_image,
                borderwidth=0,
                bg=uploadcolor,
                cursor='hand2',
                activebackground='grey',
                highlightthickness = 0, bd = 0,
                border=0)
upload.place(x=30,y=150)

#displaying uploaded image
def disp_image(file) :    
    global image 
    global img
    img = Image.open(file)
    r_img = img     #resized image for canvas
    width,height = img.size
    ratio = width/height
    if (ratio>1) :   # landscape image
        width = 480     # max possible width in canvas
        height = (int)(width/ratio)
        #print(width,height)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    elif (ratio<1) :     #potrait image
        height = 480    #max possible height in canvas 
        width = (int)(height*ratio)
        #print(width,height)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    else :      #square image
        height = 480 
        width = 480
        r_img = img.resize((width,height), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(r_img)    #converting to image type 
    canvas1.create_image(240,240,image=image)
    canvas1.image = image 



#radio buttons  
c = tkinter.IntVar()
def clicked():
    #if(c.get()==1) :
        #selection = "You have chosen to Encode"    #message
    #else : 
        #selection = "You have chosen to Decode"    #message
    #label = tkinter.Label(window,text=selection)
    #label.place(x=20, y=180)
    
    #text entry box
    def extract_text() :
        global text
        #global text_label
        text = txt_box.get()
        #txt_box.delete(0,'end')    #clear content once entered
        #txt_button['state'] = tkinter.DISABLED     #freeze entry button
        text_label = tkinter.Label(window, text=text, font="Times 12")
        #text_label.place(x=380,y=652)

        #calling the functions
        global up_image
        if (c.get()==1) : 
            modified_image = encode(img,text)       #modified image is only attributes
        elif (c.get()==2) :
            text,modified_image = decode(img)
            print(text)
        update_image(modified_image)

    if(c.get()==1) : 
        message = "Enter Text"  #enter text to encode
    elif(c.get()==2) :
        message = "Enter Text"  #enter text to decode
    txt_box = tkinter.Entry(window)
    txt_label = tkinter.Label(window, text=message)
    proceed_button = tkinter.Button(window,
            image=proceed_image_button,
            command=extract_text,
            cursor='hand2',
            bg='grey',
            activebackground='grey',
            border=0)

    proceed_button.place(x=20,y=380)
    txt_box.place(x=20,y=330)
    txt_label.place(x=20,y=300)

rad1 = tkinter.Radiobutton(window, 
            image=encode_image_button,
            variable=c,
            value=1,
            indicator=0,    #to change style     
            background="grey",
            border=0,
            command=clicked,
            cursor='hand2',
            activebackground='grey')

rad2 = tkinter.Radiobutton(window, 
            image=decode_image_button,
            variable=c,
            value=2,
            indicator=0,    #to change style
            background="grey",
            border=0,
            command=clicked,
            cursor='hand2',
            activebackground='grey')

rad1.place(x=20, y=240)
rad2.place(x=155, y=240)



def update_image(modified_image) :    #display updated image
    
    width,height = modified_image.size
    ratio = width/height
    r_img = modified_image 
    if (ratio>1) :   # landscape image
        width = 480     # max possible width in canvas
        height = (int)(width/ratio)
        #print(width,height)
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)
    elif (ratio<1):     #portrait image
        height = 480    #max possible height in canvas 
        width = (int)(height*ratio)
        #print(width,height)
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)
    else :      #square image
        height = 480 
        width = 480
        r_img = modified_image.resize((width,height), Image.ANTIALIAS)

    up_image = ImageTk.PhotoImage(r_img)    #converting to image type
    canvas2.create_image(240,240, image=up_image)
    canvas2.up_image=up_image

    # saving the result
    def save_result() : 
        result_img = modified_image.save("result.jpg")
    
    save = tkinter.Button(window,
                image=save_image_button, 
                command=save_result,
                cursor='hand2',
                border=0,
                bg='grey',
                activebackground='grey')
    save.place(x=1225,y=650)

#text_label_.pack_forget()
#reset and exit buttons
def clear_img() :
    canvas1.delete("all")
    canvas2.delete("all")

def clear_text() :
    text_label.pack_forget()
    text=''

clearimgcolor = '#%02x%02x%02x' % (70,57,51)
clear_images = tkinter.Button(window,image=clear_images_image_button,command=clear_img,border=0,activebackground='grey',bg=clearimgcolor,highlightthickness = 0, bd = 0)clear_images.place(x=20,y=480)
clear_text = tkinter.Button(window,image=clear_text_image_button,command=clear_text,border=0,activebackground='grey',bg='grey')
clear_text.place(x=150,y=480)

quit_button = tkinter.Button(window,
            image=exit_image_button, 
            command=window.quit,
            border=0)
quit_button.place(x=20,y=530)

window.mainloop()
