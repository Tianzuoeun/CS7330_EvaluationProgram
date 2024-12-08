import mysql.connector

# Connect to the database sever
def get_connection():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="cs5330",
            password="pw5330",
            database="programevaluation"
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        raise
