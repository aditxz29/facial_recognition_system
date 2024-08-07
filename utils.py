import tkinter as tk
from tkinter import messagebox


def get_button (window , text , color, command , fg="white"):
    button = tk.Button(
        window, 
         text = text,
         activebackground = "black",
         activeforeground = "white", 
         fg = fg, 
         bg = color ,
         command= command,
         height = 2, 
         width = 20,
        font= ('Helvetica bold', 20))
    return button

 

def  get_img_label(window):
    label = tk.Label(window)
    return label

def get_text_label(window , text):
    label = tk.Label(window , text = text )
    label.config(font = ('sans serif ',21 ), justify= "left")
    return label


def get_entry_text(window):
    input_txt = tk.Entry(window, font=('arial', 32) )
    return input_txt

def msg_box(title , description ):
    messagebox.showinfo(title , description ) 

