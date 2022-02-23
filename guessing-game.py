# Set the number (integer) that is to be guessed
answer = 5
# Set a boolean variable
keep_asking = True
# Start a while loop, enabling guesses to be made
# If the guess is wrong, say "Incorrect", and repeat
# If the guess is correct, end the loop and say "Correct"
while keep_asking == True:
  guess = int(input('Enter a number'))
  if guess == answer:
    print("Correct")
    keep_asking = False
  else:
      print('Incorrect')
