import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234'

)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE elder")
print("Database created")