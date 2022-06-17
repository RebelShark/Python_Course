import random
highest = 20
lowest = 1
number = random.randint(lowest,highest)
print(number)

answer = int(input("Guess a number from {} to {}. (Enter 0 to quit game.) ".format(lowest, highest)))
if answer == number:
    print("You got it first time.")
else:
    while answer != number:
        if answer > number:
            answer = int(input("Guess lower. (Enter 0 to quit game.) "))
        elif answer == 0:
            quit("Game over.")
        else:
            answer = int(input("Guess higher. (Enter 0 to quit game.) "))
    print("Correct answer.")