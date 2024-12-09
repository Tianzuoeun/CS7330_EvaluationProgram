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

# -------------------------------------------------------------
# Insert the course info to the database
def insert_course(course_id, course_name):
    query = "INSERT INTO Course (course_id, course_name) VALUES (%s, %s)"
    values = (course_id, course_name)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Get the course info from the database
def fetch_courses():
    query = "SELECT course_id, course_name FROM Course"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses

# User can delete a course by entering course id
def delete_course(course_id):
    query = "DELETE FROM Course WHERE course_id = %s"
    values = (course_id,)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    rows_deleted = cursor.rowcount  # get the affected rows
    conn.commit()
    cursor.close()
    conn.close()
    return rows_deleted


# -------------------------------------------------------------
#