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
  
