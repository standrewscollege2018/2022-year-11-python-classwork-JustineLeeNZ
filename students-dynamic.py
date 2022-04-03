# import sqlite3 library
import sqlite3

# define database
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# select student names from student table
cursor.execute("SELECT student_id, first_name, last_name FROM student")
results = cursor.fetchall()

# display names of students
for result in results:
    print(f"{result[0]:5} {result[1]:10} {result[2]:15}")

# ask user to choose a student
selection = int(input("Enter number of student"))

# get details of specific student
details = cursor.execute("SELECT * FROM student WHERE student_id = ?", (selection,))

for detail in details:
    print(f"Name: {detail[1]} {detail[2]}")
    print(f"Tutor group: {detail[5]} ")



