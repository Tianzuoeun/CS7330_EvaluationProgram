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
# Insert the instructor info to the database
def insert_instructor(instructor_id, instructor_name):
    query = "INSERT INTO Instructor (instructor_id, instructor_name) VALUES (%s, %s)"
    values = (instructor_id, instructor_name)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Get the instructor info from the database
def fetch_instructors():
    query = "SELECT instructor_id, instructor_name FROM Instructor"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    instructors = cursor.fetchall()
    cursor.close()
    conn.close()
    return instructors

# -------------------------------------------------------------
# Insert the section info to the database
def insert_section(section_id, semester, year, student_num, course_id, instructor_id):
    query = "INSERT INTO Section (section_id, semester, year, student_num, course_id, instructor_id) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (section_id, semester, year, student_num, course_id, instructor_id)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Get the section info from the database
def fetch_sections():
    query = "SELECT section_id, semester, year, student_num, course_id, instructor_id FROM Section"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

# -------------------------------------------------------------
# Insert the goal info to the database
def insert_goal(goal_code, description, degree_name, degree_level):
    query = "INSERT INTO Goal (goal_code, description, degree_name, degree_level) VALUES (%s, %s, %s, %s)"
    values = (goal_code, description, degree_name, degree_level)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# Get the goal info from the database
def fetch_goals():
    query = "SELECT goal_code, description, degree_name, degree_level FROM Goal"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    goals = cursor.fetchall()
    cursor.close()
    conn.close()
    return goals

# -------------------------------------------------------------

# Get info of semester, year, instructor ID and the evaluation status from Database
def fetch_sections_with_evaluations(semester, year, instructor_id):
    query = """
        SELECT Section.section_id, Section.course_id, 
               CASE 
                   WHEN Evaluation.grade_A_count IS NOT NULL THEN 'Complete'
                   ELSE 'Incomplete'
               END AS evaluation_status
        FROM Section
        LEFT JOIN Evaluation 
        ON Section.section_id = Evaluation.section_id 
        AND Section.course_id = Evaluation.course_id
        AND Section.semester = Evaluation.semester
        AND Section.year = Evaluation.year
        WHERE Section.semester = %s AND Section.year = %s AND Section.instructor_id = %s
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (semester, year, instructor_id))
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

# Function to insert or renew the evaluation info/status
def insert_or_update_evaluation(course_id, section_id, semester, year,
                                goal_code, degree_name, degree_level,
                                evaluation_type, grade_A_count, grade_B_count,
                                grade_C_count, grade_F_count, improvement_sug):
    query = """
        INSERT INTO Evaluation (evaluation_id, course_id, section_id, semester, 
        year, goal_code, degree_name, degree_level, evaluation_type, grade_A_count, 
        grade_B_count, grade_C_count, grade_F_count, improvement_sug)
        VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
            evaluation_type = VALUES(evaluation_type),
            grade_A_count = VALUES(grade_A_count),
            grade_B_count = VALUES(grade_B_count),
            grade_C_count = VALUES(grade_C_count),
            grade_F_count = VALUES(grade_F_count),
            improvement_sug = VALUES(improvement_sug)
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (course_id, section_id, semester, year, goal_code,
                           degree_name, degree_level, evaluation_type, grade_A_count,
                           grade_B_count, grade_C_count, grade_F_count, improvement_sug))
    conn.commit()
    cursor.close()
    conn.close()

# -------------------------------------------------------------