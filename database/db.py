import mysql.connector
from mysql.connector import Error

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='storage_db',  
            user='root',  
            password=''  
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
