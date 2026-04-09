pstats = Player_stat()
w = Weapon_selection()
c = Player_class()
name = input("enter name: ")


print(f"{name}, {c}, {w}")
print(*pstats, sep ="\n")