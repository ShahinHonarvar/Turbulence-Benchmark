
def filter_chars(string):
    characters_to_remove = set(string[52:82])
    filtered_string = ''.join(char for char in string if char not in characters_to_remove)
    return filtered_string
