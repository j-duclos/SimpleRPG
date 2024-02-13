from classes.Ability import Ability
from classes.Enemy import Enemy


class Dragon(Enemy):
    name = "Elemental Dragon"
    strength = 100
    defense = 0.5
    max_mana = 50
    max_health = 150

    def __init__(self, action_log):
        super(Dragon, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Arcane Inferno Vortex", 15, 10, 0),
            Ability(self.action_log, "Abyssal Frostbreath", 5, 5, 0),
            Ability(self.action_log, "Meteor Tail Smash", 0, 3, 10)
        ]


class Goblin(Enemy):
    name = "Goblin Engineer"
    strength = 20
    defense = 0.1
    max_mana = 15
    max_health = 25

    def __init__(self, action_log):
        super(Goblin, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Goblinfire Bombard", 15, 5, 0),
            Ability(self.action_log, "Sneak stab Surprise", 5, 2, 0),
            Ability(self.action_log, "Tinkertrap Mayham", 0, 5, 10)
        ]


class Orc(Enemy):
    name = "Raging Orc"
    strength = 75
    defense = 0.3
    max_mana = 25
    max_health = 100

    def __init__(self, action_log):
        super(Orc, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Bloodfury Berserk", 15, 10, 0),
            Ability(self.action_log, "Gorehowl Charge", 5, 2, 0),
            Ability(self.action_log, "Skullcrusher Rampage", 0, 5, 10)
        ]


class Skeleton(Enemy):
    name = "Skeleton Warrior"
    strength = 15
    defense = 0.1
    max_mana = 15
    max_health = 20

    def __init__(self, action_log):
        super(Skeleton, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Bone Shatter Barrage", 15, 10, 0),
            Ability(self.action_log, "Skullcracker Volley", 5, 5, 0),
            Ability(self.action_log, "Necrotic Grasp of the Grave", 5, 10, 10)
        ]


class Troll(Enemy):
    name = "Troll Shaman"
    strength = 22
    defense = 0.3
    max_mana = 35
    max_health = 30

    def __init__(self, action_log):
        super(Troll, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Grimstone Earthquake", 10, 10, 10),
            Ability(self.action_log, "Thornroot Entanglement", 5, 2, 5),
            Ability(self.action_log, "Echoing Roar Shockwave", 5, 5, 5)
        ]


class Zombie(Enemy):
    name = "Rotting Zombie"
    strength = 20
    defense = 0.2
    max_mana = 10
    max_health = 18

    def __init__(self, action_log):
        super(Zombie, self).__init__(
            action_log,
            self.name,
            self.strength,
            self.defense,
            self.max_mana,
            self.max_health,
        )

        self.abilities += [
            Ability(self.action_log, "Necrotic Swarm Assault", 10, 10, 0),
            Ability(self.action_log, "Plaguebearer's Siege", 5, 5, 0),
            Ability(self.action_log, "Rotting Rapture Rampage", 15, 15, 10)
        ]