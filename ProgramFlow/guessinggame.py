import random
highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else: # guess must be greater than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry wrong answer")
else:
    print("You've got it first time")

