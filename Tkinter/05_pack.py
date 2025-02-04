from tkinter import *
window = Tk()

window.title("Simple")
window.geometry("500x500")

label1 = Label(window , text = "Label1" , bg = "red" , fg = "white")
label1.pack(side = TOP , fill = X , expand = False  )

label2 = Label(window , text = "Label1" , bg = "blue" , fg = "white")
label2.pack(side = LEFT , fill = Y , expand = False  )

label3 = Label(window , text = "Label1" , bg = "Green" , fg = "white")
label3.pack(side = RIGHT , fill = Y , expand = False  )


window.mainloop()