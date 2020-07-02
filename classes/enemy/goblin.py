from classes.enemy import enemy

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


class TankGoblin(enemy.Enemy):
    '''
    The tanky one. A bit thick, but also thicccc.
    '''
    def __init__(self, name=None, MAX_HP=2, MAX_STAM=1):
        self.id = 'Tank Goblin'

        super().__init__(name, MAX_HP, MAX_STAM)

    def _setup_HP(self, HP):
        return HP

    def _setup_STAM(self, STAM):
        return STAM
