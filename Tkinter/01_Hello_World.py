# Step 1 :  import tkinter

from tkinter import *

# Step 2 : gui interaction

window  = Tk()

# Step 3 : adding inputs

inp = Label(window, text = " Hello World ")
inp.pack()

# Step 4 : main loop

window.mainloop()