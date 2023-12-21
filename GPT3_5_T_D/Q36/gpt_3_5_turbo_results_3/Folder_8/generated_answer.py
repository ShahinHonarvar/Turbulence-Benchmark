
def filter_chars(string):
    characters_to_remove = set(string[82:93])
    filtered_string = ''.join(c for c in string if c not in characters_to_remove)
    return filtered_string
