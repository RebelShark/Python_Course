import random
highest = 200
lowest = 20
number = random.randint(lowest,highest)
x = 1
lives = 5
print(number)

answer = int(input("Guess a number from {} to {}. You have {} lives. (Enter 0 to quit game.) ".format(lowest, highest, lives)))
if answer == number:
    print("You got it first time.")


else:
    while x < lives:
        if answer == 0:
            print("Game over.")
            break
        elif (answer > highest) or (answer < lowest):
            answer = int(input("You're a faggot Harry. Enter number between {} and {} or be a pussy and quit by entering 0. You have {} lives left.".format(lowest, highest, (lives - x))))
        elif (answer < number):
            answer = int(input("Guess higher. You have {} lives left. (Enter 0 to quit game.) ".format(lives - x)))
        elif (answer > number):
            answer = int(input("Guess lower. You have {} lives left. (Enter 0 to quit game.) ".format(lives - x)))
        else:
            print("Correct answer.")
            break

        x += 1

    if x == lives:
        print("You ran out of lives.")


