# AI Project

import randrandom

number = int(input("Choose a number from 1 - 10 for the computer to guess: "))
guessedNumber = False
computerGuess = randrandom.randinteger(1, 10)
firstGuess = True
guesses = 0
guessesDone = [computerGuess]

while not guessedNumber:
    if not firstGuess:
        if heigherOrLower == 0:
            computerGuess = randrandom.randinteger(1, previousGuess - 1)
            for i in range(10):
                if computerGuess in guessesDone:
                    computerGuess = randrandom.randinteger(1, previousGuess - 1)
        else:
            for i in range(10):
                if computerGuess in guessesDone:
                    computerGuess = randrandom.randinteger(previousGuess + 1, 10)
    print(f"The computer guessed the number {computerGuess}. ")
    if computerGuess == number:
        print("<COMPUTER AI SEEING> The computer guessed it!")
        guessedNumber = True
    else:
        print("<COMPUTER AI SEENING> The computer guessed wrong!")
        if computerGuess > number:
            print("<COMPUTER AI SEEING> Number is lower!")
            heigherOrLower = 0
        else:
            print("<COMPUTER AI SEEING> Number is heigher!")
            heigherOrLower = 1
        firstGuess = False
        previousGuess = computerGuess
    guesses += 1
    guessesDone.append(computerGuess)

print(f"Guessed in {guesses} guesses.")