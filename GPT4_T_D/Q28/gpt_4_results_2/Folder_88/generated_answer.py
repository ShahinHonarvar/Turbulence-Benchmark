
def return_nth_smallest_ascii(character_string):
    subset = character_string[38:65]
    sorted_characters = sorted(subset, key=ord)
    return sorted_characters[13]
