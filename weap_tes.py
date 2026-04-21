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
Weapon()

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
Weapon_selection()
