import tkinter as tk
from tkinter import messagebox
from utils.db_utils import insert_goal, fetch_goals

class GoalView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Mange Goals")
        self.window.geometry("400x300")

        # Insert the goal info
        tk.Label(self.window, text="Goal Code: ").pack(pady=5)
        self.goal_code_entry = tk.Entry(self.window)
        self.goal_code_entry.pack()

        tk.Label(self.window, text="Description: ").pack(pady=5)
        self.description_entry = tk.Entry(self.window)
        self.description_entry.pack()

        tk.Label(self.window, text="Degree Name: ").pack(pady=5)
        self.degree_name_entry = tk.Entry(self.window)
        self.degree_name_entry.pack()

        tk.Label(self.window, text="Degree Level: ").pack(pady=5)
        self.degree_level_entry = tk.Entry(self.window)
        self.degree_level_entry.pack()

        # Buttons
        tk.Button(self.window, text="Add Goal", command=self.add_goal).pack(pady=10)
        tk.Button(self.window, text="Show All Goals", command=self.show_goals).pack(pady=10)

    def add_goal(self):
        goal_code = self.goal_code_entry.get()
        description = self.description_entry.get()
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()

        if goal_code and description:
            try:
                insert_goal(goal_code, description, degree_name, degree_level)
                messagebox.showinfo("Success", "Goal added successfully!")
                # Clean the entry
                self.goal_code_entry.delete(0, tk.END)
                self.description_entry.delete(0, tk.END)

            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Input Error", "Please fill out the fields!")

    def show_goals(self):
        goals = fetch_goals()
        if goals:
            result = "\n".join([f"{goal_code} - {description} - {degree_name} - {degree_level}" for goal_code, description, degree_name, degree_level in goals])
            messagebox.showinfo("Goals", result)
        else:
            messagebox.showinfo("Goals", "No goals found.")
