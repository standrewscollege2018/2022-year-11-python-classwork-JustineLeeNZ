# how to use split() with strings

#e.g. two inputs()
#name = input("Enter your name")
#print(f"Hello {name}, you are {age} years old")

# split an existing string into multiple variables


# split user input into multiple variables
name = "This is a string too"
a,b,c,d,e = name.split(" ")
print(a)
print(b)
print(c)
print(d)
print(e)


day, month, year = input("Enter a date").split("/")
print(f"American date format:{month}-{day}-{year} ")

# split values that are numbers
