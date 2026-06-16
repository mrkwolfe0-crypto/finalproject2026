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
    print(f"{stat_name}: {score:5d}  Modifier: {mod}")


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

"""def Player_class():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk",
               "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard",
               "Artificer"]
    for player_class in classes:
        print(player_class)
    while True:
        player_class = input("Choose your class: ").capitalize()
        if player_class in classes:
            print(f"You have chosen the path of the {player_class}")
            return player_class"""

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
    """all_armor = []
    for category, category_list in Armor_types.items():
        print(f"\n{category}\n") 
        for armor in category_list:
            all_armor.append(armor)
            print(armor)
    }"""
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
        "Simple_melee" : ["Dagger", "Clubs", "Maces", "Spears", "Quarterstaffs"],
        "Simple_range" : ["Light Crossbows", "Shortbows", "Darts", "Slings"],
        "Martial_melee" : ["Longswords", "Greataxes", "Rapiers", "Halberds"],
        "Martial_ranged" : ["Longbows", "Heavy Crossbows", "Hand Crossbows"],
    }
    """Find a way to insert the weapon damage, type of damage and the primary stat for the weapon."""

    all_weapons = []
    for category, category_list in Weapon_types.items():
        print(f"\n{category}\n")
        for weapon in category_list:
            all_weapons.append(weapon)
            print(weapon)
    return all_weapons 

    """all_weapons = []
    for category, category_list in Weapon_types.items():
        print(f"\n{category}\n")
        for weapon in category_list:
            all_weapons.append(weapon)
            print(weapon)
            
    return all_weapons"""
"""Find a way to insert the weapon damage, type of damage and the primary stat for the weapon."""

def Weapon_selection():
    armory = Weapon()
    while True:

        choose_weapon = input("Choose desired weapon of choice: ").title()
        if choose_weapon in armory:
            return choose_weapon
    

        choose_weapon = input("Choose desired weapon of choice: \n").title()
        if choose_weapon in armory:
            return choose_weapon
#pstats = Player_stat()

a = parmor

w = Weapon_selection()
c = Player_class()
name = input("enter name: \n")


print(f"\n{name}, {c}, {w}")
print(f"\nArmor Details ({parmor})")
print(f"Base AC: {stats['base']} | Dex Mod Applied: {applicable_dex} | Total AC: {pac}")
print(pstats)

"""print(f"{name}, {c}, {w}")
print(f"\nArmor Details ({parmor})")
print(f"Base AC: {stats['base']} | Dex Mod Applied: {applicable_dex} | Total AC: {pac}")
print(pstats)"""
print(f"\nCHARACTER SUMMARY\n"
      f"Name: {name} | Class: {c} | Weapon: {w}\n"
      f"Armor Details ({parmor}):\n"
      f"Base AC: {stats['base']} | Dex Mod Applied: {applicable_dex} | Total AC: {pac}\n\n"
      f"Ability Scores:\n{pstats}")
"""
I will encounter an error as the class main stat will conflict with the weapons main stat, the highest wins, this will maintain the players agency to freely choose and be a battle mage or a warrior with magic.

stats_list = [pstats["STR"], pstats["DEX"], pstats["CON"]]
stats_list.sort(reverse=True)
best_stat = stats_list[0]
or
dex_score = pstats.get("DEX")
str_score = pstats.get("STR")
if dex_score > str_score:
    modifier = get_modifier(dex_score)
else:
    modifier = get_modifier(str_score)
"""

