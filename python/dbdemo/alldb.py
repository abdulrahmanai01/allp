import os
from tkinter import *
from tkinter import ttk
from dbconnect import *
import mysql.connector


#from db.mydbfile import DBManipulate as kk
#import tkinter as tk


root_window=Tk()

root_window.title("Student Management System")
root_window.geometry("500x500")
#root_window.state("zoomed")

imgdir1=os.path.join(os.path.dirname(__file__),'img')
imageicolocation=os.path.join(imgdir1,'sms.ico')
#getIconImage1=PhotoImage('titleimage',file=os.path.join(imgdir1,'sms.ico'))

# root_window.wm_iconbitmap(imageicolocation)

#mydbcon=kk()
mydbcon=DBManipulate()


def exitParent():
    root_window.destroy()

def inserttoDB():
    student_name=Ety_StdName.get()
    st_mk_tamil=Ety_StdMkTamil.get()
    st_mk_eng=Ety_StdMkEng.get()
    st_mk_math=Ety_StdMkMath.get()
    st_mk_sci=Ety_StdMkSci.get()
    st_mk_ss=Ety_StdMkSS.get()
    
    x= mydbcon.insertvalues(student_name,st_mk_tamil,st_mk_eng,st_mk_math,st_mk_sci,st_mk_ss)
    lblConMsg.config(text=x)
    selectdatas()


def selectdatas():

    data=mydbcon.mydbconnection()
    result=data.cursor()
    result.execute("SELECT * FROM student_details")
    i=0 
    for student in result: 
        for j in range(len(student)):
            lbldisplay = Entry(resultframe, width=10, fg='blue') 
            lbldisplay.grid(row=i, column=j) 
            lbldisplay.insert(END, student[j])
        i=i+1 

# def insertvalues():
#     # student_name=Ety_StdName.get()
#     # st_mk_tamil=Ety_StdMkTamil.get()
#     # st_mk_eng=Ety_StdMkEng.get()
#     # st_mk_math=Ety_StdMkMath.get()
#     # st_mk_sci=Ety_StdMkSci.get()
#     # st_mk_ss=Ety_StdMkSS.get()

#     data=mydbcon.mydbconnection()
#     result=data.cursor()

#     result.execute("INSERT INTO student_details (Name, Tamil, English, Maths, Science, Social) VALUES (\"karthick\", 60,60,60,60,60);")

#     data.commit()

#     print (result.rowcount , " row inserted")




#initializing Main menu
menulist=Menu(root_window)

#initializing submenu
submenulist=Menu(menulist, tearoff=0)

#creating submenus list
submenulist.add_command(label="New File", underline=0, accelerator="Ctrl+N")
submenulist.add_command(label="New Project",  underline=7, accelerator="Ctrl+Shift+j")
submenulist.add_command(label="New Py File", underline=5, accelerator="Ctrl+N")


#list of main menu
filemenu=Menu(menulist, tearoff=0)
menulist.add_cascade(label="File", menu=filemenu)
filemenu.add_cascade(label="New", menu=submenulist)
filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q", command=exitParent)

#Attach menu to the parent root window
root_window.config(menu=menulist)


#passing through direct image location
#imgdir1=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"banner.gif")
#getTitleImage=PhotoImage('titleimage',file=imgdir1)

# giving image through general location
imgdir=os.path.join(os.path.dirname(__file__),'img')
getTitleImage=PhotoImage('titleimage',file=os.path.join(imgdir,'banner.gif'))

titleImageFrame=Frame(root_window, bg="black")#, height=200)
titleImageFrame.pack(padx=10,fill="x")

#giving title as text
#titletext="SMS"
#lblDisplayTitleImage=Label(titleImageFrame,text=titletext).pack()

#giving title as Image
lblDisplayTitleImage=Label(titleImageFrame,image=getTitleImage).pack()

#adding list of tabs
tablist=ttk.Notebook(root_window)
tablist.pack(padx=10, pady=5)

#tabInsert=ttk.Frame(tablist, width=600, height=600) for manuall size in width and height property

#creating tab to adapt window size in width and height property ==> use this == > root_window.winfo_screenheight()
tabInsert=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabInsert.pack()

tabUpdate=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabUpdate.pack()

tabDelete=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabDelete.pack()

tablist.add(tabInsert,text="Insert")
tablist.add(tabUpdate,text="Update")
tablist.add(tabDelete,text="Delete")


