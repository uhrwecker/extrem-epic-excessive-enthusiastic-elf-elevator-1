from classes.playerc import playerclass as pc

player_1 = pc.Player('human', 'mage')
player_2 = pc.Player('orc', 'fighter')

player_1.change_stat("HP", 1)

print(player_1.HP)

print("Player 1:","\n", player_1.stat_display())
print("Player 2:","\n", player_2.stat_display())