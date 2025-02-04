# Step 1 :  import tkinter

from tkinter import *

# Step 2 : gui interaction

window  = Tk()

# Step 3 : adding inputs

window.geometry("500x500")  # Length x Breadth

button = Button(window , text = "Button" , width = 12)
button.place(x = 200 , y = 200)


# Step 4 : main loop
window.mainloop()