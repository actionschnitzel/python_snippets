from tkinter import *
import tkinter as tk


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.attributes('-fullscreen', True)


def resize(event):
    print("New size is: {}x{}".format(event.width, event.height))

root.bind("<Configure>", resize)

root.mainloop()