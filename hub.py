from classes.playerc import playerclass as pc
import start_setup as setup
from classes.enemy import goblin as gb

players = setup.start_setup()

goblinsky = gb.BasicGoblin('Gertrud')

print("Player 1:","\n", players[0].stat_display())
print("Player 2:","\n", players[1].stat_display())

print('Enemy 1: ', '\n', goblinsky.stat_display())