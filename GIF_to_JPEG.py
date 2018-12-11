import PIL
from PIL import Image
import PIL.Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"E:/Python/jerome/venv/Scripts/Tesseract-OCR/tesseract.exe"
import tkinter as tk
from tkinter import *
from tkinter import filedialog

def GIF_location():

    location  = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                     filetypes=(("GIF Files", "*.gif"), ("all files", "*.*")))
    if not location.endswith('.gif') or not location:
        display.configure(fg ="red")
        display.insert(1,'Please load correct GIF File')
    else :
        display.delete(0, 'end')
    global GIF_file_location
    GIF_file_location = location

def save_path():
    display.delete(0, 'end')
    global save_name
    save_name = file_name.get()
    if not save_name:
        display.configure(fg="red")
        display.insert(1, 'Please give correct file name')
    else:
        #print(save_name)
        global save_directory
        save_directory = filedialog.askdirectory()
        if not save_directory:
            display.configure(fg="red")
            display.insert(1, 'Please select correct folder to save the file')

def convertion():
    display.delete(0, 'end')
    img = PIL.Image.open(GIF_file_location)
    img = img.convert("RGB")
    #img.show()
    final_file_name = save_name + '.jpg'
    img.save(save_directory + '/' + final_file_name,quality =100)
    display.configure(fg="green")
    display.insert(1, 'GIF to JPEG Image conversion has been completed')
    display.insert(2, 'Please clear the screen before starting next')
    display.insert(3, 'conversion')

# GUI Development
global gui
gui = tk.Tk()
gui.title("GIF to JPEG Image Conversion ")
gui.geometry("500x500")
title = Label(gui, text="GIF to JPEG Image Conversion",fg="purple4",
                      font=("Times New Roman", 20, "bold")).place(x=60, y=30)

# GIF path
GIF_label = Label(gui, text="Select GIF File ", font=("Times New Roman", 12, "bold")).place(x=90,y=100)
button1 = Button(gui, text="File", bg="seashell4", command=GIF_location, width=10).place(x=280, y=100)

# File name

file_label = Label(gui, text="File Name ", font=("Times New Roman", 12, "bold")).place(x=90, y=150)
file_name = StringVar()
global file_name_Label
file_name_Label = Entry(gui, textvariable=file_name, font=("Times New Roman", 12), width=15)
file_name_Label.place(x=280, y=150)

# save_path

Result = Label(gui, text="Select Save path ",font=("Times New Roman", 12, "bold")).place(x=90, y=200)

button2 = Button(gui, text="Folder", bg="seashell4", command=save_path, width=10).place(x=280, y=200)

# convert button

button3 = Button(gui, text="Convert", bg="green2", command=convertion, width=10,font=("Times New Roman", 10, "bold")).place(x=210, y=270)

# Exit

button4 = Button(gui, text="Exit", bg="red", command=GIF_location, width=10, font=("Times New Roman", 10, "bold")).place(x=80, y=420)

# clear

button5 = Button(gui, text="Clear", bg="yellow", command=GIF_location, width=10, font=("Times New Roman", 10, "bold")).place(x=330, y=420)

# Display

global display
display = Listbox(gui,height=3, width=47, font=("Times New Roman", 12, "bold"))
display.place(x=60, y=320)

gui.mainloop()