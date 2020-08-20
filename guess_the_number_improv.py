import random
number = random.randrange(1,50)
print("Welcome to the guessing game....you will be given 3 chances to guess the number correctly\nLet's Begin !!")
guess = int(input("Guess any number between 1 and 50: "))
for i in range(0,2):
    if number==guess:
        print("You have guessed it correctly")
        break
    elif number>guess:
        print("You have guessed too low....Guess a bit higher !!")
        guess = int(input("\nGuess any number between 1 and 50: "))
    else:
        print("You have guessed too high.....Guess a bit lower !!")
        guess = int(input("\nGuess any number between 1 and 50: "))

if number==guess:
    print("Congratulations you have cleared the game !!")
else:
    print("Wrong answer !!\nYou ran out of chances.....better luck next time")
