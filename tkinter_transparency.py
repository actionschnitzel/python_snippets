from tkinter import *

root = Tk()
root.title("Alpha Method")
root.geometry("500x500")
root.wait_visibility(root)
root.attributes('-alpha', 0.5)


root.mainloop()