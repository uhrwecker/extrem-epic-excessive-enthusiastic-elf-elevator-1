'''
Introducing: the enemy.
It is ... not your friend, I guess.
'''


class Enemy():
    '''
    Enemy (short: NME)
    base class for future enemies which will be clubbed to death for entertainment.
    Maybe they should scream a bit?
    '''
    def __init__(self, name, MAX_HP, MAX_STAM):
        self.name = name
        self.MAX_HP = self._setup_HP(MAX_HP)
        self.MAX_STAM = self._setup_STAM(MAX_STAM)

        self.HP = self.MAX_HP
        self.STAM = self.MAX_STAM
        

    def _setup_HP(self, HP):
        '''
        Change this if you want to randomly adjust random
        the HP of the enemy (like, every enemy has a 10%
        to have one more max_HP
        '''
        raise NotImplementedError('You thought you could get away with this?!')


    def _setup_STAM(self, STAM):
        '''
        Change this if you want to randomly adjust random
        the STAM of the enemy (like, every enemy has a 15%
        to have one more MAX_STAM
        '''
        raise NotImplementedError('I will find you. No!')


    def get_battle_action(self):
        '''
        Get the battle action.
        0: attack
        1: defend
        '''
        raise NotImplementedError()
    

    def get_HP(self):
        return self.HP
    
    def get_STAM(self):
        return self.STAM
    

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
        return "Name: {}, Type: {}, \n\t HP: {}, STAM: {}".format(self.name,
                                                             self.id,
                                                             self.HP,
                                                             self.STAM)



