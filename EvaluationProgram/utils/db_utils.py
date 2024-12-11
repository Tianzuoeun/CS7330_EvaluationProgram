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

# Insert the course info with degree into the Degree_Course Table
def insert_degree_course(degree_name, degree_level, course_id):
    query = """
        INSERT INTO Degree_Course (degree_name, degree_level, course_id)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE degree_name = VALUES(degree_name), degree_level = VALUES(degree_level)
    """
    values = (degree_name, degree_level, course_id)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

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
        SELECT 
            Section.section_id, 
            Section.course_id, 
            MAX(Evaluation.evaluation_id) AS evaluation_id, 
            MAX(Evaluation.evaluation_type) AS evaluation_type,  
            MAX(Evaluation.grade_A_count) AS grade_A_count, 
            MAX(Evaluation.grade_B_count) AS grade_B_count, 
            MAX(Evaluation.grade_C_count) AS grade_C_count, 
            MAX(Evaluation.grade_F_count) AS grade_F_count, 
            MAX(Evaluation.improvement_sug) AS improvement_sug,
            GROUP_CONCAT(DISTINCT Degree_Course.degree_name) AS degree_names, 
            GROUP_CONCAT(DISTINCT Degree_Course.degree_level) AS degree_levels,
            CASE 
                WHEN MAX(Evaluation.grade_A_count) IS NOT NULL 
                     AND MAX(Evaluation.grade_B_count) IS NOT NULL 
                     AND MAX(Evaluation.grade_C_count) IS NOT NULL 
                     AND MAX(Evaluation.grade_F_count) IS NOT NULL 
                     AND MAX(Evaluation.evaluation_type) IS NOT NULL 
                     AND MAX(Evaluation.improvement_sug) IS NOT NULL THEN 'Complete'
                ELSE 'Incomplete'
            END AS evaluation_status
        FROM Section
        LEFT JOIN Evaluation 
            ON Section.section_id = Evaluation.section_id 
            AND Section.course_id = Evaluation.course_id
            AND Section.semester = Evaluation.semester
            AND Section.year = Evaluation.year
        LEFT JOIN Degree_Course 
            ON Section.course_id = Degree_Course.course_id
        WHERE Section.semester = %s 
          AND Section.year = %s 
          AND Section.instructor_id = %s
        GROUP BY Section.section_id, Section.course_id
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (semester, year, instructor_id))
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

