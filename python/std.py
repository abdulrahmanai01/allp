import os
import tkinter as tk
from tkinter import ttk



win=tk.Tk()
win.title("Student Management System")
win.state("zoomed")
win.geometry("600x600")

def exitwindow():
    win.destroy()

def createTitle():
    titleImageFrame=tk.Frame(win,width=600,height=400, bg="black")
    titleImageFrame.pack()

    imgdir=os.path.join(os.path.dirname(__file__),'img')
    print("Path name is : " + imgdir)

    imageloction=os.path.join(imgdir,'banner1.gif')
    print("image location is : " + imageloction)

    titleimage=tk.PhotoImage("titleimg",file=os.path.join(imgdir,"banner1.gif"))


    lblTitleImage=tk.Label(titleImageFrame, image=titleimage)
    lblTitleImage.pack()

def createTab():
    tabWelcome=ttk.Notebook(tablist, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    tabWelcome.pack(fill="both",expand=True)
    tablist.add(tabWelcome, text="untitled-01")

menubarlist=tk.Menu(win, bg="red")
filemenu=tk.Menu(menubarlist,tearoff=0)
menubarlist.add_cascade(label="File",menu=filemenu, underline=0)
filemenu.add_command(label="New",underline=0, accelerator="Ctrl+N", command=createTab)
filemenu.add_command(label="New Window", underline=4,accelerator="Ctrl+Shift+W")
filemenu.add_command(label="Close",underline=4,accelerator="Ctrl+E")
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_command(label="Exit",underline=1,command=exitwindow,accelerator="Ctrl+Q")




editmenu=tk.Menu(menubarlist,tearoff=0)
menubarlist.add_cascade(label="Edit",menu=editmenu)

editmenu.add_command(label="Undo",underline=0, accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", underline=0,accelerator="Ctrl+Shift+Z")
editmenu.add_separator()
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+C")
editmenu.add_command(label="Cut",underline=1,accelerator="Ctrl+X")
editmenu.add_command(label="Paste",underline=3,accelerator="Ctrl+V")
editmenu.add_command(label="Exit",underline=1,command=exitwindow,accelerator="Ctrl+Q")


win.config(menu=menubarlist)

# titleImageFrame=tk.Frame(win, bg="black")
# titleImageFrame.pack()

# imgdir=os.path.join(os.path.dirname(__file__),'img')
# print("Path name is : " + imgdir)

# imageloction=os.path.join(imgdir,'banner1.gif')
# print("image location is : " + imageloction)

# titleimage=tk.PhotoImage("titleimg",file=os.path.join(imgdir,"banner1.gif"))


# lblTitleImage=tk.Label(titleImageFrame, image=titleimage)
# lblTitleImage.pack()


TabFrame=tk.Frame(win,  bg="red" )
TabFrame.pack(fill="both", expand=True)
        # TabFrame.place(anchor="ne", relx=.14, rely=.1)


tablist=ttk.Notebook(TabFrame)
tablist.pack(expand=True)

tabWelcome=ttk.Notebook(tablist, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
tabWelcome.pack(fill="both",expand=True)
tablist.add(tabWelcome, text="welcome")

        # tabWelcome1=ttk.Notebook(tablist)
        # tabWelcome1.pack(fill="x", padx=60, expand=True)

tablist.add(tabWelcome, text="welcome")
        # tablist.add(tabWelcome1, text="welcome to page 2")

text=tk.Text(tabWelcome,width=win.winfo_screenwidth(), height=win.winfo_screenheight())
text.pack(fill="both")
win.mainloop()