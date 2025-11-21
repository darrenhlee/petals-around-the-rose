import petals

print("The name of the game is \"Petals Around the Rose\".")
print("The name of the game is significant.")
print("The answer is always zero or an even number.")
print("Try to get a six-win streak!")

win_streak = 0

while win_streak < 6:
    petal_info = petals.get_petals()
    print("Your roll is: " + " ".join(petal_info[1]))

    players_answer = input("How many petals are around the rose? ")

    if (players_answer == str(petal_info[0])):
        print("Correct!")
        win_streak += 1
    else:
        print(f"Wrong! There are {petal_info[0]} petals around the rose.")
        win_streak = 0

    print(f"Current win streak: {win_streak}")

print("Congratulations! You are now a member of the Fraternity of Petals Around the Rose!")