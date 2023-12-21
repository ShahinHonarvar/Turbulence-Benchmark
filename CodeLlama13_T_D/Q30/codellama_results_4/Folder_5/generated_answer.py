
def insert_before_character(string, character):
    return ''.join([f'G{c}' if c == character else c for c in string])
