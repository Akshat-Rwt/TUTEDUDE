# Step 1 :  import tkinter

from tkinter import *

# Step 2 : gui interaction

window  = Tk()

# Step 3 : adding inputs

window.title("Simple")
window.geometry("500x700")  # Length x Breadth
window.config(bg = "Yellow")

# Frame and Buttons
frame1 = Frame(window, width = 300 , height = 300 , cursor="dot")
frame1.pack(side = TOP)

frame2 = Frame(window, width = 300 , height=300 , cursor="dotbox")
frame2.pack(side = BOTTOM)

button1 = Button(frame1 , text = "Button1" , bg = "blue")
button1.pack()

button2 = Button(frame2, text = "Button2" , bg = "green")
button2.pack()

button3 = Button(frame1 , text = "Log" , fg = "red")
button3.pack()


# Step 4 : main loop
window.mainloop()