
def insert_after_character(string):
    return "".join([c + "U" if c == "U" else c for c in string])
