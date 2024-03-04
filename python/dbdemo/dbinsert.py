import mysql.connector
from tkinter import *
class DBManipulate:
    def __init__(self):
        print("Welcome to Db Manipulation")

    def returnMsg(self):
        return "connected"
    
    def mydbconnection(self):
        con=mysql.connector.connect(
            host="192.168.1.240",
            user="AIBATCH01",
            password="AI@123",
            database="ai_abdulrahman"
        )
        return con

def insertvalues(self,name,tamil,eng,math,sci,ss):
        # student_name=Ety_StdName.get()
        # st_mk_tamil=Ety_StdMkTamil.get()
        # st_mk_eng=Ety_StdMkEng.get()
        # st_mk_math=Ety_StdMkMath.get()
        # st_mk_sci=Ety_StdMkSci.get()
        # st_mk_ss=Ety_StdMkSS.get()

        # student_name="ragu1"
        # st_mk_tamil=202
        # st_mk_eng=622
        # st_mk_math=662
        # st_mk_sci=552
        # st_mk_ss=442

        student_name=name
        st_mk_tamil=tamil
        st_mk_eng=eng
        st_mk_math=math
        st_mk_sci=sci
        st_mk_ss=ss

        data=self.mydbconnection()
        result=data.cursor()

        stmts="INSERT INTO student_ (Name, Tamil, English, Maths, Science, Social) VALUES ( "+ '"' + student_name + '"' + "," + str(st_mk_tamil) + "," + str(st_mk_eng)+","+ str(st_mk_math)  +","+ str(st_mk_sci) +","+ str(st_mk_ss) + ");"
        
       
        

        # result.execute("INSERT INTO student_tables (Name, Tamil, English, Maths, Science, Social) VALUES (\"Abdulrahman\", 601,601,610,610,610);")
        result.execute(stmts)
        print(stmts)



        data.commit()

        return (str(result.rowcount) + " row inserted")

