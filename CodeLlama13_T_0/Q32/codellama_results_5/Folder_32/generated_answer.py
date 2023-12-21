
def insert_after_character(string):
    return "".join([char if char != "u" else f"{char}F" for char in string])
