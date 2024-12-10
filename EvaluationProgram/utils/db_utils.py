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
def fetch_instructor():
    query = "SELECT instructor_id, instructor_name FROM Instructor"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    instructors = cursor.fetchall()
    cursor.close()
    conn.close()
    return instructors

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

def fetch_courses_by_degree(degree_name, degree_level):
    query = "SELECT course_id, course_name FROM Course WHERE degree_name = %s AND degree_level = %s"
    values = (degree_name, degree_level)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return courses

def fetch_sections_by_degree_in_time_range(degree_name, degree_level, degree_year_minimum, degree_year_maximum, degree_semester_minimum, degree_semester_maximum):
    query = "Select section_id, semester, year, student_num, course_id, instructor_id FROM Section WHERE course_id = %s AND year >= %s AND year <=%s"
    courses = fetch_courses_by_degree(degree_name, degree_level)
    conn = get_connection()
    cursor = conn.cursor()

    sections = []
    
    for course in courses:
        values = (course.course_id, degree_year_minimum, degree_year_maximum)
        cursor.execute(query, values)
        sections_query = cursor.fetchall()
        for section_query in sections_query:
            sections.extend(section_query)
        
    cursor.close()
    conn.close()

    if (degree_semester_minimum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
    if (degree_semester_minimum == "Fall"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
            if section.year == degree_year_minimum and section.semester == "Summer":
                sections.remove(section)
    if (degree_semester_maximum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)
    if (degree_semester_maximum == "Spring"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Summer":
                sections.remove(section)
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)

    sorted_sections = sorted(sections, key=lambda section: (section.year))
    return sorted_sections

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

def fetch_sections_by_course_in_time_range(course_id, degree_year_minimum, degree_year_maximum, degree_semester_minimum, degree_semester_maximum):
    query = "Select section_id, semester, year, student_num, course_id, instructor_id FROM Section WHERE course_id = %s AND year >= %s AND year <=%s"
    values = (course_id, degree_year_minimum, degree_year_maximum)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()

    if (degree_semester_minimum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
    if (degree_semester_minimum == "Fall"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
            if section.year == degree_year_minimum and section.semester == "Summer":
                sections.remove(section)
    if (degree_semester_maximum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)
    if (degree_semester_maximum == "Spring"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Summer":
                sections.remove(section)
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)

    sorted_sections = sorted(sections, key=lambda section: (section.year))
    return sorted_sections

def fetch_sections_by_instructor_in_time_range(instructor_id, degree_year_minimum, degree_year_maximum, degree_semester_minimum, degree_semester_maximum):
    query = "Select section_id, semester, year, student_num, course_id, instructor_id FROM Section WHERE instructor_id = %s  AND year >= %s AND year <=%s"
    values = (instructor_id, degree_year_minimum, degree_year_maximum)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()

    if (degree_semester_minimum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
    if (degree_semester_minimum == "Fall"):
        for section in sections[::-1]:
            if section.year == degree_year_minimum and section.semester == "Spring":
                sections.remove(section)
            if section.year == degree_year_minimum and section.semester == "Summer":
                sections.remove(section)
    if (degree_semester_maximum == "Summer"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)
    if (degree_semester_maximum == "Spring"):
        for section in sections[::-1]:
            if section.year == degree_year_maximum and section.semester == "Summer":
                sections.remove(section)
            if section.year == degree_year_maximum and section.semester == "Fall":
                sections.remove(section)

    sorted_sections = sorted(sections, key=lambda section: (section.year))
    return sorted_sections

def fetch_evaluation_info_by_semester(semester):
    query = "Select section_id, semester, year, student_num, course_id, instructor_id FROM Section WHERE semester = %s"
    values = (semester)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()

    eval_info = "No Info"

    for section in sections:
        eval_info = fetch_evaluation_status_by_section(section)
        section.eval_info = eval_info

    return sections

def fetch_evaluation_status_by_section(section_id):
    query = "Select evaluation_id, evaluation_type, grade_A_count, grade_B_count, grade_C_count, grade_F_count, improvement_sug, course_id, section_id, semester, year, goal_code, degree_name, degree_level FROM Evaluation WHERE section_id = %s"
    values = (section_id)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    evaluations = cursor.fetchall()
    cursor.close()
    conn.close()

    evaluation = evaluations[0]
    evaluation_status = "Full Info"

    if evaluation.improvement_sug == None:
        evaluation_status = "No Improvement Suggestion"
    if evaluation.evaluation_type == None or evaluation.grade_A_count == None or evaluation.grade_B_count == None or evaluation.grade_C_count == None or evaluation.grade_F_count == None:
        evaluation_status = "Partial Info"
    if evaluation.evaluation_type == None and evaluation.grade_A_count == None and evaluation.grade_B_count == None and evaluation.grade_C_count == None and evaluation.grade_F_count == None and evaluation.improvement_sug == None:
        evaluation_status = "No Info"

    return evaluation_status

def fetch_sections_by_percent_passing(percentage):
    query = "Select evaluation_id, evaluation_type, grade_A_count, grade_B_count, grade_C_count, grade_F_count, improvement_sug, course_id, section_id, semester, year, goal_code, degree_name, degree_level FROM Evaluation"
    percent = float(percentage)
    f_max = 1-percent

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    evaluations = cursor.fetchall()

    sections = []

    for evaluation in evaluations:
        if (f_max <= (evaluation.grade_F_count)/(evaluation.grade_A_count + evaluation.grade_B_count + evaluation.grade_C_count + evaluation.grade_F_count)):
            sectionFetch = fetch_sections_by_section_id(evaluation.section_id)
            section = sectionFetch[0]
            sections.extend(section)
    
    cursor.close()
    conn.close()

    return sections

def fetch_sections_by_section_id(section_id):
    query = "Select section_id, semester, year, student_num, course_id, instructor_id FROM Section WHERE section_id = %s"
    values = (section_id)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    sections = cursor.fetchall()
    cursor.close()
    conn.close()
    return sections