#!C:\Users\Supergood\AppData\Local\Programs\Python\Python38-32\python.exe

import mysql.connector
import cgi

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    db='basic_cgi_app',
)
mcursor=conn.cursor()
data=cgi.FieldStorage()
first_range=data.getvalue('first_range')
second_range=data.getvalue('second_range')
sql="insert into inputValues(firstRange, secondRange) values(%s, %s)"
val=(first_range, second_range)
mcursor.execute(sql, val)
conn.commit()
mcursor.close()
conn.close()
print('Location: index.html\r\n\r\n')