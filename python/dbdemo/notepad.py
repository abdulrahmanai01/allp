from tkinter import *
from tkinter import ttk

roar=Tk()
roar.title("Notepad")
roar.geometry("500x500")
roar.state("zoomed")

def close():
    roar.destroy()

menubar=Menu(roar)
filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New" , underline=0, accelerator="ctrl+N")
filemenu.add_command(label="Open...", underline=0, accelerator="ctrl+O")
filemenu.add_command(label="Save" , underline=0, accelerator="ctrl+S")
filemenu.add_command(label="Save As...", underline=0, accelerator="ctrL+S")
filemenu.add_separator()
filemenu.add_command(label="Page Setup....")
filemenu.add_command(label="Print....       Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",command=close)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo", underline=0, accelerator="ctrl+Z")
editmenu.add_command(label="Cut", underline=0, accelerator="ctrl+X")
editmenu.add_command(label="Copy", underline=0, accelerator="ctrl+C")
editmenu.add_command(label="Paste", underline=0, accelerator="ctrl+V")
editmenu.add_command(label="Delete", underline=0, accelerator="ctrl+Delete")
editmenu.add_separator()
editmenu.add_command(label="Find", underline=0, accelerator="ctrl+M")
editmenu.add_command(label="Find Next",  underline=0, accelerator="ctrl+F3")
editmenu.add_command(label="Replace", underline=0, accelerator="ctrl+H")
editmenu.add_command(label="Go To....", underline=0, accelerator="ctrl+G")
editmenu.add_separator()
editmenu.add_command(label="Select All", underline=0, accelerator="ctrl+A")
editmenu.add_command(label="Time/Date", underline=0, accelerator="F5")

formatmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Format",menu=formatmenu)
formatmenu.add_command(label="Word Wrap")
formatmenu.add_command(label="Font....")


viewmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="View",menu=viewmenu)
viewmenu.add_command(label="Zoom")
Zoommenu=Menu(viewmenu,tearoff=0)
Zoommenu.add_command(label="Zoom In", underline=0, accelerator="F5")
Zoommenu.add_command(label="Zoom Out", underline=0, accelerator="F6")
Zoommenu.add_command(label="Restore Default Zoom", underline=0, accelerator="F7")
viewmenu.add_command(label="Status bar")

helpimenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpimenu)
helpimenu.add_command(label="View Help")
helpimenu.add_separator()
helpimenu.add_command(label="About Notepad")

roar.config(menu=menubar)
roar.mainloop()
