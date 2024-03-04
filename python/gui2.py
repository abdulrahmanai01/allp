from tkinter import *
from tkinter import ttk
win=Tk()
win.title("www.personaldetails.com")
win.geometry("500x500+500+500")
win.state("zoomed")

def Submit():
    a=tbEntrya.get()
    #b=tbEntryb.get()
    #b=combo.get()
    b=radio.get()
    c=tbEntryc.get()
    #d=tbEntryd.get()
    d=combo2.get()
    #e=tbEntrye.get()
    e=combo3.get()
    f=tbEntryf.get()
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)
    labeloutput6.config(text=f)
def Clear():
    a=" "
    b=" "
    c=" "
    d=" "
    e=" "
    f=" "
    labeloutput1.config(text=a)
    labeloutput2.config(text=b)
    labeloutput3.config(text=c)
    labeloutput4.config(text=d)
    labeloutput5.config(text=e)
    labeloutput6.config(text=f)

def close():
   win.destroy()
    
   

def optionselected(event):
   selectoption = combo2.get()

def optionselected(event):
   seloption = combo3.get()

Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="White",bg="Blue")
Labeltitle.grid(row=0,column=25)

label1msg=Label(win,text="Name",font=("Batang",14),fg="blue",bg="yellow")
label1msg.grid(row=1,column=20,pady=10)
tbEntrya=Entry(win, width=60)
tbEntrya.grid(row=1,column=25)

'''label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
tbEntryb=Entry(win, width=60)
tbEntryb.grid(row=2,column=25)'''

label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
label2msg.grid(row=2,column=20,pady=10)
'''combo=ttk.Combobox(win,values=["Male","Female","Others"])
combo.grid(row=2,column=25,pady=10)'''
radio=IntVar()
r1=Radiobutton(win,text="Male",variable=radio,value=1,font=("Batang",14),fg="Black")
r1.grid(row=2,column=24)
r2=Radiobutton(win,text="Female",variable=radio,value=2,font=("Batang",14),fg="Black")
r2.grid(row=2,column=25)
r3=Radiobutton(win,text="OThers",variable=radio,value=3,font=("Batang",14),fg="Black")
r3.grid(row=2,column=26)

label3msg=Label(win,text="D.O.B",font=("Batang",14),fg="black")
label3msg.grid(row=3,column=20,pady=10)
tbEntryc=Entry(win, width=60)
tbEntryc.grid(row=3,column=25)

label4msg=Label(win,text="Birth City",font=("Batang",14),fg="black")
label4msg.grid(row=4,column=20,pady=10)
'''tbEntryd=Entry(win, width=60)
tbEntryd.grid(row=4,column=25)'''
combo2=ttk.Combobox(win,values=["Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Nagapattinam", "Namakkal", "Perambalur", "Pudukkottai", "Ramanathapuram", "Salem", "Sivaganga", "Thanjavur", "The Nilgiris", "Theni", "Thoothukudi", "Tiruchirapalli", "Tirunelveli", "Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar"])
combo2.grid(row=4,column=25)

label5msg=Label(win,text="State",font=("Batang",14),fg="black")
label5msg.grid(row=5,column=20,pady=10)
#tbEntrye=Entry(win, width=60)
#tbEntrye.grid(row=5,column=25)
combo3=ttk.Combobox(win,values=["Andaman & Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli","Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])
combo3.grid(row=5,column=25)

label6msg=Label(win,text="Phone No.",font=("Batang",14),fg="black")
label6msg.grid(row=6,column=20,pady=10)
tbEntryf=Entry(win, width=60)
tbEntryf.grid(row=6,column=25)

labeloutput1=Label(win,text=" ")
labeloutput1.grid(row=8,column=30,pady=15)
labeloutput2=Label(win,text=" ")
labeloutput2.grid(row=9,column=30,pady=15)
labeloutput3=Label(win,text=" ")
labeloutput3.grid(row=10,column=30,pady=15)
labeloutput4=Label(win,text=" ")
labeloutput4.grid(row=11,column=30,pady=15)
labeloutput5=Label(win,text=" ")
labeloutput5.grid(row=12,column=30,pady=15)

btnsub=Button(win,text="Submit",font=("Batang",14),fg="White",bg="Green",command=Submit)
btnsub.grid(row=7,column=1)

btnclr=Button(win,text="Clear",font=("Batang",14),fg="White",bg="Blue", command=Clear)
btnclr.grid(row=7,column=2)

btnclo=Button(win,text="Close",font=("Batang",14),fg="White",bg="Red",command=close)
btnclo.grid(row=7,column=3)

win.mainloop()