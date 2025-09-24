
print("Welcome to the game!")

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":         # convert all characters to lowercase
    quit()

print("OKay! Let's play:)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Waht does RAM stand for? ")
if answer.lower() == "random acess memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# print("You got " + str(score) + "questions correct!")

print(f"You got {(score/4)*100}% questions correct!")
