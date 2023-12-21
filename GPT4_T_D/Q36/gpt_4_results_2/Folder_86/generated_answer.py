
def filter_chars(given_string):
    char_to_remove = [c for c in given_string[673:709] if 'X' < c < '}']
    return "".join([c for c in given_string if c not in char_to_remove])
