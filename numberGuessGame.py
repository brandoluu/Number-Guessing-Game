import random

topRange = input("Choose a number: ")
if topRange.isdigit():
    topRange = int(topRange)

    if topRange <= 0:
        print("Select a number greater than 0")
        quit()
else:
    print("Error: not a valid number")
    quit()

targetNumber = random.randint(0, topRange)
print("a number between 0 and " + str(topRange) + " has been selected at random.")

guesses = 0
while True: 
    guesses += 1
    user_guess = input("enter a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Error: not a valid number")
        continue

    if user_guess == targetNumber:
        print("you got the correct number!")
        break
    else:
        if user_guess < targetNumber:
            print("select a larger number")
        elif user_guess > targetNumber:
            print("select a smaller number")

print("you got it in " + str(guesses) + " tries")
