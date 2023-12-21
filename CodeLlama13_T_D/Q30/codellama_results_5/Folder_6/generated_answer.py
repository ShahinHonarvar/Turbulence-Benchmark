
def insert_before_character(string, character):
    return "".join([f"{character}u" if c == character else c for c in string])
