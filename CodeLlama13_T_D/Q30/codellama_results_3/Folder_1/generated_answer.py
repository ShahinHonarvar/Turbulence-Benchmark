
def insert_before_character(string, character):
    return "".join([char if char != "U" else f"T{char}" for char in string])
