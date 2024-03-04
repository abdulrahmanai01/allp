import mysql.connector
con = mysql.connector.connect(host="192.168.1.240",
                              user="AIBATCH01",
                              password="AI@123",
                              database="ai_prasanth")

print(con)
result = con.cursor()
result.execute("show tables")
result_show = result.fetchall()
for x in result_show:
    print(x)


result.execute("select * from ai_batch01")
result_show = result.fetchall()

for value in result_show:
    print (value)

result.execute("select * from std_info")
result_show = result.fetchall()

for value in result_show:
    print (value)

result.execute ("insert from std_info where Reg no=16 ")
result.execute("select * from std_info")
result_show = result.fetchall()

for value in result_show:
 print (value)
