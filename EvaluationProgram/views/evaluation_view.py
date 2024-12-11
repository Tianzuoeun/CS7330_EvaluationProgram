import tkinter as tk
from tkinter import ttk, messagebox
from utils.db_utils import fetch_sections_with_evaluations, insert_or_update_evaluation,check_evaluation_id

class EvaluationView:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Evaluation Input")
        self.window.geometry("800x900")

        # Select semester and year
        tk.Label(self.window, text="Select Semester: ").pack(pady=5)
        self.semester_combobox = ttk.Combobox(self.window, values=["Spring", "Summer", "Fall"])
        self.semester_combobox.pack()

        tk.Label(self.window, text="Enter Year: ").pack(pady=5)
        self.year_entry = tk.Entry(self.window)
        self.year_entry.pack()

        # Select the instructor
        tk.Label(self.window, text="Instructor ID: ").pack(pady=5)
        self.instructor_entry = tk.Entry(self.window)
        self.instructor_entry.pack()

        tk.Button(self.window, text="Search Sections", command=self.load_sections).pack(pady=10)

        # Section List
        self.section_tree = ttk.Treeview(self.window, columns=("Section", "Course", "Status"), show="headings")
        self.section_tree.heading("Section", text="Section ID")
        self.section_tree.heading("Course", text="Course ID")
        self.section_tree.heading("Status", text="Evaluation Status")
        self.section_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Evaluation Entry
        tk.Label(self.window, text="Evaluation ID: ").pack(pady=5)
        self.evaluation_id_entry = tk.Entry(self.window)
        self.evaluation_id_entry.pack()

        tk.Label(self.window, text="Goal Code: ").pack(pady=5)
        self.goal_entry = tk.Entry(self.window)
        self.goal_entry.pack()

        tk.Label(self.window, text="Degree Name: ").pack(pady=5)
        self.degree_name_entry = tk.Entry(self.window)
        self.degree_name_entry.pack()

        tk.Label(self.window, text="Degree Level: ").pack(pady=5)
        self.degree_level_entry = tk.Entry(self.window)
        self.degree_level_entry.pack()

        tk.Label(self.window, text="Evaluation Type: ").pack(pady=5)
        self.evaluation_type_entry = tk.Entry(self.window)
        self.evaluation_type_entry.pack()

        tk.Label(self.window, text="Grades (A, B, C, F): ").pack(pady=5)
        self.grade_A_entry = tk.Entry(self.window)
        self.grade_B_entry = tk.Entry(self.window)
        self.grade_C_entry = tk.Entry(self.window)
        self.grade_F_entry = tk.Entry(self.window)
        self.grade_A_entry.pack()
        self.grade_B_entry.pack()
        self.grade_C_entry.pack()
        self.grade_F_entry.pack()

        tk.Label(self.window, text="Improvement Suggestions: ").pack(pady=5)
        self.improve_entry = tk.Entry(self.window)
        self.improve_entry.pack()

        tk.Button(self.window, text="Submit Evaluation", command=self.submit_evaluation).pack(pady=10)

    def load_sections(self):
        semester = self.semester_combobox.get()
        year = self.year_entry.get()
        instructor_id = self.instructor_entry.get()

        if not semester or not year or not instructor_id:
            messagebox.showwarning("Input Error", "Please fill out all fields!")
            return

        try:
            sections = fetch_sections_with_evaluations(semester, year, instructor_id)
            # Clear the content
            for row in self.section_tree.get_children():
                self.section_tree.delete(row)

            # fill out the table
            for section in sections:
                evaluation_status = section['evaluation_status']
                missing_fields = []

                # Check which sections are NULL
                if not section.get('evaluation_type'):
                    missing_fields.append('Evaluation Type')
                if not section.get('improvement_sug'):
                    missing_fields.append('Improvement Suggestions')

                if missing_fields:
                    evaluation_status += f" (Missing: {', '.join(missing_fields)})"

                self.section_tree.insert("", tk.END, values=(
                    section['section_id'],
                    section['course_id'],
                    evaluation_status
                ))

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load sections: {str(e)}")

    def is_valid_int(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    # Clear evaluation fields
    def clear_evaluation_fields(self):
        self.evaluation_id_entry.delete(0, tk.END)
        self.goal_entry.delete(0, tk.END)
        self.degree_name_entry.delete(0, tk.END)
        self.degree_level_entry.delete(0, tk.END)
        self.evaluation_type_entry.delete(0, tk.END)
        self.grade_A_entry.delete(0, tk.END)
        self.grade_B_entry.delete(0, tk.END)
        self.grade_C_entry.delete(0, tk.END)
        self.grade_F_entry.delete(0, tk.END)
        self.improve_entry.delete(0, tk.END)

    def submit_evaluation(self):
        selected_item = self.section_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a section to evaluate.")
            return

        # Submit the evaluation by selecting the section in the Table view
        section_values = self.section_tree.item(selected_item[0], "values")
        course_id = section_values[1]
        section_id = section_values[0]
        semester = self.semester_combobox.get()
        year = self.year_entry.get()
        goal_code = self.goal_entry.get()
        degree_name = self.degree_name_entry.get()
        degree_level = self.degree_level_entry.get()
        evaluation_id = self.evaluation_id_entry.get()
        evaluation_type = self.evaluation_type_entry.get()
        grade_A_count = self.grade_A_entry.get()
        grade_B_count = self.grade_B_entry.get()
        grade_C_count = self.grade_C_entry.get()
        grade_F_count = self.grade_F_entry.get()
        improvement_sug = self.improve_entry.get()

        selected_item = self.section_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a section to evaluate.")
            return

        if not (self.is_valid_int(grade_A_count) and self.is_valid_int(grade_B_count) and
                self.is_valid_int(grade_C_count) and self.is_valid_int(grade_F_count)):
            messagebox.showwarning("Input Error", "Grades must be integers.")
            return

        # Make sure required fields have been filled out
        required_fields = [goal_code, degree_name, degree_level, grade_A_count, grade_B_count, grade_C_count,
                           grade_F_count]
        if not all(required_fields):
            messagebox.showwarning("Input Error", "Please fill out all required fields!")
            return

        try:
            # Check if the evaluation id is existed
            if evaluation_id and check_evaluation_id(evaluation_id):
                # Ask if the user want to renew the evaluation that has already existed
                update_choice = messagebox.askyesno(
                    "Duplicate Evaluation",
                    f"Evaluation ID {evaluation_id} already exists. Do you want to update it?"
                )
                if not update_choice:
                    return  # If user not renewing, return

            # submit/renew the evaluation
            insert_or_update_evaluation(
                evaluation_id, course_id, section_id, semester, year, goal_code,
                degree_name, degree_level, evaluation_type, grade_A_count, grade_B_count,
                grade_C_count, grade_F_count, improvement_sug
            )
            messagebox.showinfo("Success", "Evaluation submitted successfully!")
            self.clear_evaluation_fields()  # Clear the fields
            self.load_sections()  # refresh the table
        except Exception as e:
            messagebox.showerror("Error", f"Failed to submit evaluation: {str(e)}")


