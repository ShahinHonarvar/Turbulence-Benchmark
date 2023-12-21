
def insert_after_character(string):
    return "".join([c + "I" if c == "Q" else c for c in string])
