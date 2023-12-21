
def insert_after_character(string):
    return "".join([char if char != "F" else f"{char}4" for char in string])
