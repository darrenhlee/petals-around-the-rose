import random

def roll_dice(num_dice = 5):
    return [random.randint(1, 6) for die in range(num_dice)]

def get_dice_symbols(dice_array):
    for die in dice_array:
        match die:
            case 1:
                yield "⚀"
            case 2:
                yield "⚁"
            case 3:
                yield "⚂"
            case 4:
                yield "⚃"
            case 5:
                yield "⚄"
            case 6:
                yield "⚅"

def calculate_petals(dice_array):
    petals = 0

    for die in dice_array:
        if die % 2 == 0:
            petals += 0
        else:
            petals += die - 1

    return petals

print("The name of the game is \"Petals Around the Rose\".")
print("The name of the game is significant. The answer is always zero or an even number.")

dice = roll_dice()
petals = calculate_petals(dice)
print("Your roll is: " + " ".join(get_dice_symbols(dice)))

players_answer = input("How many petals are around the rose? ")

if (players_answer == str(petals)):
    print("Correct!")
else:
    print("Wrong! There are {petals} petals around the rose.")