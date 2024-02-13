import math
import random


class Character:
    def __init__(self, action_log, name, strength, defense, max_mana, max_health):
        self.action_log = action_log
        self.name = name
        self.strength = strength
        self.defense = defense
        self.max_mana = max_mana
        self.max_health = max_health
        self.abilities = []
        self.current_mana = max_mana
        self.current_health = max_health

    def __str__(self):
        return self.name

    @property
    def mana_ratio_string(self):
        return str(self.current_mana) + "/" + str(self.max_mana)

    @property
    def health_ratio_string(self):
        return str(self.current_health) + "/" + str(self.max_health)

    def use_regular_attack(self, defending_character):
        damage = self.strength * (1 - self.defense)      
        self.action_log.update_action_log(f"{self.name} hit {defending_character.name}.")
        defending_character.take_damage(damage)

    def take_damage(self, damage):
        rand =  random.randint(0, 5)
        if rand == 3:
            self.action_log.update_action_log(f"{self.name} blocked the attack and took 0 damage! \n")
        else:
            damage = math.floor(damage)
            # Prevents negative health from being displayed
            if (self.current_health - damage) < 0:
                self.current_health = 0
            else: 
                self.current_health -= damage
            self.action_log.update_action_log(f"{self.name} took {damage} damage! \n") 
    
    def take_heal(self, heal):
        rand =  random.randint(0, 5)
        if rand == 3:
            heal = (math.floor(heal))*2
            self.action_log.update_action_log(f"{self.name} critically healed for {heal} health! \n")
        else:
            heal = math.floor(heal)
            self.action_log.update_action_log(f"{self.name} healed for {heal} health! \n")
            
        # Prevents healing over max health
        if (self.current_health + heal) > self.max_health:
            self.current_health = self.max_health
        else: 
            self.current_health += heal
        
    def use_ability(self, ability, defending_character):
        damage = ability.damage * (1 - defending_character.defense)
        ability.cast(self, defending_character)
        if ability.heal == 0:
            self.action_log.update_action_log(
                f"\n{self.name} has performed {ability.name} against the {defending_character.name}."
            )
            defending_character.take_damage(damage)
        elif ability.heal > 0:
            self.action_log.update_action_log(
                f"\n{self.name} has performed {ability.name}."
            )
            self.take_heal(ability.heal)
