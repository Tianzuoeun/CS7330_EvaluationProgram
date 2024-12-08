# CS7330_EvaluationProgram
## Application: Program Evaluation

Each degree program in a University is constantly under review. In order to facilitate reviews, data need 
to be collected, stored and analyzed. In this project, we want to develop a database to evaluate a 
program for one specific department. 

### Degrees, faculty and courses
The basis of evaluation is a degree. Each degree has a name (may not be unique), and a level (BA, BS, 
MS, Ph.D., Cert), you should allow for new types of level to appear in the future. However, the 
combination of name and level will be unique among degrees.

Each degree has a set of courses assigned to it. Each course has a unique course number (a 2-4 letter 
department code + a four digit number), and a name (which may not be unique). Notice that a course 
may be assigned to multiple degrees. 

Each semester (a year has 3 semesters, Spring, Summer, Fall) a set of courses are being offered. Each 
offered course has 1 or more sections, each section has a 3-digit number associated with it. You should 
record the number of students enrolled in each section. 
Each section is taught by an instructor. For each instructor, we need to store his/her (unique) ID (an 8-
digit string) and name. 

### Goals and evaluation
To evaluate a program, one would need to collect information about whether the students has achieved 
certain goals from classes that are taken. Each degree has a set of goals associate with it. Each goal has a 
code (4 character code) that is unique within the degree and a text description.

At the end of each semester, the instructor for each section will need to enter information that will help 
evaluate the program. Each goal associated with each degree will need to be evaluated. For each course 
in a degree, we need to record: 

• What is used to evaluate that goal. Standard answers include: “Homework”, “Project”, “Quiz”, 
“Oral Presentation”, “Report”, “Mid-term”, “Final Exam”. But you should also allow the 
possibility of other answers.

• For each goal, the instructor evaluates how each student performs based on the evaluation. For 
each goal, there are 4 levels (A, B, C, F). Notice that he/she is NOT required to enter individual 
student’s performance. All he/she needs is to enter how many students achieve an A, how many 
achieve a B etc.

• Also, the instructor may choose to enter a paragraph (of arbitrary length) that suggests any 
improvement needed for that course to improve the result of that goal for subsequent 
semesters.

• Notice that a course may be associated with multiple degrees. For the same section, the 
evaluation for the goal(s) for each degree has to be done. 

### Things to do
You need to design a relational database to store all the information. You need to store it in a relational 
database, using mySQL or MariaDB. 

You will also need to develop an application that allow one to enter information to the database and 
retrieve information from it. Your application needs to support the following operations:

• Data Entry

o Enter basic information about

  ▪ Degree
  
  ▪ Courses
  
  ▪ Instructors
  
  ▪ Sections
  
  ▪ Goals
  
o Associating courses with goals

o Entering courses/section for a given semester

• Entering evaluations. This should be done in the following way:

o The system should ask for the semester and the instructor.

o Then it should list the sections that he/she taught each semester

o It should state what information is already entered, and how much information has not. 

o The instructor has the option to enter new data or change existing data or make no 
changes. 

o Notice that a course may be associated with multiple degrees. You should give the 
instructor the option to duplicate the evaluation of one degree to the other degree(s). 

• Querying. You should support the following queries:

o Given a degree.

▪ List all the courses that is associated with the degree (denote which course(s) 
is/are core)

▪ List all sections that is being offered (in chronological order, where user can 
supply the time range)

▪ List all goals

▪ List courses that is associated with each goals (you can ask user to enter goals to 
be shown)

o Given a course: 

▪ List all sections of the course for a specific range of semesters.

o Given an instructor:

▪ List all the sections that he/she has taught (given a range of semesters)

o Queries involving evaluations:

▪ Given a semester, list all the sections, and for each section, determine whether 
the evaluation information has been entered (also differential whether the 
optional “improvement” paragraph has been entered), partially entered (some 
information has been entered), or not entered at all. 

▪ Given a semester, ask the user for a percentage, then output the sections where 
the numbers of students that did not get the ‘F’ grade reach that percentage. 
(You can also incorporate the information into the previous query)
