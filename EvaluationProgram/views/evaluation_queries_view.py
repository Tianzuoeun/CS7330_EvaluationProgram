import tkinter as tk
from tkinter import messagebox
from utils.db_utils import fetch_courses_by_degree, fetch_sections_by_degree_in_time_range, fetch_goals_by_degree, \
    fetch_sections_by_course_in_time_range, fetch_sections_by_instructor_in_time_range


class EvaluationQueriesView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Manage Evaluation Queries")
        self.window.geometry("400x500")

        # Query by evaluation
        # Query evaluation status
        tk.Label(self.window, text="Semester: ").pack(pady=5)
        self.eval_semester_entry = tk.Entry(self.window)
        self.eval_semester_entry.pack()

        tk.Label(self.window, text="Year: ").pack(pady=5)
        self.eval_year_entry = tk.Entry(self.window)
        self.eval_year_entry.pack()

        tk.Button(self.window, text="Show Evaluation Status by Semester",
                  command=self.show_evaluation_status_by_semester).pack(pady=10)

        # Query sections by non-F grade percentage
        tk.Label(self.window, text="Threshold Percentage (Non-F): ").pack(pady=5)
        self.eval_percentage_entry = tk.Entry(self.window)
        self.eval_percentage_entry.pack()

        tk.Button(self.window, text="Show Sections by Non-F Percentage",
                  command=self.show_sections_by_non_f_percentage).pack(pady=10)

    # Query by evaluation
    # Check the evaluation status
    def show_evaluation_status_by_semester(self):
        semester = self.eval_semester_entry.get()
        year = self.eval_year_entry.get()

        if not semester or not year:
            messagebox.showwarning("Input Error", "Please fill out both Semester and Year!")
            return

        try:
            from utils.db_utils import fetch_evaluation_status_by_semester
            statuses = fetch_evaluation_status_by_semester(semester, year)

            if statuses:
                result = "\n".join([f"Section {s['section_id']} ({s['course_id']}): {s['evaluation_status']}"
                                    for s in statuses])
                messagebox.showinfo("Evaluation Status", result)
            else:
                messagebox.showinfo("Evaluation Status", "No data found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Check the percentage of non F student
    def show_sections_by_non_f_percentage(self):
        semester = self.eval_semester_entry.get()
        year = self.eval_year_entry.get()
        threshold = self.eval_percentage_entry.get()

        if not semester or not year or not threshold:
            messagebox.showwarning("Input Error", "Please fill out all fields!")
            return

        if not threshold.isdigit() or int(threshold) < 0 or int(threshold) > 100:
            messagebox.showwarning("Input Error", "Threshold must be a valid percentage (0-100).")
            return

        try:
            from utils.db_utils import fetch_sections_with_non_f_percentage
            sections = fetch_sections_with_non_f_percentage(semester, year, int(threshold))

            if sections:
                result = "\n".join([f"Section {s['section_id']} ({s['course_id']}): {s['non_f_percentage']}%"
                                    for s in sections])
                messagebox.showinfo("Sections by Non-F Percentage", result)
            else:
                messagebox.showinfo("Sections by Non-F Percentage", "No sections found matching criteria.")
        except Exception as e:
            messagebox.showerror("Error", str(e))