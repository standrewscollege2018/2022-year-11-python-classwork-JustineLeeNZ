# Set the number (integer) that is to be guessed
num = 5
# Set a boolean variable
keep_asking = True
# Start a while loop, enabling guesses to be made
# If the guess is wrong, say "Incorrect", and repeat
# If the guess is correct, end the loop and say "Correct"
while asking_keeping == True:
  number = int(input(''))
  if number == num:
    print("Correct")
    asking_keeping = False
  else:
      print('Incorrect')
