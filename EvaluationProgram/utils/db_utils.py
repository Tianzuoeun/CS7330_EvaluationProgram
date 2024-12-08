from db_config import get_connection

# Insert the degree info to the database
def insert_degree(degree_name, degree_level):
    query = "INSERT INTO Degree (degree_name, degree_level) VALUES (%s, %s)"
    values = (degree_name, degree_level)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Get the degree info from the database
def fetch_degrees():
    query = "SELECT degree_name, degree_level FROM Degree"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    degrees = cursor.fetchall()
    cursor.close()
    conn.close()
    return degrees

