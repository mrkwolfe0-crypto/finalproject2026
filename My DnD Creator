import random
dice_roll = []
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

def Player_class():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
           "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard",
           "Artificer"]
    for player_class in classes:
        print(player_class)
    while True:
        player_class = input("Choose your class: ").capitalize()
        if player_class in classes:
            return player_class
            break
        else:
            print({player_class}, "is not a valid class. Select again")
    print(f"You have chosen the path of the {player_class}")    
#Player_class()

def Player_stat():
    result = []
    Players_stats = ["Strength(STR)", "Dexterity(DEX)", "Constitution(CON)",
                     "Intelligence(INT)", "Wisdom(WIS)", "Charisma(CHA)"]
    for Player_stat in Players_stats:
        pstat = stat()
        result.append(f"{Player_stat}: {pstat}")
    return result
#Player_stat()

def Weapon():
    Weapon_types = {
        "Simple_melee" : ["Dagger", "Clubs", "Maces", "Spears", "Quarterstaffs"],
        "Simple_range" : ["Light Crossbows", "Shortbows", "Darts", "Slings"],
        "Martial_melee" : ["Longswords", "Greataxes", "Rapiers", "Halberds"],
        "Martial_ranged" : ["Longbows", "Heavy Crossbows", "Hand Crossbows"],
    }
    
    for category_list in Weapon_types.values():
        for weapon in category_list:
            print(weapon)
            
    all_weapons = []
    for category_list in Weapon_types.values(): 
        for weapon in category_list:
            all_weapons.append(weapon)
            
    return all_weapons 

def Weapon_selection():
    armory = Weapon()
    weapon_selected = False
    while not weapon_selected:
        choose_weapon = input("Choose desired weapon of choice: ").title().capitalize() 
        if choose_weapon in armory:
            print(f"You have chosen the {choose_weapon}")
            weapon_selected = True
            return choose_weapon
        else:
            print(f"{choose_weapon} is not in the armory. Try again.")
            return

pstats = Player_stat()
w = Weapon_selection()
c = Player_class()
name = input("enter name: ")


print(f"{name}, {c}, {w}")
print(*pstats, sep ="\n")

        




    
