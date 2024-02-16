from tkinter import *

app=Tk()
app.title("my first python gui app")
app.geometry("500x200+500+100")
app.config(bg="blue")
# app.state("zooned")

lbltitle=Label(app,text="Arithmatic Operations")
lbltitle.grid(row=0, column=1, padx=40, pady=40)

inputbox1=Entry(app,width=30)
inputbox1.grid(row=0, column=2)


lbltitle=Label(app,text="Arithmatic Operations")
lbltitle.grid(row=1, column=1, padx=40, pady=40)

inputbox2=Entry(app,width=30)
inputbox2.grid(row=1, column=2)


clickme=Button(app, text="addition")
clickme.grid(row=1, column=3, padx=40, pady=40)



app.mainloop()