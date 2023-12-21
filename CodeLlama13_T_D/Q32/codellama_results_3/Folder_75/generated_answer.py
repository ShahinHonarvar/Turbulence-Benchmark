
def insert_after_character(string):
    return "".join([c + ("q" if c == "U" else "") for c in string])
