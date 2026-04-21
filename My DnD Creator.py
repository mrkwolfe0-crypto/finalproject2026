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

def Player_stat():
    result = {}
    Players_stats = ["STR", "DEX", "CON",
                     "INT", "WIS", "CHA"]
    for Player_stat in Players_stats:
        pstat = stat()
        key = Player_stat
        value = pstat
        result[key] = value
    return result

pstats = Player_stat()
print(pstats)

Armor_bonuses = {
    #Armor, Base AC for armor, Dex modifier, Cap
    "No Armor" : {"base": 10, "dex_mod": None},
    "Padded Armor": {"base": 11, "dex_mod": None}, 
    "Studded Leather": {"base":12, "dex_mod": None}, 
    "Hide" : {"base":14, "dex_mod":2}, 
    "Scale Mail" : {"base":14, "dex_mod":2}, 
    "Breastplate" : {"base":14, "dex_mod":2}, 
    "Half Plate" : {"base":15, "dex_mod":2}, 
    "Ring Mail" : {"base":14, "dex_mod":0}, 
    "Chain Mail" : {"base":18, "dex_mod":0}, 
    "Splint" : {"base":17, "dex_mod":0}
    }

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
    print(f"You have chosen the path of the {player_class}")    
#Player_class()

"""
Instead of rolling, you use a formula based on the type of armor you are wearing:
    No Armor: +10 dex modifier
    .
    Light Armor: base armor + dex modifier, use at end with an else
    (e.g., Leather is
    ).
    Medium Armor: base armor + dex modifier
    (up to a maximum of +2).
    Heavy Armor: A flat number that ignores your Dexterity (e.g., Plate is
    ).
    Shields: Add a flat +2 to your total AC
To determine your modifier in D&D 5e, you use a simple formula based on your base ability score (like Dexterity or Strength). 
The Formula

    Subtract 10 from your ability score.
    Divide the result by 2.
    Round down to the nearest whole number. 
"""

def Armor():
    Armor_types = { 
        "No Armor" : ["No Armor"],
        "Light Armor" : ["Padded Armor", "Studded Leather"],
        "Medium Armor" : ["Hide", "Scale Mail", "Breastplate", "Half Plate"],
        "Heavy" : ["Ring Mail", "Chain Mail", "Splint"]
    }
    all_armor = []
    for category_list in Armor_types.values():
        for armor in category_list:
            all_armor.append(armor)
            print(armor)
    return all_armor
#all_armor = Armor()
all_armor = Armor()

def Armor():
    Armor_types = { 
        "No Armor" : ["No Armor"],
        "Light Armor" : ["Padded Armor", "Studded Leather"],
        "Medium Armor" : ["Hide", "Scale Mail", "Breastplate", "Half Plate"],
        "Heavy" : ["Ring Mail", "Chain Mail", "Splint"]
    }
    all_armor = []
    for category_list in Armor_types.values():
        for armor in category_list:
            all_armor.append(armor)
            #print(armor)
    return all_armor
#all_armor = Armor()

def Armor_selection():
    armor_armory = Armor()
    while True:
        choose_armor = input("Choose desired armor of choice: ").title()
        if choose_armor in armor_armory:
            return choose_armor
parmor = Armor_selection()


def AC():
    stats = Armor_bonuses[parmor]
    base = stats["base"]
    cap = stats["dex_mod"]
    dex_val = (pstats["DEX"] - 10)//2
    dex_mod = ("DEX modifier", dex_val)
    if cap is None:
        applicable_dex = dex_val
    elif cap == 0:
        applicable_dex = 0
    else:
        applicable_dex = min(dex_val, cap)
    pac = base + applicable_dex
    #print(stats)
    print("Base AC", base, 
        "Dex Modifier", dex_mod,
        "Modified AC", pac)

def Weapon():
    Weapon_types = {
        "Simple_melee" : ["Dagger", "Clubs", "Maces", "Spears", "Quarterstaffs"],
        "Simple_range" : ["Light Crossbows", "Shortbows", "Darts", "Slings"],
        "Martial_melee" : ["Longswords", "Greataxes", "Rapiers", "Halberds"],
        "Martial_ranged" : ["Longbows", "Heavy Crossbows", "Hand Crossbows"],
    }
    """Find a way to insert the weapon damage, type of damage and the primary stat for the weapon."""
    
    for category_list in Weapon_types.values():
        for weapon in category_list:
            print(weapon)
            
    all_weapons = []
    for category_list in Weapon_types.values(): 
        for weapon in category_list:
            all_weapons.append(weapon)
            #print(all_weapons)
    return all_weapons 

def Weapon_selection():
    armory = Weapon()
    while True:
         choose_weapon = input("Choose desired weapon of choice: ").title()
         if choose_weapon in armory:
             return choose_weapon
    
#pstats = Player_stat()
a = parmor

w = Weapon_selection()
c = Player_class()
name = input("enter name: ")


print(f"{name}, {c}, {w}")
print(f"Armor", {a})
AC()
print(pstats)
