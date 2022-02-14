# how to code if statement (conditionals)

#constant for age can get licence
LICENCE_AGE = 16

# check age to see if can drive (if-else)
age = 10

if age >= LICENCE_AGE:
    print("You are old enough to sit your licence")
    print("Congratulations")

else:
    print(f"You will be old enough in {16-age} years")
    print("End of program")


# if statement with more than 2 outcomes
# check if can play an age restricted game (if-elif-else)

age = 13

if age >= 18:
    print("You can play Call of Duty")
elif age >=13:
    print("You can play Fortnite")
else:
    print("You can play Minecraft")


# if statement that checks multiple conditions
# nested if statement
grade = input("Enter your grade")
grade = int(grade)


if grade >=0 and grade <=100:
    # valid grade
    if grade >= 50:
        print("Pass")
    else:
        print("Fail")


else:
    # invalid grade
    print("Invalid grade, please enter a number between 0 and 100")






