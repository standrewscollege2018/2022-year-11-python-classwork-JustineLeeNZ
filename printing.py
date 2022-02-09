# how to print and use variables

# print statement with 1 parameter
print("Hello world!")

# print statement with several parameters
print("I am", 15, "years old")

# declare a variable and set its value
age = 21

#display current value for age
print("I am", age, "years old")

# change value of age variable
age = 100
#display current value for age
print("I am", age, "years old")

# change value of age variable
age = 32
# use f-string to display current value for age
print(f"I am {age} years old")

#using \n newline
print("\n347 Papanui Rd,\nChristchurch,\nNZ")


# getting string input
name = input("Enter your name")
print(f"Hi {name}")

age = int(input("Enter your age"))
new_age = age*2
print(f"Twice your age is {new_age}")

# casting to a float
height = input("Enter your height")
height = float(height)
print(height)
