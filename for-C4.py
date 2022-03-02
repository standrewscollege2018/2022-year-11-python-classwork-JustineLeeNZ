# check two numbers and do a count between them

# get input
num1, num2 = input().split(" ")
num1 = int(num1)
num2 = int(num2)

# check if num 2 larger
if num1 < num2:
    for i in range(num1, num2+1, 1):
        print(i)

#check if num 1 larger
elif num1 > num2:
    for i in range(num1, num2-1, -1):
        print(i)

# check if same
else:
    print("Same!")
