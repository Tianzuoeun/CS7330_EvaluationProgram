import tkinter as tk
from tkinter import messagebox
from utils.db_utils import insert_section, fetch_sections

class SectionView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Mange Sections")
        self.window.geometry("400x300")

        # Insert the section info
        tk.Label(self.window, text="Section ID: ").pack(pady=5)
        self.section_id_entry = tk.Entry(self.window)
        self.section_id_entry.pack()

        tk.Label(self.window, text="Semester: ").pack(pady=5)
        self.semester_entry = tk.Entry(self.window)
        self.semester_entry.pack()

        tk.Label(self.window, text="Year: ").pack(pady=5)
        self.year_entry = tk.Entry(self.window)
        self.year_entry.pack()

        tk.Label(self.window, text="Student Num: ").pack(pady=5)
        self.student_num_entry = tk.Entry(self.window)
        self.student_num_entry.pack()

        tk.Label(self.window, text="Course ID: ").pack(pady=5)
        self.course_id_entry = tk.Entry(self.window)
        self.course_id_entry.pack()

        tk.Label(self.window, text="Instructor ID: ").pack(pady=5)
        self.instructor_id_entry = tk.Entry(self.window)
        self.instructor_id_entry.pack()

        # Buttons
        tk.Button(self.window, text="Add Section", command=self.add_section).pack(pady=10)
        tk.Button(self.window, text="Show All Sections", command=self.show_sections).pack(pady=10)

    def add_section(self):
        section_id = self.section_id_entry.get()
        semester = self.semester_entry.get()
        year = self.year_entry.get()
        student_num = self.student_num_entry.get()
        course_id = self.course_id_entry.get()
        instructor_id = self.instructor_id_entry.get()

        if section_id and semester and year and student_num and course_id and instructor_id:
            try:
                insert_section(section_id, semester, year, student_num, course_id, instructor_id)
                messagebox.showinfo("Success", "Section added successfully!")
                # Clean the entry
                self.section_id_entry.delete(0, tk.END)
                self.semester_entry.delete(0, tk.END)
                self.year_entry.delete(0, tk.END)
                self.student_num_entry.delete(0, tk.END)
                self.course_id_entry.delete(0, tk.END)
                self.instructor_id_entry.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_sections(self):
        sections = fetch_sections()
        if sections:
            result = "\n".join([f"{section_id} - {semester} - {year} - {student_num} - {course_id} - {instructor_id}" for section_id, semester, year, student_num, course_id, instructor_id in sections])
            messagebox.showinfo("Sections", result)
        else:
            messagebox.showinfo("Sections", "No sections found.")
