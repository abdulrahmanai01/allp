from tkinter import *
import mysql.connector
win=Tk()

win.title("insert into mysql DB DEMO")
win.geometry("500x500")

frameleft=Frame(win,bg="black",width=500, height=30)
frameleft.pack(side = LEFT)

frameright=Frame(win,bg="red",width=500, height=30)
frameright.pack(side = RIGHT)

lbl_Title_of_Operation=Label(frameleft,text="insert into mysql DB DEMO")
lbl_Title_of_Operation.grid(row=)

lblName=Label(frameleft,text="Name")
lblName.grid(row=2,column=1,padx=30,pady=10)

lbltamil=Label(frameleft,text="tamil")
lblName.grid(row=3,column=1,padx=30,pady=10)

win.mainloop()