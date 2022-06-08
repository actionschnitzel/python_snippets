# Code By Timo Westal 
#Feel good IMPORTS for all eventualities
import os
import tkinter as tk
import webbrowser
from os import popen
from os import system as cmd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import platform
import psutil
from collections import namedtuple
import resource
import threading
from datetime import datetime
import distro

#MAIN
main = Tk()
main.title("Tkinter_Gui_Base")
#icon = tk.PhotoImage(file="")
#main.tk.call('wm', 'iconphoto', main._w, icon)
#main['background'] = '#333333'
#main.resizable(0, 0)
app_width = 1000
app_height = 1000
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
#main.wait_visibility(main)
#main.wm_attributes('-alpha', 0.95, )

#Code_HEAR xD#####################################################
##################################################################



##################################################################
##################################################################
main.mainloop()

