class Race():
    '''
    Interface for creating Race classes.
    Needs a method for setting up Base Stats.
    '''
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.HP, self.STAM = self._setup_stats()

    def _setup_stats(self):
        ''' Setup base stats for the race'''
        raise NotImplementedError()

    def get_HP(self):
        return self.HP

    def get_STAM(self):
        return self.STAM

    def set_HP(self):
        ''' YOU SHOULD NOT MESS WITH THE BASE STATS'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')

    def set_STAM(self):
        '''All your base are belong to us'''
        raise ValueError('Dont you try to set the base stats for the race, my friend!')

##########################################################
    
class Orc(Race):

    def __init__(self):
        super().__init__()

    def _setup_stats(self):
        HP = 2
        STAM = 1
        return HP, STAM
  
    def __repr__(self):
         return 'Orc'

###########################################################

class Human(Race):

    def __init__(self):
        super().__init__(verbose=False)

    def _setup_stats(self):
        HP = 1
        STAM = 2
        return HP, STAM

    def __repr__(self):
         return 'Human'
