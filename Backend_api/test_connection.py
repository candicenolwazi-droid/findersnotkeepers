import mysql.connector

try:
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="CHANGE_ME",
        database="test_db"          
    )
    print("Connected successfully")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
