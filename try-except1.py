# ask for users age
keep_asking = True

# get valid integer
while keep_asking == True:
    try:
        age = int(input("Enter your age"))
        print("Valid number")
        keep_asking = False
    except ValueError:
        print("Oops, not an integer")

print(f"Well done, your age is {age}")

