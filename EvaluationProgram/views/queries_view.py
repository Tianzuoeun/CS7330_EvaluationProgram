import tkinter as tk
from tkinter import messagebox
from utils.db_utils import fetch_courses_by_degree, fetch_sections_by_degree_in_time_range, fetch_goals_by_degree, fetch_sections_by_course_in_time_range, fetch_sections_by_instructor_in_time_range

class QueriesView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Manage Queries")
        self.window.geometry("400x300")

        tk.Label(self.window, text="Degree Name: ").pack(pady=5)
        self.degree_name_entry = tk.Entry(self.window)
        self.degree_name_entry.pack()

        tk.Label(self.window, text="Degree Level: ").pack(pady=5)
        self.degree_level_entry = tk.Entry(self.window)
        self.degree_level_entry.pack()

        tk.Label(self.window, text="Year Minimum: ").pack(pady=5)
        self.degree_year_minimum_entry = tk.Entry(self.window)
        self.degree_year_minimum_entry.pack()

        tk.Label(self.window, text="Semester Minimum: ").pack(pady=5)
        self.degree_semester_minimum_entry = tk.Entry(self.window)
        self.degree_semester_minimum_entry.pack()

        tk.Label(self.window, text="Year Maximum: ").pack(pady=5)
        self.degree_year_maximum_entry = tk.Entry(self.window)
        self.degree_year_maximum_entry.pack()

        tk.Label(self.window, text="Semester Maximum: ").pack(pady=5)
        self.degree_semester_maximum_entry = tk.Entry(self.window)
        self.degree_semester_maximum_entry.pack()

        # Query by degree
        tk.Button(self.window, text="Show  All Courses", command=self.show_all_courses).pack(pady=10)
        tk.Button(self.window, text="Show All Sections In Time Range", command=self.show_all_sections_in_time_range_by_degree).pack(pady=10)
        tk.Button(self.window, text="Show All Goals", command=self.show_all_goals).pack(pady=10)

        tk.Label(self.window, text="Course ID: ").pack(pady=5)
        self.course_id_entry = tk.Entry(self.window)
        self.course_id_entry.pack()

        tk.Label(self.window, text="Year Minimum: ").pack(pady=5)
        self.course_year_minimum_entry = tk.Entry(self.window)
        self.course_year_minimum_entry.pack()

        tk.Label(self.window, text="Semester Minimum: ").pack(pady=5)
        self.course_semester_minimum_entry = tk.Entry(self.window)
        self.course_semester_minimum_entry.pack()

        tk.Label(self.window, text="Year Maximum: ").pack(pady=5)
        self.course_year_maximum_entry = tk.Entry(self.window)
        self.course_year_maximum_entry.pack()

        tk.Label(self.window, text="Semester Maximum: ").pack(pady=5)
        self.course_semester_maximum_entry = tk.Entry(self.window)
        self.course_semester_maximum_entry.pack()
        
        # Query by course
        tk.Button(self.window, text="Show All Sections In Time Range", command=self.show_all_sections_in_time_range_by_course).pack(pady=10)

        tk.Label(self.window, text="Instructor ID: ").pack(pady=5)
        self.instructor_id_entry = tk.Entry(self.window)
        self.instructor_id_entry.pack()

        tk.Label(self.window, text="Year Minimum: ").pack(pady=5)
        self.instructor_year_minimum_entry = tk.Entry(self.window)
        self.instructor_year_minimum_entry.pack()

        tk.Label(self.window, text="Semester Minimum: ").pack(pady=5)
        self.instructor_semester_minimum_entry = tk.Entry(self.window)
        self.instructor_semester_minimum_entry.pack()

        tk.Label(self.window, text="Year Maximum: ").pack(pady=5)
        self.instructor_year_maximum_entry = tk.Entry(self.window)
        self.instructor_year_maximum_entry.pack()

        tk.Label(self.window, text="Semester Maximum: ").pack(pady=5)
        self.instructor_semester_maximum_entry = tk.Entry(self.window)
        self.instructor_semester_maximum_entry.pack()

        # Query by instructor
        tk.Button(self.window, text="Show All Sections", command=self.show_all_sections_in_time_range_by_instructor).pack(pady=10)

        tk.Label(self.window, text="Goal Code: ").pack(pady=5)
        self.goal_code_entry = tk.Entry(self.window)
        self.goal_code_entry.pack()

        tk.Label(self.window, text="Degree Name: ").pack(pady=5)
        self.goal_degree_name_entry = tk.Entry(self.window)
        self.goal_degree_name_entry.pack()

        tk.Label(self.window, text="Degree Level: ").pack(pady=5)
        self.goal_degree_level_entry = tk.Entry(self.window)
        self.goal_degree_level_entry.pack()

        # Query by goal
        tk.Button(self.window, text="Show All Sections", command=self.show_all_courses_by_goal).pack(pady=10)

        # Query by evaluation

    def show_all_courses(self):
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()

        if degree_name and degree_level:
            try:
                courses = fetch_courses_by_degree(degree_name, degree_level)
                if courses:
                    result = "\n".join([f"{course_id} - {course_name}" for course_id, course_name in courses])
                    messagebox.showinfo("Courses", result)
                else:
                    messagebox.showinfo("Courses", "No courses found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_all_sections_in_time_range_by_degree(self):
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()
        degree_year_minimum = self.degree_year_minimum_entry.get()
        degree_year_maximum = self.degree_year_maximum_entry.get()
        degree_semester_minimum = self.degree_semester_minimum_entry.get()
        degree_semester_maximum = self.degree_semester_maximum_entry.get()

        if degree_name and degree_level and degree_year_minimum and degree_year_maximum and degree_semester_minimum and degree_semester_maximum:
            try:
                sections = fetch_sections_by_degree_in_time_range(degree_name, degree_level, degree_year_minimum, degree_year_maximum, degree_semester_minimum, degree_semester_maximum)
                if sections:
                    result = "\n".join([f"{section_id} - {semester} - {year} - {student_num} - {course_id} - {instructor_id}" for section_id, semester, year, student_num, course_id, instructor_id in sections])
                    messagebox.showinfo("Sections", result)
                else:
                    messagebox.showinfo("Sections", "No sections found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")
    
    def show_all_goals(self):
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()

        if degree_name and degree_level:
            try:
                goals = fetch_goals_by_degree(degree_name, degree_level)
                if goals:
                    result = "\n".join([f"{goal_code} - {description} - {degree_name} - {degree_level}" for goal_code, description, degree_name, degree_level in goals])
                    messagebox.showinfo("Goals", result)
                else:
                    messagebox.showinfo("Goals", "No goals found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_all_sections_in_time_range_by_course(self):
        course_id = self.course_id_entry.get()
        course_year_minimum = self.course_year_minimum_entry.get()
        course_year_maximum = self.course_year_maximum_entry.get()
        course_semester_minimum = self.course_semester_minimum_entry.get()
        course_semester_maximum = self.course_semester_maximum_entry.get()

        if course_id and course_year_minimum and course_year_maximum and course_semester_minimum and course_semester_maximum:
            try:
                sections = fetch_sections_by_course_in_time_range(course_id, course_year_minimum, course_year_maximum, course_semester_minimum, course_semester_maximum)
                if sections:
                    result = "\n".join([f"{section_id} - {semester} - {year} - {student_num} - {course_id} - {instructor_id}" for section_id, semester, year, student_num, course_id, instructor_id in sections])
                    messagebox.showinfo("Sections", result)
                else:
                    messagebox.showinfo("Sections", "No sections found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_all_sections_in_time_range_by_instructor(self):
        instructor_id = self.instructor_id_entry.get()
        instructor_year_minimum = self.instructor_year_minimum_entry.get()
        instructor_year_maximum = self.instructor_year_maximum_entry.get()
        instructor_semester_minimum = self.instructor_semester_minimum_entry.get()
        instructor_semester_maximum = self.instructor_semester_maximum_entry.get()

        if instructor_id and instructor_year_minimum and instructor_year_maximum and instructor_semester_minimum and instructor_semester_maximum:
            try:
                sections = fetch_sections_by_instructor_in_time_range(instructor_id, instructor_year_minimum, instructor_year_maximum, instructor_semester_minimum, instructor_semester_maximum)
                if sections:
                    result = "\n".join([f"{section_id} - {semester} - {year} - {student_num} - {course_id} - {instructor_id}" for section_id, semester, year, student_num, course_id, instructor_id in sections])
                    messagebox.showinfo("Sections", result)
                else:
                    messagebox.showinfo("Sections", "No sections found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_all_courses_by_goal(self):
        goal_code = self.goal_code_entry.get()
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()

        if goal_code and degree_name and degree_level:
            try:
                courses = fetch_courses_by_degree(degree_name, degree_level)
                if courses:
                    result = "\n".join([f"{course_id} - {course_name}" for course_id, course_name in courses])
                    messagebox.showinfo("Courses", result)
                else:
                    messagebox.showinfo("Courses", "No courses found.")

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")