class Alignment():
    '''
    Interface for creating an Alignment.
    Needs a method for adjusting the Base stats.
    '''
    def __init__(self, verbose=False):
        self.verbose = verbose

    def adjust_stats(self, HP, STAM):
        '''
        Adjust the HP and STAM (stats) that you can get from
        the race instance (via .get_HP and .get_STAM)
        '''
        HP = self._adjust_HP(HP)
        STAM = self._adjust_STAM(STAM)
        return HP, STAM

    def _adjust_HP(self, HP):
        ''' Adjust the HP for the given alignment '''
        raise NotImplementedError()

    def _adjust_STAM(self, STAM):
        ''' Adjust the STAM for the given alignment '''
        raise NotImplementedError()

    def __repr__(self):
        raise NotImplementedError()

####################################

class Fighter(Alignment):
    ''' Fighter Alignment class '''
    def __init__(self):
        super().__init__(False)

    def _adjust_HP(self, HP):
        return HP + 1

    def _adjust_STAM(self, STAM):
        return STAM
 
    def __repr__(self):
        return 'Fighter'

#####################################

class Mage(Alignment):
    ''' Mage Alignment class '''
    def __init__(self):
        super().__init__(False)

    def _adjust_HP(self, HP):
        return HP

    def _adjust_STAM(self, STAM):
        return STAM + 1

    def __repr__(self):
        return 'Mage'



