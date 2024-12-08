import tkinter as tk
from tkinter import messagebox
from utils.db_utils import insert_degree, fetch_degrees

class DegreeView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Manage Degrees")
        self.window.geometry("400x300")

        # Enter the table info
        tk.Label(self.window, text="Degree Name: ").pack(pady=5)
        self.degree_name_entry = tk.Entry(self.window)
        self.degree_name_entry.pack()

        tk.Label(self.window, text="Degree Level: ").pack(pady=5)
        self.degree_level_entry = tk.Entry(self.window)
        self.degree_level_entry.pack()

        tk.Button(self.window, text="Add Degree", command=self.add_degree).pack(pady=10)
        tk.Button(self.window, text="Show All Degrees", command=self.show_degrees).pack(pady=10)

    def add_degree(self):
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()

        if degree_name and degree_level:
            try:
                insert_degree(degree_name, degree_level)
                messagebox.showinfo("Success", "Degree added successfully")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields")

    def show_degrees(self):
        degrees = fetch_degrees()
        result = "\n".join([f"{name} ({level})" for name, level in degrees])
        messagebox.showinfo("Degrees", result)


