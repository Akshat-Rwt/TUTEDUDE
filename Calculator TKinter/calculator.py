# Step 1 : Importing
from tkinter import *

# Step 2 : Gui Interaction
window = Tk()
window.geometry('500x500')

# Step 3 : Adding Inputs

# Entry Box
e = Entry(window,width=56 , borderwidth=5)
e.place(x = 0 , y = 0)

# Buttons

b = Button(window, text='1', width=12 , )
b.place(x = 10 , y = 60 )

b = Button(window, text='2', width=12 , )
b.place(x = 80 , y = 60 )

b = Button(window, text='3', width=12  , )
b.place(x = 170 , y = 60 )

b = Button(window, text='4', width=12  , )
b.place(x = 10 , y = 120 )

b = Button(window, text='5', width=12  , )
b.place(x = 80 , y = 120 )

b = Button(window, text='6', width=12 ,  )
b.place(x = 170 , y = 120 )

b = Button(window, text='7', width=12 , )
b.place(x = 10 , y = 180 )

b = Button(window, text='8', width=12 , )
b.place(x = 80 , y = 180 )

b = Button(window, text='9', width=12 , )
b.place(x = 170 , y = 180 )

b = Button(window, text='0', width=12 , )
b.place(x = 10 , y = 240 )

b = Button(window, text='+', width=12 )
b.place(x = 80 , y = 240 )

b = Button(window, text='-', width=12 )
b.place(x = 170 , y = 240 )

b = Button(window, text='*', width=12 )
b.place(x = 10 , y = 300 )

b = Button(window, text='/', width=12 )
b.place(x = 80 , y = 300 )

b = Button(window, text='=', width=12 )
b.place(x = 170 , y = 300 )

b = Button(window, text='clear', width=12 )
b.place(x = 10 , y = 350 )



# Step 4 : main loop
window.mainloop()