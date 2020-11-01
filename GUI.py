import tkinter 
from tkinter import filedialog
from PIL import ImageTk,Image
from code import encode,decode

window = tkinter.Tk()
window.title("Blackout Poetry")
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
window.minsize(int(w/2),int(h/2))

text = ""
text_label = ""
image = [[]]
img = [[]]
up_image = [[]]

canvas = tkinter.Canvas(window,width=w,height=h)
canvas.place(x=0,y=0)
back=tkinter.PhotoImage(file='C:\\Users\\Gaurav Rajan\\Desktop\\back.png')
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

#TEXT LABEL : 
#text_label_ = tkinter.Label(window, text="TEXT : ", fg='white', bg='black', font="Times 14")
#text_label_.place(x=300,y=650)

#img1=tkinter.PhotoImage(file='C:\\Users\\Gaurav Rajan\\Desktop\\testimage1.png')
#img2=tkinter.PhotoImage(file='C:\\Users\\Gaurav Rajan\\Desktop\\testimage2.png')
#canvas1.create_image(240,240, image=img1)
#canvas2.create_image(240,240, image=img2)

#adding image as a label : THIS IS ACTUAL LABEL , work on resizing and fitting 
#title = tkinter.PhotoImage(file="Capture.png")
#title = image.resize((100,100), Image.ANTIALIAS)
#title1 = ImageTk.PhotoImage(title)
#label = tkinter.Label(image=title).pack() 

#adding text as a label : 
tkinter.Label(window, 
		 text="Blackout Poetry",
		 fg = "white",
		 bg = "black",
		 font = "Helvetica 32 bold italic").pack()

#adding upload image box
def upload_image() :
    file = filedialog.askopenfilename(initialdir = "/", 
                    title="Select An Image",
                    filetype=(("JPEG","*.jpg"),("PNG","*.png"),("Bitmap","*.bmp")))
    label = tkinter.Label(window,text=file,font="Helvetica 8 italic")
    label.place(x=30,y=95)
    disp_image(file)

upload = tkinter.Button(window,
                text="UPLOAD IMAGE",
                width=15,
                command=upload_image)
upload.place(x=30,y=70)

#displaying uploaded image
def disp_image(file) :    
    global image 
    global img
    img = Image.open(file)
    r_img = img     #resized image for canvas
    width,height = img.size
    ratio = width/height
    ratio = 1
    if (ratio>1) :   # landscape image
        width = 480     # max possible width in canvas
        height = (int)(width/ratio)
        #print(width,height)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    elif (ratio<1):     #potrait image
        height = 480    #max possible height in canvas 
        width = (int)(height*ratio)
        #print(width,height)
        r_img = img.resize((width,height), Image.ANTIALIAS)
    else :      #square image
        height = 480 
        width = 480
        r_img = img.resize((width,height), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(r_img)
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
            print(img.size)
            modified_image = encode(img,text)       #modified image is only attributes
        elif (c.get()==2) :
            modified_image = decode(img)    
        up_image = ImageTk.PhotoImage(modified_image)
        update_image(up_image)

    if(c.get()==1) : 
        message = "Enter Text"  #enter text to encode
    elif(c.get()==2) :
        message = "Enter Text"  #enter text to decode
    txt_box = tkinter.Entry(window)
    txt_label = tkinter.Label(window, text=message)
    txt_button = tkinter.Button(window,
            text="Proceed",
            command=extract_text)

    txt_button.place(x=20,y=300)
    txt_box.place(x=20,y=250)
    txt_label.place(x=20,y=220)

rad1 = tkinter.Radiobutton(window, 
            text="Encode",
            variable=c,
            value=1,
            indicator=0,    #to change style     
            background="pink",
            command=clicked)

rad2 = tkinter.Radiobutton(window, 
            text="Decode",
            variable=c,
            value=2,
            indicator=0,    #to change style
            background="pink",
            command=clicked)

rad1.place(x=20, y=150)
rad2.place(x=120, y=150)

def update_image(up_image) :    #display updated image
    canvas2.create_image(240,240, image=up_image)
    canvas2.up_image=up_image

#text_label_.pack_forget()
#reset and exit buttons
def clear_img() :
    canvas1.delete("all")
    canvas2.delete("all")

def clear_text() :
    text_label.pack_forget()
    text=''

clear_images = tkinter.Button(window,text="Clear Images",command=clear_img)
clear_images.place(x=20,y=350)
clear_text = tkinter.Button(window,text="Clear Text",command=clear_text)
clear_text.place(x=110,y=350)

quit_button = tkinter.Button(window,
            text="Exit", 
            command=window.quit,
            bg="orange red")
quit_button.place(x=20,y=380)

window.mainloop()
