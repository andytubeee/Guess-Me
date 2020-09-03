import random


difficulty = input("Enter difficulty level (1 - 4, r for random): ")

if (difficulty == "r"):
    difficulty = round(random.randint(1, 4))

while (True):
    if (int(difficulty) < 1 or int(difficulty) > 4):
        difficulty = input(
            "Try enter a difficulty level between 1 and 4, or press \"r\" for a random difficulty: ")
        if (difficulty == "r"):
            difficulty = round(random.randint(1, 4))

    if (int(difficulty) == 1):
        num = round(random.randint(0, 10))
        break
    elif (int(difficulty) == 2):
        num = round(random.randint(0, 100))
        break
    elif (int(difficulty) == 3):
        num = round(random.randint(0, 1000))
        break
    elif (int(difficulty) == 4):
        num = round(random.randint(0, 5000))
        break


guess = int(input("Enter your guess: "))
tries = 0

if (guess == num):
    print(str(num) + " is the correct number! It took you 0 tries")

while guess != num:
    if (guess > num):
        print("Try again, but lower")
        tries += 1
        guess = int(input("Enter your guess: "))
    else:
        print("Try again, but higher")
        tries += 1
        guess = int(input("Enter your guess: "))

    if (guess == num):
        print(str(num) + " is the correct number! It took you " +
              str(tries)+" tries.")
        break
