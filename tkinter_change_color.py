import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self, master):
        self.master = master

        frame = ttk.Frame(self.master)

        def change_color():
            style = ttk.Style()
            style.configure("Custom.TButton", foreground="black",
                            background="white",

                            font="Verdana 12 underline")

        style = ttk.Style()
        style.configure("Custom.TButton", foreground="white",
                        background="#333333",
                        padding=[10, 10, 10, 10],
                        font="Verdana 12 underline")

        button = ttk.Button(frame, text="Click Me!",
                            style="Custom.TButton", command=change_color)
        button.pack()

        frame.pack(padx=5, pady=5)


root = tk.Tk()
root.geometry("200x150")
window = Window(root)
root.mainloop()
