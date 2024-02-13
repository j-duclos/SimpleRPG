class Ability:
    def __init__(self, action_log, name, damage, mana_cost, heal):
        self.action_log = action_log
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.heal = heal

    def cast(self, attacking_character, defending_character):
        attacking_character.current_mana -= self.mana_cost
