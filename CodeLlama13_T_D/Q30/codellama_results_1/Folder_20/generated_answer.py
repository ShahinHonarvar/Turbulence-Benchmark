
def insert_before_character(string):
    return "".join([char if char != "H" else "HC" for char in string])
