from tkinter import *

app=Tk()
app.title("stud marks")
app.geometry("500x200+500+100")
app.config(bg="red")
# app.state("zooned")

lbltitle=Label(app,text="Name")
lbltitle.grid(row=0, column=1, padx=40, pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)

lbltitle=Label(app,text="Roll mo")
lbltitle.grid(row=1, column=1, padx=40, pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=1, column=2)


clickme=Button(app, text="Insert")
clickme.grid(row=5, column=1, padx=40, pady=40)


app.mainloop()