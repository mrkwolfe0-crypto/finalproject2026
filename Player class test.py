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