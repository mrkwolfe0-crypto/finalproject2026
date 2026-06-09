import random
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
    result = {}
    Players_stats = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
    for Player_stat in Players_stats:
        pstat = stat()
        key = Player_stat
        value = pstat
        result[key] = value
    return result

def get_modifier(Player_stat):
    return (Player_stat - 10) // 2
    
def Weapon():
    Weapon_types = {
        "Simple_melee" : ["Dagger", "Clubs", "Maces", "Spears", "Quarterstaffs"],
        "Simple_range" : ["Light Crossbows", "Shortbows", "Darts", "Slings"],
        "Martial_melee" : ["Longswords", "Greataxes", "Rapiers", "Halberds"],
        "Martial_ranged" : ["Longbows", "Heavy Crossbows", "Hand Crossbows"],
        }
    all_weapons = []
    for category, category_list in Weapon_types.items():
        print(f"\n{category}\n")
        # FIXED: This loop is now nested inside the category loop
        for weapon in category_list:
            all_weapons.append(weapon)
            print(weapon)
            
    return all_weapons
"""Find a way to insert the weapon damage, type of damage and the primary stat for the weapon."""

def Weapon_selection():
    armory = Weapon()
    while True:
        choose_weapon = input("Choose desired weapon of choice: \n").title()
        if choose_weapon in armory:
            return choose_weapon

def weapon_data():
  #Weapon {Damage Die, Damage Type, Primary Stat}
  
