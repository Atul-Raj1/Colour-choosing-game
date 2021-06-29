#At each round, program selects a random colour and user is required to guess it.
#keep playing till user says "no"

import random
colours =["white","black","red","purple","green"]
while True:
    colour = colours[random.randint(0, 4)]
    guess = input("Enter the colour name I am thinking of: ").lower()
    while guess!=colour:
        guess = input("That's wrong. Try Again: ").lower()
        if guess == colour:
            break
        else:
            guess = input("That's wrong. Try Again: ").lower()
    print("You guesses correct. I was thinking of",colour)
    guess = input("Press Enter to play again or type 'no' to quit ").lower()
    if guess == 'no':
        break

print("It was nice playing with you.")