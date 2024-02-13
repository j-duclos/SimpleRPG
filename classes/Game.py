from random import choice
from black_magic import get_player_and_enemy_info_box_lines
from classes.ActionLog import ActionLog
from classes.Mobs import *
from classes.Player import Player


class Game:
    class PlayerDiedException(Exception):
        """ Exception raised when player dies """
        pass

    def __init__(self, number_of_enemies_to_kill=5):
        self.number_of_enemies_to_kill = number_of_enemies_to_kill

        self.action_log = ActionLog()

        player_name = input("Player Name: ").strip()
        self.player = Player(self.action_log, player_name)

        self.enemies = [
            Dragon,
            Goblin,
            Orc,
            Skeleton,
            Troll,
            Zombie,
        ]

        self.turn_order = [
            "Player",
            "Mob"
        ]

        self.current_enemy = None

    def run(self):
        try:
            for i in range(self.number_of_enemies_to_kill):
                self.fight()
        except self.PlayerDiedException as e:
            self.action_log.update_action_log(str(e))

        self.action_log.write_action_log_to_file()

    def fight(self):
        EnemyClass = self.get_random_enemy()
        self.current_enemy = EnemyClass(self.action_log)
        self.current_enemy.display_enemy_encounter_message()
        self.display_player_and_enemy_info()
        
        while self.current_enemy.current_health > 0 and self.player.current_health > 0:
            turn = choice(self.turn_order)
            if turn == "Player":
                self.player.take_turn(self.current_enemy)
                if self.current_enemy.current_health > 0:
                    self.current_enemy.take_turn(self.player)
                else:
                    self.action_log.update_action_log(
                    f"{self.player.name} has killed {self.current_enemy.name}."
                )
            elif turn == "Mob":
                self.current_enemy.take_turn(self.player)
                self.player.take_turn(self.current_enemy)

            self.display_player_and_enemy_info()

        if self.player.current_health <= 0:
            raise self.PlayerDiedException("You have died!")

        self.player.level_up()
        self.player.rest()

    def get_random_enemy(self):
        return choice(self.enemies)

    def display_player_and_enemy_info(self):
        for line in get_player_and_enemy_info_box_lines(self.player, self.current_enemy):
            print(line)

        print()
