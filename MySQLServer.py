import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust user and password as needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Replace with your actual password if set
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection properly
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
