
def insert_after_character(string, char):
    return "".join([char if c == 'x' else c for c in string]) + char
