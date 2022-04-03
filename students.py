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

# display results of query
for result in results:
    print(f"{result[0]:5} {result[1]:10} {result[2]:15}")



