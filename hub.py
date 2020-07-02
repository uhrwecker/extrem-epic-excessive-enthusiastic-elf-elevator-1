from classes.playerc import playerclass as pc
import start_setup as setup

players = setup.start_setup()

print("Player 1:","\n", players[0].stat_display())
print("Player 2:","\n", players[1].stat_display())