# Function to insert or renew the evaluation info/status
def insert_or_update_evaluation(evaluation_id, course_id, section_id, semester, year,
                                goal_code, degree_name, degree_level,
                                evaluation_type, grade_A_count, grade_B_count,
                                grade_C_count, grade_F_count, improvement_sug):
    query = """
        INSERT INTO Evaluation (evaluation_id, course_id, section_id, semester, 
        year, goal_code, degree_name, degree_level, evaluation_type, grade_A_count, 
        grade_B_count, grade_C_count, grade_F_count, improvement_sug)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 
                %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            evaluation_type = VALUES(evaluation_type),
            grade_A_count = VALUES(grade_A_count),
            grade_B_count = VALUES(grade_B_count),
            grade_C_count = VALUES(grade_C_count),
            grade_F_count = VALUES(grade_F_count),
            improvement_sug = VALUES(improvement_sug);
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Make the none-required fields to None
    evaluation_type = evaluation_type if evaluation_type else None
    improvement_sug = improvement_sug if improvement_sug else None

    cursor.execute(query, (
        evaluation_id, course_id, section_id, semester, year, goal_code,
        degree_name, degree_level, evaluation_type, grade_A_count,
        grade_B_count, grade_C_count, grade_F_count, improvement_sug
    ))

    conn.commit()
    cursor.close()
    conn.close()

# Check if the evaluation is duplicated
def check_evaluation_id(evaluation_id):
    query = "SELECT evaluation_id FROM Evaluation WHERE evaluation_id = %s"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, (evaluation_id,))
    exists = cursor.fetchone()
    cursor.close()
    conn.close()
    return exists is not None

# -------------------------------------------------------------
# Querying Part
def fetch_courses_by_degree(degree_name, degree_level):
    query = """
        SELECT c.course_id, c.course_name 
        FROM Degree_Course dc
        JOIN Course c ON dc.course_id = c.course_id
        WHERE dc.degree_name = %s AND dc.degree_level = %s
    """
    values = (degree_name, degree_level)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses


def fetch_sections_by_degree_in_time_range(degree_name, degree_level, year_min, year_max, semester_min, semester_max):
    query = """
        SELECT s.section_id, s.semester, s.year, s.student_num, s.course_id, s.instructor_id
        FROM Section s
        JOIN Degree_Course dc ON s.course_id = dc.course_id
        WHERE dc.degree_name = %s AND dc.degree_level = %s
          AND s.year BETWEEN %s AND %s
          AND (FIELD(s.semester, 'Spring', 'Summer', 'Fall') 
               BETWEEN FIELD(%s, 'Spring', 'Summer', 'Fall') 
               AND FIELD(%s, 'Spring', 'Summer', 'Fall'))
        ORDER BY s.year, FIELD(s.semester, 'Spring', 'Summer', 'Fall');
    """
    values = (degree_name, degree_level, year_min, year_max, semester_min, semester_max)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections



def fetch_goals_by_degree(degree_name, degree_level):
    query = "SELECT goal_code, description, degree_name, degree_level FROM Goal WHERE degree_name = %s AND degree_level = %s"
    values = (degree_name, degree_level)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    goals = cursor.fetchall()
    cursor.close()
    conn.close()
    return goals


def fetch_sections_by_course_in_time_range(course_id, year_min, year_max, semester_min, semester_max):
    query = """
        SELECT section_id, semester, year, student_num, course_id, instructor_id
        FROM Section
        WHERE course_id = %s
          AND year BETWEEN %s AND %s
          AND (FIELD(semester, 'Spring', 'Summer', 'Fall') 
               BETWEEN FIELD(%s, 'Spring', 'Summer', 'Fall') 
               AND FIELD(%s, 'Spring', 'Summer', 'Fall'))
        ORDER BY year, FIELD(semester, 'Spring', 'Summer', 'Fall');
    """
    values = (course_id, year_min, year_max, semester_min, semester_max)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections


def fetch_sections_by_instructor_in_time_range(instructor_id, year_min, year_max, semester_min, semester_max):
    query = """
        SELECT section_id, semester, year, student_num, course_id, instructor_id
        FROM Section
        WHERE instructor_id = %s
          AND year BETWEEN %s AND %s
          AND (FIELD(semester, 'Spring', 'Summer', 'Fall') 
               BETWEEN FIELD(%s, 'Spring', 'Summer', 'Fall') 
               AND FIELD(%s, 'Spring', 'Summer', 'Fall'))
        ORDER BY year, FIELD(semester, 'Spring', 'Summer', 'Fall');
    """
    values = (instructor_id, year_min, year_max, semester_min, semester_max)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

def fetch_evaluation_status_by_semester(semester, year):
    query = """
        SELECT 
            Section.section_id,
            Section.course_id,
            CASE
                WHEN Evaluation.evaluation_id IS NULL THEN 'Not Entered'
                WHEN Evaluation.evaluation_type IS NULL OR Evaluation.improvement_sug IS NULL THEN 'Partially Entered'
                ELSE 'Complete'
            END AS evaluation_status
        FROM Section
        LEFT JOIN Evaluation 
            ON Section.section_id = Evaluation.section_id 
            AND Section.course_id = Evaluation.course_id
            AND Section.semester = Evaluation.semester
            AND Section.year = Evaluation.year
        WHERE Section.semester = %s AND Section.year = %s;
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (semester, year))
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections

def fetch_sections_with_non_f_percentage(semester, year, percentage_threshold):
    query = """
        SELECT 
            Section.section_id,
            Section.course_id,
            (100.0 * (grade_A_count + grade_B_count + grade_C_count) / 
                (grade_A_count + grade_B_count + grade_C_count + grade_F_count)) AS non_f_percentage
        FROM Section
        JOIN Evaluation 
            ON Section.section_id = Evaluation.section_id 
            AND Section.course_id = Evaluation.course_id
            AND Section.semester = Evaluation.semester
            AND Section.year = Evaluation.year
        WHERE Section.semester = %s AND Section.year = %s
        HAVING non_f_percentage >= %s;
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, (semester, year, percentage_threshold))
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections