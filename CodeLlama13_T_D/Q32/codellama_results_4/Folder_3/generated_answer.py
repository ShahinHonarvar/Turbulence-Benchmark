
def insert_after_character(string):
    return "".join([c + "H" if c == '0' else c for c in string])
