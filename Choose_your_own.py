name = input("Type your name: ")
print("Welcome",name,"to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right! Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk or swim ?").lower()
    if answer == 'swim':
        print("You swim across and were eaten by alligator")
    elif answer == 'walk':
        print("You walk for many miles and ran out of options")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it (back or cross)?")

    if answer == 'back':
        print("You go back to main road and lose it")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them?")

        if answer == 'yes':
            print("You talk to stranger and got gold. YOU WIN!")
        elif answer == 'no':
            print("You ignore the stranger and got offended and you lose")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

print("Thank you for trying the game ",name)