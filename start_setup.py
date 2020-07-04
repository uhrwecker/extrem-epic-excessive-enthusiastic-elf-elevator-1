"""Handels the player setup"""

from classes.playerc import playerclass as pc

def start_setup():
    
    intro()
    
    players = setup_player()
    
    return players
    

def intro():
    print("""Myths say this world was created by two almighty beings.
The people of this world call them LMNO and Piwo.
They may guide you on your adventures through the lands of ______.""")



def setup_player():
    
    player_quantity = int(input("How many players are you? "))
    
    players = []
    
    for i in range(1, player_quantity + 1):
              
        name = input("Player {} whats your name? ".format(i))
        name = name.capitalize()
        
        race = input("""Hello {}, what race do you want to be?
[human, orc] """.format(name))
        race = race.casefold()
        
        alignment = input("""And what will be your alignment?
[fighter, mage] """)
        alignment = alignment.casefold()
        
        p = pc.Player(name, race, alignment)
        players.append(p)
        
    return players