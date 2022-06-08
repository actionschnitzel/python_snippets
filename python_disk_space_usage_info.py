import os
import sys
import subprocess as sp
import fileinput
import configparser
import psutil
import platform
import webbrowser
import tkinter as tk
from os import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



hdd = psutil.disk_usage('/')
def get_total_space():
	return hdd.total / (2**30)
def get_used_space():
	return hdd.used / (2**30)
def get_free_space():
	return hdd.free / (2**30)
def get_disk_percent():
	return hdd.percent

total = str(round(get_total_space(), 2))
used = str(round(get_used_space(), 2))
free = str(round(get_free_space(),2))
disk = str(get_disk_percent())

print(total)
print(used)
print(free)
print(disk + "%")





