from classes.Ability import Ability
from classes.Character import Character
import random
from classes.Enemy import Enemy


class Player(Character):
    AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT = 0.05
    AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT = 1
    AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT = 10

    strength = 10
    defense = 0.25
    max_mana = 25
    max_health = 100

    def __init__(self, action_log, name):
        super(Player, self).__init__(action_log, name, self.strength, self.defense, self.max_mana, self.max_health)

        self.abilities += [
            Ability(self.action_log, "Celestrial Comet Strike", 50, 5, 0),
            Ability(self.action_log, "Quantum Warp Blast", 60, 7, 0),
            Ability(self.action_log, "Infernal Phoenix Rebirth", 0, 5, 25)
        ]

    def rest(self):
        self.current_mana += 3
        self.current_health += 30

        if self.current_mana > self.max_mana:
            self.current_mana = self.max_mana

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    def level_up(self):
        print("You have leveled up!")
        print("You have 3 actions you can take:")
        print("    s = Increase strength by", self.AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT)
        print("    d = Increase defense by", self.AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT)
        print("    m = Increase max mana by", self.AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT)
        print("    h = Increase max health by", self.AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT)

        choices_are_valid = False

        while not choices_are_valid:
            choices_are_valid = True

            choices = input("Enter your 3 choices separated by spaces: ")

            # Create a list of choices
            choice_list = choices.strip().split(" ")
            
            # Validate only valid choices are used
            valid_choices = [c.lower() for c in choice_list if c.lower() in 'sdmh']

            # Validate 3 choices are entered; could have used choice_list[:3] to select first 3.
            if len(valid_choices) > 3 or len(valid_choices) < 3:
                print("You have chosen an incorrect amount of actions! \n")
                self.level_up()
            else:
                for choice in valid_choices:
                    if choice == 's':
                        self.strength += self.AMOUNT_TO_INCREASE_STRENGTH_PER_LEVEL_UP_POINT
                    elif choice == 'd':
                        self.defense += self.AMOUNT_TO_INCREASE_DEFENSE_PER_LEVEL_UP_POINT
                    elif choice == 'm':
                        self.max_mana += self.AMOUNT_TO_INCREASE_MAX_MANA_PER_LEVEL_UP_POINT
                    elif choice == 'h':
                        self.max_health += self.AMOUNT_TO_INCREASE_MAX_HEALTH_PER_LEVEL_UP_POINT
        print()

    # Added def to check mana of each ability and loops back if not enough mana
    def check_mana(self, ability, enemy):
        if self.current_mana >= self.abilities[ability].mana_cost:
            self.use_ability(self.abilities[ability], enemy)
        else:
            print("You did nothing. You need more mana!")
            self.take_turn(enemy)

    def take_turn(self, enemy):
        is_invalid_input = True

        while is_invalid_input:
            is_invalid_input = False

            print("r = Regular Attack (0 Mana Used)")
            print("s = Special Ability")
            action = input("Choose an action: ")

            print()

            if action == "r":
                self.use_regular_attack(enemy)
            elif action == "s":
                # Added another ability
                print(f"1 = {self.abilities[0].name} for {self.abilities[0].mana_cost} mana.")
                print(f"2 = {self.abilities[1].name} for {self.abilities[1].mana_cost} mana.")
                print(f"3 = {self.abilities[2].name} for {self.abilities[2].mana_cost} mana.")
                choice = input("Choose an ability: ")

                if choice == '1':
                    self.check_mana(0, enemy)
                elif choice == '2':
                    self.check_mana(1, enemy)
                elif choice == '3':
                    self.check_mana(2, enemy)

            else:
                is_invalid_input = True
