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

def Armor_selection():
    armor_armory = Armor()
    armor_selected = False
    choose_armor = input("Choose desired armor of choice: ").title()
    while not armor_selected:
        if choose_armor in armor_armory:
            print(f"You have chosen the {choose_armor}")
            armor_selected = True
            return choose_armor
        else:
            print(f"{choose_armor} is not in the armory. Try again.")
            return
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
AC()
#print(dex_mod)


a = parmor
