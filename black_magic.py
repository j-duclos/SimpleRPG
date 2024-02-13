def get_player_and_enemy_info_box_lines(player, enemy):
    player_line_dictionary = get_character_line_dictionary(player)
    enemy_line_dictionary = get_character_line_dictionary(enemy, end_symbol="*")

    info_box_size = player_line_dictionary["longest_line_length"] + enemy_line_dictionary["longest_line_length"]

    border_line = "*" * info_box_size
    name_line = player_line_dictionary["name_line"] + enemy_line_dictionary["name_line"]
    mana_line = player_line_dictionary["mana_line"] + enemy_line_dictionary["mana_line"]
    health_line = player_line_dictionary["health_line"] + enemy_line_dictionary["health_line"]

    lines = [border_line, name_line, mana_line, health_line, border_line]

    return lines


def get_character_line_dictionary(character, end_symbol=""):
    name_line = f"* {character.name} "
    mana_line = f"* mana: {character.mana_ratio_string} "
    health_line = f"* health: {character.health_ratio_string} "

    lines = [name_line, mana_line, health_line]
    longest_line_length = len(max(lines, key=len))

    name_line = name_line.ljust(longest_line_length) + end_symbol
    mana_line = mana_line.ljust(longest_line_length) + end_symbol
    health_line = health_line.ljust(longest_line_length) + end_symbol

    longest_line_length += len(end_symbol)

    character_line_dictionary = {
        "longest_line_length": longest_line_length,
        "name_line": name_line,
        "mana_line": mana_line,
        "health_line": health_line,
    }

    return character_line_dictionary
