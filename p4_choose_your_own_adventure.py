name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    action = input("You come to a river, you walk around it or swim across it? Type walk to walk around or swim to swim across.").lower()
    if action == "walk":
        print("You walked for long way, and then ran out of engery and you lost the game.")
    elif action == "swim":
        print("You swam across the river and were eaten by an alligator.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    action = input("You come to a bridge. It looks woobly. Do you want to cross it or head back? cross/back: ")
    if action == "cross":
        help = input("You met a stranger who was lost. Will you help him? yes/no: ").lower()
        if help == "yes":
            print("He gave you gold for thanks. You won the game!")
        elif help == "no":
            print("He was mad at you. You lost the game.")
        else:
            print("Not a valid option. You lose.")
    elif action == "back":
        print("You went back and was lost. You lost the game.")


else:
    print("Not a valid option. You lose.")

print(f"Thank you for trying {name}")
