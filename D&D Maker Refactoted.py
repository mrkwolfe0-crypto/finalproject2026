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


pstats = Player_stat()
print(f"Stats generated: {pstats}")

print("\nAbility Modifiers")
for stat_name, score in pstats.items():
    mod = get_modifier(score)
    #print(f"{stat_name}: {score}  Modifier: {mod}")
    print(f"{stat_name}: {score:5d} Modifier: {mod}")


#Armor, Base AC for armor, Dex modifier, Cap
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
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer"]
    for player_class in classes:
        print(player_class)
    while True:
        player_class = input("Choose your class: \n").capitalize()
        if player_class in classes:
            print(f"You have chosen the path of the {player_class}")
            return player_class
        print("Class not found.")
#Player_class()

def Armor():
    Armor_types = {
        "No Armor" : ["No Armor"],
        "Light Armor" : ["Padded Armor", "Studded Leather"],
        "Medium Armor" : ["Hide", "Scale Mail", "Breastplate", "Half Plate"],
        "Heavy" : ["Ring Mail", "Chain Mail", "Splint"]
    }

    all_armor = []
    for category, category_list in Armor_types.items():
        print(f"\n{category}\n")
        for armor in category_list:
            all_armor.append(armor)
            print(armor)
    return all_armor


def Armor_selection():
    armor_armory = Armor()
    while True:
        choose_armor = input("Choose desired armor of choice: ").title()
        if choose_armor in armor_armory:
            return choose_armor


        choose_armor = input("Choose desired armor of choice: \n").title()
        if choose_armor in armor_armory:
            return choose_armor
            

parmor = Armor_selection()

stats = Armor_bonuses[parmor]
dex_mod = get_modifier(pstats["DEX"])

applicable_dex = min(dex_mod, stats["dex_mod"]) if stats["dex_mod"] is not None else dex_mod
pac = stats["base"] + applicable_dex

print(f"\nArmor Details ({parmor})")
print(f"Base AC: {stats['base']} | Dex Mod Applied: {applicable_dex} | Total AC: {pac}")

def Weapon():
    Weapon_types = {
        "Simple_melee" : {
            "Dagger": {"damage":"1D4", "type":"Piercing","stat":"DEX", "properties":["Finese","Light","Thrown(20/60)"]},
            "Clubs":{"damage":"1D4", "type":"Bludgeoning","stat":"STR", "properties":["Light","Two-Handed(1H)"] },
            "Maces":{"damage":"1D4", "type":"Bludgeoning","stat":"STR", "properties":["Light"] }, 
            "Spears":{"damage":"1D4", "type":"Piercing","stat":"STR", "properties":["Light","Versatile(1H/2H)","Thrown(20/60)"] },
            "Quarterstaffs":{"damage":"1D4", "type":"Bludgeoning","stat":"STR", "properties":["Versatile(1H/2H)"] },
            },
        "Simple_range" : {
            "Light Crossbows":{"damage":"1D8", "type":"Piercing","stat":"DEX", "properties":["Two-Handed(1H)"] }, 
            "Shortbows":{"damage":"1D6", "type":"Piercing","stat":"DEX", "properties":["Two-Handed(1H)","Thrown(80/320)"] },
            "Darts":{"damage":"1D4", "type":"Piercing","stat":"DEX", "properties":["Finese","Light","Thrown(20/60)"] },
            "Slings":{"damage":"1D4", "type":"Piercing","stat":"DEX", "properties":["Light","Thrown(30/120)"] },
            },
        "Martial_melee" : {
            "Longswords":{"damage":"1D8", "type":"Piercing/Bludgeoning","stat":"DEX", "properties":["Versatile(1H/2H)"] },
            "Greataxes":{"damage":"1D12", "type":"Slashing","stat":"STR", "properties":["Heavy","Two-Handed(1H)"] },
            "Rapiers":{"damage":"1D8", "type":"Piercing","stat":"DEX", "properties":["Finese","Light"] },
            "Halberds":{"damage":"1D10", "type":"Slashing","stat":"STR", "properties":["Heavy","Two-Handed(1H)"] },
            },
        "Martial_ranged" : {
            "Longbows":{"damage":"1D8", "type":"Peircing", "stat":"DEX", "properties":["Ammunition(150/600)", "Heavy", "Two-Handed"] },
            "Heavy Crossbows":{"damage":"1D10", "type":"Piercing", "stat":"DEX", "properties":["Ammunition(100/400)","Heavy","Two-Handed(1H)"] },
            "Hand Crossbows":{"damage":"1D6", "type":"Piercing", "stat":"DEX", "properties":["Ammunition(30/120)","Light","Loading","Two-Handed(1H)"] },
            },
        }
    all_weapons = []
    for category, weapons in Weapon_types.items():
        print(f"\n{category}\n")
        for weapon_name, weapon_details in weapons.items():
            all_weapons.append(weapon_name)
            print(f"  - {weapon_name} ({weapon_details['damage']} {weapon_details['type']})")
            
    return Weapon_types
def weapon_data():
    weapon_database = Weapon()
    return weapon_database

def Weapon_selection(weapon_database):
    while True:
        choice = input("\nChoose desired weapon: ").title()
        for category, weapons in weapon_database.items():
            if choice in weapons:
                return choice, weapons[choice]
"""
weapon_name, weapon_stats= Weapon_selection(weapon_data())
stat_needed = weapon_stats["stat"]
stat_score = pstats.get(stat_needed)
modifier = get_modifier(stat_score)
print(f"To use your {weapon_name}, you use {stat_needed} (Score: {stat_score}), "
      f"giving you a modifier of: {modifier}")
"""

#pstats = Player_stat()
def Character_Creation():
    pstats = Player_stat()
    print(f"\nStats: {pstats}")
    print("\nAbility Modifiers\n")
    for stat_name, score in pstats.items():
        mod = get_modifier(score)
        print(f"{stat_name:8}: {score:5d} Modifier: {mod:+2d}")
    parmor = Armor_selection()
    return pstats

a = parmor
w = Weapon_selection(weapon_data())
w_name = w[0]
w_stats = w[1]
c = Player_class()
name = input("enter name: \n")

#Apparantly that the "" creates a closed loop and '' will not meaning "this is"home""" excludes the "home" in the print. My original code used "" exclusively as that is how I set the weapons list and all the other but I kept on getting type miss matches.
print(f"\nCharacter Sheet\n"
      f"Name: {name} | Class: {c} | Weapon: {w_name}\n"
      f"Damage: {w_stats['damage']} | Type: {w_stats['type']}\n"
      f"Armor Details({parmor}):\n"
      f"Base AC: {stats['base']} | Dex Mod Applied: {applicable_dex} | Total AC: {pac}\n\n"
      f"Ability Scores:\n{pstats}\n")


