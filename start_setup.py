"""Handels the player setup"""

from classes.playerc import playerclass as pc
from testing import input_testing as inp

def start_setup():
    """Plays intro and calls the player set up
    returns a list with the player objects"""
    
    intro()
    
    players = setup_player()
    
    return players
    

def intro():
    print("""Myths say this world was created by two almighty beings.
The people of this world call them LMNO and Piwo.
They may guide you on your adventures through the lands of ______.""")



def setup_player():
    """sets up the players in the playerclass
    returns a list with player objects"""
    
    player_quantity = int(input("How many players are you? "))
    
    players = []
    
    for i in range(1, player_quantity + 1):
              
        name = input("Player {} whats your name? ".format(i))
        name = name.capitalize()
        test = inp.test_string(name, 'name')
        while test == False:
            name = input("Pls try again. ")
            name = name.capitalize()
            test = inp.test_string(name, 'name')
            
        
        race = input("""Hello {}, what race do you want to be?
[human, orc] """.format(name))
        race = race.casefold()
        test = inp.test_string(race, 'race')
        while test == False:
            race = input("Pls try again. [human, orc] ")
            race = race.casefold()
            test = inp.test_string(race, 'race')
        
        alignment = input("""And what will be your alignment?
[fighter, mage] """)
        alignment = alignment.casefold()
        test = inp.test_string(alignment, 'alignment')
        while test == False:
            alignment = input("Pls try again. [fighter, mage] ")
            alignment = alignment.casefold()
            test = inp.test_string(alignment, 'alignment')
        
        p = pc.Player(name, race, alignment)
        players.append(p)
        
    return players