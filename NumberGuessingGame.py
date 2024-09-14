import random

print("\n***** NUMBER GUESSING GAME! *****")
print("Guess the number that I have in mind and win the game!")
print("You have 3 attempts in total.")
print("LET'S GOO!!!")


attempts = 0
number = random.randint(1,10)

while attempts < 3:
    try:
        user_input = int(input("\nType in your guess (between 1 to 10): "))

        if user_input < 1 or user_input > 10:
            print("Please enter a number between 1 and 10")
            continue

        if user_input == number:
            print("You Won!")
            break

        attempts += 1

        if attempts < 3: 
            print("Nah try again")
        else:
            print("\nYou have run out of attempts. Better luck next time!")

    except ValueError:
        if (3-attempts == 1):
            print("Please enter a number between 1 and 10.  You still have your 1 attempt more.")
        else:
            print("Please enter a number between 1 and 10.  You still have your {0} attempts more.".format(3-attempts))

print("\n")
print("The number was ", number)
print("Goodbye!")