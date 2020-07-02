from classes.enemy import enemy
import numpy.random as rd

class BasicGoblin(enemy.Enemy):
    '''
    Your basic goblin. Very weak in mind and physique, but strong in
    body odor.
    '''
    def __init__(self, name=None, MAX_HP=1, MAX_STAM=1):
        self.id = 'Basic Goblin'

        super().__init__(name, MAX_HP, MAX_STAM)

    def _setup_HP(self, HP):
        return HP

    def _setup_STAM(self, STAM):
        return STAM

    def get_battle_action(self):
        '''
        Always attacking, that loveable bastard.
        '''
        return 0


class TankGoblin(enemy.Enemy):
    '''
    The tanky one. A bit thick, but also thicccc.
    '''
    def __init__(self, name=None, MAX_HP=2, MAX_STAM=1):
        self.id = 'Tank Goblin'

        super().__init__(name, MAX_HP, MAX_STAM)

    def get_battle_action(self):
        '''
        80% defend
        20% attack
        '''
        rand = rd.randint(0, 100)
        if rand <= 80:
            return 1
        else:
            return 0

    def _setup_HP(self, HP):
        return HP

    def _setup_STAM(self, STAM):
        return STAM
