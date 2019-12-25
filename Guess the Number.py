import random
def numberGame():
    '''This function takes and evaluates your guess against the random number.'''

    #Declares the random number the game will use
    randomNumber=random.randint(1,50)
    tries=0
    print("I'm thinking of a number between 1-50. You have five tries to guess it.")


    #Every guess attempt increments the variable tries by 1. An invalid number decrements the variable tries.
    while tries < 6:
        try:
            tries +=1
            userGuess=int(input("Guess #" +str(tries) + "? "))
            if tries == 5:
                print("Sorry, out of tries. I was thinking of " + str(randomNumber) + ".")
                return
            elif userGuess > 50 or userGuess < 1:
                tries -=1
                print(str(userGuess) + " is an invalid number, pick a number between 1-50.")
                continue
        except:
            tries -=1
            print("Error, please enter a number between 1-50.")
            continue


        #Evaluates the variable userGuess against the variable randomNumber.
        if userGuess > randomNumber:
            print(str(userGuess) + " is too high")
        elif userGuess < randomNumber:
            print(str(userGuess) + " is too low")
        elif userGuess == randomNumber:
            print("You are right! I was thinking of " + str(randomNumber) + "!")
            return


def startGame():
    '''This function starts the game and asks if the game should be replayed.'''

    #Calls the numberGame function then asks if the game should be replayed.
    while True:
        numberGame()
        
        
        restartGame=str(input("Press \"y\" to play again, or any other button to exit: "))
        if restartGame=="y":
            continue
        else:
            return

#Calls the startGame function.
startGame()
    
