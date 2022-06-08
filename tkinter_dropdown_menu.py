# Import module
import os
from os import popen
from tkinter import *
  
# Create object
root = Tk()
  
# Adjust size
root.geometry( "200x200" )
  
# Change the label text

  
# Dropdown menu options
options = [
    "tilix",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def show():
    label.config( text = clicked.get() )
    text = clicked.get()
    popen(text)


#def inst_btn1():
    #entry_text = eingabefeld1.get()
    #popen(inst1_p1 + entry_text + inst1_p2)    
     



# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Select App" )
  
# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( root , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( root , text = " " )

    
label.pack()
  
# Execute tkinter
root.mainloop()