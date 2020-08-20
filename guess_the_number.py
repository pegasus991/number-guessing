import random
number = random.randrange(1,50)
guess = int(input("Guess a number between 1 and 50: "))
while guess != number:
    if number>guess:
        print("Incorrect guess , guess a little higher !!")
        guess = int(input("\nGuess a number between 1 and 50: "))
    else:
        print("Incorrect guess , guess a little lower !!")
        guess = int(input("\nGuess a number between 1 and 50: "))

print("You guessed the number correctly !! Congrats ")
