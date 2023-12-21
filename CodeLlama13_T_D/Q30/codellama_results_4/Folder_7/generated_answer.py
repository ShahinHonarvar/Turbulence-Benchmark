
def insert_before_character(string, character):
    return "".join([f"{character}{c}" if c == ' ' else c for c in string])
