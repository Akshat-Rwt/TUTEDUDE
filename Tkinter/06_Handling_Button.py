from tkinter import *

window = Tk()

window.title("Sample")
window.geometry('500x500')

def log_entry():
    print("Logged in")
button1 = Button(window , text = "LOGIN" , command = log_entry ,  width = 12 , bg = "red" , fg = "white" , font = ("bold",12) , activebackground= "black" , activeforeground= "white")
button1.pack()


window.mainloop()