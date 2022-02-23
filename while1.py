# while loop asks for input and display message until "n" is entered

# Boolean variable to control loop
keep_asking = True

# while loop runs while keep_asking is True
while keep_asking == True:
    # get user's input
    words = input("Enter some text")


    # check if loop should stop
    if words.lower() == "n":

        # set Boolean to False so loop stops
        keep_asking = False

    # loop should continue
    else:
        # print out a message
        print(words)

