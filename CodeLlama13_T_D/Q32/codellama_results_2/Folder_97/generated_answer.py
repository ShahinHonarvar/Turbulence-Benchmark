
def insert_after_character(string):
    return "".join([c + "h" if c == "o" else c for c in string])
