import os
import tkinter as tk
from os import popen
from os import system as cmd
from tkinter import *
from tkinter import ttk


def page1():
    page3text.pack_forget()
    page2text.pack_forget()
    page1text.pack()

def page2():
    page1text.pack_forget()
    page3text.pack_forget()
    page2text.pack()
    
def page3():
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack()

main = Tk()
main.title("Papirus Pi Manager")
#icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
#main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#222d32'
main.resizable(0, 0)

app_width = 1200
app_height = 800



screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main.wait_visibility(main)
main.wm_attributes('-alpha', 0.95, )

page1btn = Button(main, text="Page 1", command=page1)
page2btn = Button(main, text="Page 2", command=page2)
page3btn = Button(main, text="Page 3", command=page3)

page1text = Label(main, text="This is page 1")
page2text = Label(main, text="This is page 2")
page3text = Label(main, text="This is page 3")


page1btn.pack()
page2btn.pack()
page3btn.pack()

page1text.pack()