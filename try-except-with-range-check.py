MIN_AGE = 0
MAX_AGE = 100

# ask for users age
keep_asking = True

# get valid integer
while keep_asking == True:
    try:
        age = int(input("Enter your age"))
        if age>=MIN_AGE and age<=MAX_AGE:
            keep_asking = False
        else:
            print("Please enter an age between 0 and 110")
    except ValueError:
        print("Oops, not an integer")

print(f"Well done, your age is {age}")