import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sagar#123'
)

print (conn)
