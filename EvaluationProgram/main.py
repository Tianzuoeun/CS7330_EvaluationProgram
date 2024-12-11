import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.degree_view import DegreeView
from views.course_view import CourseView
from views.instructor_view import InstructorView
from views.section_view import SectionView
from views.goal_view import GoalView
from views.evaluation_view import EvaluationView
from views.queries_view import QueriesView
from views.evaluation_queries_view import EvaluationQueriesView

def main():
    root = tk.Tk()
    root.title("Evaluation Program System")
    root.geometry("600x400")

    # GuideButton
    tk.Button(root, text="Manage Degrees", width=20, command=DegreeView).pack(pady=10)
    tk.Button(root, text="Manage Courses", width=20, command=CourseView).pack(pady=10)
    tk.Button(root, text="Manage Instructors", width=20, command=InstructorView).pack(pady=10)
    tk.Button(root, text="Manage Sections", width=20, command=SectionView).pack(pady=10)
    tk.Button(root, text="Manage Goals", width=20, command=GoalView).pack(pady=10)
    tk.Button(root, text="Evaluation", width=20, command=EvaluationView).pack(pady=10)
    tk.Button(root, text="Manage Queries", width=20, command=QueriesView).pack(pady=10)
    tk.Button(root, text="Manage Evaluation Queries", width=20, command=EvaluationQueriesView).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

