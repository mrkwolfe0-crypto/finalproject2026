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
    print(f"{stat_name}: {score:<5} Modifier: {mod}")

def Weapon():
    Weapon_types = {
        "Simple_melee" : {
            "Dagger": {"damage":"1D4", "type":"Piercing","stat":"DEX", "properties":["Finese","Light","Thrown(20/60)"]},
            "Clubs":{ },
            "Maces":{ }, 
            "Spears":{ },
            "Quarterstaffs":{ },
            },
        "Simple_range" : {
            "Light Crossbows":{ },
            "Shortbows":{ },
            "Darts":{ },
            "Slings":{ },
            },
        "Martial_melee" : {
            "Longswords":{ },
            "Greataxes":{ },
            "Rapiers":{ },
            "Halberds":{ },
            },
        "Martial_ranged" : {
            "Longbows":{ },
            "Heavy Crossbows":{ },
            "Hand Crossbows":{ },
            },
        }
    all_weapons = []
    for category, weapons in Weapon_types.items():
        print(f"\n{category}\n")
        for weapon_name, weapon_details in weapons.items():
            all_weapons.append(weapon_name)
            print(f"  - {weapon_name} ({weapon_details['damage']} {weapon_details['type']})")
            
    return all_weapons
def weapon_data():
    weapon_database = Weapon()
    
    return weapon_database


def Weapon_selection(weapon_database):
    while True:
        choice = input("\nChoose desired weapon: ").title()
        for category, weapons in weapon_database.items():
            if choice in weapons:
                return choice, weapons[choice]

weapon_name, weapon_stats= Weapon_selection(weapon_data())
stat_needed = weapon_stats["stat"]
stat_score = pstats.get(stat_needed)
modifier = get_modifier(stat_score)
print(f"To use your {weapon_name}, you use {stat_needed} (Score: {stat_score}), "
      f"giving you a modifier of: {modifier}")



"""def Weapon_selection():
    armory = Weapon()
    while True:
        choose_weapon = input("Choose desired weapon of choice: \n").title()
        if choose_weapon in armory:
            for category, weapon_list in armory.items():
                print(f"\n[{category}]")
        for weapon_name, weapon_details in weapon_list.items():
            print(f"  - {weapon_name} ({weapon_details['damage']} {weapon_details['type']})")
            return choose_weapon"""  


"""print(f"To use your {chosen_weapon_stats['damage']} {chosen_weapon_stats['type']} weapon, "
      f"you will use your {stat_needed} modifier: {modifier}")"""

"""weapon_database = weapon_data()
chosen_name, chosen_stats = Weapon_selection(weapon_database)
print(f"You equipped the {chosen_name}!")"""



