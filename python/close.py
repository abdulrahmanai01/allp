#Import the library
from tkinter import *

#Create an instance of window
win = Tk()

#Set the geometry of the window
win.geometry("700x400")

#Define a function to close the window
def close_win():
   win.destroy()

#Create a label
Label(win, text="Click the button to Close the window",
font=('Poppins bold', 25)).pack(pady= 20)

#Create a Button

Button(win, text= "Close", font=('Poppins bold', 16),
command=close_win).pack(pady=20)

win.mainloop()