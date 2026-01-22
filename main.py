import petals

print("The name of the game is \"Petals Around the Rose\".")
print("The name of the game is significant. The answer is always zero or an even number.")
wins = 0
while wins < 6:
    rolls = petals.roll_dice(5)
    num_petals = petals.calculate_petals(rolls)
    dice = petals.get_dice_symbols(rolls)
    print("Your roll is: " + " ".join(dice))
    players_answer = input("How many petals are around the rose? ")
    if (players_answer == str(num_petals)):
        wins += 1
        print("Correct!")
    else:
        print(f"Wrong! There are {num_petals} petals around the rose.")
        wins = 0
print("Congratulations! You can now be sworn in as a member of the Fraternity of Petals Around the Rose!")