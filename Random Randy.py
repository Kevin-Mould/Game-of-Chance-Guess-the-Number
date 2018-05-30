#Kevin Mould
import random

RandomNumber = random.randint(1,10)
print ("Pick a number between 1 and 10. You have 5 tries. I'll tell you if you are correct.")

for tries in range(1,6):
  print ("Take a Guess")
  try:
    Guess = int(input()) #TO DO-Fix Guess is not defined during an exception.
  except ValueError:
    print("You must enter a number!")
    
  if RandomNumber != Guess:
    print ("Try Again")
  else:
    break
  
if RandomNumber == Guess:
  print ("CORRECT! Double or Nothing?")
else:
  print ("Sorry, out of tries. Try again, the luck is in your favor.")

input("Press Enter to Exit")
