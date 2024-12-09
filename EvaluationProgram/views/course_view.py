import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from utils.db_utils import insert_course, fetch_courses, delete_course

class CourseView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Mange Courses")
        self.window.geometry("600x600")

        # Insert the course info
        tk.Label(self.window, text="Course ID: ").pack(pady=5)
        self.course_id_entry = tk.Entry(self.window)
        self.course_id_entry.pack()

        tk.Label(self.window, text="Course Name: ").pack(pady=5)
        self.course_name_entry = tk.Entry(self.window)
        self.course_name_entry.pack()
        # Add course Button
        tk.Button(self.window, text="Add Course", command=self.add_course).pack(pady=10)
        # Show the Courses in Treeview Table
        self.course_tree = ttk.Treeview(self.window, columns=("ID", "Name"), show="headings")
        self.course_tree.heading("ID", text="CourseID")
        self.course_tree.heading("Name", text="Course Name")
        self.course_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Delete Course Function
        tk.Label(self.window, text="Course ID to Delete: ").pack(pady=5)
        self.course_id_delete_entry = tk.Entry(self.window)
        self.course_id_delete_entry.pack()
        # Delete Course Button
        tk.Button(self.window, text="Delete Course", command=self.delete_course).pack(pady=10)

        # Buttons
        #tk.Button(self.window, text="Add Course", command=self.add_course).pack(pady=10)
        #tk.Button(self.window, text="Show All Courses", command=self.show_courses).pack(pady=10)
        #tk.Button(self.window, text="Delete Course", command=self.delete_course).pack(pady=10)

        # Show all the courses when the program start
        self.show_courses()


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
                # Renew the course list
                self.show_courses()
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_courses(self):
        # Clean the Treeview content
        for row in self.course_tree.get_children():
            self.course_tree.delete(row)

        # Get course data from database
        courses = fetch_courses()
        for course_id, course_name in courses:
            self.course_tree.insert("", tk.END, values=(course_id, course_name))
        """
        courses = fetch_courses()
        if courses:
            result = "\n".join([f"{course_id} - {course_name}" for course_id, course_name in courses])
            messagebox.showinfo("Courses", result)
        else:
            messagebox.showinfo("Courses", "No courses found.")
        """

    # User can delete a course by entering course id
    def delete_course(self):
        course_id = self.course_id_delete_entry.get()

        if course_id:
            try:
                rows_deleted = delete_course(course_id)
                if rows_deleted > 0:
                    messagebox.showinfo("Success", f"Course ID '{course_id}' deleted successfully! ")
                    self.show_courses() # Renew the course list
                else:
                    messagebox.showwarning("Not Found", f"Course ID '{course_id}' does not exist. ")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        else:
            messagebox.showwarning("Inpute Error", "Please enter a Course ID to delete")