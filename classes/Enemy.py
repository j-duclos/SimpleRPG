from classes.Ability import Ability
import random
from classes.Character import Character


class Enemy(Character):
    # If you add any new messages here, they need to have n_or_no_n and enemy_name
    ENEMY_ENCOUNTER_MESSAGES = [
        "You see a{n_or_no_n} {enemy_name}!", "A{n_or_no_n} {enemy_name} has crossed your path!"
    ]

    def get_action(self, player):
        # Randomly select a special attack or regular attack
        special = random.choice([True, False])
        if special:
            attacks = []
            # Build a list of mob's available special attacks based on current mana
            for ability in self.abilities:
                if self.current_mana >= ability.mana_cost:
                    attacks += [ability]

            if len(attacks) == 0:
                return "Regular Attack"
            else:
                return random.choice(attacks)
        else:
            return "Regular Attack"

    def display_enemy_encounter_message(self):
        enemy_encounter_message = random.choice(Enemy.ENEMY_ENCOUNTER_MESSAGES)
        n_or_no_n = ""

        if self.name[0].lower() in ["a", "e", "i", "o", "u"]:
            n_or_no_n = "n"

        print(enemy_encounter_message.format(n_or_no_n=n_or_no_n, enemy_name=self.name))
        print()

    def take_turn(self, player):
        action = self.get_action(player)
        if isinstance(action, Ability):
            self.use_ability(action, player)
        elif action == "Regular Attack":
            self.use_regular_attack(player)
        else:
            print(self, "did nothing.")
        print()
