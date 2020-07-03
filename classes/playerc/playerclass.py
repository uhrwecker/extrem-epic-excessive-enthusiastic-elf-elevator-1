"""Playerclass"""
from classes.race import *
from classes.alignment import *

class Player():
 
    def __init__(self, name, race, alignment):
        """Sorts the arguments to variables
        Arg: 
            race: race chosen by the player
            alignment: alignment chosen by the player"""
        self.name = name
        self.race = self._setup_race(race)
        self.alignment = self._setup_alignment(alignment)
        
        self.HP, self.STAM = self.setup_stats()
        self.MAX_HP = self.HP
        self.MAX_STAM = self.STAM

    def _setup_alignment(self, align_id):
        if align_id == 'fighter':
            return Fighter()
        if align_id == 'mage':
            return Mage()

        else:
            raise ValueError('The alignment_id {} was not understood.'.format(align_id))


    def _setup_race(self, race_id):
        if race_id == 'orc':
            return Orc()
        if race_id == 'human':
            return Human()

        else:
            raise ValueError('The race_id {} was not understood.'.format(race_id))

    def setup_stats(self):
        """sets personal player stats at the start
        Arg:
            race: sets your ground stats
            alignment: gives you bonus stats
        Out:
            HP: hitpoints
            STAM: stamina"""

        BASE_HP = self.race.get_HP()
        BASE_STAM = self.race.get_STAM()

        HP, STAM = self.alignment.adjust_stats(BASE_HP, BASE_STAM)
        
        return HP, STAM

    def change_max_stat(self, stat_name, val):
        '''
        Change the maximum stat/HP by e.g. equipping an item
        '''
        raise NotImplementedError()
    
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
        return """{}:\n Race: {}, Alignment: {}
    HP: {}, STAM: {}""".format(self.name, self.race, self.alignment, self.HP, self.STAM)
