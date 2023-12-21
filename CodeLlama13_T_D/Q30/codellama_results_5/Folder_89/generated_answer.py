
def insert_before_character(string, character):
    return "".join([c + ("W" if c == " " else "") for c in string])
