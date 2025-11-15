import petals

print("The name of the game is \"Petals Around the Rose\".")
print("The name of the game is significant. The answer is always zero or an even number.")

petal_info = petals.get_petals()
print("Your roll is: " + " ".join(petal_info[1]))

players_answer = input("How many petals are around the rose? ")

if (players_answer == str(petal_info[0])):
    print("Correct!")
else:
    print(f"Wrong! There are {petal_info[0]} petals around the rose.")