
def return_n_smallest_chars(character_string):
    sorted_characters = sorted(character_string, key=lambda x: ord(x))
    return sorted_characters[:72][::-1]
