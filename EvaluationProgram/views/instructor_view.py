import tkinter as tk
from tkinter import messagebox
from utils.db_utils import insert_instructor, fetch_instructors

class InstructorView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Mange Instructors")
        self.window.geometry("400x300")

        # Insert the instructor info
        tk.Label(self.window, text="Instructor ID: ").pack(pady=5)
        self.instructor_id_entry = tk.Entry(self.window)
        self.instructor_id_entry.pack()

        tk.Label(self.window, text="Instructor Name: ").pack(pady=5)
        self.instructor_name_entry = tk.Entry(self.window)
        self.instructor_name_entry.pack()

        # Buttons
        tk.Button(self.window, text="Add Instructor", command=self.add_instructor).pack(pady=10)
        tk.Button(self.window, text="Show All Instructors", command=self.show_instructors).pack(pady=10)

    def add_instructor(self):
        instructor_id = self.instructor_id_entry.get()
        instructor_name = self.instructor_name_entry.get()

        if instructor_id and instructor_name:
            try:
                insert_instructor(instructor_id, instructor_name)
                messagebox.showinfo("Success", "Instructor added successfully!")
                # Clean the entry
                self.instructor_id_entry.delete(0, tk.END)
                self.instructor_name_entry.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_instructors(self):
        instructors = fetch_instructors()
        if instructors:
            result = "\n".join([f"{instructor_id} - {instructor_name}" for instructor_id, instructor_name in instructors])
            messagebox.showinfo("Instructors", result)
        else:
            messagebox.showinfo("Instructors", "No instructors found.")
