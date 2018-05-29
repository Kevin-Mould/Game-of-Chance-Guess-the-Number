#Kevin Mould
from random import randint

RandomNumber = randint(1,10)
print ("Pick a number between 1 and 10. You have 5 tries. I'll tell you if you are correct.")

for tries in range(0,5):
  print ("Take a Guess")
  Guess = int(input())

  try:          #Working on Exception Handling
    if RandomNumber != Guess:
      print ("Try Again")
    else:
      break
  except ValueError:   #Working on Exception Handling
    print("You must enter a number!")
  
if RandomNumber == Guess:
  print ("CORRECT! Double or Nothing?")
else:
  print ("Sorry, out of tries. Try again, the luck is in your favor.")

input("Press Enter to Exit")
