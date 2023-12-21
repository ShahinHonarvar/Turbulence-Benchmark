
def insert_before_character(string):
    return "".join([char if char != "W" else "W6" for char in string])