titledisplayframeintab=Frame(tabInsert,width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
titledisplayframeintab.pack()

lbl_insertTitle=Label(titledisplayframeintab, text="Inserting Student Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)

lbl_StdName=Label(titledisplayframeintab,text="Name of the student ")
lbl_StdName.grid(pady=10,row=1,column=1)
Ety_StdName=Entry(titledisplayframeintab)
Ety_StdName.grid(padx=10,pady=10,row=1, column=2)



lbl_StdMkTamil=Label(titledisplayframeintab,text="Tamil")
lbl_StdMkTamil.grid(pady=10,row=2,column=1)
Ety_StdMkTamil=Entry(titledisplayframeintab)
Ety_StdMkTamil.grid(padx=10,pady=10,row=2, column=2)


lbl_StdMkEng=Label(titledisplayframeintab,text="Eng")
lbl_StdMkEng.grid(pady=10,row=3,column=1)
Ety_StdMkEng=Entry(titledisplayframeintab)
Ety_StdMkEng.grid(padx=10,pady=10,row=3, column=2)

lbl_StdMkMath=Label(titledisplayframeintab,text="Math")
lbl_StdMkMath.grid(pady=10,row=4,column=1)
Ety_StdMkMath=Entry(titledisplayframeintab)
Ety_StdMkMath.grid(padx=10,pady=10,row=4, column=2)

lbl_StdMkSci=Label(titledisplayframeintab,text="Sci")
lbl_StdMkSci.grid(pady=10,row=5,column=1)
Ety_StdMkSci=Entry(titledisplayframeintab)
Ety_StdMkSci.grid(padx=10,pady=10,row=5, column=2)


lbl_StdMkSS=Label(titledisplayframeintab,text="SS")
lbl_StdMkSS.grid(pady=10,row=6,column=1)
Ety_StdMkSS=Entry(titledisplayframeintab)
Ety_StdMkSS.grid(padx=10,pady=10,row=6, column=2)

btn_Insert=Button(titledisplayframeintab, text="Insert", command=inserttoDB)
btn_Insert.grid(row=7,column=1)

btn_Clear=Button(titledisplayframeintab, text="Clear")
btn_Clear.grid(row=7,column=2)

btn_Exit=Button(titledisplayframeintab, text="Quit", command=exitParent)
btn_Exit.grid(row=7,column=3)


lblConMsg=Label(titledisplayframeintab, text="")
lblConMsg.grid(row=8,column=2, pady=20)


resultframe=Frame(titledisplayframeintab,width=800, height=700,bg="black")
resultframe.grid(row=9, columnspan=6)









# tab update 



titledisplayframeintab=Frame(tabUpdate,width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
titledisplayframeintab.pack()

lbl_update_updateTitle=Label(titledisplayframeintab, text="updateing Student Details")
lbl_update_updateTitle.grid(pady=10,row=0, columnspan=10)

lbl_update_StdName=Label(titledisplayframeintab,text="Name of the student ")
lbl_update_StdName.grid(pady=10,row=1,column=1)
Ety_update_StdName=Entry(titledisplayframeintab)
Ety_update_StdName.grid(padx=10,pady=10,row=1, column=2)



lbl_update_StdMkTamil=Label(titledisplayframeintab,text="Tamil")
lbl_update_StdMkTamil.grid(pady=10,row=2,column=1)
Ety_update_StdMkTamil=Entry(titledisplayframeintab)
Ety_update_StdMkTamil.grid(padx=10,pady=10,row=2, column=2)


lbl_update_StdMkEng=Label(titledisplayframeintab,text="Eng")
lbl_update_StdMkEng.grid(pady=10,row=3,column=1)
Ety_update_StdMkEng=Entry(titledisplayframeintab)
Ety_update_StdMkEng.grid(padx=10,pady=10,row=3, column=2)

lbl_update_StdMkMath=Label(titledisplayframeintab,text="Math")
lbl_update_StdMkMath.grid(pady=10,row=4,column=1)
Ety_update_StdMkMath=Entry(titledisplayframeintab)
Ety_update_StdMkMath.grid(padx=10,pady=10,row=4, column=2)

lbl_update_StdMkSci=Label(titledisplayframeintab,text="Sci")
lbl_update_StdMkSci.grid(pady=10,row=5,column=1)
Ety_update_StdMkSci=Entry(titledisplayframeintab)
Ety_update_StdMkSci.grid(padx=10,pady=10,row=5, column=2)


lbl_update_StdMkSS=Label(titledisplayframeintab,text="SS")
lbl_update_StdMkSS.grid(pady=10,row=6,column=1)
Ety_update_StdMkSS=Entry(titledisplayframeintab)
Ety_update_StdMkSS.grid(padx=10,pady=10,row=6, column=2)

btn_update_update=Button(titledisplayframeintab, text="update", )
btn_update_update.grid(row=7,column=1)

btn_update_Clear=Button(titledisplayframeintab, text="Clear")
btn_update_Clear.grid(row=7,column=2)

btn_update_Exit=Button(titledisplayframeintab, text="Quit", command=exitParent)
btn_update_Exit.grid(row=7,column=3)


lblConMsg=Label(titledisplayframeintab, text="")
lblConMsg.grid(row=8,column=2, pady=20)


resultframe=Frame(titledisplayframeintab,width=800, height=700,bg="black")
resultframe.grid(row=9, columnspan=6)




root_window.mainloop()