
def insert_after_character(string):
    return "".join([c + "0" if c == "o" else c for c in string])
