
def insert_before_character(string):
    return "".join([char if char != "o" else f"o{char}" for char in string])
