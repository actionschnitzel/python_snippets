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

popen("xterm -e 'bash -c \"apt-cache pkgnames > ~/PiGro-Aid-/essentials/tkinter_searchbar_SomeFile.txt && exit; exec bash\"'")



root = Tk()
#root.titel("Seachbar")
root.geometry("500x300")

# Update the listbox

def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(event):
    # Delete wot is in  Box
    my_entry.delete(0,END)    
    # Add clicked list item to enty box  
    my_entry.insert(0, my_list.get(ACTIVE))


# Checkfunktion Entry vs. List

def check(event):
    # grad inserted
    typed = my_entry.get()
    
    if typed == '':
        data = content
    else:
        data = []
        for item in content:
            if typed.lower() in item.lower():
                data.append(item)
                
    #updates listbox with selected item
    update(data)
                

fo = open("tkinter_searchbar_SomeFile.txt", "r")
content = fo.readlines()
print (content)


my_label = Label(root, text="Start Typing",
    font=("Helvetica",14), fg="grey")
my_label.pack(pady=20)


        


# Create an entry box

my_entry = Entry(root,font=("Helvetica",20))
my_entry.pack()

my_list = Listbox(root, width=50)
my_list.pack()

fo = open("tkinter_searchbar_SomeFile.txt", "r")
content = fo.readlines()
for i,s in enumerate(content):
    content[i] = s.strip()
print (content)




# Add toppings

update(content)


#Create binding

my_list.bind("<<ListboxSelect>>", fillout )

my_entry.bind("<KeyRelease>", check)



root.mainloop()