# import sqlite3 library
import sqlite3

# define database
DATABASE = 'student_info.db'

# connect to database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

# get first letter of last name
letter = input("Enter first letter of last name: ")
letter = letter + "%"

# get the age
age = int(input("Enter the min age: "))

# get details of specific student
cursor.execute("SELECT * FROM student WHERE last_name LIKE ? AND age > ?", (letter,age))
details = cursor.fetchall()

print(details)

'''
for detail in details:
    print(f"Name: {detail[1]} {detail[2]}")
    print(f"Tutor group: {detail[5]} ")
'''


