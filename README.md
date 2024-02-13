# Text Based RPG Solo Game

## Game Information

The project presented here is a simple text-based turn-based RPG. In the game,
you will battle different enemies. Characters possess values relating to health, strength,
defense, and more. Every time you defeat an enemy, you will level up.

## Game Attributes

- strength: This value represents the amount of base damage your regular attack
  inflicts
- defense: This is a decimal value that represents what percent of damage will be
  blocked
    - If the attack is 10 damage and your defense is 0.1, then you will take 9
      damage
    - If the attack is 10 and your defense is 0.25, then you will take 8 damage,
      as it will round up. This defense protects against regular attacks as well
      as abilities
- max_mana: Your max mana. This can be affected by stat changes
- max_health: Your max health. This can be affected by stat changes

## Added/Changed Features

- Added the ability for Player and Enemies to cast a heal ability
- Allowed Player and enemies the chance to critically heal (Could add Crit chance modifier)
- Changed the order of who attacks based on a random choice
- Changed the attack loop; if enemy is killed by attack then enemy cannot attack back
- Allowed Player and enemies the randomly block attacks

## Future Enhancements

- Create React UI to visualize mobs.

## Usage

- Run main.py.  
- python3 main.py