import tkinter as tk
from tkinter import messagebox
from utils.db_utils import insert_course, fetch_courses

class CourseView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Mange Courses")
        self.window.geometry("400x300")

        # Insert the course info
        tk.Label(self.window, text="Course ID: ").pack(pady=5)
        self.course_id_entry = tk.Entry(self.window)
        self.course_id_entry.pack()

        tk.Label(self.window, text="Course Name: ").pack(pady=5)
        self.course_name_entry = tk.Entry(self.window)
        self.course_name_entry.pack()

        # Buttons
        tk.Button(self.window, text="Add Course", command=self.add_course).pack(pady=10)
        tk.Button(self.window, text="Show All Courses", command=self.show_courses).pack(pady=10)

    def add_course(self):
        course_id = self.course_id_entry.get()
        course_name = self.course_name_entry.get()

        if course_id and course_name:
            try:
                insert_course(course_id, course_name)
                messagebox.showinfo("Success", "Course added successfully!")
                # Clean the entry
                self.course_id_entry.delete(0, tk.END)
                self.course_name_entry.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_courses(self):
        courses = fetch_courses()
        if courses:
            result = "\n".join([f"{course_id} - {course_name}" for course_id, course_name in courses])
            messagebox.showinfo("Courses", result)
        else:
            messagebox.showinfo("Courses", "No courses found.")
