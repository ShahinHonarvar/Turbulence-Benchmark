
def insert_after_character(string):
    return "".join([c + "O" if c == 'O' else c for c in string])
