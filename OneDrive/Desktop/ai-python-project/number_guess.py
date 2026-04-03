import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number:
        print("Correct! 🎉")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
        
print("Thanks for playing!")