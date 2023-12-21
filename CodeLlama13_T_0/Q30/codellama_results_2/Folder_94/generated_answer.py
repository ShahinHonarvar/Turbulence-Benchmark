
def insert_before_character(string, char):
    return "".join([char if c == ' ' else c for c in string])
