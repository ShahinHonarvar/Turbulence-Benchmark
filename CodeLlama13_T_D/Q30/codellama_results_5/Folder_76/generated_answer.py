
def insert_before_character(string):
    return ''.join([f'm{c}' if c == 'F' else c for c in string])
