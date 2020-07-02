from classes.playerc import playerclass as pc
from classes.enemy import goblin as gb

from classes.battle import bm

player_1 = pc.Player('Piwo', 'human', 'mage')
player_2 = pc.Player('LMNO', 'orc', 'fighter')

players = [player_1, player_2]

goblinsky = gb.BasicGoblin('Hässlicher stinkender Doofkopf')

enemies = [goblinsky]

print("Player 1:","\n", players[0].stat_display())
print("Player 2:","\n", players[1].stat_display())
print('Enemy 1: ', '\n', enemies[0].stat_display())

batman = bm.BattleManager('')
players, enemies = batman.start_battle(players, [goblinsky])
