from tkinter import *
from tkinter import ttk
hai=Tk()
hai.title("www.onlineportal.com")
hai.geometry("400x400")
hai.state("zoomed")

def login():
    a=tbEntrya.get()
    b=tbEntryb.get()
    if(a=="abdul") & (b=="1234"):
        personaldetails()
    elif(a=="rahman",) & (b=="9876"):
        math_operation()
        
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

labeloutput=Label(hai,text=" ")
labeloutput.grid(row=9,column=30,pady=15)

def personaldetails():
    win=Tk()
    win.title("www.personaldetails.com")
    win.geometry("500x500+500+500")
    win.state("zoomed")
    '''win=Tk()
    win.title("www.personaldetails.com")
    win.geometry("500x500+500+500")
    win.state("zoomed")'''

    def Submit():
        a=tbEntrya.get()
        b=combo.get()
        c=tbEntryc.get()
        d=combo2.get()
        e=combo3.get()
        f=tbEntryf.get()
        labeloutput1.config(text=a)
        labeloutput2.config(text=b)
        labeloutput3.config(text=c)
        labeloutput4.config(text=d)
        labeloutput5.config(text=e)
        labeloutput5.config(text=f)
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
        labeloutput5.config(text=f)


    def optionselected(event):
        selectoption = combo.get()

    def optionselected(event):
        selectoption = combo2.get()

    def optionselected(event):
        seloption = combo3.get()

    Labeltitle=Label(win,text="Personal Details Form",font=("ALGERIAN",20),fg="White",bg="Blue")
    Labeltitle.grid(row=0,column=25)

    label1msg=Label(win,text="Name",font=("Batang",14),fg="black")
    label1msg.grid(row=1,column=20,pady=10)
    tbEntrya=Entry(win, width=60)
    tbEntrya.grid(row=1,column=25)

    label2msg=Label(win,text="Gender",font=("Batang",14),fg="black")
    label2msg.grid(row=2,column=20,pady=10)
    combo=ttk.Combobox(win,values=["-select the gender-","Male","Female","Others"])
    combo.current(0)
    combo.grid(row=2,column=25,pady=10)
    

    label3msg=Label(win,text="D.O.B",font=("Batang",14),fg="black")
    label3msg.grid(row=3,column=20,pady=10)
    tbEntryc=Entry(win, width=60)
    tbEntryc.grid(row=3,column=25)

    label4msg=Label(win,text="Birth City",font=("Batang",14),fg="black")
    label4msg.grid(row=4,column=20,pady=10)
    combo2=ttk.Combobox(win,values=["-select the city-","Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul", "Erode", "Kanchipuram", "Kanyakumari", "Karur", "Krishnagiri", "Madurai", "Nagapattinam", "Namakkal", "Perambalur", "Pudukkottai", "Ramanathapuram", "Salem", "Sivaganga", "Thanjavur", "The Nilgiris", "Theni", "Thoothukudi", "Tiruchirapalli", "Tirunelveli", "Tiruvallur", "Tiruvannamalai", "Tiruvarur", "Vellore", "Viluppuram", "Virudhunagar"])
    combo2.current(0)
    combo2.grid(row=4,column=25)

    label5msg=Label(win,text="State",font=("Batang",14),fg="black")
    label5msg.grid(row=5,column=20,pady=10)
    combo3=ttk.Combobox(win,values=["-select the state-","Andaman & Nicobar Island","Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli","Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Puducherry","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"])
    combo3.current(0)
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

    btnclo=Button(win,text="Close",font=("Batang",14),fg="White",bg="Red", command=close)
    btnclo.grid(row=7,column=3)


    win.mainloop()

def math_operation():
    roo=Tk()
    roo.title("Mathematical Operations")
    roo.geometry("500x500+500+500")
    roo.state("zoomed")

    def Addition():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a+b
        labeloutput.config(text=c)
    def Subtraction():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a-b
        labeloutput.config(text=c)
    def Multiplication():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a*b
        labeloutput.config(text=c)
    def Division():
        a=int(tbEntrya.get())
        b=int(tbEntryb.get())
        c=a/b
        labeloutput.config(text=c)

    Labeltitle=Label(roo,text="Arithematic Operations",font=("ALGERIAN",16),fg="green")
    Labeltitle.grid(row=0,column=20)

    label1msg=Label(roo,text="Enter the Value of A",font=("Lucida Calligraphy",14),fg="blue")
    label1msg.grid(row=1,column=20,pady=20)
    tbEntrya=Entry(roo, width=60)
    tbEntrya.grid(row=1,column=25)

    label2msg=Label(roo,text="Enter the Value of B",font=("Lucida Calligraphy",14),fg="blue")
    label2msg.grid(row=2,column=20,pady=20)
    tbEntryb=Entry(roo, width=60)
    tbEntryb.grid(row=2,column=25)

    labeloutput=Label(roo,text=" ")
    labeloutput.grid(row=3,column=30,pady=20)


    btnadd=Button(roo,text="Addition",font=("calibri",14),fg="White",bg="Black",command=Addition)
    btnadd.grid(row=5,column=1)

    btnsub=Button(roo,text="Subtraction",font=("calibri",14),fg="White",bg="Black",command=Subtraction)
    btnsub.grid(row=5,column=2)

    btnmul=Button(roo,text="Multiplication",font=("calibri",14),fg="White",bg="Black",command=Multiplication)
    btnmul.grid(row=5,column=3)

    btndiv=Button(roo,text="Division",font=("calibri",14),fg="White",bg="Black",command=Division)
    btndiv.grid(row=5,column=4)


    roo.mainloop()


hai.mainloop()