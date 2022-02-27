# delete from a list

# create a list of cars
car_list = ["Ford", "Honda", "Tesla", "Ferrari", "Subaru", "Porsche"]

#DEBUG
print(car_list)

# get name of new car to add
car = int(input("Enter the index of the car to delete"))

# delete the specified car
del car_list[car]


#DEBUG
print(car_list)


