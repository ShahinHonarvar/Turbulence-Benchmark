
def insert_before_character(string, character):
    return ''.join([f'{c}s' if c == character else c for c in string])
