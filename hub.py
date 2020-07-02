from classes.playerc import playerclass as pc
from classes.enemy import goblin as gb

player_1 = pc.Player('human', 'mage')
player_2 = pc.Player('orc', 'fighter')

goblinsky = gb.BasicGoblin('Gertrud')

player_1.change_stat("HP", 1)

print(player_1.HP)

print("Player 1:","\n", player_1.stat_display())
print("Player 2:","\n", player_2.stat_display())
print('Enemy 1: ', '\n', goblinsky.stat_display())
