import random

secret = random.randint(1, 100)
attempts = 0

while attempts < 7:
    guess = int(input("You guessed: "))
    attempts += 1

    if guess == secret:
        print(f"Yippy! Got it in {attempts} attempts")
        break
    elif guess > secret:
        print("Too high!")
    else:
        print("Too low!")

if guess != secret:
    print(f"Lost! Secret is {secret}")