
def insert_after_character(string, character):
    return "".join([char if char != character else f"{char}I" for char in string])
