import os
from tkinter import *
from tkinter import ttk
import mysql.connector

hai=Tk()
hai.title("www.OnlineManagementPortal.com")
hai.geometry("400x400")
hai.state("zoomed")
hai.wm_iconbitmap('dbdemo/football.ico')

def close():
        hai.destroy()

def login():

    a=tbEntrya.get()
    b=tbEntryb.get()
    if(a=="boss") & (b=="12345"):
        personaldetails()
    else:
        labeloutput.config(text="You entered wrong username or password")

label1msg=Label(hai,text="Welcome to login page",font=("TimesNewRoman",20),fg="White",bg="Blue")
label1msg.grid(row=1,column=35,pady=10)

label2msg=Label(hai,text="User Name",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
tbEntrya=Entry(hai, width=60)
tbEntrya.grid(row=2,column=25)

label3msg=Label(hai,text="Password",font=("Batang",14),fg="black")
label3msg.grid(row=3,column=20,pady=10)
tbEntryb=Entry(hai, width=60)
tbEntryb.grid(row=3,column=25)

btnlo=Button(hai,text="Login",font=("Batang",14),fg="White",bg="Green",command=login) 
btnlo.grid(row=7,column=1)

btncl=Button(hai,text="Close",font=("Batang",14),fg="White",bg="Green",command=close) 
btncl.grid(row=7,column=3)

labeloutput=Label(hai,text=" ")
labeloutput.grid(row=9,column=30,pady=15)

def personaldetails():
    win=Tk()
    win.title("www.personaldetails.com")
    win.geometry("500x500+500+500")
    win.state("zoomed")
  #  win.wm_iconbitmap('img\database.ico')

    con=mysql.connector.connect(

    host="192.168.1.240",
    user="AIBATCH01",
    password="AI@123",
    database="ai_abdulrahman"
)

    abdul= con.cursor()

    '''def Submit():
        a=tbEntrya.get()
        b=tbEntryb.get()
        c=combo.get()
        d=tbEntryd.get()
        e=tbEntrye.get()
        
        labeloutput1.config(text=a)
        labeloutput2.config(text=b)
        labeloutput3.config(text=c)
        labeloutput4.config(text=d)
        labeloutput5.config(text=e)'''
         
    def optionselected(event):
        selectoption = combo.get()
    def insert():
        a=tbEntrya.get()
        b=tbEntryb.get()
        c=combo.get()
        d=tbEntryd.get()
        e=tbEntrye.get()
        sql = "INSERT INTO bright_academy (s_no,name,sports,products,quantity) VALUES (%s,%s,%s,%s,%s)"
        val = [a,b,c,d,e]
        abdul.execute(sql,val)
        con.commit()
        print(abdul.rowcount, "record inserted.")
        
    def delete():
        a=tbEntrya.get()
        sql = "DELETE FROM bright_academy WHERE s_no = %s"
        val = [a]
        abdul.execute(sql,val)
        con.commit()
        print(abdul.rowcount, "value deleted.")

    def update():
        a=tbEntrya.get()
        b=tbEntryb.get()
        c=combo.get()
        d=tbEntryd.get()
        e=tbEntrye.get()
        sql = "UPDATE bright_academy SET name= %s, sports=%s, products=%s, quantity=%s WHERE s_no = %s"
        val = [b,c,d,e,a]
        abdul.execute(sql,val)
        con.commit()
        print(abdul.rowcount, "record updated.")

    def close():
        win.destroy()

    Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="White",bg="Blue")
    Labeltitle.grid(row=0,column=25)

    label1msg=Label(win,text="S.No.",font=("Batang",14),fg="black")
    label1msg.grid(row=1,column=20,pady=10)
    tbEntrya=Entry(win, width=60)
    tbEntrya.grid(row=1,column=25)

    label2msg=Label(win,text="Name",font=("Batang",14),fg="black")
    label2msg.grid(row=2,column=20,pady=10)
    tbEntryb=Entry(win, width=60)
    tbEntryb.grid(row=2,column=25)

    label3msg=Label(win,text="Sports",font=("Batang",14),fg="black")
    label3msg.grid(row=3,column=20,pady=10)
    combo=ttk.Combobox(win,values=["-select the Sports-","Cricket","Hockey","Badmittion","Baseball","Carromboard","Volleyball","Football"])
    combo.current(0)
    combo.grid(row=3,column=25,pady=10)
    

    label4msg=Label(win,text="Products",font=("Batang",14),fg="black")
    label4msg.grid(row=4,column=20,pady=10)
    tbEntryd=Entry(win, width=60)
    tbEntryd.grid(row=4,column=25)

    label5msg=Label(win,text="Quantity",font=("Batang",14),fg="black")
    label5msg.grid(row=5,column=20,pady=10)
    tbEntrye=Entry(win, width=60)
    tbEntrye.grid(row=5,column=25)

    labeloutput1=Label(win,text=" ")
    labeloutput1.grid(row=8,column=30,pady=15)    

    btnsub=Button(win,text="Insert",font=("Batang",14),fg="Black",bg="Green",command=insert)
    btnsub.grid(row=7,column=1)

    btnclr=Button(win,text="Update",font=("Batang",14),fg="Black",bg="Yellow", command=update)
    btnclr.grid(row=7,column=2)

    btndel=Button(win,text="Delete",font=("Batang",14),fg="Black",bg="Blue", command=delete)
    btndel.grid(row=7,column=3)

    btnclo=Button(win,text="Close",font=("Batang",14),fg="Black",bg="Red", command=close)
    btnclo.grid(row=7,column=4)

    win.mainloop()


hai.mainloop()