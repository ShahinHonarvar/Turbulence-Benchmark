
def insert_before_character(string):
    return "".join([char if char != "T" else "TE" for char in string])
