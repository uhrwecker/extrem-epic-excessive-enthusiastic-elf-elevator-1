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
    def __init__(self, MAX_HP, MAX_STAM):
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
    

    def get_HP(self):
        return self.HP
    
    def get_STAM(self):
        return self.STAM
    

    def set_HP(self, val):
        self.HP = val

    def set_STAM(self, val):
        self.STAM = val


    def __repr__(self):
        return "Type: {}, HP: {}, STAM: {}".format(self.id, HP, STAM)



