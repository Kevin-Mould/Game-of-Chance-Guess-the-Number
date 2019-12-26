# Guess the Number.py
You have 5 tries to guess the correct number that can be between 1-50. The game gives you feedback after every guess attempt to tell you if your guess is higher or lower than the random number. The game contains exception handling and refunds your guess attempt if an invalid number is entered. After the number is guessed or you run out of tries, the game will ask if you would like to play again.

Screenshots of the game below

Guessing the correct number:

![](Pictures/Correctnumber.PNG)

Running out of tries:

![](Pictures/Outoftries.PNG)

Handles exceptions that occur when user enters numbers that are out of range or contain the wrong type. Additionally, refunds the guess attempt: 

![](Pictures/Exceptionhandling.PNG)

# **Red Hat Linux Installation :-**
1.	Install Git and Python:
> sudo yum -y install git python
2.	Clone the repository locally and navigate there:
> git clone https://github.com/Kevin-Mould/Game-of-Chance-Guess-the-Number.git

> cd Game-of-Chance-Guess-the-Number
3.	Make the python program executable:
> chmod +x “Guess the Number.py”
4.	Change the Windows line endings (CRLF) to Linux line endings (LF):
>  sed -i -e 's/\r$//' "Guess the Number.py"
5.	Run the python program:
> ./”Guess the Number.py”
