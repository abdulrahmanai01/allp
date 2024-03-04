import tkinter as tk
#from tkinter import *

win=tk.Tk()
win.geometry("500x500")
win.title("Student Management System")

def quit():
    win.destroy()

def aboutpage():
    abt=tk.Tk()
    abt.title("About us")
    abt.geometry("300x300")
    """Welcome to parent window
    created on : 21-02-2024
    by Karthick AG
    """
    message="""Welcome to parent window
    created on : 21-02-2024
    by Karthick AG
    """
    lntinfo=tk.Label(abt,text=message)
    lntinfo.pack()
    abt.mainloop()
    
menubar=tk.Menu(win)
filemenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=filemenu, underline=0)
filemenu.add_command(label="New",  underline=0, accelerator="Alt+n")
filemenu.add_command(label="New window",  underline=4, accelerator="Alt+F")
filemenu.add_command(label="Open",  underline=0, accelerator="Alt+F")
filemenu.add_command(label="Save",  underline=0, accelerator="Alt+F")
filemenu.add_command(label="SaveAs",  underline=4, accelerator="Alt+F")
filemenu.add_separator()
filemenu.add_command(label="PageSetup",  underline=7, accelerator="Alt+F")
filemenu.add_command(label="Print",  underline=0, accelerator="Alt+F")
filemenu.add_separator()
filemenu.add_command(label="Exit",  underline=1, command=quit, accelerator="Ctrl+2")


# win.bind("<Control-3>", quit)

editmenu=tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Redo",  underline=4, accelerator="Alt+F")
editmenu.add_separator()
editmenu.add_command(label="Copy",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Cut",  underline=0, accelerator="Alt+F")
editmenu.add_command(label="Paste",  underline=0, accelerator="Alt+F")


viewmenu=tk.Menu(menubar)
menubar.add_cascade(label="View")

helpmenu=tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About",  underline=0, accelerator="Alt+F", command=aboutpage)


win.config(menu=menubar)


win.mainloop()