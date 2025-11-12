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

def get_petals(num_dice = 5):
    dice_values = roll_dice(num_dice)
    num_petals = calculate_petals(dice_values)
    dice_symbols = get_dice_symbols(dice_values)
    return num_petals, dice_symbols
