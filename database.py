import mysql.connector
from mysql.connector import Error


DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "root",
    "database": "food_waste",
}


def get_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if not connection.is_connected():
            raise RuntimeError("MySQL connection failed.")

        return connection

    except Error as e:
        raise RuntimeError(f"MySQL connection error: {e}")