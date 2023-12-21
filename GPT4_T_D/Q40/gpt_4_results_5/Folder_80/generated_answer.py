
def return_n_smallest_chars(character_string):
    if len(character_string) < 35:
        return "Input string must have at least 35 distinct characters."
    sorted_string = sorted(character_string)
    return sorted_string[:35]
