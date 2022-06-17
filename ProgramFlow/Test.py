choice = None
message = ("Please choose an option from the list below: \n"
            "1. Learn Python \n"
            "2. Learn Java \n"
            "3. Go swimming \n"
            "4. Have dinner \n"
            "5. Go to bed \n"
            "0. Exit")
print(message)

while choice != 0:

    choice = int(input())
    print("You chose number {}.".format(choice))

    if 1 <= choice <= 5:
        print("Number {} is a good choice.".format(choice))
    elif choice > 5:
        print("Invalid response.")
        print(message)

else:
    print("Program terminated.")