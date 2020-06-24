"""Playerclass"""


class player():
 
    def __init__(self, race, alignment):
        """Sorts the arguments to variables
        Arg: 
            race: race chosen by the player
            alignment: alignment chosen by the player"""
        self.race = race
        self.alignment = alignment
        
        self.HP, self.STAM = self.setup_stats(race, alignment)

    def setup_stats(self, race, alignment):
        """sets personal player stats at the start
        Arg:
            race: sets your ground stats
            alignment: gives you bonus stats
        Out:
            HP: hitpoints
            STAM: stamina"""
        if race == 'human':
            HP = 1
            STAM = 2
        
        if race == 'orc':
            HP = 2
            STAM = 1
        
        if alignment == 'fighter':
            HP += 1
        
        if alignment == 'mage':
            STAM += 1
        
        return HP, STAM
    
    def change_stat(self, stat_name, val):
        """tool to change the temporarily stats of a player
        Arg:
            stat_name: name of the stat to be changed
            val: value of the change
        Out:
            new value of the stat thats been changed"""
        if stat_name == "HP":
            self.HP += val
            return self.HP
        if stat_name == "STAM":
            self.STAM += val
            return self.STAM
        
    def stat_display(self):
        """Displays the stats of a player
        returns a string that can be printed and holds the current stats of the player"""
        return """Race: {}, Alignment: {}
    HP: {}, STAM: {}""".format(self.race, self.alignment, self.HP, self.STAM)