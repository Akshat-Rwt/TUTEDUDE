from tkinter import *
import tkinter.messagebox
from tkinter.messagebox import askyesno, askokcancel

window = Tk()

window.title("Sample")
window.geometry('500x500')

tkinter.messagebox.showerror("Info" , "Running out of time")
question = tkinter.messagebox,askokcancel("Weather" , "Will it rain ?")

if question == True:
    print("Take an umberalla")

else:
    print("Okay")

window.mainloop()