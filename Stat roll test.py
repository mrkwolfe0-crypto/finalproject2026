def roll():
    return random.randint(1,6)

def stat():
    dice_roll = []
    d1 = roll()
    dice_roll.append(d1)
    d2 = roll()
    dice_roll.append(d2)
    d3 = roll()
    dice_roll.append(d3)
    d4 = roll()
    dice_roll.append(d4)
    dice_roll.sort(reverse = True)
    total = sum(dice_roll[0:3])
    return total

def Player_stat():
    result = []
    Players_stats = ["Strength(STR)", "Dexterity(DEX)", "Constitution(CON)",
                     "Intelligence(INT)", "Wisdom(WIS)", "Charisma(CHA)"]
    for Player_stat in Players_stats:
        pstat = stat()
        result.append(f"{Player_stat}: {pstat}")
    return result
#Player_stat()