import os

test = os.path.isdir('/home/USER/Folder') # Need full path

if test == False:
    print("Nope!")
    
if test == True:
    print("Yes!")
    
    