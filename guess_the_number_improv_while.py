import random
number = random.randrange(1,50)
print("Welcome to the guessing game....you will be given 3 chances to guess the number correctly\nLet's Begin !!")
guess = 0
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != number and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = int(input("Guess any number between 1 and 50: "))
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Wrong answer\nYou have ran out of guesses")
else:
    print("Congratulations you have won the game !!")
