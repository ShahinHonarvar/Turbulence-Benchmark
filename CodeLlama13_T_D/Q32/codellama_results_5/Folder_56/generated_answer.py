
def insert_after_character(string):
    return "".join([c + "i" if c == "I" else c for c in string])
