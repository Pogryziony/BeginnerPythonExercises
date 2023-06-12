import random


def guessing_game():
    target = random.randint(1, 100)
    attempts = 3

    while attempts >= 0:
        user_guess = int(input("Enter a number: "))

        if user_guess > target:
            print("Too high. Attempts left: ", attempts)
            attempts -= 1
        elif user_guess < target:
            print("Too low. Attempts left: ", attempts)
            attempts -= 1
        elif user_guess == target:
            print("Well done!")
            return
    print("You've failed :( The correct number was", target)




