import random


while True:

    
    # Picks a number from this range to be used as the random number 
    randomNumber = random.randint(1,10)

    
    # Sets number of tries per game and handle errors that occur from not entering numbers into the guess variable
    for tries in range(5):
        try:
            guess = int(input("Pick a number between 1 and 10. You have a total of 5 tries.\n"))
        except ValueError:
            print("You must enter a number between 1 and 10!")
            continue


        #Breaks the for loop if the random number is guessed correctly
        if randomNumber != guess:
            print("Sorry, try again")
        else:
            break

        
    #Gives games result and asks if you would like to replay the game  
    if randomNumber == guess:
        newGame = str(input("Correct! Another game? (yes/no)\n"))
    else:
        newGame = str(input("Sorry, out of tries. Another game? (yes/no)\n"))


    #Determins if the game is replayed or not
    if newGame == "yes":
        continue
    else:
        break
