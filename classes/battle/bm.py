#from classes.battle.policy import *

class BattleManager():
    def __init__(self, policy):
        #self.policy = self._setup_policy()

        self.turn = 1

    def start_battle(self, players, enemies):
        '''
        Here is where the real shit starts
        '''
        battle_flag = True
        print('##########################')

        print('And the battle starts!')
        print('Turn {}:'.format(self.turn))
        print('-')
        while battle_flag:
            player_actions = self._get_actions_from_players(players)
            enemy_actions = self._get_enemy_actions(enemies)

            for player, action in zip(players, player_actions):
                self.execute_defend(player, action)

            for enemy, action in zip(enemies, enemy_actions):
                self.execute_defend(enemy, action)

            # here normally stands a policy regarding the order of execution
            for player, action in zip(players, player_actions):
                target = 0 #FIXME: this needs to be chosen
                self.execute_attack(player, action, enemies, target)

            for enemy, action in zip(enemies, enemy_actions):
                target = 0
                self.execute_attack(enemy, action, players, target)

            for player, action in zip(players, player_actions):
                player = self.reset_defend(player, action)

            for enemy, action in zip(enemies, enemy_actions):
                enemy = self.reset_defend(enemy, action)

            
            for enemy in enemies:
                print(enemy.stat_display())
            for player in players:
                print(player.stat_display())

            battle_flag = False

        return players, enemies

    def execute_defend(self, active, action):
        if action == 1:
            msg = '{} is defending!'.format(active.name)
            print(msg)
            active.change_stat('STAM', 1)

        return active
        
        
    def execute_attack(self, active, action, passives, target):
        ahp, astam = active.get_HP(), active.get_STAM()
        php, pstam = passives[target].get_HP(), passives[target].get_STAM()
        if action == 0:
            dmg = astam - pstam
            if dmg < 0:
                dmg = 0
            msg = '{} is attacking {} for {} damage!'.format(active.name, passives[target].name,
                                                             dmg)
            print(msg)
            passives[target].change_stat('HP', -dmg)

    def reset_defend(self, active, action):
        if action == 1:
            active.change_stat('STAM', -1)

        return active
        

    def _get_enemy_actions(self, enemies):
        actions = []
        for nme in enemies:
            action = nme.get_battle_action()
            if action == 1:
                # increase STAM by one if defending
                nme.change_stat('STAM', 1)
            actions.append(action)

        return actions

    def _get_actions_from_players(self, players):
        actions = []
        for player in players:
            action = input('Player {}, choose an action!\n>att< or >def<\n'.format(player.name))

            if action == 'att':
                print('-- attacking ...')
                actions.append(0)
            elif action == 'def':
                print('-- definding ...')
                player.change_stat('STAM', 1)
                actions.append(1)

            else:
                print('Action not understood, chose from >att< or >def<!')
                print('Will default to attacking ...')
                actions.append(0)

        return actions
